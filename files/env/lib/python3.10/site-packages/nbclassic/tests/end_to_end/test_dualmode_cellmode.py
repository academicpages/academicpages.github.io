"""Test keyboard shortcuts that change the cell's mode."""


from .utils import EDITOR_PAGE


def test_dualmode_cellmode(notebook_frontend):
    def get_cell_cm_mode(index):
        code_mirror_mode = notebook_frontend.evaluate(
            f"() => {{ return Jupyter.notebook.get_cell({index}).code_mirror.getMode().name; }}",
            page=EDITOR_PAGE
        )
        return code_mirror_mode

    index = 0
    a = 'hello\nmulti\nline'

    notebook_frontend.edit_cell(index=index, content=a)

    """check for the default cell type"""
    notebook_frontend.to_command_mode()
    notebook_frontend.press("r", page=EDITOR_PAGE)
    assert notebook_frontend.get_cell_type(index) == 'raw'
    assert get_cell_cm_mode(index) == 'null'

    """check cell type after changing to markdown"""
    notebook_frontend.press("1", page=EDITOR_PAGE)
    assert notebook_frontend.get_cell_type(index) == 'markdown'
    assert notebook_frontend.get_cell_contents(index) == '# ' + a
    assert get_cell_cm_mode(index) == 'ipythongfm'

    notebook_frontend.press("2", page=EDITOR_PAGE)
    assert notebook_frontend.get_cell_type(index) == 'markdown'
    assert notebook_frontend.get_cell_contents(index) == '## ' + a

    notebook_frontend.press("3", page=EDITOR_PAGE)
    assert notebook_frontend.get_cell_type(index) == 'markdown'
    assert notebook_frontend.get_cell_contents(index) == '### ' + a

    notebook_frontend.press("4", page=EDITOR_PAGE)
    assert notebook_frontend.get_cell_type(index) == 'markdown'
    assert notebook_frontend.get_cell_contents(index) == '#### ' + a

    notebook_frontend.press("5", page=EDITOR_PAGE)
    assert notebook_frontend.get_cell_type(index) == 'markdown'
    assert notebook_frontend.get_cell_contents(index) == '##### ' + a

    notebook_frontend.press("6", page=EDITOR_PAGE)
    assert notebook_frontend.get_cell_type(index) == 'markdown'
    assert notebook_frontend.get_cell_contents(index) == '###### ' + a

    notebook_frontend.press("m", page=EDITOR_PAGE)
    assert notebook_frontend.get_cell_type(index) == 'markdown'
    assert notebook_frontend.get_cell_contents(index) == '###### ' + a

    notebook_frontend.press("y", page=EDITOR_PAGE)
    assert notebook_frontend.get_cell_type(index) == 'code'
    assert notebook_frontend.get_cell_contents(index) == '###### ' + a
    assert get_cell_cm_mode(index) == 'ipython'

    notebook_frontend.press("1", page=EDITOR_PAGE)
    assert notebook_frontend.get_cell_type(index) == 'markdown'
    assert notebook_frontend.get_cell_contents(index) == '# ' + a
