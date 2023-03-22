INITIAL_CELLS = ['1', '2', '3', '4', '5', '6']
def test_move_multiselection(prefill_notebook):
    notebook = prefill_notebook(INITIAL_CELLS)
    def assert_oder(pre_message, expected_state):
        for i in range(len(expected_state)):
            assert expected_state[i] == notebook.get_cell_contents(i), f"{pre_message}: Verify that cell {i} has for content: {expected_state[i]} found: {notebook.get_cell_contents(i)}"
    
    # Select 3 first cells
    notebook.select_cell_range(0, 2)
    notebook.browser.execute_script(
        "Jupyter.notebook.move_selection_up();"   
    )
    # Should not move up at top
    assert_oder('move up at top', ['1', '2', '3', '4', '5','6'])

    # We do not need to reselect, move/up down should keep the selection.
    notebook.browser.execute_script(
        "Jupyter.notebook.move_selection_down();"
    )
    notebook.browser.execute_script(
        "Jupyter.notebook.move_selection_down();"
    )
    notebook.browser.execute_script(
        "Jupyter.notebook.move_selection_down();"
    )
    
    # 3 times down should move the 3 selected cells to the bottom
    assert_oder("move down to bottom", ['4', '5', '6', '1', '2', '3'])
    notebook.browser.execute_script(
        "Jupyter.notebook.move_selection_down();"
    )

    # They can't go any futher
    assert_oder("move down to bottom", ['4', '5', '6', '1', '2', '3'])

    notebook.browser.execute_script(
        "Jupyter.notebook.move_selection_up();"   
    )
    notebook.browser.execute_script(
        "Jupyter.notebook.move_selection_up();"   
    )
    notebook.browser.execute_script(
        "Jupyter.notebook.move_selection_up();"   
    )

    # Bring them back on top
    assert_oder('move up at top', ['1', '2', '3', '4', '5','6'])
