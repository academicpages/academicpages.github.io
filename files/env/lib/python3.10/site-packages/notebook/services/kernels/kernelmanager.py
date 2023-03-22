"""A MultiKernelManager for use in the notebook webserver
- raises HTTPErrors
- creates REST API models
"""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

from collections import defaultdict
from datetime import datetime, timedelta
from functools import partial
import os

from tornado import web
from tornado.concurrent import Future
from tornado.ioloop import IOLoop, PeriodicCallback

from jupyter_client.session import Session
from jupyter_client.multikernelmanager import MultiKernelManager
from traitlets import (Any, Bool, Dict, List, Unicode, TraitError, Integer,
       Float, Instance, default, validate
)

from notebook.utils import maybe_future, to_os_path, exists
from notebook._tz import utcnow, isoformat
from ipython_genutils.py3compat import getcwd

from notebook.prometheus.metrics import KERNEL_CURRENTLY_RUNNING_TOTAL

# Since use of AsyncMultiKernelManager is optional at the moment, don't require appropriate jupyter_client.
# This will be confirmed at runtime in notebookapp.  The following block can be removed once the jupyter_client's
# floor has been updated.
try:
    from jupyter_client.multikernelmanager import AsyncMultiKernelManager
except ImportError:
    class AsyncMultiKernelManager:
        """Empty class to satisfy unused reference by AsyncMappingKernelManager."""
        def __init__(self, **kwargs):
            pass


