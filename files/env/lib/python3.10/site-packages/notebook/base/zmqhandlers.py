"""Tornado handlers for WebSocket <-> ZMQ sockets."""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

import json
import struct
import sys
from urllib.parse import urlparse

import tornado
from tornado import gen, ioloop, web
from tornado.iostream import StreamClosedError
from tornado.websocket import WebSocketHandler, WebSocketClosedError

from jupyter_client.session import Session
try:
    from jupyter_client.jsonutil import json_default, extract_dates
except ImportError:
    from jupyter_client.jsonutil import (
        date_default as json_default, extract_dates
    )
from ipython_genutils.py3compat import cast_unicode

from notebook.utils import maybe_future
from .handlers import IPythonHandler


def serialize_binary_message(msg):
    """serialize a message as a binary blob

    Header:

    4 bytes: number of msg parts (nbufs) as 32b int
    4 * nbufs bytes: offset for each buffer as integer as 32b int

    Offsets are from the start of the buffer, including the header.

    Returns
    -------

    The message serialized to bytes.

    """
    # don't modify msg or buffer list in-place
    msg = msg.copy()
    buffers = list(msg.pop('buffers'))
    bmsg = json.dumps(msg, default=json_default).encode('utf8')
    buffers.insert(0, bmsg)
    nbufs = len(buffers)
    offsets = [4 * (nbufs + 1)]
    for buf in buffers[:-1]:
        offsets.append(offsets[-1] + len(buf))
    offsets_buf = struct.pack('!' + 'I' * (nbufs + 1), nbufs, *offsets)
    buffers.insert(0, offsets_buf)
    return b''.join(buffers)


def deserialize_binary_message(bmsg):
    """deserialize a message from a binary blog

    Header:

    4 bytes: number of msg parts (nbufs) as 32b int
    4 * nbufs bytes: offset for each buffer as integer as 32b int

    Offsets are from the start of the buffer, including the header.

    Returns
    -------

    message dictionary
    """
    nbufs = struct.unpack('!i', bmsg[:4])[0]
    offsets = list(struct.unpack('!' + 'I' * nbufs, bmsg[4:4*(nbufs+1)]))
    offsets.append(None)
    bufs = []
    for start, stop in zip(offsets[:-1], offsets[1:]):
        bufs.append(bmsg[start:stop])
    msg = json.loads(bufs[0].decode('utf8'))
    msg['header'] = extract_dates(msg['header'])
    msg['parent_header'] = extract_dates(msg['parent_header'])
    msg['buffers'] = bufs[1:]
    return msg

# ping interval for keeping websockets alive (30 seconds)
WS_PING_INTERVAL = 30000


class WebSocketMixin:
    """Mixin for common websocket options"""
    ping_callback = None
    last_ping = 0
    last_pong = 0
    stream = None

    @property
    def ping_interval(self):
        """The interval for websocket keep-alive pings.

        Set ws_ping_interval = 0 to disable pings.
        """
        return self.settings.get('ws_ping_interval', WS_PING_INTERVAL)

    @property
    def ping_timeout(self):
        """If no ping is received in this many milliseconds,
        close the websocket connection (VPNs, etc. can fail to cleanly close ws connections).
        Default is max of 3 pings or 30 seconds.
        """
        return self.settings.get('ws_ping_timeout',
            max(3 * self.ping_interval, WS_PING_INTERVAL)
        )

    def check_origin(self, origin=None):
        """Check Origin == Host or Access-Control-Allow-Origin.

        Tornado >= 4 calls this method automatically, raising 403 if it returns False.
        """

        if self.allow_origin == '*' or (
            hasattr(self, 'skip_check_origin') and self.skip_check_origin()):
            return True

        host = self.request.headers.get("Host")
        if origin is None:
            origin = self.get_origin()

        # If no origin or host header is provided, assume from script
        if origin is None or host is None:
            return True

        origin = origin.lower()
        origin_host = urlparse(origin).netloc

        # OK if origin matches host
        if origin_host == host:
            return True

        # Check CORS headers
        if self.allow_origin:
            allow = self.allow_origin == origin
        elif self.allow_origin_pat:
            allow = bool(self.allow_origin_pat.match(origin))
        else:
            # No CORS headers deny the request
            allow = False
        if not allow:
            self.log.warning("Blocking Cross Origin WebSocket Attempt.  Origin: %s, Host: %s",
                origin, host,
            )
        return allow

    def clear_cookie(self, *args, **kwargs):
        """meaningless for websockets"""
        pass

    def open(self, *args, **kwargs):
        self.log.debug("Opening websocket %s", self.request.path)

        # start the pinging
        if self.ping_interval > 0:
            loop = ioloop.IOLoop.current()
            self.last_ping = loop.time()  # Remember time of last ping
            self.last_pong = self.last_ping
            self.ping_callback = ioloop.PeriodicCallback(
                self.send_ping, self.ping_interval,
            )
            self.ping_callback.start()
        return super().open(*args, **kwargs)

    def send_ping(self):
        """send a ping to keep the websocket alive"""
        if self.ws_connection is None and self.ping_callback is not None:
            self.ping_callback.stop()
            return

        # check for timeout on pong.  Make sure that we really have sent a recent ping in
        # case the machine with both server and client has been suspended since the last ping.
        now = ioloop.IOLoop.current().time()
        since_last_pong = 1e3 * (now - self.last_pong)
        since_last_ping = 1e3 * (now - self.last_ping)
        if since_last_ping < 2*self.ping_interval and since_last_pong > self.ping_timeout:
            self.log.warning("WebSocket ping timeout after %i ms.", since_last_pong)
            self.close()
            return
        try:
            self.ping(b'')
        except (StreamClosedError, WebSocketClosedError):
            # websocket has been closed, stop pinging
            self.ping_callback.stop()
            return

        self.last_ping = now

    def on_pong(self, data):
        self.last_pong = ioloop.IOLoop.current().time()


