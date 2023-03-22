import json
import nbformat
from nbformat.v4 import new_notebook, new_code_cell
import os
import pytest
import requests
from subprocess import Popen
import sys
from tempfile import mkstemp
from testpath.tempdir import TemporaryDirectory
import time
from urllib.parse import urljoin

from selenium.webdriver import Firefox, Remote, Chrome
from .utils import Notebook

pjoin = os.path.join


def _wait_for_server(proc, info_file_path):
    """Wait 30 seconds for the notebook server to start"""
    for i in range(300):
        if proc.poll() is not None:
            raise RuntimeError("Notebook server failed to start")
        if os.path.exists(info_file_path):
            try:
                with open(info_file_path) as f:
                    return json.load(f)
            except ValueError:
                # If the server is halfway through writing the file, we may
                # get invalid JSON; it should be ready next iteration.
                pass
        time.sleep(0.1)
    raise RuntimeError("Didn't find %s in 30 seconds", info_file_path)


@pytest.fixture(scope='session')
def notebook_server():
    info = {}
    with TemporaryDirectory() as td:
        nbdir = info['nbdir'] = pjoin(td, 'notebooks')
        os.makedirs(pjoin(nbdir, 'sub ∂ir1', 'sub ∂ir 1a'))
        os.makedirs(pjoin(nbdir, 'sub ∂ir2', 'sub ∂ir 1b'))

        info['extra_env'] = {
            'JUPYTER_CONFIG_DIR': pjoin(td, 'jupyter_config'),
            'JUPYTER_RUNTIME_DIR': pjoin(td, 'jupyter_runtime'),
            'IPYTHONDIR': pjoin(td, 'ipython'),
        }
        env = os.environ.copy()
        env.update(info['extra_env'])

        command = [sys.executable, '-m', 'notebook',
                   '--no-browser',
                   '--notebook-dir', nbdir,
                   # run with a base URL that would be escaped,
                   # to test that we don't double-escape URLs
                   '--NotebookApp.base_url=/a@b/',
                   ]
        print("command=", command)
        proc = info['popen'] = Popen(command, cwd=nbdir, env=env)
        info_file_path = pjoin(td, 'jupyter_runtime',
                               f'nbserver-{proc.pid:d}.json')
        info.update(_wait_for_server(proc, info_file_path))

        print("Notebook server info:", info)
        yield info

    # Shut the server down
    requests.post(urljoin(info['url'], 'api/shutdown'),
                  headers={'Authorization': 'token '+info['token']})


def make_sauce_driver():
    """This function helps travis create a driver on Sauce Labs.

    This function will err if used without specifying the variables expected
    in that context.
    """

    username = os.environ["SAUCE_USERNAME"]
    access_key = os.environ["SAUCE_ACCESS_KEY"]
    capabilities = {
        "tunnel-identifier": os.environ["TRAVIS_JOB_NUMBER"],
        "build": os.environ["TRAVIS_BUILD_NUMBER"],
        "tags": [os.environ['TRAVIS_PYTHON_VERSION'], 'CI'],
        "platform": "Windows 10",
        "browserName": os.environ['JUPYTER_TEST_BROWSER'],
        "version": "latest",
    }
    if capabilities['browserName'] == 'firefox':
        # Attempt to work around issue where browser loses authentication
        capabilities['version'] = '57.0'
    hub_url = f"{username}:{access_key}@localhost:4445"
    print("Connecting remote driver on Sauce Labs")
    driver = Remote(desired_capabilities=capabilities,
                    command_executor=f"http://{hub_url}/wd/hub")
    return driver


@pytest.fixture(scope='session')
def selenium_driver():
    if os.environ.get('SAUCE_USERNAME'):
        driver = make_sauce_driver()
    elif os.environ.get('JUPYTER_TEST_BROWSER') == 'chrome':
        driver = Chrome()
    else:
        driver = Firefox()

    yield driver

    # Teardown
    driver.quit()


@pytest.fixture(scope='module')
def authenticated_browser(selenium_driver, notebook_server):
    selenium_driver.jupyter_server_info = notebook_server
    selenium_driver.get("{url}?token={token}".format(**notebook_server))
    return selenium_driver

@pytest.fixture
def notebook(authenticated_browser):
    tree_wh = authenticated_browser.current_window_handle
    yield Notebook.new_notebook(authenticated_browser)
    authenticated_browser.switch_to.window(tree_wh)

@pytest.fixture
def prefill_notebook(selenium_driver, notebook_server):
    def inner(cells):
        cells = [new_code_cell(c) if isinstance(c, str) else c
                 for c in cells]
        nb = new_notebook(cells=cells)
        fd, path = mkstemp(dir=notebook_server['nbdir'], suffix='.ipynb')
        with open(fd, 'w', encoding='utf-8') as f:
            nbformat.write(nb, f)
        fname = os.path.basename(path)
        selenium_driver.get(
            "{url}notebooks/{}?token={token}".format(fname, **notebook_server)
        )
        return Notebook(selenium_driver)

    return inner
