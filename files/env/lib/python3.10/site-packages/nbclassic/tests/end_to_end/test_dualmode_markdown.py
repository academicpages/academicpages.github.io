"""Test markdown"""


from .utils import EDITOR_PAGE, validate_dualmode_state


def test_dualmode_markdown(notebook_frontend):
    def is_cell_rendered(index):
        JS = f'() => {{ return !!IPython.notebook.get_cell({index}).rendered; }}'
        return notebook_frontend.evaluate(JS, EDITOR_PAGE)

    a = 'print("a")'
    index = 1
    notebook_frontend.append(a)

    # Markdown rendering / unrendering
    notebook_frontend.focus_cell(index)
    validate_dualmode_state(notebook_frontend, 'command', index)
    notebook_frontend.press("m", EDITOR_PAGE)
    assert notebook_frontend.get_cell_type(index) == 'markdown'
    assert not is_cell_rendered(index)  # cell is not rendered

    notebook_frontend.press("Enter", EDITOR_PAGE)  # cell is unrendered
    assert not is_cell_rendered(index)  # cell is not rendered
    validate_dualmode_state(notebook_frontend, 'edit', index)

    notebook_frontend.press("Enter", EDITOR_PAGE, [notebook_frontend.get_platform_modifier_key()])
    assert is_cell_rendered(index)  # cell is rendered with crtl+enter
    validate_dualmode_state(notebook_frontend, 'command', index)

    notebook_frontend.press("Enter", EDITOR_PAGE)  # cell is unrendered
    assert not is_cell_rendered(index)  # cell is not rendered

    notebook_frontend.focus_cell(index - 1)
    assert not is_cell_rendered(index)  # Select index-1; cell index is still not rendered
    validate_dualmode_state(notebook_frontend, 'command', index - 1)

    notebook_frontend.focus_cell(index)
    validate_dualmode_state(notebook_frontend, 'command', index)
    notebook_frontend.press("Enter", EDITOR_PAGE, [notebook_frontend.get_platform_modifier_key()])
    assert is_cell_rendered(index)  # Cell is rendered

    notebook_frontend.focus_cell(index - 1)
    validate_dualmode_state(notebook_frontend, 'command', index - 1)

    notebook_frontend.press("Enter", EDITOR_PAGE, ['Shift'])
    validate_dualmode_state(notebook_frontend, 'command', index)
    assert is_cell_rendered(index)  # Cell is rendered

    notebook_frontend.press("Enter", EDITOR_PAGE, ['Shift'])
    validate_dualmode_state(notebook_frontend, 'edit', index + 1)
    assert is_cell_rendered(index)  # Cell is rendered
