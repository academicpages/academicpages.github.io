# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
import asyncio
import datetime
import json
import os
from logging import Logger
from queue import Empty, Queue
from threading import Thread
from time import monotonic
from typing import Any, Dict, Optional

import websocket
from jupyter_client.asynchronous.client import AsyncKernelClient
from jupyter_client.clientabc import KernelClientABC
from jupyter_client.kernelspec import KernelSpecManager
from jupyter_client.manager import AsyncKernelManager
from jupyter_client.managerabc import KernelManagerABC
from tornado import web
from tornado.escape import json_decode, json_encode, url_escape, utf8
from traitlets import DottedObjectName, Instance, Type, default

from .._tz import UTC
from ..services.kernels.kernelmanager import AsyncMappingKernelManager
from ..services.sessions.sessionmanager import SessionManager
from ..utils import ensure_async, url_path_join
from .gateway_client import GatewayClient, gateway_request


class GatewayMappingKernelManager(AsyncMappingKernelManager):
    """Kernel manager that supports remote kernels hosted by Jupyter Kernel or Enterprise Gateway."""

    # We'll maintain our own set of kernel ids
    _kernels: Dict[str, "GatewayKernelManager"] = {}

    @default("kernel_manager_class")
    def _default_kernel_manager_class(self):
        return "jupyter_server.gateway.managers.GatewayKernelManager"

    @default("shared_context")
    def _default_shared_context(self):
        return False  # no need to share zmq contexts

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.kernels_url = url_path_join(
            GatewayClient.instance().url, GatewayClient.instance().kernels_endpoint
        )

    def remove_kernel(self, kernel_id):
        """Complete override since we want to be more tolerant of missing keys"""
        try:
            return self._kernels.pop(kernel_id)
        except KeyError:
            pass

    async def start_kernel(self, kernel_id=None, path=None, **kwargs):
        """Start a kernel for a session and return its kernel_id.

        Parameters
        ----------
        kernel_id : uuid
            The uuid to associate the new kernel with. If this
            is not None, this kernel will be persistent whenever it is
            requested.
        path : API path
            The API path (unicode, '/' delimited) for the cwd.
            Will be transformed to an OS path relative to root_dir.
        """
        self.log.info(f"Request start kernel: kernel_id={kernel_id}, path='{path}'")

        if kernel_id is None:
            if path is not None:
                kwargs["cwd"] = self.cwd_for_path(path)

        km = self.kernel_manager_factory(parent=self, log=self.log)
        await km.start_kernel(kernel_id=kernel_id, **kwargs)
        kernel_id = km.kernel_id
        self._kernels[kernel_id] = km

        # Initialize culling if not already
        if not self._initialized_culler:
            self.initialize_culler()

        return kernel_id

    async def kernel_model(self, kernel_id):
        """Return a dictionary of kernel information described in the
        JSON standard model.

        Parameters
        ----------
        kernel_id : uuid
            The uuid of the kernel.
        """
        model = None
        km = self.get_kernel(str(kernel_id))
        if km:
            model = km.kernel
        return model

    async def list_kernels(self, **kwargs):
        """Get a list of running kernels from the Gateway server.

        We'll use this opportunity to refresh the models in each of
        the kernels we're managing.
        """
        self.log.debug(f"Request list kernels: {self.kernels_url}")
        response = await gateway_request(self.kernels_url, method="GET")
        kernels = json_decode(response.body)
        # Refresh our models to those we know about, and filter
        # the return value with only our kernels.
        kernel_models = {}
        for model in kernels:
            kid = model["id"]
            if kid in self._kernels:
                await self._kernels[kid].refresh_model(model)
                kernel_models[kid] = model
        # Remove any of our kernels that may have been culled on the gateway server
        our_kernels = self._kernels.copy()
        culled_ids = []
        for kid, _ in our_kernels.items():
            if kid not in kernel_models:
                self.log.warning(
                    f"Kernel {kid} no longer active - probably culled on Gateway server."
                )
                self._kernels.pop(kid, None)
                culled_ids.append(kid)  # TODO: Figure out what do with these.
        return list(kernel_models.values())

    async def shutdown_kernel(self, kernel_id, now=False, restart=False):
        """Shutdown a kernel by its kernel uuid.

        Parameters
        ==========
        kernel_id : uuid
            The id of the kernel to shutdown.
        now : bool
            Shutdown the kernel immediately (True) or gracefully (False)
        restart : bool
            The purpose of this shutdown is to restart the kernel (True)
        """
        km = self.get_kernel(kernel_id)
        await km.shutdown_kernel(now=now, restart=restart)
        self.remove_kernel(kernel_id)

    async def restart_kernel(self, kernel_id, now=False, **kwargs):
        """Restart a kernel by its kernel uuid.

        Parameters
        ==========
        kernel_id : uuid
            The id of the kernel to restart.
        """
        km = self.get_kernel(kernel_id)
        await km.restart_kernel(now=now, **kwargs)

    async def interrupt_kernel(self, kernel_id, **kwargs):
        """Interrupt a kernel by its kernel uuid.

        Parameters
        ==========
        kernel_id : uuid
            The id of the kernel to interrupt.
        """
        km = self.get_kernel(kernel_id)
        await km.interrupt_kernel()

    async def shutdown_all(self, now=False):
        """Shutdown all kernels."""
        kids = list(self._kernels)
        for kernel_id in kids:
            km = self.get_kernel(kernel_id)
            await km.shutdown_kernel(now=now)
            self.remove_kernel(kernel_id)

    async def cull_kernels(self):
        """Override cull_kernels, so we can be sure their state is current."""
        await self.list_kernels()
        await super().cull_kernels()


