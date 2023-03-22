"""Test clipboard functionality"""


from .utils import EDITOR_PAGE, validate_dualmode_state


INITIAL_CELLS = ['', 'print("a")', 'print("b")', 'print("c")']


def test_dualmode_clipboard(prefill_notebook):
    notebook_frontend = prefill_notebook(INITIAL_CELLS)
    _, a, b, c = INITIAL_CELLS
    for i in range(1, 4):
        notebook_frontend.execute_cell(i)

    # Copy/paste/cut
    num_cells = len(notebook_frontend.cells)
    assert notebook_frontend.get_cell_contents(1) == a  # Cell 1 is a

    notebook_frontend.focus_cell(1)
    notebook_frontend.press("x", EDITOR_PAGE)  # Cut
    validate_dualmode_state(notebook_frontend, 'command', 1)
    assert notebook_frontend.get_cell_contents(1) == b  # Cell 2 is now where cell 1 was
    assert len(notebook_frontend.cells) == num_cells - 1  # A cell was removed

    notebook_frontend.focus_cell(2)
    notebook_frontend.press("v", EDITOR_PAGE)  # Paste
    validate_dualmode_state(notebook_frontend, 'command', 3)
    assert notebook_frontend.get_cell_contents(3) == a  # Cell 3 has the cut contents
    assert len(notebook_frontend.cells) == num_cells  # A cell was added

    notebook_frontend.press("v", EDITOR_PAGE)  # Paste
    validate_dualmode_state(notebook_frontend, 'command', 4)
    assert notebook_frontend.get_cell_contents(4) == a  # Cell a has the cut contents
    assert len(notebook_frontend.cells) == num_cells + 1  # A cell was added

    notebook_frontend.focus_cell(1)
    notebook_frontend.press("c", EDITOR_PAGE)  # Copy
    validate_dualmode_state(notebook_frontend, 'command', 1)
    assert notebook_frontend.get_cell_contents(1) == b  # Cell 1 is b

    notebook_frontend.focus_cell(2)
    notebook_frontend.press("c", EDITOR_PAGE)  # Copy
    validate_dualmode_state(notebook_frontend, 'command', 2)
    assert notebook_frontend.get_cell_contents(2) == c  # Cell 2 is c

    notebook_frontend.focus_cell(4)
    notebook_frontend.press("v", EDITOR_PAGE)  # Paste
    validate_dualmode_state(notebook_frontend, 'command', 5)
    assert notebook_frontend.get_cell_contents(2) == c  # Cell 2 has the copied contents
    assert notebook_frontend.get_cell_contents(5) == c  # Cell 5 has the copied contents
    assert len(notebook_frontend.cells) == num_cells + 2  # A cell was added

    notebook_frontend.focus_cell(0)
    notebook_frontend.press('v', EDITOR_PAGE, ['Shift'])  # Paste
    validate_dualmode_state(notebook_frontend, 'command', 0)
    assert notebook_frontend.get_cell_contents(0) == c  # Cell 0 has the copied contents
    assert len(notebook_frontend.cells) == num_cells + 3  # A cell was added
