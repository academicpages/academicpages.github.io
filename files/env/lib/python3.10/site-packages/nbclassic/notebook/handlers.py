"""Tornado handlers for the live notebook view.

This is a fork from jupyter/notebook#6.x
"""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

from collections import namedtuple

from tornado import web, gen

from jupyter_server.transutils import _i18n
from jupyter_server.utils import (
    ensure_async
)
from jupyter_server.base.handlers import path_regex, FilesRedirectHandler
from jupyter_server.extension.handler import (
    ExtensionHandlerMixin,
    ExtensionHandlerJinjaMixin
)
from jupyter_server.base.handlers import JupyterHandler
HTTPError = web.HTTPError

from nbclassic import nbclassic_path


def get_frontend_exporters():
    from nbconvert.exporters.base import get_export_names, get_exporter

    # name=exporter_name, display=export_from_notebook+extension
    ExporterInfo = namedtuple('ExporterInfo', ['name', 'display'])

    default_exporters = [
        ExporterInfo(name='html', display='HTML (.html)'),
        ExporterInfo(name='latex', display='LaTeX (.tex)'),
        ExporterInfo(name='markdown', display='Markdown (.md)'),
        ExporterInfo(name='notebook', display='Notebook (.ipynb)'),
        ExporterInfo(name='pdf', display='PDF via LaTeX (.pdf)'),
        ExporterInfo(name='rst', display='reST (.rst)'),
        ExporterInfo(name='script', display='Script (.txt)'),
        ExporterInfo(name='slides', display='Reveal.js slides (.slides.html)')
    ]

    frontend_exporters = []
    for name in get_export_names():
        exporter_class = get_exporter(name)
        exporter_instance = exporter_class()
        ux_name = getattr(exporter_instance, 'export_from_notebook', None)
        super_uxname = getattr(super(exporter_class, exporter_instance),
                               'export_from_notebook', None)

        # Ensure export_from_notebook is explicitly defined & not inherited
        if ux_name is not None and ux_name != super_uxname:
            display = _i18n('{} ({})'.format(ux_name,
                                             exporter_instance.file_extension))
            frontend_exporters.append(ExporterInfo(name, display))

    # Ensure default_exporters are in frontend_exporters if not already
    # This protects against nbconvert versions lower than 5.5
    names = set(exporter.name.lower() for exporter in frontend_exporters)
    for exporter in default_exporters:
        if exporter.name not in names:
            frontend_exporters.append(exporter)

    # Protect against nbconvert 5.5.0
    python_exporter = ExporterInfo(name='python', display='python (.py)')
    if python_exporter in frontend_exporters:
        frontend_exporters.remove(python_exporter)

    # Protect against nbconvert 5.4.x
    template_exporter = ExporterInfo(name='custom', display='custom (.txt)')
    if template_exporter in frontend_exporters:
        frontend_exporters.remove(template_exporter)
    return sorted(frontend_exporters)


class NotebookHandler(ExtensionHandlerJinjaMixin, ExtensionHandlerMixin, JupyterHandler):

    @web.authenticated
    @gen.coroutine
    def get(self, path):
        """get renders the notebook template if a name is given, or
        redirects to the '/files/' handler if the name is not given."""
        path = path.strip('/')
        cm = self.contents_manager

        # will raise 404 on not found
        try:
            model = yield ensure_async(cm.get(path, content=False))
        except web.HTTPError as e:
            if e.status_code == 404 and 'files' in path.split('/'):
                # 404, but '/files/' in URL, let FilesRedirect take care of it
                yield FilesRedirectHandler.redirect_to_files(self, path)
            else:
                raise
        if model['type'] != 'notebook':
            # not a notebook, redirect to files
            yield FilesRedirectHandler.redirect_to_files(self, path)
        name = path.rsplit('/', 1)[-1]
        self.write(self.render_template('notebook.html',
                                        notebook_path=path,
                                        notebook_name=name,
                                        kill_kernel=False,
                                        mathjax_url=self.mathjax_url,
                                        mathjax_config=self.mathjax_config,
                                        get_frontend_exporters=get_frontend_exporters
                                        )
                   )

# -----------------------------------------------------------------------------
# URL to handler mappings
# -----------------------------------------------------------------------------


default_handlers = [
    (r"{}/notebooks{}".format(nbclassic_path(), path_regex), NotebookHandler),
]
