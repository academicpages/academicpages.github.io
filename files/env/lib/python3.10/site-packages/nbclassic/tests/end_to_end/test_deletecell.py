"""Test cell deletion"""


from .utils import TREE_PAGE, EDITOR_PAGE


def cell_is_deletable(notebook, index):
    JS = f'() => {{ return Jupyter.notebook.get_cell({index}).is_deletable(); }}'
    return notebook.evaluate(JS, EDITOR_PAGE)


def remove_all_cells(notebook):
    for i in range(len(notebook.cells)):
        notebook.delete_cell(0)


INITIAL_CELLS = ['print("a")', 'print("b")', 'print("c")']


def test_delete_cells(notebook_frontend):
    a, b, c = INITIAL_CELLS
    notebook_frontend.populate(INITIAL_CELLS)

    # Validate initial state
    assert notebook_frontend.get_cells_contents() == [a, b, c]
    for cell in range(0, 3):
        assert cell_is_deletable(notebook_frontend, cell)

    notebook_frontend.set_cell_metadata(0, 'deletable', 'false')
    notebook_frontend.set_cell_metadata(1, 'deletable', 0
    )
    assert not cell_is_deletable(notebook_frontend, 0)
    assert cell_is_deletable(notebook_frontend, 1)
    assert cell_is_deletable(notebook_frontend, 2)

    # Try to delete cell a (should not be deleted)
    notebook_frontend.delete_cell(0)
    assert notebook_frontend.get_cells_contents() == [a, b, c]

    # Try to delete cell b (should succeed)
    notebook_frontend.delete_cell(1)
    assert notebook_frontend.get_cells_contents() == [a, c]

    # Try to delete cell c (should succeed)
    notebook_frontend.delete_cell(1)
    assert notebook_frontend.get_cells_contents() == [a]

    # Change the deletable state of cell a
    notebook_frontend.set_cell_metadata(0, 'deletable', 'true')

    # Try to delete cell a (should succeed)
    notebook_frontend.delete_cell(0)
    assert len(notebook_frontend.cells) == 1 # it contains an empty cell

    # Make sure copied cells are deletable
    notebook_frontend.edit_cell(index=0, content=a)
    notebook_frontend.set_cell_metadata(0, 'deletable', 'false')
    assert not cell_is_deletable(notebook_frontend, 0)
    notebook_frontend.to_command_mode()
    notebook_frontend.type_active('cv')
    assert len(notebook_frontend.cells) == 2
    assert cell_is_deletable(notebook_frontend, 1)

    notebook_frontend.set_cell_metadata(0, 'deletable', 'true')  # to perform below test, remove all the cells
    notebook_frontend.delete_all_cells()
    assert len(notebook_frontend.cells) == 1    # notebook should create one automatically on empty notebook
