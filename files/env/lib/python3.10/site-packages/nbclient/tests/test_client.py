import asyncio
import concurrent.futures
import copy
import datetime
import functools
import os
import re
import threading
import warnings
from base64 import b64decode, b64encode
from queue import Empty
from unittest.mock import MagicMock, Mock

import nbformat
import pytest
import xmltodict  # type: ignore
from jupyter_client import KernelManager
from jupyter_client.kernelspec import KernelSpecManager
from nbconvert.filters import strip_ansi  # type: ignore
from nbformat import NotebookNode
from testpath import modified_env  # type: ignore
from traitlets import TraitError

from .. import NotebookClient, execute
from ..exceptions import CellExecutionError
from .base import NBClientTestsBase

addr_pat = re.compile(r'0x[0-9a-f]{7,9}')
current_dir = os.path.dirname(__file__)
ipython_input_pat = re.compile(
    r'(<ipython-input-\d+-[0-9a-f]+>|<IPY-INPUT>) in (<module>|<cell line: \d>\(\))'
)
# Tracebacks look different in IPython 8,
# see: https://github.com/ipython/ipython/blob/master/docs/source/whatsnew/version8.rst#traceback-improvements  # noqa
ipython8_input_pat = re.compile(
    r'(Input In \[\d+\]|<IPY-INPUT>), in (<module>|<cell line: \d>\(\))'
)

hook_methods = [
    "on_cell_start",
    "on_cell_execute",
    "on_cell_complete",
    "on_cell_error",
    "on_notebook_start",
    "on_notebook_complete",
    "on_notebook_error",
]


class AsyncMock(Mock):
    pass


def make_async(mock_value):
    async def _():
        return mock_value

    return _()


def normalize_base64(b64_text):
    # if it's base64, pass it through b64 decode/encode to avoid
    # equivalent values from being considered unequal
    try:
        return b64encode(b64decode(b64_text.encode('ascii'))).decode('ascii')
    except (ValueError, TypeError):
        return b64_text


def run_notebook(filename, opts, resources=None):
    """Loads and runs a notebook, returning both the version prior to
    running it and the version after running it.

    """
    with open(filename) as f:
        input_nb = nbformat.read(f, 4)

    cleaned_input_nb = copy.deepcopy(input_nb)
    for cell in cleaned_input_nb.cells:
        if 'execution_count' in cell:
            del cell['execution_count']
        cell['outputs'] = []

    if resources:
        opts = {'resources': resources, **opts}
    executor = NotebookClient(cleaned_input_nb, **opts)

    with warnings.catch_warnings():
        # suppress warning from jupyter_client's deprecated cleanup()
        warnings.simplefilter(action='ignore', category=FutureWarning)
        # Override terminal size to standardise traceback format
        with modified_env({'COLUMNS': '80', 'LINES': '24'}):
            output_nb = executor.execute()

    return input_nb, output_nb


def run_notebook_wrapper(args):
    # since concurrent.futures.ProcessPoolExecutor doesn't have starmap,
    # we need to unpack the arguments
    return run_notebook(*args)


async def async_run_notebook(filename, opts, resources=None):
    """Loads and runs a notebook, returning both the version prior to
    running it and the version after running it.

    """
    with open(filename) as f:
        input_nb = nbformat.read(f, 4)

    cleaned_input_nb = copy.deepcopy(input_nb)
    for cell in cleaned_input_nb.cells:
        if 'execution_count' in cell:
            del cell['execution_count']
        cell['outputs'] = []

    if resources:
        opts = {'resources': resources, **opts}
    executor = NotebookClient(cleaned_input_nb, **opts)

    # Override terminal size to standardise traceback format
    with modified_env({'COLUMNS': '80', 'LINES': '24'}):
        output_nb = await executor.async_execute()

    return input_nb, output_nb


def prepare_cell_mocks(*messages, reply_msg=None):
    """
    This function prepares a executor object which has a fake kernel client
    to mock the messages sent over zeromq. The mock kernel client will return
    the messages passed into this wrapper back from ``preproc.kc.iopub_channel.get_msg``
    callbacks. It also appends a kernel idle message to the end of messages.
    """
    parent_id = 'fake_id'
    messages = list(messages)
    # Always terminate messages with an idle to exit the loop
    messages.append({'msg_type': 'status', 'content': {'execution_state': 'idle'}})

    def shell_channel_message_mock():
        # Return the message generator for
        # self.kc.shell_channel.get_msg => {'parent_header': {'msg_id': parent_id}}
        return AsyncMock(
            return_value=make_async(
                NBClientTestsBase.merge_dicts(
                    {
                        'parent_header': {'msg_id': parent_id},
                        'content': {'status': 'ok', 'execution_count': 1},
                    },
                    reply_msg or {},
                )
            )
        )

    def iopub_messages_mock():
        # Return the message generator for
        # self.kc.iopub_channel.get_msg => messages[i]
        return AsyncMock(
            side_effect=[
                # Default the parent_header so mocks don't need to include this
                make_async(
                    NBClientTestsBase.merge_dicts({'parent_header': {'msg_id': parent_id}}, msg)
                )
                for msg in messages
            ]
        )

    def prepared_wrapper(func):
        @functools.wraps(func)
        def test_mock_wrapper(self):
            """
            This inner function wrapper populates the executor object with
            the fake kernel client. This client has its iopub and shell
            channels mocked so as to fake the setup handshake and return
            the messages passed into prepare_cell_mocks as the execute_cell loop
            processes them.
            """
            cell_mock = NotebookNode(
                source='"foo" = "bar"', metadata={}, cell_type='code', outputs=[]
            )
            executor = NotebookClient({})
            executor.nb = {'cells': [cell_mock]}

            # self.kc.iopub_channel.get_msg => message_mock.side_effect[i]
            message_mock = iopub_messages_mock()
            executor.kc = MagicMock(
                iopub_channel=MagicMock(get_msg=message_mock),
                shell_channel=MagicMock(get_msg=shell_channel_message_mock()),
                execute=MagicMock(return_value=parent_id),
                is_alive=MagicMock(return_value=make_async(True)),
            )
            executor.parent_id = parent_id
            return func(self, executor, cell_mock, message_mock)

        return test_mock_wrapper

    return prepared_wrapper


def normalize_output(output):
    """
    Normalizes outputs for comparison.
    """
    output = dict(output)
    if 'metadata' in output:
        del output['metadata']
    if 'text' in output:
        output['text'] = re.sub(addr_pat, '<HEXADDR>', output['text'])
    if 'text/plain' in output.get('data', {}):
        output['data']['text/plain'] = re.sub(addr_pat, '<HEXADDR>', output['data']['text/plain'])
    if 'application/vnd.jupyter.widget-view+json' in output.get('data', {}):
        output['data']['application/vnd.jupyter.widget-view+json']['model_id'] = '<MODEL_ID>'
    if 'image/svg+xml' in output.get('data', {}):
        output['data']['image/svg+xml'] = xmltodict.parse(output['data']['image/svg+xml'])
    for key, value in output.get('data', {}).items():
        if isinstance(value, str):
            output['data'][key] = normalize_base64(value)
    if 'traceback' in output:
        tb = []
        for line in output["traceback"]:
            line = re.sub(ipython_input_pat, '<IPY-INPUT>', strip_ansi(line))
            line = re.sub(ipython8_input_pat, '<IPY-INPUT>', strip_ansi(line))
            tb.append(line)
        output['traceback'] = tb

    return output


