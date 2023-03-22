"""Tests arrow keys on both command and edit mode"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_dualmode_arrows(notebook):

    # Tests in command mode.
    # Setting up the cells to test the keys to move up.
    notebook.to_command_mode()
    [notebook.body.send_keys("b") for i in range(3)]

    # Use both "k" and up arrow keys to moving up and enter a value.
    # Once located on the top cell, use the up arrow keys to prove the top cell is still selected.
    notebook.body.send_keys("k")
    notebook.body.send_keys(Keys.ENTER)
    notebook.body.send_keys("2")
    notebook.to_command_mode()
    notebook.body.send_keys(Keys.UP)
    notebook.body.send_keys(Keys.ENTER)
    notebook.body.send_keys("1")
    notebook.to_command_mode()
    notebook.body.send_keys("k")
    notebook.body.send_keys(Keys.UP)
    notebook.body.send_keys(Keys.ENTER)
    notebook.body.send_keys("0")
    notebook.to_command_mode()
    assert notebook.get_cells_contents() == ["0", "1", "2", ""]

    # Use the "k" key on the top cell as well
    notebook.body.send_keys("k")
    notebook.body.send_keys(Keys.ENTER)
    notebook.body.send_keys(" edit #1")
    notebook.to_command_mode()
    assert notebook.get_cells_contents() == ["0 edit #1", "1", "2", ""]

    # Setting up the cells to test the keys to move down
    [notebook.body.send_keys("j") for i in range(3)]
    [notebook.body.send_keys("a") for i in range(2)]
    notebook.body.send_keys("k")

    # Use both "j" key and down arrow keys to moving down and enter a value.
    # Once located on the bottom cell, use the down arrow key to prove the bottom cell is still selected.
    notebook.body.send_keys(Keys.DOWN)
    notebook.body.send_keys(Keys.ENTER)
    notebook.body.send_keys("3")
    notebook.to_command_mode()
    notebook.body.send_keys("j")
    notebook.body.send_keys(Keys.ENTER)
    notebook.body.send_keys("4")
    notebook.to_command_mode()
    notebook.body.send_keys("j")
    notebook.body.send_keys(Keys.DOWN)
    notebook.body.send_keys(Keys.ENTER)
    notebook.body.send_keys("5")
    notebook.to_command_mode()
    assert notebook.get_cells_contents() == ["0 edit #1", "1", "2", "3", "4", "5"]

    # Use the "j" key on the top cell as well
    notebook.body.send_keys("j")
    notebook.body.send_keys(Keys.ENTER)
    notebook.body.send_keys(" edit #1")
    notebook.to_command_mode()
    assert notebook.get_cells_contents() == ["0 edit #1", "1", "2", "3", "4", "5 edit #1"]

    # On the bottom cell, use both left and right arrow keys to prove the bottom cell is still selected.
    notebook.body.send_keys(Keys.LEFT)
    notebook.body.send_keys(Keys.ENTER)
    notebook.body.send_keys(", #2")
    notebook.to_command_mode()
    assert notebook.get_cells_contents() == ["0 edit #1", "1", "2", "3", "4", "5 edit #1, #2"]
    notebook.body.send_keys(Keys.RIGHT)
    notebook.body.send_keys(Keys.ENTER)
    notebook.body.send_keys(" and #3")
    notebook.to_command_mode()
    assert notebook.get_cells_contents() == ["0 edit #1", "1", "2", "3", "4", "5 edit #1, #2 and #3"]


    # Tests in edit mode.
    # First, erase the previous content and then setup the cells to test the keys to move up.
    [notebook.browser.find_element(By.CLASS_NAME, "fa-cut.fa").click() for i in range(6)]
    [notebook.body.send_keys("b") for i in range(2)]
    notebook.body.send_keys("a")
    notebook.body.send_keys(Keys.ENTER)

    # Use the up arrow key to move down and enter a value.
    # We will use the left arrow key to move one char to the left since moving up on last character only moves selector to the first one.
    # Once located on the top cell, use the up arrow key to prove the top cell is still selected.
    notebook.body.send_keys(Keys.UP)
    notebook.body.send_keys("1")
    notebook.body.send_keys(Keys.LEFT)
    [notebook.body.send_keys(Keys.UP) for i in range(2)]
    notebook.body.send_keys("0")

    # Use the down arrow key to move down and enter a value.
    # We will use the right arrow key to move one char to the right since moving down puts selector to the last character.
    # Once located on the bottom cell, use the down arrow key to prove the bottom cell is still selected. 
    notebook.body.send_keys(Keys.DOWN)
    notebook.body.send_keys(Keys.RIGHT)
    notebook.body.send_keys(Keys.DOWN)
    notebook.body.send_keys("2")
    [notebook.body.send_keys(Keys.DOWN) for i in range(2)]
    notebook.body.send_keys("3")
    notebook.to_command_mode()
    assert notebook.get_cells_contents() == ["0", "1", "2", "3"]