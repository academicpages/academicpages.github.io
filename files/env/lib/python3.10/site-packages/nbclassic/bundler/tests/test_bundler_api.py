"""Test the bundlers API."""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

import io
from os.path import join as pjoin

from nbclassic.tests.launchnotebook import NotebookTestBase
from nbformat import write
from nbformat.v4 import (
    new_notebook, new_markdown_cell, new_code_cell, new_output,
)

from unittest.mock import patch

    
def bundle(handler, model):
    """Bundler test stub. Echo the notebook path."""
    handler.finish(model['path'])

class BundleAPITest(NotebookTestBase):
    """Test the bundlers web service API"""
    @classmethod
    def setup_class(cls):
        """Make a test nbclassic. Borrowed from nbconvert test. Assumes the class
        teardown will clean it up in the end."""
        super(BundleAPITest, cls).setup_class()
        nbdir = cls.notebook_dir

        nb = new_notebook()

        nb.cells.append(new_markdown_cell(u'Created by test'))
        cc1 = new_code_cell(source=u'print(2*6)')
        cc1.outputs.append(new_output(output_type="stream", text=u'12'))
        nb.cells.append(cc1)
        
        with io.open(pjoin(nbdir, 'testnb.ipynb'), 'w',
                     encoding='utf-8') as f:
            write(nb, f, version=4)

    def test_missing_bundler_arg(self):
        """Should respond with 400 error about missing bundler arg"""
        resp = self.request('GET', 'bundle/fake.ipynb')
        self.assertEqual(resp.status_code, 400)
        self.assertIn('Missing argument bundler', resp.text)

    def test_notebook_not_found(self):
        """Should respond with 404 error about missing notebook"""
        resp = self.request('GET', 'bundle/fake.ipynb',
            params={'bundler': 'fake_bundler'})
        self.assertEqual(resp.status_code, 404)
        self.assertIn('Not Found', resp.text)

    def test_bundler_not_enabled(self):
        """Should respond with 400 error about disabled bundler"""
        resp = self.request('GET', 'bundle/testnb.ipynb',
            params={'bundler': 'fake_bundler'})
        self.assertEqual(resp.status_code, 400)
        self.assertIn('Bundler fake_bundler not enabled', resp.text)

    def test_bundler_import_error(self):
        """Should respond with 500 error about failure to load bundler module"""
        with patch('nbclassic.bundler.handlers.BundlerHandler.get_bundler') as mock:
            mock.return_value = {'module_name': 'fake_module'}
            resp = self.request('GET', 'bundle/testnb.ipynb',
                params={'bundler': 'fake_bundler'})
            mock.assert_called_with('fake_bundler')
        self.assertEqual(resp.status_code, 500)
        self.assertIn('Could not import bundler fake_bundler', resp.text)
        
    def test_bundler_invoke(self):
        """Should respond with 200 and output from test bundler stub"""
        with patch('nbclassic.bundler.handlers.BundlerHandler.get_bundler') as mock:
            mock.return_value = {'module_name': 'nbclassic.bundler.tests.test_bundler_api'}
            resp = self.request('GET', 'bundle/testnb.ipynb',
                params={'bundler': 'stub_bundler'})
            mock.assert_called_with('stub_bundler')
        self.assertEqual(resp.status_code, 200)
        self.assertIn('testnb.ipynb', resp.text)