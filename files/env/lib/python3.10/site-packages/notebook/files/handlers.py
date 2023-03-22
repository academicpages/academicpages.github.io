"""Serve files directly from the ContentsManager."""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

import mimetypes
import json
from base64 import decodebytes

from tornado import  gen, web

from notebook.base.handlers import IPythonHandler
from notebook.utils import maybe_future


class FilesHandler(IPythonHandler):
    """serve files via ContentsManager

    Normally used when ContentsManager is not a FileContentsManager.

    FileContentsManager subclasses use AuthenticatedFilesHandler by default,
    a subclass of StaticFileHandler.
    """

    @property
    def content_security_policy(self):
        # In case we're serving HTML/SVG, confine any Javascript to a unique
        # origin so it can't interact with the notebook server.
        return super().content_security_policy + "; sandbox allow-scripts"

    @web.authenticated
    def head(self, path):
        self.check_xsrf_cookie()
        return self.get(path, include_body=False)

    @web.authenticated
    @gen.coroutine
    def get(self, path, include_body=True):
        # /files/ requests must originate from the same site
        self.check_xsrf_cookie()
        cm = self.contents_manager

        if cm.is_hidden(path) and not cm.allow_hidden:
            self.log.info("Refusing to serve hidden file, via 404 Error")
            raise web.HTTPError(404)

        path = path.strip('/')
        if '/' in path:
            _, name = path.rsplit('/', 1)
        else:
            name = path
        
        model = yield maybe_future(cm.get(path, type='file', content=include_body))
        
        if self.get_argument("download", False):
            self.set_attachment_header(name)
        
        # get mimetype from filename
        if name.lower().endswith('.ipynb'):
            self.set_header('Content-Type', 'application/x-ipynb+json')
        else:
            cur_mime = mimetypes.guess_type(name)[0]
            if cur_mime == 'text/plain':
                self.set_header('Content-Type', 'text/plain; charset=UTF-8')
            elif cur_mime is not None:
                self.set_header('Content-Type', cur_mime)
            else:
                if model['format'] == 'base64':
                    self.set_header('Content-Type', 'application/octet-stream')
                else:
                    self.set_header('Content-Type', 'text/plain; charset=UTF-8')

        if include_body:
            if model['format'] == 'base64':
                b64_bytes = model['content'].encode('ascii')
                self.write(decodebytes(b64_bytes))
            elif model['format'] == 'json':
                self.write(json.dumps(model['content']))
            else:
                self.write(model['content'])
            self.flush()


default_handlers = []
