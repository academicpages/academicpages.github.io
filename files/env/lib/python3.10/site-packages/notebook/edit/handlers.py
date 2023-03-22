"""Tornado handlers for the terminal emulator."""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

from tornado import web
from ..base.handlers import IPythonHandler, path_regex
from ..utils import url_escape

class EditorHandler(IPythonHandler):
    """Render the text editor interface."""
    @web.authenticated
    def get(self, path):
        path = path.strip('/')
        if not self.contents_manager.file_exists(path):
            raise web.HTTPError(404, f'File does not exist: {path}')

        basename = path.rsplit('/', 1)[-1]
        self.write(self.render_template('edit.html',
            file_path=url_escape(path),
            basename=basename,
            page_title=basename + " (editing)",
            )
        )

default_handlers = [
    (fr"/edit{path_regex}", EditorHandler),
]
