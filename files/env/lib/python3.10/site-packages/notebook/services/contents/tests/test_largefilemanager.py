from unittest import TestCase
from ipython_genutils.tempdir import TemporaryDirectory
from ..largefilemanager import LargeFileManager
import os
from tornado import web


def _make_dir(contents_manager, api_path):
    """
    Make a directory.
    """
    os_path = contents_manager._get_os_path(api_path)
    try:
        os.makedirs(os_path)
    except OSError:
        print(f"Directory already exists: {os_path!r}")


class TestLargeFileManager(TestCase):

    def setUp(self):
        self._temp_dir = TemporaryDirectory()
        self.td = self._temp_dir.name
        self.contents_manager = LargeFileManager(root_dir=self.td)

    def make_dir(self, api_path):
        """make a subdirectory at api_path

        override in subclasses if contents are not on the filesystem.
        """
        _make_dir(self.contents_manager, api_path)

    def test_save(self):

        cm = self.contents_manager
        # Create a notebook
        model = cm.new_untitled(type='notebook')
        name = model['name']
        path = model['path']

        # Get the model with 'content'
        full_model = cm.get(path)
        # Save the notebook
        model = cm.save(full_model, path)
        assert isinstance(model, dict)
        self.assertIn('name', model)
        self.assertIn('path', model)
        self.assertEqual(model['name'], name)
        self.assertEqual(model['path'], path)

        try:
            model = {'name': 'test', 'path': 'test', 'chunk': 1}
            cm.save(model, model['path'])
        except web.HTTPError as e:
            self.assertEqual('HTTP 400: Bad Request (No file type provided)', str(e))

        try:
            model = {'name': 'test', 'path': 'test', 'chunk': 1, 'type': 'notebook'}
            cm.save(model, model['path'])
        except web.HTTPError as e:
            self.assertEqual('HTTP 400: Bad Request (File type "notebook" is not supported for large file transfer)', str(e))

        try:
            model = {'name': 'test', 'path': 'test', 'chunk': 1, 'type': 'file'}
            cm.save(model, model['path'])
        except web.HTTPError as e:
            self.assertEqual('HTTP 400: Bad Request (No file content provided)', str(e))

        try:
            model = {'name': 'test', 'path': 'test', 'chunk': 2, 'type': 'file',
                     'content': 'test', 'format': 'json'}
            cm.save(model, model['path'])
        except web.HTTPError as e:
            self.assertEqual("HTTP 400: Bad Request (Must specify format of file contents as 'text' or 'base64')",
            				 str(e))

        # Save model for different chunks
        model = {'name': 'test', 'path': 'test', 'type': 'file',
                 'content': 'test==', 'format': 'text'}
        name = model['name']
        path = model['path']
        cm.save(model, path)

        for chunk in (1, 2, -1):
            for fm in ('text', 'base64'):
                full_model = cm.get(path)
                full_model['chunk'] = chunk
                full_model['format'] = fm
                model_res = cm.save(full_model, path)
                assert isinstance(model_res, dict)

                self.assertIn('name', model_res)
                self.assertIn('path', model_res)
                self.assertNotIn('chunk', model_res)
                self.assertEqual(model_res['name'], name)
                self.assertEqual(model_res['path'], path)

        # Test in sub-directory
        # Create a directory and notebook in that directory
        sub_dir = '/foo/'
        self.make_dir('foo')
        model = cm.new_untitled(path=sub_dir, type='notebook')
        name = model['name']
        path = model['path']
        model = cm.get(path)

        # Change the name in the model for rename
        model = cm.save(model, path)
        assert isinstance(model, dict)
        self.assertIn('name', model)
        self.assertIn('path', model)
        self.assertEqual(model['name'], 'Untitled.ipynb')
        self.assertEqual(model['path'], 'foo/Untitled.ipynb')
