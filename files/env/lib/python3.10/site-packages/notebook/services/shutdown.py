"""HTTP handler to shut down the notebook server.
"""
from tornado import web, ioloop
from notebook.base.handlers import IPythonHandler

class ShutdownHandler(IPythonHandler):
    @web.authenticated
    def post(self):
        self.log.info("Shutting down on /api/shutdown request.")
        ioloop.IOLoop.current().stop()


default_handlers = [
    (r"/api/shutdown", ShutdownHandler),
]
