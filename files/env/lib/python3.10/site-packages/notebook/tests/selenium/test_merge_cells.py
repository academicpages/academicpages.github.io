"""Tests the merge cell api."""

INITIAL_CELLS = [
    "foo = 5",
    "bar = 10",
    "baz = 15",
    "print(foo)",
    "print(bar)",
    "print(baz)",
]

def test_merge_cells(prefill_notebook):
    notebook = prefill_notebook(INITIAL_CELLS)
    a, b, c, d, e, f = INITIAL_CELLS

    # Before merging, there are 6 separate cells
    assert notebook.get_cells_contents() == [a, b, c, d, e, f]

    # Focus on the second cell and merge it with the cell above
    notebook.focus_cell(1)
    notebook.browser.execute_script("Jupyter.notebook.merge_cell_above();")
    merged_a_b = f"{a}\n\n{b}"
    assert notebook.get_cells_contents() == [merged_a_b, c, d, e, f]

    # Focus on the second cell and merge it with the cell below
    notebook.focus_cell(1)
    notebook.browser.execute_script("Jupyter.notebook.merge_cell_below();")
    merged_c_d = f"{c}\n\n{d}"
    assert notebook.get_cells_contents() == [merged_a_b, merged_c_d, e, f]

    # Merge everything down to a single cell with selected cells
    notebook.select_cell_range(0,3)
    notebook.browser.execute_script("Jupyter.notebook.merge_selected_cells();")
    merged_all = f"{merged_a_b}\n\n{merged_c_d}\n\n{e}\n\n{f}"
    assert notebook.get_cells_contents() == [merged_all]

