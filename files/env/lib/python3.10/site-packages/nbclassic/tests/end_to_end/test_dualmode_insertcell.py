"""Test cell insertion"""


from .utils import TREE_PAGE, EDITOR_PAGE


INITIAL_CELLS = ['print("a")', 'print("b")', 'print("c")']


def test_insert_cell(prefill_notebook):
    notebook_frontend = prefill_notebook(INITIAL_CELLS)

    notebook_frontend.to_command_mode()
    notebook_frontend.focus_cell(2)
    notebook_frontend.convert_cell_type(2, "markdown")

    # insert code cell above
    notebook_frontend.press_active("a")
    assert notebook_frontend.get_cell_contents(2).replace('\u200b', '') == ""
    # ^TODO: Why are there NBSP's in here? Might be empty cells only?
    assert notebook_frontend.get_cell_type(2) == "code"
    assert len(notebook_frontend.cells) == 4

    # insert code cell below
    notebook_frontend.press_active("b")
    assert notebook_frontend.get_cell_contents(2).replace('\u200b', '') == ""
    assert notebook_frontend.get_cell_contents(3).replace('\u200b', '') == ""
    assert notebook_frontend.get_cell_type(3) == "code"
    assert len(notebook_frontend.cells) == 5

    notebook_frontend.edit_cell(index=1, content="cell1")
    notebook_frontend.focus_cell(1)
    notebook_frontend.press_active("a")
    assert notebook_frontend.get_cell_contents(1).replace('\u200b', '') == ""
    assert notebook_frontend.get_cell_contents(2) == "cell1"

    notebook_frontend.edit_cell(index=1, content='cell1')
    notebook_frontend.edit_cell(index=2, content='cell2')
    notebook_frontend.edit_cell(index=3, content='cell3')
    notebook_frontend.focus_cell(2)
    notebook_frontend.press_active("b")
    assert notebook_frontend.get_cell_contents(1) == "cell1"
    assert notebook_frontend.get_cell_contents(2) == "cell2"
    assert notebook_frontend.get_cell_contents(3).replace('\u200b', '') == ""
    assert notebook_frontend.get_cell_contents(4) == "cell3"

    # insert above multiple selected cells
    notebook_frontend.focus_cell(1)
    notebook_frontend.press('ArrowDown', EDITOR_PAGE, ['Shift'])
    notebook_frontend.press_active('a')

    # insert below multiple selected cells
    notebook_frontend.focus_cell(2)
    notebook_frontend.press('ArrowDown', EDITOR_PAGE, ['Shift'])
    notebook_frontend.press_active('b')
    assert notebook_frontend.get_cells_contents()[1:5] == ["", "cell1", "cell2", ""]
