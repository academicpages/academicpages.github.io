"""Test keyboard shortcuts that change the cell's mode."""

def test_dualmode_cellmode(notebook):
    def get_cell_cm_mode(index):
        code_mirror_mode = notebook.browser.execute_script(
            "return Jupyter.notebook.get_cell(%s).code_mirror.getMode().name;"%index)
        return code_mirror_mode
    
    
    index = 0
    a = 'hello\nmulti\nline'
    
    notebook.edit_cell(index=index, content=a)

    """check for the default cell type"""
    notebook.to_command_mode()
    notebook.body.send_keys("r")
    assert notebook.get_cell_type(index) == 'raw'
    assert get_cell_cm_mode(index) == 'null'

    """check cell type after changing to markdown"""
    notebook.body.send_keys("1")
    assert notebook.get_cell_type(index) == 'markdown'
    assert notebook.get_cell_contents(index) == '# ' + a
    assert get_cell_cm_mode(index) == 'ipythongfm'

    notebook.body.send_keys("2")
    assert notebook.get_cell_type(index) == 'markdown'
    assert notebook.get_cell_contents(index) == '## ' + a
    
    notebook.body.send_keys("3")
    assert notebook.get_cell_type(index) == 'markdown'
    assert notebook.get_cell_contents(index) == '### ' + a

    notebook.body.send_keys("4")
    assert notebook.get_cell_type(index) == 'markdown'
    assert notebook.get_cell_contents(index) == '#### ' + a

    notebook.body.send_keys("5")
    assert notebook.get_cell_type(index) == 'markdown'
    assert notebook.get_cell_contents(index) == '##### ' + a

    notebook.body.send_keys("6")
    assert notebook.get_cell_type(index) == 'markdown'
    assert notebook.get_cell_contents(index) == '###### ' + a

    notebook.body.send_keys("m")
    assert notebook.get_cell_type(index) == 'markdown'
    assert notebook.get_cell_contents(index) == '###### ' + a

    notebook.body.send_keys("y")
    assert notebook.get_cell_type(index) == 'code'
    assert notebook.get_cell_contents(index) == '###### ' + a
    assert get_cell_cm_mode(index) == 'ipython'

    notebook.body.send_keys("1")
    assert notebook.get_cell_type(index) == 'markdown'
    assert notebook.get_cell_contents(index) == '# ' + a