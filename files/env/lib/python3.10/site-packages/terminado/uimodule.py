"""A Tornado UI module for a terminal backed by terminado.

See the Tornado docs for information on UI modules:
http://www.tornadoweb.org/en/stable/guide/templates.html#ui-modules
"""
# Copyright (c) Jupyter Development Team
# Copyright (c) 2014, Ramalingam Saravanan <sarava@sarava.net>
# Distributed under the terms of the Simplified BSD License.

import os.path

import tornado.web


class Terminal(tornado.web.UIModule):
    def render(self, ws_url, cols=80, rows=25):
        return (
            '<div class="terminado-container" '
            'data-ws-url="{ws_url}" '
            'data-rows="{rows}" data-cols="{cols}"/>'
        ).format(ws_url=ws_url, rows=rows, cols=cols)

    def javascript_files(self):
        # TODO: Can we calculate these dynamically?
        return ["/xstatic/termjs/term.js", "/static/terminado.js"]

    def embedded_javascript(self):
        file = os.path.join(os.path.dirname(__file__), "uimod_embed.js")
        with open(file) as f:
            return f.read()
