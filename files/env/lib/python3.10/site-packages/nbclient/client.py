import asyncio
import atexit
import base64
import collections
import datetime
import signal
import typing as t
from contextlib import asynccontextmanager, contextmanager
from queue import Empty
from textwrap import dedent
from time import monotonic
from typing import Optional

from jupyter_client import KernelManager
from jupyter_client.client import KernelClient
from nbformat import NotebookNode
from nbformat.v4 import output_from_msg
from traitlets import (
    Any,
    Bool,
    Callable,
    Dict,
    Enum,
    Integer,
    List,
    Type,
    Unicode,
    default,
)
from traitlets.config.configurable import LoggingConfigurable

from .exceptions import (
    CellControlSignal,
    CellExecutionComplete,
    CellExecutionError,
    CellTimeoutError,
    DeadKernelError,
)
from .output_widget import OutputWidget
from .util import ensure_async, run_hook, run_sync


def timestamp(msg: Optional[Dict] = None) -> str:
    if msg and 'header' in msg:  # The test mocks don't provide a header, so tolerate that
        msg_header = msg['header']
        if 'date' in msg_header and isinstance(msg_header['date'], datetime.datetime):
            try:
                # reformat datetime into expected format
                formatted_time = datetime.datetime.strftime(
                    msg_header['date'], '%Y-%m-%dT%H:%M:%S.%fZ'
                )
                if (
                    formatted_time
                ):  # docs indicate strftime may return empty string, so let's catch that too
                    return formatted_time
            except Exception:
                pass  # fallback to a local time

    return datetime.datetime.utcnow().isoformat() + 'Z'


