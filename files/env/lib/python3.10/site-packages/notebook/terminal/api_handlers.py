import json
from tornado import web, gen
from ..base.handlers import APIHandler


class TerminalRootHandler(APIHandler):
    @web.authenticated
    def get(self):
        models = self.terminal_manager.list()
        self.finish(json.dumps(models))

    @web.authenticated
    def post(self):
        """POST /terminals creates a new terminal and redirects to it"""
        model = self.terminal_manager.create()
        self.finish(json.dumps(model))


class TerminalHandler(APIHandler):
    SUPPORTED_METHODS = ('GET', 'DELETE')

    @web.authenticated
    def get(self, name):
        model = self.terminal_manager.get(name)
        self.finish(json.dumps(model))

    @web.authenticated
    @gen.coroutine
    def delete(self, name):
        yield self.terminal_manager.terminate(name, force=True)
        self.set_status(204)
        self.finish()
