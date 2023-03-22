from selenium.webdriver.common.by import By

from .utils import wait_for_selector


def interrupt_from_menu(notebook):
    # Click interrupt button in kernel menu
    notebook.browser.find_element(By.ID, 'kernellink').click()
    wait_for_selector(notebook.browser, '#int_kernel', single=True).click()

def interrupt_from_keyboard(notebook):
    notebook.body.send_keys("ii")


def test_interrupt(notebook):
    """ Test the interrupt function using both the button in the Kernel menu and the keyboard shortcut "ii"

        Having trouble accessing the Interrupt message when execution is halted. I am assuming that the
        message does not lie in the "outputs" field of the cell's JSON object. Using a timeout work-around for
        test with an infinite loop. We know the interrupt function is working if this test passes.
        Hope this is a good start.
    """

    text = ('import time\n'
            'for x in range(3):\n'
            '   time.sleep(1)')

    notebook.edit_cell(index=0, content=text)

    for interrupt_method in (interrupt_from_menu, interrupt_from_keyboard):
        notebook.clear_cell_output(0)
        notebook.to_command_mode()
        notebook.execute_cell(0)

        interrupt_method(notebook)

        # Wait for an output to appear
        output = wait_for_selector(notebook.browser, '.output_subarea', single=True)
        assert 'KeyboardInterrupt' in output.text