def assert_notebooks_equal(expected, actual):
    expected_cells = expected['cells']
    actual_cells = actual['cells']
    assert len(expected_cells) == len(actual_cells)

    for expected_cell, actual_cell in zip(expected_cells, actual_cells):
        # Uncomment these to help debug test failures better
        # from pprint import pprint
        # pprint(expected_cell)
        # pprint(actual_cell)
        expected_outputs = expected_cell.get('outputs', [])
        actual_outputs = actual_cell.get('outputs', [])
        normalized_expected_outputs = list(map(normalize_output, expected_outputs))
        normalized_actual_outputs = list(map(normalize_output, actual_outputs))
        assert normalized_expected_outputs == normalized_actual_outputs

        expected_execution_count = expected_cell.get('execution_count', None)
        actual_execution_count = actual_cell.get('execution_count', None)
        assert expected_execution_count == actual_execution_count


def notebook_resources():
    """
    Prepare a notebook resources dictionary for executing test
    notebooks in the ``files`` folder.
    """
    return {'metadata': {'path': os.path.join(current_dir, 'files')}}


def filter_messages_on_error_output(err_output):
    allowed_lines = [
        # ipykernel migh be installed without debugpy extension
        "[IPKernelApp] WARNING | debugpy_stream undefined, debugging will not be enabled",
    ]
    filtered_result = [line for line in err_output.splitlines() if line not in allowed_lines]

    return os.linesep.join(filtered_result)


@pytest.mark.parametrize(
    ["input_name", "opts"],
    [
        ("Other Comms.ipynb", dict(kernel_name="python")),
        ("Clear Output.ipynb", dict(kernel_name="python")),
        ("Empty Cell.ipynb", dict(kernel_name="python")),
        ("Factorials.ipynb", dict(kernel_name="python")),
        ("HelloWorld.ipynb", dict(kernel_name="python")),
        ("Inline Image.ipynb", dict(kernel_name="python")),
        (
            "Interrupt.ipynb",
            dict(kernel_name="python", timeout=1, interrupt_on_timeout=True, allow_errors=True),
        ),
        ("JupyterWidgets.ipynb", dict(kernel_name="python")),
        ("Skip Exceptions with Cell Tags.ipynb", dict(kernel_name="python")),
        ("Skip Exceptions.ipynb", dict(kernel_name="python", allow_errors=True)),
        ("Skip Execution with Cell Tag.ipynb", dict(kernel_name="python")),
        ("SVG.ipynb", dict(kernel_name="python")),
        ("Unicode.ipynb", dict(kernel_name="python")),
        ("UnicodePy3.ipynb", dict(kernel_name="python")),
        ("update-display-id.ipynb", dict(kernel_name="python")),
        ("Check History in Memory.ipynb", dict(kernel_name="python")),
    ],
)
def test_run_all_notebooks(input_name, opts):
    """Runs a series of test notebooks and compares them to their actual output"""
    input_file = os.path.join(current_dir, 'files', input_name)
    input_nb, output_nb = run_notebook(input_file, opts, notebook_resources())
    assert_notebooks_equal(input_nb, output_nb)


def test_parallel_notebooks(capfd, tmpdir):
    """Two notebooks should be able to be run simultaneously without problems.

    The two notebooks spawned here use the filesystem to check that the other notebook
    wrote to the filesystem."""

    opts = dict(kernel_name="python")
    input_name = "Parallel Execute {label}.ipynb"
    input_file = os.path.join(current_dir, "files", input_name)
    res = notebook_resources()

    with modified_env({"NBEXECUTE_TEST_PARALLEL_TMPDIR": str(tmpdir)}):
        threads = [
            threading.Thread(target=run_notebook, args=(input_file.format(label=label), opts, res))
            for label in ("A", "B")
        ]
        [t.start() for t in threads]
        [t.join(timeout=2) for t in threads]

    captured = capfd.readouterr()
    assert filter_messages_on_error_output(captured.err) == ""


def test_many_parallel_notebooks(capfd):
    """Ensure that when many IPython kernels are run in parallel, nothing awful happens.

    Specifically, many IPython kernels when run simultaneously would encounter errors
    due to using the same SQLite history database.
    """
    opts = dict(kernel_name="python", timeout=5)
    input_name = "HelloWorld.ipynb"
    input_file = os.path.join(current_dir, "files", input_name)
    res = NBClientTestsBase().build_resources()
    res["metadata"]["path"] = os.path.join(current_dir, "files")

    with warnings.catch_warnings():
        # suppress warning from jupyter_client's deprecated cleanup()
        warnings.simplefilter(action='ignore', category=FutureWarning)

        # run once, to trigger creating the original context
        run_notebook(input_file, opts, res)

        with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor:
            executor.map(run_notebook_wrapper, [(input_file, opts, res) for i in range(8)])

    captured = capfd.readouterr()
    assert filter_messages_on_error_output(captured.err) == ""


def test_async_parallel_notebooks(capfd, tmpdir):
    """Two notebooks should be able to be run simultaneously without problems.

    The two notebooks spawned here use the filesystem to check that the other notebook
    wrote to the filesystem."""

    opts = dict(kernel_name="python")
    input_name = "Parallel Execute {label}.ipynb"
    input_file = os.path.join(current_dir, "files", input_name)
    res = notebook_resources()

    with modified_env({"NBEXECUTE_TEST_PARALLEL_TMPDIR": str(tmpdir)}):
        tasks = [
            async_run_notebook(input_file.format(label=label), opts, res) for label in ("A", "B")
        ]
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.gather(*tasks))

    captured = capfd.readouterr()
    assert filter_messages_on_error_output(captured.err) == ""


def test_many_async_parallel_notebooks(capfd):
    """Ensure that when many IPython kernels are run in parallel, nothing awful happens.

    Specifically, many IPython kernels when run simultaneously would encounter errors
    due to using the same SQLite history database.
    """
    opts = dict(kernel_name="python", timeout=5)
    input_name = "HelloWorld.ipynb"
    input_file = os.path.join(current_dir, "files", input_name)
    res = NBClientTestsBase().build_resources()
    res["metadata"]["path"] = os.path.join(current_dir, "files")

    # run once, to trigger creating the original context
    run_notebook(input_file, opts, res)

    tasks = [async_run_notebook(input_file, opts, res) for i in range(4)]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(*tasks))

    captured = capfd.readouterr()
    assert filter_messages_on_error_output(captured.err) == ""


def test_execution_timing():
    """Compare the execution timing information stored in the cell with the
    actual time it took to run the cell. Also check for the cell timing string
    format."""
    opts = dict(kernel_name="python")
    input_name = "Sleep1s.ipynb"
    input_file = os.path.join(current_dir, "files", input_name)
    res = notebook_resources()
    input_nb, output_nb = run_notebook(input_file, opts, res)

    def get_time_from_str(s):
        time_format = '%Y-%m-%dT%H:%M:%S.%fZ'
        return datetime.datetime.strptime(s, time_format)

    execution_timing = output_nb['cells'][1]['metadata']['execution']
    status_busy = get_time_from_str(execution_timing['iopub.status.busy'])
    execute_input = get_time_from_str(execution_timing['iopub.execute_input'])
    execute_reply = get_time_from_str(execution_timing['shell.execute_reply'])
    status_idle = get_time_from_str(execution_timing['iopub.status.idle'])

    cell_start = get_time_from_str(output_nb['cells'][2]['outputs'][0]['text'])
    cell_end = get_time_from_str(output_nb['cells'][3]['outputs'][0]['text'])

    delta = datetime.timedelta(milliseconds=100)
    assert status_busy - cell_start < delta
    assert execute_input - cell_start < delta
    assert execute_reply - cell_end < delta
    assert status_idle - cell_end < delta


