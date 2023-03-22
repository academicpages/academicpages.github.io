""" Defines a KernelClient that provides thread-safe sockets with async callbacks on message
replies.
"""
import asyncio
import atexit
import errno
import time
from threading import Event
from threading import Thread
from typing import Any
from typing import Awaitable
from typing import Dict
from typing import List
from typing import Optional
from typing import Union

import zmq
from traitlets import Instance
from traitlets import Type
from zmq import ZMQError
from zmq.eventloop import ioloop
from zmq.eventloop import zmqstream

from .session import Session
from jupyter_client import KernelClient
from jupyter_client.channels import HBChannel

# Local imports
# import ZMQError in top-level namespace, to avoid ugly attribute-error messages
# during garbage collection of threads at exit


async def get_msg(msg: Awaitable) -> Union[List[bytes], List[zmq.Message]]:
    return await msg


class ThreadedZMQSocketChannel(object):
    """A ZMQ socket invoking a callback in the ioloop"""

    session = None
    socket = None
    ioloop = None
    stream = None
    _inspect = None

    def __init__(
        self,
        socket: Optional[zmq.Socket],
        session: Optional[Session],
        loop: Optional[zmq.eventloop.ioloop.ZMQIOLoop],
    ) -> None:
        """Create a channel.

        Parameters
        ----------
        socket : :class:`zmq.Socket`
            The ZMQ socket to use.
        session : :class:`session.Session`
            The session to use.
        loop
            A pyzmq ioloop to connect the socket to using a ZMQStream
        """
        super().__init__()

        self.socket = socket
        self.session = session
        self.ioloop = loop
        evt = Event()

        def setup_stream():
            assert self.socket is not None
            self.stream = zmqstream.ZMQStream(self.socket, self.ioloop)
            self.stream.on_recv(self._handle_recv)  # type:ignore[arg-type]
            evt.set()

        assert self.ioloop is not None
        self.ioloop.add_callback(setup_stream)
        evt.wait()

    _is_alive = False

    def is_alive(self) -> bool:
        return self._is_alive

    def start(self) -> None:
        self._is_alive = True

    def stop(self) -> None:
        self._is_alive = False

    def close(self) -> None:
        if self.socket is not None:
            try:
                self.socket.close(linger=0)
            except Exception:
                pass
            self.socket = None

    def send(self, msg: Dict[str, Any]) -> None:
        """Queue a message to be sent from the IOLoop's thread.

        Parameters
        ----------
        msg : message to send

        This is threadsafe, as it uses IOLoop.add_callback to give the loop's
        thread control of the action.
        """

        def thread_send():
            assert self.session is not None
            self.session.send(self.stream, msg)

        assert self.ioloop is not None
        self.ioloop.add_callback(thread_send)

    def _handle_recv(self, future_msg: Awaitable) -> None:
        """Callback for stream.on_recv.

        Unpacks message, and calls handlers with it.
        """
        assert self.ioloop is not None
        msg_list = self.ioloop._asyncio_event_loop.run_until_complete(get_msg(future_msg))
        assert self.session is not None
        ident, smsg = self.session.feed_identities(msg_list)
        msg = self.session.deserialize(smsg)
        # let client inspect messages
        if self._inspect:
            self._inspect(msg)
        self.call_handlers(msg)

    def call_handlers(self, msg: Dict[str, Any]) -> None:
        """This method is called in the ioloop thread when a message arrives.

        Subclasses should override this method to handle incoming messages.
        It is important to remember that this method is called in the thread
        so that some logic must be done to ensure that the application level
        handlers are called in the application thread.
        """
        pass

    def process_events(self) -> None:
        """Subclasses should override this with a method
        processing any pending GUI events.
        """
        pass

    def flush(self, timeout: float = 1.0) -> None:
        """Immediately processes all pending messages on this channel.

        This is only used for the IOPub channel.

        Callers should use this method to ensure that :meth:`call_handlers`
        has been called for all messages that have been received on the
        0MQ SUB socket of this channel.

        This method is thread safe.

        Parameters
        ----------
        timeout : float, optional
            The maximum amount of time to spend flushing, in seconds. The
            default is one second.
        """
        # We do the IOLoop callback process twice to ensure that the IOLoop
        # gets to perform at least one full poll.
        stop_time = time.time() + timeout
        assert self.ioloop is not None
        for _ in range(2):
            self._flushed = False
            self.ioloop.add_callback(self._flush)
            while not self._flushed and time.time() < stop_time:
                time.sleep(0.01)

    def _flush(self) -> None:
        """Callback for :method:`self.flush`."""
        assert self.stream is not None
        self.stream.flush()
        self._flushed = True


