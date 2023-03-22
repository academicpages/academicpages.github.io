'''Test'''

from selenium.webdriver.common.keys import Keys

from .utils import cmdtrl, shift, validate_dualmode_state

def test_dualmode_markdown(notebook):
    def is_cell_rendered(index):
        JS = 'return !!IPython.notebook.get_cell(%s).rendered;'%index
        return notebook.browser.execute_script(JS)


    a = 'print("a")'
    index = 1
    notebook.append(a)

    #Markdown rendering / unrendering
    notebook.focus_cell(index)
    validate_dualmode_state(notebook, 'command', index)
    notebook.body.send_keys("m")
    assert notebook.get_cell_type(index) == 'markdown'
    assert not is_cell_rendered(index) #cell is not rendered
    
    notebook.body.send_keys(Keys.ENTER)#cell is unrendered
    assert not is_cell_rendered(index) #cell is not rendered
    validate_dualmode_state(notebook, 'edit', index)

    cmdtrl(notebook.browser, Keys.ENTER)
    assert is_cell_rendered(index) #cell is rendered with crtl+enter
    validate_dualmode_state(notebook, 'command', index)

    notebook.body.send_keys(Keys.ENTER)#cell is unrendered
    assert not is_cell_rendered(index) #cell is not rendered

    notebook.focus_cell(index - 1)
    assert not is_cell_rendered(index) #Select index-1; cell index is still not rendered
    validate_dualmode_state(notebook, 'command', index - 1)

    notebook.focus_cell(index)
    validate_dualmode_state(notebook, 'command', index)
    cmdtrl(notebook.browser, Keys.ENTER)
    assert is_cell_rendered(index)#Cell is rendered

    notebook.focus_cell(index - 1)
    validate_dualmode_state(notebook, 'command', index - 1)

    shift(notebook.browser, Keys.ENTER)
    validate_dualmode_state(notebook, 'command', index)
    assert is_cell_rendered(index)#Cell is rendered

    shift(notebook.browser, Keys.ENTER)
    validate_dualmode_state(notebook, 'edit', index + 1)
    assert is_cell_rendered(index)#Cell is rendered
