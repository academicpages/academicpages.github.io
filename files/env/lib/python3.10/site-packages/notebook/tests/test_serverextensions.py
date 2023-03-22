import os
import site
import sys
from unittest import TestCase
from unittest.mock import patch

from ipython_genutils.tempdir import TemporaryDirectory
from ipython_genutils import py3compat

from notebook.config_manager import BaseJSONConfigManager
from traitlets.tests.utils import check_help_all_output
from jupyter_core import paths

from notebook.serverextensions import toggle_serverextension_python
from notebook import nbextensions, extensions
from notebook.notebookapp import NotebookApp
from notebook.nbextensions import _get_config_dir

from types import SimpleNamespace

from collections import OrderedDict


def test_help_output():
    check_help_all_output('notebook.serverextensions')
    check_help_all_output('notebook.serverextensions', ['enable'])
    check_help_all_output('notebook.serverextensions', ['disable'])
    check_help_all_output('notebook.serverextensions', ['install'])
    check_help_all_output('notebook.serverextensions', ['uninstall'])

outer_file = __file__

class MockExtensionModule:
    __file__ = outer_file

    @staticmethod
    def _jupyter_server_extension_paths():
        return [{
            'module': '_mockdestination/index'
        }]

    loaded = False

    def load_jupyter_server_extension(self, app):
        self.loaded = True


class MockEnvTestCase(TestCase):

    def tempdir(self):
        td = TemporaryDirectory()
        self.tempdirs.append(td)
        return py3compat.cast_unicode(td.name)

    def setUp(self):
        self.tempdirs = []
        self._mock_extensions = []

        self.test_dir = self.tempdir()
        self.data_dir = os.path.join(self.test_dir, 'data')
        self.config_dir = os.path.join(self.test_dir, 'config')
        self.system_data_dir = os.path.join(self.test_dir, 'system_data')
        self.system_config_dir = os.path.join(self.test_dir, 'system_config')
        self.system_path = [self.system_data_dir]
        self.system_config_path = [self.system_config_dir]

        self.patches = []
        p = patch.dict('os.environ', {
            'JUPYTER_CONFIG_DIR': self.config_dir,
            'JUPYTER_DATA_DIR': self.data_dir,
        })
        self.patches.append(p)
        for mod in (paths, nbextensions):
            p = patch.object(mod,
                'SYSTEM_JUPYTER_PATH', self.system_path)
            self.patches.append(p)
            p = patch.object(mod,
                'ENV_JUPYTER_PATH', [])
            self.patches.append(p)
        for mod in (paths, extensions):
            p = patch.object(mod,
                'SYSTEM_CONFIG_PATH', self.system_config_path)
            self.patches.append(p)
            p = patch.object(mod,
                'ENV_CONFIG_PATH', [])
            self.patches.append(p)
        # avoid adding the user site to the config paths with jupyter-core >= 4.9
        # https://github.com/jupyter/jupyter_core/pull/242
        p = patch.object(site,
            'ENABLE_USER_SITE', False)
        self.patches.append(p)
        for p in self.patches:
            p.start()
            self.addCleanup(p.stop)
        # verify our patches
        self.assertEqual(paths.jupyter_config_path(), [self.config_dir] + self.system_config_path)
        self.assertEqual(extensions._get_config_dir(user=False), self.system_config_dir)
        self.assertEqual(paths.jupyter_path(), [self.data_dir] + self.system_path)

    def tearDown(self):
        for modulename in self._mock_extensions:
            sys.modules.pop(modulename)

    def _inject_mock_extension(self, modulename='mockextension'):

        sys.modules[modulename] = ext = MockExtensionModule()
        self._mock_extensions.append(modulename)
        return ext

class TestInstallServerExtension(MockEnvTestCase):

    def _get_config(self, user=True):
        cm = BaseJSONConfigManager(config_dir=_get_config_dir(user))
        data = cm.get("jupyter_notebook_config")
        return data.get("NotebookApp", {}).get("nbserver_extensions", {})

    def test_enable(self):
        self._inject_mock_extension()
        toggle_serverextension_python('mockextension', True)

        config = self._get_config()
        assert config['mockextension']

    def test_disable(self):
        self._inject_mock_extension()
        toggle_serverextension_python('mockextension', True)
        toggle_serverextension_python('mockextension', False)

        config = self._get_config()
        assert not config['mockextension']

    def test_merge_config(self):
        # enabled at sys level
        mock_sys = self._inject_mock_extension('mockext_sys')
        # enabled at sys, disabled at user
        mock_both = self._inject_mock_extension('mockext_both')
        # enabled at user
        mock_user = self._inject_mock_extension('mockext_user')
        # enabled at Python
        mock_py = self._inject_mock_extension('mockext_py')

        toggle_serverextension_python('mockext_sys', enabled=True, user=False)
        toggle_serverextension_python('mockext_user', enabled=True, user=True)
        toggle_serverextension_python('mockext_both', enabled=True, user=False)
        toggle_serverextension_python('mockext_both', enabled=False, user=True)

        app = NotebookApp(nbserver_extensions={'mockext_py': True})
        app.init_server_extension_config()
        app.init_server_extensions()

        assert mock_user.loaded
        assert mock_sys.loaded
        assert mock_py.loaded
        assert not mock_both.loaded


class TestOrderedServerExtension(MockEnvTestCase):
    """
    Test that Server Extensions are loaded _in order_
    """

    def setUp(self):
        super().setUp()
        mockextension1 = SimpleNamespace()
        mockextension2 = SimpleNamespace()

        def load_jupyter_server_extension(obj):
            obj.mockI = True
            obj.mock_shared = 'I'

        mockextension1.load_jupyter_server_extension = load_jupyter_server_extension

        def load_jupyter_server_extension(obj):
            obj.mockII = True
            obj.mock_shared = 'II'

        mockextension2.load_jupyter_server_extension = load_jupyter_server_extension

        sys.modules['mockextension2'] = mockextension2
        sys.modules['mockextension1'] = mockextension1

    def tearDown(self):
        super().tearDown()
        del sys.modules['mockextension2']
        del sys.modules['mockextension1']


    def test_load_ordered(self):
        app = NotebookApp()
        app.nbserver_extensions = OrderedDict([('mockextension2',True),('mockextension1',True)])

        app.init_server_extensions()

        assert app.mockII is True, "Mock II should have been loaded"
        assert app.mockI is True, "Mock I should have been loaded"
        assert app.mock_shared == 'II', "Mock II should be loaded after Mock I"
