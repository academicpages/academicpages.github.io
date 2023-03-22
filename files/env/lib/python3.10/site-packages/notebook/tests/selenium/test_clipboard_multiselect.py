"""Tests clipboard by copying, cutting and pasting multiple cells"""
from selenium.webdriver.common.keys import Keys
from .utils import wait_for_selector, wait_for_xpath

def test_clipboard_multiselect(prefill_notebook):
    notebook = prefill_notebook(['', '1', '2', '3', '4', '5a', '6b', '7c', '8d'])

    assert notebook.get_cells_contents() == ['', '1', '2', '3', '4', '5a', '6b', '7c', '8d']
    
    # Select the first 3 cells with value and replace the last 3
    [notebook.body.send_keys(Keys.UP) for i in range(8)]
    notebook.select_cell_range(1, 3)
    notebook.body.send_keys("c")
    notebook.select_cell_range(6, 8)
    wait_for_xpath(notebook.browser, '//a[text()="Edit"]', single=True).click()
    wait_for_selector(notebook.browser, '#paste_cell_replace', single=True).click()

    assert notebook.get_cells_contents() == ['', '1', '2', '3', '4', '5a', '1', '2', '3']
    
    # Select the last four cells, cut them and paste them below the first cell
    notebook.select_cell_range(5, 8)
    wait_for_selector(notebook.browser, '.fa-cut.fa', single=True).click()
    for i in range(8):
        notebook.body.send_keys(Keys.UP)
    notebook.body.send_keys("v")

    assert notebook.get_cells_contents() == ['', '5a', '1', '2', '3', '1', '2', '3', '4']
