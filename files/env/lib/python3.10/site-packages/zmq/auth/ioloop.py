"""ZAP Authenticator integrated with the tornado IOLoop.

.. versionadded:: 14.1
"""

# Copyright (C) PyZMQ Developers
# Distributed under the terms of the Modified BSD License.
from typing import Any, Optional

from tornado import ioloop

import zmq
from zmq.eventloop import zmqstream

from .base import Authenticator


class IOLoopAuthenticator(Authenticator):
    """ZAP authentication for use in the tornado IOLoop"""

    zap_stream: zmqstream.ZMQStream
    io_loop: ioloop.IOLoop

    def __init__(
        self,
        context: Optional["zmq.Context"] = None,
        encoding: str = 'utf-8',
        log: Any = None,
        io_loop: Optional[ioloop.IOLoop] = None,
    ):
        super().__init__(context, encoding, log)
        self.zap_stream = None  # type: ignore
        self.io_loop = io_loop or ioloop.IOLoop.current()

    def start(self) -> None:
        """Start ZAP authentication"""
        super().start()
        self.zap_stream = zmqstream.ZMQStream(self.zap_socket, self.io_loop)
        self.zap_stream.on_recv(self.handle_zap_message)

    def stop(self):
        """Stop ZAP authentication"""
        if self.zap_stream:
            self.zap_stream.close()
            self.zap_stream = None
        super().stop()


__all__ = ['IOLoopAuthenticator']
