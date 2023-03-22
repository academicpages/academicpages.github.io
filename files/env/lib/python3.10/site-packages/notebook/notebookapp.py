"""A tornado based Jupyter notebook server."""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

import notebook
import asyncio
import binascii
import datetime
import errno
import functools
import gettext
import hashlib
import hmac
import importlib
import inspect
import ipaddress
import json
import logging
import mimetypes
import os
import random
import re
import select
import signal
import socket
import stat
import sys
import tempfile
import threading
import time
import warnings
import webbrowser

try:
    import resource
except ImportError:
    # Windows
    resource = None

from base64 import encodebytes

from jinja2 import Environment, FileSystemLoader

from notebook.transutils import trans, _

# check for tornado 3.1.0
try:
    import tornado
except ImportError as e:
    raise ImportError(_("The Jupyter Notebook requires tornado >= 5.0")) from e
try:
    version_info = tornado.version_info
except AttributeError as e:
    raise ImportError(_("The Jupyter Notebook requires tornado >= 5.0, but you have < 1.1.0")) from e
if version_info < (5,0):
    raise ImportError(_("The Jupyter Notebook requires tornado >= 5.0, but you have %s") % tornado.version)

from tornado import httpserver
from tornado import ioloop
from tornado import web
from tornado.httputil import url_concat
from tornado.log import LogFormatter, app_log, access_log, gen_log
if not sys.platform.startswith('win'):
    from tornado.netutil import bind_unix_socket

from notebook import (
    DEFAULT_NOTEBOOK_PORT,
    DEFAULT_TEMPLATE_PATH_LIST,
    __version__,
)
import nbclassic
# Packagers: modify this line if you store the notebook static files elsewhere
DEFAULT_STATIC_FILES_PATH = os.path.join(os.path.dirname(nbclassic.__file__), "static")

from .base.handlers import Template404, RedirectWithParams
from .log import log_request
from .services.kernels.kernelmanager import MappingKernelManager, AsyncMappingKernelManager
from .services.config import ConfigManager
from .services.contents.manager import ContentsManager
from .services.contents.filemanager import FileContentsManager
from .services.contents.largefilemanager import LargeFileManager
from .services.sessions.sessionmanager import SessionManager
from .gateway.managers import GatewayKernelManager, GatewayKernelSpecManager, GatewaySessionManager, GatewayClient

from .auth.login import LoginHandler
from .auth.logout import LogoutHandler
from .base.handlers import FileFindHandler

from traitlets.config import Config
from traitlets.config.application import catch_config_error, boolean_flag
from jupyter_core.application import (
    JupyterApp, base_flags, base_aliases,
)
from jupyter_core.paths import jupyter_config_path
from jupyter_client import KernelManager
from jupyter_client.kernelspec import KernelSpecManager
from jupyter_client.session import Session
from nbformat.sign import NotebookNotary
from traitlets import (
    Any, Dict, Unicode, Integer, List, Bool, Bytes, Instance,
    TraitError, Type, Float, observe, default, validate
)
from ipython_genutils import py3compat
from jupyter_core.paths import jupyter_runtime_dir, jupyter_path
from notebook._sysinfo import get_sys_info

from ._tz import utcnow, utcfromtimestamp
from .utils import (
    check_pid,
    pathname2url,
    run_sync,
    unix_socket_in_use,
    url_escape,
    url_path_join,
    urldecode_unix_socket_path,
    urlencode_unix_socket,
    urljoin,
)
from .traittypes import TypeFromClasses

# Check if we can use async kernel management
try:
    from jupyter_client import AsyncMultiKernelManager
    async_kernel_mgmt_available = True
except ImportError:
    async_kernel_mgmt_available = False

# Tolerate missing terminado package.
try:
    from .terminal import TerminalManager
    terminado_available = True
except ImportError:
    terminado_available = False

#-----------------------------------------------------------------------------
# Module globals
#-----------------------------------------------------------------------------

_examples = """
jupyter notebook                       # start the notebook
jupyter notebook --certfile=mycert.pem # use SSL/TLS certificate
jupyter notebook password              # enter a password to protect the server
"""

#-----------------------------------------------------------------------------
# Helper functions
#-----------------------------------------------------------------------------

def random_ports(port, n):
    """Generate a list of n random ports near the given port.

    The first 5 ports will be sequential, and the remaining n-5 will be
    randomly selected in the range [port-2*n, port+2*n].
    """
    for i in range(min(5, n)):
        yield port + i
    for i in range(n-5):
        yield max(1, port + random.randint(-2*n, 2*n))

def load_handlers(name):
    """Load the (URL pattern, handler) tuples for each component."""
    mod = __import__(name, fromlist=['default_handlers'])
    return mod.default_handlers

#-----------------------------------------------------------------------------
# The Tornado web application
#-----------------------------------------------------------------------------


class NotebookWebApplication(web.Application):

    def __init__(self, jupyter_app, kernel_manager, contents_manager,
                 session_manager, kernel_spec_manager,
                 config_manager, extra_services, log,
                 base_url, default_url, settings_overrides, jinja_env_options):

        settings = self.init_settings(
            jupyter_app, kernel_manager, contents_manager,
            session_manager, kernel_spec_manager, config_manager,
            extra_services, log, base_url,
            default_url, settings_overrides, jinja_env_options)
        handlers = self.init_handlers(settings)

        if settings['autoreload']:
            log.info('Autoreload enabled: the webapp will restart when any Python src file changes.')

        super().__init__(handlers, **settings)

    def init_settings(self, jupyter_app, kernel_manager, contents_manager,
                      session_manager, kernel_spec_manager,
                      config_manager, extra_services,
                      log, base_url, default_url, settings_overrides,
                      jinja_env_options=None):

        _template_path = settings_overrides.get(
            "template_path",
            jupyter_app.template_file_path,
        )
        if isinstance(_template_path, py3compat.string_types):
            _template_path = (_template_path,)
        template_path = [os.path.expanduser(path) for path in _template_path]

        jenv_opt = {"autoescape": True}
        jenv_opt.update(jinja_env_options if jinja_env_options else {})

        env = Environment(loader=FileSystemLoader(template_path), extensions=['jinja2.ext.i18n'], **jenv_opt)
        sys_info = get_sys_info()

        # If the user is running the notebook in a git directory, make the assumption
        # that this is a dev install and suggest to the developer `npm run build:watch`.
        base_dir = os.path.realpath(os.path.join(__file__, '..', '..'))
        dev_mode = os.path.exists(os.path.join(base_dir, '.git'))

        nbui = gettext.translation('nbui', localedir=os.path.join(base_dir, 'notebook/i18n'), fallback=True)
        env.install_gettext_translations(nbui, newstyle=False)

        if dev_mode:
            DEV_NOTE_NPM = f"""It looks like you're running the notebook from source.
    If you're working on the Javascript of the notebook, try running

    {'npm run build:watch'}

    in another terminal window to have the system incrementally
    watch and build the notebook's JavaScript for you, as you make changes."""
            log.info(DEV_NOTE_NPM)

        if sys_info['commit_source'] == 'repository':
            # don't cache (rely on 304) when working from master
            version_hash = ''
        else:
            # reset the cache on server restart
            version_hash = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

        if jupyter_app.ignore_minified_js:
            log.warning(_("""The `ignore_minified_js` flag is deprecated and no longer works."""))
            log.warning(_("""Alternatively use `%s` when working on the notebook's Javascript and LESS""") % 'npm run build:watch')
            warnings.warn(_("The `ignore_minified_js` flag is deprecated and will be removed in Notebook 6.0"), DeprecationWarning)

        now = utcnow()

        root_dir = contents_manager.root_dir
        home = py3compat.str_to_unicode(os.path.expanduser('~'), encoding=sys.getfilesystemencoding())
        if root_dir.startswith(home + os.path.sep):
            # collapse $HOME to ~
            root_dir = '~' + root_dir[len(home):]

        # Use the NotebookApp logger and its formatting for tornado request logging.
        log_function = functools.partial(
            log_request, log=log, log_json=jupyter_app.log_json)
        settings = dict(
            # basics
            log_function=log_function,
            base_url=base_url,
            default_url=default_url,
            template_path=template_path,
            static_path=jupyter_app.static_file_path,
            static_custom_path=jupyter_app.static_custom_path,
            static_handler_class = FileFindHandler,
            static_url_prefix = url_path_join(base_url,'/static/'),
            static_handler_args = {
                # don't cache custom.js
                'no_cache_paths': [url_path_join(base_url, 'static', 'custom')],
            },
            version_hash=version_hash,
            ignore_minified_js=jupyter_app.ignore_minified_js,

            # rate limits
            iopub_msg_rate_limit=jupyter_app.iopub_msg_rate_limit,
            iopub_data_rate_limit=jupyter_app.iopub_data_rate_limit,
            rate_limit_window=jupyter_app.rate_limit_window,

            # authentication
            cookie_secret=jupyter_app.cookie_secret,
            login_url=url_path_join(base_url,'/login'),
            login_handler_class=jupyter_app.login_handler_class,
            logout_handler_class=jupyter_app.logout_handler_class,
            password=jupyter_app.password,
            xsrf_cookies=True,
            disable_check_xsrf=jupyter_app.disable_check_xsrf,
            allow_remote_access=jupyter_app.allow_remote_access,
            local_hostnames=jupyter_app.local_hostnames,
            authenticate_prometheus=jupyter_app.authenticate_prometheus,

            # managers
            kernel_manager=kernel_manager,
            contents_manager=contents_manager,
            session_manager=session_manager,
            kernel_spec_manager=kernel_spec_manager,
            config_manager=config_manager,

            # handlers
            extra_services=extra_services,

            # Jupyter stuff
            started=now,
            # place for extensions to register activity
            # so that they can prevent idle-shutdown
            last_activity_times={},
            jinja_template_vars=jupyter_app.jinja_template_vars,
            nbextensions_path=jupyter_app.nbextensions_path,
            websocket_url=jupyter_app.websocket_url,
            mathjax_url=jupyter_app.mathjax_url,
            mathjax_config=jupyter_app.mathjax_config,
            shutdown_button=jupyter_app.quit_button,
            config=jupyter_app.config,
            config_dir=jupyter_app.config_dir,
            allow_password_change=jupyter_app.allow_password_change,
            server_root_dir=root_dir,
            jinja2_env=env,
            terminals_available=terminado_available and jupyter_app.terminals_enabled,
        )

        # allow custom overrides for the tornado web app.
        settings.update(settings_overrides)
        return settings

    def init_handlers(self, settings):
        """Load the (URL pattern, handler) tuples for each component."""

        # Order matters. The first handler to match the URL will handle the request.
        handlers = []
        # load extra services specified by users before default handlers
        for service in settings['extra_services']:
            handlers.extend(load_handlers(service))
        handlers.extend(load_handlers('notebook.tree.handlers'))
        handlers.extend([(r"/login", settings['login_handler_class'])])
        handlers.extend([(r"/logout", settings['logout_handler_class'])])
        handlers.extend(load_handlers('notebook.files.handlers'))
        handlers.extend(load_handlers('notebook.view.handlers'))
        handlers.extend(load_handlers('notebook.notebook.handlers'))
        handlers.extend(load_handlers('notebook.nbconvert.handlers'))
        handlers.extend(load_handlers('notebook.bundler.handlers'))
        handlers.extend(load_handlers('notebook.kernelspecs.handlers'))
        handlers.extend(load_handlers('notebook.edit.handlers'))
        handlers.extend(load_handlers('notebook.services.api.handlers'))
        handlers.extend(load_handlers('notebook.services.config.handlers'))
        handlers.extend(load_handlers('notebook.services.contents.handlers'))
        handlers.extend(load_handlers('notebook.services.sessions.handlers'))
        handlers.extend(load_handlers('notebook.services.nbconvert.handlers'))
        handlers.extend(load_handlers('notebook.services.security.handlers'))
        handlers.extend(load_handlers('notebook.services.shutdown'))
        handlers.extend(load_handlers('notebook.services.kernels.handlers'))
        handlers.extend(load_handlers('notebook.services.kernelspecs.handlers'))

        handlers.extend(settings['contents_manager'].get_extra_handlers())

        # If gateway mode is enabled, replace appropriate handlers to perform redirection
        if GatewayClient.instance().gateway_enabled:
            # for each handler required for gateway, locate its pattern
            # in the current list and replace that entry...
            gateway_handlers = load_handlers('notebook.gateway.handlers')
            for i, gwh in enumerate(gateway_handlers):
                for j, h in enumerate(handlers):
                    if gwh[0] == h[0]:
                        handlers[j] = (gwh[0], gwh[1])
                        break

        handlers.append(
            (r"/nbextensions/(.*)", FileFindHandler, {
                'path': settings['nbextensions_path'],
                'no_cache_paths': ['/'], # don't cache anything in nbextensions
            }),
        )
        handlers.append(
            (r"/custom/(.*)", FileFindHandler, {
                'path': settings['static_custom_path'],
                'no_cache_paths': ['/'], # don't cache anything in custom
            })
        )
        # register base handlers last
        handlers.extend(load_handlers('notebook.base.handlers'))
        # set the URL that will be redirected from `/`
        handlers.append(
            (r'/?', RedirectWithParams, {
                'url' : settings['default_url'],
                'permanent': False, # want 302, not 301
            })
        )

        # prepend base_url onto the patterns that we match
        new_handlers = []
        for handler in handlers:
            pattern = url_path_join(settings['base_url'], handler[0])
            new_handler = tuple([pattern] + list(handler[1:]))
            new_handlers.append(new_handler)
        # add 404 on the end, which will catch everything that falls through
        new_handlers.append((r'(.*)', Template404))
        return new_handlers

    def last_activity(self):
        """Get a UTC timestamp for when the server last did something.

        Includes: API activity, kernel activity, kernel shutdown, and terminal
        activity.
        """
        sources = [
            self.settings['started'],
            self.settings['kernel_manager'].last_kernel_activity,
        ]
        try:
            sources.append(self.settings['api_last_activity'])
        except KeyError:
            pass
        try:
            sources.append(self.settings['terminal_last_activity'])
        except KeyError:
            pass
        sources.extend(self.settings['last_activity_times'].values())
        return max(sources)


