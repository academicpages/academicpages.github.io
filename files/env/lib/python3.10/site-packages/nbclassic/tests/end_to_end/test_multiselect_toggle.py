"""Test multiselect toggle"""


from .utils import EDITOR_PAGE


INITIAL_CELLS = ['print("a")', 'print("b")', 'print("c")']


def test_multiselect_toggle(prefill_notebook):
    notebook_frontend = prefill_notebook(INITIAL_CELLS)

    def extend_selection_by(delta):
        notebook_frontend.evaluate(
            f"Jupyter.notebook.extend_selection_by({delta});", EDITOR_PAGE)

    def n_selected_cells():
        return notebook_frontend.evaluate(
            "() => { return Jupyter.notebook.get_selected_cells().length; }", EDITOR_PAGE)

    def select_cells():
        notebook_frontend.focus_cell(0)
        extend_selection_by(2)

    # Test that cells, which start off not collapsed, are collapsed after
    # calling the multiselected cell toggle.
    select_cells()
    assert n_selected_cells() == 3
    notebook_frontend.evaluate("Jupyter.notebook.execute_selected_cells();", EDITOR_PAGE)
    select_cells()
    notebook_frontend.evaluate("Jupyter.notebook.toggle_cells_outputs();", EDITOR_PAGE)
    cell_output_states = notebook_frontend.evaluate(
        "() => { return Jupyter.notebook.get_cells().map(c => c.collapsed) }", EDITOR_PAGE)
    assert cell_output_states == [False] * 3, "ensure that all cells are not collapsed"

    # Test that cells, which start off not scrolled are scrolled after
    # calling the multiselected scroll toggle.
    select_cells()
    assert n_selected_cells() == 3
    notebook_frontend.evaluate("Jupyter.notebook.toggle_cells_outputs_scroll();", EDITOR_PAGE)
    cell_scrolled_states = notebook_frontend.evaluate(
        "() => { return Jupyter.notebook.get_cells().map(c => c.output_area.scroll_state) }", EDITOR_PAGE)
    assert all(cell_scrolled_states), "ensure that all have scrolling enabled"

    # Test that cells, which start off not cleared are cleared after
    # calling the multiselected scroll toggle.
    select_cells()
    assert n_selected_cells() == 3
    notebook_frontend.evaluate("Jupyter.notebook.clear_cells_outputs();", EDITOR_PAGE)
    cell_outputs_cleared = notebook_frontend.evaluate(
        "() => { return Jupyter.notebook.get_cells().map(c => c.output_area.element.html()) }", EDITOR_PAGE)
    assert cell_outputs_cleared == [""] * 3, "ensure that all cells are cleared"
