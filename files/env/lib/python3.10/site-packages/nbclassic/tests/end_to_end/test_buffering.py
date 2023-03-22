"""Tests buffering of execution requests."""


from .utils import TREE_PAGE, EDITOR_PAGE


def test_kernels_buffer_without_conn(prefill_notebook):
    """Test that execution request made while disconnected is buffered."""

    notebook_frontend = prefill_notebook(["print(1 + 2)"])
    notebook_frontend.wait_for_kernel_ready()

    notebook_frontend.evaluate("() => { IPython.notebook.kernel.stop_channels }", page=EDITOR_PAGE)
    notebook_frontend.execute_cell(0)

    notebook_frontend.evaluate("() => { IPython.notebook.kernel.reconnect }", page=EDITOR_PAGE)
    notebook_frontend.wait_for_kernel_ready()

    outputs = notebook_frontend.wait_for_cell_output(0)
    assert outputs.get_inner_text().strip() == '3'


def test_buffered_cells_execute_in_order(prefill_notebook):
    """Test that buffered requests execute in order."""

    notebook_frontend = prefill_notebook(['', 'k=1', 'k+=1', 'k*=3', 'print(k)'])

    # Repeated execution of cell queued up in the kernel executes
    # each execution request in order.
    notebook_frontend.wait_for_kernel_ready()
    notebook_frontend.evaluate("() => IPython.notebook.kernel.stop_channels();", page=EDITOR_PAGE)
    # k == 1
    notebook_frontend.execute_cell(1)
    # k == 2
    notebook_frontend.execute_cell(2)
    # k == 6
    notebook_frontend.execute_cell(3)
    # k == 7
    notebook_frontend.execute_cell(2)
    notebook_frontend.execute_cell(4)
    notebook_frontend.evaluate("() => IPython.notebook.kernel.reconnect();", page=EDITOR_PAGE)
    notebook_frontend.wait_for_kernel_ready()

    outputs = notebook_frontend.wait_for_cell_output(4)
    assert outputs.get_inner_text().strip() == '7'
