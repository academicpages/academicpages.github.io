from notebook.tests.selenium.utils import wait_for_selector
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


def wait_for_rename(browser, nbname, timeout=10):
    wait = WebDriverWait(browser, timeout)
    def notebook_renamed(browser):
        elem = browser.find_element(By.ID, 'notebook_name')
        current_name = browser.execute_script('return arguments[0].innerText', elem)
        return current_name == nbname
    return wait.until(notebook_renamed)

def save_as(nb):
    JS = 'Jupyter.notebook.save_notebook_as()'
    return nb.browser.execute_script(JS)

def get_notebook_name(nb):
    JS = 'return Jupyter.notebook.notebook_name'
    return nb.browser.execute_script(JS)

def set_notebook_name(nb, name):
    JS = f'Jupyter.notebook.rename("{name}")'
    nb.browser.execute_script(JS)

def test_save_notebook_as(notebook):
    # Set a name for comparison later
    set_notebook_name(notebook, name="nb1.ipynb")
    wait_for_rename(notebook.browser, "nb1")
    assert get_notebook_name(notebook) == "nb1.ipynb"
    # Wait for Save As modal, save
    save_as(notebook)
    wait_for_selector(notebook.browser, '.save-message')
    inp = notebook.browser.find_element(By.XPATH, '//input[@data-testid="save-as"]')
    inp.send_keys('new_notebook.ipynb')
    inp.send_keys(Keys.RETURN)
    wait_for_rename(notebook.browser, "new_notebook")
    # Test that the name changed
    assert get_notebook_name(notebook) == "new_notebook.ipynb"
    # Test that address bar was updated (TODO: get the base url)
    assert "new_notebook.ipynb" in notebook.browser.current_url