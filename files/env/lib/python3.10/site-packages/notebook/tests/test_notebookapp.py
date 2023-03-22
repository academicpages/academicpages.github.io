"""Test NotebookApp"""

import getpass
import logging
import os
import re
import sys
from tempfile import NamedTemporaryFile

from unittest.mock import patch

import pytest

from traitlets.tests.utils import check_help_all_output

from jupyter_core.application import NoStart
from ipython_genutils.tempdir import TemporaryDirectory
from traitlets import TraitError
from notebook import notebookapp, __version__
from notebook.auth.security import passwd_check
NotebookApp = notebookapp.NotebookApp

from .launchnotebook import NotebookTestBase, UNIXSocketNotebookTestBase


def test_help_output():
    """ipython notebook --help-all works"""
    check_help_all_output('notebook')

def test_server_info_file():
    td = TemporaryDirectory()
    nbapp = NotebookApp(runtime_dir=td.name, log=logging.getLogger())
    def get_servers():
        return list(notebookapp.list_running_servers(nbapp.runtime_dir))
    nbapp.initialize(argv=[])
    nbapp.write_server_info_file()
    servers = get_servers()
    assert len(servers) == 1
    assert servers[0]['port'] == nbapp.port
    assert servers[0]['url'] == nbapp.connection_url
    nbapp.remove_server_info_file()
    assert get_servers() == []

    # The ENOENT error should be silenced.
    nbapp.remove_server_info_file()

def test_nb_dir():
    with TemporaryDirectory() as td:
        app = NotebookApp(notebook_dir=td)
        assert app.notebook_dir == td

def test_no_create_nb_dir():
    with TemporaryDirectory() as td:
        nbdir = os.path.join(td, 'notebooks')
        app = NotebookApp()
        with pytest.raises(TraitError):
            app.notebook_dir = nbdir

def test_missing_nb_dir():
    with TemporaryDirectory() as td:
        nbdir = os.path.join(td, 'notebook', 'dir', 'is', 'missing')
        app = NotebookApp()
        with pytest.raises(TraitError):
            app.notebook_dir = nbdir

def test_invalid_nb_dir():
    with NamedTemporaryFile() as tf:
        app = NotebookApp()
        with pytest.raises(TraitError):
            app.notebook_dir = tf

def test_nb_dir_with_slash():
    with TemporaryDirectory(suffix="_slash" + os.sep) as td:
        app = NotebookApp(notebook_dir=td)
        assert not app.notebook_dir.endswith(os.sep)

def test_nb_dir_root():
    root = os.path.abspath(os.sep) # gets the right value on Windows, Posix
    app = NotebookApp(notebook_dir=root)
    assert app.notebook_dir == root

def test_generate_config():
    with TemporaryDirectory() as td:
        app = NotebookApp(config_dir=td)
        app.initialize(['--generate-config', '--allow-root'])
        with pytest.raises(NoStart):
            app.start()
        assert os.path.exists(os.path.join(td, 'jupyter_notebook_config.py'))

#test if the version testin function works
@pytest.mark.parametrize(
    'version', [
        '4.1.0.b1',
        '4.1.b1',
        '4.2',
        'X.y.z',
        '1.2.3.dev1.post2',
    ]
)
def test_pep440_bad_version(version):
    with pytest.raises(ValueError):
        raise_on_bad_version(version)

@pytest.mark.parametrize(
    'version', [
        '4.1.1',
        '4.2.1b3',
    ]
)
def test_pep440_good_version(version):
    raise_on_bad_version(version)

pep440re = re.compile(r'^(\d+)\.(\d+)\.(\d+((a|b|rc)\d+)?)(\.post\d+)?(\.dev\d*)?$')

def raise_on_bad_version(version):
    if not pep440re.match(version):
        raise ValueError("Versions String does apparently not match Pep 440 specification, "
                         "which might lead to sdist and wheel being seen as 2 different release. "
                         "E.g: do not use dots for beta/alpha/rc markers.")

def test_current_version():
    raise_on_bad_version(__version__)

def test_notebook_password():
    password = 'secret'
    with TemporaryDirectory() as td:
        with patch.dict('os.environ', {
            'JUPYTER_CONFIG_DIR': td,
        }), patch.object(getpass, 'getpass', return_value=password):
            app = notebookapp.NotebookPasswordApp(log_level=logging.ERROR)
            app.initialize([])
            app.start()
            nb = NotebookApp()
            nb.load_config_file()
            assert nb.password != ''
            passwd_check(nb.password, password)

class StopAppTest(notebookapp.NbserverStopApp):
    """For testing the logic of NbserverStopApp."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.servers_shut_down = []

    def shutdown_server(self, server):
        self.servers_shut_down.append(server)
        return True

def test_notebook_stop():
    def list_running_servers(runtime_dir):
        for port in range(100, 110):
            yield {
                'pid': 1000 + port,
                'port': port,
                'base_url': '/',
                'hostname': 'localhost',
                'notebook_dir': '/',
                'secure': False,
                'token': '',
                'password': False,
                'url': f'http://localhost:{port}',
            }

    mock_servers = patch('notebook.notebookapp.list_running_servers', list_running_servers)

    # test stop with a match
    with mock_servers:
        app = StopAppTest()
        app.initialize(['105'])
        app.start()
    assert len(app.servers_shut_down) == 1
    assert app.servers_shut_down[0]['port'] == 105

    # test no match
    with mock_servers, patch('os.kill') as os_kill:
        app = StopAppTest()
        app.initialize(['999'])
        with pytest.raises(SystemExit) as exc:
            app.start()
        assert exc.value.code == 1
    assert len(app.servers_shut_down) == 0


class NotebookAppTests(NotebookTestBase):
    def test_list_running_servers(self):
        servers = list(notebookapp.list_running_servers())
        assert len(servers) >= 1
        assert self.port in {info['port'] for info in servers}

    def test_log_json_default(self):
        self.assertFalse(self.notebook.log_json)

    def test_validate_log_json(self):
        self.assertFalse(self.notebook._validate_log_json(dict(value=False)))


# UNIX sockets aren't available on Windows.
if not sys.platform.startswith('win'):
    class NotebookUnixSocketTests(UNIXSocketNotebookTestBase):
        def test_run(self):
            self.fetch_url(self.base_url() + 'api/contents')

        def test_list_running_sock_servers(self):
            servers = list(notebookapp.list_running_servers())
            assert len(servers) >= 1
            assert self.sock in {info['sock'] for info in servers}


class NotebookAppJSONLoggingTests(NotebookTestBase):
    """Tests for when json logging is enabled."""
    @classmethod
    def setup_class(cls):
        super().setup_class()
        try:
            import json_logging
            cls.json_logging_available = True
        except ImportError:
            cls.json_logging_available = False

    @classmethod
    def get_patch_env(cls):
        test_env = super().get_patch_env()
        test_env.update({'JUPYTER_ENABLE_JSON_LOGGING': 'true'})
        return test_env

    def test_log_json_enabled(self):
        self.assertTrue(self.notebook._default_log_json())

    def test_validate_log_json(self):
        self.assertEqual(
            self.notebook._validate_log_json(dict(value=True)),
            self.json_logging_available)