class NotebookPasswordApp(JupyterApp):
    """Set a password for the notebook server.

    Setting a password secures the notebook server
    and removes the need for token-based authentication.
    """

    description = __doc__

    def _config_file_default(self):
        return os.path.join(self.config_dir, 'jupyter_notebook_config.json')

    def start(self):
        from .auth.security import set_password
        set_password(config_file=self.config_file)
        self.log.info(f"Wrote hashed password to {self.config_file}")


def shutdown_server(server_info, timeout=5, log=None):
    """Shutdown a notebook server in a separate process.

    *server_info* should be a dictionary as produced by list_running_servers().

    Will first try to request shutdown using /api/shutdown .
    On Unix, if the server is still running after *timeout* seconds, it will
    send SIGTERM. After another timeout, it escalates to SIGKILL.

    Returns True if the server was stopped by any means, False if stopping it
    failed (on Windows).
    """
    from tornado import gen
    from tornado.httpclient import AsyncHTTPClient, HTTPClient, HTTPRequest
    from tornado.netutil import Resolver
    url = server_info['url']
    pid = server_info['pid']
    resolver = None

    # UNIX Socket handling.
    if url.startswith('http+unix://'):
        # This library doesn't understand our URI form, but it's just HTTP.
        url = url.replace('http+unix://', 'http://')

        class UnixSocketResolver(Resolver):
            def initialize(self, resolver):
                self.resolver = resolver

            def close(self):
                self.resolver.close()

            @gen.coroutine
            def resolve(self, host, port, *args, **kwargs):
                raise gen.Return([
                    (socket.AF_UNIX, urldecode_unix_socket_path(host))
                ])

        resolver = UnixSocketResolver(resolver=Resolver())

    req = HTTPRequest(url + 'api/shutdown', method='POST', body=b'', headers={
        'Authorization': 'token ' + server_info['token']
    })
    if log: log.debug("POST request to %sapi/shutdown", url)
    AsyncHTTPClient.configure(None, resolver=resolver)
    HTTPClient(AsyncHTTPClient).fetch(req)

    # Poll to see if it shut down.
    for _ in range(timeout*10):
        if not check_pid(pid):
            if log: log.debug("Server PID %s is gone", pid)
            return True
        time.sleep(0.1)

    if sys.platform.startswith('win'):
        return False

    if log: log.debug("SIGTERM to PID %s", pid)
    os.kill(pid, signal.SIGTERM)

    # Poll to see if it shut down.
    for _ in range(timeout * 10):
        if not check_pid(pid):
            if log: log.debug("Server PID %s is gone", pid)
            return True
        time.sleep(0.1)

    if log: log.debug("SIGKILL to PID %s", pid)
    os.kill(pid, signal.SIGKILL)
    return True  # SIGKILL cannot be caught


class NbserverStopApp(JupyterApp):
    version = __version__
    description="Stop currently running notebook server."

    port = Integer(DEFAULT_NOTEBOOK_PORT, config=True,
        help=f"Port of the server to be killed. Default {DEFAULT_NOTEBOOK_PORT}")

    sock = Unicode('', config=True,
        help="UNIX socket of the server to be killed.")

    def parse_command_line(self, argv=None):
        super().parse_command_line(argv)
        if self.extra_args:
            try:
                self.port = int(self.extra_args[0])
            except ValueError:
                # self.extra_args[0] was not an int, so it must be a string (unix socket).
                self.sock = self.extra_args[0]

    def shutdown_server(self, server):
        return shutdown_server(server, log=self.log)

    def _shutdown_or_exit(self, target_endpoint, server):
        print(f"Shutting down server on {target_endpoint}...")
        server_stopped = self.shutdown_server(server)
        if not server_stopped and sys.platform.startswith('win'):
            # the pid check on Windows appears to be unreliable, so fetch another
            # list of servers and ensure our server is not in the list before
            # sending the wrong impression.
            servers = list(list_running_servers(self.runtime_dir))
            if server not in servers:
                server_stopped = True
        if not server_stopped:
            sys.exit(f"Could not stop server on {target_endpoint}")

    @staticmethod
    def _maybe_remove_unix_socket(socket_path):
        try:
            os.unlink(socket_path)
        except OSError:
            pass

    def start(self):
        servers = list(list_running_servers(self.runtime_dir))
        if not servers:
            self.exit("There are no running servers (per %s)" % self.runtime_dir)

        for server in servers:
            if self.sock:
                sock = server.get('sock', None)
                if sock and sock == self.sock:
                    self._shutdown_or_exit(sock, server)
                    # Attempt to remove the UNIX socket after stopping.
                    self._maybe_remove_unix_socket(sock)
                    return
            elif self.port:
                port = server.get('port', None)
                if port == self.port:
                    self._shutdown_or_exit(port, server)
                    return
        else:
            current_endpoint = self.sock or self.port
            print(
                f"There is currently no server running on {current_endpoint}",
                file=sys.stderr
            )
            print("Ports/sockets currently in use:", file=sys.stderr)
            for server in servers:
                print("  - {}".format(server.get('sock') or server['port']), file=sys.stderr)
            self.exit(1)


class NbserverListApp(JupyterApp):
    version = __version__
    description=_("List currently running notebook servers.")

    flags = dict(
        jsonlist=({'NbserverListApp': {'jsonlist': True}},
              _("Produce machine-readable JSON list output.")),
        json=({'NbserverListApp': {'json': True}},
              _("Produce machine-readable JSON object on each line of output.")),
    )

    jsonlist = Bool(False, config=True,
          help=_("If True, the output will be a JSON list of objects, one per "
                 "active notebook server, each with the details from the "
                 "relevant server info file."))
    json = Bool(False, config=True,
          help=_("If True, each line of output will be a JSON object with the "
                  "details from the server info file. For a JSON list output, "
                  "see the NbserverListApp.jsonlist configuration value"))

    def start(self):
        serverinfo_list = list(list_running_servers(self.runtime_dir))
        if self.jsonlist:
            print(json.dumps(serverinfo_list, indent=2))
        elif self.json:
            for serverinfo in serverinfo_list:
                print(json.dumps(serverinfo))
        else:
            print("Currently running servers:")
            for serverinfo in serverinfo_list:
                url = serverinfo['url']
                if serverinfo.get('token'):
                    url = url + '?token=%s' % serverinfo['token']
                print(url, "::", serverinfo['notebook_dir'])

