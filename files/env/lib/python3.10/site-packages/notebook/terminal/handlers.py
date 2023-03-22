"""Tornado handlers for the terminal emulator."""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

import json
from tornado import web
import terminado
from notebook._tz import utcnow
from ..base.handlers import IPythonHandler
from ..base.zmqhandlers import WebSocketMixin


class TerminalHandler(IPythonHandler):
    """Render the terminal interface."""
    @web.authenticated
    def get(self, term_name):
        self.write(
            self.render_template(
                'terminal.html',
                ws_path=f"terminals/websocket/{term_name}",
            )
        )


class NamedTerminalHandler(IPythonHandler):
    """Creates and renders a named terminal interface."""
    @web.authenticated
    def get(self):
        model = self.terminal_manager.create()
        term_name = model['name']
        new_path = self.request.path.replace("terminals/new", "terminals/" + term_name)
        self.redirect(new_path)


class NewTerminalHandler(IPythonHandler):
    """Creates and renders a terminal interface using the named argument."""
    @web.authenticated
    def get(self, term_name):
        if term_name == 'new':
            raise web.HTTPError(400, "Terminal name 'new' is reserved.")
        new_path = self.request.path.replace(f"new/{term_name}", term_name)
        if term_name in self.terminal_manager.terminals:
            self.set_header('Location', new_path)
            self.set_status(302)
            self.finish(json.dumps(self.terminal_manager.get_terminal_model(term_name)))
            return

        self.terminal_manager.create_with_name(term_name)
        self.redirect(new_path)


class TermSocket(WebSocketMixin, IPythonHandler, terminado.TermSocket):

    def origin_check(self):
        """Terminado adds redundant origin_check

        Tornado already calls check_origin, so don't do anything here.
        """
        return True

    def get(self, *args, **kwargs):
        if not self.get_current_user():
            raise web.HTTPError(403)
        if not args[0] in self.term_manager.terminals:
            raise web.HTTPError(404)
        return super().get(*args, **kwargs)

    def on_message(self, message):
        super().on_message(message)
        self._update_activity()

    def write_message(self, message, binary=False):
        super().write_message(message, binary=binary)
        self._update_activity()

    def _update_activity(self):
        self.application.settings['terminal_last_activity'] = utcnow()
        # terminal may not be around on deletion/cull
        if self.term_name in self.terminal_manager.terminals:
            self.terminal_manager.terminals[self.term_name].last_activity = utcnow()
