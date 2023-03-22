"""Base class to manage a running kernel"""
# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
import asyncio
import functools
import os
import re
import signal
import sys
import typing as t
import uuid
from asyncio.futures import Future
from concurrent.futures import Future as CFuture
from contextlib import contextmanager
from enum import Enum

import zmq
from traitlets import Any
from traitlets import Bool
from traitlets import default
from traitlets import DottedObjectName
from traitlets import Float
from traitlets import Instance
from traitlets import observe
from traitlets import observe_compat
from traitlets import Type
from traitlets import Unicode
from traitlets.utils.importstring import import_item

from .connect import ConnectionFileMixin
from .managerabc import KernelManagerABC
from .provisioning import KernelProvisionerBase
from .provisioning import KernelProvisionerFactory as KPF
from .utils import ensure_async
from .utils import run_sync
from jupyter_client import KernelClient
from jupyter_client import kernelspec


class _ShutdownStatus(Enum):
    """

    This is so far used only for testing in order to track the internal state of
    the shutdown logic, and verifying which path is taken for which
    missbehavior.

    """

    Unset = None
    ShutdownRequest = "ShutdownRequest"
    SigtermRequest = "SigtermRequest"
    SigkillRequest = "SigkillRequest"


F = t.TypeVar('F', bound=t.Callable[..., t.Any])


def in_pending_state(method: F) -> F:
    """Sets the kernel to a pending state by
    creating a fresh Future for the KernelManager's `ready`
    attribute. Once the method is finished, set the Future's results.
    """

    @t.no_type_check
    @functools.wraps(method)
    async def wrapper(self, *args, **kwargs):
        # Create a future for the decorated method
        try:
            self._ready = Future()
        except RuntimeError:
            # No event loop running, use concurrent future
            self._ready = CFuture()
        try:
            # call wrapped method, await, and set the result or exception.
            out = await method(self, *args, **kwargs)
            # Add a small sleep to ensure tests can capture the state before done
            await asyncio.sleep(0.01)
            self._ready.set_result(None)
            return out
        except Exception as e:
            self._ready.set_exception(e)
            self.log.exception(self._ready.exception())
            raise e

    return t.cast(F, wrapper)


