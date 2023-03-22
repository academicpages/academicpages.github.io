"""Tornado handler for bundling notebooks."""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

import asyncio
import inspect
import concurrent.futures

from nbclassic import nbclassic_path

from traitlets.utils.importstring import import_item
from tornado import web, gen

from jupyter_server.utils import url2path
from jupyter_server.base.handlers import JupyterHandler
from jupyter_server.services.config import ConfigManager

from . import tools


def maybe_future(obj):
    """Like tornado's deprecated gen.maybe_future

    but more compatible with asyncio for recent versions
    of tornado
    """
    if inspect.isawaitable(obj):
        return asyncio.ensure_future(obj)
    elif isinstance(obj, concurrent.futures.Future):
        return asyncio.wrap_future(obj)
    else:
        # not awaitable, wrap scalar in future
        f = asyncio.Future()
        f.set_result(obj)
        return f


class BundlerHandler(JupyterHandler):
    def initialize(self):
        """Make tools module available on the handler instance for compatibility
        with existing bundler API and ease of reference."""
        self.tools = tools
    
    def get_bundler(self, bundler_id):
        """
        Get bundler metadata from config given a bundler ID.
        
        Parameters
        ----------
        bundler_id: str
            Unique bundler ID within the notebook/bundlerextensions config section
        
        Returns
        -------
        dict
            Bundler metadata with label, group, and module_name attributes
        
        
        Raises
        ------
        KeyError
            If the bundler ID is unknown
        """
        cm = ConfigManager()
        return cm.get('notebook').get('bundlerextensions', {})[bundler_id]

    @web.authenticated
    @gen.coroutine
    def get(self, path):
        """Bundle the given nbclassic.
        
        Parameters
        ----------
        path: str
            Path to the notebook (path parameter)
        bundler: str
            Bundler ID to use (query parameter)
        """
        bundler_id = self.get_query_argument('bundler')
        model = self.contents_manager.get(path=url2path(path))

        try:
            bundler = self.get_bundler(bundler_id)
        except KeyError as e:
            raise web.HTTPError(400, 'Bundler %s not enabled' %
                                bundler_id) from e

        module_name = bundler['module_name']
        try:
            # no-op in python3, decode error in python2
            module_name = str(module_name)
        except UnicodeEncodeError:
            # Encode unicode as utf-8 in python2 else import_item fails
            module_name = module_name.encode('utf-8')
        
        try:
            bundler_mod = import_item(module_name)
        except ImportError as e:
            raise web.HTTPError(500, 'Could not import bundler %s ' %
                                bundler_id) from e

        # Let the bundler respond in any way it sees fit and assume it will
        # finish the request
        yield maybe_future(bundler_mod.bundle(self, model))


default_handlers = [
    (r"%s/bundle/(.*)" % nbclassic_path(), BundlerHandler)
]
