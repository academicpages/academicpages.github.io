"""Utilities for driving Selenium interactively to develop tests.

These are not used in the tests themselves - rather, the developer writing tests
can use them to experiment with Selenium.
"""
from selenium.webdriver import Firefox

from notebook.tests.selenium.utils import Notebook
from notebook.notebookapp import list_running_servers

class NoServerError(Exception):

    def __init__(self, message):
        self.message = message

def quick_driver(lab=False):
    """Quickly create a selenium driver pointing at an active noteboook server.

    Usage example:
    
        from notebook.tests.selenium.quick_selenium import quick_driver
        driver = quick_driver
        
    Note: you need to manually close the driver that opens with driver.quit()
    """
    try:
        server = list(list_running_servers())[0]
    except IndexError as e:
        raise NoServerError('You need a server running before you can run '
                            'this command') from e
    driver = Firefox()
    auth_url = '{url}?token={token}'.format(**server)
    driver.get(auth_url)

    # If this redirects us to a lab page and we don't want that;
    # then we need to redirect ourselves to the classic notebook view
    if driver.current_url.endswith('/lab') and not lab:
        driver.get(driver.current_url.rstrip('lab')+'tree')
    return driver


def quick_notebook():
    """Quickly create a new classic notebook in a selenium driver


    Usage example:
    
        from notebook.tests.selenium.quick_selenium import quick_notebook
        nb = quick_notebook()

    Note: you need to manually close the driver that opens with nb.browser.quit()
    """
    return Notebook.new_notebook(quick_driver())
