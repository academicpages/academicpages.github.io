"""Tornado handlers for WebSocket <-> ZMQ sockets."""
# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
import json
import re
import struct
import sys
from typing import Optional, no_type_check
from urllib.parse import urlparse

import tornado

try:
    from jupyter_client.jsonutil import json_default
except ImportError:
    from jupyter_client.jsonutil import date_default as json_default

from jupyter_client.jsonutil import extract_dates
from jupyter_client.session import Session
from tornado import ioloop, web
from tornado.iostream import IOStream
from tornado.websocket import WebSocketHandler

from .handlers import JupyterHandler


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
    buffers = list(msg.pop("buffers"))
    if sys.version_info < (3, 4):
        buffers = [x.tobytes() for x in buffers]
    bmsg = json.dumps(msg, default=json_default).encode("utf8")
    buffers.insert(0, bmsg)
    nbufs = len(buffers)
    offsets = [4 * (nbufs + 1)]
    for buf in buffers[:-1]:
        offsets.append(offsets[-1] + len(buf))
    offsets_buf = struct.pack("!" + "I" * (nbufs + 1), nbufs, *offsets)
    buffers.insert(0, offsets_buf)
    return b"".join(buffers)


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
    nbufs = struct.unpack("!i", bmsg[:4])[0]
    offsets = list(struct.unpack("!" + "I" * nbufs, bmsg[4 : 4 * (nbufs + 1)]))
    offsets.append(None)
    bufs = []
    for start, stop in zip(offsets[:-1], offsets[1:]):
        bufs.append(bmsg[start:stop])
    msg = json.loads(bufs[0].decode("utf8"))
    msg["header"] = extract_dates(msg["header"])
    msg["parent_header"] = extract_dates(msg["parent_header"])
    msg["buffers"] = bufs[1:]
    return msg


def serialize_msg_to_ws_v1(msg_or_list, channel, pack=None):
    if pack:
        msg_list = [
            pack(msg_or_list["header"]),
            pack(msg_or_list["parent_header"]),
            pack(msg_or_list["metadata"]),
            pack(msg_or_list["content"]),
        ]
    else:
        msg_list = msg_or_list
    channel = channel.encode("utf-8")
    offsets: list = []
    offsets.append(8 * (1 + 1 + len(msg_list) + 1))
    offsets.append(len(channel) + offsets[-1])
    for msg in msg_list:
        offsets.append(len(msg) + offsets[-1])
    offset_number = len(offsets).to_bytes(8, byteorder="little")
    offsets = [offset.to_bytes(8, byteorder="little") for offset in offsets]
    bin_msg = b"".join([offset_number] + offsets + [channel] + msg_list)
    return bin_msg


def deserialize_msg_from_ws_v1(ws_msg):
    offset_number = int.from_bytes(ws_msg[:8], "little")
    offsets = [
        int.from_bytes(ws_msg[8 * (i + 1) : 8 * (i + 2)], "little") for i in range(offset_number)
    ]
    channel = ws_msg[offsets[0] : offsets[1]].decode("utf-8")
    msg_list = [ws_msg[offsets[i] : offsets[i + 1]] for i in range(1, offset_number - 1)]
    return channel, msg_list


# ping interval for keeping websockets alive (30 seconds)
WS_PING_INTERVAL = 30000