class ZMQStreamHandler(WebSocketMixin, WebSocketHandler):

    if tornado.version_info < (4,1):
        """Backport send_error from tornado 4.1 to 4.0"""
        def send_error(self, *args, **kwargs):
            if self.stream is None:
                super(WebSocketHandler, self).send_error(*args, **kwargs)
            else:
                # If we get an uncaught exception during the handshake,
                # we have no choice but to abruptly close the connection.
                # TODO: for uncaught exceptions after the handshake,
                # we can close the connection more gracefully.
                self.stream.close()


    def _reserialize_reply(self, msg_or_list, channel=None):
        """Reserialize a reply message using JSON.

        msg_or_list can be an already-deserialized msg dict or the zmq buffer list.
        If it is the zmq list, it will be deserialized with self.session.

        This takes the msg list from the ZMQ socket and serializes the result for the websocket.
        This method should be used by self._on_zmq_reply to build messages that can
        be sent back to the browser.

        """
        if isinstance(msg_or_list, dict):
            # already unpacked
            msg = msg_or_list
        else:
            idents, msg_list = self.session.feed_identities(msg_or_list)
            msg = self.session.deserialize(msg_list)
        if channel:
            msg['channel'] = channel
        if msg['buffers']:
            buf = serialize_binary_message(msg)
            return buf
        else:
            smsg = json.dumps(msg, default=json_default)
            return cast_unicode(smsg)

    def _on_zmq_reply(self, stream, msg_list):
        # Sometimes this gets triggered when the on_close method is scheduled in the
        # eventloop but hasn't been called.
        if self.ws_connection is None or stream.closed():
            self.log.warning("zmq message arrived on closed channel")
            self.close()
            return
        channel = getattr(stream, 'channel', None)
        try:
            msg = self._reserialize_reply(msg_list, channel=channel)
        except Exception:
            self.log.critical(f"Malformed message: {msg_list!r}", exc_info=True)
            return

        try:
            self.write_message(msg, binary=isinstance(msg, bytes))
        except (StreamClosedError, WebSocketClosedError):
            self.log.warning("zmq message arrived on closed channel")
            self.close()
            return


class AuthenticatedZMQStreamHandler(ZMQStreamHandler, IPythonHandler):

    def set_default_headers(self):
        """Undo the set_default_headers in IPythonHandler

        which doesn't make sense for websockets
        """
        pass

    def pre_get(self):
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

    @gen.coroutine
    def get(self, *args, **kwargs):
        # pre_get can be a coroutine in subclasses
        # assign and yield in two step to avoid tornado 3 issues
        res = self.pre_get()
        yield maybe_future(res)
        res = super().get(*args, **kwargs)
        yield maybe_future(res)

    def initialize(self):
        self.log.debug("Initializing websocket connection %s", self.request.path)
        self.session = Session(config=self.config)

    def get_compression_options(self):
        return self.settings.get('websocket_compression_options', None)
