"""Test asyncio support"""
# Copyright (c) PyZMQ Developers
# Distributed under the terms of the Modified BSD License.

import asyncio
import json
import os
import sys
from concurrent.futures import CancelledError
from multiprocessing import Process

import pytest
from pytest import mark

import zmq
import zmq.asyncio as zaio
from zmq.auth.asyncio import AsyncioAuthenticator
from zmq.tests import BaseZMQTestCase
from zmq.tests.test_auth import TestThreadAuthentication


class ProcessForTeardownTest(Process):
    def __init__(self, event_loop_policy_class):
        Process.__init__(self)
        self.event_loop_policy_class = event_loop_policy_class

    def run(self):
        """Leave context, socket and event loop upon implicit disposal"""
        asyncio.set_event_loop_policy(self.event_loop_policy_class())

        actx = zaio.Context.instance()
        socket = actx.socket(zmq.PAIR)
        socket.bind_to_random_port("tcp://127.0.0.1")

        async def never_ending_task(socket):
            await socket.recv()  # never ever receive anything

        loop = asyncio.new_event_loop()
        coro = asyncio.wait_for(never_ending_task(socket), timeout=1)
        try:
            loop.run_until_complete(coro)
        except asyncio.TimeoutError:
            pass  # expected timeout
        else:
            assert False, "never_ending_task was completed unexpectedly"
        finally:
            loop.close()


