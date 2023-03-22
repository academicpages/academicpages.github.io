"""Tornado handlers for api specifications."""
# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
import json
import os

from tornado import web

from jupyter_server._tz import isoformat, utcfromtimestamp
from jupyter_server.auth import authorized
from jupyter_server.utils import ensure_async

from ...base.handlers import APIHandler, JupyterHandler

AUTH_RESOURCE = "api"


class APISpecHandler(web.StaticFileHandler, JupyterHandler):
    auth_resource = AUTH_RESOURCE

    def initialize(self):
        web.StaticFileHandler.initialize(self, path=os.path.dirname(__file__))

    @web.authenticated
    @authorized
    def get(self):
        self.log.warning("Serving api spec (experimental, incomplete)")
        return web.StaticFileHandler.get(self, "api.yaml")

    def get_content_type(self):
        return "text/x-yaml"


class APIStatusHandler(APIHandler):

    auth_resource = AUTH_RESOURCE
    _track_activity = False

    @web.authenticated
    @authorized
    async def get(self):
        # if started was missing, use unix epoch
        started = self.settings.get("started", utcfromtimestamp(0))
        started = isoformat(started)

        kernels = await ensure_async(self.kernel_manager.list_kernels())
        total_connections = sum(k["connections"] for k in kernels)
        last_activity = isoformat(self.application.last_activity())
        model = {
            "started": started,
            "last_activity": last_activity,
            "kernels": len(kernels),
            "connections": total_connections,
        }
        self.finish(json.dumps(model, sort_keys=True))


default_handlers = [
    (r"/api/spec.yaml", APISpecHandler),
    (r"/api/status", APIStatusHandler),
]