class MappingKernelManager(MultiKernelManager):
    """A KernelManager that handles notebook mapping and HTTP error handling"""

    @default('kernel_manager_class')
    def _default_kernel_manager_class(self):
        return "jupyter_client.ioloop.IOLoopKernelManager"

    kernel_argv = List(Unicode())

    root_dir = Unicode(config=True)

    _kernel_connections = Dict()

    _culler_callback = None

    _initialized_culler = False

    @default('root_dir')
    def _default_root_dir(self):
        try:
            return self.parent.notebook_dir
        except AttributeError:
            return getcwd()

    @validate('root_dir')
    def _update_root_dir(self, proposal):
        """Do a bit of validation of the root dir."""
        value = proposal['value']
        if not os.path.isabs(value):
            # If we receive a non-absolute path, make it absolute.
            value = os.path.abspath(value)
        if not exists(value) or not os.path.isdir(value):
            raise TraitError(f"kernel root dir {value!r} is not a directory")
        return value

    cull_idle_timeout = Integer(0, config=True,
        help="""Timeout (in seconds) after which a kernel is considered idle and ready to be culled.
        Values of 0 or lower disable culling. Very short timeouts may result in kernels being culled
        for users with poor network connections."""
    )

    cull_interval_default = 300  # 5 minutes
    cull_interval = Integer(cull_interval_default, config=True,
        help="""The interval (in seconds) on which to check for idle kernels exceeding the cull timeout value."""
    )

    cull_connected = Bool(False, config=True,
        help="""Whether to consider culling kernels which have one or more connections.
        Only effective if cull_idle_timeout > 0."""
    )

    cull_busy = Bool(False, config=True,
        help="""Whether to consider culling kernels which are busy.
        Only effective if cull_idle_timeout > 0."""
    )

    buffer_offline_messages = Bool(True, config=True,
        help="""Whether messages from kernels whose frontends have disconnected should be buffered in-memory.
        When True (default), messages are buffered and replayed on reconnect,
        avoiding lost messages due to interrupted connectivity.
        Disable if long-running kernels will produce too much output while
        no frontends are connected.
        """
    )

    kernel_info_timeout = Float(60, config=True,
        help="""Timeout for giving up on a kernel (in seconds).
        On starting and restarting kernels, we check whether the
        kernel is running and responsive by sending kernel_info_requests.
        This sets the timeout in seconds for how long the kernel can take
        before being presumed dead.
        This affects the MappingKernelManager (which handles kernel restarts)
        and the ZMQChannelsHandler (which handles the startup).
        """
    )

    _kernel_buffers = Any()
    @default('_kernel_buffers')
    def _default_kernel_buffers(self):
        return defaultdict(lambda: {'buffer': [], 'session_key': '', 'channels': {}})

    last_kernel_activity = Instance(datetime,
        help="The last activity on any kernel, including shutting down a kernel")

    allowed_message_types = List(trait=Unicode(), config=True,
        help="""White list of allowed kernel message types.
        When the list is empty, all message types are allowed.
        """
    )

    #-------------------------------------------------------------------------
    # Methods for managing kernels and sessions
    #-------------------------------------------------------------------------

    def __init__(self, **kwargs):
        # Pin the superclass to better control the MRO.  This is needed by
        # AsyncMappingKernelManager so that it can give priority to methods
        # on AsyncMultiKernelManager over this superclass.
        self.pinned_superclass = MultiKernelManager
        self.pinned_superclass.__init__(self, **kwargs)
        self.last_kernel_activity = utcnow()

    def _handle_kernel_died(self, kernel_id):
        """notice that a kernel died"""
        self.log.warning("Kernel %s died, removing from map.", kernel_id)
        self.remove_kernel(kernel_id)

    def cwd_for_path(self, path):
        """Turn API path into absolute OS path."""
        os_path = to_os_path(path, self.root_dir)
        # in the case of notebooks and kernels not being on the same filesystem,
        # walk up to root_dir if the paths don't exist
        while not os.path.isdir(os_path) and os_path != self.root_dir:
            os_path = os.path.dirname(os_path)
        return os_path

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
        kernel_name : str
            The name identifying which kernel spec to launch. This is ignored if
            an existing kernel is returned, but it may be checked in the future.
        """
        if kernel_id is None:
            if path is not None:
                kwargs['cwd'] = self.cwd_for_path(path)
            kernel_id = await maybe_future(self.pinned_superclass.start_kernel(self, **kwargs))
            self._kernel_connections[kernel_id] = 0
            self.start_watching_activity(kernel_id)
            self.log.info(f"Kernel started: {kernel_id}, name: {self._kernels[kernel_id].kernel_name}")
            self.log.debug(f"Kernel args: {kwargs!r}")
            # register callback for failed auto-restart
            self.add_restart_callback(kernel_id,
                lambda : self._handle_kernel_died(kernel_id),
                'dead',
            )

            # Increase the metric of number of kernels running
            # for the relevant kernel type by 1
            KERNEL_CURRENTLY_RUNNING_TOTAL.labels(
                type=self._kernels[kernel_id].kernel_name
            ).inc()

        else:
            self._check_kernel_id(kernel_id)
            self.log.info(f"Using existing kernel: {kernel_id}")

        # Initialize culling if not already
        if not self._initialized_culler:
            self.initialize_culler()

        return kernel_id

    def start_buffering(self, kernel_id, session_key, channels):
        """Start buffering messages for a kernel
        Parameters
        ----------
        kernel_id : str
            The id of the kernel to start buffering.
        session_key: str
            The session_key, if any, that should get the buffer.
            If the session_key matches the current buffered session_key,
            the buffer will be returned.
        channels: dict({'channel': ZMQStream})
            The zmq channels whose messages should be buffered.
        """

        if not self.buffer_offline_messages:
            for channel, stream in channels.items():
                stream.close()
            return

        self.log.info("Starting buffering for %s", session_key)
        self._check_kernel_id(kernel_id)
        # clear previous buffering state
        self.stop_buffering(kernel_id)
        buffer_info = self._kernel_buffers[kernel_id]
        # record the session key because only one session can buffer
        buffer_info['session_key'] = session_key
        # TODO: the buffer should likely be a memory bounded queue, we're starting with a list to keep it simple
        buffer_info['buffer'] = []
        buffer_info['channels'] = channels

        # forward any future messages to the internal buffer
        def buffer_msg(channel, msg_parts):
            self.log.debug("Buffering msg on %s:%s", kernel_id, channel)
            buffer_info['buffer'].append((channel, msg_parts))

        for channel, stream in channels.items():
            stream.on_recv(partial(buffer_msg, channel))

    def get_buffer(self, kernel_id, session_key):
        """Get the buffer for a given kernel
        Parameters
        ----------
        kernel_id : str
            The id of the kernel to stop buffering.
        session_key: str, optional
            The session_key, if any, that should get the buffer.
            If the session_key matches the current buffered session_key,
            the buffer will be returned.
        """
        self.log.debug("Getting buffer for %s", kernel_id)
        if kernel_id not in self._kernel_buffers:
            return

        buffer_info = self._kernel_buffers[kernel_id]
        if buffer_info['session_key'] == session_key:
            # remove buffer
            self._kernel_buffers.pop(kernel_id)
            # only return buffer_info if it's a match
            return buffer_info
        else:
            self.stop_buffering(kernel_id)

    def stop_buffering(self, kernel_id):
        """Stop buffering kernel messages
        Parameters
        ----------
        kernel_id : str
            The id of the kernel to stop buffering.
        """
        self.log.debug("Clearing buffer for %s", kernel_id)
        self._check_kernel_id(kernel_id)

        if kernel_id not in self._kernel_buffers:
            return
        buffer_info = self._kernel_buffers.pop(kernel_id)
        # close buffering streams
        for stream in buffer_info['channels'].values():
            if not stream.closed():
                stream.on_recv(None)
                stream.close()

        msg_buffer = buffer_info['buffer']
        if msg_buffer:
            self.log.info("Discarding %s buffered messages for %s",
                len(msg_buffer), buffer_info['session_key'])

    def shutdown_kernel(self, kernel_id, now=False, restart=False):
        """Shutdown a kernel by kernel_id"""
        self._check_kernel_id(kernel_id)
        kernel = self._kernels[kernel_id]
        if kernel._activity_stream:
            kernel._activity_stream.close()
            kernel._activity_stream = None
        self.stop_buffering(kernel_id)

        # Decrease the metric of number of kernels
        # running for the relevant kernel type by 1
        KERNEL_CURRENTLY_RUNNING_TOTAL.labels(
            type=self._kernels[kernel_id].kernel_name
        ).dec()

        self.pinned_superclass.shutdown_kernel(self, kernel_id, now=now, restart=restart)
        # Unlike its async sibling method in AsyncMappingKernelManager, removing the kernel_id
        # from the connections dictionary isn't as problematic before the shutdown since the
        # method is synchronous.  However, we'll keep the relative call orders the same from
        # a maintenance perspective.
        self._kernel_connections.pop(kernel_id, None)

    async def restart_kernel(self, kernel_id, now=False):
        """Restart a kernel by kernel_id"""
        self._check_kernel_id(kernel_id)
        await maybe_future(self.pinned_superclass.restart_kernel(self, kernel_id, now=now))
        kernel = self.get_kernel(kernel_id)
        # return a Future that will resolve when the kernel has successfully restarted
        channel = kernel.connect_shell()
        future = Future()

        def finish():
            """Common cleanup when restart finishes/fails for any reason."""
            if not channel.closed():
                channel.close()
            loop.remove_timeout(timeout)
            kernel.remove_restart_callback(on_restart_failed, 'dead')

        def on_reply(msg):
            self.log.debug("Kernel info reply received: %s", kernel_id)
            finish()
            if not future.done():
                future.set_result(msg)

        def on_timeout():
            self.log.warning("Timeout waiting for kernel_info_reply: %s", kernel_id)
            finish()
            if not future.done():
                future.set_exception(TimeoutError("Timeout waiting for restart"))

        def on_restart_failed():
            self.log.warning("Restarting kernel failed: %s", kernel_id)
            finish()
            if not future.done():
                future.set_exception(RuntimeError("Restart failed"))

        kernel.add_restart_callback(on_restart_failed, 'dead')
        kernel.session.send(channel, "kernel_info_request")
        channel.on_recv(on_reply)
        loop = IOLoop.current()
        timeout = loop.add_timeout(loop.time() + self.kernel_info_timeout, on_timeout)
        return future

    def notify_connect(self, kernel_id):
        """Notice a new connection to a kernel"""
        if kernel_id in self._kernel_connections:
            self._kernel_connections[kernel_id] += 1

    def notify_disconnect(self, kernel_id):
        """Notice a disconnection from a kernel"""
        if kernel_id in self._kernel_connections:
            self._kernel_connections[kernel_id] -= 1

    def kernel_model(self, kernel_id):
        """Return a JSON-safe dict representing a kernel
        For use in representing kernels in the JSON APIs.
        """
        self._check_kernel_id(kernel_id)
        kernel = self._kernels[kernel_id]

        model = {
            "id": kernel_id,
            "name": kernel.kernel_name,
            "last_activity": isoformat(kernel.last_activity),
            "execution_state": kernel.execution_state,
            "connections": self._kernel_connections[kernel_id],
        }
        return model

    def list_kernels(self):
        """Returns a list of kernel_id's of kernels running."""
        kernels = []
        kernel_ids = self.pinned_superclass.list_kernel_ids(self)
        for kernel_id in kernel_ids:
            try:
                model = self.kernel_model(kernel_id)
                kernels.append(model)
            except (web.HTTPError, KeyError):
                pass  # Probably due to a (now) non-existent kernel, continue building the list
        return kernels

    # override _check_kernel_id to raise 404 instead of KeyError
    def _check_kernel_id(self, kernel_id):
        """Check a that a kernel_id exists and raise 404 if not."""
        if kernel_id not in self:
            raise web.HTTPError(404, f'Kernel does not exist: {kernel_id}')

    # monitoring activity:

    def start_watching_activity(self, kernel_id):
        """Start watching IOPub messages on a kernel for activity.
        - update last_activity on every message
        - record execution_state from status messages
        """
        kernel = self._kernels[kernel_id]
        # add busy/activity markers:
        kernel.execution_state = 'starting'
        kernel.last_activity = utcnow()
        kernel._activity_stream = kernel.connect_iopub()
        session = Session(
            config=kernel.session.config,
            key=kernel.session.key,
        )

        def record_activity(msg_list):
            """Record an IOPub message arriving from a kernel"""
            self.last_kernel_activity = kernel.last_activity = utcnow()

            idents, fed_msg_list = session.feed_identities(msg_list)
            msg = session.deserialize(fed_msg_list)

            msg_type = msg['header']['msg_type']
            if msg_type == 'status':
                kernel.execution_state = msg['content']['execution_state']
                self.log.debug("activity on %s: %s (%s)", kernel_id, msg_type, kernel.execution_state)
            else:
                self.log.debug("activity on %s: %s", kernel_id, msg_type)

        kernel._activity_stream.on_recv(record_activity)

    def initialize_culler(self):
        """Start idle culler if 'cull_idle_timeout' is greater than zero.
        Regardless of that value, set flag that we've been here.
        """
        if not self._initialized_culler and self.cull_idle_timeout > 0:
            if self._culler_callback is None:
                loop = IOLoop.current()
                if self.cull_interval <= 0:  # handle case where user set invalid value
                    self.log.warning("Invalid value for 'cull_interval' detected (%s) - using default value (%s).",
                        self.cull_interval, self.cull_interval_default)
                    self.cull_interval = self.cull_interval_default
                self._culler_callback = PeriodicCallback(
                    self.cull_kernels, 1000*self.cull_interval)
                self.log.info("Culling kernels with idle durations > %s seconds at %s second intervals ...",
                    self.cull_idle_timeout, self.cull_interval)
                if self.cull_busy:
                    self.log.info("Culling kernels even if busy")
                if self.cull_connected:
                    self.log.info("Culling kernels even with connected clients")
                self._culler_callback.start()

        self._initialized_culler = True

    async def cull_kernels(self):
        self.log.debug("Polling every %s seconds for kernels idle > %s seconds...",
            self.cull_interval, self.cull_idle_timeout)
        """Create a separate list of kernels to avoid conflicting updates while iterating"""
        for kernel_id in list(self._kernels):
            try:
                await self.cull_kernel_if_idle(kernel_id)
            except Exception as e:
                self.log.exception(
                    f"The following exception was encountered while checking the idle duration of kernel "
                    f"{kernel_id}: {e}"
                )

    async def cull_kernel_if_idle(self, kernel_id):
        try:
            kernel = self._kernels[kernel_id]
        except KeyError:
            return  # KeyErrors are somewhat expected since the kernel can be shutdown as the culling check is made.

        if hasattr(kernel, 'last_activity'):  # last_activity is monkey-patched, so ensure that has occurred
            self.log.debug("kernel_id=%s, kernel_name=%s, last_activity=%s",
                           kernel_id, kernel.kernel_name, kernel.last_activity)
            dt_now = utcnow()
            dt_idle = dt_now - kernel.last_activity
            # Compute idle properties
            is_idle_time = dt_idle > timedelta(seconds=self.cull_idle_timeout)
            is_idle_execute = self.cull_busy or (kernel.execution_state != 'busy')
            connections = self._kernel_connections.get(kernel_id, 0)
            is_idle_connected = self.cull_connected or not connections
            # Cull the kernel if all three criteria are met
            if (is_idle_time and is_idle_execute and is_idle_connected):
                idle_duration = int(dt_idle.total_seconds())
                self.log.warning("Culling '%s' kernel '%s' (%s) with %d connections due to %s seconds of inactivity.",
                                 kernel.execution_state, kernel.kernel_name, kernel_id, connections, idle_duration)
                await maybe_future(self.shutdown_kernel(kernel_id))


