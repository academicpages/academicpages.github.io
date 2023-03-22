# Copyright (C) PyZMQ Developers
# Distributed under the terms of the Modified BSD License.


import asyncio
import os
import threading
import time

import pytest

import zmq
from zmq.tests import BaseZMQTestCase, have_gevent

try:
    from tornado.ioloop import IOLoop as BaseIOLoop

    from zmq.eventloop import ioloop
except ImportError:
    _tornado = False
else:
    _tornado = True

# tornado 5 with asyncio disables custom IOLoop implementations
t5asyncio = False
if _tornado:
    import tornado

    if tornado.version_info >= (5,) and asyncio:
        t5asyncio = True


def printer():
    os.system("say hello")
    raise Exception
    print(time.time())


class Delay(threading.Thread):
    def __init__(self, f, delay=1):
        self.f = f
        self.delay = delay
        self.aborted = False
        self.cond = threading.Condition()
        super().__init__()

    def run(self):
        self.cond.acquire()
        self.cond.wait(self.delay)
        self.cond.release()
        if not self.aborted:
            self.f()

    def abort(self):
        self.aborted = True
        self.cond.acquire()
        self.cond.notify()
        self.cond.release()


class TestIOLoop(BaseZMQTestCase):
    if _tornado:
        IOLoop = ioloop.IOLoop

    def setUp(self):
        if not _tornado:
            pytest.skip("tornado required")
        super().setUp()
        if asyncio:
            asyncio.set_event_loop(asyncio.new_event_loop())

    def tearDown(self):
        super().tearDown()
        BaseIOLoop.clear_current()
        BaseIOLoop.clear_instance()

    def test_simple(self):
        """simple IOLoop creation test"""
        loop = self.IOLoop()
        loop.make_current()
        dc = ioloop.PeriodicCallback(loop.stop, 200)
        pc = ioloop.PeriodicCallback(lambda: None, 10)
        pc.start()
        dc.start()
        t = Delay(loop.stop, 1)
        t.start()
        loop.start()
        if t.is_alive():
            t.abort()
        else:
            self.fail("IOLoop failed to exit")

    def test_instance(self):
        """IOLoop.instance returns the right object"""
        loop = self.IOLoop.instance()
        if not t5asyncio:
            assert isinstance(loop, self.IOLoop)
        base_loop = BaseIOLoop.instance()
        assert base_loop is loop

    def test_current(self):
        """IOLoop.current returns the right object"""
        loop = ioloop.IOLoop.current()
        if not t5asyncio:
            assert isinstance(loop, self.IOLoop)
        base_loop = BaseIOLoop.current()
        assert base_loop is loop

    def test_close_all(self):
        """Test close(all_fds=True)"""
        loop = self.IOLoop.current()
        req, rep = self.create_bound_pair(zmq.REQ, zmq.REP)
        loop.add_handler(req, lambda msg: msg, ioloop.IOLoop.READ)
        loop.add_handler(rep, lambda msg: msg, ioloop.IOLoop.READ)
        assert req.closed == False
        assert rep.closed == False
        loop.close(all_fds=True)
        assert req.closed == True
        assert rep.closed == True


if have_gevent and _tornado:
    import zmq.green.eventloop.ioloop as green_ioloop

    class TestIOLoopGreen(TestIOLoop):
        IOLoop = green_ioloop.IOLoop

        def xtest_instance(self):
            """Green IOLoop.instance returns the right object"""
            loop = self.IOLoop.instance()
            if not t5asyncio:
                assert isinstance(loop, self.IOLoop)
            base_loop = BaseIOLoop.instance()
            assert base_loop is loop

        def xtest_current(self):
            """Green IOLoop.current returns the right object"""
            loop = self.IOLoop.current()
            if not t5asyncio:
                assert isinstance(loop, self.IOLoop)
            base_loop = BaseIOLoop.current()
            assert base_loop is loop
