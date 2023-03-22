"""Test kernel interrupt"""


from .utils import EDITOR_PAGE


def interrupt_from_menu(notebook_frontend):
    # Click interrupt button in kernel menu
    notebook_frontend.try_click_selector('#kernellink', page=EDITOR_PAGE)
    notebook_frontend.try_click_selector('#int_kernel', page=EDITOR_PAGE)
    notebook_frontend.press('Escape', page=EDITOR_PAGE)


def interrupt_from_keyboard(notebook_frontend):
    notebook_frontend.type("ii", page=EDITOR_PAGE)
    notebook_frontend.press('Escape', page=EDITOR_PAGE)


def test_interrupt(notebook_frontend):
    """ Test the interrupt function using both the button in the Kernel menu and the keyboard shortcut "ii"
    """

    text = ('import time\n'
            'for x in range(3):\n'
            '   time.sleep(1)')

    notebook_frontend.edit_cell(index=0, content=text)

    for interrupt_method in (interrupt_from_menu, interrupt_from_keyboard):
        notebook_frontend.clear_cell_output(0)
        notebook_frontend.to_command_mode()
        notebook_frontend.execute_cell(0)

        interrupt_method(notebook_frontend)

        # Wait for an output to appear
        output = notebook_frontend.wait_for_cell_output(0)
        assert 'KeyboardInterrupt' in output.get_inner_text()
