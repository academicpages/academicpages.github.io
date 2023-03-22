"""Test kernel menu"""


from .utils import EDITOR_PAGE


restart_selectors = [
    '#restart_kernel', '#restart_clear_output', '#restart_run_all'
]
notify_interaction = '#notification_kernel > span'
shutdown_selector = '#shutdown_kernel'
confirm_selector = '.btn-danger'
cancel_selector = ".modal-footer button:first-of-type"


def test_cancel_restart_or_shutdown(notebook_frontend):
    """Click each of the restart options, then cancel the confirmation dialog"""
    kernel_menu = notebook_frontend.locate('#kernellink', EDITOR_PAGE)
    if not kernel_menu:
        raise Exception('Could not find kernel_menu')

    for menu_item in restart_selectors + [shutdown_selector]:
        kernel_menu.click()
        notebook_frontend.wait_for_selector(menu_item, EDITOR_PAGE).click()
        notebook_frontend.wait_for_selector(cancel_selector, EDITOR_PAGE).click()

        modal = notebook_frontend.wait_for_selector('.modal-backdrop', EDITOR_PAGE)
        modal.wait_for('hidden')

        assert notebook_frontend.is_kernel_running()


def test_menu_items(notebook_frontend):
    kernel_menu = notebook_frontend.locate('#kernellink', EDITOR_PAGE)

    for menu_item in restart_selectors:
        # Shutdown
        kernel_menu.click()
        notebook_frontend.wait_for_selector(shutdown_selector, EDITOR_PAGE).click()

        # Confirm shutdown
        notebook_frontend.wait_for_selector(confirm_selector, EDITOR_PAGE).click()

        notebook_frontend.wait_for_condition(lambda: not notebook_frontend.is_kernel_running())

        # Restart
        # (can't click the menu while a modal dialog is fading out)
        modal = notebook_frontend.locate('.modal-backdrop', EDITOR_PAGE).expect_not_to_be_visible()
        kernel_menu.click()

        notebook_frontend.wait_for_selector(menu_item, EDITOR_PAGE).click()
        notebook_frontend.wait_for_condition(
            lambda: notebook_frontend.is_kernel_running(),
            timeout=120,
            period=5
        )
