"""Tests arrow keys on both command and edit mode"""


from .utils import EDITOR_PAGE


def test_dualmode_arrows(notebook_frontend):

    # Tests in command mode.
    # Setting up the cells to test the keys to move up.
    notebook_frontend.to_command_mode()
    [notebook_frontend.press("b", page=EDITOR_PAGE) for i in range(3)]

    # Use both "k" and up arrow keys to moving up and enter a value.
    # Once located on the top cell, use the up arrow keys to prove the top cell is still selected.
    notebook_frontend.press("k", page=EDITOR_PAGE)
    notebook_frontend.press("Enter", page=EDITOR_PAGE)
    notebook_frontend.press("2", page=EDITOR_PAGE)
    notebook_frontend.to_command_mode()
    notebook_frontend.press("ArrowUp", page=EDITOR_PAGE)
    notebook_frontend.press("Enter", page=EDITOR_PAGE)
    notebook_frontend.press("1", page=EDITOR_PAGE)
    notebook_frontend.to_command_mode()
    notebook_frontend.press("k", page=EDITOR_PAGE)
    notebook_frontend.press("ArrowUp", page=EDITOR_PAGE)
    notebook_frontend.press("Enter", page=EDITOR_PAGE)
    notebook_frontend.press("0", page=EDITOR_PAGE)
    notebook_frontend.to_command_mode()
    assert notebook_frontend.get_cells_contents() == ["0", "1", "2", ""]

    # Use the "k" key on the top cell as well
    notebook_frontend.press("k", page=EDITOR_PAGE)
    notebook_frontend.press("Enter", page=EDITOR_PAGE)
    notebook_frontend.type(" edit #1", page=EDITOR_PAGE)
    notebook_frontend.to_command_mode()
    assert notebook_frontend.get_cells_contents() == ["0 edit #1", "1", "2", ""]

    # Setting up the cells to test the keys to move down
    [notebook_frontend.press("j", page=EDITOR_PAGE) for i in range(3)]
    [notebook_frontend.press("a", page=EDITOR_PAGE) for i in range(2)]
    notebook_frontend.press("k", page=EDITOR_PAGE)

    # Use both "j" key and down arrow keys to moving down and enter a value.
    # Once located on the bottom cell, use the down arrow key to prove the bottom cell is still selected.
    notebook_frontend.press("ArrowDown", page=EDITOR_PAGE)
    notebook_frontend.press("Enter", page=EDITOR_PAGE)
    notebook_frontend.press("3", page=EDITOR_PAGE)
    notebook_frontend.to_command_mode()
    notebook_frontend.press("j", page=EDITOR_PAGE)
    notebook_frontend.press("Enter", page=EDITOR_PAGE)
    notebook_frontend.press("4", page=EDITOR_PAGE)
    notebook_frontend.to_command_mode()
    notebook_frontend.press("j", page=EDITOR_PAGE)
    notebook_frontend.press("ArrowDown", page=EDITOR_PAGE)
    notebook_frontend.press("Enter", page=EDITOR_PAGE)
    notebook_frontend.press("5", page=EDITOR_PAGE)
    notebook_frontend.to_command_mode()
    assert notebook_frontend.get_cells_contents() == ["0 edit #1", "1", "2", "3", "4", "5"]

    # Use the "j" key on the top cell as well
    notebook_frontend.press("j", page=EDITOR_PAGE)
    notebook_frontend.press("Enter", page=EDITOR_PAGE)
    notebook_frontend.type(" edit #1", page=EDITOR_PAGE)
    notebook_frontend.to_command_mode()
    assert notebook_frontend.get_cells_contents() == ["0 edit #1", "1", "2", "3", "4", "5 edit #1"]

    # On the bottom cell, use both left and right arrow keys to prove the bottom cell is still selected.
    notebook_frontend.press("ArrowLeft", page=EDITOR_PAGE)
    notebook_frontend.press("Enter", page=EDITOR_PAGE)
    notebook_frontend.type(", #2", page=EDITOR_PAGE)
    notebook_frontend.to_command_mode()
    assert notebook_frontend.get_cells_contents() == ["0 edit #1", "1", "2", "3", "4", "5 edit #1, #2"]
    notebook_frontend.press("ArrowRight", page=EDITOR_PAGE)
    notebook_frontend.press("Enter", page=EDITOR_PAGE)
    notebook_frontend.type(" and #3", page=EDITOR_PAGE)
    notebook_frontend.to_command_mode()
    assert notebook_frontend.get_cells_contents() == ["0 edit #1", "1", "2", "3", "4", "5 edit #1, #2 and #3"]

    # Tests in edit mode.
    # First, erase the previous content and then setup the cells to test the keys to move up.
    [notebook_frontend.locate(".fa-cut.fa", page=EDITOR_PAGE).click() for i in range(6)]
    [notebook_frontend.press("b", page=EDITOR_PAGE) for i in range(2)]
    notebook_frontend.press("a", page=EDITOR_PAGE)
    notebook_frontend.press("Enter", page=EDITOR_PAGE)

    # Use the up arrow key to move down and enter a value.
    # We will use the left arrow key to move one char to the left since moving up on last character only moves selector to the first one.
    # Once located on the top cell, use the up arrow key to prove the top cell is still selected.
    notebook_frontend.press("ArrowUp", page=EDITOR_PAGE)
    notebook_frontend.press("1", page=EDITOR_PAGE)
    notebook_frontend.press("ArrowLeft", page=EDITOR_PAGE)
    [notebook_frontend.press("ArrowUp", page=EDITOR_PAGE) for i in range(2)]
    notebook_frontend.press("0", page=EDITOR_PAGE)

    # Use the down arrow key to move down and enter a value.
    # We will use the right arrow key to move one char to the right since moving down puts selector to the last character.
    # Once located on the bottom cell, use the down arrow key to prove the bottom cell is still selected.
    notebook_frontend.press("ArrowDown", page=EDITOR_PAGE)
    notebook_frontend.press("ArrowRight", page=EDITOR_PAGE)
    notebook_frontend.press("ArrowDown", page=EDITOR_PAGE)
    notebook_frontend.press("2", page=EDITOR_PAGE)
    [notebook_frontend.press("ArrowDown", page=EDITOR_PAGE) for i in range(2)]
    notebook_frontend.press("3", page=EDITOR_PAGE)
    notebook_frontend.to_command_mode()
    assert notebook_frontend.get_cells_contents() == ["0", "1", "2", "3"]
