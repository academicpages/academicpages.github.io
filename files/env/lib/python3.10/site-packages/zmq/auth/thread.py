"""ZAP Authenticator in a Python Thread.

.. versionadded:: 14.1
"""

# Copyright (C) PyZMQ Developers
# Distributed under the terms of the Modified BSD License.

import logging
from itertools import chain
from threading import Event, Thread
from typing import Any, Dict, List, Optional, TypeVar, cast

import zmq
from zmq.utils import jsonapi

from .base import Authenticator


class AuthenticationThread(Thread):
    """A Thread for running a zmq Authenticator

    This is run in the background by ThreadedAuthenticator
    """

    def __init__(
        self,
        context: "zmq.Context",
        endpoint: str,
        encoding: str = 'utf-8',
        log: Any = None,
        authenticator: Optional[Authenticator] = None,
    ) -> None:
        super().__init__()
        self.context = context or zmq.Context.instance()
        self.encoding = encoding
        self.log = log = log or logging.getLogger('zmq.auth')
        self.started = Event()
        self.authenticator: Authenticator = authenticator or Authenticator(
            context, encoding=encoding, log=log
        )

        # create a socket to communicate back to main thread.
        self.pipe = context.socket(zmq.PAIR)
        self.pipe.linger = 1
        self.pipe.connect(endpoint)

    def run(self) -> None:
        """Start the Authentication Agent thread task"""
        self.authenticator.start()
        self.started.set()
        zap = self.authenticator.zap_socket
        poller = zmq.Poller()
        poller.register(self.pipe, zmq.POLLIN)
        poller.register(zap, zmq.POLLIN)
        while True:
            try:
                socks = dict(poller.poll())
            except zmq.ZMQError:
                break  # interrupted

            if self.pipe in socks and socks[self.pipe] == zmq.POLLIN:
                # Make sure all API requests are processed before
                # looking at the ZAP socket.
                while True:
                    try:
                        msg = self.pipe.recv_multipart(flags=zmq.NOBLOCK)
                    except zmq.Again:
                        break

                    terminate = self._handle_pipe(msg)
                    if terminate:
                        break
                if terminate:
                    break

            if zap in socks and socks[zap] == zmq.POLLIN:
                self._handle_zap()

        self.pipe.close()
        self.authenticator.stop()

    def _handle_zap(self) -> None:
        """
        Handle a message from the ZAP socket.
        """
        if self.authenticator.zap_socket is None:
            raise RuntimeError("ZAP socket closed")
        msg = self.authenticator.zap_socket.recv_multipart()
        if not msg:
            return
        self.authenticator.handle_zap_message(msg)

    def _handle_pipe(self, msg: List[bytes]) -> bool:
        """
        Handle a message from front-end API.
        """
        terminate = False

        if msg is None:
            terminate = True
            return terminate

        command = msg[0]
        self.log.debug("auth received API command %r", command)

        if command == b'ALLOW':
            addresses = [m.decode(self.encoding) for m in msg[1:]]
            try:
                self.authenticator.allow(*addresses)
            except Exception:
                self.log.exception("Failed to allow %s", addresses)

        elif command == b'DENY':
            addresses = [m.decode(self.encoding) for m in msg[1:]]
            try:
                self.authenticator.deny(*addresses)
            except Exception:
                self.log.exception("Failed to deny %s", addresses)

        elif command == b'PLAIN':
            domain = msg[1].decode(self.encoding)
            json_passwords = msg[2]
            passwords: Dict[str, str] = cast(
                Dict[str, str], jsonapi.loads(json_passwords)
            )
            self.authenticator.configure_plain(domain, passwords)

        elif command == b'CURVE':
            # For now we don't do anything with domains
            domain = msg[1].decode(self.encoding)

            # If location is CURVE_ALLOW_ANY, allow all clients. Otherwise
            # treat location as a directory that holds the certificates.
            location = msg[2].decode(self.encoding)
            self.authenticator.configure_curve(domain, location)

        elif command == b'TERMINATE':
            terminate = True

        else:
            self.log.error("Invalid auth command from API: %r", command)

        return terminate


T = TypeVar("T", bound=type)


def _inherit_docstrings(cls: T) -> T:
    """inherit docstrings from Authenticator, so we don't duplicate them"""
    for name, method in cls.__dict__.items():
        if name.startswith('_') or not callable(method):
            continue
        upstream_method = getattr(Authenticator, name, None)
        if not method.__doc__:
            method.__doc__ = upstream_method.__doc__
    return cls


@_inherit_docstrings
class ThreadAuthenticator:
    """Run ZAP authentication in a background thread"""

    context: "zmq.Context"
    log: Any
    encoding: str
    pipe: "zmq.Socket"
    pipe_endpoint: str = ''
    thread: AuthenticationThread

    def __init__(
        self,
        context: Optional["zmq.Context"] = None,
        encoding: str = 'utf-8',
        log: Any = None,
    ):
        self.log = log
        self.encoding = encoding
        self.pipe = None  # type: ignore
        self.pipe_endpoint = f"inproc://{id(self)}.inproc"
        self.thread = None  # type: ignore
        self.context = context or zmq.Context.instance()

    # proxy base Authenticator attributes

    def __setattr__(self, key: str, value: Any):
        for obj in chain([self], self.__class__.mro()):
            if key in obj.__dict__ or (key in getattr(obj, "__annotations__", {})):
                object.__setattr__(self, key, value)
                return
        setattr(self.thread.authenticator, key, value)

    def __getattr__(self, key: str):
        return getattr(self.thread.authenticator, key)

    def allow(self, *addresses: str):
        self.pipe.send_multipart(
            [b'ALLOW'] + [a.encode(self.encoding) for a in addresses]
        )

    def deny(self, *addresses: str):
        self.pipe.send_multipart(
            [b'DENY'] + [a.encode(self.encoding) for a in addresses]
        )

    def configure_plain(
        self, domain: str = '*', passwords: Optional[Dict[str, str]] = None
    ):
        self.pipe.send_multipart(
            [b'PLAIN', domain.encode(self.encoding), jsonapi.dumps(passwords or {})]
        )

    def configure_curve(self, domain: str = '*', location: str = ''):
        domain = domain.encode(self.encoding)
        location = location.encode(self.encoding)
        self.pipe.send_multipart([b'CURVE', domain, location])

    def configure_curve_callback(
        self, domain: str = '*', credentials_provider: Any = None
    ):
        self.thread.authenticator.configure_curve_callback(
            domain, credentials_provider=credentials_provider
        )

    def start(self) -> None:
        """Start the authentication thread"""
        # create a socket to communicate with auth thread.
        self.pipe = self.context.socket(zmq.PAIR)
        self.pipe.linger = 1
        self.pipe.bind(self.pipe_endpoint)
        self.thread = AuthenticationThread(
            self.context, self.pipe_endpoint, encoding=self.encoding, log=self.log
        )
        self.thread.start()
        if not self.thread.started.wait(timeout=10):
            raise RuntimeError("Authenticator thread failed to start")

    def stop(self) -> None:
        """Stop the authentication thread"""
        if self.pipe:
            self.pipe.send(b'TERMINATE')
            if self.is_alive():
                self.thread.join()
            self.thread = None  # type: ignore
            self.pipe.close()
            self.pipe = None  # type: ignore

    def is_alive(self) -> bool:
        """Is the ZAP thread currently running?"""
        if self.thread and self.thread.is_alive():
            return True
        return False

    def __del__(self) -> None:
        self.stop()


__all__ = ['ThreadAuthenticator']
