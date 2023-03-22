from selenium.webdriver.common.keys import Keys
from .utils import shift

def undelete(nb):
    nb.browser.execute_script('Jupyter.notebook.undelete_cell();')

INITIAL_CELLS = ['print("a")', 'print("b")', 'print("c")', 'print("d")']

def test_undelete_cells(prefill_notebook):
    notebook = prefill_notebook(INITIAL_CELLS)
    a, b, c, d = INITIAL_CELLS

    # Verify initial state
    assert notebook.get_cells_contents() == [a, b, c, d]

    # Delete cells [1, 2]
    notebook.focus_cell(1)
    shift(notebook.browser, Keys.DOWN)
    notebook.current_cell.send_keys('dd')
    assert notebook.get_cells_contents() == [a, d]

    # Delete new cell 1 (which contains d)
    notebook.focus_cell(1)
    notebook.current_cell.send_keys('dd')
    assert notebook.get_cells_contents() == [a]

    # Undelete d
    undelete(notebook)
    assert notebook.get_cells_contents() == [a, d]

    # Undelete b, c
    undelete(notebook)
    assert notebook.get_cells_contents() == [a, b, c, d]

    # Nothing more to undelete
    undelete(notebook)
    assert notebook.get_cells_contents() == [a, b, c, d]

    # Delete first two cells and restore
    notebook.focus_cell(0)
    shift(notebook.browser, Keys.DOWN)
    notebook.current_cell.send_keys('dd')
    assert notebook.get_cells_contents() == [c, d]
    undelete(notebook)
    assert notebook.get_cells_contents() == [a, b, c, d]

    # Delete last two cells and restore
    notebook.focus_cell(-1)
    shift(notebook.browser, Keys.UP)
    notebook.current_cell.send_keys('dd')
    assert notebook.get_cells_contents() == [a, b]
    undelete(notebook)
    assert notebook.get_cells_contents() == [a, b, c, d]

    # Merge cells [1, 2], restore the deleted one
    bc = b + "\n\n" + c
    notebook.focus_cell(1)
    shift(notebook.browser, 'j')
    shift(notebook.browser, 'm')
    assert notebook.get_cells_contents() == [a, bc, d]
    undelete(notebook)
    assert notebook.get_cells_contents() == [a, bc, c, d]

    # Merge cells [2, 3], restore the deleted one
    cd = c + "\n\n" + d
    notebook.focus_cell(-1)
    shift(notebook.browser, 'k')
    shift(notebook.browser, 'm')
    assert notebook.get_cells_contents() == [a, bc, cd]
    undelete(notebook)
    assert notebook.get_cells_contents() == [a, bc, cd, d]

    # Reset contents to [a, b, c, d] --------------------------------------
    notebook.edit_cell(index=1, content=b)
    notebook.edit_cell(index=2, content=c)
    assert notebook.get_cells_contents() == [a, b, c, d]

    # Merge cell below, restore the deleted one
    ab = a + "\n\n" + b
    notebook.focus_cell(0)
    notebook.browser.execute_script("Jupyter.notebook.merge_cell_below();")
    assert notebook.get_cells_contents() == [ab, c, d]
    undelete(notebook)
    assert notebook.get_cells_contents() == [ab, b, c, d]

    # Merge cell above, restore the deleted one
    cd = c + "\n\n" + d
    notebook.focus_cell(-1)
    notebook.browser.execute_script("Jupyter.notebook.merge_cell_above();")
    assert notebook.get_cells_contents() == [ab, b, cd]
    undelete(notebook)
    assert notebook.get_cells_contents() == [ab, b, c, cd]
