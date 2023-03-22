"""Test the bundlerextension CLI."""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

import os
import shutil
import unittest

from unittest.mock import patch
from ipython_genutils.tempdir import TemporaryDirectory
from ipython_genutils import py3compat

from traitlets.tests.utils import check_help_all_output

import notebook.nbextensions as nbextensions
from notebook.config_manager import BaseJSONConfigManager
from ..bundlerextensions import (_get_config_dir, enable_bundler_python, 
    disable_bundler_python)

def test_help_output():
    check_help_all_output('notebook.bundler.bundlerextensions')
    check_help_all_output('notebook.bundler.bundlerextensions', ['enable'])
    check_help_all_output('notebook.bundler.bundlerextensions', ['disable'])

class TestBundlerExtensionCLI(unittest.TestCase):
    """Tests the bundlerextension CLI against the example zip_bundler."""
    def setUp(self):
        """Build an isolated config environment."""
        td = TemporaryDirectory()
        
        self.test_dir = py3compat.cast_unicode(td.name)
        self.data_dir = os.path.join(self.test_dir, 'data')
        self.config_dir = os.path.join(self.test_dir, 'config')
        self.system_data_dir = os.path.join(self.test_dir, 'system_data')
        self.system_path = [self.system_data_dir]
        
        # Use temp directory, not real user or system config paths
        self.patch_env = patch.dict('os.environ', {
            'JUPYTER_CONFIG_DIR': self.config_dir,
            'JUPYTER_DATA_DIR': self.data_dir,
        })
        self.patch_env.start()
        self.patch_system_path = patch.object(nbextensions,
            'SYSTEM_JUPYTER_PATH', self.system_path)
        self.patch_system_path.start()
         
    def tearDown(self):
        """Remove the test config environment."""
        shutil.rmtree(self.test_dir, ignore_errors=True)
        self.patch_env.stop()
        self.patch_system_path.stop()
                
    def test_enable(self):
        """Should add the bundler to the notebook configuration."""
        enable_bundler_python('notebook.bundler.zip_bundler')
        
        config_dir = os.path.join(_get_config_dir(user=True), 'nbconfig')
        cm = BaseJSONConfigManager(config_dir=config_dir)
        bundlers = cm.get('notebook').get('bundlerextensions', {})
        self.assertEqual(len(bundlers), 1)
        self.assertIn('notebook_zip_download', bundlers)
    
    def test_disable(self):
        """Should remove the bundler from the notebook configuration."""
        self.test_enable()
        disable_bundler_python('notebook.bundler.zip_bundler')
        
        config_dir = os.path.join(_get_config_dir(user=True), 'nbconfig')
        cm = BaseJSONConfigManager(config_dir=config_dir)
        bundlers = cm.get('notebook').get('bundlerextensions', {})
        self.assertEqual(len(bundlers), 0)
