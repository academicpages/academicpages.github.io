"""Tests shutdown of the Kernel."""
from .utils import wait_for_selector, wait_for_xpath

def test_shutdown(notebook):
    notebook.edit_cell(content="print(21)")
    wait_for_xpath(notebook.browser, '//a[text()="Kernel"]', single=True).click()
    wait_for_selector(notebook.browser, '#shutdown_kernel', single=True).click()
    wait_for_selector(notebook.browser, '.btn.btn-default.btn-sm.btn-danger', single=True).click()

    #Wait until all shutdown modal elements disappear before trying to execute the cell
    wait_for_xpath(notebook.browser, "//div[contains(@class,'modal')]", obscures=True)
    notebook.execute_cell(0)

    assert not notebook.is_kernel_running()
    assert len(notebook.get_cell_output()) == 0