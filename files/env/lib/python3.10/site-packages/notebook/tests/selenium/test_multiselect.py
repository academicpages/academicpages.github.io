from selenium.webdriver.common.by import By


INITIAL_CELLS = ['print("a")', 'print("b")', 'print("c")']


def test_multiselect(prefill_notebook):
    notebook = prefill_notebook(INITIAL_CELLS)

    def extend_selection_by(delta):
        notebook.browser.execute_script(
            "Jupyter.notebook.extend_selection_by(arguments[0]);", delta)

    def n_selected_cells():
        return notebook.browser.execute_script(
            "return Jupyter.notebook.get_selected_cells().length;")

    notebook.focus_cell(0)
    assert n_selected_cells() == 1

    # Check that only one cell is selected according to CSS classes as well
    selected_css = notebook.browser.find_elements(
        By.CSS_SELECTOR,
        '.cell.jupyter-soft-selected, .cell.selected')
    assert len(selected_css) == 1

    # Extend the selection down one
    extend_selection_by(1)
    assert n_selected_cells() == 2

    # Contract the selection up one
    extend_selection_by(-1)
    assert n_selected_cells() == 1

    # Extend the selection up one
    notebook.focus_cell(1)
    extend_selection_by(-1)
    assert n_selected_cells() == 2

    # Convert selected cells to Markdown
    notebook.browser.execute_script("Jupyter.notebook.cells_to_markdown();")
    cell_types = notebook.browser.execute_script(
        "return Jupyter.notebook.get_cells().map(c => c.cell_type)")
    assert cell_types == ['markdown', 'markdown', 'code']
    # One cell left selected after conversion
    assert n_selected_cells() == 1

    # Convert selected cells to raw
    notebook.focus_cell(1)
    extend_selection_by(1)
    assert n_selected_cells() == 2
    notebook.browser.execute_script("Jupyter.notebook.cells_to_raw();")
    cell_types = notebook.browser.execute_script(
        "return Jupyter.notebook.get_cells().map(c => c.cell_type)")
    assert cell_types == ['markdown', 'raw', 'raw']
    # One cell left selected after conversion
    assert n_selected_cells() == 1

    # Convert selected cells to code
    notebook.focus_cell(0)
    extend_selection_by(2)
    assert n_selected_cells() == 3
    notebook.browser.execute_script("Jupyter.notebook.cells_to_code();")
    cell_types = notebook.browser.execute_script(
        "return Jupyter.notebook.get_cells().map(c => c.cell_type)")
    assert cell_types == ['code'] * 3
    # One cell left selected after conversion
    assert n_selected_cells() == 1
