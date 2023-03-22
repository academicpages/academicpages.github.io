''' Test keyboard invoked execution '''

from selenium.webdriver.common.keys import Keys

from .utils import shift, cmdtrl, alt, validate_dualmode_state

INITIAL_CELLS = ['', 'print("a")', 'print("b")', 'print("c")']

def test_dualmode_execute(prefill_notebook):
    notebook = prefill_notebook(INITIAL_CELLS)
    for i in range(1, 4):
        notebook.execute_cell(i)

    #shift-enter
    #last cell in notebook
    base_index = 3
    notebook.focus_cell(base_index)
    shift(notebook.browser, Keys.ENTER) #creates one cell
    validate_dualmode_state(notebook, 'edit', base_index + 1)

    #Not last cell in notebook & starts in edit mode
    notebook.focus_cell(base_index)
    notebook.body.send_keys(Keys.ENTER) #Enter edit mode
    validate_dualmode_state(notebook, 'edit', base_index)
    shift(notebook.browser, Keys.ENTER) #creates one cell
    validate_dualmode_state(notebook, 'command', base_index + 1)

    #Starts in command mode
    notebook.body.send_keys('k')
    validate_dualmode_state(notebook, 'command', base_index)
    shift(notebook.browser, Keys.ENTER) #creates one cell
    validate_dualmode_state(notebook, 'command', base_index + 1)


    #Ctrl-enter
    #Last cell in notebook
    base_index += 1
    cmdtrl(notebook.browser, Keys.ENTER)
    validate_dualmode_state(notebook, 'command', base_index)

    #Not last cell in notebook & stats in edit mode
    notebook.focus_cell(base_index - 1)
    notebook.body.send_keys(Keys.ENTER) #Enter edit mode
    validate_dualmode_state(notebook, 'edit', base_index - 1)
    cmdtrl(notebook.browser, Keys.ENTER)

    #Starts in command mode
    notebook.body.send_keys('j')
    validate_dualmode_state(notebook, 'command', base_index)
    cmdtrl(notebook.browser, Keys.ENTER)
    validate_dualmode_state(notebook, 'command', base_index)


    #Alt-enter
    #Last cell in notebook
    alt(notebook.browser, Keys.ENTER)
    validate_dualmode_state(notebook, 'edit', base_index + 1)
    #Not last cell in notebook &starts in edit mode
    notebook.focus_cell(base_index)
    notebook.body.send_keys(Keys.ENTER) #Enter edit mode
    validate_dualmode_state(notebook, 'edit', base_index)
    alt(notebook.browser, Keys.ENTER)
    validate_dualmode_state(notebook, 'edit', base_index + 1)
    #starts in command mode
    notebook.body.send_keys(Keys.ESCAPE, 'k')
    validate_dualmode_state(notebook, 'command', base_index)
    alt(notebook.browser, Keys.ENTER)
    validate_dualmode_state(notebook, 'edit', base_index + 1)


    #Notebook will now have 8 cells, the index of the last cell will be 7
    assert len(notebook) == 8 #Cells where added
    notebook.focus_cell(7)
    validate_dualmode_state(notebook, 'command', 7)
