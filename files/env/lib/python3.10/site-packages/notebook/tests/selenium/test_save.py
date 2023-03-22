"""Test saving a notebook with escaped characters
"""

from urllib.parse import quote
from selenium.webdriver.common.by import By

from .utils import wait_for_selector


promise_js = """
var done = arguments[arguments.length - 1];
%s.then(
    data => { done(["success", data]); },
    error => { done(["error", error]); }
);
"""


def execute_promise(js, browser):
    state, data = browser.execute_async_script(promise_js % js)
    if state == 'success':
        return data
    raise Exception(data)


def test_save(notebook):
    # don't use unicode with ambiguous composed/decomposed normalization
    # because the filesystem may use a different normalization than literals.
    # This causes no actual problems, but will break string comparison.
    nbname = "has#hash and space and unicø∂e.ipynb"
    escaped_name = quote(nbname)

    notebook.edit_cell(index=0, content="s = '??'")

    notebook.browser.execute_script("Jupyter.notebook.set_notebook_name(arguments[0])", nbname)

    model = execute_promise("Jupyter.notebook.save_notebook()", notebook.browser)
    assert model['name'] == nbname

    current_name = notebook.browser.execute_script("return Jupyter.notebook.notebook_name")
    assert current_name == nbname

    current_path = notebook.browser.execute_script("return Jupyter.notebook.notebook_path")
    assert current_path == nbname

    displayed_name = notebook.browser.find_element(By.ID, 'notebook_name').text
    assert displayed_name + '.ipynb' == nbname

    execute_promise("Jupyter.notebook.save_checkpoint()", notebook.browser)

    checkpoints = notebook.browser.execute_script("return Jupyter.notebook.checkpoints")
    assert len(checkpoints) == 1

    notebook.browser.find_element(By.CSS_SELECTOR, '#ipython_notebook a').click()
    hrefs_nonmatch = []
    for link in wait_for_selector(notebook.browser, 'a.item_link'):
        href = link.get_attribute('href')
        if escaped_name in href:
            print("Opening", href)
            notebook.browser.get(href)
            wait_for_selector(notebook.browser, '.cell')
            break
        hrefs_nonmatch.append(href)
    else:
        raise AssertionError(f"{escaped_name!r} not found in {hrefs_nonmatch!r}")

    current_name = notebook.browser.execute_script("return Jupyter.notebook.notebook_name")
    assert current_name == nbname