class IOLoopThread(Thread):
    """Run a pyzmq ioloop in a thread to send and receive messages"""

    _exiting = False
    ioloop = None

    def __init__(self):
        super().__init__()
        self.daemon = True

    @staticmethod
    @atexit.register
    def _notice_exit() -> None:
        # Class definitions can be torn down during interpreter shutdown.
        # We only need to set _exiting flag if this hasn't happened.
        if IOLoopThread is not None:
            IOLoopThread._exiting = True

    def start(self) -> None:
        """Start the IOLoop thread

        Don't return until self.ioloop is defined,
        which is created in the thread
        """
        self._start_event = Event()
        Thread.start(self)
        self._start_event.wait()

    def run(self) -> None:
        """Run my loop, ignoring EINTR events in the poller"""
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        self.ioloop = ioloop.IOLoop()
        self.ioloop._asyncio_event_loop = loop
        # signal that self.ioloop is defined
        self._start_event.set()
        while True:
            try:
                self.ioloop.start()
            except ZMQError as e:
                if e.errno == errno.EINTR:
                    continue
                else:
                    raise
            except Exception:
                if self._exiting:
                    break
                else:
                    raise
            else:
                break

    def stop(self) -> None:
        """Stop the channel's event loop and join its thread.

        This calls :meth:`~threading.Thread.join` and returns when the thread
        terminates. :class:`RuntimeError` will be raised if
        :meth:`~threading.Thread.start` is called again.
        """
        if self.ioloop is not None:
            self.ioloop.add_callback(self.ioloop.stop)
        self.join()
        self.close()
        self.ioloop = None

    def __del__(self):
        self.close()

    def close(self) -> None:
        if self.ioloop is not None:
            try:
                self.ioloop.close(all_fds=True)
            except Exception:
                pass


class ThreadedKernelClient(KernelClient):
    """A KernelClient that provides thread-safe sockets with async callbacks on message replies."""

    @property
    def ioloop(self):
        return self.ioloop_thread.ioloop

    ioloop_thread = Instance(IOLoopThread, allow_none=True)

    def start_channels(
        self,
        shell: bool = True,
        iopub: bool = True,
        stdin: bool = True,
        hb: bool = True,
        control: bool = True,
    ) -> None:
        self.ioloop_thread = IOLoopThread()
        self.ioloop_thread.start()

        if shell:
            self.shell_channel._inspect = self._check_kernel_info_reply

        super().start_channels(shell, iopub, stdin, hb, control)

    def _check_kernel_info_reply(self, msg: Dict[str, Any]) -> None:
        """This is run in the ioloop thread when the kernel info reply is received"""
        if msg["msg_type"] == "kernel_info_reply":
            self._handle_kernel_info_reply(msg)
            self.shell_channel._inspect = None

    def stop_channels(self) -> None:
        super().stop_channels()
        if self.ioloop_thread.is_alive():
            self.ioloop_thread.stop()

    iopub_channel_class = Type(ThreadedZMQSocketChannel)
    shell_channel_class = Type(ThreadedZMQSocketChannel)
    stdin_channel_class = Type(ThreadedZMQSocketChannel)
    hb_channel_class = Type(HBChannel)
    control_channel_class = Type(ThreadedZMQSocketChannel)

    def is_alive(self) -> bool:
        """Is the kernel process still running?"""
        if self._hb_channel is not None:
            # We don't have access to the KernelManager,
            # so we use the heartbeat.
            return self._hb_channel.is_beating()
        # no heartbeat and not local, we can't tell if it's running,
        # so naively return True
        return True
