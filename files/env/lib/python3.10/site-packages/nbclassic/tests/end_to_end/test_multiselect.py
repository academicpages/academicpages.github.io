"""Test cell multiselection operations"""


from .utils import EDITOR_PAGE


INITIAL_CELLS = ['print("a")', 'print("b")', 'print("c")']


def test_multiselect(prefill_notebook):
    notebook_frontend = prefill_notebook(INITIAL_CELLS)

    def extend_selection_by(delta):
        notebook_frontend.evaluate(
            f"Jupyter.notebook.extend_selection_by({delta});", EDITOR_PAGE)

    def n_selected_cells():
        return notebook_frontend.evaluate(
            "() => { return Jupyter.notebook.get_selected_cells().length; }", EDITOR_PAGE)

    notebook_frontend.focus_cell(0)
    assert n_selected_cells() == 1

    # Check that only one cell is selected according to CSS classes as well
    selected_css = notebook_frontend.locate_all(
        '.cell.jupyter-soft-selected, .cell.selected', EDITOR_PAGE)
    assert len(selected_css) == 1

    # Extend the selection down one
    extend_selection_by(1)
    assert n_selected_cells() == 2

    # Contract the selection up one
    extend_selection_by(-1)
    assert n_selected_cells() == 1

    # Extend the selection up one
    notebook_frontend.focus_cell(1)
    extend_selection_by(-1)
    assert n_selected_cells() == 2

    # Convert selected cells to Markdown
    notebook_frontend.evaluate("Jupyter.notebook.cells_to_markdown();", EDITOR_PAGE)
    cell_types = notebook_frontend.evaluate(
        "() => { return Jupyter.notebook.get_cells().map(c => c.cell_type) }", EDITOR_PAGE)
    assert cell_types == ['markdown', 'markdown', 'code']
    # One cell left selected after conversion
    assert n_selected_cells() == 1

    # Convert selected cells to raw
    notebook_frontend.focus_cell(1)
    extend_selection_by(1)
    assert n_selected_cells() == 2
    notebook_frontend.evaluate("Jupyter.notebook.cells_to_raw();", EDITOR_PAGE)
    cell_types = notebook_frontend.evaluate(
        "() => { return Jupyter.notebook.get_cells().map(c => c.cell_type) }", EDITOR_PAGE)
    assert cell_types == ['markdown', 'raw', 'raw']
    # One cell left selected after conversion
    assert n_selected_cells() == 1

    # Convert selected cells to code
    notebook_frontend.focus_cell(0)
    extend_selection_by(2)
    assert n_selected_cells() == 3
    notebook_frontend.evaluate("Jupyter.notebook.cells_to_code();", EDITOR_PAGE)
    cell_types = notebook_frontend.evaluate(
        "() => { return Jupyter.notebook.get_cells().map(c => c.cell_type) }", EDITOR_PAGE)
    assert cell_types == ['code'] * 3
    # One cell left selected after conversion
    assert n_selected_cells() == 1
