"""tornado IOLoop API with zmq compatibility

This module is deprecated in pyzmq 17.
To use zmq with tornado,
eventloop integration is no longer required
and tornado itself should be used.
"""

# Copyright (C) PyZMQ Developers
# Distributed under the terms of the Modified BSD License.


import time
import warnings
from typing import Any

try:
    import tornado
    from tornado import ioloop
    from tornado.log import gen_log

    if not hasattr(ioloop.IOLoop, 'configurable_default'):
        raise ImportError(
            "Tornado too old: %s" % getattr(tornado, 'version', 'unknown')
        )
except ImportError:
    from .minitornado import ioloop  # type: ignore
    from .minitornado.log import gen_log  # type: ignore

PeriodicCallback = ioloop.PeriodicCallback  # type: ignore


class DelayedCallback(PeriodicCallback):  # type: ignore
    """Schedules the given callback to be called once.

    The callback is called once, after callback_time milliseconds.

    `start` must be called after the DelayedCallback is created.

    The timeout is calculated from when `start` is called.
    """

    def __init__(self, callback, callback_time, io_loop=None):
        # PeriodicCallback require callback_time to be positive
        warnings.warn(
            """DelayedCallback is deprecated.
        Use loop.add_timeout instead.""",
            DeprecationWarning,
        )
        callback_time = max(callback_time, 1e-3)
        super().__init__(callback, callback_time, io_loop)

    def start(self):
        """Starts the timer."""
        self._running = True
        self._firstrun = True
        self._next_timeout = time.time() + self.callback_time / 1000.0
        self.io_loop.add_timeout(self._next_timeout, self._run)

    def _run(self):
        if not self._running:
            return
        self._running = False
        try:
            self.callback()
        except Exception:
            gen_log.error("Error in delayed callback", exc_info=True)


def _deprecated():
    if _deprecated.called:  # type: ignore
        return
    _deprecated.called = True  # type: ignore
    warnings.warn(
        "zmq.eventloop.ioloop is deprecated in pyzmq 17."
        " pyzmq now works with default tornado and asyncio eventloops.",
        DeprecationWarning,
        stacklevel=3,
    )


_deprecated.called = False  # type: ignore

_IOLoop: Any
# resolve 'true' default loop
if '.minitornado.' in ioloop.__name__:
    from ._deprecated import ZMQIOLoop as _IOLoop  # type: ignore
else:
    _IOLoop = ioloop.IOLoop
    while _IOLoop.configurable_default() is not _IOLoop:
        _IOLoop = _IOLoop.configurable_default()


class ZMQIOLoop(_IOLoop):
    """DEPRECATED: No longer needed as of pyzmq-17

    PyZMQ tornado integration now works with the default :mod:`tornado.ioloop.IOLoop`.
    """

    def __init__(self, *args, **kwargs):
        _deprecated()
        # super is object, which takes no args
        return super().__init__()

    @classmethod
    def instance(cls, *args, **kwargs):
        """Returns a global `IOLoop` instance.

        Most applications have a single, global `IOLoop` running on the
        main thread.  Use this method to get this instance from
        another thread.  To get the current thread's `IOLoop`, use `current()`.
        """
        # install ZMQIOLoop as the active IOLoop implementation
        # when using tornado 3
        ioloop.IOLoop.configure(cls)
        _deprecated()
        loop = ioloop.IOLoop.instance(*args, **kwargs)
        return loop

    @classmethod
    def current(cls, *args, **kwargs):
        """Returns the current thread’s IOLoop."""
        # install ZMQIOLoop as the active IOLoop implementation
        # when using tornado 3
        ioloop.IOLoop.configure(cls)
        _deprecated()
        loop = ioloop.IOLoop.current(*args, **kwargs)
        return loop


# public API name
IOLoop = ZMQIOLoop


def install():
    """DEPRECATED

    pyzmq 17 no longer needs any special integration for tornado.
    """
    _deprecated()
    ioloop.IOLoop.configure(ZMQIOLoop)


# if minitornado is used, fallback on deprecated ZMQIOLoop, install implementations
if '.minitornado.' in ioloop.__name__:
    from ._deprecated import IOLoop, ZMQIOLoop, install  # type: ignore # noqa