#-----------------------------------------------------------------------------
# Aliases and Flags
#-----------------------------------------------------------------------------

flags = dict(base_flags)
flags['no-browser']=(
    {'NotebookApp' : {'open_browser' : False}},
    _("Don't open the notebook in a browser after startup.")
)
flags['pylab']=(
    {'NotebookApp' : {'pylab' : 'warn'}},
    _("DISABLED: use %pylab or %matplotlib in the notebook to enable matplotlib.")
)
flags['no-mathjax']=(
    {'NotebookApp' : {'enable_mathjax' : False}},
    """Disable MathJax

    MathJax is the javascript library Jupyter uses to render math/LaTeX. It is
    very large, so you may want to disable it if you have a slow internet
    connection, or for offline use of the notebook.

    When disabled, equations etc. will appear as their untransformed TeX source.
    """
)

flags['allow-root']=(
    {'NotebookApp' : {'allow_root' : True}},
    _("Allow the notebook to be run from root user.")
)

flags['autoreload'] = (
    {'NotebookApp': {'autoreload': True}},
    """Autoreload the webapp

    Enable reloading of the tornado webapp and all imported Python packages
    when any changes are made to any Python src files in Notebook or
    extensions.
    """
)

# Add notebook manager flags
flags.update(boolean_flag('script', 'FileContentsManager.save_script',
               'DEPRECATED, IGNORED',
               'DEPRECATED, IGNORED'))

aliases = dict(base_aliases)

aliases.update({
    'ip': 'NotebookApp.ip',
    'port': 'NotebookApp.port',
    'port-retries': 'NotebookApp.port_retries',
    'sock': 'NotebookApp.sock',
    'sock-mode': 'NotebookApp.sock_mode',
    'transport': 'KernelManager.transport',
    'keyfile': 'NotebookApp.keyfile',
    'certfile': 'NotebookApp.certfile',
    'client-ca': 'NotebookApp.client_ca',
    'notebook-dir': 'NotebookApp.notebook_dir',
    'browser': 'NotebookApp.browser',
    'pylab': 'NotebookApp.pylab',
    'gateway-url': 'GatewayClient.url',
})

#-----------------------------------------------------------------------------
# NotebookApp
#-----------------------------------------------------------------------------

