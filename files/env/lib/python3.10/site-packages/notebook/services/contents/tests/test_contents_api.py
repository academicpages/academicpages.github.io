"""Test the contents webservice API."""

from contextlib import contextmanager
from functools import partial
import json
import os
import shutil
import sys
from unicodedata import normalize

pjoin = os.path.join

import requests
from send2trash import send2trash
from send2trash.exceptions import TrashPermissionError

from ..filecheckpoints import GenericFileCheckpoints

from traitlets.config import Config
from notebook.utils import url_path_join, url_escape, to_os_path
from notebook.tests.launchnotebook import NotebookTestBase, assert_http_error
from nbformat import write, from_dict
from nbformat.v4 import (
    new_notebook, new_markdown_cell,
)
from nbformat import v2
from ipython_genutils import py3compat
from ipython_genutils.tempdir import TemporaryDirectory

from base64 import encodebytes, decodebytes


def uniq_stable(elems):
    """uniq_stable(elems) -> list

    Return from an iterable, a list of all the unique elements in the input,
    maintaining the order in which they first appear.
    """
    seen = set()
    return [x for x in elems if x not in seen and not seen.add(x)]

def notebooks_only(dir_model):
    return [nb for nb in dir_model['content'] if nb['type']=='notebook']

def dirs_only(dir_model):
    return [x for x in dir_model['content'] if x['type']=='directory']


class API:
    """Wrapper for contents API calls."""
    def __init__(self, request):
        self.request = request

    def _req(self, verb, path, body=None, params=None):
        response = self.request(verb,
                url_path_join('api/contents', path),
                data=body, params=params,
        )
        response.raise_for_status()
        return response

    def list(self, path='/'):
        return self._req('GET', path)

    def read(self, path, type=None, format=None, content=None):
        params = {}
        if type is not None:
            params['type'] = type
        if format is not None:
            params['format'] = format
        if content == False:
            params['content'] = '0'
        return self._req('GET', path, params=params)

    def create_untitled(self, path='/', ext='.ipynb'):
        body = None
        if ext:
            body = json.dumps({'ext': ext})
        return self._req('POST', path, body)

    def mkdir_untitled(self, path='/'):
        return self._req('POST', path, json.dumps({'type': 'directory'}))

    def copy(self, copy_from, path='/'):
        body = json.dumps({'copy_from':copy_from})
        return self._req('POST', path, body)

    def create(self, path='/'):
        return self._req('PUT', path)

    def upload(self, path, body):
        return self._req('PUT', path, body)

    def mkdir(self, path='/'):
        return self._req('PUT', path, json.dumps({'type': 'directory'}))

    def copy_put(self, copy_from, path='/'):
        body = json.dumps({'copy_from':copy_from})
        return self._req('PUT', path, body)

    def save(self, path, body):
        return self._req('PUT', path, body)

    def delete(self, path='/'):
        return self._req('DELETE', path)

    def rename(self, path, new_path):
        body = json.dumps({'path': new_path})
        return self._req('PATCH', path, body)

    def get_checkpoints(self,  path):
        return self._req('GET', url_path_join(path, 'checkpoints'))

    def new_checkpoint(self,  path):
        return self._req('POST', url_path_join(path, 'checkpoints'))

    def restore_checkpoint(self, path, checkpoint_id):
        return self._req('POST', url_path_join(path, 'checkpoints', checkpoint_id))

    def delete_checkpoint(self, path, checkpoint_id):
        return self._req('DELETE', url_path_join(path, 'checkpoints', checkpoint_id))

