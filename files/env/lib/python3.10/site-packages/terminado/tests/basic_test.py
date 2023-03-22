# basic_tests.py -- Basic unit tests for Terminado

# Copyright (c) Jupyter Development Team
# Copyright (c) 2014, Ramalingam Saravanan <sarava@sarava.net>
# Distributed under the terms of the Simplified BSD License.


import asyncio
import datetime
import json
import os
import re

# We must set the policy for python >=3.8, see https://www.tornadoweb.org/en/stable/#installation
# Snippet from https://github.com/tornadoweb/tornado/issues/2608#issuecomment-619524992
import sys
import unittest
from sys import platform

import pytest
import tornado
import tornado.httpserver
import tornado.testing
from tornado.ioloop import IOLoop

from terminado import NamedTermManager, SingleTermManager, TermSocket, UniqueTermManager

if sys.version_info[0] == 3 and sys.version_info[1] >= 8 and sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

#
# The timeout we use to assume no more messages are coming
# from the sever.
#
DONE_TIMEOUT = 1.0
ASYNC_TEST_TIMEOUT = 30
os.environ["ASYNC_TEST_TIMEOUT"] = str(ASYNC_TEST_TIMEOUT)

MAX_TERMS = 3  # Testing thresholds


class TestTermClient:
    """Test connection to a terminal manager"""

    __test__ = False

    def __init__(self, websocket):
        self.ws = websocket
        self.pending_read = None

    async def read_msg(self):

        # Because the Tornado Websocket client has no way to cancel
        # a pending read, we have to keep track of them...
        if self.pending_read is None:
            self.pending_read = self.ws.read_message()

        response = await self.pending_read
        self.pending_read = None
        if response:
            response = json.loads(response)
        return response

    async def read_all_msg(self, timeout=DONE_TIMEOUT):
        """Read messages until read times out"""
        msglist: list = []
        delta = datetime.timedelta(seconds=timeout)
        while True:
            try:
                mf = self.read_msg()
                msg = await tornado.gen.with_timeout(delta, mf)
            except tornado.gen.TimeoutError:
                return msglist

            msglist.append(msg)

    async def write_msg(self, msg):
        await self.ws.write_message(json.dumps(msg))

    async def read_stdout(self, timeout=DONE_TIMEOUT):
        """Read standard output until timeout read reached,
        return stdout and any non-stdout msgs received."""
        msglist = await self.read_all_msg(timeout)
        stdout = "".join([msg[1] for msg in msglist if msg[0] == "stdout"])
        othermsg = [msg for msg in msglist if msg[0] != "stdout"]
        return (stdout, othermsg)

    async def discard_stdout(self, timeout=DONE_TIMEOUT):
        """Read standard output messages, discarding the data
        as it's received. Return the number of bytes discarded
        and any non-stdout msgs"""
        othermsg: list = []
        bytes_discarded = 0
        delta = datetime.timedelta(seconds=timeout)
        while True:
            try:
                mf = self.read_msg()
                msg = await tornado.gen.with_timeout(delta, mf)
            except tornado.gen.TimeoutError:
                return bytes_discarded, othermsg
            if msg[0] == "stdout":
                bytes_discarded += len(msg[1])
            else:
                othermsg.append(msg)

    async def write_stdin(self, data):
        """Write to terminal stdin"""
        await self.write_msg(["stdin", data])

    async def get_pid(self):
        """Get process ID of terminal shell process"""
        await self.read_stdout()  # Clear out any pending
        await self.write_stdin("echo $$\r")
        (stdout, extra) = await self.read_stdout()
        if os.name == "nt":
            match = re.search(r"echo \$\$\\.*?\\r\\n(\d+)", repr(stdout))
            assert match is not None
            pid = int(match.groups()[0])
        else:
            # This should work on any OS, but keeping the above Windows special
            # case as I can't verify on Windows.
            for li in stdout.splitlines():
                if re.match(r"\d+$", li):
                    pid = int(li)
                    break
        return pid

    def close(self):
        self.ws.close()


class TermTestCase(tornado.testing.AsyncHTTPTestCase):

    # Factory for TestTermClient, because it has to be async
    # See:  https://github.com/tornadoweb/tornado/issues/1161
    async def get_term_client(self, path):
        port = self.get_http_port()
        url = "ws://127.0.0.1:%d%s" % (port, path)
        request = tornado.httpclient.HTTPRequest(
            url, headers={"Origin": "http://127.0.0.1:%d" % port}
        )

        ws = await tornado.websocket.websocket_connect(request)
        return TestTermClient(ws)

    async def get_term_clients(self, paths):
        return await asyncio.gather(*(self.get_term_client(path) for path in paths))

    async def get_pids(self, tm_list):
        pids = []
        for tm in tm_list:  # Must be sequential, in case terms are shared
            pid = await tm.get_pid()
            pids.append(pid)

        return pids

    def tearDown(self):
        run = IOLoop.current().run_sync
        run(self.named_tm.kill_all)
        run(self.single_tm.kill_all)
        run(self.unique_tm.kill_all)
        super().tearDown()

    def get_app(self):
        self.named_tm = NamedTermManager(
            shell_command=["bash"],
            max_terminals=MAX_TERMS,
        )

        self.single_tm = SingleTermManager(shell_command=["bash"])

        self.unique_tm = UniqueTermManager(
            shell_command=["bash"],
            max_terminals=MAX_TERMS,
        )

        named_tm = self.named_tm

        class NewTerminalHandler(tornado.web.RequestHandler):
            """Create a new named terminal, return redirect"""

            def get(self):
                name, terminal = named_tm.new_named_terminal()
                self.redirect("/named/" + name, permanent=False)

        return tornado.web.Application(
            [
                (r"/new", NewTerminalHandler),
                (r"/named/(\w+)", TermSocket, {"term_manager": self.named_tm}),
                (r"/single", TermSocket, {"term_manager": self.single_tm}),
                (r"/unique", TermSocket, {"term_manager": self.unique_tm}),
            ],
            debug=True,
        )

    test_urls = ("/named/term1", "/unique") + (("/single",) if os.name != "nt" else ())