def test_synchronous_setup_kernel():
    nb = nbformat.v4.new_notebook()
    executor = NotebookClient(nb)
    with executor.setup_kernel():
        # Prove it initialized client
        assert executor.kc is not None
    # Prove it removed the client (and hopefully cleaned up)
    assert executor.kc is None


def test_startnewkernel_with_kernelmanager():
    nb = nbformat.v4.new_notebook()
    km = KernelManager()
    executor = NotebookClient(nb, km=km)
    executor.start_new_kernel()
    kc = executor.start_new_kernel_client()
    # prove it initialized client
    assert kc is not None
    # since we are not using the setup_kernel context manager,
    # cleanup has to be done manually
    kc.shutdown()
    km.cleanup_resources()
    kc.stop_channels()


def test_start_new_kernel_history_file_setting():
    nb = nbformat.v4.new_notebook()
    km = KernelManager()
    executor = NotebookClient(nb, km=km)
    kc = km.client()

    # Should start empty
    assert executor.extra_arguments == []
    # Should assign memory setting for ipykernel
    executor.start_new_kernel()
    assert executor.extra_arguments == ['--HistoryManager.hist_file=:memory:']
    # Should not add a second hist_file assignment
    executor.start_new_kernel()
    assert executor.extra_arguments == ['--HistoryManager.hist_file=:memory:']

    # since we are not using the setup_kernel context manager,
    # cleanup has to be done manually
    kc.shutdown()
    km.cleanup_resources()
    kc.stop_channels()


