from selenium.webdriver.common.keys import Keys
from .utils import shift

INITIAL_CELLS = ['print("a")', 'print("b")', 'print("c")']

def test_insert_cell(prefill_notebook):
    notebook = prefill_notebook(INITIAL_CELLS)

    notebook.to_command_mode()
    notebook.focus_cell(2)
    notebook.convert_cell_type(2, "markdown")
    
    # insert code cell above
    notebook.current_cell.send_keys("a")
    assert notebook.get_cell_contents(2) == ""
    assert notebook.get_cell_type(2) == "code"
    assert len(notebook.cells) == 4
    
    # insert code cell below
    notebook.current_cell.send_keys("b")
    assert notebook.get_cell_contents(2) == ""
    assert notebook.get_cell_contents(3) == ""
    assert notebook.get_cell_type(3) == "code"
    assert len(notebook.cells) == 5

    notebook.edit_cell(index=1, content="cell1")
    notebook.focus_cell(1)
    notebook.current_cell.send_keys("a")
    assert notebook.get_cell_contents(1) == ""
    assert notebook.get_cell_contents(2) == "cell1"

    notebook.edit_cell(index=1, content='cell1')
    notebook.edit_cell(index=2, content='cell2')
    notebook.edit_cell(index=3, content='cell3')
    notebook.focus_cell(2)
    notebook.current_cell.send_keys("b")
    assert notebook.get_cell_contents(1) == "cell1"
    assert notebook.get_cell_contents(2) == "cell2"
    assert notebook.get_cell_contents(3) == ""
    assert notebook.get_cell_contents(4) == "cell3"

    # insert above multiple selected cells
    notebook.focus_cell(1)
    shift(notebook.browser, Keys.DOWN)
    notebook.current_cell.send_keys('a')
    
    # insert below multiple selected cells
    notebook.focus_cell(2)
    shift(notebook.browser, Keys.DOWN)
    notebook.current_cell.send_keys('b')
    assert notebook.get_cells_contents()[1:5] == ["", "cell1", "cell2", ""]