class NotebookClient(LoggingConfigurable):
    """
    Encompasses a Client for executing cells in a notebook
    """

    timeout: int = Integer(
        None,
        allow_none=True,
        help=dedent(
            """
            The time to wait (in seconds) for output from executions.
            If a cell execution takes longer, a TimeoutError is raised.

            ``None`` or ``-1`` will disable the timeout. If ``timeout_func`` is set,
            it overrides ``timeout``.
            """
        ),
    ).tag(config=True)

    timeout_func: t.Any = Any(
        default_value=None,
        allow_none=True,
        help=dedent(
            """
            A callable which, when given the cell source as input,
            returns the time to wait (in seconds) for output from cell
            executions. If a cell execution takes longer, a TimeoutError
            is raised.

            Returning ``None`` or ``-1`` will disable the timeout for the cell.
            Not setting ``timeout_func`` will cause the client to
            default to using the ``timeout`` trait for all cells. The
            ``timeout_func`` trait overrides ``timeout`` if it is not ``None``.
            """
        ),
    ).tag(config=True)

    interrupt_on_timeout: bool = Bool(
        False,
        help=dedent(
            """
            If execution of a cell times out, interrupt the kernel and
            continue executing other cells rather than throwing an error and
            stopping.
            """
        ),
    ).tag(config=True)

    startup_timeout: int = Integer(
        60,
        help=dedent(
            """
            The time to wait (in seconds) for the kernel to start.
            If kernel startup takes longer, a RuntimeError is
            raised.
            """
        ),
    ).tag(config=True)

    allow_errors: bool = Bool(
        False,
        help=dedent(
            """
            If ``False`` (default), when a cell raises an error the
            execution is stopped and a `CellExecutionError`
            is raised, except if the error name is in
            ``allow_error_names``.
            If ``True``, execution errors are ignored and the execution
            is continued until the end of the notebook. Output from
            exceptions is included in the cell output in both cases.
            """
        ),
    ).tag(config=True)

    allow_error_names: t.List[str] = List(
        Unicode(),
        help=dedent(
            """
            List of error names which won't stop the execution. Use this if the
            ``allow_errors`` option it too general and you want to allow only
            specific kinds of errors.
            """
        ),
    ).tag(config=True)

    force_raise_errors: bool = Bool(
        False,
        help=dedent(
            """
            If False (default), errors from executing the notebook can be
            allowed with a ``raises-exception`` tag on a single cell, or the
            ``allow_errors`` or ``allow_error_names`` configurable options for
            all cells. An allowed error will be recorded in notebook output, and
            execution will continue. If an error occurs when it is not
            explicitly allowed, a `CellExecutionError` will be raised.
            If True, `CellExecutionError` will be raised for any error that occurs
            while executing the notebook. This overrides the ``allow_errors``
            and ``allow_error_names`` options and the ``raises-exception`` cell
            tag.
            """
        ),
    ).tag(config=True)

    skip_cells_with_tag: str = Unicode(
        'skip-execution',
        help=dedent(
            """
            Name of the cell tag to use to denote a cell that should be skipped.
            """
        ),
    ).tag(config=True)

    extra_arguments: t.List = List(Unicode()).tag(config=True)

    kernel_name: str = Unicode(
        '',
        help=dedent(
            """
            Name of kernel to use to execute the cells.
            If not set, use the kernel_spec embedded in the notebook.
            """
        ),
    ).tag(config=True)

    raise_on_iopub_timeout: bool = Bool(
        False,
        help=dedent(
            """
            If ``False`` (default), then the kernel will continue waiting for
            iopub messages until it receives a kernel idle message, or until a
            timeout occurs, at which point the currently executing cell will be
            skipped. If ``True``, then an error will be raised after the first
            timeout. This option generally does not need to be used, but may be
            useful in contexts where there is the possibility of executing
            notebooks with memory-consuming infinite loops.
            """
        ),
    ).tag(config=True)

    store_widget_state: bool = Bool(
        True,
        help=dedent(
            """
            If ``True`` (default), then the state of the Jupyter widgets created
            at the kernel will be stored in the metadata of the notebook.
            """
        ),
    ).tag(config=True)

    record_timing: bool = Bool(
        True,
        help=dedent(
            """
            If ``True`` (default), then the execution timings of each cell will
            be stored in the metadata of the notebook.
            """
        ),
    ).tag(config=True)

    iopub_timeout: int = Integer(
        4,
        allow_none=False,
        help=dedent(
            """
            The time to wait (in seconds) for IOPub output. This generally
            doesn't need to be set, but on some slow networks (such as CI
            systems) the default timeout might not be long enough to get all
            messages.
            """
        ),
    ).tag(config=True)

    shell_timeout_interval: int = Integer(
        5,
        allow_none=False,
        help=dedent(
            """
            The time to wait (in seconds) for Shell output before retrying.
            This generally doesn't need to be set, but if one needs to check
            for dead kernels at a faster rate this can help.
            """
        ),
    ).tag(config=True)

    shutdown_kernel = Enum(
        ['graceful', 'immediate'],
        default_value='graceful',
        help=dedent(
            """
            If ``graceful`` (default), then the kernel is given time to clean
            up after executing all cells, e.g., to execute its ``atexit`` hooks.
            If ``immediate``, then the kernel is signaled to immediately
            terminate.
            """
        ),
    ).tag(config=True)

    ipython_hist_file: str = Unicode(
        default_value=':memory:',
        help="""Path to file to use for SQLite history database for an IPython kernel.

        The specific value ``:memory:`` (including the colon
        at both end but not the back ticks), avoids creating a history file. Otherwise, IPython
        will create a history file for each kernel.

        When running kernels simultaneously (e.g. via multiprocessing) saving history a single
        SQLite file can result in database errors, so using ``:memory:`` is recommended in
        non-interactive contexts.
        """,
    ).tag(config=True)

    kernel_manager_class: KernelManager = Type(config=True, help='The kernel manager class to use.')

    on_notebook_start: t.Optional[t.Callable] = Callable(
        default_value=None,
        allow_none=True,
        help=dedent(
            """
            A callable which executes after the kernel manager and kernel client are setup, and
            cells are about to execute.
            Called with kwargs `notebook`.
            """
        ),
    ).tag(config=True)

    on_notebook_complete: t.Optional[t.Callable] = Callable(
        default_value=None,
        allow_none=True,
        help=dedent(
            """
            A callable which executes after the kernel is cleaned up.
            Called with kwargs `notebook`.
            """
        ),
    ).tag(config=True)

    on_notebook_error: t.Optional[t.Callable] = Callable(
        default_value=None,
        allow_none=True,
        help=dedent(
            """
            A callable which executes when the notebook encounters an error.
            Called with kwargs `notebook`.
            """
        ),
    ).tag(config=True)

    on_cell_start: t.Optional[t.Callable] = Callable(
        default_value=None,
        allow_none=True,
        help=dedent(
            """
            A callable which executes before a cell is executed and before non-executing cells
            are skipped.
            Called with kwargs `cell` and `cell_index`.
            """
        ),
    ).tag(config=True)

    on_cell_execute: t.Optional[t.Callable] = Callable(
        default_value=None,
        allow_none=True,
        help=dedent(
            """
            A callable which executes just before a code cell is executed.
            Called with kwargs `cell` and `cell_index`.
            """
        ),
    ).tag(config=True)

    on_cell_complete: t.Optional[t.Callable] = Callable(
        default_value=None,
        allow_none=True,
        help=dedent(
            """
            A callable which executes after a cell execution is complete. It is
            called even when a cell results in a failure.
            Called with kwargs `cell` and `cell_index`.
            """
        ),
    ).tag(config=True)

    on_cell_error: t.Optional[t.Callable] = Callable(
        default_value=None,
        allow_none=True,
        help=dedent(
            """
            A callable which executes when a cell execution results in an error.
            This is executed even if errors are suppressed with `cell_allows_errors`.
            Called with kwargs `cell` and `cell_index`.
            """
        ),
    ).tag(config=True)

    @default('kernel_manager_class')
    def _kernel_manager_class_default(self) -> KernelManager:
        """Use a dynamic default to avoid importing jupyter_client at startup"""
        from jupyter_client import AsyncKernelManager

        return AsyncKernelManager

    _display_id_map: t.Dict[str, t.Dict] = Dict(
        help=dedent(
            """
              mapping of locations of outputs with a given display_id
              tracks cell index and output index within cell.outputs for
              each appearance of the display_id
              {
                   'display_id': {
                  cell_idx: [output_idx,]
                   }
              }
              """
        )
    )

    display_data_priority: t.List = List(
        [
            'text/html',
            'application/pdf',
            'text/latex',
            'image/svg+xml',
            'image/png',
            'image/jpeg',
            'text/markdown',
            'text/plain',
        ],
        help="""
            An ordered list of preferred output type, the first
            encountered will usually be used when converting discarding
            the others.
            """,
    ).tag(config=True)

    resources: t.Dict = Dict(
        help=dedent(
            """
            Additional resources used in the conversion process. For example,
            passing ``{'metadata': {'path': run_path}}`` sets the
            execution path to ``run_path``.
            """
        )
    )

    def __init__(self, nb: NotebookNode, km: t.Optional[KernelManager] = None, **kw) -> None:
        """Initializes the execution manager.

        Parameters
        ----------
        nb : NotebookNode
            Notebook being executed.
        km : KernelManager (optional)
            Optional kernel manager. If none is provided, a kernel manager will
            be created.
        """
        super().__init__(**kw)
        self.nb: NotebookNode = nb
        self.km: t.Optional[KernelManager] = km
        self.owns_km: bool = km is None  # whether the NotebookClient owns the kernel manager
        self.kc: t.Optional[KernelClient] = None
        self.reset_execution_trackers()
        self.widget_registry: t.Dict[str, t.Dict] = {
            '@jupyter-widgets/output': {'OutputModel': OutputWidget}
        }
        # comm_open_handlers should return an object with a .handle_msg(msg) method or None
        self.comm_open_handlers: t.Dict[str, t.Any] = {
            'jupyter.widget': self.on_comm_open_jupyter_widget
        }

    def reset_execution_trackers(self) -> None:
        """Resets any per-execution trackers."""
        self.task_poll_for_reply: t.Optional[asyncio.Future] = None
        self.code_cells_executed = 0
        self._display_id_map = {}
        self.widget_state: t.Dict[str, t.Dict] = {}
        self.widget_buffers: t.Dict[str, t.Dict[t.Tuple[str, ...], t.Dict[str, str]]] = {}
        # maps to list of hooks, where the last is used, this is used
        # to support nested use of output widgets.
        self.output_hook_stack: t.Any = collections.defaultdict(list)
        # our front-end mimicking Output widgets
        self.comm_objects: t.Dict[str, t.Any] = {}

    def create_kernel_manager(self) -> KernelManager:
        """Creates a new kernel manager.

        Returns
        -------
        km : KernelManager
            Kernel manager whose client class is asynchronous.
        """
        if not self.kernel_name:
            kn = self.nb.metadata.get('kernelspec', {}).get('name')
            if kn is not None:
                self.kernel_name = kn

        if not self.kernel_name:
            self.km = self.kernel_manager_class(config=self.config)
        else:
            self.km = self.kernel_manager_class(kernel_name=self.kernel_name, config=self.config)

        # If the current kernel manager is still using the default (synchronous) KernelClient class,
        # switch to the async version since that's what NBClient prefers.
        if self.km.client_class == 'jupyter_client.client.KernelClient':
            self.km.client_class = 'jupyter_client.asynchronous.AsyncKernelClient'

        return self.km

    async def _async_cleanup_kernel(self) -> None:
        assert self.km is not None
        now = self.shutdown_kernel == "immediate"
        try:
            # Queue the manager to kill the process, and recover gracefully if it's already dead.
            if await ensure_async(self.km.is_alive()):
                await ensure_async(self.km.shutdown_kernel(now=now))
        except RuntimeError as e:
            # The error isn't specialized, so we have to check the message
            if 'No kernel is running!' not in str(e):
                raise
        finally:
            # Remove any state left over even if we failed to stop the kernel
            await ensure_async(self.km.cleanup_resources())
            if getattr(self, "kc") and self.kc is not None:
                await ensure_async(self.kc.stop_channels())
                self.kc = None
                self.km = None

    _cleanup_kernel = run_sync(_async_cleanup_kernel)

    async def async_start_new_kernel(self, **kwargs) -> None:
        """Creates a new kernel.

        Parameters
        ----------
        kwargs :
            Any options for ``self.kernel_manager_class.start_kernel()``. Because
            that defaults to AsyncKernelManager, this will likely include options
            accepted by ``AsyncKernelManager.start_kernel()``, which includes ``cwd``.
        """
        assert self.km is not None
        resource_path = self.resources.get('metadata', {}).get('path') or None
        if resource_path and 'cwd' not in kwargs:
            kwargs["cwd"] = resource_path

        has_history_manager_arg = any(
            arg.startswith('--HistoryManager.hist_file') for arg in self.extra_arguments
        )
        if (
            hasattr(self.km, 'ipykernel')
            and self.km.ipykernel
            and self.ipython_hist_file
            and not has_history_manager_arg
        ):
            self.extra_arguments += [f'--HistoryManager.hist_file={self.ipython_hist_file}']

        await ensure_async(self.km.start_kernel(extra_arguments=self.extra_arguments, **kwargs))

    start_new_kernel = run_sync(async_start_new_kernel)

    async def async_start_new_kernel_client(self) -> KernelClient:
        """Creates a new kernel client.

        Returns
        -------
        kc : KernelClient
            Kernel client as created by the kernel manager ``km``.
        """
        assert self.km is not None
        self.kc = self.km.client()
        await ensure_async(self.kc.start_channels())
        try:
            await ensure_async(self.kc.wait_for_ready(timeout=self.startup_timeout))
        except RuntimeError:
            await self._async_cleanup_kernel()
            raise
        self.kc.allow_stdin = False
        await run_hook(self.on_notebook_start, notebook=self.nb)
        return self.kc

    start_new_kernel_client = run_sync(async_start_new_kernel_client)

    @contextmanager
    def setup_kernel(self, **kwargs) -> t.Generator:
        """
        Context manager for setting up the kernel to execute a notebook.

        The assigns the Kernel Manager (``self.km``) if missing and Kernel Client(``self.kc``).

        When control returns from the yield it stops the client's zmq channels, and shuts
        down the kernel.
        """
        # by default, cleanup the kernel client if we own the kernel manager
        # and keep it alive if we don't
        cleanup_kc = kwargs.pop('cleanup_kc', self.owns_km)

        # Can't use run_until_complete on an asynccontextmanager function :(
        if self.km is None:
            self.km = self.create_kernel_manager()

        if not self.km.has_kernel:
            self.start_new_kernel(**kwargs)
            self.start_new_kernel_client()
        try:
            yield
        finally:
            if cleanup_kc:
                self._cleanup_kernel()

    @asynccontextmanager
    async def async_setup_kernel(self, **kwargs) -> t.AsyncGenerator:
        """
        Context manager for setting up the kernel to execute a notebook.

        This assigns the Kernel Manager (``self.km``) if missing and Kernel Client(``self.kc``).

        When control returns from the yield it stops the client's zmq channels, and shuts
        down the kernel.

        Handlers for SIGINT and SIGTERM are also added to cleanup in case of unexpected shutdown.
        """
        # by default, cleanup the kernel client if we own the kernel manager
        # and keep it alive if we don't
        cleanup_kc = kwargs.pop('cleanup_kc', self.owns_km)
        if self.km is None:
            self.km = self.create_kernel_manager()

        # self._cleanup_kernel uses run_async, which ensures the ioloop is running again.
        # This is necessary as the ioloop has stopped once atexit fires.
        atexit.register(self._cleanup_kernel)

        def on_signal():
            asyncio.ensure_future(self._async_cleanup_kernel())
            atexit.unregister(self._cleanup_kernel)

        loop = asyncio.get_event_loop()
        try:
            loop.add_signal_handler(signal.SIGINT, on_signal)
            loop.add_signal_handler(signal.SIGTERM, on_signal)
        except (NotImplementedError, RuntimeError):
            # NotImplementedError: Windows does not support signals.
            # RuntimeError: Raised when add_signal_handler is called outside the main thread
            pass

        if not self.km.has_kernel:
            await self.async_start_new_kernel(**kwargs)
            await self.async_start_new_kernel_client()
        try:
            yield
        except RuntimeError as e:
            await run_hook(self.on_notebook_error, notebook=self.nb)
            raise e
        finally:
            if cleanup_kc:
                await self._async_cleanup_kernel()
            await run_hook(self.on_notebook_complete, notebook=self.nb)
            atexit.unregister(self._cleanup_kernel)
            try:
                loop.remove_signal_handler(signal.SIGINT)
                loop.remove_signal_handler(signal.SIGTERM)
            except (NotImplementedError, RuntimeError):
                pass

    async def async_execute(self, reset_kc: bool = False, **kwargs) -> NotebookNode:
        """
        Executes each code cell.

        Parameters
        ----------
        kwargs :
            Any option for ``self.kernel_manager_class.start_kernel()``. Because
            that defaults to AsyncKernelManager, this will likely include options
            accepted by ``jupyter_client.AsyncKernelManager.start_kernel()``,
            which includes ``cwd``.

            ``reset_kc`` if True, the kernel client will be reset and a new one
            will be created (default: False).

        Returns
        -------
        nb : NotebookNode
            The executed notebook.
        """
        if reset_kc and self.owns_km:
            await self._async_cleanup_kernel()
        self.reset_execution_trackers()

        async with self.async_setup_kernel(**kwargs):
            assert self.kc is not None
            self.log.info("Executing notebook with kernel: %s" % self.kernel_name)
            msg_id = await ensure_async(self.kc.kernel_info())
            info_msg = await self.async_wait_for_reply(msg_id)
            if info_msg is not None:
                if 'language_info' in info_msg['content']:
                    self.nb.metadata['language_info'] = info_msg['content']['language_info']
                else:
                    raise RuntimeError(
                        'Kernel info received message content has no "language_info" key. '
                        'Content is:\n' + str(info_msg['content'])
                    )
            for index, cell in enumerate(self.nb.cells):
                # Ignore `'execution_count' in content` as it's always 1
                # when store_history is False
                await self.async_execute_cell(
                    cell, index, execution_count=self.code_cells_executed + 1
                )
            self.set_widgets_metadata()

        return self.nb

    execute = run_sync(async_execute)

    def set_widgets_metadata(self) -> None:
        if self.widget_state:
            self.nb.metadata.widgets = {
                'application/vnd.jupyter.widget-state+json': {
                    'state': {
                        model_id: self._serialize_widget_state(state)
                        for model_id, state in self.widget_state.items()
                        if '_model_name' in state
                    },
                    'version_major': 2,
                    'version_minor': 0,
                }
            }
            for key, widget in self.nb.metadata.widgets[
                'application/vnd.jupyter.widget-state+json'
            ]['state'].items():
                buffers = self.widget_buffers.get(key)
                if buffers:
                    widget['buffers'] = list(buffers.values())

    def _update_display_id(self, display_id: str, msg: t.Dict) -> None:
        """Update outputs with a given display_id"""
        if display_id not in self._display_id_map:
            self.log.debug("display id %r not in %s", display_id, self._display_id_map)
            return

        if msg['header']['msg_type'] == 'update_display_data':
            msg['header']['msg_type'] = 'display_data'

        try:
            out = output_from_msg(msg)
        except ValueError:
            self.log.error("unhandled iopub msg: " + msg['msg_type'])
            return

        for cell_idx, output_indices in self._display_id_map[display_id].items():
            cell = self.nb['cells'][cell_idx]
            outputs = cell['outputs']
            for output_idx in output_indices:
                outputs[output_idx]['data'] = out['data']
                outputs[output_idx]['metadata'] = out['metadata']

    async def _async_poll_for_reply(
        self,
        msg_id: str,
        cell: NotebookNode,
        timeout: t.Optional[int],
        task_poll_output_msg: asyncio.Future,
        task_poll_kernel_alive: asyncio.Future,
    ) -> t.Dict:

        assert self.kc is not None
        new_timeout: t.Optional[float] = None
        if timeout is not None:
            deadline = monotonic() + timeout
            new_timeout = float(timeout)
        while True:
            try:
                msg = await ensure_async(self.kc.shell_channel.get_msg(timeout=new_timeout))
                if msg['parent_header'].get('msg_id') == msg_id:
                    if self.record_timing:
                        cell['metadata']['execution']['shell.execute_reply'] = timestamp(msg)
                    try:
                        await asyncio.wait_for(task_poll_output_msg, self.iopub_timeout)
                    except (asyncio.TimeoutError, Empty):
                        if self.raise_on_iopub_timeout:
                            task_poll_kernel_alive.cancel()
                            raise CellTimeoutError.error_from_timeout_and_cell(
                                "Timeout waiting for IOPub output", self.iopub_timeout, cell
                            )
                        else:
                            self.log.warning("Timeout waiting for IOPub output")
                    task_poll_kernel_alive.cancel()
                    return msg
                else:
                    if new_timeout is not None:
                        new_timeout = max(0, deadline - monotonic())
            except Empty:
                # received no message, check if kernel is still alive
                assert timeout is not None
                task_poll_kernel_alive.cancel()
                await self._async_check_alive()
                await self._async_handle_timeout(timeout, cell)

    async def _async_poll_output_msg(
        self, parent_msg_id: str, cell: NotebookNode, cell_index: int
    ) -> None:

        assert self.kc is not None
        while True:
            msg = await ensure_async(self.kc.iopub_channel.get_msg(timeout=None))
            if msg['parent_header'].get('msg_id') == parent_msg_id:
                try:
                    # Will raise CellExecutionComplete when completed
                    self.process_message(msg, cell, cell_index)
                except CellExecutionComplete:
                    return

    async def _async_poll_kernel_alive(self) -> None:
        while True:
            await asyncio.sleep(1)
            try:
                await self._async_check_alive()
            except DeadKernelError:
                assert self.task_poll_for_reply is not None
                self.task_poll_for_reply.cancel()
                return

    def _get_timeout(self, cell: t.Optional[NotebookNode]) -> int:
        if self.timeout_func is not None and cell is not None:
            timeout = self.timeout_func(cell)
        else:
            timeout = self.timeout

        if not timeout or timeout < 0:
            timeout = None

        return timeout

    async def _async_handle_timeout(
        self, timeout: int, cell: t.Optional[NotebookNode] = None
    ) -> None:

        self.log.error("Timeout waiting for execute reply (%is)." % timeout)
        if self.interrupt_on_timeout:
            self.log.error("Interrupting kernel")
            assert self.km is not None
            await ensure_async(self.km.interrupt_kernel())
        else:
            raise CellTimeoutError.error_from_timeout_and_cell(
                "Cell execution timed out", timeout, cell
            )

    async def _async_check_alive(self) -> None:
        assert self.kc is not None
        if not await ensure_async(self.kc.is_alive()):
            self.log.error("Kernel died while waiting for execute reply.")
            raise DeadKernelError("Kernel died")

    async def async_wait_for_reply(
        self, msg_id: str, cell: t.Optional[NotebookNode] = None
    ) -> t.Optional[t.Dict]:

        assert self.kc is not None
        # wait for finish, with timeout
        timeout = self._get_timeout(cell)
        cummulative_time = 0
        while True:
            try:
                msg = await ensure_async(
                    self.kc.shell_channel.get_msg(timeout=self.shell_timeout_interval)
                )
            except Empty:
                await self._async_check_alive()
                cummulative_time += self.shell_timeout_interval
                if timeout and cummulative_time > timeout:
                    await self._async_async_handle_timeout(timeout, cell)
                    break
            else:
                if msg['parent_header'].get('msg_id') == msg_id:
                    return msg
        return None

    wait_for_reply = run_sync(async_wait_for_reply)
    # Backwards compatibility naming for papermill
    _wait_for_reply = wait_for_reply

    def _passed_deadline(self, deadline: int) -> bool:
        if deadline is not None and deadline - monotonic() <= 0:
            return True
        return False

    async def _check_raise_for_error(
        self, cell: NotebookNode, cell_index: int, exec_reply: t.Optional[t.Dict]
    ) -> None:

        if exec_reply is None:
            return None

        exec_reply_content = exec_reply['content']
        if exec_reply_content['status'] != 'error':
            return None

        cell_allows_errors = (not self.force_raise_errors) and (
            self.allow_errors
            or exec_reply_content.get('ename') in self.allow_error_names
            or "raises-exception" in cell.metadata.get("tags", [])
        )
        await run_hook(self.on_cell_error, cell=cell, cell_index=cell_index)
        if not cell_allows_errors:
            raise CellExecutionError.from_cell_and_msg(cell, exec_reply_content)

    async def async_execute_cell(
        self,
        cell: NotebookNode,
        cell_index: int,
        execution_count: t.Optional[int] = None,
        store_history: bool = True,
    ) -> NotebookNode:
        """
        Executes a single code cell.

        To execute all cells see :meth:`execute`.

        Parameters
        ----------
        cell : nbformat.NotebookNode
            The cell which is currently being processed.
        cell_index : int
            The position of the cell within the notebook object.
        execution_count : int
            The execution count to be assigned to the cell (default: Use kernel response)
        store_history : bool
            Determines if history should be stored in the kernel (default: False).
            Specific to ipython kernels, which can store command histories.

        Returns
        -------
        output : dict
            The execution output payload (or None for no output).

        Raises
        ------
        CellExecutionError
            If execution failed and should raise an exception, this will be raised
            with defaults about the failure.

        Returns
        -------
        cell : NotebookNode
            The cell which was just processed.
        """
        assert self.kc is not None

        await run_hook(self.on_cell_start, cell=cell, cell_index=cell_index)

        if cell.cell_type != 'code' or not cell.source.strip():
            self.log.debug("Skipping non-executing cell %s", cell_index)
            return cell

        if self.skip_cells_with_tag in cell.metadata.get("tags", []):
            self.log.debug("Skipping tagged cell %s", cell_index)
            return cell

        if self.record_timing:  # clear execution metadata prior to execution
            cell['metadata']['execution'] = {}

        self.log.debug("Executing cell:\n%s", cell.source)

        cell_allows_errors = (not self.force_raise_errors) and (
            self.allow_errors or "raises-exception" in cell.metadata.get("tags", [])
        )

        await run_hook(self.on_cell_execute, cell=cell, cell_index=cell_index)
        parent_msg_id = await ensure_async(
            self.kc.execute(
                cell.source, store_history=store_history, stop_on_error=not cell_allows_errors
            )
        )
        await run_hook(self.on_cell_complete, cell=cell, cell_index=cell_index)
        # We launched a code cell to execute
        self.code_cells_executed += 1
        exec_timeout = self._get_timeout(cell)

        cell.outputs = []
        self.clear_before_next_output = False

        task_poll_kernel_alive = asyncio.ensure_future(self._async_poll_kernel_alive())
        task_poll_output_msg = asyncio.ensure_future(
            self._async_poll_output_msg(parent_msg_id, cell, cell_index)
        )
        self.task_poll_for_reply = asyncio.ensure_future(
            self._async_poll_for_reply(
                parent_msg_id, cell, exec_timeout, task_poll_output_msg, task_poll_kernel_alive
            )
        )
        try:
            exec_reply = await self.task_poll_for_reply
        except asyncio.CancelledError:
            # can only be cancelled by task_poll_kernel_alive when the kernel is dead
            task_poll_output_msg.cancel()
            raise DeadKernelError("Kernel died")
        except Exception as e:
            # Best effort to cancel request if it hasn't been resolved
            try:
                # Check if the task_poll_output is doing the raising for us
                if not isinstance(e, CellControlSignal):
                    task_poll_output_msg.cancel()
            finally:
                raise

        if execution_count:
            cell['execution_count'] = execution_count
        await self._check_raise_for_error(cell, cell_index, exec_reply)
        self.nb['cells'][cell_index] = cell
        return cell

    execute_cell = run_sync(async_execute_cell)

    def process_message(
        self, msg: t.Dict, cell: NotebookNode, cell_index: int
    ) -> t.Optional[t.List]:
        """
        Processes a kernel message, updates cell state, and returns the
        resulting output object that was appended to cell.outputs.

        The input argument *cell* is modified in-place.

        Parameters
        ----------
        msg : dict
            The kernel message being processed.
        cell : nbformat.NotebookNode
            The cell which is currently being processed.
        cell_index : int
            The position of the cell within the notebook object.

        Returns
        -------
        output : dict
            The execution output payload (or None for no output).

        Raises
        ------
        CellExecutionComplete
          Once a message arrives which indicates computation completeness.

        """
        msg_type = msg['msg_type']
        self.log.debug("msg_type: %s", msg_type)
        content = msg['content']
        self.log.debug("content: %s", content)

        display_id = content.get('transient', {}).get('display_id', None)
        if display_id and msg_type in {'execute_result', 'display_data', 'update_display_data'}:
            self._update_display_id(display_id, msg)

        # set the prompt number for the input and the output
        if 'execution_count' in content:
            cell['execution_count'] = content['execution_count']

        if self.record_timing:
            if msg_type == 'status':
                if content['execution_state'] == 'idle':
                    cell['metadata']['execution']['iopub.status.idle'] = timestamp(msg)
                elif content['execution_state'] == 'busy':
                    cell['metadata']['execution']['iopub.status.busy'] = timestamp(msg)
            elif msg_type == 'execute_input':
                cell['metadata']['execution']['iopub.execute_input'] = timestamp(msg)

        if msg_type == 'status':
            if content['execution_state'] == 'idle':
                raise CellExecutionComplete()
        elif msg_type == 'clear_output':
            self.clear_output(cell.outputs, msg, cell_index)
        elif msg_type.startswith('comm'):
            self.handle_comm_msg(cell.outputs, msg, cell_index)
        # Check for remaining messages we don't process
        elif msg_type not in ['execute_input', 'update_display_data']:
            # Assign output as our processed "result"
            return self.output(cell.outputs, msg, display_id, cell_index)
        return None

    def output(
        self, outs: t.List, msg: t.Dict, display_id: str, cell_index: int
    ) -> t.Optional[t.List]:

        msg_type = msg['msg_type']

        parent_msg_id = msg['parent_header'].get('msg_id')
        if self.output_hook_stack[parent_msg_id]:
            # if we have a hook registered, it will override our
            # default output behaviour (e.g. OutputWidget)
            hook = self.output_hook_stack[parent_msg_id][-1]
            hook.output(outs, msg, display_id, cell_index)
            return None

        try:
            out = output_from_msg(msg)
        except ValueError:
            self.log.error("unhandled iopub msg: " + msg_type)
            return None

        if self.clear_before_next_output:
            self.log.debug('Executing delayed clear_output')
            outs[:] = []
            self.clear_display_id_mapping(cell_index)
            self.clear_before_next_output = False

        if display_id:
            # record output index in:
            #   _display_id_map[display_id][cell_idx]
            cell_map = self._display_id_map.setdefault(display_id, {})
            output_idx_list = cell_map.setdefault(cell_index, [])
            output_idx_list.append(len(outs))

        outs.append(out)

        return out

    def clear_output(self, outs: t.List, msg: t.Dict, cell_index: int) -> None:

        content = msg['content']

        parent_msg_id = msg['parent_header'].get('msg_id')
        if self.output_hook_stack[parent_msg_id]:
            # if we have a hook registered, it will override our
            # default clear_output behaviour (e.g. OutputWidget)
            hook = self.output_hook_stack[parent_msg_id][-1]
            hook.clear_output(outs, msg, cell_index)
            return

        if content.get('wait'):
            self.log.debug('Wait to clear output')
            self.clear_before_next_output = True
        else:
            self.log.debug('Immediate clear output')
            outs[:] = []
            self.clear_display_id_mapping(cell_index)

    def clear_display_id_mapping(self, cell_index: int) -> None:

        for display_id, cell_map in self._display_id_map.items():
            if cell_index in cell_map:
                cell_map[cell_index] = []

    def handle_comm_msg(self, outs: t.List, msg: t.Dict, cell_index: int) -> None:

        content = msg['content']
        data = content['data']
        if self.store_widget_state and 'state' in data:  # ignore custom msg'es
            self.widget_state.setdefault(content['comm_id'], {}).update(data['state'])
            if 'buffer_paths' in data and data['buffer_paths']:
                comm_id = content['comm_id']
                if comm_id not in self.widget_buffers:
                    self.widget_buffers[comm_id] = {}
                # for each comm, the path uniquely identifies a buffer
                new_buffers: t.Dict[t.Tuple[str, ...], t.Dict[str, str]] = {
                    tuple(k["path"]): k for k in self._get_buffer_data(msg)
                }
                self.widget_buffers[comm_id].update(new_buffers)
        # There are cases where we need to mimic a frontend, to get similar behaviour as
        # when using the Output widget from Jupyter lab/notebook
        if msg['msg_type'] == 'comm_open':
            target = msg['content'].get('target_name')
            handler = self.comm_open_handlers.get(target)
            if handler:
                comm_id = msg['content']['comm_id']
                comm_object = handler(msg)
                if comm_object:
                    self.comm_objects[comm_id] = comm_object
            else:
                self.log.warning(f'No handler found for comm target {target!r}')
        elif msg['msg_type'] == 'comm_msg':
            content = msg['content']
            comm_id = msg['content']['comm_id']
            if comm_id in self.comm_objects:
                self.comm_objects[comm_id].handle_msg(msg)

    def _serialize_widget_state(self, state: t.Dict) -> t.Dict[str, t.Any]:
        """Serialize a widget state, following format in @jupyter-widgets/schema."""
        return {
            'model_name': state.get('_model_name'),
            'model_module': state.get('_model_module'),
            'model_module_version': state.get('_model_module_version'),
            'state': state,
        }

    def _get_buffer_data(self, msg: t.Dict) -> t.List[t.Dict[str, str]]:
        encoded_buffers = []
        paths = msg['content']['data']['buffer_paths']
        buffers = msg['buffers']
        for path, buffer in zip(paths, buffers):
            encoded_buffers.append(
                {
                    'data': base64.b64encode(buffer).decode('utf-8'),
                    'encoding': 'base64',
                    'path': path,
                }
            )
        return encoded_buffers

    def register_output_hook(self, msg_id: str, hook: OutputWidget) -> None:
        """Registers an override object that handles output/clear_output instead.

        Multiple hooks can be registered, where the last one will be used (stack based)
        """
        # mimics
        # https://jupyterlab.github.io/jupyterlab/services/interfaces/kernel.ikernelconnection.html#registermessagehook
        self.output_hook_stack[msg_id].append(hook)

    def remove_output_hook(self, msg_id: str, hook: OutputWidget) -> None:
        """Unregisters an override object that handles output/clear_output instead"""
        # mimics
        # https://jupyterlab.github.io/jupyterlab/services/interfaces/kernel.ikernelconnection.html#removemessagehook
        removed_hook = self.output_hook_stack[msg_id].pop()
        assert removed_hook == hook

    def on_comm_open_jupyter_widget(self, msg: t.Dict):
        content = msg['content']
        data = content['data']
        state = data['state']
        comm_id = msg['content']['comm_id']
        module = self.widget_registry.get(state['_model_module'])
        if module:
            widget_class = module.get(state['_model_name'])
            if widget_class:
                return widget_class(comm_id, state, self.kc, self)


def execute(
    nb: NotebookNode, cwd: t.Optional[str] = None, km: t.Optional[KernelManager] = None, **kwargs
) -> NotebookClient:
    """Execute a notebook's code, updating outputs within the notebook object.

    This is a convenient wrapper around NotebookClient. It returns the
    modified notebook object.

    Parameters
    ----------
    nb : NotebookNode
      The notebook object to be executed
    cwd : str, optional
      If supplied, the kernel will run in this directory
    km : AsyncKernelManager, optional
      If supplied, the specified kernel manager will be used for code execution.
    kwargs :
      Any other options for NotebookClient, e.g. timeout, kernel_name
    """
    resources = {}
    if cwd is not None:
        resources['metadata'] = {'path': cwd}
    return NotebookClient(nb=nb, resources=resources, km=km, **kwargs).execute()