class TestExecute(NBClientTestsBase):
    """Contains test functions for execute.py"""

    maxDiff = None

    def test_constructor(self):
        NotebookClient({})

    def test_populate_language_info(self):
        nb = nbformat.v4.new_notebook()  # Certainly has no language_info.
        executor = NotebookClient(nb, kernel_name="python")
        nb = executor.execute()
        assert 'language_info' in nb.metadata

    def test_empty_path(self):
        """Can the kernel be started when the path is empty?"""
        filename = os.path.join(current_dir, 'files', 'HelloWorld.ipynb')
        res = self.build_resources()
        res['metadata']['path'] = ''
        input_nb, output_nb = run_notebook(filename, {}, res)
        assert_notebooks_equal(input_nb, output_nb)

    @pytest.mark.xfail(
        "python3" not in KernelSpecManager().find_kernel_specs(),
        reason="requires a python3 kernelspec",
    )
    def test_empty_kernel_name(self):
        """Can kernel in nb metadata be found when an empty string is passed?

        Note: this pattern should be discouraged in practice.
        Passing in no kernel_name to NotebookClient is recommended instead.
        """
        filename = os.path.join(current_dir, 'files', 'UnicodePy3.ipynb')
        res = self.build_resources()
        input_nb, output_nb = run_notebook(filename, {"kernel_name": ""}, res)
        assert_notebooks_equal(input_nb, output_nb)
        with pytest.raises(TraitError):
            input_nb, output_nb = run_notebook(filename, {"kernel_name": None}, res)

    def test_disable_stdin(self):
        """Test disabling standard input"""
        filename = os.path.join(current_dir, 'files', 'Disable Stdin.ipynb')
        res = self.build_resources()
        res['metadata']['path'] = os.path.dirname(filename)
        input_nb, output_nb = run_notebook(filename, dict(allow_errors=True), res)

        # We need to special-case this particular notebook, because the
        # traceback contains machine-specific stuff like where IPython
        # is installed. It is sufficient here to just check that an error
        # was thrown, and that it was a StdinNotImplementedError
        self.assertEqual(len(output_nb['cells']), 1)
        self.assertEqual(len(output_nb['cells'][0]['outputs']), 1)
        output = output_nb['cells'][0]['outputs'][0]
        self.assertEqual(output['output_type'], 'error')
        self.assertEqual(output['ename'], 'StdinNotImplementedError')
        self.assertEqual(
            output['evalue'],
            'raw_input was called, but this frontend does not support input requests.',
        )

    def test_timeout(self):
        """Check that an error is raised when a computation times out"""
        filename = os.path.join(current_dir, 'files', 'Interrupt.ipynb')
        res = self.build_resources()
        res['metadata']['path'] = os.path.dirname(filename)

        with pytest.raises(TimeoutError) as err:
            run_notebook(filename, dict(timeout=1), res)
        self.assertEqual(
            str(err.value.args[0]),
            """A cell timed out while it was being executed, after 1 seconds.
The message was: Cell execution timed out.
Here is a preview of the cell contents:
-------------------
while True: continue
-------------------
""",
        )

    def test_timeout_func(self):
        """Check that an error is raised when a computation times out"""
        filename = os.path.join(current_dir, 'files', 'Interrupt.ipynb')
        res = self.build_resources()
        res['metadata']['path'] = os.path.dirname(filename)

        def timeout_func(source):
            return 10

        with pytest.raises(TimeoutError):
            run_notebook(filename, dict(timeout_func=timeout_func), res)

    def test_kernel_death_after_timeout(self):
        """Check that an error is raised when the kernel is_alive is false after a cell timed out"""
        filename = os.path.join(current_dir, 'files', 'Interrupt.ipynb')
        with open(filename) as f:
            input_nb = nbformat.read(f, 4)
        res = self.build_resources()
        res['metadata']['path'] = os.path.dirname(filename)

        executor = NotebookClient(input_nb, timeout=1)

        with pytest.raises(TimeoutError):
            executor.execute()
        km = executor.create_kernel_manager()

        async def is_alive():
            return False

        km.is_alive = is_alive
        # Will be a RuntimeError or subclass DeadKernelError depending
        # on if jupyter_client or nbconvert catches the dead client first
        with pytest.raises(RuntimeError):
            input_nb, output_nb = executor.execute()

    def test_kernel_death_during_execution(self):
        """Check that an error is raised when the kernel is_alive is false during a cell
        execution.
        """
        filename = os.path.join(current_dir, 'files', 'Autokill.ipynb')
        with open(filename) as f:
            input_nb = nbformat.read(f, 4)

        executor = NotebookClient(input_nb)

        with pytest.raises(RuntimeError):
            executor.execute()

    def test_allow_errors(self):
        """
        Check that conversion halts if ``allow_errors`` is False.
        """
        filename = os.path.join(current_dir, 'files', 'Skip Exceptions.ipynb')
        res = self.build_resources()
        res['metadata']['path'] = os.path.dirname(filename)
        with pytest.raises(CellExecutionError) as exc:
            run_notebook(filename, dict(allow_errors=False), res)
            self.assertIsInstance(str(exc.value), str)
            assert "# üñîçø∂é" in str(exc.value)

    def test_force_raise_errors(self):
        """
        Check that conversion halts if the ``force_raise_errors`` traitlet on
        NotebookClient is set to True.
        """
        filename = os.path.join(current_dir, 'files', 'Skip Exceptions with Cell Tags.ipynb')
        res = self.build_resources()
        res['metadata']['path'] = os.path.dirname(filename)
        with pytest.raises(CellExecutionError) as exc:
            run_notebook(filename, dict(force_raise_errors=True), res)
            self.assertIsInstance(str(exc.value), str)
            assert "# üñîçø∂é" in str(exc.value)

    def test_reset_kernel_client(self):
        filename = os.path.join(current_dir, 'files', 'HelloWorld.ipynb')

        with open(filename) as f:
            input_nb = nbformat.read(f, 4)

        executor = NotebookClient(
            input_nb,
            resources=self.build_resources(),
        )

        executor.execute(cleanup_kc=False)
        # we didn't ask to reset the kernel client, a new one must have been created
        kc = executor.kc
        assert kc is not None

        executor.execute(cleanup_kc=False)
        # we didn't ask to reset the kernel client, the previously created one must have been reused
        assert kc == executor.kc

        executor.execute(reset_kc=True, cleanup_kc=False)
        # we asked to reset the kernel client, the previous one must have been cleaned up,
        # a new one must have been created
        assert kc != executor.kc

    def test_cleanup_kernel_client(self):
        filename = os.path.join(current_dir, 'files', 'HelloWorld.ipynb')

        with open(filename) as f:
            input_nb = nbformat.read(f, 4)

        executor = NotebookClient(
            input_nb,
            resources=self.build_resources(),
        )

        executor.execute()
        # we asked to cleanup the kernel client (default is True)
        assert executor.kc is None

        executor.execute(cleanup_kc=False)
        # we didn't ask to reset the kernel client
        # a new one must have been created and should still be available
        assert executor.kc is not None

    def test_custom_kernel_manager(self):
        from .fake_kernelmanager import FakeCustomKernelManager

        filename = os.path.join(current_dir, 'files', 'HelloWorld.ipynb')

        with open(filename) as f:
            input_nb = nbformat.read(f, 4)

        cleaned_input_nb = copy.deepcopy(input_nb)
        for cell in cleaned_input_nb.cells:
            if 'execution_count' in cell:
                del cell['execution_count']
            cell['outputs'] = []

        executor = NotebookClient(
            cleaned_input_nb,
            resources=self.build_resources(),
            kernel_manager_class=FakeCustomKernelManager,
        )

        # Override terminal size to standardise traceback format
        with modified_env({'COLUMNS': '80', 'LINES': '24'}):
            executor.execute()

        expected = FakeCustomKernelManager.expected_methods.items()

        for method, call_count in expected:
            self.assertNotEqual(call_count, 0, f'{method} was called')

    def test_process_message_wrapper(self):
        outputs = []

        class WrappedPreProc(NotebookClient):
            def process_message(self, msg, cell, cell_index):
                result = super().process_message(msg, cell, cell_index)
                if result:
                    outputs.append(result)
                return result

        current_dir = os.path.dirname(__file__)
        filename = os.path.join(current_dir, 'files', 'HelloWorld.ipynb')

        with open(filename) as f:
            input_nb = nbformat.read(f, 4)

        original = copy.deepcopy(input_nb)
        wpp = WrappedPreProc(input_nb)
        executed = wpp.execute()
        assert outputs == [{'name': 'stdout', 'output_type': 'stream', 'text': 'Hello World\n'}]
        assert_notebooks_equal(original, executed)

    def test_execute_function(self):
        # Test the execute() convenience API
        filename = os.path.join(current_dir, 'files', 'HelloWorld.ipynb')

        with open(filename) as f:
            input_nb = nbformat.read(f, 4)

        original = copy.deepcopy(input_nb)
        executed = execute(original, os.path.dirname(filename))
        assert_notebooks_equal(original, executed)

    def test_widgets(self):
        """Runs a test notebook with widgets and checks the widget state is saved."""
        input_file = os.path.join(current_dir, 'files', 'JupyterWidgets.ipynb')
        opts = dict(kernel_name="python")
        res = self.build_resources()
        res['metadata']['path'] = os.path.dirname(input_file)
        input_nb, output_nb = run_notebook(input_file, opts, res)

        output_data = [
            output.get('data', {}) for cell in output_nb['cells'] for output in cell['outputs']
        ]

        model_ids = [
            data['application/vnd.jupyter.widget-view+json']['model_id']
            for data in output_data
            if 'application/vnd.jupyter.widget-view+json' in data
        ]

        wdata = output_nb['metadata']['widgets']['application/vnd.jupyter.widget-state+json']
        for k in model_ids:
            d = wdata['state'][k]
            assert 'model_name' in d
            assert 'model_module' in d
            assert 'state' in d
        assert 'version_major' in wdata
        assert 'version_minor' in wdata

    def test_execution_hook(self):
        filename = os.path.join(current_dir, 'files', 'HelloWorld.ipynb')
        with open(filename) as f:
            input_nb = nbformat.read(f, 4)
        hooks = [MagicMock() for i in range(7)]
        executor = NotebookClient(input_nb)
        for executor_hook, hook in zip(hook_methods, hooks):
            setattr(executor, executor_hook, hook)
        executor.execute()
        for hook in hooks[:3]:
            hook.assert_called_once()
        hooks[3].assert_not_called()
        for hook in hooks[4:6]:
            hook.assert_called_once()
        hooks[6].assert_not_called()

    def test_error_execution_hook_error(self):
        filename = os.path.join(current_dir, 'files', 'Error.ipynb')
        with open(filename) as f:
            input_nb = nbformat.read(f, 4)
        hooks = [MagicMock() for i in range(7)]
        executor = NotebookClient(input_nb)
        for executor_hook, hook in zip(hook_methods, hooks):
            setattr(executor, executor_hook, hook)
        with pytest.raises(CellExecutionError):
            executor.execute()
        for hook in hooks[:5]:
            hook.assert_called_once()
        hooks[6].assert_not_called()

    def test_error_notebook_hook(self):
        filename = os.path.join(current_dir, 'files', 'Autokill.ipynb')
        with open(filename) as f:
            input_nb = nbformat.read(f, 4)
        hooks = [MagicMock() for i in range(7)]
        executor = NotebookClient(input_nb)
        for executor_hook, hook in zip(hook_methods, hooks):
            setattr(executor, executor_hook, hook)
        with pytest.raises(RuntimeError):
            executor.execute()
        for hook in hooks[:3]:
            hook.assert_called_once()
        hooks[3].assert_not_called()
        for hook in hooks[4:]:
            hook.assert_called_once()

    def test_async_execution_hook(self):
        filename = os.path.join(current_dir, 'files', 'HelloWorld.ipynb')
        with open(filename) as f:
            input_nb = nbformat.read(f, 4)
        hooks = [AsyncMock() for i in range(7)]
        executor = NotebookClient(input_nb)
        for executor_hook, hook in zip(hook_methods, hooks):
            setattr(executor, executor_hook, hook)
        executor.execute()
        for hook in hooks[:3]:
            hook.assert_called_once()
        hooks[3].assert_not_called()
        for hook in hooks[4:6]:
            hook.assert_called_once()
        hooks[6].assert_not_called()

    def test_error_async_execution_hook(self):
        filename = os.path.join(current_dir, 'files', 'Error.ipynb')
        with open(filename) as f:
            input_nb = nbformat.read(f, 4)
        hooks = [AsyncMock() for i in range(7)]
        executor = NotebookClient(input_nb)
        for executor_hook, hook in zip(hook_methods, hooks):
            setattr(executor, executor_hook, hook)
        with pytest.raises(CellExecutionError):
            executor.execute().execute()
        for hook in hooks[:5]:
            hook.assert_called_once()
        hooks[6].assert_not_called()


