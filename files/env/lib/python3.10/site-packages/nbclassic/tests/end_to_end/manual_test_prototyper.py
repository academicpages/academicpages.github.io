"""Test basic cell execution methods, related shortcuts, and error modes

Run this manually:
    # Normal pytest run
    pytest nbclassic/tests/end_to_end/test_interrupt.py
    # with playwright debug (run and poke around in the web console)
    PWDEBUG=1 pytest -s nbclassic/tests/end_to_end/test_interrupt.py
"""


from .utils import TREE_PAGE, EDITOR_PAGE


# # Use/uncomment this for manual test prototytping
# # (the test suite will run this if it's uncommented)
# def test_do_something(notebook_frontend):
#     # Do something with the notebook_frontend here
#     notebook_frontend.add_cell()
#     notebook_frontend.add_cell()
#     assert len(notebook_frontend.cells) == 3
#
#     notebook_frontend.delete_all_cells()
#     assert len(notebook_frontend.cells) == 1
#
#     notebook_frontend.editor_page.pause()
#     cell_texts = ['aa = 1', 'bb = 2', 'cc = 3']
#     a, b, c = cell_texts
#     notebook_frontend.populate(cell_texts)
#     assert notebook_frontend.get_cells_contents() == [a, b, c]
#     notebook_frontend._pause()
