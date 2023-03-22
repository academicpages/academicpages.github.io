# Copyright (C) PyZMQ Developers
# Distributed under the terms of the Modified BSD License.

import asyncio
import sys

import zmq
import zmq.asyncio as zaio
from zmq.tests import BaseZMQTestCase, require_zmq_4
from zmq.utils.monitor import recv_monitor_message


class TestSocketMonitor(BaseZMQTestCase):
    @require_zmq_4
    def test_monitor(self):
        """Test monitoring interface for sockets."""
        s_rep = self.context.socket(zmq.REP)
        s_req = self.context.socket(zmq.REQ)
        self.sockets.extend([s_rep, s_req])
        s_req.bind("tcp://127.0.0.1:6666")
        # try monitoring the REP socket

        s_rep.monitor(
            "inproc://monitor.rep",
            zmq.EVENT_CONNECT_DELAYED | zmq.EVENT_CONNECTED | zmq.EVENT_MONITOR_STOPPED,
        )
        # create listening socket for monitor
        s_event = self.context.socket(zmq.PAIR)
        self.sockets.append(s_event)
        s_event.connect("inproc://monitor.rep")
        s_event.linger = 0
        # test receive event for connect event
        s_rep.connect("tcp://127.0.0.1:6666")
        m = recv_monitor_message(s_event)
        if m['event'] == zmq.EVENT_CONNECT_DELAYED:
            assert m['endpoint'] == b"tcp://127.0.0.1:6666"
            # test receive event for connected event
            m = recv_monitor_message(s_event)
        assert m['event'] == zmq.EVENT_CONNECTED
        assert m['endpoint'] == b"tcp://127.0.0.1:6666"

        # test monitor can be disabled.
        s_rep.disable_monitor()
        m = recv_monitor_message(s_event)
        assert m['event'] == zmq.EVENT_MONITOR_STOPPED

    @require_zmq_4
    def test_monitor_repeat(self):
        s = self.socket(zmq.PULL)
        m = s.get_monitor_socket()
        self.sockets.append(m)
        m2 = s.get_monitor_socket()
        assert m is m2
        s.disable_monitor()
        evt = recv_monitor_message(m)
        assert evt['event'] == zmq.EVENT_MONITOR_STOPPED
        m.close()
        s.close()

    @require_zmq_4
    def test_monitor_connected(self):
        """Test connected monitoring socket."""
        s_rep = self.context.socket(zmq.REP)
        s_req = self.context.socket(zmq.REQ)
        self.sockets.extend([s_rep, s_req])
        s_req.bind("tcp://127.0.0.1:6667")
        # try monitoring the REP socket
        # create listening socket for monitor
        s_event = s_rep.get_monitor_socket()
        s_event.linger = 0
        self.sockets.append(s_event)
        # test receive event for connect event
        s_rep.connect("tcp://127.0.0.1:6667")
        m = recv_monitor_message(s_event)
        if m['event'] == zmq.EVENT_CONNECT_DELAYED:
            assert m['endpoint'] == b"tcp://127.0.0.1:6667"
            # test receive event for connected event
            m = recv_monitor_message(s_event)
        assert m['event'] == zmq.EVENT_CONNECTED
        assert m['endpoint'] == b"tcp://127.0.0.1:6667"


class TestSocketMonitorAsyncIO(BaseZMQTestCase):
    Context = zaio.Context  # makes BaseZMQTestCase create asyncio self.context

    def setUp(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        super().setUp()
        context = zaio.Context.instance()

    def tearDown(self):
        super().tearDown()
        self.loop.close()
        # verify cleanup of references to selectors
        assert zaio._selectors == {}
        if 'zmq._asyncio_selector' in sys.modules:
            assert zmq._asyncio_selector._selector_loops == set()

    @require_zmq_4
    def test_monitor(self):
        """Test monitoring interface for sockets."""
        s_rep = self.context.socket(zmq.REP)
        s_req = self.context.socket(zmq.REQ)
        self.sockets.extend([s_rep, s_req])
        s_req.bind("tcp://127.0.0.1:6666")
        # try monitoring the REP socket

        s_rep.monitor(
            "inproc://monitor.rep",
            zmq.EVENT_CONNECT_DELAYED | zmq.EVENT_CONNECTED | zmq.EVENT_MONITOR_STOPPED,
        )
        # create listening socket for monitor
        s_event = self.context.socket(zmq.PAIR)
        self.sockets.append(s_event)
        s_event.connect("inproc://monitor.rep")
        s_event.linger = 0
        # test receive event for connect event
        s_rep.connect("tcp://127.0.0.1:6666")
        m = self.loop.run_until_complete(recv_monitor_message(s_event))
        if m['event'] == zmq.EVENT_CONNECT_DELAYED:
            assert m['endpoint'] == b"tcp://127.0.0.1:6666"
            # test receive event for connected event
            m = self.loop.run_until_complete(recv_monitor_message(s_event))
        assert m['event'] == zmq.EVENT_CONNECTED
        assert m['endpoint'] == b"tcp://127.0.0.1:6666"

        # test monitor can be disabled.
        s_rep.disable_monitor()
        m = self.loop.run_until_complete(recv_monitor_message(s_event))
        assert m['event'] == zmq.EVENT_MONITOR_STOPPED

    @require_zmq_4
    def test_monitor_repeat(self):
        s = self.socket(zmq.PULL)
        m = s.get_monitor_socket()
        self.sockets.append(m)
        m2 = s.get_monitor_socket()
        assert m is m2
        s.disable_monitor()
        evt = self.loop.run_until_complete(recv_monitor_message(m))
        assert evt['event'] == zmq.EVENT_MONITOR_STOPPED
        m.close()
        s.close()

    @require_zmq_4
    def test_monitor_connected(self):
        """Test connected monitoring socket."""
        s_rep = self.context.socket(zmq.REP)
        s_req = self.context.socket(zmq.REQ)
        self.sockets.extend([s_rep, s_req])
        s_req.bind("tcp://127.0.0.1:6667")
        # try monitoring the REP socket
        # create listening socket for monitor
        s_event = s_rep.get_monitor_socket()
        s_event.linger = 0
        self.sockets.append(s_event)
        # test receive event for connect event
        s_rep.connect("tcp://127.0.0.1:6667")
        m = self.loop.run_until_complete(recv_monitor_message(s_event))
        if m['event'] == zmq.EVENT_CONNECT_DELAYED:
            assert m['endpoint'] == b"tcp://127.0.0.1:6667"
            # test receive event for connected event
            m = self.loop.run_until_complete(recv_monitor_message(s_event))
        assert m['event'] == zmq.EVENT_CONNECTED
        assert m['endpoint'] == b"tcp://127.0.0.1:6667"
