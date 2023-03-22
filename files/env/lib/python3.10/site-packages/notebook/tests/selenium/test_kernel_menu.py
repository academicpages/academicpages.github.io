from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from notebook.tests.selenium.utils import wait_for_selector

restart_selectors = [
    '#restart_kernel', '#restart_clear_output', '#restart_run_all'
]
notify_interaction = '#notification_kernel > span'

shutdown_selector = '#shutdown_kernel'
confirm_selector = '.btn-danger'
cancel_selector = ".modal-footer button:first-of-type"


def test_cancel_restart_or_shutdown(notebook):
    """Click each of the restart options, then cancel the confirmation dialog"""
    browser = notebook.browser
    kernel_menu = browser.find_element(By.ID, 'kernellink')

    for menu_item in restart_selectors + [shutdown_selector]:
        kernel_menu.click()
        wait_for_selector(browser, menu_item, visible=True, single=True).click()
        wait_for_selector(browser, cancel_selector, visible=True, single=True).click()
        WebDriverWait(browser, 3).until(
            EC.invisibility_of_element((By.CSS_SELECTOR, '.modal-backdrop'))
        )
        assert notebook.is_kernel_running()


def test_menu_items(notebook):
    browser = notebook.browser
    kernel_menu = browser.find_element(By.ID, 'kernellink')

    for menu_item in restart_selectors:
        # Shutdown
        kernel_menu.click()
        wait_for_selector(browser, shutdown_selector, visible=True, single=True).click()

        # Confirm shutdown
        wait_for_selector(browser, confirm_selector, visible=True, single=True).click()

        WebDriverWait(browser, 3).until(
            lambda b: not notebook.is_kernel_running(),
            message="Kernel did not shut down as expected"
        )

        # Restart
        # Selenium can't click the menu while a modal dialog is fading out
        WebDriverWait(browser, 3).until(
            EC.invisibility_of_element((By.CSS_SELECTOR, '.modal-backdrop'))
        )
        kernel_menu.click()

        wait_for_selector(browser, menu_item, visible=True, single=True).click()
        WebDriverWait(browser, 10).until(
            lambda b: notebook.is_kernel_running(),
            message=f"Restart ({menu_item!r}) after shutdown did not start kernel"
        )