class NotebookApp(JupyterApp):

    name = 'jupyter-notebook'
    version = __version__
    description = _("""The Jupyter HTML Notebook.

    This launches a Tornado based HTML Notebook Server that serves up an HTML5/Javascript Notebook client.""")
    examples = _examples
    aliases = aliases
    flags = flags

    classes = [
        KernelManager, Session, MappingKernelManager, KernelSpecManager,
        ContentsManager, FileContentsManager, NotebookNotary,
        GatewayKernelManager, GatewayKernelSpecManager, GatewaySessionManager, GatewayClient,
    ]
    if terminado_available:  # Only necessary when terminado is available
        classes.append(TerminalManager)

    flags = Dict(flags)
    aliases = Dict(aliases)

    subcommands = dict(
        list=(NbserverListApp, NbserverListApp.description.splitlines()[0]),
        stop=(NbserverStopApp, NbserverStopApp.description.splitlines()[0]),
        password=(NotebookPasswordApp, NotebookPasswordApp.description.splitlines()[0]),
    )

    _log_formatter_cls = LogFormatter

    _json_logging_import_error_logged = False

    log_json = Bool(False, config=True,
        help=_('Set to True to enable JSON formatted logs. '
               'Run "pip install notebook[json-logging]" to install the '
               'required dependent packages. Can also be set using the '
               'environment variable JUPYTER_ENABLE_JSON_LOGGING=true.')
    )

    @default('log_json')
    def _default_log_json(self):
        """Get the log_json value from the environment."""
        return os.getenv('JUPYTER_ENABLE_JSON_LOGGING', 'false').lower() == 'true'

    @validate('log_json')
    def _validate_log_json(self, proposal):
        # If log_json=True, see if the json_logging package can be imported and
        # override _log_formatter_cls if so.
        value = proposal['value']
        if value:
            try:
                import json_logging
                self.log.debug('initializing json logging')
                json_logging.init_non_web(enable_json=True)
                self._log_formatter_cls = json_logging.JSONLogFormatter
            except ImportError:
                # If configured for json logs and we can't do it, log a hint.
                # Only log the error once though.
                if not self._json_logging_import_error_logged:
                    self.log.warning(
                        'Unable to use json logging due to missing packages. '
                        'Run "pip install notebook[json-logging]" to fix.'
                    )
                    self._json_logging_import_error_logged = True
                value = False
        return value

    @default('log_level')
    def _default_log_level(self):
        return logging.INFO

    @default('log_datefmt')
    def _default_log_datefmt(self):
        """Exclude date from default date format"""
        return "%H:%M:%S"

    @default('log_format')
    def _default_log_format(self):
        """override default log format to include time"""
        return "%(color)s[%(levelname)1.1s %(asctime)s.%(msecs).03d %(name)s]%(end_color)s %(message)s"

    ignore_minified_js = Bool(False,
            config=True,
            help=_('Deprecated: Use minified JS file or not, mainly use during dev to avoid JS recompilation'),
            )

    # file to be opened in the notebook server
    file_to_run = Unicode('', config=True)

    # Network related information

    allow_origin = Unicode('', config=True,
        help="""Set the Access-Control-Allow-Origin header

        Use '*' to allow any origin to access your server.

        Takes precedence over allow_origin_pat.
        """
    )

    allow_origin_pat = Unicode('', config=True,
        help="""Use a regular expression for the Access-Control-Allow-Origin header

        Requests from an origin matching the expression will get replies with:

            Access-Control-Allow-Origin: origin

        where `origin` is the origin of the request.

        Ignored if allow_origin is set.
        """
    )

    allow_credentials = Bool(False, config=True,
        help=_("Set the Access-Control-Allow-Credentials: true header")
    )

    allow_root = Bool(False, config=True,
        help=_("Whether to allow the user to run the notebook as root.")
    )

    use_redirect_file = Bool(True, config=True,
        help="""Disable launching browser by redirect file

        For versions of notebook > 5.7.2, a security feature measure was added that
        prevented the authentication token used to launch the browser from being visible.
        This feature makes it difficult for other users on a multi-user system from
        running code in your Jupyter session as you.

        However, some environments (like Windows Subsystem for Linux (WSL) and Chromebooks),
        launching a browser using a redirect file can lead the browser failing to load.
        This is because of the difference in file structures/paths between the runtime and
        the browser.

        Disabling this setting to False will disable this behavior, allowing the browser
        to launch by using a URL and visible token (as before).
        """
    )

    autoreload = Bool(False, config=True,
        help= ("Reload the webapp when changes are made to any Python src files.")
    )

    default_url = Unicode('/tree', config=True,
        help=_("The default URL to redirect to from `/`")
    )

    ip = Unicode('localhost', config=True,
        help=_("The IP address the notebook server will listen on.")
    )

    @default('ip')
    def _default_ip(self):
        """Return localhost if available, 127.0.0.1 otherwise.

        On some (horribly broken) systems, localhost cannot be bound.
        """
        s = socket.socket()
        try:
            s.bind(('localhost', 0))
        except OSError as e:
            self.log.warning(_("Cannot bind to localhost, using 127.0.0.1 as default ip\n%s"), e)
            return '127.0.0.1'
        else:
            s.close()
            return 'localhost'

    @validate('ip')
    def _validate_ip(self, proposal):
        value = proposal['value']
        if value == '*':
            value = ''
        return value

    custom_display_url = Unicode('', config=True,
        help=_("""Override URL shown to users.

        Replace actual URL, including protocol, address, port and base URL,
        with the given value when displaying URL to the users. Do not change
        the actual connection URL. If authentication token is enabled, the
        token is added to the custom URL automatically.

        This option is intended to be used when the URL to display to the user
        cannot be determined reliably by the Jupyter notebook server (proxified
        or containerized setups for example).""")
    )

    port_env = 'JUPYTER_PORT'
    port_default_value = DEFAULT_NOTEBOOK_PORT
    port = Integer(port_default_value, config=True,
        help=_("The port the notebook server will listen on (env: JUPYTER_PORT).")
    )

    @default('port')
    def port_default(self):
        return int(os.getenv(self.port_env, self.port_default_value))

    port_retries_env = 'JUPYTER_PORT_RETRIES'
    port_retries_default_value = 50
    port_retries = Integer(port_retries_default_value, config=True,
        help=_("The number of additional ports to try if the specified port is not "
               "available (env: JUPYTER_PORT_RETRIES).")
    )

    @default('port_retries')
    def port_retries_default(self):
        return int(os.getenv(self.port_retries_env, self.port_retries_default_value))


    sock = Unicode('', config=True,
        help=_("The UNIX socket the notebook server will listen on.")
    )

    sock_mode = Unicode('0600', config=True,
        help=_("The permissions mode for UNIX socket creation (default: 0600).")
    )

    @validate('sock_mode')
    def _validate_sock_mode(self, proposal):
        value = proposal['value']
        try:
            converted_value = int(value.encode(), 8)
            assert all((
                # Ensure the mode is at least user readable/writable.
                bool(converted_value & stat.S_IRUSR),
                bool(converted_value & stat.S_IWUSR),
                # And isn't out of bounds.
                converted_value <= 2 ** 12
            ))
        except ValueError as e:
            raise TraitError(
                'invalid --sock-mode value: %s, please specify as e.g. "0600"' % value
            ) from e
        except AssertionError as e:
            raise TraitError(
                'invalid --sock-mode value: %s, must have u+rw (0600) at a minimum' % value
            ) from e
        return value


    certfile = Unicode('', config=True,
        help=_("""The full path to an SSL/TLS certificate file.""")
    )

    keyfile = Unicode('', config=True,
        help=_("""The full path to a private key file for usage with SSL/TLS.""")
    )

    client_ca = Unicode('', config=True,
        help=_("""The full path to a certificate authority certificate for SSL/TLS client authentication.""")
    )

    cookie_secret_file = Unicode(config=True,
        help=_("""The file where the cookie secret is stored.""")
    )

    @default('cookie_secret_file')
    def _default_cookie_secret_file(self):
        return os.path.join(self.runtime_dir, 'notebook_cookie_secret')

    cookie_secret = Bytes(b'', config=True,
        help="""The random bytes used to secure cookies.
        By default this is a new random number every time you start the Notebook.
        Set it to a value in a config file to enable logins to persist across server sessions.

        Note: Cookie secrets should be kept private, do not share config files with
        cookie_secret stored in plaintext (you can read the value from a file).
        """
    )

    @default('cookie_secret')
    def _default_cookie_secret(self):
        if os.path.exists(self.cookie_secret_file):
            with open(self.cookie_secret_file, 'rb') as f:
                key =  f.read()
        else:
            key = encodebytes(os.urandom(32))
            self._write_cookie_secret_file(key)
        h = hmac.new(key, digestmod=hashlib.sha256)
        h.update(self.password.encode())
        return h.digest()

    def _write_cookie_secret_file(self, secret):
        """write my secret to my secret_file"""
        self.log.info(_("Writing notebook server cookie secret to %s"), self.cookie_secret_file)
        try:
            with open(self.cookie_secret_file, 'wb') as f:
                f.write(secret)
        except OSError as e:
            self.log.error(_("Failed to write cookie secret to %s: %s"),
                           self.cookie_secret_file, e)
        try:
            os.chmod(self.cookie_secret_file, 0o600)
        except OSError:
            self.log.warning(
                _("Could not set permissions on %s"),
                self.cookie_secret_file
            )

    token = Unicode('<generated>',
        help=_("""Token used for authenticating first-time connections to the server.

        The token can be read from the file referenced by JUPYTER_TOKEN_FILE or set directly
        with the JUPYTER_TOKEN environment variable.

        When no password is enabled,
        the default is to generate a new, random token.

        Setting to an empty string disables authentication altogether, which is NOT RECOMMENDED.
        """)
    ).tag(config=True)

    _token_generated = True

    @default('token')
    def _token_default(self):
        if os.getenv('JUPYTER_TOKEN'):
            self._token_generated = False
            return os.getenv('JUPYTER_TOKEN')
        if os.getenv('JUPYTER_TOKEN_FILE'):
            self._token_generated = False
            with open(os.getenv('JUPYTER_TOKEN_FILE')) as token_file:
                return token_file.read()
        if self.password:
            # no token if password is enabled
            self._token_generated = False
            return ''
        else:
            self._token_generated = True
            return binascii.hexlify(os.urandom(24)).decode('ascii')

    max_body_size = Integer(512 * 1024 * 1024, config=True,
        help="""
        Sets the maximum allowed size of the client request body, specified in
        the Content-Length request header field. If the size in a request
        exceeds the configured value, a malformed HTTP message is returned to
        the client.

        Note: max_body_size is applied even in streaming mode.
        """
    )

    max_buffer_size = Integer(512 * 1024 * 1024, config=True,
        help="""
        Gets or sets the maximum amount of memory, in bytes, that is allocated
        for use by the buffer manager.
        """
    )

    min_open_files_limit = Integer(config=True,
        help="""
        Gets or sets a lower bound on the open file handles process resource
        limit. This may need to be increased if you run into an
        OSError: [Errno 24] Too many open files.
        This is not applicable when running on Windows.
        """)

    @default('min_open_files_limit')
    def _default_min_open_files_limit(self):
        if resource is None:
            # Ignoring min_open_files_limit because the limit cannot be adjusted (for example, on Windows)
            return None

        soft, hard = resource.getrlimit(resource.RLIMIT_NOFILE)

        DEFAULT_SOFT = 4096
        if hard >= DEFAULT_SOFT:
            return DEFAULT_SOFT

        self.log.debug("Default value for min_open_files_limit is ignored (hard=%r, soft=%r)", hard, soft)

        return soft

    @observe('token')
    def _token_changed(self, change):
        self._token_generated = False

    password = Unicode('', config=True,
                      help="""Hashed password to use for web authentication.

                      To generate, type in a python/IPython shell:

                        from notebook.auth import passwd; passwd()

                      The string should be of the form type:salt:hashed-password.
                      """
    )

    password_required = Bool(False, config=True,
                      help="""Forces users to use a password for the Notebook server.
                      This is useful in a multi user environment, for instance when
                      everybody in the LAN can access each other's machine through ssh.

                      In such a case, serving the notebook server on localhost is not secure
                      since any user can connect to the notebook server via ssh.

                      """
    )

    allow_password_change = Bool(True, config=True,
                    help="""Allow password to be changed at login for the notebook server.

                    While logging in with a token, the notebook server UI will give the opportunity to
                    the user to enter a new password at the same time that will replace
                    the token login mechanism.

                    This can be set to false to prevent changing password from the UI/API.
                    """
    )


    disable_check_xsrf = Bool(False, config=True,
        help="""Disable cross-site-request-forgery protection

        Jupyter notebook 4.3.1 introduces protection from cross-site request forgeries,
        requiring API requests to either:

        - originate from pages served by this server (validated with XSRF cookie and token), or
        - authenticate with a token

        Some anonymous compute resources still desire the ability to run code,
        completely without authentication.
        These services can disable all authentication and security checks,
        with the full knowledge of what that implies.
        """
    )

    allow_remote_access = Bool(config=True,
       help="""Allow requests where the Host header doesn't point to a local server

       By default, requests get a 403 forbidden response if the 'Host' header
       shows that the browser thinks it's on a non-local domain.
       Setting this option to True disables this check.

       This protects against 'DNS rebinding' attacks, where a remote web server
       serves you a page and then changes its DNS to send later requests to a
       local IP, bypassing same-origin checks.

       Local IP addresses (such as 127.0.0.1 and ::1) are allowed as local,
       along with hostnames configured in local_hostnames.
       """)

    @default('allow_remote_access')
    def _default_allow_remote(self):
        """Disallow remote access if we're listening only on loopback addresses"""

        # if blank, self.ip was configured to "*" meaning bind to all interfaces,
        # see _valdate_ip
        if self.ip == "":
            return True

        try:
            addr = ipaddress.ip_address(self.ip)
        except ValueError:
            # Address is a hostname
            for info in socket.getaddrinfo(self.ip, self.port, 0, socket.SOCK_STREAM):
                addr = info[4][0]
                if not py3compat.PY3:
                    addr = addr.decode('ascii')

                try:
                    parsed = ipaddress.ip_address(addr.split('%')[0])
                except ValueError:
                    self.log.warning("Unrecognised IP address: %r", addr)
                    continue

                # Macs map localhost to 'fe80::1%lo0', a link local address
                # scoped to the loopback interface. For now, we'll assume that
                # any scoped link-local address is effectively local.
                if not (parsed.is_loopback
                        or (('%' in addr) and parsed.is_link_local)):
                    return True
            return False
        else:
            return not addr.is_loopback

    local_hostnames = List(Unicode(), ['localhost'], config=True,
       help="""Hostnames to allow as local when allow_remote_access is False.

       Local IP addresses (such as 127.0.0.1 and ::1) are automatically accepted
       as local as well.
       """
    )

    open_browser = Bool(True, config=True,
                        help="""Whether to open in a browser after starting.
                        The specific browser used is platform dependent and
                        determined by the python standard library `webbrowser`
                        module, unless it is overridden using the --browser
                        (NotebookApp.browser) configuration option.
                        """)

    browser = Unicode('', config=True,
                      help="""Specify what command to use to invoke a web
                      browser when opening the notebook. If not specified, the
                      default browser will be determined by the `webbrowser`
                      standard library module, which allows setting of the
                      BROWSER environment variable to override it.
                      """)

    webbrowser_open_new = Integer(2, config=True,
        help=_("""Specify Where to open the notebook on startup. This is the
        `new` argument passed to the standard library method `webbrowser.open`.
        The behaviour is not guaranteed, but depends on browser support. Valid
        values are:

         - 2 opens a new tab,
         - 1 opens a new window,
         - 0 opens in an existing window.

        See the `webbrowser.open` documentation for details.
        """))

    webapp_settings = Dict(config=True,
        help=_("DEPRECATED, use tornado_settings")
    )

    @observe('webapp_settings')
    def _update_webapp_settings(self, change):
        self.log.warning(_("\n    webapp_settings is deprecated, use tornado_settings.\n"))
        self.tornado_settings = change['new']

    tornado_settings = Dict(config=True,
            help=_("Supply overrides for the tornado.web.Application that the "
                 "Jupyter notebook uses."))

    websocket_compression_options = Any(None, config=True,
        help=_("""
        Set the tornado compression options for websocket connections.

        This value will be returned from :meth:`WebSocketHandler.get_compression_options`.
        None (default) will disable compression.
        A dict (even an empty one) will enable compression.

        See the tornado docs for WebSocketHandler.get_compression_options for details.
        """)
    )
    terminado_settings = Dict(config=True,
            help=_('Supply overrides for terminado. Currently only supports "shell_command". '
                 'On Unix, if "shell_command" is not provided, a non-login shell is launched '
                 "by default when the notebook server is connected to a terminal, a login "
                 "shell otherwise."))

    cookie_options = Dict(config=True,
        help=_("Extra keyword arguments to pass to `set_secure_cookie`."
             " See tornado's set_secure_cookie docs for details.")
    )
    get_secure_cookie_kwargs = Dict(config=True,
        help=_("Extra keyword arguments to pass to `get_secure_cookie`."
             " See tornado's get_secure_cookie docs for details.")
    )
    ssl_options = Dict(config=True,
            help=_("""Supply SSL options for the tornado HTTPServer.
            See the tornado docs for details."""))

    jinja_environment_options = Dict(config=True,
            help=_("Supply extra arguments that will be passed to Jinja environment."))

    jinja_template_vars = Dict(
        config=True,
        help=_("Extra variables to supply to jinja templates when rendering."),
    )

    enable_mathjax = Bool(True, config=True,
        help="""Whether to enable MathJax for typesetting math/TeX

        MathJax is the javascript library Jupyter uses to render math/LaTeX. It is
        very large, so you may want to disable it if you have a slow internet
        connection, or for offline use of the notebook.

        When disabled, equations etc. will appear as their untransformed TeX source.
        """
    )

    @observe('enable_mathjax')
    def _update_enable_mathjax(self, change):
        """set mathjax url to empty if mathjax is disabled"""
        if not change['new']:
            self.mathjax_url = ''

    base_url = Unicode('/', config=True,
                               help='''The base URL for the notebook server.

                               Leading and trailing slashes can be omitted,
                               and will automatically be added.
                               ''')

    @validate('base_url')
    def _update_base_url(self, proposal):
        value = proposal['value']
        if not value.startswith('/'):
            value = '/' + value
        if not value.endswith('/'):
            value = value + '/'
        return value

    base_project_url = Unicode('/', config=True, help=_("""DEPRECATED use base_url"""))

    @observe('base_project_url')
    def _update_base_project_url(self, change):
        self.log.warning(_("base_project_url is deprecated, use base_url"))
        self.base_url = change['new']

    extra_static_paths = List(Unicode(), config=True,
        help="""Extra paths to search for serving static files.

        This allows adding javascript/css to be available from the notebook server machine,
        or overriding individual files in the IPython"""
    )

    @property
    def static_file_path(self):
        """return extra paths + the default location"""
        return self.extra_static_paths + [DEFAULT_STATIC_FILES_PATH]

    static_custom_path = List(Unicode(),
        help=_("""Path to search for custom.js, css""")
    )

    @default('static_custom_path')
    def _default_static_custom_path(self):
        return [
            os.path.join(d, 'custom') for d in (
                self.config_dir,
                DEFAULT_STATIC_FILES_PATH)
        ]

    extra_template_paths = List(Unicode(), config=True,
        help=_("""Extra paths to search for serving jinja templates.

        Can be used to override templates from notebook.templates.""")
    )

    @property
    def template_file_path(self):
        """return extra paths + the default locations"""
        return self.extra_template_paths + DEFAULT_TEMPLATE_PATH_LIST

    extra_nbextensions_path = List(Unicode(), config=True,
        help=_("""extra paths to look for Javascript notebook extensions""")
    )

    extra_services = List(Unicode(), config=True,
        help=_("""handlers that should be loaded at higher priority than the default services""")
    )

    @property
    def nbextensions_path(self):
        """The path to look for Javascript notebook extensions"""
        path = self.extra_nbextensions_path + jupyter_path('nbextensions')
        # FIXME: remove IPython nbextensions path after a migration period
        try:
            from IPython.paths import get_ipython_dir
        except ImportError:
            pass
        else:
            path.append(os.path.join(get_ipython_dir(), 'nbextensions'))
        return path

    websocket_url = Unicode("", config=True,
        help="""The base URL for websockets,
        if it differs from the HTTP server (hint: it almost certainly doesn't).

        Should be in the form of an HTTP origin: ws[s]://hostname[:port]
        """
    )

    mathjax_url = Unicode("", config=True,
        help="""A custom url for MathJax.js.
        Should be in the form of a case-sensitive url to MathJax,
        for example:  /static/components/MathJax/MathJax.js
        """
    )

    @default('mathjax_url')
    def _default_mathjax_url(self):
        if not self.enable_mathjax:
            return ''
        static_url_prefix = self.tornado_settings.get("static_url_prefix", "static")
        return url_path_join(static_url_prefix, 'components', 'MathJax', 'MathJax.js')

    @observe('mathjax_url')
    def _update_mathjax_url(self, change):
        new = change['new']
        if new and not self.enable_mathjax:
            # enable_mathjax=False overrides mathjax_url
            self.mathjax_url = ''
        else:
            self.log.info(_("Using MathJax: %s"), new)

    mathjax_config = Unicode("TeX-AMS-MML_HTMLorMML-full,Safe", config=True,
        help=_("""The MathJax.js configuration file that is to be used.""")
    )

    @observe('mathjax_config')
    def _update_mathjax_config(self, change):
        self.log.info(_("Using MathJax configuration file: %s"), change['new'])

    quit_button = Bool(True, config=True,
        help="""If True, display a button in the dashboard to quit
        (shutdown the notebook server)."""
    )

    # We relax this trait to handle Contents Managers using jupyter_server
    # as the core backend.
    contents_manager_class = TypeFromClasses(
        default_value=LargeFileManager,
        klasses=[
            ContentsManager,
            # To make custom ContentsManagers both forward+backward
            # compatible, we'll relax the strictness of this trait
            # and allow jupyter_server contents managers to pass
            # through. If jupyter_server is not installed, this class
            # will be ignored.
            'jupyter_server.contents.services.managers.ContentsManager'
        ],
        config=True,
        help=_('The notebook manager class to use.')
    )

    # Throws a deprecation warning to jupyter_server based contents managers.
    @observe('contents_manager_class')
    def _observe_contents_manager_class(self, change):
        new = change['new']
        # If 'new' is a class, get a string representing the import
        # module path.
        if inspect.isclass(new):
            new = new.__module__

        if new.startswith('jupyter_server'):
            self.log.warning(
                "The specified 'contents_manager_class' class inherits a manager from the "
                "'jupyter_server' package. These (future-looking) managers are not "
                "guaranteed to work with the 'notebook' package. For longer term support "
                "consider switching to NBClassic—a notebook frontend that leverages "
                "Jupyter Server as its server backend."
            )

    kernel_manager_class = Type(
        default_value=MappingKernelManager,
        klass=MappingKernelManager,
        config=True,
        help=_('The kernel manager class to use.')
    )

    session_manager_class = Type(
        default_value=SessionManager,
        config=True,
        help=_('The session manager class to use.')
    )

    config_manager_class = Type(
        default_value=ConfigManager,
        config = True,
        help=_('The config manager class to use')
    )

    kernel_spec_manager = Instance(KernelSpecManager, allow_none=True)

    kernel_spec_manager_class = Type(
        default_value=KernelSpecManager,
        config=True,
        help="""
        The kernel spec manager class to use. Should be a subclass
        of `jupyter_client.kernelspec.KernelSpecManager`.

        The Api of KernelSpecManager is provisional and might change
        without warning between this version of Jupyter and the next stable one.
        """
    )

    login_handler_class = Type(
        default_value=LoginHandler,
        klass=web.RequestHandler,
        config=True,
        help=_('The login handler class to use.'),
    )

    logout_handler_class = Type(
        default_value=LogoutHandler,
        klass=web.RequestHandler,
        config=True,
        help=_('The logout handler class to use.'),
    )

    trust_xheaders = Bool(False, config=True,
        help=(_("Whether to trust or not X-Scheme/X-Forwarded-Proto and X-Real-Ip/X-Forwarded-For headers "
              "sent by the upstream reverse proxy. Necessary if the proxy handles SSL"))
    )

    info_file = Unicode()

    @default('info_file')
    def _default_info_file(self):
        info_file = "nbserver-%s.json" % os.getpid()
        return os.path.join(self.runtime_dir, info_file)

    browser_open_file = Unicode()

    @default('browser_open_file')
    def _default_browser_open_file(self):
        basename = "nbserver-%s-open.html" % os.getpid()
        return os.path.join(self.runtime_dir, basename)

    pylab = Unicode('disabled', config=True,
        help=_("""
        DISABLED: use %pylab or %matplotlib in the notebook to enable matplotlib.
        """)
    )

    @observe('pylab')
    def _update_pylab(self, change):
        """when --pylab is specified, display a warning and exit"""
        if change['new'] != 'warn':
            backend = ' %s' % change['new']
        else:
            backend = ''
        self.log.error(_("Support for specifying --pylab on the command line has been removed."))
        self.log.error(
            _("Please use `%pylab{0}` or `%matplotlib{0}` in the notebook itself.").format(backend)
        )
        self.exit(1)

    notebook_dir = Unicode(config=True,
        help=_("The directory to use for notebooks and kernels.")
    )

    @default('notebook_dir')
    def _default_notebook_dir(self):
        if self.file_to_run:
            return os.path.dirname(os.path.abspath(self.file_to_run))
        else:
            return py3compat.getcwd()

    @validate('notebook_dir')
    def _notebook_dir_validate(self, proposal):
        value = proposal['value']
        # Strip any trailing slashes
        # *except* if it's root
        _, path = os.path.splitdrive(value)
        if path == os.sep:
            return value
        value = value.rstrip(os.sep)
        if not os.path.isabs(value):
            # If we receive a non-absolute path, make it absolute.
            value = os.path.abspath(value)
        if not os.path.isdir(value):
            raise TraitError(trans.gettext("No such notebook dir: '%r'") % value)
        return value

    # TODO: Remove me in notebook 5.0
    server_extensions = List(Unicode(), config=True,
        help=(_("DEPRECATED use the nbserver_extensions dict instead"))
    )

    @observe('server_extensions')
    def _update_server_extensions(self, change):
        self.log.warning(_("server_extensions is deprecated, use nbserver_extensions"))
        self.server_extensions = change['new']

    nbserver_extensions = Dict({}, config=True,
        help=(_("Dict of Python modules to load as notebook server extensions. "
              "Entry values can be used to enable and disable the loading of "
              "the extensions. The extensions will be loaded in alphabetical "
              "order."))
    )

    reraise_server_extension_failures = Bool(
        False,
        config=True,
        help=_("Reraise exceptions encountered loading server extensions?"),
    )

    iopub_msg_rate_limit = Float(1000, config=True, help=_("""(msgs/sec)
        Maximum rate at which messages can be sent on iopub before they are
        limited."""))

    iopub_data_rate_limit = Float(1000000, config=True, help=_("""(bytes/sec)
        Maximum rate at which stream output can be sent on iopub before they are
        limited."""))

    rate_limit_window = Float(3, config=True, help=_("""(sec) Time window used to
        check the message and data rate limits."""))

    shutdown_no_activity_timeout = Integer(0, config=True,
        help=("Shut down the server after N seconds with no kernels or "
              "terminals running and no activity. "
              "This can be used together with culling idle kernels "
              "(MappingKernelManager.cull_idle_timeout) to "
              "shutdown the notebook server when it's not in use. This is not "
              "precisely timed: it may shut down up to a minute later. "
              "0 (the default) disables this automatic shutdown.")
    )

    terminals_enabled = Bool(True, config=True,
         help=_("""Set to False to disable terminals.

         This does *not* make the notebook server more secure by itself.
         Anything the user can in a terminal, they can also do in a notebook.

         Terminals may also be automatically disabled if the terminado package
         is not available.
         """))

    authenticate_prometheus = Bool(
        True,
        help=""""
        Require authentication to access prometheus metrics.
        """
    ).tag(config=True)

    @default('authenticate_prometheus')
    def _default_authenticate_prometheus(self):
        """ Authenticate Prometheus by default, unless auth is disabled. """
        auth = bool(self.password) or bool(self.token)
        if auth is False:
            self.log.info(_("Authentication of /metrics is OFF, since other authentication is disabled."))
        return auth

    @observe('authenticate_prometheus')
    def _update_authenticate_prometheus(self, change):
        newauth = change['new']
        if self.authenticate_prometheus is True and newauth is False:
            self.log.info(_("Authentication of /metrics is being turned OFF."))
        self.authenticate_prometheus = newauth

    # Since use of terminals is also a function of whether the terminado package is
    # available, this variable holds the "final indication" of whether terminal functionality
    # should be considered (particularly during shutdown/cleanup).  It is enabled only
    # once both the terminals "service" can be initialized and terminals_enabled is True.
    # Note: this variable is slightly different from 'terminals_available' in the web settings
    # in that this variable *could* remain false if terminado is available, yet the terminal
    # service's initialization still fails.  As a result, this variable holds the truth.
    terminals_available = False

    def parse_command_line(self, argv=None):
        super().parse_command_line(argv)

        if self.extra_args:
            arg0 = self.extra_args[0]
            f = os.path.abspath(arg0)
            self.argv.remove(arg0)
            if not os.path.exists(f):
                self.log.critical(_("No such file or directory: %s"), f)
                self.exit(1)

            # Use config here, to ensure that it takes higher priority than
            # anything that comes from the config dirs.
            c = Config()
            if os.path.isdir(f):
                c.NotebookApp.notebook_dir = f
            elif os.path.isfile(f):
                c.NotebookApp.file_to_run = f
            self.update_config(c)

    def init_configurables(self):

        # If gateway server is configured, replace appropriate managers to perform redirection.  To make
        # this determination, instantiate the GatewayClient config singleton.
        self.gateway_config = GatewayClient.instance(parent=self)

        if self.gateway_config.gateway_enabled:
            self.kernel_manager_class = 'notebook.gateway.managers.GatewayKernelManager'
            self.session_manager_class = 'notebook.gateway.managers.GatewaySessionManager'
            self.kernel_spec_manager_class = 'notebook.gateway.managers.GatewayKernelSpecManager'

        self.kernel_spec_manager = self.kernel_spec_manager_class(
            parent=self,
        )

        self.kernel_manager = self.kernel_manager_class(
            parent=self,
            log=self.log,
            connection_dir=self.runtime_dir,
            kernel_spec_manager=self.kernel_spec_manager,
        )
        #  Ensure the appropriate version of Python and jupyter_client is available.
        if isinstance(self.kernel_manager, AsyncMappingKernelManager):
            if not async_kernel_mgmt_available:  # Can be removed once jupyter_client >= 6.1 is required.
                raise ValueError("You are using `AsyncMappingKernelManager` without an appropriate "
                                 "jupyter_client installed!  Please upgrade jupyter_client or change kernel managers.")
            self.log.info("Asynchronous kernel management has been configured to use '{}'.".
                          format(self.kernel_manager.__class__.__name__))

        self.contents_manager = self.contents_manager_class(
            parent=self,
            log=self.log,
        )
        self.session_manager = self.session_manager_class(
            parent=self,
            log=self.log,
            kernel_manager=self.kernel_manager,
            contents_manager=self.contents_manager,
        )
        self.config_manager = self.config_manager_class(
            parent=self,
            log=self.log,
        )

    def init_logging(self):
        # This prevents double log messages because tornado use a root logger that
        # self.log is a child of. The logging module dispatches log messages to a log
        # and all of its ancenstors until propagate is set to False.
        self.log.propagate = False

        for log in app_log, access_log, gen_log:
            # consistent log output name (NotebookApp instead of tornado.access, etc.)
            log.name = self.log.name
        # hook up tornado 3's loggers to our app handlers
        logger = logging.getLogger('tornado')
        logger.propagate = True
        logger.parent = self.log
        logger.setLevel(self.log.level)

    def init_resources(self):
        """initialize system resources"""
        if resource is None:
            self.log.debug('Ignoring min_open_files_limit because the limit cannot be adjusted (for example, on Windows)')
            return

        old_soft, old_hard = resource.getrlimit(resource.RLIMIT_NOFILE)
        soft = self.min_open_files_limit
        hard = old_hard
        if old_soft < soft:
            if hard < soft:
                hard = soft
            self.log.debug(
                f'Raising open file limit: soft {old_soft}->{soft}; hard {old_hard}->{hard}'
            )
            resource.setrlimit(resource.RLIMIT_NOFILE, (soft, hard))

    def init_webapp(self):
        """initialize tornado webapp and httpserver"""
        self.tornado_settings['allow_origin'] = self.allow_origin
        self.tornado_settings['websocket_compression_options'] = self.websocket_compression_options
        if self.allow_origin_pat:
            self.tornado_settings['allow_origin_pat'] = re.compile(self.allow_origin_pat)
        self.tornado_settings['allow_credentials'] = self.allow_credentials
        self.tornado_settings['autoreload'] = self.autoreload
        self.tornado_settings['cookie_options'] = self.cookie_options
        self.tornado_settings['get_secure_cookie_kwargs'] = self.get_secure_cookie_kwargs
        self.tornado_settings['token'] = self.token

        # ensure default_url starts with base_url
        if not self.default_url.startswith(self.base_url):
            self.default_url = url_path_join(self.base_url, self.default_url)

        if self.password_required and (not self.password):
            self.log.critical(_("Notebook servers are configured to only be run with a password."))
            self.log.critical(_("Hint: run the following command to set a password"))
            self.log.critical(_("\t$ python -m notebook.auth password"))
            sys.exit(1)

        # Socket options validation.
        if self.sock:
            if self.port != DEFAULT_NOTEBOOK_PORT:
                self.log.critical(
                    _('Options --port and --sock are mutually exclusive. Aborting.'),
                )
                sys.exit(1)
            else:
                # Reset the default port if we're using a UNIX socket.
                self.port = 0

            if self.open_browser:
                # If we're bound to a UNIX socket, we can't reliably connect from a browser.
                self.log.info(
                    _('Ignoring --NotebookApp.open_browser due to --sock being used.'),
                )

            if self.file_to_run:
                self.log.critical(
                    _('Options --NotebookApp.file_to_run and --sock are mutually exclusive.'),
                )
                sys.exit(1)

            if sys.platform.startswith('win'):
                self.log.critical(
                    _('Option --sock is not supported on Windows, but got value of %s. Aborting.' % self.sock),
                )
                sys.exit(1)

        self.web_app = NotebookWebApplication(
            self, self.kernel_manager, self.contents_manager,
            self.session_manager, self.kernel_spec_manager,
            self.config_manager, self.extra_services,
            self.log, self.base_url, self.default_url, self.tornado_settings,
            self.jinja_environment_options,
        )
        ssl_options = self.ssl_options
        if self.certfile:
            ssl_options['certfile'] = self.certfile
        if self.keyfile:
            ssl_options['keyfile'] = self.keyfile
        if self.client_ca:
            ssl_options['ca_certs'] = self.client_ca
        if not ssl_options:
            # None indicates no SSL config
            ssl_options = None
        else:
            # SSL may be missing, so only import it if it's to be used
            import ssl
            # PROTOCOL_TLS selects the highest ssl/tls protocol version that both the client and
            # server support. When PROTOCOL_TLS is not available use PROTOCOL_SSLv23.
            # PROTOCOL_TLS is new in version 2.7.13, 3.5.3 and 3.6
            ssl_options.setdefault(
                'ssl_version',
                getattr(ssl, 'PROTOCOL_TLS', ssl.PROTOCOL_SSLv23)
            )
            if ssl_options.get('ca_certs', False):
                ssl_options.setdefault('cert_reqs', ssl.CERT_REQUIRED)

        self.login_handler_class.validate_security(self, ssl_options=ssl_options)
        self.http_server = httpserver.HTTPServer(self.web_app, ssl_options=ssl_options,
                                                 xheaders=self.trust_xheaders,
                                                 max_body_size=self.max_body_size,
                                                 max_buffer_size=self.max_buffer_size)

    def _bind_http_server(self):
        return self._bind_http_server_unix() if self.sock else self._bind_http_server_tcp()

    def _bind_http_server_unix(self):
        if unix_socket_in_use(self.sock):
            self.log.warning(_('The socket %s is already in use.') % self.sock)
            return False

        try:
            sock = bind_unix_socket(self.sock, mode=int(self.sock_mode.encode(), 8))
            self.http_server.add_socket(sock)
        except OSError as e:
            if e.errno == errno.EADDRINUSE:
                self.log.warning(_('The socket %s is already in use.') % self.sock)
                return False
            elif e.errno in (errno.EACCES, getattr(errno, 'WSAEACCES', errno.EACCES)):
                self.log.warning(_("Permission to listen on sock %s denied") % self.sock)
                return False
            else:
                raise
        else:
            return True

    def _bind_http_server_tcp(self):
        success = None
        for port in random_ports(self.port, self.port_retries+1):
            try:
                self.http_server.listen(port, self.ip)
            except OSError as e:
                eacces = (errno.EACCES, getattr(errno, 'WSAEACCES', errno.EACCES))
                if sys.platform == 'cygwin':
                    # Cygwin has a bug that causes EPERM to be returned in this
                    # case instead of EACCES:
                    # https://cygwin.com/ml/cygwin/2019-04/msg00160.html
                    eacces += (errno.EPERM,)

                if e.errno == errno.EADDRINUSE:
                    if self.port_retries:
                        self.log.info(_('The port %i is already in use, trying another port.') % port)
                    else:
                        self.log.info(_('The port %i is already in use.') % port)
                    continue
                elif e.errno in eacces:
                    self.log.warning(_("Permission to listen on port %i denied.") % port)
                    continue
                else:
                    raise
            else:
                self.port = port
                success = True
                break
        if not success:
            if self.port_retries:
                self.log.critical(_('ERROR: the notebook server could not be started because '
                              'no available port could be found.'))
            else:
                self.log.critical(_('ERROR: the notebook server could not be started because '
                              'port %i is not available.') % port)
            self.exit(1)
        return success

    def _concat_token(self, url):
        token = self.token if self._token_generated else '...'
        return url_concat(url, {'token': token})

    @property
    def display_url(self):
        if self.custom_display_url:
            url = self.custom_display_url
            if not url.endswith('/'):
                url += '/'
        elif self.sock:
            url = self._unix_sock_url()
        else:
            if self.ip in ('', '0.0.0.0'):
                ip = "%s" % socket.gethostname()
            else:
                ip = self.ip
            url = self._tcp_url(ip)
        if self.token and not self.sock:
            url = self._concat_token(url)
            if not self.custom_display_url:
                url += '\n or %s' % self._concat_token(self._tcp_url('127.0.0.1'))
        return url

    @property
    def connection_url(self):
        if self.sock:
            return self._unix_sock_url()
        else:
            ip = self.ip if self.ip else 'localhost'
            return self._tcp_url(ip)

    def _unix_sock_url(self, token=None):
        return f'{urlencode_unix_socket(self.sock)}{self.base_url}'

    def _tcp_url(self, ip, port=None):
        proto = 'https' if self.certfile else 'http'
        return "%s://%s:%i%s" % (proto, ip, port or self.port, self.base_url)

    def init_terminals(self):
        if not self.terminals_enabled:
            return

        try:
            from .terminal import initialize
            initialize(nb_app=self)
            self.terminals_available = True
        except ImportError as e:
            self.log.warning(_("Terminals not available (error was %s)"), e)

    def init_signal(self):
        if not sys.platform.startswith('win') and sys.stdin and sys.stdin.isatty():
            signal.signal(signal.SIGINT, self._handle_sigint)
        signal.signal(signal.SIGTERM, self._signal_stop)
        if hasattr(signal, 'SIGUSR1'):
            # Windows doesn't support SIGUSR1
            signal.signal(signal.SIGUSR1, self._signal_info)
        if hasattr(signal, 'SIGINFO'):
            # only on BSD-based systems
            signal.signal(signal.SIGINFO, self._signal_info)

    def _handle_sigint(self, sig, frame):
        """SIGINT handler spawns confirmation dialog"""
        # register more forceful signal handler for ^C^C case
        signal.signal(signal.SIGINT, self._signal_stop)
        # request confirmation dialog in bg thread, to avoid
        # blocking the App
        thread = threading.Thread(target=self._confirm_exit)
        thread.daemon = True
        thread.start()

    def _restore_sigint_handler(self):
        """callback for restoring original SIGINT handler"""
        signal.signal(signal.SIGINT, self._handle_sigint)

    def _confirm_exit(self):
        """confirm shutdown on ^C

        A second ^C, or answering 'y' within 5s will cause shutdown,
        otherwise original SIGINT handler will be restored.

        This doesn't work on Windows.
        """
        info = self.log.info
        info(_('interrupted'))
        # Check if answer_yes is set
        if self.answer_yes:
            self.log.critical(_("Shutting down..."))
            # schedule stop on the main thread,
            # since this might be called from a signal handler
            self.io_loop.add_callback_from_signal(self.io_loop.stop)
            return
        print(self.notebook_info())
        yes = _('y')
        no = _('n')
        sys.stdout.write(_("Shutdown this notebook server (%s/[%s])? ") % (yes, no))
        sys.stdout.flush()
        r,w,x = select.select([sys.stdin], [], [], 5)
        if r:
            line = sys.stdin.readline()
            if line.lower().startswith(yes) and no not in line.lower():
                self.log.critical(_("Shutdown confirmed"))
                # schedule stop on the main thread,
                # since this might be called from a signal handler
                self.io_loop.add_callback_from_signal(self.io_loop.stop)
                return
        else:
            print(_("No answer for 5s:"), end=' ')
        print(_("resuming operation..."))
        # no answer, or answer is no:
        # set it back to original SIGINT handler
        # use IOLoop.add_callback because signal.signal must be called
        # from main thread
        self.io_loop.add_callback_from_signal(self._restore_sigint_handler)

    def _signal_stop(self, sig, frame):
        self.log.critical(_("received signal %s, stopping"), sig)
        self.io_loop.add_callback_from_signal(self.io_loop.stop)

    def _signal_info(self, sig, frame):
        print(self.notebook_info())

    def init_components(self):
        """Check the components submodule, and warn if it's unclean"""
        # TODO: this should still check, but now we use bower, not git submodule
        pass

    def init_server_extension_config(self):
        """Consolidate server extensions specified by all configs.

        The resulting list is stored on self.nbserver_extensions and updates config object.

        The extension API is experimental, and may change in future releases.
        """
        # TODO: Remove me in notebook 5.0
        for modulename in self.server_extensions:
            # Don't override disable state of the extension if it already exist
            # in the new traitlet
            if not modulename in self.nbserver_extensions:
                self.nbserver_extensions[modulename] = True

        # Load server extensions with ConfigManager.
        # This enables merging on keys, which we want for extension enabling.
        # Regular config loading only merges at the class level,
        # so each level (user > env > system) clobbers the previous.
        config_path = jupyter_config_path()
        if self.config_dir not in config_path:
            # add self.config_dir to the front, if set manually
            config_path.insert(0, self.config_dir)
        manager = ConfigManager(read_config_path=config_path)
        section = manager.get(self.config_file_name)
        extensions = section.get('NotebookApp', {}).get('nbserver_extensions', {})

        for modulename, enabled in sorted(extensions.items()):
            if modulename not in self.nbserver_extensions:
                self.config.NotebookApp.nbserver_extensions.update({modulename: enabled})
                self.nbserver_extensions.update({modulename: enabled})

    def init_server_extensions(self):
        """Load any extensions specified by config.

        Import the module, then call the load_jupyter_server_extension function,
        if one exists.

        The extension API is experimental, and may change in future releases.
        """


        for modulename, enabled in sorted(self.nbserver_extensions.items()):
            if enabled:
                try:
                    mod = importlib.import_module(modulename)
                    func = getattr(mod, 'load_jupyter_server_extension', None)
                    if func is not None:
                        func(self)
                except Exception:
                    if self.reraise_server_extension_failures:
                        raise
                    self.log.warning(_("Error loading server extension %s"), modulename,
                                  exc_info=True)

    def init_mime_overrides(self):
        # On some Windows machines, an application has registered incorrect
        # mimetypes in the registry.
        # Tornado uses this when serving .css and .js files, causing browsers to
        # reject these files. We know the mimetype always needs to be text/css for css
        # and application/javascript for JS, so we override it here
        # and explicitly tell the mimetypes to not trust the Windows registry
        if os.name == 'nt':
            # do not trust windows registry, which regularly has bad info
            mimetypes.init(files=[])
        # ensure css, js are correct, which are required for pages to function
        mimetypes.add_type('text/css', '.css')
        mimetypes.add_type('application/javascript', '.js')
        # for python <3.8
        mimetypes.add_type('application/wasm', '.wasm')

    def shutdown_no_activity(self):
        """Shutdown server on timeout when there are no kernels or terminals."""
        km = self.kernel_manager
        if len(km) != 0:
            return   # Kernels still running

        if self.terminals_available:
            term_mgr = self.web_app.settings['terminal_manager']
            if term_mgr.terminals:
                return   # Terminals still running

        seconds_since_active = \
            (utcnow() - self.web_app.last_activity()).total_seconds()
        self.log.debug("No activity for %d seconds.",
                       seconds_since_active)
        if seconds_since_active > self.shutdown_no_activity_timeout:
            self.log.info("No kernels or terminals for %d seconds; shutting down.",
                          seconds_since_active)
            self.stop()

    def init_shutdown_no_activity(self):
        if self.shutdown_no_activity_timeout > 0:
            self.log.info("Will shut down after %d seconds with no kernels or terminals.",
                          self.shutdown_no_activity_timeout)
            pc = ioloop.PeriodicCallback(self.shutdown_no_activity, 60000)
            pc.start()

    def _init_asyncio_patch(self):
        """set default asyncio policy to be compatible with tornado

        Tornado 6 (at least) is not compatible with the default
        asyncio implementation on Windows

        Pick the older SelectorEventLoopPolicy on Windows
        if the known-incompatible default policy is in use.

        do this as early as possible to make it a low priority and overrideable

        ref: https://github.com/tornadoweb/tornado/issues/2608

        FIXME: if/when tornado supports the defaults in asyncio,
               remove and bump tornado requirement for py38

        With the introduction of the async kernel, the existing sync kernel
        requires the use of nested loops in order to run code synchronously.
        This is done in `jupyter_client` using the helper util `run_sync`:

        ref: https://github.com/jupyter/jupyter_client/blob/f453b51eeeff9e905c583b7da3905c0e35cfbdf0/jupyter_client/utils.py#L11

        which creates a new event loop and relies on `nest_asyncio` patching
        to allow nested loops. This requires that *all* potential tasks are
        patched before executing. When only some tasks are patched it leads to
        the following issue:

        ref: https://github.com/jupyter/notebook/issues/6164

        So we must call `nest_asyncio.apply()` method as early as possible. It
        is preferable to do this in the consuming application rather than the
        `jupyter_client` as it is a global patch and would impact all consumers
        rather than just the ones that rely on synchronous kernel behavior.
        """
        import nest_asyncio

        try:
            nest_asyncio.apply()
        except RuntimeError:
            # nest_asyncio requires a running loop in order to patch.
            # In tests the loop may not have been created yet.
            pass

        if sys.platform.startswith("win") and sys.version_info >= (3, 8):
            import asyncio
            try:
                from asyncio import (
                    WindowsProactorEventLoopPolicy,
                    WindowsSelectorEventLoopPolicy,
                )
            except ImportError:
                pass
                # not affected
            else:
                if type(asyncio.get_event_loop_policy()) is WindowsProactorEventLoopPolicy:
                    # WindowsProactorEventLoopPolicy is not compatible with tornado 6
                    # fallback to the pre-3.8 default of Selector
                    asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())

    @catch_config_error
    def initialize(self, argv=None):
        self._init_asyncio_patch()

        super().initialize(argv)
        self.init_logging()
        if self._dispatching:
            return
        self.init_resources()
        self.init_configurables()
        self.init_server_extension_config()
        self.init_components()
        self.init_webapp()
        self.init_terminals()
        self.init_signal()
        self.init_server_extensions()
        self.init_mime_overrides()
        self.init_shutdown_no_activity()

    def cleanup_kernels(self):
        """Shutdown all kernels.

        The kernels will shutdown themselves when this process no longer exists,
        but explicit shutdown allows the KernelManagers to cleanup the connection files.
        """
        n_kernels = len(self.kernel_manager.list_kernel_ids())
        kernel_msg = trans.ngettext('Shutting down %d kernel', 'Shutting down %d kernels', n_kernels)
        self.log.info(kernel_msg % n_kernels)
        run_sync(self.kernel_manager.shutdown_all())

    def cleanup_terminals(self):
        """Shutdown all terminals.

        The terminals will shutdown themselves when this process no longer exists,
        but explicit shutdown allows the TerminalManager to cleanup.
        """
        if not self.terminals_available:
            return

        terminal_manager = self.web_app.settings['terminal_manager']
        n_terminals = len(terminal_manager.list())
        terminal_msg = trans.ngettext('Shutting down %d terminal', 'Shutting down %d terminals', n_terminals)
        self.log.info(terminal_msg % n_terminals)
        run_sync(terminal_manager.terminate_all())

    def notebook_info(self, kernel_count=True):
        "Return the current working directory and the server url information"
        info = self.contents_manager.info_string() + "\n"
        if kernel_count:
            n_kernels = len(self.kernel_manager.list_kernel_ids())
            kernel_msg = trans.ngettext("%d active kernel", "%d active kernels", n_kernels)
            info += kernel_msg % n_kernels
            info += "\n"
        # Format the info so that the URL fits on a single line in 80 char display
        info += _("Jupyter Notebook {version} is running at:\n{url}".
                  format(version=NotebookApp.version, url=self.display_url))
        if self.gateway_config.gateway_enabled:
            info += _("\nKernels will be managed by the Gateway server running at:\n%s") % self.gateway_config.url
        return info

    def server_info(self):
        """Return a JSONable dict of information about this server."""
        return {'url': self.connection_url,
                'hostname': self.ip if self.ip else 'localhost',
                'port': self.port,
                'sock': self.sock,
                'secure': bool(self.certfile),
                'base_url': self.base_url,
                'token': self.token,
                'notebook_dir': os.path.abspath(self.notebook_dir),
                'password': bool(self.password),
                'pid': os.getpid(),
               }

    def write_server_info_file(self):
        """Write the result of server_info() to the JSON file info_file."""
        try:
            with open(self.info_file, 'w') as f:
                json.dump(self.server_info(), f, indent=2, sort_keys=True)
        except OSError as e:
            self.log.error(_("Failed to write server-info to %s: %s"),
                           self.info_file, e)

    def remove_server_info_file(self):
        """Remove the nbserver-<pid>.json file created for this server.

        Ignores the error raised when the file has already been removed.
        """
        try:
            os.unlink(self.info_file)
        except OSError as e:
            if e.errno != errno.ENOENT:
                raise

    def write_browser_open_file(self):
        """Write an nbserver-<pid>-open.html file

        This can be used to open the notebook in a browser
        """
        # default_url contains base_url, but so does connection_url
        open_url = self.default_url[len(self.base_url):]

        with open(self.browser_open_file, 'w', encoding='utf-8') as f:
            self._write_browser_open_file(open_url, f)

    def _write_browser_open_file(self, url, fh):
        if self.token:
            url = url_concat(url, {'token': self.token})
        url = url_path_join(self.connection_url, url)

        jinja2_env = self.web_app.settings['jinja2_env']
        template = jinja2_env.get_template('browser-open.html')
        fh.write(template.render(open_url=url))

    def remove_browser_open_file(self):
        """Remove the nbserver-<pid>-open.html file created for this server.

        Ignores the error raised when the file has already been removed.
        """
        try:
            os.unlink(self.browser_open_file)
        except OSError as e:
            if e.errno != errno.ENOENT:
                raise

    def launch_browser(self):
        try:
            browser = webbrowser.get(self.browser or None)
        except webbrowser.Error as e:
            self.log.warning(_('No web browser found: %s.') % e)
            browser = None

        if not browser:
            return

        if not self.use_redirect_file:
            uri = self.default_url[len(self.base_url):]

            if self.token:
                uri = url_concat(uri, {'token': self.token})

        if self.file_to_run:
            if not os.path.exists(self.file_to_run):
                self.log.critical(_("%s does not exist") % self.file_to_run)
                self.exit(1)

            relpath = os.path.relpath(self.file_to_run, self.notebook_dir)
            uri = url_escape(url_path_join('notebooks', *relpath.split(os.sep)))

            # Write a temporary file to open in the browser
            fd, open_file = tempfile.mkstemp(suffix='.html')
            with open(fd, 'w', encoding='utf-8') as fh:
                self._write_browser_open_file(uri, fh)
        else:
            open_file = self.browser_open_file

        if self.use_redirect_file:
            assembled_url = urljoin('file:', pathname2url(open_file))
        else:
            assembled_url = url_path_join(self.connection_url, uri)

        b = lambda: browser.open(assembled_url, new=self.webbrowser_open_new)
        threading.Thread(target=b).start()

    def start(self):
        """ Start the Notebook server app, after initialization

        This method takes no arguments so all configuration and initialization
        must be done prior to calling this method."""

        super().start()

        if not self.allow_root:
            # check if we are running as root, and abort if it's not allowed
            try:
                uid = os.geteuid()
            except AttributeError:
                uid = -1 # anything nonzero here, since we can't check UID assume non-root
            if uid == 0:
                self.log.critical(_("Running as root is not recommended. Use --allow-root to bypass."))
                self.exit(1)

        success = self._bind_http_server()
        if not success:
            self.log.critical(_('ERROR: the notebook server could not be started because '
                              'no available port could be found.'))
            self.exit(1)

        info = self.log.info
        for line in self.notebook_info(kernel_count=False).split("\n"):
            info(line)
        info(_("Use Control-C to stop this server and shut down all kernels (twice to skip confirmation)."))
        if 'dev' in notebook.__version__:
            info(_("Welcome to Project Jupyter! Explore the various tools available"
                 " and their corresponding documentation. If you are interested"
                 " in contributing to the platform, please visit the community"
                 "resources section at https://jupyter.org/community.html."))

        self.write_server_info_file()
        self.write_browser_open_file()

        if (self.open_browser or self.file_to_run) and not self.sock:
            self.launch_browser()

        if self.token and self._token_generated:
            # log full URL with generated token, so there's a copy/pasteable link
            # with auth info.
            if self.sock:
                self.log.critical('\n'.join([
                    '\n',
                    'Notebook is listening on %s' % self.display_url,
                    '',
                    (
                        'UNIX sockets are not browser-connectable, but you can tunnel to '
                        'the instance via e.g.`ssh -L 8888:%s -N user@this_host` and then '
                        'open e.g. %s in a browser.'
                    ) % (self.sock, self._concat_token(self._tcp_url('localhost', 8888)))
                ]))
            else:
                if not self.custom_display_url:
                    self.log.critical('\n'.join([
                        '\n',
                        'To access the notebook, open this file in a browser:',
                        '    %s' % urljoin('file:', pathname2url(self.browser_open_file)),
                        'Or copy and paste one of these URLs:',
                        '    %s' % self.display_url,
                    ]))
                else:
                    self.log.critical('\n'.join([
                        '\n',
                        'To access the notebook, open this file in a browser:',
                        '    %s' % urljoin('file:', pathname2url(self.browser_open_file)),
                        'Or copy and paste this URL:',
                        '    %s' % self.display_url,
                    ]))

        self.io_loop = ioloop.IOLoop.current()
        if sys.platform.startswith('win'):
            # add no-op to wake every 5s
            # to handle signals that may be ignored by the inner loop
            pc = ioloop.PeriodicCallback(lambda : None, 5000)
            pc.start()
        try:
            self.io_loop.start()
        except KeyboardInterrupt:
            info(_("Interrupted..."))
        finally:
            self.remove_server_info_file()
            self.remove_browser_open_file()
            self.cleanup_kernels()
            self.cleanup_terminals()

    def stop(self):
        def _stop():
            self.http_server.stop()
            self.io_loop.stop()
        self.io_loop.add_callback(_stop)


def list_running_servers(runtime_dir=None):
    """Iterate over the server info files of running notebook servers.

    Given a runtime directory, find nbserver-* files in the security directory,
    and yield dicts of their information, each one pertaining to
    a currently running notebook server instance.
    """
    if runtime_dir is None:
        runtime_dir = jupyter_runtime_dir()

    # The runtime dir might not exist
    if not os.path.isdir(runtime_dir):
        return

    for file_name in os.listdir(runtime_dir):
        if re.match('nbserver-(.+).json', file_name):
            with open(os.path.join(runtime_dir, file_name), encoding='utf-8') as f:
                info = json.load(f)

            # Simple check whether that process is really still running
            # Also remove leftover files from IPython 2.x without a pid field
            if ('pid' in info) and check_pid(info['pid']):
                yield info
            else:
                # If the process has died, try to delete its info file
                try:
                    os.unlink(os.path.join(runtime_dir, file_name))
                except OSError:
                    pass  # TODO: This should warn or log or something
#-----------------------------------------------------------------------------
# Main entry point
#-----------------------------------------------------------------------------

main = launch_new_instance = NotebookApp.launch_instance
