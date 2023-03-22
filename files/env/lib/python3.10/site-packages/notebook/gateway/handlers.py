# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

import os
import logging
import mimetypes
import random

from ..base.handlers import APIHandler, IPythonHandler
from ..utils import url_path_join

from tornado import gen, web
from tornado.concurrent import Future
from tornado.ioloop import IOLoop, PeriodicCallback
from tornado.websocket import WebSocketHandler, websocket_connect
from tornado.httpclient import HTTPRequest
from tornado.escape import url_escape, json_decode, utf8

from ipython_genutils.py3compat import cast_unicode
from jupyter_client.session import Session
from traitlets.config.configurable import LoggingConfigurable

from .managers import GatewayClient

# Keepalive ping interval (default: 30 seconds)
GATEWAY_WS_PING_INTERVAL_SECS = int(os.getenv('GATEWAY_WS_PING_INTERVAL_SECS', 30))


class WebSocketChannelsHandler(WebSocketHandler, IPythonHandler):

    session = None
    gateway = None
    kernel_id = None
    ping_callback = None

    def check_origin(self, origin=None):
        return IPythonHandler.check_origin(self, origin)

    def set_default_headers(self):
        """Undo the set_default_headers in IPythonHandler which doesn't make sense for websockets"""
        pass

    def get_compression_options(self):
        # use deflate compress websocket
        return {}

    def authenticate(self):
        """Run before finishing the GET request

        Extend this method to add logic that should fire before
        the websocket finishes completing.
        """
        # authenticate the request before opening the websocket
        if self.get_current_user() is None:
            self.log.warning("Couldn't authenticate WebSocket connection")
            raise web.HTTPError(403)

        if self.get_argument('session_id', False):
            self.session.session = cast_unicode(self.get_argument('session_id'))
        else:
            self.log.warning("No session ID specified")

    def initialize(self):
        self.log.debug("Initializing websocket connection %s", self.request.path)
        self.session = Session(config=self.config)
        self.gateway = GatewayWebSocketClient(gateway_url=GatewayClient.instance().url)

    @gen.coroutine
    def get(self, kernel_id, *args, **kwargs):
        self.authenticate()
        self.kernel_id = cast_unicode(kernel_id, 'ascii')
        yield super().get(kernel_id=kernel_id, *args, **kwargs)

    def send_ping(self):
        if self.ws_connection is None and self.ping_callback is not None:
            self.ping_callback.stop()
            return

        self.ping(b'')

    def open(self, kernel_id, *args, **kwargs):
        """Handle web socket connection open to notebook server and delegate to gateway web socket handler """
        self.ping_callback = PeriodicCallback(self.send_ping, GATEWAY_WS_PING_INTERVAL_SECS * 1000)
        self.ping_callback.start()

        self.gateway.on_open(
            kernel_id=kernel_id,
            message_callback=self.write_message,
            compression_options=self.get_compression_options()
        )

    def on_message(self, message):
        """Forward message to gateway web socket handler."""
        self.gateway.on_message(message)

    def write_message(self, message, binary=False):
        """Send message back to notebook client.  This is called via callback from self.gateway._read_messages."""
        if self.ws_connection:  # prevent WebSocketClosedError
            if isinstance(message, bytes):
                binary = True
            super().write_message(message, binary=binary)
        elif self.log.isEnabledFor(logging.DEBUG):
            msg_summary = WebSocketChannelsHandler._get_message_summary(json_decode(utf8(message)))
            self.log.debug(f"Notebook client closed websocket connection - message dropped: {msg_summary}")

    def on_close(self):
        self.log.debug("Closing websocket connection %s", self.request.path)
        self.gateway.on_close()
        super().on_close()

    @staticmethod
    def _get_message_summary(message):
        summary = []
        message_type = message['msg_type']
        summary.append(f'type: {message_type}')

        if message_type == 'status':
            summary.append(f', state: {message["content"]["execution_state"]}')
        elif message_type == 'error':
            summary.append(
                f', {message["content"]["ename"]}:'
                f'{message["content"]["evalue"]}:'
                f'{message["content"]["traceback"]}'
            )
        else:
            summary.append(', ...')  # don't display potentially sensitive data

        return ''.join(summary)