class CommonTests(TermTestCase):
    @tornado.testing.gen_test
    async def test_basic(self):
        for url in self.test_urls:
            tm = await self.get_term_client(url)
            response = await tm.read_msg()
            self.assertEqual(response, ["setup", {}])

            # Check for initial shell prompt
            response = await tm.read_msg()
            self.assertEqual(response[0], "stdout")
            self.assertGreater(len(response[1]), 0)
            tm.close()

    @tornado.testing.gen_test
    async def test_basic_command(self):
        for url in self.test_urls:
            tm = await self.get_term_client(url)
            await tm.read_all_msg()
            await tm.write_stdin("whoami\n")
            (stdout, other) = await tm.read_stdout()
            if os.name == "nt":
                assert "whoami" in stdout
            else:
                assert stdout.startswith("who")
            assert other == []
            tm.close()


class NamedTermTests(TermTestCase):
    def test_new(self):
        response = self.fetch("/new", follow_redirects=False)
        self.assertEqual(response.code, 302)
        url = response.headers["Location"]

        # Check that the new terminal was created
        name = url.split("/")[2]
        self.assertIn(name, self.named_tm.terminals)

    @tornado.testing.gen_test
    async def test_namespace(self):
        names = ["/named/1"] * 2 + ["/named/2"] * 2
        tms = await self.get_term_clients(names)
        pids = await self.get_pids(tms)

        self.assertEqual(pids[0], pids[1])
        self.assertEqual(pids[2], pids[3])
        self.assertNotEqual(pids[0], pids[3])

        terminal = self.named_tm.terminals["1"]
        killed = await terminal.terminate(True)
        assert killed
        assert not terminal.ptyproc.isalive()
        assert terminal.ptyproc.closed

    @tornado.testing.gen_test
    @pytest.mark.skipif("linux" not in platform, reason="It only works on Linux")
    async def test_max_terminals(self):
        urls = ["/named/%d" % i for i in range(MAX_TERMS + 1)]
        tms = await self.get_term_clients(urls[:MAX_TERMS])
        _ = await self.get_pids(tms)

        # MAX_TERMS+1 should fail
        tm = await self.get_term_client(urls[MAX_TERMS])
        msg = await tm.read_msg()
        self.assertEqual(msg, None)  # Connection closed


class SingleTermTests(TermTestCase):
    @tornado.testing.gen_test
    async def test_single_process(self):
        tms = await self.get_term_clients(["/single", "/single"])
        pids = await self.get_pids(tms)
        self.assertEqual(pids[0], pids[1])

        assert self.single_tm.terminal is not None
        killed = await self.single_tm.terminal.terminate(True)
        assert killed
        assert self.single_tm.terminal.ptyproc.closed


class UniqueTermTests(TermTestCase):
    @tornado.testing.gen_test
    async def test_unique_processes(self):
        tms = await self.get_term_clients(["/unique", "/unique"])
        pids = await self.get_pids(tms)
        self.assertNotEqual(pids[0], pids[1])

    @tornado.testing.gen_test
    @pytest.mark.skipif("linux" not in platform, reason="It only works on Linux")
    async def test_max_terminals(self):
        tms = await self.get_term_clients(["/unique"] * MAX_TERMS)
        pids = await self.get_pids(tms)
        self.assertEqual(len(set(pids)), MAX_TERMS)  # All PIDs unique

        # MAX_TERMS+1 should fail
        tm = await self.get_term_client("/unique")
        msg = await tm.read_msg()
        self.assertEqual(msg, None)  # Connection closed

        # Close one
        tms[0].close()
        msg = await tms[0].read_msg()  # Closed
        self.assertEqual(msg, None)

        # Should be able to open back up to MAX_TERMS
        tm = await self.get_term_client("/unique")
        msg = await tm.read_msg()
        self.assertEqual(msg[0], "setup")

    @tornado.testing.gen_test
    @pytest.mark.timeout(timeout=ASYNC_TEST_TIMEOUT, method="thread")
    async def test_large_io_doesnt_hang(self):
        # This is a regression test for an error where Terminado hangs when
        # the PTY buffer size is exceeded. While the buffer size varies from
        # OS to OS, 30KBish seems like a reasonable amount and will trigger
        # this on both OSX and Debian.
        massive_payload = "ten bytes " * 3000
        massive_payload = "echo " + massive_payload + "\n"
        tm = await self.get_term_client("/unique")
        # Clear all startup messages.
        await tm.read_all_msg()
        # Write a payload that doesn't fit in a single PTY buffer.
        await tm.write_stdin(massive_payload)
        # Verify that the server didn't hang when responding, and that
        # we got a reasonable amount of data back (to tell us the read
        # didn't just timeout.
        bytes_discarded, other = await tm.discard_stdout()
        # Echo wont actually output anything on Windows.
        if "win" not in platform:
            assert bytes_discarded > 10000
        assert other == []
        tm.close()


if __name__ == "__main__":
    unittest.main()
