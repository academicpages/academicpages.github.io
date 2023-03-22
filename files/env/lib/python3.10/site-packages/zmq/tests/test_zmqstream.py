# Copyright (C) PyZMQ Developers
# Distributed under the terms of the Modified BSD License.


import asyncio
from unittest import TestCase

import pytest

import zmq

try:
    import tornado
    from tornado import gen

    from zmq.eventloop import ioloop, zmqstream
except ImportError:
    tornado = None  # type: ignore


class TestZMQStream(TestCase):
    def setUp(self):
        if tornado is None:
            pytest.skip()
        if asyncio:
            asyncio.set_event_loop(asyncio.new_event_loop())
        self.context = zmq.Context()
        self.loop = ioloop.IOLoop()
        self.loop.make_current()
        self.push = zmqstream.ZMQStream(self.context.socket(zmq.PUSH))
        self.pull = zmqstream.ZMQStream(self.context.socket(zmq.PULL))
        port = self.push.bind_to_random_port('tcp://127.0.0.1')
        self.pull.connect('tcp://127.0.0.1:%i' % port)
        self.stream = self.push

    def tearDown(self):
        self.loop.close(all_fds=True)
        self.context.term()
        ioloop.IOLoop.clear_current()

    def run_until_timeout(self, timeout=10):
        timed_out = []

        @gen.coroutine
        def sleep_timeout():
            yield gen.sleep(timeout)
            timed_out[:] = ['timed out']
            self.loop.stop()

        self.loop.add_callback(lambda: sleep_timeout())
        self.loop.start()
        assert not timed_out

    def test_callable_check(self):
        """Ensure callable check works (py3k)."""

        self.stream.on_send(lambda *args: None)
        self.stream.on_recv(lambda *args: None)
        self.assertRaises(AssertionError, self.stream.on_recv, 1)
        self.assertRaises(AssertionError, self.stream.on_send, 1)
        self.assertRaises(AssertionError, self.stream.on_recv, zmq)

    def test_on_recv_basic(self):
        sent = [b'basic']

        def callback(msg):
            assert msg == sent
            self.loop.stop()

        self.loop.add_callback(lambda: self.push.send_multipart(sent))
        self.pull.on_recv(callback)
        self.run_until_timeout()

    def test_on_recv_wake(self):
        sent = [b'wake']

        def callback(msg):
            assert msg == sent
            self.loop.stop()

        self.pull.on_recv(callback)
        self.loop.call_later(1, lambda: self.push.send_multipart(sent))
        self.run_until_timeout()
