#############################################################################
# Copyright (c) 2018, Voilà Contributors                                    #
# Copyright (c) 2018, QuantStack                                            #
#                                                                           #
# Distributed under the terms of the BSD 3-Clause License.                  #
#                                                                           #
# The full license is in the file LICENSE, distributed with this software.  #
#############################################################################
import os

from tornado import web

from jupyter_server.utils import url_path_join, url_escape

from .utils import get_server_root_dir
from .handler import BaseVoilaHandler


class VoilaTreeHandler(BaseVoilaHandler):

    def initialize(self, **kwargs):
        super().initialize(**kwargs)
        self.allowed_extensions = list(self.voila_configuration.extension_language_mapping.keys()) + ['.ipynb']

    def get_template(self, name):
        """Return the jinja template object for a given name"""
        return self.settings['voila_jinja2_env'].get_template(name)

    def generate_breadcrumbs(self, path):
        breadcrumbs = [(url_path_join(self.base_url, 'voila/tree'), '')]
        parts = path.split('/')
        for i in range(len(parts)):
            if parts[i]:
                link = url_path_join(self.base_url, 'voila/tree',
                                     url_escape(url_path_join(*parts[:i + 1])),
                                     )
                breadcrumbs.append((link, parts[i]))
        return breadcrumbs

    def generate_page_title(self, path):
        parts = path.split('/')
        if len(parts) > 3:  # not too many parts
            parts = parts[-2:]
        page_title = url_path_join(*parts)
        if page_title:
            return page_title + '/'
        else:
            return 'Voilà Home'

    @web.authenticated
    def get(self, path=''):
        cm = self.contents_manager

        if cm.dir_exists(path=path):
            if cm.is_hidden(path) and not cm.allow_hidden:
                self.log.info("Refusing to serve hidden directory, via 404 Error")
                raise web.HTTPError(404)
            breadcrumbs = self.generate_breadcrumbs(path)
            page_title = self.generate_page_title(path)
            contents = cm.get(path)

            def allowed_content(content):
                if content['type'] in ['directory', 'notebook']:
                    return True
                __, ext = os.path.splitext(content.get('path'))
                return ext in self.allowed_extensions

            contents['content'] = sorted(contents['content'], key=lambda i: i['name'])
            contents['content'] = filter(allowed_content, contents['content'])

            self.write(self.render_template(
                'tree.html',
                page_title=page_title,
                notebook_path=path,
                breadcrumbs=breadcrumbs,
                contents=contents,
                terminals_available=False,
                server_root=get_server_root_dir(self.settings),
                query=self.request.query,
            ))
        elif cm.file_exists(path):
            # it's not a directory, we have redirecting to do
            model = cm.get(path, content=False)
            # redirect to /api/notebooks if it's a notebook, otherwise /api/files
            service = 'notebooks' if model['type'] == 'notebook' else 'files'
            url = url_path_join(
                self.base_url, service, url_escape(path),
            )
            self.log.debug("Redirecting %s to %s", self.request.path, url)
            self.redirect(url)
        else:
            raise web.HTTPError(404)
