"""Tornado handlers for viewing HTML files."""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

from tornado import web
from ..base.handlers import IPythonHandler, path_regex
from ..utils import url_escape, url_path_join

class ViewHandler(IPythonHandler):
    """Render HTML files within an iframe."""
    @web.authenticated
    def get(self, path):
        path = path.strip('/')
        if not self.contents_manager.file_exists(path):
            raise web.HTTPError(404, f'File does not exist: {path}')

        basename = path.rsplit('/', 1)[-1]
        file_url = url_path_join(self.base_url, 'files', url_escape(path))
        self.write(
            self.render_template('view.html', file_url=file_url, page_title=basename)
        )

default_handlers = [
    (fr"/view{path_regex}", ViewHandler),
]