class GatewayKernelSpecManager(KernelSpecManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        base_endpoint = url_path_join(
            GatewayClient.instance().url, GatewayClient.instance().kernelspecs_endpoint
        )

        self.base_endpoint = GatewayKernelSpecManager._get_endpoint_for_user_filter(base_endpoint)
        self.base_resource_endpoint = url_path_join(
            GatewayClient.instance().url,
            GatewayClient.instance().kernelspecs_resource_endpoint,
        )

    @staticmethod
    def _get_endpoint_for_user_filter(default_endpoint):
        kernel_user = os.environ.get("KERNEL_USERNAME")
        if kernel_user:
            return "?user=".join([default_endpoint, kernel_user])
        return default_endpoint

    def _replace_path_kernelspec_resources(self, kernel_specs):
        """Helper method that replaces any gateway base_url with the server's base_url
        This enables clients to properly route through jupyter_server to a gateway
        for kernel resources such as logo files
        """
        kernelspecs = kernel_specs["kernelspecs"]
        for kernel_name in kernelspecs:
            resources = kernelspecs[kernel_name]["resources"]
            for resource_name in resources:
                original_path = resources[resource_name]
                split_eg_base_url = str.rsplit(original_path, sep="/kernelspecs/", maxsplit=1)
                new_path = url_path_join(self.parent.base_url, "kernelspecs", split_eg_base_url[1])
                kernel_specs["kernelspecs"][kernel_name]["resources"][resource_name] = new_path
                if original_path != new_path:
                    self.log.debug(
                        f"Replaced original kernel resource path {original_path} with new "
                        f"path {kernel_specs['kernelspecs'][kernel_name]['resources'][resource_name]}"
                    )
        return kernel_specs

    def _get_kernelspecs_endpoint_url(self, kernel_name=None):
        """Builds a url for the kernels endpoint
        Parameters
        ----------
        kernel_name : kernel name (optional)
        """
        if kernel_name:
            return url_path_join(self.base_endpoint, url_escape(kernel_name))

        return self.base_endpoint

    async def get_all_specs(self):
        fetched_kspecs = await self.list_kernel_specs()

        # get the default kernel name and compare to that of this server.
        # If different log a warning and reset the default.  However, the
        # caller of this method will still return this server's value until
        # the next fetch of kernelspecs - at which time they'll match.
        km = self.parent.kernel_manager
        remote_default_kernel_name = fetched_kspecs.get("default")
        if remote_default_kernel_name != km.default_kernel_name:
            self.log.info(
                f"Default kernel name on Gateway server ({remote_default_kernel_name}) differs from "
                f"Notebook server ({km.default_kernel_name}).  Updating to Gateway server's value."
            )
            km.default_kernel_name = remote_default_kernel_name

        remote_kspecs = fetched_kspecs.get("kernelspecs")
        return remote_kspecs

    async def list_kernel_specs(self):
        """Get a list of kernel specs."""
        kernel_spec_url = self._get_kernelspecs_endpoint_url()
        self.log.debug(f"Request list kernel specs at: {kernel_spec_url}")
        response = await gateway_request(kernel_spec_url, method="GET")
        kernel_specs = json_decode(response.body)
        kernel_specs = self._replace_path_kernelspec_resources(kernel_specs)
        return kernel_specs

    async def get_kernel_spec(self, kernel_name, **kwargs):
        """Get kernel spec for kernel_name.

        Parameters
        ----------
        kernel_name : str
            The name of the kernel.
        """
        kernel_spec_url = self._get_kernelspecs_endpoint_url(kernel_name=str(kernel_name))
        self.log.debug(f"Request kernel spec at: {kernel_spec_url}")
        try:
            response = await gateway_request(kernel_spec_url, method="GET")
        except web.HTTPError as error:
            if error.status_code == 404:
                # Convert not found to KeyError since that's what the Notebook handler expects
                # message is not used, but might as well make it useful for troubleshooting
                raise KeyError(
                    "kernelspec {kernel_name} not found on Gateway server at: {gateway_url}".format(
                        kernel_name=kernel_name,
                        gateway_url=GatewayClient.instance().url,
                    )
                ) from error
            else:
                raise
        else:
            kernel_spec = json_decode(response.body)

        return kernel_spec

    async def get_kernel_spec_resource(self, kernel_name, path):
        """Get kernel spec for kernel_name.

        Parameters
        ----------
        kernel_name : str
            The name of the kernel.
        path : str
            The name of the desired resource
        """
        kernel_spec_resource_url = url_path_join(
            self.base_resource_endpoint, str(kernel_name), str(path)
        )
        self.log.debug(f"Request kernel spec resource '{path}' at: {kernel_spec_resource_url}")
        try:
            response = await gateway_request(kernel_spec_resource_url, method="GET")
        except web.HTTPError as error:
            if error.status_code == 404:
                kernel_spec_resource = None
            else:
                raise
        else:
            kernel_spec_resource = response.body
        return kernel_spec_resource


class GatewaySessionManager(SessionManager):
    kernel_manager = Instance("jupyter_server.gateway.managers.GatewayMappingKernelManager")

    async def kernel_culled(self, kernel_id):
        """Checks if the kernel is still considered alive and returns true if it's not found."""
        kernel = None
        try:
            km = self.kernel_manager.get_kernel(kernel_id)
            kernel = await km.refresh_model()
        except Exception:  # Let exceptions here reflect culled kernel
            pass
        return kernel is None


"""KernelManager class to manage a kernel running on a Gateway Server via the REST API"""


class GatewayKernelManager(AsyncKernelManager):
    """Manages a single kernel remotely via a Gateway Server."""

    kernel_id = None
    kernel = None

    @default("cache_ports")
    def _default_cache_ports(self):
        return False  # no need to cache ports here

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.kernels_url = url_path_join(
            GatewayClient.instance().url, GatewayClient.instance().kernels_endpoint
        )
        self.kernel_url: str
        self.kernel = self.kernel_id = None
        # simulate busy/activity markers:
        self.execution_state = self.last_activity = None

    @property
    def has_kernel(self):
        """Has a kernel been started that we are managing."""
        return self.kernel is not None

    client_class = DottedObjectName("jupyter_server.gateway.managers.GatewayKernelClient")
    client_factory = Type(klass="jupyter_server.gateway.managers.GatewayKernelClient")

    # --------------------------------------------------------------------------
    # create a Client connected to our Kernel
    # --------------------------------------------------------------------------

    def client(self, **kwargs):
        """Create a client configured to connect to our kernel"""
        kw = {}
        kw.update(self.get_connection_info(session=True))
        kw.update(
            dict(
                connection_file=self.connection_file,
                parent=self,
            )
        )
        kw["kernel_id"] = self.kernel_id

        # add kwargs last, for manual overrides
        kw.update(kwargs)
        return self.client_factory(**kw)

    async def refresh_model(self, model=None):
        """Refresh the kernel model.

        Parameters
        ----------
        model : dict
            The model from which to refresh the kernel.  If None, the kernel
            model is fetched from the Gateway server.
        """
        if model is None:
            self.log.debug("Request kernel at: %s" % self.kernel_url)
            try:
                response = await gateway_request(self.kernel_url, method="GET")

            except web.HTTPError as error:
                if error.status_code == 404:
                    self.log.warning("Kernel not found at: %s" % self.kernel_url)
                    model = None
                else:
                    raise
            else:
                model = json_decode(response.body)
            self.log.debug("Kernel retrieved: %s" % model)

        if model:  # Update activity markers
            self.last_activity = datetime.datetime.strptime(
                model["last_activity"], "%Y-%m-%dT%H:%M:%S.%fZ"
            ).replace(tzinfo=UTC)
            self.execution_state = model["execution_state"]
            if isinstance(self.parent, AsyncMappingKernelManager):
                # Update connections only if there's a mapping kernel manager parent for
                # this kernel manager.  The current kernel manager instance may not have
                # a parent instance if, say, a server extension is using another application
                # (e.g., papermill) that uses a KernelManager instance directly.
                self.parent._kernel_connections[self.kernel_id] = int(model["connections"])

        self.kernel = model
        return model

    # --------------------------------------------------------------------------
    # Kernel management
    # --------------------------------------------------------------------------

    async def start_kernel(self, **kwargs):
        """Starts a kernel via HTTP in an asynchronous manner.

        Parameters
        ----------
        `**kwargs` : optional
             keyword arguments that are passed down to build the kernel_cmd
             and launching the kernel (e.g. Popen kwargs).
        """
        kernel_id = kwargs.get("kernel_id")

        if kernel_id is None:
            kernel_name = kwargs.get("kernel_name", "python3")
            self.log.debug("Request new kernel at: %s" % self.kernels_url)

            # Let KERNEL_USERNAME take precedent over http_user config option.
            if os.environ.get("KERNEL_USERNAME") is None and GatewayClient.instance().http_user:
                os.environ["KERNEL_USERNAME"] = GatewayClient.instance().http_user

            kernel_env = {
                k: v
                for (k, v) in dict(os.environ).items()
                if k.startswith("KERNEL_") or k in GatewayClient.instance().env_whitelist.split(",")
            }

            # Add any env entries in this request
            kernel_env.update(kwargs.get("env", {}))

            # Convey the full path to where this notebook file is located.
            if kwargs.get("cwd") is not None and kernel_env.get("KERNEL_WORKING_DIR") is None:
                kernel_env["KERNEL_WORKING_DIR"] = kwargs["cwd"]

            json_body = json_encode({"name": kernel_name, "env": kernel_env})

            response = await gateway_request(
                self.kernels_url,
                method="POST",
                headers={"Content-Type": "application/json"},
                body=json_body,
            )
            self.kernel = json_decode(response.body)
            self.kernel_id = self.kernel["id"]
            self.kernel_url = url_path_join(self.kernels_url, url_escape(str(self.kernel_id)))
            self.log.info(f"GatewayKernelManager started kernel: {self.kernel_id}, args: {kwargs}")
        else:
            self.kernel_id = kernel_id
            self.kernel_url = url_path_join(self.kernels_url, url_escape(str(self.kernel_id)))
            self.kernel = await self.refresh_model()
            self.log.info(f"GatewayKernelManager using existing kernel: {self.kernel_id}")

    async def shutdown_kernel(self, now=False, restart=False):
        """Attempts to stop the kernel process cleanly via HTTP."""

        if self.has_kernel:
            self.log.debug("Request shutdown kernel at: %s", self.kernel_url)
            try:
                response = await gateway_request(self.kernel_url, method="DELETE")
                self.log.debug("Shutdown kernel response: %d %s", response.code, response.reason)
            except web.HTTPError as error:
                if error.status_code == 404:
                    self.log.debug("Shutdown kernel response: kernel not found (ignored)")
                else:
                    raise

    async def restart_kernel(self, **kw):
        """Restarts a kernel via HTTP."""
        if self.has_kernel:
            assert self.kernel_url is not None
            kernel_url = self.kernel_url + "/restart"
            self.log.debug("Request restart kernel at: %s", kernel_url)
            response = await gateway_request(
                kernel_url,
                method="POST",
                headers={"Content-Type": "application/json"},
                body=json_encode({}),
            )
            self.log.debug("Restart kernel response: %d %s", response.code, response.reason)

    async def interrupt_kernel(self):
        """Interrupts the kernel via an HTTP request."""
        if self.has_kernel:
            assert self.kernel_url is not None
            kernel_url = self.kernel_url + "/interrupt"
            self.log.debug("Request interrupt kernel at: %s", kernel_url)
            response = await gateway_request(
                kernel_url,
                method="POST",
                headers={"Content-Type": "application/json"},
                body=json_encode({}),
            )
            self.log.debug("Interrupt kernel response: %d %s", response.code, response.reason)

    async def is_alive(self):
        """Is the kernel process still running?"""
        if self.has_kernel:
            # Go ahead and issue a request to get the kernel
            self.kernel = await self.refresh_model()
            return True
        else:  # we don't have a kernel
            return False

    def cleanup_resources(self, restart=False):
        """Clean up resources when the kernel is shut down"""
        pass


KernelManagerABC.register(GatewayKernelManager)


class ChannelQueue(Queue):

    channel_name: Optional[str] = None
    response_router_finished: bool

    def __init__(self, channel_name: str, channel_socket: websocket.WebSocket, log: Logger):
        super().__init__()
        self.channel_name = channel_name
        self.channel_socket = channel_socket
        self.log = log
        self.response_router_finished = False

    async def _async_get(self, timeout=None):
        if timeout is None:
            timeout = float("inf")
        elif timeout < 0:
            raise ValueError("'timeout' must be a non-negative number")
        end_time = monotonic() + timeout

        while True:
            try:
                return self.get(block=False)
            except Empty:
                if self.response_router_finished:
                    raise RuntimeError("Response router had finished")
                if monotonic() > end_time:
                    raise
                await asyncio.sleep(0)

    async def get_msg(self, *args: Any, **kwargs: Any) -> dict:
        timeout = kwargs.get("timeout", 1)
        msg = await self._async_get(timeout=timeout)
        self.log.debug(
            "Received message on channel: {}, msg_id: {}, msg_type: {}".format(
                self.channel_name, msg["msg_id"], msg["msg_type"] if msg else "null"
            )
        )
        self.task_done()
        return msg

    def send(self, msg: dict) -> None:
        message = json.dumps(msg, default=ChannelQueue.serialize_datetime).replace("</", "<\\/")
        self.log.debug(
            "Sending message on channel: {}, msg_id: {}, msg_type: {}".format(
                self.channel_name, msg["msg_id"], msg["msg_type"] if msg else "null"
            )
        )
        self.channel_socket.send(message)

    @staticmethod
    def serialize_datetime(dt):
        if isinstance(dt, datetime.datetime):
            return dt.timestamp()
        return None

    def start(self) -> None:
        pass

    def stop(self) -> None:
        if not self.empty():
            # If unprocessed messages are detected, drain the queue collecting non-status
            # messages.  If any remain that are not 'shutdown_reply' and this is not iopub
            # go ahead and issue a warning.
            msgs = []
            while self.qsize():
                msg = self.get_nowait()
                if msg["msg_type"] != "status":
                    msgs.append(msg["msg_type"])
            if self.channel_name == "iopub" and "shutdown_reply" in msgs:
                return
            if len(msgs):
                self.log.warning(
                    "Stopping channel '{}' with {} unprocessed non-status messages: {}.".format(
                        self.channel_name, len(msgs), msgs
                    )
                )

    def is_alive(self) -> bool:
        return self.channel_socket is not None


class HBChannelQueue(ChannelQueue):
    def is_beating(self) -> bool:
        # Just use the is_alive status for now
        return self.is_alive()


class GatewayKernelClient(AsyncKernelClient):
    """Communicates with a single kernel indirectly via a websocket to a gateway server.

    There are five channels associated with each kernel:

    * shell: for request/reply calls to the kernel.
    * iopub: for the kernel to publish results to frontends.
    * hb: for monitoring the kernel's heartbeat.
    * stdin: for frontends to reply to raw_input calls in the kernel.
    * control: for kernel management calls to the kernel.

    The messages that can be sent on these channels are exposed as methods of the
    client (KernelClient.execute, complete, history, etc.). These methods only
    send the message, they don't wait for a reply. To get results, use e.g.
    :meth:`get_shell_msg` to fetch messages from the shell channel.
    """

    # flag for whether execute requests should be allowed to call raw_input:
    allow_stdin = False
    _channels_stopped: bool
    _channel_queues: Optional[Dict[str, ChannelQueue]]
    _control_channel: Optional[ChannelQueue]
    _hb_channel: Optional[ChannelQueue]
    _stdin_channel: Optional[ChannelQueue]
    _iopub_channel: Optional[ChannelQueue]
    _shell_channel: Optional[ChannelQueue]

    def __init__(self, kernel_id, **kwargs):
        super().__init__(**kwargs)
        self.kernel_id = kernel_id
        self.channel_socket: Optional[websocket.WebSocket] = None
        self.response_router: Optional[Thread] = None
        self._channels_stopped = False
        self._channel_queues = {}

    # --------------------------------------------------------------------------
    # Channel management methods
    # --------------------------------------------------------------------------

    async def start_channels(self, shell=True, iopub=True, stdin=True, hb=True, control=True):
        """Starts the channels for this kernel.

        For this class, we establish a websocket connection to the destination
        and set up the channel-based queues on which applicable messages will
        be posted.
        """

        ws_url = url_path_join(
            GatewayClient.instance().ws_url,
            GatewayClient.instance().kernels_endpoint,
            url_escape(self.kernel_id),
            "channels",
        )
        # Gather cert info in case where ssl is desired...
        ssl_options = {
            "ca_certs": GatewayClient.instance().ca_certs,
            "certfile": GatewayClient.instance().client_cert,
            "keyfile": GatewayClient.instance().client_key,
        }

        self.channel_socket = websocket.create_connection(
            ws_url,
            timeout=GatewayClient.instance().KERNEL_LAUNCH_TIMEOUT,
            enable_multithread=True,
            sslopt=ssl_options,
        )

        await ensure_async(
            super().start_channels(shell=shell, iopub=iopub, stdin=stdin, hb=hb, control=control)
        )

        self.response_router = Thread(target=self._route_responses)
        self.response_router.start()

    def stop_channels(self):
        """Stops all the running channels for this kernel.

        For this class, we close the websocket connection and destroy the
        channel-based queues.
        """
        super().stop_channels()
        self._channels_stopped = True
        self.log.debug("Closing websocket connection")

        assert self.channel_socket is not None
        self.channel_socket.close()
        assert self.response_router is not None
        self.response_router.join()

        if self._channel_queues:
            self._channel_queues.clear()
            self._channel_queues = None

    # Channels are implemented via a ChannelQueue that is used to send and receive messages

    @property
    def shell_channel(self):
        """Get the shell channel object for this kernel."""
        if self._shell_channel is None:
            self.log.debug("creating shell channel queue")
            assert self.channel_socket is not None
            self._shell_channel = ChannelQueue("shell", self.channel_socket, self.log)
            assert self._channel_queues is not None
            self._channel_queues["shell"] = self._shell_channel
        return self._shell_channel

    @property
    def iopub_channel(self):
        """Get the iopub channel object for this kernel."""
        if self._iopub_channel is None:
            self.log.debug("creating iopub channel queue")
            assert self.channel_socket is not None
            self._iopub_channel = ChannelQueue("iopub", self.channel_socket, self.log)
            assert self._channel_queues is not None
            self._channel_queues["iopub"] = self._iopub_channel
        return self._iopub_channel

    @property
    def stdin_channel(self):
        """Get the stdin channel object for this kernel."""
        if self._stdin_channel is None:
            self.log.debug("creating stdin channel queue")
            assert self.channel_socket is not None
            self._stdin_channel = ChannelQueue("stdin", self.channel_socket, self.log)
            assert self._channel_queues is not None
            self._channel_queues["stdin"] = self._stdin_channel
        return self._stdin_channel

    @property
    def hb_channel(self):
        """Get the hb channel object for this kernel."""
        if self._hb_channel is None:
            self.log.debug("creating hb channel queue")
            assert self.channel_socket is not None
            self._hb_channel = HBChannelQueue("hb", self.channel_socket, self.log)
            assert self._channel_queues is not None
            self._channel_queues["hb"] = self._hb_channel
        return self._hb_channel

    @property
    def control_channel(self):
        """Get the control channel object for this kernel."""
        if self._control_channel is None:
            self.log.debug("creating control channel queue")
            assert self.channel_socket is not None
            self._control_channel = ChannelQueue("control", self.channel_socket, self.log)
            assert self._channel_queues is not None
            self._channel_queues["control"] = self._control_channel
        return self._control_channel

    def _route_responses(self):
        """
        Reads responses from the websocket and routes each to the appropriate channel queue based
        on the message's channel.  It does this for the duration of the class's lifetime until the
        channels are stopped, at which time the socket is closed (unblocking the router) and
        the thread terminates.  If shutdown happens to occur while processing a response (unlikely),
        termination takes place via the loop control boolean.
        """
        try:
            while not self._channels_stopped:
                assert self.channel_socket is not None
                raw_message = self.channel_socket.recv()
                if not raw_message:
                    break
                response_message = json_decode(utf8(raw_message))
                channel = response_message["channel"]
                assert self._channel_queues is not None
                self._channel_queues[channel].put_nowait(response_message)

        except websocket.WebSocketConnectionClosedException:
            pass  # websocket closure most likely due to shut down

        except BaseException as be:
            if not self._channels_stopped:
                self.log.warning(f"Unexpected exception encountered ({be})")

        # Notify channel queues that this thread had finished and no more messages are being received
        assert self._channel_queues is not None
        for channel_queue in self._channel_queues.values():
            channel_queue.response_router_finished = True

        self.log.debug("Response router thread exiting...")


KernelClientABC.register(GatewayKernelClient)
