"""Tests for adapting Jupyter msg spec versions"""
# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
import copy
import json
from unittest import TestCase

from jupyter_client.adapter import adapt
from jupyter_client.adapter import code_to_line
from jupyter_client.adapter import V4toV5
from jupyter_client.session import Session


def test_default_version():
    s = Session()
    msg = s.msg("msg_type")
    msg["header"].pop("version")
    original = copy.deepcopy(msg)
    adapted = adapt(original)
    assert adapted["header"]["version"] == V4toV5.version


def test_code_to_line_no_code():
    line, pos = code_to_line("", 0)
    assert line == ""
    assert pos == 0


class AdapterTest(TestCase):
    def setUp(self):
        self.session = Session()

    def adapt(self, msg, version=None):
        original = copy.deepcopy(msg)
        adapted = adapt(msg, version or self.to_version)
        return original, adapted

    def check_header(self, msg):
        pass


class V4toV5TestCase(AdapterTest):
    from_version = 4
    to_version = 5

    def msg(self, msg_type, content):
        """Create a v4 msg (same as v5, minus version header)"""
        msg = self.session.msg(msg_type, content)
        msg["header"].pop("version")
        return msg

    def test_same_version(self):
        msg = self.msg("execute_result", content={"status": "ok"})
        original, adapted = self.adapt(msg, self.from_version)

        self.assertEqual(original, adapted)

    def test_no_adapt(self):
        msg = self.msg("input_reply", {"value": "some text"})
        v4, v5 = self.adapt(msg)
        self.assertEqual(v5["header"]["version"], V4toV5.version)
        v5["header"].pop("version")
        self.assertEqual(v4, v5)

    def test_rename_type(self):
        for v5_type, v4_type in [
            ("execute_result", "pyout"),
            ("execute_input", "pyin"),
            ("error", "pyerr"),
        ]:
            msg = self.msg(v4_type, {"key": "value"})
            v4, v5 = self.adapt(msg)
            self.assertEqual(v5["header"]["version"], V4toV5.version)
            self.assertEqual(v5["header"]["msg_type"], v5_type)
            self.assertEqual(v4["content"], v5["content"])

    def test_execute_request(self):
        msg = self.msg(
            "execute_request",
            {
                "code": "a=5",
                "silent": False,
                "user_expressions": {"a": "apple"},
                "user_variables": ["b"],
            },
        )
        v4, v5 = self.adapt(msg)
        self.assertEqual(v4["header"]["msg_type"], v5["header"]["msg_type"])
        v4c = v4["content"]
        v5c = v5["content"]
        self.assertEqual(v5c["user_expressions"], {"a": "apple", "b": "b"})
        self.assertNotIn("user_variables", v5c)
        self.assertEqual(v5c["code"], v4c["code"])

    def test_execute_reply(self):
        msg = self.msg(
            "execute_reply",
            {
                "status": "ok",
                "execution_count": 7,
                "user_variables": {"a": 1},
                "user_expressions": {"a+a": 2},
                "payload": [{"source": "page", "text": "blah"}],
            },
        )
        v4, v5 = self.adapt(msg)
        v5c = v5["content"]
        self.assertNotIn("user_variables", v5c)
        self.assertEqual(v5c["user_expressions"], {"a": 1, "a+a": 2})
        self.assertEqual(v5c["payload"], [{"source": "page", "data": {"text/plain": "blah"}}])

    def test_complete_request(self):
        msg = self.msg(
            "complete_request",
            {
                "text": "a.is",
                "line": "foo = a.is",
                "block": None,
                "cursor_pos": 10,
            },
        )
        v4, v5 = self.adapt(msg)
        v4c = v4["content"]
        v5c = v5["content"]
        for key in ("text", "line", "block"):
            self.assertNotIn(key, v5c)
        self.assertEqual(v5c["cursor_pos"], v4c["cursor_pos"])
        self.assertEqual(v5c["code"], v4c["line"])

    def test_complete_reply(self):
        msg = self.msg(
            "complete_reply",
            {
                "matched_text": "a.is",
                "matches": [
                    "a.isalnum",
                    "a.isalpha",
                    "a.isdigit",
                    "a.islower",
                ],
            },
        )
        v4, v5 = self.adapt(msg)
        v4c = v4["content"]
        v5c = v5["content"]

        self.assertEqual(v5c["matches"], v4c["matches"])
        self.assertEqual(v5c["metadata"], {})
        self.assertEqual(v5c["cursor_start"], -4)
        self.assertEqual(v5c["cursor_end"], None)

    def test_object_info_request(self):
        msg = self.msg(
            "object_info_request",
            {
                "oname": "foo",
                "detail_level": 1,
            },
        )
        v4, v5 = self.adapt(msg)
        self.assertEqual(v5["header"]["msg_type"], "inspect_request")
        v4c = v4["content"]
        v5c = v5["content"]
        self.assertEqual(v5c["code"], v4c["oname"])
        self.assertEqual(v5c["cursor_pos"], len(v4c["oname"]))
        self.assertEqual(v5c["detail_level"], v4c["detail_level"])

    def test_object_info_reply(self):
        msg = self.msg(
            "object_info_reply",
            {
                "name": "foo",
                "found": True,
                "status": "ok",
                "definition": "foo(a=5)",
                "docstring": "the docstring",
            },
        )
        v4, v5 = self.adapt(msg)
        self.assertEqual(v5["header"]["msg_type"], "inspect_reply")
        v4c = v4["content"]
        v5c = v5["content"]
        self.assertEqual(sorted(v5c), ["data", "found", "metadata", "status"])
        text = v5c["data"]["text/plain"]
        self.assertEqual(text, "\n".join([v4c["definition"], v4c["docstring"]]))

    def test_object_info_reply_not_found(self):
        msg = self.msg(
            "object_info_reply",
            {
                "name": "foo",
                "found": False,
            },
        )
        v4, v5 = self.adapt(msg)
        self.assertEqual(v5["header"]["msg_type"], "inspect_reply")
        v4["content"]
        v5c = v5["content"]
        self.assertEqual(
            v5c,
            {
                "status": "ok",
                "found": False,
                "data": {},
                "metadata": {},
            },
        )

    def test_kernel_info_reply(self):
        msg = self.msg(
            "kernel_info_reply",
            {
                "language": "python",
                "language_version": [2, 8, 0],
                "ipython_version": [1, 2, 3],
            },
        )
        v4, v5 = self.adapt(msg)
        v4["content"]
        v5c = v5["content"]
        self.assertEqual(
            v5c,
            {
                "protocol_version": "4.1",
                "implementation": "ipython",
                "implementation_version": "1.2.3",
                "language_info": {
                    "name": "python",
                    "version": "2.8.0",
                },
                "banner": "",
            },
        )

    # iopub channel

    def test_display_data(self):
        jsondata = dict(a=5)
        msg = self.msg(
            "display_data",
            {
                "data": {
                    "text/plain": "some text",
                    "application/json": json.dumps(jsondata),
                },
                "metadata": {"text/plain": {"key": "value"}},
            },
        )
        v4, v5 = self.adapt(msg)
        v4c = v4["content"]
        v5c = v5["content"]
        self.assertEqual(v5c["metadata"], v4c["metadata"])
        self.assertEqual(v5c["data"]["text/plain"], v4c["data"]["text/plain"])
        self.assertEqual(v5c["data"]["application/json"], jsondata)

    # stdin channel

    def test_input_request(self):
        msg = self.msg("input_request", {"prompt": "$>"})
        v4, v5 = self.adapt(msg)
        self.assertEqual(v5["content"]["prompt"], v4["content"]["prompt"])
        self.assertFalse(v5["content"]["password"])


