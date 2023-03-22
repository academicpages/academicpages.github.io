"""Test keyboard invoked execution"""


from .utils import EDITOR_PAGE, validate_dualmode_state


INITIAL_CELLS = ['', 'print("a")', 'print("b")', 'print("c")']


def test_dualmode_execute(prefill_notebook):
    notebook_frontend = prefill_notebook(INITIAL_CELLS)
    for i in range(1, 4):
        notebook_frontend.execute_cell(i)

    # shift-enter
    # ...........
    # last cell in notebook
    base_index = 3
    notebook_frontend.focus_cell(base_index)
    notebook_frontend.press("Enter", EDITOR_PAGE, ['Shift'])  # creates one cell
    validate_dualmode_state(notebook_frontend, 'edit', base_index + 1)
    # ...............................................
    # Not last cell in notebook & starts in edit mode
    notebook_frontend.focus_cell(base_index)
    notebook_frontend.press("Enter", EDITOR_PAGE)  # Enter edit mode
    validate_dualmode_state(notebook_frontend, 'edit', base_index)
    notebook_frontend.press("Enter", EDITOR_PAGE, ['Shift'])  # creates one cell
    validate_dualmode_state(notebook_frontend, 'command', base_index + 1)
    # ......................
    # Starts in command mode
    notebook_frontend.press('k', EDITOR_PAGE)
    validate_dualmode_state(notebook_frontend, 'command', base_index)
    notebook_frontend.press("Enter", EDITOR_PAGE, ['Shift'])  # creates one cell
    validate_dualmode_state(notebook_frontend, 'command', base_index + 1)

    # Ctrl-enter
    # ..........
    # Last cell in notebook
    base_index += 1
    notebook_frontend.press("Enter", EDITOR_PAGE, [notebook_frontend.get_platform_modifier_key()])
    validate_dualmode_state(notebook_frontend, 'command', base_index)
    # ...............................................
    # Not last cell in notebook & stats in edit mode
    notebook_frontend.focus_cell(base_index - 1)
    notebook_frontend.press("Enter", EDITOR_PAGE)  # Enter edit mode
    validate_dualmode_state(notebook_frontend, 'edit', base_index - 1)
    notebook_frontend.press("Enter", EDITOR_PAGE, [notebook_frontend.get_platform_modifier_key()])
    # ...............................................
    # Starts in command mode
    notebook_frontend.press('j', EDITOR_PAGE)
    validate_dualmode_state(notebook_frontend, 'command', base_index)
    notebook_frontend.press("Enter", EDITOR_PAGE, [notebook_frontend.get_platform_modifier_key()])
    validate_dualmode_state(notebook_frontend, 'command', base_index)

    # Alt-enter
    # ...............................................
    # Last cell in notebook
    notebook_frontend.press("Enter", EDITOR_PAGE, ['Alt'])
    validate_dualmode_state(notebook_frontend, 'edit', base_index + 1)
    # Not last cell in notebook &starts in edit mode
    notebook_frontend.focus_cell(base_index)
    notebook_frontend.press("Enter", EDITOR_PAGE)  # Enter edit mode
    validate_dualmode_state(notebook_frontend, 'edit', base_index)
    notebook_frontend.press("Enter", EDITOR_PAGE, ['Alt'])
    validate_dualmode_state(notebook_frontend, 'edit', base_index + 1)
    # starts in command mode
    notebook_frontend.press("Escape", EDITOR_PAGE)
    notebook_frontend.press('k', EDITOR_PAGE)
    validate_dualmode_state(notebook_frontend, 'command', base_index)
    notebook_frontend.press("Enter", EDITOR_PAGE, ['Alt'])
    validate_dualmode_state(notebook_frontend, 'edit', base_index + 1)

    # Notebook will now have 8 cells, the index of the last cell will be 7
    assert len(notebook_frontend.cells) == 8  # Cells were added
    notebook_frontend.focus_cell(7)
    validate_dualmode_state(notebook_frontend, 'command', 7)
