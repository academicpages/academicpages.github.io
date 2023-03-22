"""Test cell multiselect move"""


from .utils import EDITOR_PAGE


INITIAL_CELLS = ['1', '2', '3', '4', '5', '6']


def test_move_multiselection(prefill_notebook):
    notebook_frontend = prefill_notebook(INITIAL_CELLS)

    def assert_order(pre_message, expected_state):
        for i in range(len(expected_state)):
            assert expected_state[i] == notebook_frontend.get_cell_contents(
                i), f"{pre_message}: Verify that cell {i} has for content: {expected_state[i]} found: {notebook_frontend.get_cell_contents(i)}"

    # Select 3 first cells
    notebook_frontend.select_cell_range(0, 2)
    notebook_frontend.evaluate(
        "Jupyter.notebook.move_selection_up();",
        EDITOR_PAGE
    )
    # Should not move up at top
    assert_order('move up at top', ['1', '2', '3', '4', '5', '6'])

    # We do not need to reselect, move/up down should keep the selection.
    notebook_frontend.evaluate(
        "Jupyter.notebook.move_selection_down();",
        EDITOR_PAGE
    )
    notebook_frontend.evaluate(
        "Jupyter.notebook.move_selection_down();",
        EDITOR_PAGE
    )
    notebook_frontend.evaluate(
        "Jupyter.notebook.move_selection_down();",
        EDITOR_PAGE
    )

    # 3 times down should move the 3 selected cells to the bottom
    assert_order("move down to bottom", ['4', '5', '6', '1', '2', '3'])
    notebook_frontend.evaluate(
        "Jupyter.notebook.move_selection_down();",
        EDITOR_PAGE
    )

    # They can't go any futher
    assert_order("move down to bottom", ['4', '5', '6', '1', '2', '3'])

    notebook_frontend.evaluate(
        "Jupyter.notebook.move_selection_up();",
        EDITOR_PAGE
    )
    notebook_frontend.evaluate(
        "Jupyter.notebook.move_selection_up();",
        EDITOR_PAGE
    )
    notebook_frontend.evaluate(
        "Jupyter.notebook.move_selection_up();",
        EDITOR_PAGE
    )

    # Bring them back on top
    assert_order('move up at top', ['1', '2', '3', '4', '5', '6'])