class APITest(NotebookTestBase):
    """Test the kernels web service API"""
    dirs_nbs = [('', 'inroot'),
                ('Directory with spaces in', 'inspace'),
                ('unicodé', 'innonascii'),
                ('foo', 'a'),
                ('foo', 'b'),
                ('foo', 'name with spaces'),
                ('foo', 'unicodé'),
                ('foo/bar', 'baz'),
                ('ordering', 'A'),
                ('ordering', 'b'),
                ('ordering', 'C'),
                ('å b', 'ç d'),
               ]
    hidden_dirs = ['.hidden', '__pycache__']

    # Don't include root dir.
    dirs = uniq_stable([py3compat.cast_unicode(d) for (d,n) in dirs_nbs[1:]])
    top_level_dirs = {normalize('NFC', d.split('/')[0]) for d in dirs}

    @staticmethod
    def _blob_for_name(name):
        return name.encode('utf-8') + b'\xFF'

    @staticmethod
    def _txt_for_name(name):
        return f'{name} text file'

    def to_os_path(self, api_path):
        return to_os_path(api_path, root=self.notebook_dir)

    def make_dir(self, api_path):
        """Create a directory at api_path"""
        os_path = self.to_os_path(api_path)
        try:
            os.makedirs(os_path)
        except OSError:
            print(f"Directory already exists: {os_path!r}")

    def make_txt(self, api_path, txt):
        """Make a text file at a given api_path"""
        os_path = self.to_os_path(api_path)
        with open(os_path, 'w', encoding='utf-8') as f:
            f.write(txt)

    def make_blob(self, api_path, blob):
        """Make a binary file at a given api_path"""
        os_path = self.to_os_path(api_path)
        with open(os_path, 'wb') as f:
            f.write(blob)

    def make_nb(self, api_path, nb):
        """Make a notebook file at a given api_path"""
        os_path = self.to_os_path(api_path)

        with open(os_path, 'w', encoding='utf-8') as f:
            write(nb, f, version=4)

    def delete_dir(self, api_path):
        """Delete a directory at api_path, removing any contents."""
        os_path = self.to_os_path(api_path)
        shutil.rmtree(os_path, ignore_errors=True)

    def delete_file(self, api_path):
        """Delete a file at the given path if it exists."""
        if self.isfile(api_path):
            os.unlink(self.to_os_path(api_path))

    def isfile(self, api_path):
        return os.path.isfile(self.to_os_path(api_path))

    def isdir(self, api_path):
        return os.path.isdir(self.to_os_path(api_path))

    def can_send2trash(self, api_path):
        """Send a path to trash, if possible. Return success."""
        try:
            send2trash(self.to_os_path(api_path))
            return True
        except TrashPermissionError as e:
            return False

    def setUp(self):
        for d in (self.dirs + self.hidden_dirs):
            self.make_dir(d)
            self.addCleanup(partial(self.delete_dir, d))

        for d, name in self.dirs_nbs:
            # create a notebook
            nb = new_notebook()
            nbname = f'{d}/{name}.ipynb'
            self.make_nb(nbname, nb)
            self.addCleanup(partial(self.delete_file, nbname))

            # create a text file
            txt = self._txt_for_name(name)
            txtname = f'{d}/{name}.txt'
            self.make_txt(txtname, txt)
            self.addCleanup(partial(self.delete_file, txtname))

            blob = self._blob_for_name(name)
            blobname = f'{d}/{name}.blob'
            self.make_blob(blobname, blob)
            self.addCleanup(partial(self.delete_file, blobname))

        self.api = API(self.request)

    def test_list_notebooks(self):
        nbs = notebooks_only(self.api.list().json())
        self.assertEqual(len(nbs), 1)
        self.assertEqual(nbs[0]['name'], 'inroot.ipynb')

        nbs = notebooks_only(self.api.list('/Directory with spaces in/').json())
        self.assertEqual(len(nbs), 1)
        self.assertEqual(nbs[0]['name'], 'inspace.ipynb')

        nbs = notebooks_only(self.api.list('/unicodé/').json())
        self.assertEqual(len(nbs), 1)
        self.assertEqual(nbs[0]['name'], 'innonascii.ipynb')
        self.assertEqual(nbs[0]['path'], 'unicodé/innonascii.ipynb')

        nbs = notebooks_only(self.api.list('/foo/bar/').json())
        self.assertEqual(len(nbs), 1)
        self.assertEqual(nbs[0]['name'], 'baz.ipynb')
        self.assertEqual(nbs[0]['path'], 'foo/bar/baz.ipynb')

        nbs = notebooks_only(self.api.list('foo').json())
        self.assertEqual(len(nbs), 4)
        nbnames = { normalize('NFC', n['name']) for n in nbs }
        expected = [ 'a.ipynb', 'b.ipynb', 'name with spaces.ipynb', 'unicodé.ipynb']
        expected = { normalize('NFC', name) for name in expected }
        self.assertEqual(nbnames, expected)

        nbs = notebooks_only(self.api.list('ordering').json())
        nbnames = {n['name'] for n in nbs}
        expected = {'A.ipynb', 'b.ipynb', 'C.ipynb'}
        self.assertEqual(nbnames, expected)

    def test_list_dirs(self):
        dirs = dirs_only(self.api.list().json())
        dir_names = {normalize('NFC', d['name']) for d in dirs}
        self.assertEqual(dir_names, self.top_level_dirs)  # Excluding hidden dirs

    def test_get_dir_no_content(self):
        for d in self.dirs:
            model = self.api.read(d, content=False).json()
            self.assertEqual(model['path'], d)
            self.assertEqual(model['type'], 'directory')
            self.assertIn('content', model)
            self.assertEqual(model['content'], None)

    def test_list_nonexistant_dir(self):
        with assert_http_error(404):
            self.api.list('nonexistant')

    def test_get_nb_contents(self):
        for d, name in self.dirs_nbs:
            path = url_path_join(d, name + '.ipynb')
            nb = self.api.read(path).json()
            self.assertEqual(nb['name'], f'{name}.ipynb')
            self.assertEqual(nb['path'], path)
            self.assertEqual(nb['type'], 'notebook')
            self.assertIn('content', nb)
            self.assertEqual(nb['format'], 'json')
            self.assertIn('metadata', nb['content'])
            self.assertIsInstance(nb['content']['metadata'], dict)

    def test_get_nb_no_content(self):
        for d, name in self.dirs_nbs:
            path = url_path_join(d, name + '.ipynb')
            nb = self.api.read(path, content=False).json()
            self.assertEqual(nb['name'], f'{name}.ipynb')
            self.assertEqual(nb['path'], path)
            self.assertEqual(nb['type'], 'notebook')
            self.assertIn('content', nb)
            self.assertEqual(nb['content'], None)

    def test_get_nb_invalid(self):
        nb = {
            'nbformat': 4,
            'metadata': {},
            'cells': [{
                'cell_type': 'wrong',
                'metadata': {},
            }],
        }
        path = 'å b/Validate tést.ipynb'
        self.make_txt(path, py3compat.cast_unicode(json.dumps(nb)))
        model = self.api.read(path).json()
        self.assertEqual(model['path'], path)
        self.assertEqual(model['type'], 'notebook')
        self.assertIn('content', model)
        self.assertIn('message', model)
        self.assertIn("validation failed", model['message'].lower())

    def test_get_contents_no_such_file(self):
        # Name that doesn't exist - should be a 404
        with assert_http_error(404):
            self.api.read('foo/q.ipynb')

    def test_get_404_hidden(self):
        if sys.platform == 'win32':
            self.skipTest("Disabled copying hidden files on Windows")
        self.make_txt('.hidden/visible.txt', 'test string')
        self.make_txt('.hidden.txt', 'test string')
        with assert_http_error(404):
            resp = self.api.read('.hidden/visible.txt')
        with assert_http_error(404):
            resp = self.api.read('.hidden.txt')

    def test_get_text_file_contents(self):
        for d, name in self.dirs_nbs:
            path = url_path_join(d, name + '.txt')
            model = self.api.read(path).json()
            self.assertEqual(model['name'], f'{name}.txt')
            self.assertEqual(model['path'], path)
            self.assertIn('content', model)
            self.assertEqual(model['format'], 'text')
            self.assertEqual(model['type'], 'file')
            self.assertEqual(model['content'], self._txt_for_name(name))

        # Name that doesn't exist - should be a 404
        with assert_http_error(404):
            self.api.read('foo/q.txt')

        # Specifying format=text should fail on a non-UTF-8 file
        with assert_http_error(400):
            self.api.read('foo/bar/baz.blob', type='file', format='text')

    def test_get_binary_file_contents(self):
        for d, name in self.dirs_nbs:
            path = url_path_join(d, name + '.blob')
            model = self.api.read(path).json()
            self.assertEqual(model['name'], f'{name}.blob')
            self.assertEqual(model['path'], path)
            self.assertIn('content', model)
            self.assertEqual(model['format'], 'base64')
            self.assertEqual(model['type'], 'file')
            self.assertEqual(
                decodebytes(model['content'].encode('ascii')),
                self._blob_for_name(name),
            )

        # Name that doesn't exist - should be a 404
        with assert_http_error(404):
            self.api.read('foo/q.txt')

    def test_get_bad_type(self):
        with assert_http_error(400):
            self.api.read('unicodé', type='file')  # this is a directory

        with assert_http_error(400):
            self.api.read('unicodé/innonascii.ipynb', type='directory')

    def _check_created(self, resp, path, type='notebook'):
        self.assertEqual(resp.status_code, 201)
        location_header = py3compat.str_to_unicode(resp.headers['Location'])
        self.assertEqual(location_header, url_path_join(self.url_prefix, 'api/contents', url_escape(path)))
        rjson = resp.json()
        self.assertEqual(rjson['name'], path.rsplit('/', 1)[-1])
        self.assertEqual(rjson['path'], path)
        self.assertEqual(rjson['type'], type)
        isright = self.isdir if type == 'directory' else self.isfile
        assert isright(path)

    def test_create_untitled(self):
        resp = self.api.create_untitled(path='å b')
        self._check_created(resp, 'å b/Untitled.ipynb')

        # Second time
        resp = self.api.create_untitled(path='å b')
        self._check_created(resp, 'å b/Untitled1.ipynb')

        # And two directories down
        resp = self.api.create_untitled(path='foo/bar')
        self._check_created(resp, 'foo/bar/Untitled.ipynb')

    def test_create_untitled_txt(self):
        resp = self.api.create_untitled(path='foo/bar', ext='.txt')
        self._check_created(resp, 'foo/bar/untitled.txt', type='file')

        resp = self.api.read(path='foo/bar/untitled.txt')
        model = resp.json()
        self.assertEqual(model['type'], 'file')
        self.assertEqual(model['format'], 'text')
        self.assertEqual(model['content'], '')

    def test_upload(self):
        nb = new_notebook()
        nbmodel = {'content': nb, 'type': 'notebook'}
        path = 'å b/Upload tést.ipynb'
        resp = self.api.upload(path, body=json.dumps(nbmodel))
        self._check_created(resp, path)

    def test_mkdir_untitled(self):
        resp = self.api.mkdir_untitled(path='å b')
        self._check_created(resp, 'å b/Untitled Folder', type='directory')

        # Second time
        resp = self.api.mkdir_untitled(path='å b')
        self._check_created(resp, 'å b/Untitled Folder 1', type='directory')

        # And two directories down
        resp = self.api.mkdir_untitled(path='foo/bar')
        self._check_created(resp, 'foo/bar/Untitled Folder', type='directory')

    def test_mkdir(self):
        path = 'å b/New ∂ir'
        resp = self.api.mkdir(path)
        self._check_created(resp, path, type='directory')

    def test_mkdir_hidden_400(self):
        with assert_http_error(400):
            resp = self.api.mkdir('å b/.hidden')

    def test_upload_txt(self):
        body = 'ünicode téxt'
        model = {
            'content' : body,
            'format'  : 'text',
            'type'    : 'file',
        }
        path = 'å b/Upload tést.txt'
        resp = self.api.upload(path, body=json.dumps(model))

        # check roundtrip
        resp = self.api.read(path)
        model = resp.json()
        self.assertEqual(model['type'], 'file')
        self.assertEqual(model['format'], 'text')
        self.assertEqual(model['content'], body)

    def test_upload_txt_hidden(self):
        if sys.platform == 'win32':
            self.skipTest("Disabled copying hidden files on Windows")
        with assert_http_error(400):
            body = 'ünicode téxt'
            model = {
                'content' : body,
                'format'  : 'text',
                'type'    : 'file',
            }
            path = '.hidden/Upload tést.txt'
            resp = self.api.upload(path, body=json.dumps(model))

        with assert_http_error(400):
            body = 'ünicode téxt'
            model = {
                'content' : body,
                'format'  : 'text',
                'type'    : 'file',
                'path': '.hidden/test.txt'
            }
            path = 'Upload tést.txt'
            resp = self.api.upload(path, body=json.dumps(model))

        with assert_http_error(400):
            body = 'ünicode téxt'
            model = {
                'content' : body,
                'format'  : 'text',
                'type'    : 'file',
            }
            path = '.hidden.txt'
            resp = self.api.upload(path, body=json.dumps(model))

        with assert_http_error(400):
            body = 'ünicode téxt'
            model = {
                'content' : body,
                'format'  : 'text',
                'type'    : 'file',
                'path': '.hidden.txt'
            }
            path = 'Upload tést.txt'
            resp = self.api.upload(path, body=json.dumps(model))

    def test_upload_b64(self):
        body = b'\xFFblob'
        b64body = encodebytes(body).decode('ascii')
        model = {
            'content' : b64body,
            'format'  : 'base64',
            'type'    : 'file',
        }
        path = 'å b/Upload tést.blob'
        resp = self.api.upload(path, body=json.dumps(model))

        # check roundtrip
        resp = self.api.read(path)
        model = resp.json()
        self.assertEqual(model['type'], 'file')
        self.assertEqual(model['path'], path)
        self.assertEqual(model['format'], 'base64')
        decoded = decodebytes(model['content'].encode('ascii'))
        self.assertEqual(decoded, body)

    def test_upload_v2(self):
        nb = v2.new_notebook()
        ws = v2.new_worksheet()
        nb.worksheets.append(ws)
        ws.cells.append(v2.new_code_cell(input='print("hi")'))
        nbmodel = {'content': nb, 'type': 'notebook'}
        path = 'å b/Upload tést.ipynb'
        resp = self.api.upload(path, body=json.dumps(nbmodel))
        self._check_created(resp, path)
        resp = self.api.read(path)
        data = resp.json()
        self.assertEqual(data['content']['nbformat'], 4)

    def test_copy(self):
        resp = self.api.copy('å b/ç d.ipynb', 'å b')
        self._check_created(resp, 'å b/ç d-Copy1.ipynb')

        resp = self.api.copy('å b/ç d.ipynb', 'å b')
        self._check_created(resp, 'å b/ç d-Copy2.ipynb')

    def test_copy_copy(self):
        resp = self.api.copy('å b/ç d.ipynb', 'å b')
        self._check_created(resp, 'å b/ç d-Copy1.ipynb')

        resp = self.api.copy('å b/ç d-Copy1.ipynb', 'å b')
        self._check_created(resp, 'å b/ç d-Copy2.ipynb')

    def test_copy_path(self):
        resp = self.api.copy('foo/a.ipynb', 'å b')
        self._check_created(resp, 'å b/a.ipynb')

        resp = self.api.copy('foo/a.ipynb', 'å b')
        self._check_created(resp, 'å b/a-Copy1.ipynb')

    def test_copy_400_hidden(self):
        if sys.platform == 'win32':
            self.skipTest("Disabled copying hidden files on Windows")
        self.make_txt('new.txt', 'test string')
        self.make_txt('.hidden/new.txt', 'test string')
        self.make_txt('.hidden.txt', 'test string')
        with assert_http_error(400):
            resp = self.api.copy('.hidden/old.txt', 'new.txt')
        with assert_http_error(400):
            resp = self.api.copy('old.txt', '.hidden/new.txt')
        with assert_http_error(400):
            resp = self.api.copy('.hidden.txt', 'new.txt')
        with assert_http_error(400):
            resp = self.api.copy('old.txt', '.hidden.txt')

    def test_copy_put_400(self):
        with assert_http_error(400):
            resp = self.api.copy_put('å b/ç d.ipynb', 'å b/cøpy.ipynb')

    def test_copy_put_400_hidden(self):
        if sys.platform == 'win32':
            self.skipTest("Disabled copying hidden files on Windows")
        with assert_http_error(400):
            resp = self.api.copy_put('.hidden/old.txt', 'new.txt')
        with assert_http_error(400):
            resp = self.api.copy_put('old.txt', '.hidden/new.txt')
        with assert_http_error(400):
            resp = self.api.copy_put('.hidden.txt', 'new.txt')
        with assert_http_error(400):
            resp = self.api.copy_put('old.txt', '.hidden.txt')

    def test_copy_dir_400(self):
        # can't copy directories
        with assert_http_error(400):
            resp = self.api.copy('å b', 'foo')

    def test_delete(self):
        for d, name in self.dirs_nbs:
            print(f'{d!r}, {name!r}')
            resp = self.api.delete(url_path_join(d, name + '.ipynb'))
            self.assertEqual(resp.status_code, 204)

        for d in self.dirs + ['/']:
            nbs = notebooks_only(self.api.list(d).json())
            print('------')
            print(d)
            print(nbs)
            self.assertEqual(nbs, [])

    def test_delete_dirs(self):
        # depth-first delete everything, so we don't try to delete empty directories
        for name in sorted(self.dirs + ['/'], key=len, reverse=True):
            listing = self.api.list(name).json()['content']
            for model in listing:
                self.api.delete(model['path'])
        listing = self.api.list('/').json()['content']
        self.assertEqual(listing, [])

    def test_delete_non_empty_dir(self):
        if sys.platform == 'win32':
            self.skipTest("Disabled deleting non-empty dirs on Windows")
        # Test that non empty directory can be deleted
        try:
            self.api.delete('å b')
        except requests.HTTPError as e:
            if e.response.status_code == 400:
                if not self.can_send2trash('å b'):
                    self.skipTest("Dir can't be sent to trash")
            raise
        # Check if directory has actually been deleted
        with assert_http_error(404):
            self.api.list('å b')

    def test_delete_hidden_dir(self):
        if sys.platform == 'win32':
            self.skipTest("Disabled deleting hidden dirs on Windows")
        with assert_http_error(400):
            # Test that non empty directory can be deleted
            try:
                self.api.delete('.hidden')
            except requests.HTTPError as e:
                assert e.response.status_code == 400
                raise e

    def test_delete_hidden_file(self):
        #Test deleting file in a hidden directory
        if sys.platform == 'win32':
            self.skipTest("Disabled deleting hidden dirs on Windows")
        with assert_http_error(400):
            # Test that non empty directory can be deleted
            self.api.delete('.hidden/test.txt')

        #Test deleting a hidden file
        with assert_http_error(400):
            self.api.delete('.hidden.txt')

    def test_rename(self):
        resp = self.api.rename('foo/a.ipynb', 'foo/z.ipynb')
        self.assertEqual(resp.headers['Location'].split('/')[-1], 'z.ipynb')
        self.assertEqual(resp.json()['name'], 'z.ipynb')
        self.assertEqual(resp.json()['path'], 'foo/z.ipynb')
        assert self.isfile('foo/z.ipynb')

        nbs = notebooks_only(self.api.list('foo').json())
        nbnames = {n['name'] for n in nbs}
        self.assertIn('z.ipynb', nbnames)
        self.assertNotIn('a.ipynb', nbnames)

    def test_rename_400_hidden(self):
        if sys.platform == 'win32':
            self.skipTest("Disabled copying hidden files on Windows")
        # self.make_txt('new.txt', 'test string')
        # self.make_txt('.hidden/new.txt', 'test string')
        # self.make_txt('.hidden.txt', 'test string')
        with assert_http_error(400):
            resp = self.api.rename('.hidden/old.txt', 'new.txt')
        with assert_http_error(400):
            resp = self.api.rename('old.txt', '.hidden/new.txt')
        with assert_http_error(400):
            resp = self.api.rename('.hidden.txt', 'new.txt')
        with assert_http_error(400):
            resp = self.api.rename('old.txt', '.hidden.txt')

    def test_checkpoints_follow_file(self):

        # Read initial file state
        orig = self.api.read('foo/a.ipynb')

        # Create a checkpoint of initial state
        r = self.api.new_checkpoint('foo/a.ipynb')
        cp1 = r.json()

        # Modify file and save
        nbcontent = json.loads(orig.text)['content']
        nb = from_dict(nbcontent)
        hcell = new_markdown_cell('Created by test')
        nb.cells.append(hcell)
        nbmodel = {'content': nb, 'type': 'notebook'}
        self.api.save('foo/a.ipynb', body=json.dumps(nbmodel))

        # Rename the file.
        self.api.rename('foo/a.ipynb', 'foo/z.ipynb')

        # Looking for checkpoints in the old location should yield no results.
        self.assertEqual(self.api.get_checkpoints('foo/a.ipynb').json(), [])

        # Looking for checkpoints in the new location should work.
        cps = self.api.get_checkpoints('foo/z.ipynb').json()
        self.assertEqual(cps, [cp1])

        # Delete the file.  The checkpoint should be deleted as well.
        self.api.delete('foo/z.ipynb')
        cps = self.api.get_checkpoints('foo/z.ipynb').json()
        self.assertEqual(cps, [])

    def test_rename_existing(self):
        with assert_http_error(409):
            self.api.rename('foo/a.ipynb', 'foo/b.ipynb')

    def test_save(self):
        resp = self.api.read('foo/a.ipynb')
        nbcontent = json.loads(resp.text)['content']
        nb = from_dict(nbcontent)
        nb.cells.append(new_markdown_cell('Created by test ³'))

        nbmodel = {'content': nb, 'type': 'notebook'}
        resp = self.api.save('foo/a.ipynb', body=json.dumps(nbmodel))

        nbcontent = self.api.read('foo/a.ipynb').json()['content']
        newnb = from_dict(nbcontent)
        self.assertEqual(newnb.cells[0].source,
                         'Created by test ³')

    def test_checkpoints(self):
        resp = self.api.read('foo/a.ipynb')
        r = self.api.new_checkpoint('foo/a.ipynb')
        self.assertEqual(r.status_code, 201)
        cp1 = r.json()
        self.assertEqual(set(cp1), {'id', 'last_modified'})
        self.assertEqual(r.headers['Location'].split('/')[-1], cp1['id'])

        # Modify it
        nbcontent = json.loads(resp.text)['content']
        nb = from_dict(nbcontent)
        hcell = new_markdown_cell('Created by test')
        nb.cells.append(hcell)
        # Save
        nbmodel= {'content': nb, 'type': 'notebook'}
        resp = self.api.save('foo/a.ipynb', body=json.dumps(nbmodel))

        # List checkpoints
        cps = self.api.get_checkpoints('foo/a.ipynb').json()
        self.assertEqual(cps, [cp1])

        nbcontent = self.api.read('foo/a.ipynb').json()['content']
        nb = from_dict(nbcontent)
        self.assertEqual(nb.cells[0].source, 'Created by test')

        # Restore cp1
        r = self.api.restore_checkpoint('foo/a.ipynb', cp1['id'])
        self.assertEqual(r.status_code, 204)
        nbcontent = self.api.read('foo/a.ipynb').json()['content']
        nb = from_dict(nbcontent)
        self.assertEqual(nb.cells, [])

        # Delete cp1
        r = self.api.delete_checkpoint('foo/a.ipynb', cp1['id'])
        self.assertEqual(r.status_code, 204)
        cps = self.api.get_checkpoints('foo/a.ipynb').json()
        self.assertEqual(cps, [])

    def test_file_checkpoints(self):
        """
        Test checkpointing of non-notebook files.
        """
        filename = 'foo/a.txt'
        resp = self.api.read(filename)
        orig_content = json.loads(resp.text)['content']

        # Create a checkpoint.
        r = self.api.new_checkpoint(filename)
        self.assertEqual(r.status_code, 201)
        cp1 = r.json()
        self.assertEqual(set(cp1), {'id', 'last_modified'})
        self.assertEqual(r.headers['Location'].split('/')[-1], cp1['id'])

        # Modify the file and save.
        new_content = orig_content + '\nsecond line'
        model = {
            'content': new_content,
            'type': 'file',
            'format': 'text',
        }
        resp = self.api.save(filename, body=json.dumps(model))

        # List checkpoints
        cps = self.api.get_checkpoints(filename).json()
        self.assertEqual(cps, [cp1])

        content = self.api.read(filename).json()['content']
        self.assertEqual(content, new_content)

        # Restore cp1
        r = self.api.restore_checkpoint(filename, cp1['id'])
        self.assertEqual(r.status_code, 204)
        restored_content = self.api.read(filename).json()['content']
        self.assertEqual(restored_content, orig_content)

        # Delete cp1
        r = self.api.delete_checkpoint(filename, cp1['id'])
        self.assertEqual(r.status_code, 204)
        cps = self.api.get_checkpoints(filename).json()
        self.assertEqual(cps, [])

    @contextmanager
    def patch_cp_root(self, dirname):
        """
        Temporarily patch the root dir of our checkpoint manager.
        """
        cpm = self.notebook.contents_manager.checkpoints
        old_dirname = cpm.root_dir
        cpm.root_dir = dirname
        try:
            yield
        finally:
            cpm.root_dir = old_dirname

    def test_checkpoints_separate_root(self):
        """
        Test that FileCheckpoints functions correctly even when it's
        using a different root dir from FileContentsManager.  This also keeps
        the implementation honest for use with ContentsManagers that don't map
        models to the filesystem

        Override this method to a no-op when testing other managers.
        """
        with TemporaryDirectory() as td:
            with self.patch_cp_root(td):
                self.test_checkpoints()

        with TemporaryDirectory() as td:
            with self.patch_cp_root(td):
                self.test_file_checkpoints()


class GenericFileCheckpointsAPITest(APITest):
    """
    Run the tests from APITest with GenericFileCheckpoints.
    """
    config = Config()
    config.FileContentsManager.checkpoints_class = GenericFileCheckpoints

    def test_config_did_something(self):

        self.assertIsInstance(
            self.notebook.contents_manager.checkpoints,
            GenericFileCheckpoints,
        )