class TestAsyncIOSocket(BaseZMQTestCase):
    Context = zaio.Context

    def setUp(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        super().setUp()

    def tearDown(self):
        super().tearDown()
        self.loop.close()
        # verify cleanup of references to selectors
        assert zaio._selectors == {}
        if 'zmq._asyncio_selector' in sys.modules:
            assert zmq._asyncio_selector._selector_loops == set()

    def test_socket_class(self):
        s = self.context.socket(zmq.PUSH)
        assert isinstance(s, zaio.Socket)
        s.close()

    def test_instance_subclass_first(self):
        actx = zmq.asyncio.Context.instance()
        ctx = zmq.Context.instance()
        ctx.term()
        actx.term()
        assert type(ctx) is zmq.Context
        assert type(actx) is zmq.asyncio.Context

    def test_instance_subclass_second(self):
        ctx = zmq.Context.instance()
        actx = zmq.asyncio.Context.instance()
        ctx.term()
        actx.term()
        assert type(ctx) is zmq.Context
        assert type(actx) is zmq.asyncio.Context

    def test_recv_multipart(self):
        async def test():
            a, b = self.create_bound_pair(zmq.PUSH, zmq.PULL)
            f = b.recv_multipart()
            assert not f.done()
            await a.send(b"hi")
            recvd = await f
            assert recvd == [b"hi"]

        self.loop.run_until_complete(test())

    def test_recv(self):
        async def test():
            a, b = self.create_bound_pair(zmq.PUSH, zmq.PULL)
            f1 = b.recv()
            f2 = b.recv()
            assert not f1.done()
            assert not f2.done()
            await a.send_multipart([b"hi", b"there"])
            recvd = await f2
            assert f1.done()
            assert f1.result() == b"hi"
            assert recvd == b"there"

        self.loop.run_until_complete(test())

    @mark.skipif(not hasattr(zmq, "RCVTIMEO"), reason="requires RCVTIMEO")
    def test_recv_timeout(self):
        async def test():
            a, b = self.create_bound_pair(zmq.PUSH, zmq.PULL)
            b.rcvtimeo = 100
            f1 = b.recv()
            b.rcvtimeo = 1000
            f2 = b.recv_multipart()
            with self.assertRaises(zmq.Again):
                await f1
            await a.send_multipart([b"hi", b"there"])
            recvd = await f2
            assert f2.done()
            assert recvd == [b"hi", b"there"]

        self.loop.run_until_complete(test())

    @mark.skipif(not hasattr(zmq, "SNDTIMEO"), reason="requires SNDTIMEO")
    def test_send_timeout(self):
        async def test():
            s = self.socket(zmq.PUSH)
            s.sndtimeo = 100
            with self.assertRaises(zmq.Again):
                await s.send(b"not going anywhere")

        self.loop.run_until_complete(test())

    def test_recv_string(self):
        async def test():
            a, b = self.create_bound_pair(zmq.PUSH, zmq.PULL)
            f = b.recv_string()
            assert not f.done()
            msg = "πøøπ"
            await a.send_string(msg)
            recvd = await f
            assert f.done()
            assert f.result() == msg
            assert recvd == msg

        self.loop.run_until_complete(test())

    def test_recv_json(self):
        async def test():
            a, b = self.create_bound_pair(zmq.PUSH, zmq.PULL)
            f = b.recv_json()
            assert not f.done()
            obj = dict(a=5)
            await a.send_json(obj)
            recvd = await f
            assert f.done()
            assert f.result() == obj
            assert recvd == obj

        self.loop.run_until_complete(test())

    def test_recv_json_cancelled(self):
        async def test():
            a, b = self.create_bound_pair(zmq.PUSH, zmq.PULL)
            f = b.recv_json()
            assert not f.done()
            f.cancel()
            # cycle eventloop to allow cancel events to fire
            await asyncio.sleep(0)
            obj = dict(a=5)
            await a.send_json(obj)
            # CancelledError change in 3.8 https://bugs.python.org/issue32528
            if sys.version_info < (3, 8):
                with pytest.raises(CancelledError):
                    recvd = await f
            else:
                with pytest.raises(asyncio.exceptions.CancelledError):
                    recvd = await f
            assert f.done()
            # give it a chance to incorrectly consume the event
            events = await b.poll(timeout=5)
            assert events
            await asyncio.sleep(0)
            # make sure cancelled recv didn't eat up event
            f = b.recv_json()
            recvd = await asyncio.wait_for(f, timeout=5)
            assert recvd == obj

        self.loop.run_until_complete(test())

    def test_recv_pyobj(self):
        async def test():
            a, b = self.create_bound_pair(zmq.PUSH, zmq.PULL)
            f = b.recv_pyobj()
            assert not f.done()
            obj = dict(a=5)
            await a.send_pyobj(obj)
            recvd = await f
            assert f.done()
            assert f.result() == obj
            assert recvd == obj

        self.loop.run_until_complete(test())

    def test_custom_serialize(self):
        def serialize(msg):
            frames = []
            frames.extend(msg.get("identities", []))
            content = json.dumps(msg["content"]).encode("utf8")
            frames.append(content)
            return frames

        def deserialize(frames):
            identities = frames[:-1]
            content = json.loads(frames[-1].decode("utf8"))
            return {
                "identities": identities,
                "content": content,
            }

        async def test():
            a, b = self.create_bound_pair(zmq.DEALER, zmq.ROUTER)

            msg = {
                "content": {
                    "a": 5,
                    "b": "bee",
                }
            }
            await a.send_serialized(msg, serialize)
            recvd = await b.recv_serialized(deserialize)
            assert recvd["content"] == msg["content"]
            assert recvd["identities"]
            # bounce back, tests identities
            await b.send_serialized(recvd, serialize)
            r2 = await a.recv_serialized(deserialize)
            assert r2["content"] == msg["content"]
            assert not r2["identities"]

        self.loop.run_until_complete(test())

    def test_custom_serialize_error(self):
        async def test():
            a, b = self.create_bound_pair(zmq.DEALER, zmq.ROUTER)

            msg = {
                "content": {
                    "a": 5,
                    "b": "bee",
                }
            }
            with pytest.raises(TypeError):
                await a.send_serialized(json, json.dumps)

            await a.send(b"not json")
            with pytest.raises(TypeError):
                await b.recv_serialized(json.loads)

        self.loop.run_until_complete(test())

    def test_recv_dontwait(self):
        async def test():
            push, pull = self.create_bound_pair(zmq.PUSH, zmq.PULL)
            f = pull.recv(zmq.DONTWAIT)
            with self.assertRaises(zmq.Again):
                await f
            await push.send(b"ping")
            await pull.poll()  # ensure message will be waiting
            f = pull.recv(zmq.DONTWAIT)
            assert f.done()
            msg = await f
            assert msg == b"ping"

        self.loop.run_until_complete(test())

    def test_recv_cancel(self):
        async def test():
            a, b = self.create_bound_pair(zmq.PUSH, zmq.PULL)
            f1 = b.recv()
            f2 = b.recv_multipart()
            assert f1.cancel()
            assert f1.done()
            assert not f2.done()
            await a.send_multipart([b"hi", b"there"])
            recvd = await f2
            assert f1.cancelled()
            assert f2.done()
            assert recvd == [b"hi", b"there"]

        self.loop.run_until_complete(test())

    def test_poll(self):
        async def test():
            a, b = self.create_bound_pair(zmq.PUSH, zmq.PULL)
            f = b.poll(timeout=0)
            await asyncio.sleep(0)
            assert f.result() == 0

            f = b.poll(timeout=1)
            assert not f.done()
            evt = await f

            assert evt == 0

            f = b.poll(timeout=1000)
            assert not f.done()
            await a.send_multipart([b"hi", b"there"])
            evt = await f
            assert evt == zmq.POLLIN
            recvd = await b.recv_multipart()
            assert recvd == [b"hi", b"there"]

        self.loop.run_until_complete(test())

    def test_poll_base_socket(self):
        async def test():
            ctx = zmq.Context()
            url = "inproc://test"
            a = ctx.socket(zmq.PUSH)
            b = ctx.socket(zmq.PULL)
            self.sockets.extend([a, b])
            a.bind(url)
            b.connect(url)

            poller = zaio.Poller()
            poller.register(b, zmq.POLLIN)

            f = poller.poll(timeout=1000)
            assert not f.done()
            a.send_multipart([b"hi", b"there"])
            evt = await f
            assert evt == [(b, zmq.POLLIN)]
            recvd = b.recv_multipart()
            assert recvd == [b"hi", b"there"]

        self.loop.run_until_complete(test())

    def test_poll_on_closed_socket(self):
        async def test():
            a, b = self.create_bound_pair(zmq.PUSH, zmq.PULL)

            f = b.poll(timeout=1)
            b.close()

            # The test might stall if we try to await f directly so instead just make a few
            # passes through the event loop to schedule and execute all callbacks
            for _ in range(5):
                await asyncio.sleep(0)
                if f.cancelled():
                    break
            assert f.cancelled()

        self.loop.run_until_complete(test())

    @pytest.mark.skipif(
        sys.platform.startswith("win"),
        reason="Windows does not support polling on files",
    )
    def test_poll_raw(self):
        async def test():
            p = zaio.Poller()
            # make a pipe
            r, w = os.pipe()
            r = os.fdopen(r, "rb")
            w = os.fdopen(w, "wb")

            # POLLOUT
            p.register(r, zmq.POLLIN)
            p.register(w, zmq.POLLOUT)
            evts = await p.poll(timeout=1)
            evts = dict(evts)
            assert r.fileno() not in evts
            assert w.fileno() in evts
            assert evts[w.fileno()] == zmq.POLLOUT

            # POLLIN
            p.unregister(w)
            w.write(b"x")
            w.flush()
            evts = await p.poll(timeout=1000)
            evts = dict(evts)
            assert r.fileno() in evts
            assert evts[r.fileno()] == zmq.POLLIN
            assert r.read(1) == b"x"
            r.close()
            w.close()

        loop = asyncio.new_event_loop()
        loop.run_until_complete(test())

    def test_multiple_loops(self):
        a, b = self.create_bound_pair(zmq.PUSH, zmq.PULL)

        async def test():
            await a.send(b'buf')
            msg = await b.recv()
            assert msg == b'buf'

        for i in range(3):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(asyncio.wait_for(test(), timeout=10))
            loop.close()

    def test_shadow(self):
        async def test():
            ctx = zmq.Context()
            s = ctx.socket(zmq.PULL)
            async_s = zaio.Socket(s)
            assert isinstance(async_s, self.socket_class)

    def test_process_teardown(self):
        event_loop_policy_class = type(asyncio.get_event_loop_policy())
        proc = ProcessForTeardownTest(event_loop_policy_class)
        proc.start()
        try:
            proc.join(10)  # starting new Python process may cost a lot
            self.assertEqual(
                proc.exitcode,
                0,
                "Python process died with code %d" % proc.exitcode
                if proc.exitcode
                else "process teardown hangs",
            )
        finally:
            proc.terminate()


class TestAsyncioAuthentication(TestThreadAuthentication):
    """Test authentication running in a asyncio task"""

    Context = zaio.Context

    def shortDescription(self):
        """Rewrite doc strings from TestThreadAuthentication from
        'threaded' to 'asyncio'.
        """
        doc = self._testMethodDoc
        if doc:
            doc = doc.split("\n")[0].strip()
            if doc.startswith("threaded auth"):
                doc = doc.replace("threaded auth", "asyncio auth")
        return doc

    def setUp(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        super().setUp()

    def tearDown(self):
        super().tearDown()
        self.loop.close()

    def make_auth(self):
        return AsyncioAuthenticator(self.context)

    def can_connect(self, server, client):
        """Check if client can connect to server using tcp transport"""

        async def go():
            result = False
            iface = "tcp://127.0.0.1"
            port = server.bind_to_random_port(iface)
            client.connect("%s:%i" % (iface, port))
            msg = [b"Hello World"]

            # set timeouts
            server.SNDTIMEO = client.RCVTIMEO = 1000
            try:
                await server.send_multipart(msg)
            except zmq.Again:
                return False
            try:
                rcvd_msg = await client.recv_multipart()
            except zmq.Again:
                return False
            else:
                assert rcvd_msg == msg
                result = True
            return result

        return self.loop.run_until_complete(go())

    def _select_recv(self, multipart, socket, **kwargs):
        recv = socket.recv_multipart if multipart else socket.recv

        async def coro():
            if not await socket.poll(5000):
                raise TimeoutError("Should have received a message")
            return await recv(**kwargs)

        return self.loop.run_until_complete(coro())
