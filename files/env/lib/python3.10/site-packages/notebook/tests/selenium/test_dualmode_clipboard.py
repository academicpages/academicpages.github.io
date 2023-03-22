"""Test"""
from .utils import shift, validate_dualmode_state

INITIAL_CELLS = ['', 'print("a")', 'print("b")', 'print("c")']

def test_dualmode_clipboard(prefill_notebook):
    notebook = prefill_notebook(INITIAL_CELLS)
    _, a, b, c = INITIAL_CELLS
    for i in range(1, 4):
        notebook.execute_cell(i)

    #Copy/past/cut
    num_cells = len(notebook.cells)
    assert notebook.get_cell_contents(1) == a #Cell 1 is a

    notebook.focus_cell(1)
    notebook.body.send_keys("x") #Cut
    validate_dualmode_state(notebook, 'command', 1)
    assert notebook.get_cell_contents(1) == b #Cell 2 is now where cell 1 was
    assert len(notebook.cells) == num_cells-1 #A cell was removed

    notebook.focus_cell(2)
    notebook.body.send_keys("v") #Paste
    validate_dualmode_state(notebook, 'command', 3)
    assert notebook.get_cell_contents(3) == a #Cell 3 has the cut contents
    assert len(notebook.cells) == num_cells   #A cell was added

    notebook.body.send_keys("v") #Paste
    validate_dualmode_state(notebook, 'command', 4)
    assert notebook.get_cell_contents(4) == a #Cell a has the cut contents
    assert len(notebook.cells) == num_cells+1 #A cell was added

    notebook.focus_cell(1)
    notebook.body.send_keys("c") #Copy
    validate_dualmode_state(notebook, 'command', 1)
    assert notebook.get_cell_contents(1) == b #Cell 1 is b

    notebook.focus_cell(2)
    notebook.body.send_keys("c") #Copy
    validate_dualmode_state(notebook, 'command', 2)
    assert notebook.get_cell_contents(2) == c #Cell 2 is c

    notebook.focus_cell(4)
    notebook.body.send_keys("v") #Paste
    validate_dualmode_state(notebook, 'command', 5)
    assert notebook.get_cell_contents(2) == c #Cell 2 has the copied contents
    assert notebook.get_cell_contents(5) == c #Cell 5 has the copied contents
    assert len(notebook.cells) == num_cells+2 #A cell was added

    notebook.focus_cell(0)
    shift(notebook.browser, 'v') #Paste
    validate_dualmode_state(notebook, 'command', 0)
    assert notebook.get_cell_contents(0) == c #Cell 0 has the copied contents
    assert len(notebook.cells) == num_cells+3 #A cell was added
