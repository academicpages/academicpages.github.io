"""Tests clipboard by copying, cutting and pasting multiple cells"""


from .utils import TREE_PAGE, EDITOR_PAGE


# Optionally perfom this test with Ctrl+c and Ctrl+v
def test_clipboard_multiselect(prefill_notebook):
    notebook = prefill_notebook(['', '1', '2', '3', '4', '5a', '6b', '7c', '8d'])

    assert notebook.get_cells_contents() == ['', '1', '2', '3', '4', '5a', '6b', '7c', '8d']

    # Copy the first 3 cells
    # Paste the values copied from the first three cells into the last 3 cells 

    # Selecting the fist 3 cells
    notebook.select_cell_range(1, 3)

    # Copy those selected cells
    notebook.try_click_selector('#editlink', page=EDITOR_PAGE)
    notebook.try_click_selector('//*[@id="copy_cell"]/a/span[1]', page=EDITOR_PAGE)

    # Select the last 3 cells
    notebook.select_cell_range(6, 8)

    # Paste the cells in clipboard onto selected cells
    notebook.try_click_selector('#editlink', page=EDITOR_PAGE)
    notebook.try_click_selector('//*[@id="paste_cell_replace"]/a', page=EDITOR_PAGE)

    assert notebook.get_cells_contents() == ['', '1', '2', '3', '4', '5a', '1', '2', '3']

    # Select the last four cells, cut them and paste them below the first cell

    # Select the last 4 cells
    notebook.select_cell_range(5, 8)

    # Click Edit button and the select cut button
    notebook.try_click_selector('#editlink', page=EDITOR_PAGE)
    notebook.try_click_selector('//*[@id="cut_cell"]/a', page=EDITOR_PAGE)

    # Select the first cell
    notebook.select_cell_range(0, 0)

    # Paste the cells in our clipboard below this first cell we are focused at
    notebook.try_click_selector('#editlink', page=EDITOR_PAGE)
    notebook.try_click_selector('//*[@id="paste_cell_below"]/a/span[1]', page=EDITOR_PAGE)

    assert notebook.get_cells_contents() == ['', '5a', '1', '2', '3', '1', '2', '3', '4']
