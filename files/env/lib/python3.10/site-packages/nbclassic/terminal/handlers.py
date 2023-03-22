#encoding: utf-8
"""Tornado handlers for the terminal emulator."""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

from tornado import web
from jupyter_server.base.handlers import JupyterHandler
from jupyter_server.extension.handler import (
    ExtensionHandlerMixin,
    ExtensionHandlerJinjaMixin
)

class TerminalHandler(ExtensionHandlerJinjaMixin, ExtensionHandlerMixin, JupyterHandler):
    """Render the terminal interface."""
    @web.authenticated
    def get(self, term_name):
        if term_name not in self.terminal_manager.terminals:
            self.terminal_manager.create(name=term_name)
        self.write(self.render_template('terminal.html',
                   ws_path="terminals/websocket/%s" % term_name))
