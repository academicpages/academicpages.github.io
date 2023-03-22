"""Tornado handlers for the tree view.

This is a fork from jupyter/notebook#5.7.x
"""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

import re
from tornado import web, gen

from jupyter_server.base.handlers import JupyterHandler
from jupyter_server.extension.handler import (
    ExtensionHandlerMixin,
    ExtensionHandlerJinjaMixin
)
from jupyter_server.base.handlers import path_regex
from jupyter_server.utils import url_path_join, url_escape, ensure_async

from nbclassic import nbclassic_path


class TreeHandler(ExtensionHandlerJinjaMixin, ExtensionHandlerMixin, JupyterHandler):
    """Render the tree view, listing notebooks, etc."""

    def generate_breadcrumbs(self, path):
        breadcrumbs = [(url_path_join(self.base_url, 'tree'), '')]
        parts = path.split('/')
        for i in range(len(parts)):
            if parts[i]:
                link = url_path_join(self.base_url, 'tree',
                    url_escape(url_path_join(*parts[:i+1])),
                )
                breadcrumbs.append((link, parts[i]))
        return breadcrumbs

    def generate_page_title(self, path):
        comps = path.split('/')
        if len(comps) > 3:
            for i in range(len(comps)-2):
                comps.pop(0)
        page_title = url_path_join(*comps)
        if page_title:
            return page_title+'/'
        else:
            return 'Home'

    @web.authenticated
    @gen.coroutine
    def get(self, path=''):
        path = path.strip('/')
        cm = self.contents_manager

        file_exists = False
        dir_exists = yield ensure_async(cm.dir_exists(path=path))
        if not dir_exists:
            file_exists = yield ensure_async(cm.file_exists(path))
        if dir_exists:
            is_hidden = yield ensure_async(cm.is_hidden(path))
            if is_hidden and not cm.allow_hidden:
                self.log.info("Refusing to serve hidden directory, via 404 Error")
                raise web.HTTPError(404)
            breadcrumbs = self.generate_breadcrumbs(path)
            page_title = self.generate_page_title(path)
            self.write(self.render_template('tree.html',
                page_title=page_title,
                notebook_path=path,
                breadcrumbs=breadcrumbs,
                terminals_available=self.settings['terminals_available'],
                server_root=self.settings['server_root_dir'],
                shutdown_button=self.settings.get('shutdown_button', False)
            ))
        elif file_exists :
            # it's not a directory, we have redirecting to do
            model = yield ensure_async(cm.get(path, content=False))
            # redirect to /api/notebooks if it's a notebook, otherwise /api/files
            service = 'notebooks' if model['type'] == 'notebook' else 'files'
            url = url_path_join(
                self.base_url, service, url_escape(path),
            )
            self.log.debug("Redirecting %s to %s", self.request.path, url)
            self.redirect(url)
        else:
            raise web.HTTPError(404)


#-----------------------------------------------------------------------------
# URL to handler mappings
#-----------------------------------------------------------------------------


default_handlers = [
    (r"{}/tree{}".format(nbclassic_path(), path_regex), TreeHandler),
    (r"%s/tree" % nbclassic_path(), TreeHandler),
]
