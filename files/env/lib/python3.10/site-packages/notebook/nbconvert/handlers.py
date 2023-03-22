"""Tornado handlers for nbconvert."""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

import io
import os
import zipfile

from tornado import gen, web, escape
from tornado.log import app_log

from ..base.handlers import (
    IPythonHandler, FilesRedirectHandler,
    path_regex,
)
from ..utils import maybe_future
from nbformat import from_dict

from ipython_genutils.py3compat import cast_bytes
from ipython_genutils import text

def find_resource_files(output_files_dir):
    files = []
    for dirpath, dirnames, filenames in os.walk(output_files_dir):
        files.extend([os.path.join(dirpath, f) for f in filenames])
    return files

def respond_zip(handler, name, output, resources):
    """Zip up the output and resource files and respond with the zip file.

    Returns True if it has served a zip file, False if there are no resource
    files, in which case we serve the plain output file.
    """
    # Check if we have resource files we need to zip
    output_files = resources.get('outputs', None)
    if not output_files:
        return False

    # Headers
    zip_filename = os.path.splitext(name)[0] + '.zip'
    handler.set_attachment_header(zip_filename)
    handler.set_header('Content-Type', 'application/zip')
    handler.set_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')

    # Prepare the zip file
    buffer = io.BytesIO()
    zipf = zipfile.ZipFile(buffer, mode='w', compression=zipfile.ZIP_DEFLATED)
    output_filename = os.path.splitext(name)[0] + resources['output_extension']
    zipf.writestr(output_filename, cast_bytes(output, 'utf-8'))
    for filename, data in output_files.items():
        zipf.writestr(os.path.basename(filename), data)
    zipf.close()

    handler.finish(buffer.getvalue())
    return True

def get_exporter(format, **kwargs):
    """get an exporter, raising appropriate errors"""
    # if this fails, will raise 500
    try:
        from nbconvert.exporters.base import get_exporter
    except ImportError as e:
        raise web.HTTPError(500, f"Could not import nbconvert: {e}") from e

    try:
        Exporter = get_exporter(format)
    except KeyError as e:
        # should this be 400?
        raise web.HTTPError(404, f"No exporter for format: {format}") from e

    try:
        return Exporter(**kwargs)
    except Exception as e:
        app_log.exception("Could not construct Exporter: %s", Exporter)
        raise web.HTTPError(500, f"Could not construct Exporter: {e}") from e

class NbconvertFileHandler(IPythonHandler):

    SUPPORTED_METHODS = ('GET',)

    @property
    def content_security_policy(self):
        # In case we're serving HTML/SVG, confine any Javascript to a unique
        # origin so it can't interact with the notebook server.
        return super().content_security_policy + "; sandbox allow-scripts"

    @web.authenticated
    @gen.coroutine
    def get(self, format, path):

        exporter = get_exporter(format, config=self.config, log=self.log)

        path = path.strip('/')
        # If the notebook relates to a real file (default contents manager),
        # give its path to nbconvert.
        if hasattr(self.contents_manager, '_get_os_path'):
            os_path = self.contents_manager._get_os_path(path)
            ext_resources_dir, basename = os.path.split(os_path)
        else:
            ext_resources_dir = None

        model = yield maybe_future(self.contents_manager.get(path=path))
        name = model['name']
        if model['type'] != 'notebook':
            # not a notebook, redirect to files
            return FilesRedirectHandler.redirect_to_files(self, path)

        nb = model['content']

        self.set_header('Last-Modified', model['last_modified'])

        # create resources dictionary
        mod_date = model['last_modified'].strftime(text.date_format)
        nb_title = os.path.splitext(name)[0]

        resource_dict = {
            "metadata": {
                "name": nb_title,
                "modified_date": mod_date
            },
            "config_dir": self.application.settings['config_dir']
        }

        if ext_resources_dir:
            resource_dict['metadata']['path'] = ext_resources_dir

        try:
            output, resources = exporter.from_notebook_node(
                nb,
                resources=resource_dict
            )
        except Exception as e:
            self.log.exception("nbconvert failed: %s", e)
            raise web.HTTPError(500, f"nbconvert failed: {e}") from e

        if respond_zip(self, name, output, resources):
            return

        # Force download if requested
        if self.get_argument('download', 'false').lower() == 'true':
            filename = os.path.splitext(name)[0] + resources['output_extension']
            self.set_attachment_header(filename)

        # MIME type
        if exporter.output_mimetype:
            self.set_header('Content-Type',
                            f'{exporter.output_mimetype}; charset=utf-8')

        self.set_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.finish(output)

class NbconvertPostHandler(IPythonHandler):
    SUPPORTED_METHODS = ('POST',)

    @property
    def content_security_policy(self):
        # In case we're serving HTML/SVG, confine any Javascript to a unique
        # origin so it can't interact with the notebook server.
        return super().content_security_policy + "; sandbox allow-scripts"

    @web.authenticated
    def post(self, format):
        exporter = get_exporter(format, config=self.config)

        model = self.get_json_body()
        name = model.get('name', 'notebook.ipynb')
        nbnode = from_dict(model['content'])

        try:
            output, resources = exporter.from_notebook_node(nbnode, resources={
                "metadata": {"name": name[:name.rfind('.')],},
                "config_dir": self.application.settings['config_dir'],
            })
        except Exception as e:
            raise web.HTTPError(500, f"nbconvert failed: {e}") from e

        if respond_zip(self, name, output, resources):
            return

        # MIME type
        if exporter.output_mimetype:
            self.set_header('Content-Type',
                            f'{exporter.output_mimetype}; charset=utf-8')

        self.finish(output)


#-----------------------------------------------------------------------------
# URL to handler mappings
#-----------------------------------------------------------------------------

_format_regex = r"(?P<format>\w+)"


default_handlers = [
    (fr"/nbconvert/{_format_regex}", NbconvertPostHandler),
    (fr"/nbconvert/{_format_regex}{path_regex}", NbconvertFileHandler),
]