class V5toV4TestCase(AdapterTest):
    from_version = 5
    to_version = 4

    def msg(self, msg_type, content):
        return self.session.msg(msg_type, content)

    def test_same_version(self):
        msg = self.msg("execute_result", content={"status": "ok"})
        original, adapted = self.adapt(msg, self.from_version)

        self.assertEqual(original, adapted)

    def test_no_adapt(self):
        msg = self.msg("input_reply", {"value": "some text"})
        v5, v4 = self.adapt(msg)
        self.assertNotIn("version", v4["header"])
        v5["header"].pop("version")
        self.assertEqual(v4, v5)

    def test_rename_type(self):
        for v5_type, v4_type in [
            ("execute_result", "pyout"),
            ("execute_input", "pyin"),
            ("error", "pyerr"),
        ]:
            msg = self.msg(v5_type, {"key": "value"})
            v5, v4 = self.adapt(msg)
            self.assertEqual(v4["header"]["msg_type"], v4_type)
            assert "version" not in v4["header"]
            self.assertEqual(v4["content"], v5["content"])

    def test_execute_request(self):
        msg = self.msg(
            "execute_request",
            {
                "code": "a=5",
                "silent": False,
                "user_expressions": {"a": "apple"},
            },
        )
        v5, v4 = self.adapt(msg)
        self.assertEqual(v4["header"]["msg_type"], v5["header"]["msg_type"])
        v4c = v4["content"]
        v5c = v5["content"]
        self.assertEqual(v4c["user_variables"], [])
        self.assertEqual(v5c["code"], v4c["code"])

    def test_complete_request(self):
        msg = self.msg(
            "complete_request",
            {
                "code": "def foo():\n    a.is\nfoo()",
                "cursor_pos": 19,
            },
        )
        v5, v4 = self.adapt(msg)
        v4c = v4["content"]
        v5c = v5["content"]
        self.assertNotIn("code", v4c)
        self.assertEqual(v4c["line"], v5c["code"].splitlines(True)[1])
        self.assertEqual(v4c["cursor_pos"], 8)
        self.assertEqual(v4c["text"], "")
        self.assertEqual(v4c["block"], None)

    def test_complete_reply(self):
        msg = self.msg(
            "complete_reply",
            {
                "cursor_start": 10,
                "cursor_end": 14,
                "matches": [
                    "a.isalnum",
                    "a.isalpha",
                    "a.isdigit",
                    "a.islower",
                ],
                "metadata": {},
            },
        )
        v5, v4 = self.adapt(msg)
        v4c = v4["content"]
        v5c = v5["content"]
        self.assertEqual(v4c["matched_text"], "a.is")
        self.assertEqual(v4c["matches"], v5c["matches"])

    def test_inspect_request(self):
        msg = self.msg(
            "inspect_request",
            {
                "code": "def foo():\n    apple\nbar()",
                "cursor_pos": 18,
                "detail_level": 1,
            },
        )
        v5, v4 = self.adapt(msg)
        self.assertEqual(v4["header"]["msg_type"], "object_info_request")
        v4c = v4["content"]
        v5c = v5["content"]
        self.assertEqual(v4c["oname"], "apple")
        self.assertEqual(v5c["detail_level"], v4c["detail_level"])

    def test_inspect_request_token(self):
        line = "something(range(10), kwarg=smth) ; xxx.xxx.xxx( firstarg, rand(234,23), kwarg1=2,"
        msg = self.msg(
            "inspect_request",
            {
                "code": line,
                "cursor_pos": len(line) - 1,
                "detail_level": 1,
            },
        )
        v5, v4 = self.adapt(msg)
        self.assertEqual(v4["header"]["msg_type"], "object_info_request")
        v4c = v4["content"]
        v5c = v5["content"]
        self.assertEqual(v4c["oname"], "xxx.xxx.xxx")
        self.assertEqual(v5c["detail_level"], v4c["detail_level"])

    def test_inspect_reply(self):
        msg = self.msg(
            "inspect_reply",
            {
                "name": "foo",
                "found": True,
                "data": {"text/plain": "some text"},
                "metadata": {},
            },
        )
        v5, v4 = self.adapt(msg)
        self.assertEqual(v4["header"]["msg_type"], "object_info_reply")
        v4c = v4["content"]
        v5["content"]
        self.assertEqual(sorted(v4c), ["found", "oname"])
        self.assertEqual(v4c["found"], False)

    def test_kernel_info_reply(self):
        msg = self.msg(
            "kernel_info_reply",
            {
                "protocol_version": "5.0",
                "implementation": "ipython",
                "implementation_version": "1.2.3",
                "language_info": {
                    "name": "python",
                    "version": "2.8.0",
                    "mimetype": "text/x-python",
                },
                "banner": "the banner",
            },
        )
        v5, v4 = self.adapt(msg)
        v4c = v4["content"]
        v5c = v5["content"]
        v5c["language_info"]
        self.assertEqual(
            v4c,
            {
                "protocol_version": [5, 0],
                "language": "python",
                "language_version": [2, 8, 0],
                "ipython_version": [1, 2, 3],
            },
        )

    # iopub channel

    def test_display_data(self):
        jsondata = dict(a=5)
        msg = self.msg(
            "display_data",
            {
                "data": {
                    "text/plain": "some text",
                    "application/json": jsondata,
                },
                "metadata": {"text/plain": {"key": "value"}},
            },
        )
        v5, v4 = self.adapt(msg)
        v4c = v4["content"]
        v5c = v5["content"]
        self.assertEqual(v5c["metadata"], v4c["metadata"])
        self.assertEqual(v5c["data"]["text/plain"], v4c["data"]["text/plain"])
        self.assertEqual(v4c["data"]["application/json"], json.dumps(jsondata))

    # stdin channel

    def test_input_request(self):
        msg = self.msg("input_request", {"prompt": "$>", "password": True})
        v5, v4 = self.adapt(msg)
        self.assertEqual(v5["content"]["prompt"], v4["content"]["prompt"])
        self.assertNotIn("password", v4["content"])
