"""test building messages with Session"""
# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
import hmac
import os
import platform
import uuid
from datetime import datetime
from unittest import mock

import pytest
import zmq
from tornado import ioloop
from zmq.eventloop.zmqstream import ZMQStream
from zmq.tests import BaseZMQTestCase

from jupyter_client import jsonutil
from jupyter_client import session as ss


def _bad_packer(obj):
    raise TypeError("I don't work")


def _bad_unpacker(bytes):
    raise TypeError("I don't work either")


class SessionTestCase(BaseZMQTestCase):
    def setUp(self):
        BaseZMQTestCase.setUp(self)
        self.session = ss.Session()


@pytest.fixture
def no_copy_threshold():
    """Disable zero-copy optimizations in pyzmq >= 17"""
    with mock.patch.object(zmq, "COPY_THRESHOLD", 1, create=True):
        yield


@pytest.mark.usefixtures("no_copy_threshold")
class TestSession(SessionTestCase):
    def test_msg(self):
        """message format"""
        msg = self.session.msg("execute")
        thekeys = set("header parent_header metadata content msg_type msg_id".split())
        s = set(msg.keys())
        self.assertEqual(s, thekeys)
        self.assertTrue(isinstance(msg["content"], dict))
        self.assertTrue(isinstance(msg["metadata"], dict))
        self.assertTrue(isinstance(msg["header"], dict))
        self.assertTrue(isinstance(msg["parent_header"], dict))
        self.assertTrue(isinstance(msg["msg_id"], str))
        self.assertTrue(isinstance(msg["msg_type"], str))
        self.assertEqual(msg["header"]["msg_type"], "execute")
        self.assertEqual(msg["msg_type"], "execute")

    def test_serialize(self):
        msg = self.session.msg("execute", content=dict(a=10, b=1.1))
        msg_list = self.session.serialize(msg, ident=b"foo")
        ident, msg_list = self.session.feed_identities(msg_list)
        new_msg = self.session.deserialize(msg_list)
        self.assertEqual(ident[0], b"foo")
        self.assertEqual(new_msg["msg_id"], msg["msg_id"])
        self.assertEqual(new_msg["msg_type"], msg["msg_type"])
        self.assertEqual(new_msg["header"], msg["header"])
        self.assertEqual(new_msg["content"], msg["content"])
        self.assertEqual(new_msg["parent_header"], msg["parent_header"])
        self.assertEqual(new_msg["metadata"], msg["metadata"])
        # ensure floats don't come out as Decimal:
        self.assertEqual(type(new_msg["content"]["b"]), type(new_msg["content"]["b"]))

    def test_default_secure(self):
        self.assertIsInstance(self.session.key, bytes)
        self.assertIsInstance(self.session.auth, hmac.HMAC)

    def test_send(self):
        ctx = zmq.Context()
        A = ctx.socket(zmq.PAIR)
        B = ctx.socket(zmq.PAIR)
        A.bind("inproc://test")
        B.connect("inproc://test")

        msg = self.session.msg("execute", content=dict(a=10))
        self.session.send(A, msg, ident=b"foo", buffers=[b"bar"])

        ident, msg_list = self.session.feed_identities(B.recv_multipart())
        new_msg = self.session.deserialize(msg_list)
        self.assertEqual(ident[0], b"foo")
        self.assertEqual(new_msg["msg_id"], msg["msg_id"])
        self.assertEqual(new_msg["msg_type"], msg["msg_type"])
        self.assertEqual(new_msg["header"], msg["header"])
        self.assertEqual(new_msg["content"], msg["content"])
        self.assertEqual(new_msg["parent_header"], msg["parent_header"])
        self.assertEqual(new_msg["metadata"], msg["metadata"])
        self.assertEqual(new_msg["buffers"], [b"bar"])

        content = msg["content"]
        header = msg["header"]
        header["msg_id"] = self.session.msg_id
        parent = msg["parent_header"]
        metadata = msg["metadata"]
        header["msg_type"]
        self.session.send(
            A,
            None,
            content=content,
            parent=parent,
            header=header,
            metadata=metadata,
            ident=b"foo",
            buffers=[b"bar"],
        )
        ident, msg_list = self.session.feed_identities(B.recv_multipart())
        new_msg = self.session.deserialize(msg_list)
        self.assertEqual(ident[0], b"foo")
        self.assertEqual(new_msg["msg_id"], header["msg_id"])
        self.assertEqual(new_msg["msg_type"], msg["msg_type"])
        self.assertEqual(new_msg["header"], msg["header"])
        self.assertEqual(new_msg["content"], msg["content"])
        self.assertEqual(new_msg["metadata"], msg["metadata"])
        self.assertEqual(new_msg["parent_header"], msg["parent_header"])
        self.assertEqual(new_msg["buffers"], [b"bar"])

        header["msg_id"] = self.session.msg_id

        self.session.send(A, msg, ident=b"foo", buffers=[b"bar"])
        ident, new_msg = self.session.recv(B)
        self.assertEqual(ident[0], b"foo")
        self.assertEqual(new_msg["msg_id"], header["msg_id"])
        self.assertEqual(new_msg["msg_type"], msg["msg_type"])
        self.assertEqual(new_msg["header"], msg["header"])
        self.assertEqual(new_msg["content"], msg["content"])
        self.assertEqual(new_msg["metadata"], msg["metadata"])
        self.assertEqual(new_msg["parent_header"], msg["parent_header"])
        self.assertEqual(new_msg["buffers"], [b"bar"])

        # buffers must support the buffer protocol
        with self.assertRaises(TypeError):
            self.session.send(A, msg, ident=b"foo", buffers=[1])

        # buffers must be contiguous
        buf = memoryview(os.urandom(16))
        with self.assertRaises(ValueError):
            self.session.send(A, msg, ident=b"foo", buffers=[buf[::2]])

        A.close()
        B.close()
        ctx.term()

    def test_args(self):
        """initialization arguments for Session"""
        s = self.session
        self.assertTrue(s.pack is ss.default_packer)
        self.assertTrue(s.unpack is ss.default_unpacker)
        self.assertEqual(s.username, os.environ.get("USER", "username"))

        s = ss.Session()
        self.assertEqual(s.username, os.environ.get("USER", "username"))

        self.assertRaises(TypeError, ss.Session, pack="hi")
        self.assertRaises(TypeError, ss.Session, unpack="hi")
        u = str(uuid.uuid4())
        s = ss.Session(username="carrot", session=u)
        self.assertEqual(s.session, u)
        self.assertEqual(s.username, "carrot")

    @pytest.mark.skipif(platform.python_implementation() == 'PyPy', reason='Test fails on PyPy')
    def test_tracking(self):
        """test tracking messages"""
        a, b = self.create_bound_pair(zmq.PAIR, zmq.PAIR)
        s = self.session
        s.copy_threshold = 1
        loop = ioloop.IOLoop(make_current=False)
        ZMQStream(a, io_loop=loop)
        msg = s.send(a, "hello", track=False)
        self.assertTrue(msg["tracker"] is ss.DONE)
        msg = s.send(a, "hello", track=True)
        self.assertTrue(isinstance(msg["tracker"], zmq.MessageTracker))
        M = zmq.Message(b"hi there", track=True)
        msg = s.send(a, "hello", buffers=[M], track=True)
        t = msg["tracker"]
        self.assertTrue(isinstance(t, zmq.MessageTracker))
        self.assertRaises(zmq.NotDone, t.wait, 0.1)
        del M
        t.wait(1)  # this will raise

    def test_unique_msg_ids(self):
        """test that messages receive unique ids"""
        ids = set()
        for i in range(2**12):
            h = self.session.msg_header("test")
            msg_id = h["msg_id"]
            self.assertTrue(msg_id not in ids)
            ids.add(msg_id)

    def test_feed_identities(self):
        """scrub the front for zmq IDENTITIES"""
        content = dict(code="whoda", stuff=object())
        self.session.msg("execute", content=content)

    def test_session_id(self):
        session = ss.Session()
        # get bs before us
        bs = session.bsession
        us = session.session
        self.assertEqual(us.encode("ascii"), bs)
        session = ss.Session()
        # get us before bs
        us = session.session
        bs = session.bsession
        self.assertEqual(us.encode("ascii"), bs)
        # change propagates:
        session.session = "something else"
        bs = session.bsession
        us = session.session
        self.assertEqual(us.encode("ascii"), bs)
        session = ss.Session(session="stuff")
        # get us before bs
        self.assertEqual(session.bsession, session.session.encode("ascii"))
        self.assertEqual(b"stuff", session.bsession)

    def test_zero_digest_history(self):
        session = ss.Session(digest_history_size=0)
        for i in range(11):
            session._add_digest(uuid.uuid4().bytes)
        self.assertEqual(len(session.digest_history), 0)

    def test_cull_digest_history(self):
        session = ss.Session(digest_history_size=100)
        for i in range(100):
            session._add_digest(uuid.uuid4().bytes)
        self.assertTrue(len(session.digest_history) == 100)
        session._add_digest(uuid.uuid4().bytes)
        self.assertTrue(len(session.digest_history) == 91)
        for i in range(9):
            session._add_digest(uuid.uuid4().bytes)
        self.assertTrue(len(session.digest_history) == 100)
        session._add_digest(uuid.uuid4().bytes)
        self.assertTrue(len(session.digest_history) == 91)

    def test_bad_pack(self):
        try:
            ss.Session(pack=_bad_packer)
        except ValueError as e:
            self.assertIn("could not serialize", str(e))
            self.assertIn("don't work", str(e))
        else:
            self.fail("Should have raised ValueError")

    def test_bad_unpack(self):
        try:
            ss.Session(unpack=_bad_unpacker)
        except ValueError as e:
            self.assertIn("could not handle output", str(e))
            self.assertIn("don't work either", str(e))
        else:
            self.fail("Should have raised ValueError")

    def test_bad_packer(self):
        try:
            ss.Session(packer=__name__ + "._bad_packer")
        except ValueError as e:
            self.assertIn("could not serialize", str(e))
            self.assertIn("don't work", str(e))
        else:
            self.fail("Should have raised ValueError")

    def test_bad_unpacker(self):
        try:
            ss.Session(unpacker=__name__ + "._bad_unpacker")
        except ValueError as e:
            self.assertIn("could not handle output", str(e))
            self.assertIn("don't work either", str(e))
        else:
            self.fail("Should have raised ValueError")

    def test_bad_roundtrip(self):
        with self.assertRaises(ValueError):
            ss.Session(unpack=lambda b: 5)

    def _datetime_test(self, session):
        content = dict(t=ss.utcnow())
        metadata = dict(t=ss.utcnow())
        p = session.msg("msg")
        msg = session.msg("msg", content=content, metadata=metadata, parent=p["header"])
        smsg = session.serialize(msg)
        msg2 = session.deserialize(session.feed_identities(smsg)[1])
        assert isinstance(msg2["header"]["date"], datetime)
        self.assertEqual(msg["header"], msg2["header"])
        self.assertEqual(msg["parent_header"], msg2["parent_header"])
        self.assertEqual(msg["parent_header"], msg2["parent_header"])
        assert isinstance(msg["content"]["t"], datetime)
        assert isinstance(msg["metadata"]["t"], datetime)
        assert isinstance(msg2["content"]["t"], str)
        assert isinstance(msg2["metadata"]["t"], str)
        self.assertEqual(msg["content"], jsonutil.extract_dates(msg2["content"]))
        self.assertEqual(msg["content"], jsonutil.extract_dates(msg2["content"]))

    def test_datetimes(self):
        self._datetime_test(self.session)

    def test_datetimes_pickle(self):
        session = ss.Session(packer="pickle")
        self._datetime_test(session)

    def test_datetimes_msgpack(self):
        msgpack = pytest.importorskip("msgpack")

        session = ss.Session(
            pack=msgpack.packb,
            unpack=lambda buf: msgpack.unpackb(buf, raw=False),
        )
        self._datetime_test(session)

    def test_send_raw(self):
        ctx = zmq.Context()
        A = ctx.socket(zmq.PAIR)
        B = ctx.socket(zmq.PAIR)
        A.bind("inproc://test")
        B.connect("inproc://test")

        msg = self.session.msg("execute", content=dict(a=10))
        msg_list = [
            self.session.pack(msg[part])
            for part in ["header", "parent_header", "metadata", "content"]
        ]
        self.session.send_raw(A, msg_list, ident=b"foo")

        ident, new_msg_list = self.session.feed_identities(B.recv_multipart())
        new_msg = self.session.deserialize(new_msg_list)
        self.assertEqual(ident[0], b"foo")
        self.assertEqual(new_msg["msg_type"], msg["msg_type"])
        self.assertEqual(new_msg["header"], msg["header"])
        self.assertEqual(new_msg["parent_header"], msg["parent_header"])
        self.assertEqual(new_msg["content"], msg["content"])
        self.assertEqual(new_msg["metadata"], msg["metadata"])

        A.close()
        B.close()
        ctx.term()

    def test_clone(self):
        s = self.session
        s._add_digest("initial")
        s2 = s.clone()
        assert s2.session == s.session
        assert s2.digest_history == s.digest_history
        assert s2.digest_history is not s.digest_history
        digest = "abcdef"
        s._add_digest(digest)
        assert digest in s.digest_history
        assert digest not in s2.digest_history