class WebSocketMixin:
    """Mixin for common websocket options"""

    ping_callback = None
    last_ping = 0.0
    last_pong = 0.0
    stream = None  # type: Optional[IOStream]

    @property
    def ping_interval(self):
        """The interval for websocket keep-alive pings.

        Set ws_ping_interval = 0 to disable pings.
        """
        return self.settings.get("ws_ping_interval", WS_PING_INTERVAL)  # type:ignore[attr-defined]

    @property
    def ping_timeout(self):
        """If no ping is received in this many milliseconds,
        close the websocket connection (VPNs, etc. can fail to cleanly close ws connections).
        Default is max of 3 pings or 30 seconds.
        """
        return self.settings.get(  # type:ignore[attr-defined]
            "ws_ping_timeout", max(3 * self.ping_interval, WS_PING_INTERVAL)
        )

    @no_type_check
    def check_origin(self, origin: Optional[str] = None) -> bool:
        """Check Origin == Host or Access-Control-Allow-Origin.

        Tornado >= 4 calls this method automatically, raising 403 if it returns False.
        """

        if self.allow_origin == "*" or (
            hasattr(self, "skip_check_origin") and self.skip_check_origin()
        ):
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
            allow = bool(re.match(self.allow_origin_pat, origin))
        else:
            # No CORS headers deny the request
            allow = False
        if not allow:
            self.log.warning(
                "Blocking Cross Origin WebSocket Attempt.  Origin: %s, Host: %s",
                origin,
                host,
            )
        return allow

    def clear_cookie(self, *args, **kwargs):
        """meaningless for websockets"""
        pass

    @no_type_check
    def open(self, *args, **kwargs):
        self.log.debug("Opening websocket %s", self.request.path)

        # start the pinging
        if self.ping_interval > 0:
            loop = ioloop.IOLoop.current()
            self.last_ping = loop.time()  # Remember time of last ping
            self.last_pong = self.last_ping
            self.ping_callback = ioloop.PeriodicCallback(
                self.send_ping,
                self.ping_interval,
            )
            self.ping_callback.start()
        return super().open(*args, **kwargs)

    @no_type_check
    def send_ping(self):
        """send a ping to keep the websocket alive"""
        if self.ws_connection is None and self.ping_callback is not None:
            self.ping_callback.stop()
            return

        if self.ws_connection.client_terminated:
            self.close()
            return

        # check for timeout on pong.  Make sure that we really have sent a recent ping in
        # case the machine with both server and client has been suspended since the last ping.
        now = ioloop.IOLoop.current().time()
        since_last_pong = 1e3 * (now - self.last_pong)
        since_last_ping = 1e3 * (now - self.last_ping)
        if since_last_ping < 2 * self.ping_interval and since_last_pong > self.ping_timeout:
            self.log.warning("WebSocket ping timeout after %i ms.", since_last_pong)
            self.close()
            return

        self.ping(b"")
        self.last_ping = now

    def on_pong(self, data):
        self.last_pong = ioloop.IOLoop.current().time()


class ZMQStreamHandler(WebSocketMixin, WebSocketHandler):

    if tornado.version_info < (4, 1):
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
            msg["channel"] = channel
        if msg["buffers"]:
            buf = serialize_binary_message(msg)
            return buf
        else:
            return json.dumps(msg, default=json_default)

    def select_subprotocol(self, subprotocols):
        preferred_protocol = self.settings.get("kernel_ws_protocol")
        if preferred_protocol is None:
            preferred_protocol = "v1.kernel.websocket.jupyter.org"
        elif preferred_protocol == "":
            preferred_protocol = None
        selected_subprotocol = preferred_protocol if preferred_protocol in subprotocols else None
        # None is the default, "legacy" protocol
        return selected_subprotocol

    def _on_zmq_reply(self, stream, msg_list):
        # Sometimes this gets triggered when the on_close method is scheduled in the
        # eventloop but hasn't been called.
        if self.ws_connection is None or stream.closed():
            self.log.warning("zmq message arrived on closed channel")
            self.close()
            return
        channel = getattr(stream, "channel", None)
        if self.selected_subprotocol == "v1.kernel.websocket.jupyter.org":
            bin_msg = serialize_msg_to_ws_v1(msg_list, channel)
            self.write_message(bin_msg, binary=True)
        else:
            try:
                msg = self._reserialize_reply(msg_list, channel=channel)
            except Exception:
                self.log.critical("Malformed message: %r" % msg_list, exc_info=True)
            else:
                self.write_message(msg, binary=isinstance(msg, bytes))


class AuthenticatedZMQStreamHandler(ZMQStreamHandler, JupyterHandler):
    def set_default_headers(self):
        """Undo the set_default_headers in JupyterHandler

        which doesn't make sense for websockets
        """
        pass

    def pre_get(self):
        """Run before finishing the GET request

        Extend this method to add logic that should fire before
        the websocket finishes completing.
        """
        # authenticate the request before opening the websocket
        user = self.get_current_user()
        if user is None:
            self.log.warning("Couldn't authenticate WebSocket connection")
            raise web.HTTPError(403)

        # authorize the user.
        if not self.authorizer.is_authorized(self, user, "execute", "kernels"):
            raise web.HTTPError(403)

        if self.get_argument("session_id", None):
            self.session.session = self.get_argument("session_id")
        else:
            self.log.warning("No session ID specified")

    async def get(self, *args, **kwargs):
        # pre_get can be a coroutine in subclasses
        # assign and yield in two step to avoid tornado 3 issues
        res = self.pre_get()
        await res
        res = super().get(*args, **kwargs)
        await res

    def initialize(self):
        self.log.debug("Initializing websocket connection %s", self.request.path)
        self.session = Session(config=self.config)

    def get_compression_options(self):
        return self.settings.get("websocket_compression_options", None)
