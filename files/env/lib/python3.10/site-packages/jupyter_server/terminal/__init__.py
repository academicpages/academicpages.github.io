import os
import sys
from shutil import which

import terminado

from ..utils import check_version

if not check_version(terminado.__version__, "0.8.3"):
    raise ImportError("terminado >= 0.8.3 required, found %s" % terminado.__version__)

from jupyter_server.utils import url_path_join as ujoin

from . import api_handlers
from .handlers import TermSocket
from .terminalmanager import TerminalManager


def initialize(webapp, root_dir, connection_url, settings):
    if os.name == "nt":
        default_shell = "powershell.exe"
    else:
        default_shell = which("sh")  # type:ignore[assignment]
    shell_override = settings.get("shell_command")
    shell = [os.environ.get("SHELL") or default_shell] if shell_override is None else shell_override
    # When the notebook server is not running in a terminal (e.g. when
    # it's launched by a JupyterHub spawner), it's likely that the user
    # environment hasn't been fully set up. In that case, run a login
    # shell to automatically source /etc/profile and the like, unless
    # the user has specifically set a preferred shell command.
    if os.name != "nt" and shell_override is None and not sys.stdout.isatty():
        shell.append("-l")
    terminal_manager = webapp.settings["terminal_manager"] = TerminalManager(
        shell_command=shell,
        extra_env={
            "JUPYTER_SERVER_ROOT": root_dir,
            "JUPYTER_SERVER_URL": connection_url,
        },
        parent=webapp.settings["serverapp"],
    )
    terminal_manager.log = webapp.settings["serverapp"].log
    base_url = webapp.settings["base_url"]
    handlers = [
        (
            ujoin(base_url, r"/terminals/websocket/(\w+)"),
            TermSocket,
            {"term_manager": terminal_manager},
        ),
        (ujoin(base_url, r"/api/terminals"), api_handlers.TerminalRootHandler),
        (ujoin(base_url, r"/api/terminals/(\w+)"), api_handlers.TerminalHandler),
    ]
    webapp.add_handlers(".*$", handlers)
