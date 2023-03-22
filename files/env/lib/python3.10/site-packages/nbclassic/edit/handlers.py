#encoding: utf-8
"""Tornado handlers for the terminal emulator."""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

from tornado import web, gen

from jupyter_server.base.handlers import JupyterHandler, path_regex
from jupyter_server.utils import url_escape, ensure_async
from jupyter_server.extension.handler import (
    ExtensionHandlerMixin,
    ExtensionHandlerJinjaMixin
)

from nbclassic import nbclassic_path


class EditorHandler(ExtensionHandlerJinjaMixin, ExtensionHandlerMixin, JupyterHandler):
    """Render the text editor interface."""

    @web.authenticated
    @gen.coroutine
    def get(self, path):
        path = path.strip('/')
        exists = yield ensure_async(self.contents_manager.file_exists(path))
        if not exists:
            raise web.HTTPError(404, u'File does not exist: %s' % path)

        basename = path.rsplit('/', 1)[-1]
        self.write(self.render_template('edit.html',
            file_path=url_escape(path),
            basename=basename,
            page_title=basename + " (editing)",
            )
        )


default_handlers = [
    (r"{}/edit{}".format(nbclassic_path(), path_regex), EditorHandler),
]
