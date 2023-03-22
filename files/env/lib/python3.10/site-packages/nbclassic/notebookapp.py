# coding: utf-8
"""A tornado based Jupyter notebook server."""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

from __future__ import absolute_import, print_function

import os
import gettext
import warnings

from tornado.web import RedirectHandler

import nbclassic
from nbclassic import (
    DEFAULT_STATIC_FILES_PATH,
    DEFAULT_TEMPLATE_PATH_LIST,
    nbclassic_path
)

from nbclassic._version import __version__

from traitlets import (
    Unicode, List, Bool, default
)
from jupyter_core.paths import jupyter_path

import jupyter_server
from jupyter_server.base.handlers import FileFindHandler
from jupyter_server.utils import url_path_join

# Try to load Notebook as an extension of the Jupyter Server
from jupyter_server.extension.application import (
    ExtensionApp,
    ExtensionAppJinjaMixin
)

from jupyter_server.transutils import _i18n
from jupyter_server.serverapp import (
    load_handlers
)

from .terminal.handlers import TerminalHandler
from notebook_shim.shim import NotebookConfigShimMixin
from notebook_shim.traits import NotebookAppTraits

# -----------------------------------------------------------------------------
# Module globals
# -----------------------------------------------------------------------------

_examples = """
jupyter nbclassic                       # start the notebook
jupyter nbclassic --certfile=mycert.pem # use SSL/TLS certificate
jupyter nbclassic password              # enter a password to protect the server
"""

# -----------------------------------------------------------------------------
# Aliases and Flags
# -----------------------------------------------------------------------------

flags = {}
aliases = {}
flags['no-browser'] = (
    {'ServerApp': {'open_browser': False}},
    _i18n("Don't open the notebook in a browser after startup.")
)
flags['no-mathjax'] = (
    {'NotebookApp': {'enable_mathjax': False}},
    """Disable MathJax

    MathJax is the javascript library Jupyter uses to render math/LaTeX. It is
    very large, so you may want to disable it if you have a slow internet
    connection, or for offline use of the notebook.

    When disabled, equations etc. will appear as their untransformed TeX source.
    """
)

flags['allow-root'] = (
    {'ServerApp': {'allow_root': True}},
    _i18n("Allow the notebook to be run from root user.")
)

aliases.update({
    'ip': 'ServerApp.ip',
    'port': 'ServerApp.port',
    'port-retries': 'ServerApp.port_retries',
    # 'transport': 'KernelManager.transport',
    'keyfile': 'ServerApp.keyfile',
    'certfile': 'ServerApp.certfile',
    'client-ca': 'ServerApp.client_ca',
    'notebook-dir': 'ServerApp.notebook_dir',
    'browser': 'ServerApp.browser',
    # 'gateway-url': 'GatewayClient.url',
})

# -----------------------------------------------------------------------------
# NotebookApp
# -----------------------------------------------------------------------------