class KernelManager(ConnectionFileMixin):
    """Manages a single kernel in a subprocess on this host.

    This version starts kernels with Popen.
    """

    _ready: t.Union[Future, CFuture]

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self._shutdown_status = _ShutdownStatus.Unset
        # Create a place holder future.
        try:
            asyncio.get_running_loop()
            self._ready = Future()
        except RuntimeError:
            # No event loop running, use concurrent future
            self._ready = CFuture()

    _created_context: Bool = Bool(False)

    # The PyZMQ Context to use for communication with the kernel.
    context: Instance = Instance(zmq.Context)

    @default("context")  # type:ignore[misc]
    def _context_default(self) -> zmq.Context:
        self._created_context = True
        return zmq.Context()

    # the class to create with our `client` method
    client_class: DottedObjectName = DottedObjectName(
        "jupyter_client.blocking.BlockingKernelClient"
    )
    client_factory: Type = Type(klass="jupyter_client.KernelClient")

    @default("client_factory")  # type:ignore[misc]
    def _client_factory_default(self) -> Type:
        return import_item(self.client_class)

    @observe("client_class")  # type:ignore[misc]
    def _client_class_changed(self, change: t.Dict[str, DottedObjectName]) -> None:
        self.client_factory = import_item(str(change["new"]))

    kernel_id: str = Unicode(None, allow_none=True)

    # The kernel provisioner with which this KernelManager is communicating.
    # This will generally be a LocalProvisioner instance unless the kernelspec
    # indicates otherwise.
    provisioner: t.Optional[KernelProvisionerBase] = None

    kernel_spec_manager: Instance = Instance(kernelspec.KernelSpecManager)

    @default("kernel_spec_manager")  # type:ignore[misc]
    def _kernel_spec_manager_default(self) -> kernelspec.KernelSpecManager:
        return kernelspec.KernelSpecManager(data_dir=self.data_dir)

    @observe("kernel_spec_manager")  # type:ignore[misc]
    @observe_compat  # type:ignore[misc]
    def _kernel_spec_manager_changed(self, change: t.Dict[str, Instance]) -> None:
        self._kernel_spec = None

    shutdown_wait_time: Float = Float(
        5.0,
        config=True,
        help="Time to wait for a kernel to terminate before killing it, "
        "in seconds. When a shutdown request is initiated, the kernel "
        "will be immediately sent an interrupt (SIGINT), followed"
        "by a shutdown_request message, after 1/2 of `shutdown_wait_time`"
        "it will be sent a terminate (SIGTERM) request, and finally at "
        "the end of `shutdown_wait_time` will be killed (SIGKILL). terminate "
        "and kill may be equivalent on windows.  Note that this value can be"
        "overridden by the in-use kernel provisioner since shutdown times may"
        "vary by provisioned environment.",
    )

    kernel_name: Unicode = Unicode(kernelspec.NATIVE_KERNEL_NAME)

    @observe("kernel_name")  # type:ignore[misc]
    def _kernel_name_changed(self, change: t.Dict[str, Unicode]) -> None:
        self._kernel_spec = None
        if change["new"] == "python":
            self.kernel_name = kernelspec.NATIVE_KERNEL_NAME

    _kernel_spec: t.Optional[kernelspec.KernelSpec] = None

    @property
    def kernel_spec(self) -> t.Optional[kernelspec.KernelSpec]:
        if self._kernel_spec is None and self.kernel_name != "":
            self._kernel_spec = self.kernel_spec_manager.get_kernel_spec(self.kernel_name)
        return self._kernel_spec

    cache_ports: Bool = Bool(
        help="True if the MultiKernelManager should cache ports for this KernelManager instance"
    )

    @default("cache_ports")  # type:ignore[misc]
    def _default_cache_ports(self) -> bool:
        return self.transport == "tcp"

    @property
    def ready(self) -> t.Union[CFuture, Future]:
        """A future that resolves when the kernel process has started for the first time"""
        return self._ready

    @property
    def ipykernel(self) -> bool:
        return self.kernel_name in {"python", "python2", "python3"}

    # Protected traits
    _launch_args: Any = Any()
    _control_socket: Any = Any()

    _restarter: Any = Any()

    autorestart: Bool = Bool(
        True, config=True, help="""Should we autorestart the kernel if it dies."""
    )

    shutting_down: bool = False

    def __del__(self) -> None:
        self._close_control_socket()
        self.cleanup_connection_file()

    # --------------------------------------------------------------------------
    # Kernel restarter
    # --------------------------------------------------------------------------

    def start_restarter(self) -> None:
        pass

    def stop_restarter(self) -> None:
        pass

    def add_restart_callback(self, callback: t.Callable, event: str = "restart") -> None:
        """register a callback to be called when a kernel is restarted"""
        if self._restarter is None:
            return
        self._restarter.add_callback(callback, event)

    def remove_restart_callback(self, callback: t.Callable, event: str = "restart") -> None:
        """unregister a callback to be called when a kernel is restarted"""
        if self._restarter is None:
            return
        self._restarter.remove_callback(callback, event)

    # --------------------------------------------------------------------------
    # create a Client connected to our Kernel
    # --------------------------------------------------------------------------

    def client(self, **kwargs: t.Any) -> KernelClient:
        """Create a client configured to connect to our kernel"""
        kw = {}
        kw.update(self.get_connection_info(session=True))
        kw.update(
            dict(
                connection_file=self.connection_file,
                parent=self,
            )
        )

        # add kwargs last, for manual overrides
        kw.update(kwargs)
        return self.client_factory(**kw)

    # --------------------------------------------------------------------------
    # Kernel management
    # --------------------------------------------------------------------------

    def format_kernel_cmd(self, extra_arguments: t.Optional[t.List[str]] = None) -> t.List[str]:
        """replace templated args (e.g. {connection_file})"""
        extra_arguments = extra_arguments or []
        assert self.kernel_spec is not None
        cmd = self.kernel_spec.argv + extra_arguments

        if cmd and cmd[0] in {
            "python",
            "python%i" % sys.version_info[0],
            "python%i.%i" % sys.version_info[:2],
        }:
            # executable is 'python' or 'python3', use sys.executable.
            # These will typically be the same,
            # but if the current process is in an env
            # and has been launched by abspath without
            # activating the env, python on PATH may not be sys.executable,
            # but it should be.
            cmd[0] = sys.executable

        # Make sure to use the realpath for the connection_file
        # On windows, when running with the store python, the connection_file path
        # is not usable by non python kernels because the path is being rerouted when
        # inside of a store app.
        # See this bug here: https://bugs.python.org/issue41196
        ns = dict(
            connection_file=os.path.realpath(self.connection_file),
            prefix=sys.prefix,
        )

        if self.kernel_spec:
            ns["resource_dir"] = self.kernel_spec.resource_dir

        ns.update(self._launch_args)

        pat = re.compile(r"\{([A-Za-z0-9_]+)\}")

        def from_ns(match):
            """Get the key out of ns if it's there, otherwise no change."""
            return ns.get(match.group(1), match.group())

        return [pat.sub(from_ns, arg) for arg in cmd]

    async def _async_launch_kernel(self, kernel_cmd: t.List[str], **kw: t.Any) -> None:
        """actually launch the kernel

        override in a subclass to launch kernel subprocesses differently
        Note that provisioners can now be used to customize kernel environments
        and
        """
        assert self.provisioner is not None
        connection_info = await self.provisioner.launch_kernel(kernel_cmd, **kw)
        assert self.provisioner.has_process
        # Provisioner provides the connection information.  Load into kernel manager and write file.
        self._force_connection_info(connection_info)

    _launch_kernel = run_sync(_async_launch_kernel)

    # Control socket used for polite kernel shutdown

    def _connect_control_socket(self) -> None:
        if self._control_socket is None:
            self._control_socket = self._create_connected_socket("control")
            self._control_socket.linger = 100

    def _close_control_socket(self) -> None:
        if self._control_socket is None:
            return
        self._control_socket.close()
        self._control_socket = None

    async def _async_pre_start_kernel(
        self, **kw: t.Any
    ) -> t.Tuple[t.List[str], t.Dict[str, t.Any]]:
        """Prepares a kernel for startup in a separate process.

        If random ports (port=0) are being used, this method must be called
        before the channels are created.

        Parameters
        ----------
        `**kw` : optional
             keyword arguments that are passed down to build the kernel_cmd
             and launching the kernel (e.g. Popen kwargs).
        """
        self.shutting_down = False
        self.kernel_id = self.kernel_id or kw.pop('kernel_id', str(uuid.uuid4()))
        # save kwargs for use in restart
        self._launch_args = kw.copy()
        if self.provisioner is None:  # will not be None on restarts
            self.provisioner = KPF.instance(parent=self.parent).create_provisioner_instance(
                self.kernel_id,
                self.kernel_spec,
                parent=self,
            )
        kw = await self.provisioner.pre_launch(**kw)
        kernel_cmd = kw.pop('cmd')
        return kernel_cmd, kw

    pre_start_kernel = run_sync(_async_pre_start_kernel)

    async def _async_post_start_kernel(self, **kw: t.Any) -> None:
        """Performs any post startup tasks relative to the kernel.

        Parameters
        ----------
        `**kw` : optional
             keyword arguments that were used in the kernel process's launch.
        """
        self.start_restarter()
        self._connect_control_socket()
        assert self.provisioner is not None
        await self.provisioner.post_launch(**kw)

    post_start_kernel = run_sync(_async_post_start_kernel)

    @in_pending_state
    async def _async_start_kernel(self, **kw: t.Any) -> None:
        """Starts a kernel on this host in a separate process.

        If random ports (port=0) are being used, this method must be called
        before the channels are created.

        Parameters
        ----------
        `**kw` : optional
             keyword arguments that are passed down to build the kernel_cmd
             and launching the kernel (e.g. Popen kwargs).
        """
        kernel_cmd, kw = await ensure_async(self.pre_start_kernel(**kw))

        # launch the kernel subprocess
        self.log.debug("Starting kernel: %s", kernel_cmd)
        await ensure_async(self._launch_kernel(kernel_cmd, **kw))
        await ensure_async(self.post_start_kernel(**kw))

    start_kernel = run_sync(_async_start_kernel)

    async def _async_request_shutdown(self, restart: bool = False) -> None:
        """Send a shutdown request via control channel"""
        content = dict(restart=restart)
        msg = self.session.msg("shutdown_request", content=content)
        # ensure control socket is connected
        self._connect_control_socket()
        self.session.send(self._control_socket, msg)
        assert self.provisioner is not None
        await self.provisioner.shutdown_requested(restart=restart)
        self._shutdown_status = _ShutdownStatus.ShutdownRequest

    request_shutdown = run_sync(_async_request_shutdown)

    async def _async_finish_shutdown(
        self,
        waittime: t.Optional[float] = None,
        pollinterval: float = 0.1,
        restart: t.Optional[bool] = False,
    ) -> None:
        """Wait for kernel shutdown, then kill process if it doesn't shutdown.

        This does not send shutdown requests - use :meth:`request_shutdown`
        first.
        """
        if waittime is None:
            waittime = max(self.shutdown_wait_time, 0)
        if self.provisioner:  # Allow provisioner to override
            waittime = self.provisioner.get_shutdown_wait_time(recommended=waittime)

        try:
            await asyncio.wait_for(
                self._async_wait(pollinterval=pollinterval), timeout=waittime / 2
            )
        except asyncio.TimeoutError:
            self.log.debug("Kernel is taking too long to finish, terminating")
            self._shutdown_status = _ShutdownStatus.SigtermRequest
            await ensure_async(self._send_kernel_sigterm())

        try:
            await asyncio.wait_for(
                self._async_wait(pollinterval=pollinterval), timeout=waittime / 2
            )
        except asyncio.TimeoutError:
            self.log.debug("Kernel is taking too long to finish, killing")
            self._shutdown_status = _ShutdownStatus.SigkillRequest
            await ensure_async(self._kill_kernel(restart=restart))
        else:
            # Process is no longer alive, wait and clear
            if self.has_kernel:
                assert self.provisioner is not None
                await self.provisioner.wait()

    finish_shutdown = run_sync(_async_finish_shutdown)

    async def _async_cleanup_resources(self, restart: bool = False) -> None:
        """Clean up resources when the kernel is shut down"""
        if not restart:
            self.cleanup_connection_file()

        self.cleanup_ipc_files()
        self._close_control_socket()
        self.session.parent = None

        if self._created_context and not restart:
            self.context.destroy(linger=100)

        if self.provisioner:
            await self.provisioner.cleanup(restart=restart)

    cleanup_resources = run_sync(_async_cleanup_resources)

    @in_pending_state
    async def _async_shutdown_kernel(self, now: bool = False, restart: bool = False) -> None:
        """Attempts to stop the kernel process cleanly.

        This attempts to shutdown the kernels cleanly by:

        1. Sending it a shutdown message over the control channel.
        2. If that fails, the kernel is shutdown forcibly by sending it
           a signal.

        Parameters
        ----------
        now : bool
            Should the kernel be forcible killed *now*. This skips the
            first, nice shutdown attempt.
        restart: bool
            Will this kernel be restarted after it is shutdown. When this
            is True, connection files will not be cleaned up.
        """
        self.shutting_down = True  # Used by restarter to prevent race condition
        # Stop monitoring for restarting while we shutdown.
        self.stop_restarter()

        if self.has_kernel:
            await ensure_async(self.interrupt_kernel())

        if now:
            await ensure_async(self._kill_kernel())
        else:
            await ensure_async(self.request_shutdown(restart=restart))
            # Don't send any additional kernel kill messages immediately, to give
            # the kernel a chance to properly execute shutdown actions. Wait for at
            # most 1s, checking every 0.1s.
            await ensure_async(self.finish_shutdown(restart=restart))

        await ensure_async(self.cleanup_resources(restart=restart))

    shutdown_kernel = run_sync(_async_shutdown_kernel)

    async def _async_restart_kernel(
        self, now: bool = False, newports: bool = False, **kw: t.Any
    ) -> None:
        """Restarts a kernel with the arguments that were used to launch it.

        Parameters
        ----------
        now : bool, optional
            If True, the kernel is forcefully restarted *immediately*, without
            having a chance to do any cleanup action.  Otherwise the kernel is
            given 1s to clean up before a forceful restart is issued.

            In all cases the kernel is restarted, the only difference is whether
            it is given a chance to perform a clean shutdown or not.

        newports : bool, optional
            If the old kernel was launched with random ports, this flag decides
            whether the same ports and connection file will be used again.
            If False, the same ports and connection file are used. This is
            the default. If True, new random port numbers are chosen and a
            new connection file is written. It is still possible that the newly
            chosen random port numbers happen to be the same as the old ones.

        `**kw` : optional
            Any options specified here will overwrite those used to launch the
            kernel.
        """
        if self._launch_args is None:
            raise RuntimeError("Cannot restart the kernel. No previous call to 'start_kernel'.")

        # Stop currently running kernel.
        await ensure_async(self.shutdown_kernel(now=now, restart=True))

        if newports:
            self.cleanup_random_ports()

        # Start new kernel.
        self._launch_args.update(kw)
        await ensure_async(self.start_kernel(**self._launch_args))

    restart_kernel = run_sync(_async_restart_kernel)

    @property
    def has_kernel(self) -> bool:
        """Has a kernel process been started that we are actively managing."""
        return self.provisioner is not None and self.provisioner.has_process

    async def _async_send_kernel_sigterm(self, restart: bool = False) -> None:
        """similar to _kill_kernel, but with sigterm (not sigkill), but do not block"""
        if self.has_kernel:
            assert self.provisioner is not None
            await self.provisioner.terminate(restart=restart)

    _send_kernel_sigterm = run_sync(_async_send_kernel_sigterm)

    async def _async_kill_kernel(self, restart: bool = False) -> None:
        """Kill the running kernel.

        This is a private method, callers should use shutdown_kernel(now=True).
        """
        if self.has_kernel:
            assert self.provisioner is not None
            await self.provisioner.kill(restart=restart)

            # Wait until the kernel terminates.
            try:
                await asyncio.wait_for(self._async_wait(), timeout=5.0)
            except asyncio.TimeoutError:
                # Wait timed out, just log warning but continue - not much more we can do.
                self.log.warning("Wait for final termination of kernel timed out - continuing...")
                pass
            else:
                # Process is no longer alive, wait and clear
                if self.has_kernel:
                    await self.provisioner.wait()

    _kill_kernel = run_sync(_async_kill_kernel)

    async def _async_interrupt_kernel(self) -> None:
        """Interrupts the kernel by sending it a signal.

        Unlike ``signal_kernel``, this operation is well supported on all
        platforms.
        """
        if self.has_kernel:
            assert self.kernel_spec is not None
            interrupt_mode = self.kernel_spec.interrupt_mode
            if interrupt_mode == "signal":
                await ensure_async(self.signal_kernel(signal.SIGINT))

            elif interrupt_mode == "message":
                msg = self.session.msg("interrupt_request", content={})
                self._connect_control_socket()
                self.session.send(self._control_socket, msg)
        else:
            raise RuntimeError("Cannot interrupt kernel. No kernel is running!")

    interrupt_kernel = run_sync(_async_interrupt_kernel)

    async def _async_signal_kernel(self, signum: int) -> None:
        """Sends a signal to the process group of the kernel (this
        usually includes the kernel and any subprocesses spawned by
        the kernel).

        Note that since only SIGTERM is supported on Windows, this function is
        only useful on Unix systems.
        """
        if self.has_kernel:
            assert self.provisioner is not None
            await self.provisioner.send_signal(signum)
        else:
            raise RuntimeError("Cannot signal kernel. No kernel is running!")

    signal_kernel = run_sync(_async_signal_kernel)

    async def _async_is_alive(self) -> bool:
        """Is the kernel process still running?"""
        if self.has_kernel:
            assert self.provisioner is not None
            ret = await self.provisioner.poll()
            if ret is None:
                return True
        return False

    is_alive = run_sync(_async_is_alive)

    async def _async_wait(self, pollinterval: float = 0.1) -> None:
        # Use busy loop at 100ms intervals, polling until the process is
        # not alive.  If we find the process is no longer alive, complete
        # its cleanup via the blocking wait().  Callers are responsible for
        # issuing calls to wait() using a timeout (see _kill_kernel()).
        while await ensure_async(self.is_alive()):
            await asyncio.sleep(pollinterval)


