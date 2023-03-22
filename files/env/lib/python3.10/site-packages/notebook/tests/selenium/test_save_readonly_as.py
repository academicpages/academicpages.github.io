from notebook.tests.selenium.utils import wait_for_selector
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


promise_js = """
var done = arguments[arguments.length - 1];
(%s).then(
    data => { done(["success", data]); },
    error => { done(["error", error]); }
);
"""

def execute_promise(js, browser):
    state, data = browser.execute_async_script(promise_js % js)
    if state == 'success':
        return data
    raise Exception(data)

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

def refresh_notebook(nb):
    nb.browser.refresh()
    nb.__init__(nb.browser)


# TODO(PR6474): Revisit and re-enable this test
# def test_save_readonly_notebook_as(notebook):
#     # Make notebook read-only
#     notebook.edit_cell(index=0, content='import os\nimport stat\nos.chmod("'
#         + notebook.browser.current_url.split('?')[0].split('/')[-1] + '", stat.S_IREAD)\nprint(0)')
#     notebook.browser.execute_script("Jupyter.notebook.get_cell(0).execute();")
#     notebook.wait_for_cell_output(0)
#     refresh_notebook(notebook)
#     # Test that the notebook is read-only
#     assert notebook.browser.execute_script('return Jupyter.notebook.writable') == False
#
#     # Add some content
#     test_content_0 = "print('a simple')\nprint('test script')"
#     notebook.edit_cell(index=0, content=test_content_0)
#
#     # Wait for Save As modal, save
#     save_as(notebook)
#     wait_for_selector(notebook.browser, '.save-message')
#     inp = notebook.browser.find_element_by_xpath('//input[@data-testid="save-as"]')
#     inp.send_keys('writable_notebook.ipynb')
#     inp.send_keys(Keys.RETURN)
#     wait_for_rename(notebook.browser, "writable_notebook")
#     # Test that the name changed
#     assert get_notebook_name(notebook) == "writable_notebook.ipynb"
#     # Test that address bar was updated (TODO: get the base url)
#     assert "writable_notebook.ipynb" in notebook.browser.current_url
#     # Test that it is no longer read-only
#     assert notebook.browser.execute_script('return Jupyter.notebook.writable') == True
#
#     # Add some more content
#     test_content_1 = "print('a second simple')\nprint('script to test save feature')"
#     notebook.add_and_execute_cell(content=test_content_1)
#     # and save the notebook
#     execute_promise("Jupyter.notebook.save_notebook()", notebook.browser)
#
#     # Test that it still contains the content
#     assert notebook.get_cell_contents(index=0) == test_content_0
#     assert notebook.get_cell_contents(index=1) == test_content_1
#     # even after a refresh
#     refresh_notebook(notebook)
#     assert notebook.get_cell_contents(index=0) == test_content_0
#     assert notebook.get_cell_contents(index=1) == test_content_1