# AsyncMappingKernelManager inherits as much as possible from MappingKernelManager, overriding
# only what is different.
class AsyncMappingKernelManager(MappingKernelManager, AsyncMultiKernelManager):
    @default('kernel_manager_class')
    def _default_kernel_manager_class(self):
        return "jupyter_client.ioloop.AsyncIOLoopKernelManager"

    def __init__(self, **kwargs):
        # Pin the superclass to better control the MRO.
        self.pinned_superclass = AsyncMultiKernelManager
        self.pinned_superclass.__init__(self, **kwargs)
        self.last_kernel_activity = utcnow()

    async def shutdown_kernel(self, kernel_id, now=False, restart=False):
        """Shutdown a kernel by kernel_id"""
        self._check_kernel_id(kernel_id)
        kernel = self._kernels[kernel_id]
        if kernel._activity_stream:
            kernel._activity_stream.close()
            kernel._activity_stream = None
        self.stop_buffering(kernel_id)

        # Decrease the metric of number of kernels
        # running for the relevant kernel type by 1
        KERNEL_CURRENTLY_RUNNING_TOTAL.labels(
            type=self._kernels[kernel_id].kernel_name
        ).dec()

        await self.pinned_superclass.shutdown_kernel(self, kernel_id, now=now, restart=restart)
        # Remove kernel_id from the connections dictionary only after kernel has been shutdown,
        # otherwise a race condition can occur since the shutdown may take a while - allowing
        # list/fetch kernel operations to access _kernel_connections for a non-existent key
        # (kernel_id) while "awaiting" the result of the shutdown.
        self._kernel_connections.pop(kernel_id, None)