class AsyncKernelManager(KernelManager):
    # the class to create with our `client` method
    client_class: DottedObjectName = DottedObjectName(
        "jupyter_client.asynchronous.AsyncKernelClient"
    )
    client_factory: Type = Type(klass="jupyter_client.asynchronous.AsyncKernelClient")

    _launch_kernel = KernelManager._async_launch_kernel
    start_kernel = KernelManager._async_start_kernel
    pre_start_kernel = KernelManager._async_pre_start_kernel
    post_start_kernel = KernelManager._async_post_start_kernel
    request_shutdown = KernelManager._async_request_shutdown
    finish_shutdown = KernelManager._async_finish_shutdown
    cleanup_resources = KernelManager._async_cleanup_resources
    shutdown_kernel = KernelManager._async_shutdown_kernel
    restart_kernel = KernelManager._async_restart_kernel
    _send_kernel_sigterm = KernelManager._async_send_kernel_sigterm
    _kill_kernel = KernelManager._async_kill_kernel
    interrupt_kernel = KernelManager._async_interrupt_kernel
    signal_kernel = KernelManager._async_signal_kernel
    is_alive = KernelManager._async_is_alive


KernelManagerABC.register(KernelManager)


def start_new_kernel(
    startup_timeout: float = 60, kernel_name: str = "python", **kwargs: t.Any
) -> t.Tuple[KernelManager, KernelClient]:
    """Start a new kernel, and return its Manager and Client"""
    km = KernelManager(kernel_name=kernel_name)
    km.start_kernel(**kwargs)
    kc = km.client()
    kc.start_channels()
    try:
        kc.wait_for_ready(timeout=startup_timeout)
    except RuntimeError:
        kc.stop_channels()
        km.shutdown_kernel()
        raise

    return km, kc


async def start_new_async_kernel(
    startup_timeout: float = 60, kernel_name: str = "python", **kwargs: t.Any
) -> t.Tuple[AsyncKernelManager, KernelClient]:
    """Start a new kernel, and return its Manager and Client"""
    km = AsyncKernelManager(kernel_name=kernel_name)
    await km.start_kernel(**kwargs)
    kc = km.client()
    kc.start_channels()
    try:
        await kc.wait_for_ready(timeout=startup_timeout)
    except RuntimeError:
        kc.stop_channels()
        await km.shutdown_kernel()
        raise

    return (km, kc)


@contextmanager
def run_kernel(**kwargs: t.Any) -> t.Iterator[KernelClient]:
    """Context manager to create a kernel in a subprocess.

    The kernel is shut down when the context exits.

    Returns
    -------
    kernel_client: connected KernelClient instance
    """
    km, kc = start_new_kernel(**kwargs)
    try:
        yield kc
    finally:
        kc.stop_channels()
        km.shutdown_kernel(now=True)