class TestRunCell(NBClientTestsBase):
    """Contains test functions for NotebookClient.execute_cell"""

    @prepare_cell_mocks()
    def test_idle_message(self, executor, cell_mock, message_mock):
        executor.execute_cell(cell_mock, 0)
        # Just the exit message should be fetched
        assert message_mock.call_count == 1
        # Ensure no outputs were generated
        assert cell_mock.outputs == []

    @prepare_cell_mocks(
        {
            'msg_type': 'stream',
            'header': {'msg_type': 'execute_reply'},
            'parent_header': {'msg_id': 'wrong_parent'},
            'content': {'name': 'stdout', 'text': 'foo'},
        }
    )
    def test_message_for_wrong_parent(self, executor, cell_mock, message_mock):
        executor.execute_cell(cell_mock, 0)
        # An ignored stream followed by an idle
        assert message_mock.call_count == 2
        # Ensure no output was written
        assert cell_mock.outputs == []

    @prepare_cell_mocks(
        {
            'msg_type': 'status',
            'header': {'msg_type': 'status'},
            'content': {'execution_state': 'busy'},
        }
    )
    def test_busy_message(self, executor, cell_mock, message_mock):
        executor.execute_cell(cell_mock, 0)
        # One busy message, followed by an idle
        assert message_mock.call_count == 2
        # Ensure no outputs were generated
        assert cell_mock.outputs == []

    @prepare_cell_mocks(
        {
            'msg_type': 'stream',
            'header': {'msg_type': 'stream'},
            'content': {'name': 'stdout', 'text': 'foo'},
        },
        {
            'msg_type': 'stream',
            'header': {'msg_type': 'stream'},
            'content': {'name': 'stderr', 'text': 'bar'},
        },
    )
    def test_deadline_exec_reply(self, executor, cell_mock, message_mock):
        # exec_reply is never received, so we expect to hit the timeout.
        async def get_msg(timeout):
            await asyncio.sleep(timeout)
            raise Empty

        executor.kc.shell_channel.get_msg = get_msg
        executor.timeout = 1

        with pytest.raises(TimeoutError):
            executor.execute_cell(cell_mock, 0)

        assert message_mock.call_count == 3
        # Ensure the output was captured
        self.assertListEqual(
            cell_mock.outputs,
            [
                {'output_type': 'stream', 'name': 'stdout', 'text': 'foo'},
                {'output_type': 'stream', 'name': 'stderr', 'text': 'bar'},
            ],
        )

    @prepare_cell_mocks()
    def test_deadline_iopub(self, executor, cell_mock, message_mock):
        # The shell_channel will complete, so we expect only to hit the iopub timeout.
        message_mock.side_effect = Empty()
        executor.raise_on_iopub_timeout = True

        with pytest.raises(TimeoutError):
            executor.execute_cell(cell_mock, 0)

    @prepare_cell_mocks(
        {
            'msg_type': 'stream',
            'header': {'msg_type': 'stream'},
            'content': {'name': 'stdout', 'text': 'foo'},
        },
        {
            'msg_type': 'stream',
            'header': {'msg_type': 'stream'},
            'content': {'name': 'stderr', 'text': 'bar'},
        },
    )
    def test_eventual_deadline_iopub(self, executor, cell_mock, message_mock):
        # Process a few messages before raising a timeout from iopub
        def message_seq(messages):
            yield from messages
            while True:
                yield Empty()

        message_mock.side_effect = message_seq(list(message_mock.side_effect)[:-1])
        executor.kc.shell_channel.get_msg = Mock(
            return_value=make_async({'parent_header': {'msg_id': executor.parent_id}})
        )
        executor.raise_on_iopub_timeout = True

        with pytest.raises(TimeoutError):
            executor.execute_cell(cell_mock, 0)

        assert message_mock.call_count >= 3
        # Ensure the output was captured
        self.assertListEqual(
            cell_mock.outputs,
            [
                {'output_type': 'stream', 'name': 'stdout', 'text': 'foo'},
                {'output_type': 'stream', 'name': 'stderr', 'text': 'bar'},
            ],
        )

    @prepare_cell_mocks(
        {'msg_type': 'execute_input', 'header': {'msg_type': 'execute_input'}, 'content': {}}
    )
    def test_execute_input_message(self, executor, cell_mock, message_mock):
        executor.execute_cell(cell_mock, 0)
        # One ignored execute_input, followed by an idle
        assert message_mock.call_count == 2
        # Ensure no outputs were generated
        assert cell_mock.outputs == []

    @prepare_cell_mocks(
        {
            'msg_type': 'stream',
            'header': {'msg_type': 'stream'},
            'content': {'name': 'stdout', 'text': 'foo'},
        },
        {
            'msg_type': 'stream',
            'header': {'msg_type': 'stream'},
            'content': {'name': 'stderr', 'text': 'bar'},
        },
    )
    def test_stream_messages(self, executor, cell_mock, message_mock):
        executor.execute_cell(cell_mock, 0)
        # An stdout then stderr stream followed by an idle
        assert message_mock.call_count == 3
        # Ensure the output was captured
        self.assertListEqual(
            cell_mock.outputs,
            [
                {'output_type': 'stream', 'name': 'stdout', 'text': 'foo'},
                {'output_type': 'stream', 'name': 'stderr', 'text': 'bar'},
            ],
        )

    @prepare_cell_mocks(
        {
            'msg_type': 'stream',
            'header': {'msg_type': 'execute_reply'},
            'content': {'name': 'stdout', 'text': 'foo'},
        },
        {'msg_type': 'clear_output', 'header': {'msg_type': 'clear_output'}, 'content': {}},
    )
    def test_clear_output_message(self, executor, cell_mock, message_mock):
        executor.execute_cell(cell_mock, 0)
        # A stream, followed by a clear, and then an idle
        assert message_mock.call_count == 3
        # Ensure the output was cleared
        assert cell_mock.outputs == []

    @prepare_cell_mocks(
        {
            'msg_type': 'stream',
            'header': {'msg_type': 'stream'},
            'content': {'name': 'stdout', 'text': 'foo'},
        },
        {
            'msg_type': 'clear_output',
            'header': {'msg_type': 'clear_output'},
            'content': {'wait': True},
        },
    )
    def test_clear_output_wait_message(self, executor, cell_mock, message_mock):
        executor.execute_cell(cell_mock, 0)
        # A stream, followed by a clear, and then an idle
        assert message_mock.call_count == 3
        # Should be true without another message to trigger the clear
        self.assertTrue(executor.clear_before_next_output)
        # Ensure the output wasn't cleared yet
        assert cell_mock.outputs == [{'output_type': 'stream', 'name': 'stdout', 'text': 'foo'}]

    @prepare_cell_mocks(
        {
            'msg_type': 'stream',
            'header': {'msg_type': 'stream'},
            'content': {'name': 'stdout', 'text': 'foo'},
        },
        {
            'msg_type': 'clear_output',
            'header': {'msg_type': 'clear_output'},
            'content': {'wait': True},
        },
        {
            'msg_type': 'stream',
            'header': {'msg_type': 'stream'},
            'content': {'name': 'stderr', 'text': 'bar'},
        },
    )
    def test_clear_output_wait_then_message_message(self, executor, cell_mock, message_mock):
        executor.execute_cell(cell_mock, 0)
        # An stdout stream, followed by a wait clear, an stderr stream, and then an idle
        assert message_mock.call_count == 4
        # Should be false after the stderr message
        assert not executor.clear_before_next_output
        # Ensure the output wasn't cleared yet
        assert cell_mock.outputs == [{'output_type': 'stream', 'name': 'stderr', 'text': 'bar'}]

    @prepare_cell_mocks(
        {
            'msg_type': 'stream',
            'header': {'msg_type': 'stream'},
            'content': {'name': 'stdout', 'text': 'foo'},
        },
        {
            'msg_type': 'clear_output',
            'header': {'msg_type': 'clear_output'},
            'content': {'wait': True},
        },
        {
            'msg_type': 'update_display_data',
            'header': {'msg_type': 'update_display_data'},
            'content': {'metadata': {'metafoo': 'metabar'}, 'data': {'foo': 'bar'}},
        },
    )
    def test_clear_output_wait_then_update_display_message(self, executor, cell_mock, message_mock):
        executor.execute_cell(cell_mock, 0)
        # An stdout stream, followed by a wait clear, an stderr stream, and then an idle
        assert message_mock.call_count == 4
        # Should be false after the stderr message
        assert executor.clear_before_next_output
        # Ensure the output wasn't cleared yet because update_display doesn't add outputs
        assert cell_mock.outputs == [{'output_type': 'stream', 'name': 'stdout', 'text': 'foo'}]

    @prepare_cell_mocks(
        {
            'msg_type': 'execute_reply',
            'header': {'msg_type': 'execute_reply'},
            'content': {'execution_count': 42},
        }
    )
    def test_execution_count_message(self, executor, cell_mock, message_mock):
        executor.execute_cell(cell_mock, 0)
        # An execution count followed by an idle
        assert message_mock.call_count == 2
        assert cell_mock.execution_count == 42
        # Ensure no outputs were generated
        assert cell_mock.outputs == []

    @prepare_cell_mocks(
        {
            'msg_type': 'execute_reply',
            'header': {'msg_type': 'execute_reply'},
            'content': {'execution_count': 42},
        }
    )
    def test_execution_count_message_ignored_on_override(self, executor, cell_mock, message_mock):
        executor.execute_cell(cell_mock, 0, execution_count=21)
        # An execution count followed by an idle
        assert message_mock.call_count == 2
        assert cell_mock.execution_count == 21
        # Ensure no outputs were generated
        assert cell_mock.outputs == []

    @prepare_cell_mocks(
        {
            'msg_type': 'stream',
            'header': {'msg_type': 'stream'},
            'content': {'execution_count': 42, 'name': 'stdout', 'text': 'foo'},
        }
    )
    def test_execution_count_with_stream_message(self, executor, cell_mock, message_mock):
        executor.execute_cell(cell_mock, 0)
        # An execution count followed by an idle
        assert message_mock.call_count == 2
        assert cell_mock.execution_count == 42
        # Should also consume the message stream
        assert cell_mock.outputs == [{'output_type': 'stream', 'name': 'stdout', 'text': 'foo'}]

    @prepare_cell_mocks(
        {
            'msg_type': 'comm',
            'header': {'msg_type': 'comm'},
            'content': {'comm_id': 'foobar', 'data': {'state': {'foo': 'bar'}}},
        }
    )
    def test_widget_comm_message(self, executor, cell_mock, message_mock):
        executor.execute_cell(cell_mock, 0)
        # A comm message without buffer info followed by an idle
        assert message_mock.call_count == 2
        self.assertEqual(executor.widget_state, {'foobar': {'foo': 'bar'}})
        # Buffers should still be empty
        assert not executor.widget_buffers
        # Ensure no outputs were generated
        assert cell_mock.outputs == []

    @prepare_cell_mocks(
        {
            'msg_type': 'comm',
            'header': {'msg_type': 'comm'},
            'buffers': [b'123'],
            'content': {
                'comm_id': 'foobar',
                'data': {'state': {'foo': 'bar'}, 'buffer_paths': [['path']]},
            },
        }
    )
    def test_widget_comm_buffer_message_single(self, executor, cell_mock, message_mock):
        executor.execute_cell(cell_mock, 0)
        # A comm message with buffer info followed by an idle
        assert message_mock.call_count == 2
        assert executor.widget_state == {'foobar': {'foo': 'bar'}}
        assert executor.widget_buffers == {
            'foobar': {('path',): {'data': 'MTIz', 'encoding': 'base64', 'path': ['path']}}
        }
        # Ensure no outputs were generated
        assert cell_mock.outputs == []

    @prepare_cell_mocks(
        {
            'msg_type': 'comm',
            'header': {'msg_type': 'comm'},
            'buffers': [b'123'],
            'content': {
                'comm_id': 'foobar',
                'data': {'state': {'foo': 'bar'}, 'buffer_paths': [['path']]},
            },
        },
        {
            'msg_type': 'comm',
            'header': {'msg_type': 'comm'},
            'buffers': [b'123'],
            'content': {
                'comm_id': 'foobar',
                'data': {'state': {'foo2': 'bar2'}, 'buffer_paths': [['path2']]},
            },
        },
    )
    def test_widget_comm_buffer_messages(self, executor, cell_mock, message_mock):
        executor.execute_cell(cell_mock, 0)
        # A comm message with buffer info followed by an idle
        assert message_mock.call_count == 3
        assert executor.widget_state == {'foobar': {'foo': 'bar', 'foo2': 'bar2'}}
        assert executor.widget_buffers == {
            'foobar': {
                ('path',): {'data': 'MTIz', 'encoding': 'base64', 'path': ['path']},
                ('path2',): {'data': 'MTIz', 'encoding': 'base64', 'path': ['path2']},
            }
        }
        # Ensure no outputs were generated
        assert cell_mock.outputs == []

    @prepare_cell_mocks(
        {
            'msg_type': 'comm',
            'header': {'msg_type': 'comm'},
            'content': {
                'comm_id': 'foobar',
                # No 'state'
                'data': {'foo': 'bar'},
            },
        }
    )
    def test_unknown_comm_message(self, executor, cell_mock, message_mock):
        executor.execute_cell(cell_mock, 0)
        # An unknown comm message followed by an idle
        assert message_mock.call_count == 2
        # Widget states should be empty as the message has the wrong shape
        assert not executor.widget_state
        assert not executor.widget_buffers
        # Ensure no outputs were generated
        assert cell_mock.outputs == []

    @prepare_cell_mocks(
        {
            'msg_type': 'execute_result',
            'header': {'msg_type': 'execute_result'},
            'content': {
                'metadata': {'metafoo': 'metabar'},
                'data': {'foo': 'bar'},
                'execution_count': 42,
            },
        }
    )
    def test_execute_result_message(self, executor, cell_mock, message_mock):
        executor.execute_cell(cell_mock, 0)
        # An execute followed by an idle
        assert message_mock.call_count == 2
        assert cell_mock.execution_count == 42
        # Should generate an associated message
        assert cell_mock.outputs == [
            {
                'output_type': 'execute_result',
                'metadata': {'metafoo': 'metabar'},
                'data': {'foo': 'bar'},
                'execution_count': 42,
            }
        ]
        # No display id was provided
        assert not executor._display_id_map

    @prepare_cell_mocks(
        {
            'msg_type': 'execute_result',
            'header': {'msg_type': 'execute_result'},
            'content': {
                'transient': {'display_id': 'foobar'},
                'metadata': {'metafoo': 'metabar'},
                'data': {'foo': 'bar'},
                'execution_count': 42,
            },
        }
    )
    def test_execute_result_with_display_message(self, executor, cell_mock, message_mock):
        executor.execute_cell(cell_mock, 0)
        # An execute followed by an idle
        assert message_mock.call_count == 2
        assert cell_mock.execution_count == 42
        # Should generate an associated message
        assert cell_mock.outputs == [
            {
                'output_type': 'execute_result',
                'metadata': {'metafoo': 'metabar'},
                'data': {'foo': 'bar'},
                'execution_count': 42,
            }
        ]
        assert 'foobar' in executor._display_id_map

    @prepare_cell_mocks(
        {
            'msg_type': 'display_data',
            'header': {'msg_type': 'display_data'},
            'content': {'metadata': {'metafoo': 'metabar'}, 'data': {'foo': 'bar'}},
        }
    )
    def test_display_data_without_id_message(self, executor, cell_mock, message_mock):
        executor.execute_cell(cell_mock, 0)
        # A display followed by an idle
        assert message_mock.call_count == 2
        # Should generate an associated message
        assert cell_mock.outputs == [
            {
                'output_type': 'display_data',
                'metadata': {'metafoo': 'metabar'},
                'data': {'foo': 'bar'},
            }
        ]
        # No display id was provided
        assert not executor._display_id_map

    @prepare_cell_mocks(
        {
            'msg_type': 'display_data',
            'header': {'msg_type': 'display_data'},
            'content': {
                'transient': {'display_id': 'foobar'},
                'metadata': {'metafoo': 'metabar'},
                'data': {'foo': 'bar'},
            },
        }
    )
    def test_display_data_message(self, executor, cell_mock, message_mock):
        executor.execute_cell(cell_mock, 0)
        # A display followed by an idle
        assert message_mock.call_count == 2
        # Should generate an associated message
        assert cell_mock.outputs == [
            {
                'output_type': 'display_data',
                'metadata': {'metafoo': 'metabar'},
                'data': {'foo': 'bar'},
            }
        ]
        assert 'foobar' in executor._display_id_map

    @prepare_cell_mocks(
        {
            'msg_type': 'display_data',
            'header': {'msg_type': 'display_data'},
            'content': {
                'transient': {'display_id': 'foobar'},
                'metadata': {'metafoo': 'metabar'},
                'data': {'foo': 'bar'},
            },
        },
        {
            'msg_type': 'display_data',
            'header': {'msg_type': 'display_data'},
            'content': {
                'transient': {'display_id': 'foobar_other'},
                'metadata': {'metafoo_other': 'metabar_other'},
                'data': {'foo': 'bar_other'},
            },
        },
        {
            'msg_type': 'display_data',
            'header': {'msg_type': 'display_data'},
            'content': {
                'transient': {'display_id': 'foobar'},
                'metadata': {'metafoo2': 'metabar2'},
                'data': {'foo': 'bar2', 'baz': 'foobarbaz'},
            },
        },
    )
    def test_display_data_same_id_message(self, executor, cell_mock, message_mock):
        executor.execute_cell(cell_mock, 0)
        # A display followed by an idle
        assert message_mock.call_count == 4
        # Original output should be manipulated and a copy of the second now
        assert cell_mock.outputs == [
            {
                'output_type': 'display_data',
                'metadata': {'metafoo2': 'metabar2'},
                'data': {'foo': 'bar2', 'baz': 'foobarbaz'},
            },
            {
                'output_type': 'display_data',
                'metadata': {'metafoo_other': 'metabar_other'},
                'data': {'foo': 'bar_other'},
            },
            {
                'output_type': 'display_data',
                'metadata': {'metafoo2': 'metabar2'},
                'data': {'foo': 'bar2', 'baz': 'foobarbaz'},
            },
        ]
        assert 'foobar' in executor._display_id_map

    @prepare_cell_mocks(
        {
            'msg_type': 'update_display_data',
            'header': {'msg_type': 'update_display_data'},
            'content': {'metadata': {'metafoo': 'metabar'}, 'data': {'foo': 'bar'}},
        }
    )
    def test_update_display_data_without_id_message(self, executor, cell_mock, message_mock):
        executor.execute_cell(cell_mock, 0)
        # An update followed by an idle
        assert message_mock.call_count == 2
        # Display updates don't create any outputs
        assert cell_mock.outputs == []
        # No display id was provided
        assert not executor._display_id_map

    @prepare_cell_mocks(
        {
            'msg_type': 'display_data',
            'header': {'msg_type': 'display_data'},
            'content': {
                'transient': {'display_id': 'foobar'},
                'metadata': {'metafoo2': 'metabar2'},
                'data': {'foo': 'bar2', 'baz': 'foobarbaz'},
            },
        },
        {
            'msg_type': 'update_display_data',
            'header': {'msg_type': 'update_display_data'},
            'content': {
                'transient': {'display_id': 'foobar2'},
                'metadata': {'metafoo2': 'metabar2'},
                'data': {'foo': 'bar2', 'baz': 'foobarbaz'},
            },
        },
    )
    def test_update_display_data_mismatch_id_message(self, executor, cell_mock, message_mock):
        executor.execute_cell(cell_mock, 0)
        # An update followed by an idle
        assert message_mock.call_count == 3
        # Display updates don't create any outputs
        assert cell_mock.outputs == [
            {
                'output_type': 'display_data',
                'metadata': {'metafoo2': 'metabar2'},
                'data': {'foo': 'bar2', 'baz': 'foobarbaz'},
            }
        ]
        assert 'foobar' in executor._display_id_map

    @prepare_cell_mocks(
        {
            'msg_type': 'display_data',
            'header': {'msg_type': 'display_data'},
            'content': {
                'transient': {'display_id': 'foobar'},
                'metadata': {'metafoo': 'metabar'},
                'data': {'foo': 'bar'},
            },
        },
        {
            'msg_type': 'update_display_data',
            'header': {'msg_type': 'update_display_data'},
            'content': {
                'transient': {'display_id': 'foobar'},
                'metadata': {'metafoo2': 'metabar2'},
                'data': {'foo': 'bar2', 'baz': 'foobarbaz'},
            },
        },
    )
    def test_update_display_data_message(self, executor, cell_mock, message_mock):
        executor.execute_cell(cell_mock, 0)
        # A display followed by an update then an idle
        assert message_mock.call_count == 3
        # Original output should be manipulated
        assert cell_mock.outputs == [
            {
                'output_type': 'display_data',
                'metadata': {'metafoo2': 'metabar2'},
                'data': {'foo': 'bar2', 'baz': 'foobarbaz'},
            }
        ]
        assert 'foobar' in executor._display_id_map

    @prepare_cell_mocks(
        {
            'msg_type': 'error',
            'header': {'msg_type': 'error'},
            'content': {'ename': 'foo', 'evalue': 'bar', 'traceback': ['Boom']},
        }
    )
    def test_error_message(self, executor, cell_mock, message_mock):
        executor.execute_cell(cell_mock, 0)
        # An error followed by an idle
        assert message_mock.call_count == 2
        # Should also consume the message stream
        assert cell_mock.outputs == [
            {'output_type': 'error', 'ename': 'foo', 'evalue': 'bar', 'traceback': ['Boom']}
        ]

    @prepare_cell_mocks(
        {
            'msg_type': 'error',
            'header': {'msg_type': 'error'},
            'content': {'ename': 'foo', 'evalue': 'bar', 'traceback': ['Boom']},
        },
        reply_msg={
            'msg_type': 'execute_reply',
            'header': {'msg_type': 'execute_reply'},
            # ERROR
            'content': {'status': 'error'},
        },
    )
    def test_error_and_error_status_messages(self, executor, cell_mock, message_mock):
        with self.assertRaises(CellExecutionError):
            executor.execute_cell(cell_mock, 0)

        # An error followed by an idle
        assert message_mock.call_count == 2
        # Cell outputs should still be copied
        assert cell_mock.outputs == [
            {'output_type': 'error', 'ename': 'foo', 'evalue': 'bar', 'traceback': ['Boom']}
        ]

    @prepare_cell_mocks(
        {
            'msg_type': 'error',
            'header': {'msg_type': 'error'},
            'content': {'ename': 'foo', 'evalue': 'bar', 'traceback': ['Boom']},
        },
        reply_msg={
            'msg_type': 'execute_reply',
            'header': {'msg_type': 'execute_reply'},
            # OK
            'content': {'status': 'ok'},
        },
    )
    def test_error_message_only(self, executor, cell_mock, message_mock):
        # Should NOT raise
        executor.execute_cell(cell_mock, 0)

        # An error followed by an idle
        assert message_mock.call_count == 2
        # Should also consume the message stream
        assert cell_mock.outputs == [
            {'output_type': 'error', 'ename': 'foo', 'evalue': 'bar', 'traceback': ['Boom']}
        ]

    @prepare_cell_mocks(
        reply_msg={
            'msg_type': 'execute_reply',
            'header': {'msg_type': 'execute_reply'},
            # ERROR
            'content': {'status': 'error'},
        }
    )
    def test_allow_errors(self, executor, cell_mock, message_mock):
        executor.allow_errors = True
        # Should NOT raise
        executor.execute_cell(cell_mock, 0)

        # An error followed by an idle
        assert message_mock.call_count == 1
        # Should also consume the message stream
        assert cell_mock.outputs == []

    @prepare_cell_mocks(
        reply_msg={
            'msg_type': 'execute_reply',
            'header': {'msg_type': 'execute_reply'},
            # ERROR
            'content': {'status': 'error', 'ename': 'NotImplementedError'},
        }
    )
    def test_allow_error_names(self, executor, cell_mock, message_mock):
        executor.allow_error_names = ['NotImplementedError']
        # Should NOT raise
        executor.execute_cell(cell_mock, 0)

        # An error followed by an idle
        assert message_mock.call_count == 1
        # Should also consume the message stream
        assert cell_mock.outputs == []

    @prepare_cell_mocks(
        reply_msg={
            'msg_type': 'execute_reply',
            'header': {'msg_type': 'execute_reply'},
            # ERROR
            'content': {'status': 'error'},
        }
    )
    def test_raises_exception_tag(self, executor, cell_mock, message_mock):
        cell_mock.metadata['tags'] = ['raises-exception']
        # Should NOT raise
        executor.execute_cell(cell_mock, 0)

        # An error followed by an idle
        assert message_mock.call_count == 1
        # Should also consume the message stream
        assert cell_mock.outputs == []

    @prepare_cell_mocks(
        reply_msg={
            'msg_type': 'execute_reply',
            'header': {'msg_type': 'execute_reply'},
            # ERROR
            'content': {'status': 'error'},
        }
    )
    def test_non_code_cell(self, executor, cell_mock, message_mock):
        cell_mock = NotebookNode(source='"foo" = "bar"', metadata={}, cell_type='raw', outputs=[])
        # Should NOT raise nor execute any code
        executor.execute_cell(cell_mock, 0)

        # An error followed by an idle
        assert message_mock.call_count == 0
        # Should also consume the message stream
        assert cell_mock.outputs == []

    @prepare_cell_mocks(
        reply_msg={
            'msg_type': 'execute_reply',
            'header': {'msg_type': 'execute_reply'},
            # ERROR
            'content': {'status': 'error'},
        }
    )
    def test_no_source(self, executor, cell_mock, message_mock):
        cell_mock = NotebookNode(
            # Stripped source is empty
            source='     ',
            metadata={},
            cell_type='code',
            outputs=[],
        )
        # Should NOT raise nor execute any code
        executor.execute_cell(cell_mock, 0)

        # An error followed by an idle
        assert message_mock.call_count == 0
        # Should also consume the message stream
        assert cell_mock.outputs == []

    @prepare_cell_mocks()
    def test_cell_hooks(self, executor, cell_mock, message_mock):
        hooks = [MagicMock() for i in range(7)]
        for executor_hook, hook in zip(hook_methods, hooks):
            setattr(executor, executor_hook, hook)
        executor.execute_cell(cell_mock, 0)
        for hook in hooks[:3]:
            hook.assert_called_once_with(cell=cell_mock, cell_index=0)
        for hook in hooks[4:]:
            hook.assert_not_called()

    @prepare_cell_mocks(
        {
            'msg_type': 'error',
            'header': {'msg_type': 'error'},
            'content': {'ename': 'foo', 'evalue': 'bar', 'traceback': ['Boom']},
        },
        reply_msg={
            'msg_type': 'execute_reply',
            'header': {'msg_type': 'execute_reply'},
            # ERROR
            'content': {'status': 'error'},
        },
    )
    def test_error_cell_hooks(self, executor, cell_mock, message_mock):
        hooks = [MagicMock() for i in range(7)]
        for executor_hook, hook in zip(hook_methods, hooks):
            setattr(executor, executor_hook, hook)
        with self.assertRaises(CellExecutionError):
            executor.execute_cell(cell_mock, 0)
        for hook in hooks[:4]:
            hook.assert_called_once_with(cell=cell_mock, cell_index=0)
        for hook in hooks[5:]:
            hook.assert_not_called()

    @prepare_cell_mocks(
        reply_msg={
            'msg_type': 'execute_reply',
            'header': {'msg_type': 'execute_reply'},
            # ERROR
            'content': {'status': 'error'},
        }
    )
    def test_non_code_cell_hooks(self, executor, cell_mock, message_mock):
        cell_mock = NotebookNode(source='"foo" = "bar"', metadata={}, cell_type='raw', outputs=[])
        hooks = [MagicMock() for i in range(7)]
        for executor_hook, hook in zip(hook_methods, hooks):
            setattr(executor, executor_hook, hook)
        executor.execute_cell(cell_mock, 0)
        for hook in hooks[:1]:
            hook.assert_called_once_with(cell=cell_mock, cell_index=0)
        for hook in hooks[1:]:
            hook.assert_not_called()

    @prepare_cell_mocks()
    def test_async_cell_hooks(self, executor, cell_mock, message_mock):
        hooks = [AsyncMock() for i in range(7)]
        for executor_hook, hook in zip(hook_methods, hooks):
            setattr(executor, executor_hook, hook)
        executor.execute_cell(cell_mock, 0)
        for hook in hooks[:3]:
            hook.assert_called_once_with(cell=cell_mock, cell_index=0)
        for hook in hooks[4:]:
            hook.assert_not_called()

    @prepare_cell_mocks(
        {
            'msg_type': 'error',
            'header': {'msg_type': 'error'},
            'content': {'ename': 'foo', 'evalue': 'bar', 'traceback': ['Boom']},
        },
        reply_msg={
            'msg_type': 'execute_reply',
            'header': {'msg_type': 'execute_reply'},
            # ERROR
            'content': {'status': 'error'},
        },
    )
    def test_error_async_cell_hooks(self, executor, cell_mock, message_mock):
        hooks = [AsyncMock() for i in range(7)]
        for executor_hook, hook in zip(hook_methods, hooks):
            setattr(executor, executor_hook, hook)
        with self.assertRaises(CellExecutionError):
            executor.execute_cell(cell_mock, 0)
        for hook in hooks[:4]:
            hook.assert_called_once_with(cell=cell_mock, cell_index=0)
        for hook in hooks[4:]:
            hook.assert_not_called()
