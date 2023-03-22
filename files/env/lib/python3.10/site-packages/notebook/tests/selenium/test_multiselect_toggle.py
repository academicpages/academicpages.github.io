INITIAL_CELLS = ['print("a")', 'print("b")', 'print("c")']
def test_multiselect_toggle(prefill_notebook):
    notebook = prefill_notebook(INITIAL_CELLS)
    def extend_selection_by(delta):
        notebook.browser.execute_script(
            "Jupyter.notebook.extend_selection_by(arguments[0]);", delta)

    def n_selected_cells():
        return notebook.browser.execute_script(
            "return Jupyter.notebook.get_selected_cells().length;")

    def select_cells():
        notebook.focus_cell(0)
        extend_selection_by(2)

    # Test that cells, which start off not collapsed, are collapsed after
    # calling the multiselected cell toggle.
    select_cells()
    assert n_selected_cells() == 3
    notebook.browser.execute_script("Jupyter.notebook.execute_selected_cells();")
    select_cells()
    notebook.browser.execute_script("Jupyter.notebook.toggle_cells_outputs();")
    cell_output_states = notebook.browser.execute_script(
        "return Jupyter.notebook.get_cells().map(c => c.collapsed)")
    assert cell_output_states == [False] * 3, "ensure that all cells are not collapsed"

    # Test that cells, which start off not scrolled are scrolled after
    # calling the multiselected scroll toggle.
    select_cells()
    assert n_selected_cells() == 3
    notebook.browser.execute_script("Jupyter.notebook.toggle_cells_outputs_scroll();")
    cell_scrolled_states = notebook.browser.execute_script(
        "return Jupyter.notebook.get_cells().map(c => c.output_area.scroll_state)")
    assert all(cell_scrolled_states), "ensure that all have scrolling enabled"

    # Test that cells, which start off not cleared are cleared after
    # calling the multiselected scroll toggle.
    select_cells()
    assert n_selected_cells() == 3
    notebook.browser.execute_script("Jupyter.notebook.clear_cells_outputs();")
    cell_outputs_cleared = notebook.browser.execute_script(
        "return Jupyter.notebook.get_cells().map(c => c.output_area.element.html())")
    assert cell_outputs_cleared == [""] * 3, "ensure that all cells are cleared"