class GatewayWebSocketClient(LoggingConfigurable):
    """Proxy web socket connection to a kernel/enterprise gateway."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.kernel_id = None
        self.ws = None
        self.ws_future = Future()
        self.disconnected = False
        self.retry = 0

    @gen.coroutine
    def _connect(self, kernel_id):
        # websocket is initialized before connection
        self.ws = None
        self.kernel_id = kernel_id
        ws_url = url_path_join(
            GatewayClient.instance().ws_url,
            GatewayClient.instance().kernels_endpoint, url_escape(kernel_id), 'channels'
        )
        self.log.info(f'Connecting to {ws_url}')
        kwargs = {}
        kwargs = GatewayClient.instance().load_connection_args(**kwargs)

        request = HTTPRequest(ws_url, **kwargs)
        self.ws_future = websocket_connect(request)
        self.ws_future.add_done_callback(self._connection_done)

    def _connection_done(self, fut):
        if not self.disconnected and fut.exception() is None:  # prevent concurrent.futures._base.CancelledError
            self.ws = fut.result()
            self.retry = 0
            self.log.debug(f"Connection is ready: ws: {self.ws}")
        else:
            self.log.warning("Websocket connection has been closed via client disconnect or due to error.  "
                             "Kernel with ID '{}' may not be terminated on GatewayClient: {}".
                             format(self.kernel_id, GatewayClient.instance().url))

    def _disconnect(self):
        self.disconnected = True
        if self.ws is not None:
            # Close connection
            self.ws.close()
        elif not self.ws_future.done():
            # Cancel pending connection.  Since future.cancel() is a noop on tornado, we'll track cancellation locally
            self.ws_future.cancel()
            self.log.debug(f"_disconnect: future cancelled, disconnected: {self.disconnected}")

    @gen.coroutine
    def _read_messages(self, callback):
        """Read messages from gateway server."""
        while self.ws is not None:
            message = None
            if not self.disconnected:
                try:
                    message = yield self.ws.read_message()
                except Exception as e:
                    self.log.error(f"Exception reading message from websocket: {e}")  # , exc_info=True)
                if message is None:
                    if not self.disconnected:
                        self.log.warning(f"Lost connection to Gateway: {self.kernel_id}")
                    break
                callback(message)  # pass back to notebook client (see self.on_open and WebSocketChannelsHandler.open)
            else:  # ws cancelled - stop reading
                break

        # NOTE(esevan): if websocket is not disconnected by client, try to reconnect.
        if not self.disconnected and self.retry < GatewayClient.instance().gateway_retry_max:
            jitter = random.randint(10, 100) * 0.01
            retry_interval = min(GatewayClient.instance().gateway_retry_interval * (2 ** self.retry),
                                 GatewayClient.instance().gateway_retry_interval_max) + jitter
            self.retry += 1
            self.log.info("Attempting to re-establish the connection to Gateway in %s secs (%s/%s): %s",
                          retry_interval, self.retry, GatewayClient.instance().gateway_retry_max, self.kernel_id)
            yield gen.sleep(retry_interval)
            self._connect(self.kernel_id)
            loop = IOLoop.current()
            loop.add_future(self.ws_future, lambda future: self._read_messages(callback))

    def on_open(self, kernel_id, message_callback, **kwargs):
        """Web socket connection open against gateway server."""
        self._connect(kernel_id)
        loop = IOLoop.current()
        loop.add_future(
            self.ws_future,
            lambda future: self._read_messages(message_callback)
        )

    def on_message(self, message):
        """Send message to gateway server."""
        if self.ws is None:
            loop = IOLoop.current()
            loop.add_future(
                self.ws_future,
                lambda future: self._write_message(message)
            )
        else:
            self._write_message(message)

    def _write_message(self, message):
        """Send message to gateway server."""
        try:
            if not self.disconnected and self.ws is not None:
                self.ws.write_message(message)
        except Exception as e:
            self.log.error(f"Exception writing message to websocket: {e}")  # , exc_info=True)

    def on_close(self):
        """Web socket closed event."""
        self._disconnect()


class GatewayResourceHandler(APIHandler):
    """Retrieves resources for specific kernelspec definitions from kernel/enterprise gateway."""

    @web.authenticated
    @gen.coroutine
    def get(self, kernel_name, path, include_body=True):
        ksm = self.kernel_spec_manager
        kernel_spec_res = yield ksm.get_kernel_spec_resource(kernel_name, path)
        if kernel_spec_res is None:
            self.log.warning(
                f"Kernelspec resource '{path}' for '{kernel_name}' not found.  "
                f"Gateway may not support resource serving."
            )
        else:
            self.set_header("Content-Type", mimetypes.guess_type(path)[0])
        self.finish(kernel_spec_res)


from ..services.kernels.handlers import _kernel_id_regex
from ..services.kernelspecs.handlers import kernel_name_regex

default_handlers = [
    (fr"/api/kernels/{_kernel_id_regex}/channels", WebSocketChannelsHandler),
    (fr"/kernelspecs/{kernel_name_regex}/(?P<path>.*)", GatewayResourceHandler),
]