class NotebookApp(
    NotebookConfigShimMixin,
    ExtensionAppJinjaMixin,
    ExtensionApp,
    NotebookAppTraits,
):

    name = "nbclassic"
    version = __version__
    description = _i18n("""The Jupyter HTML Notebook.

    This launches a Tornado based HTML Notebook Server that serves up an HTML5/Javascript Notebook client.""")

    aliases = aliases
    flags = flags
    extension_url = "/tree"
    subcommands = {}

    default_url = Unicode("%s/tree" % nbclassic_path()).tag(config=True)

    # Override the default open_Browser trait in ExtensionApp,
    # setting it to True.
    open_browser = Bool(
        True,
        help="""Whether to open in a browser after starting.
        The specific browser used is platform dependent and
        determined by the python standard library `webbrowser`
        module, unless it is overridden using the --browser
        (ServerApp.browser) configuration option.
        """
    ).tag(config=True)

    # Load configuration from classic notebook config file
    # for backwards compatibility
    config_file_name = Unicode(
        "jupyter_notebook_config",
        config=True,
        help="Specify a config file to load."
    )

    static_custom_path = List(Unicode(),
                              help=_i18n(
                                  """Path to search for custom.js, css""")
                              )

    @default('static_custom_path')
    def _default_static_custom_path(self):
        return [
            os.path.join(d, 'custom') for d in (
                self.config_dir,
                DEFAULT_STATIC_FILES_PATH)
        ]

    @property
    def template_file_path(self):
        """return extra paths + the default locations"""
        return self.extra_template_paths + DEFAULT_TEMPLATE_PATH_LIST

    extra_nbextensions_path = List(Unicode(), config=True,
                                   help=_i18n(
                                       """extra paths to look for Javascript notebook extensions""")
                                   )

    @property
    def nbextensions_path(self):
        """The path to look for Javascript notebook extensions"""
        path = self.extra_nbextensions_path + jupyter_path('nbextensions')
        return path

    # Local path to static files directory.
    static_paths = [DEFAULT_STATIC_FILES_PATH]

    # Local path to templates directory.
    template_paths = DEFAULT_TEMPLATE_PATH_LIST

    @property
    def static_paths(self):
        """Rename trait in jupyter_server."""
        return [DEFAULT_STATIC_FILES_PATH]

    @property
    def template_paths(self):
        """Rename trait for Jupyter Server."""
        return DEFAULT_TEMPLATE_PATH_LIST

    def _prepare_templates(self):
        super(NotebookApp, self)._prepare_templates()

        # Get translations from notebook package.
        base_dir = os.path.dirname(nbclassic.__file__)

        nbui = gettext.translation('nbui', localedir=os.path.join(
            base_dir, 'nbclassic/i18n'), fallback=True)
        self.jinja2_env.install_gettext_translations(nbui, newstyle=False)
        self.jinja2_env.globals.update(nbclassic_path=nbclassic_path)
        self.jinja2_env.globals.update(nbclassic_tree=url_path_join(self.serverapp.base_url, nbclassic_path(), "tree"))

    def _link_jupyter_server_extension(self, serverapp):
        # Monkey-patch Jupyter Server's and nbclassic's static path list to include
        # the classic notebooks static folder.

        def static_file_path_jupyter_server(self):
            """return extra paths + the default location"""
            return self.extra_static_paths + [jupyter_server.DEFAULT_STATIC_FILES_PATH, nbclassic.DEFAULT_STATIC_FILES_PATH]

        serverapp.__class__.static_file_path = property(
            static_file_path_jupyter_server)

        def static_file_path_nbclassic(self):
            """return extra paths + the default location"""
            # NBExtensions look for classic notebook static files under the `/static/notebook/...`
            # URL. Unfortunately, this conflicts with nbclassic's new static endpoints which are
            # prefixed with `/static/notebooks`, and therefore, serves these files under
            # `/static/notebook/notebooks/...`. This monkey-patch places a new file-finder path
            # to nbclassic's static file handlers that drops the extra "notebook".
            return self.extra_static_paths + \
                [os.path.join(nbclassic.DEFAULT_STATIC_FILES_PATH,
                            "notebook"), nbclassic.DEFAULT_STATIC_FILES_PATH]

        self.__class__.static_file_path = property(static_file_path_nbclassic)
        return super()._link_jupyter_server_extension(serverapp)


    def initialize_settings(self):
        """Add settings to the tornado app."""
        if self.ignore_minified_js:
            self.log.warning(
                _i18n("""The `ignore_minified_js` flag is deprecated and no longer works."""))
            self.log.warning(_i18n(
                """Alternatively use `%s` when working on the notebook's Javascript and LESS""") % 'npm run build:watch')
            warnings.warn(_i18n(
                "The `ignore_minified_js` flag is deprecated and will be removed in Notebook 6.0"), DeprecationWarning)

        settings = dict(
            static_custom_path=self.static_custom_path,
            static_handler_args={
                # don't cache custom.js
                'no_cache_paths': [
                    url_path_join(
                        self.serverapp.base_url,
                        'static',
                        self.name,
                        'custom'
                    )
                ],
            },
            ignore_minified_js=self.ignore_minified_js,
            mathjax_url=self.mathjax_url,
            mathjax_config=self.mathjax_config,
            nbextensions_path=self.nbextensions_path,
        )
        self.settings.update(**settings)


    def initialize_handlers(self):
        """Load the (URL pattern, handler) tuples for each component."""
        # Tornado adds two types of "Routers" to the web application, 1) the
        # "wildcard" router (for all original handlers given to the __init__ method)
        # and 2) the "default" router (for all handlers passed to the add_handlers
        # method). The default router is called before the wildcard router.
        # This is what allows the extension handlers to be matched before
        # the main app handlers.

        # Default routes
        # Order matters. The first handler to match the URL will handle the request.
        handlers = []
        # Add a redirect from /notebooks to /files
        # for opening non-ipynb files in edit mode.
        handlers.append(
            (
                rf"/{self.file_url_prefix}/((?!.*\.ipynb($|\?)).*)",
                RedirectHandler,
                {"url": self.serverapp.base_url+"files/{0}"}
            )
        )
        # Add a redirect from /nbclassic to /nbclassic/tree
        # if both notebook>=7 and nbclassic are installed.
        if len(nbclassic_path()) > 0:
            handlers.append(
                (
                    rf"/nbclassic",
                    RedirectHandler,
                    {"url": self.serverapp.base_url+"nbclassic/tree"}
                )
            )

        # load extra services specified by users before default handlers
        for service in self.settings['extra_services']:
            handlers.extend(load_handlers(service))

        handlers.extend(load_handlers('nbclassic.tree.handlers'))
        handlers.extend(load_handlers('nbclassic.notebook.handlers'))
        handlers.extend(load_handlers('nbclassic.edit.handlers'))
        self.handlers.extend(handlers)

        # Wildcard routes
        # These routes *must* be called after all extensions. To mimic
        # the classic notebook server as close as possible, these routes
        # need to tbe injected into the wildcard routes.
        static_handlers = []

        base_url = self.serverapp.base_url
        ujoin = url_path_join
        # Add terminal handlers
        static_handlers.append(
            (ujoin(base_url, r"/terminals/(\w+)"), TerminalHandler, {"name": self.name})
        )
        static_handlers.append(
            # (r"/nbextensions/(?!nbextensions_configurator\/list)(.*)", FileFindHandler, {
            (ujoin(base_url, r"/nbextensions/(.*)"), FileFindHandler, {
                'path': self.settings['nbextensions_path'],
                # don't cache anything in nbextensions
                'no_cache_paths': ['/'],
            }),
        )
        static_handlers.append(
            (ujoin(base_url, r"/custom/(.*)"), FileFindHandler, {
                'path': self.settings['static_custom_path'],
                # don't cache anything in nbextensions
                'no_cache_paths': ['/'],
            }),
        )
        # Add these static handlers after the Notebook base handlers
        # to match the original order of handlers in the classic
        # notebook codebase.
        base_handlers = load_handlers('jupyter_server.base.handlers')
        # The extra two handlers (+2) cover the redirect handler
        # and the final 404 handler.
        n = len(base_handlers) + 2
        # Inject the handlers in the tornado router.
        router = self.serverapp.web_app.wildcard_router
        core_rules = router.rules[:-n]
        final_rules = router.rules[-n:]
        router.rules = []
        router.add_rules(core_rules)
        router.add_rules(static_handlers)
        router.add_rules(final_rules)

# -----------------------------------------------------------------------------
# Main entry point
# -----------------------------------------------------------------------------


main = launch_new_instance = NotebookApp.launch_instance
