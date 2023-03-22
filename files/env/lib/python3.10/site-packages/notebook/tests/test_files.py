"""Test the /files/ handler."""

import os

pjoin = os.path.join

import json

from nbformat import write
from nbformat.v4 import (new_notebook,
                              new_markdown_cell, new_code_cell,
                              new_output)

from notebook.utils import url_path_join
from .launchnotebook import NotebookTestBase


class FilesTest(NotebookTestBase):
    def test_hidden_files(self):
        not_hidden = [
            'å b',
            'å b/ç. d',
        ]
        hidden = [
            '.å b',
            'å b/.ç d',
        ]
        dirs = not_hidden + hidden

        nbdir = self.notebook_dir
        for d in dirs:
            path = pjoin(nbdir, d.replace('/', os.sep))
            if not os.path.exists(path):
                os.mkdir(path)
            with open(pjoin(path, 'foo'), 'w') as f:
                f.write('foo')
            with open(pjoin(path, '.foo'), 'w') as f:
                f.write('.foo')

        for d in not_hidden:
            path = pjoin(nbdir, d.replace('/', os.sep))
            r = self.request('GET', url_path_join('files', d, 'foo'))
            r.raise_for_status()
            self.assertEqual(r.text, 'foo')
            r = self.request('GET', url_path_join('files', d, '.foo'))
            self.assertEqual(r.status_code, 404)

        for d in hidden:
            path = pjoin(nbdir, d.replace('/', os.sep))
            for foo in ('foo', '.foo'):
                r = self.request('GET', url_path_join('files', d, foo))
                self.assertEqual(r.status_code, 404)

        self.notebook.contents_manager.allow_hidden = True
        try:
            for d in not_hidden:
                path = pjoin(nbdir, d.replace('/', os.sep))
                r = self.request('GET', url_path_join('files', d, 'foo'))
                r.raise_for_status()
                self.assertEqual(r.text, 'foo')
                r = self.request('GET', url_path_join('files', d, '.foo'))
                r.raise_for_status()
                self.assertEqual(r.text, '.foo')

            for d in hidden:
                path = pjoin(nbdir, d.replace('/', os.sep))
                for foo in ('foo', '.foo'):
                    r = self.request('GET', url_path_join('files', d, foo))
                    r.raise_for_status()
                    self.assertEqual(r.text, foo)
        finally:
            self.notebook.contents_manager.allow_hidden = False

    def test_contents_manager(self):
        "make sure ContentsManager returns right files (ipynb, bin, txt)."

        nbdir = self.notebook_dir

        nb = new_notebook(
            cells=[
                new_markdown_cell('Created by test ³'),
                new_code_cell("print(2*6)", outputs=[
                    new_output("stream", text="12"),
                ])
            ]
        )

        with open(pjoin(nbdir, 'testnb.ipynb'), 'w',
            encoding='utf-8') as f:
            write(nb, f, version=4)

        with open(pjoin(nbdir, 'test.bin'), 'wb') as f:
            f.write(b'\xff' + os.urandom(5))
            f.close()

        with open(pjoin(nbdir, 'test.txt'), 'w') as f:
            f.write('foobar')
            f.close()

        r = self.request('GET', 'files/testnb.ipynb')
        self.assertEqual(r.status_code, 200)
        self.assertIn('print(2*6)', r.text)
        json.loads(r.text)

        r = self.request('GET', 'files/test.bin')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.headers['content-type'], 'application/octet-stream')
        self.assertEqual(r.content[:1], b'\xff')
        self.assertEqual(len(r.content), 6)

        r = self.request('GET', 'files/test.txt')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.headers['content-type'], 'text/plain; charset=UTF-8')
        self.assertEqual(r.text, 'foobar')

    def test_download(self):
        nbdir = self.notebook_dir

        text = 'hello'
        with open(pjoin(nbdir, 'test.txt'), 'w') as f:
            f.write(text)

        r = self.request('GET', 'files/test.txt')
        disposition = r.headers.get('Content-Disposition', '')
        self.assertNotIn('attachment', disposition)

        r = self.request('GET', 'files/test.txt?download=1')
        disposition = r.headers.get('Content-Disposition', '')
        self.assertIn('attachment', disposition)
        self.assertIn("filename*=utf-8''test.txt", disposition)

    def test_view_html(self):
        nbdir = self.notebook_dir

        html = '<div>Test test</div>'
        with open(pjoin(nbdir, 'test.html'), 'w') as f:
            f.write(html)

        r = self.request('GET', 'view/test.html')
        self.assertEqual(r.status_code, 200)

    def test_old_files_redirect(self):
        """pre-2.0 'files/' prefixed links are properly redirected"""
        nbdir = self.notebook_dir

        os.mkdir(pjoin(nbdir, 'files'))
        os.makedirs(pjoin(nbdir, 'sub', 'files'))

        for prefix in ('', 'sub'):
            with open(pjoin(nbdir, prefix, 'files', 'f1.txt'), 'w') as f:
                f.write(prefix + '/files/f1')
            with open(pjoin(nbdir, prefix, 'files', 'f2.txt'), 'w') as f:
                f.write(prefix + '/files/f2')
            with open(pjoin(nbdir, prefix, 'f2.txt'), 'w') as f:
                f.write(prefix + '/f2')
            with open(pjoin(nbdir, prefix, 'f3.txt'), 'w') as f:
                f.write(prefix + '/f3')

            url = url_path_join('notebooks', prefix, 'files', 'f1.txt')
            r = self.request('GET', url)
            self.assertEqual(r.status_code, 200)
            self.assertEqual(r.text, prefix + '/files/f1')

            url = url_path_join('notebooks', prefix, 'files', 'f2.txt')
            r = self.request('GET', url)
            self.assertEqual(r.status_code, 200)
            self.assertEqual(r.text, prefix + '/files/f2')

            url = url_path_join('notebooks', prefix, 'files', 'f3.txt')
            r = self.request('GET', url)
            self.assertEqual(r.status_code, 200)
            self.assertEqual(r.text, prefix + '/f3')
