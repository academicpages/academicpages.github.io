"""
Module with tests for Strings
"""

# -----------------------------------------------------------------------------
# Copyright (c) 2013, the IPython Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------
import os
import re

from ...tests.base import TestsBase
from ..strings import (
    add_anchor,
    add_prompts,
    ascii_only,
    comment_lines,
    get_lines,
    html2text,
    ipython2python,
    posix_path,
    prevent_list_blocks,
    strip_dollars,
    strip_files_prefix,
    wrap_text,
)

# -----------------------------------------------------------------------------
# Class
# -----------------------------------------------------------------------------


class TestStrings(TestsBase):
    def test_wrap_text(self):
        """wrap_text test"""
        test_text = """
        Tush! never tell me; I take it much unkindly
        That thou, Iago, who hast had my purse
        As if the strings were thine, shouldst know of this.
        """
        for length in [30, 5, 1]:
            self._confirm_wrap_text(test_text, length)

    def _confirm_wrap_text(self, text, length):
        for line in wrap_text(text, length).split("\n"):
            assert len(line) <= length

    def test_html2text(self):
        """html2text test"""
        # TODO: More tests
        self.assertEqual(html2text("<name>joe</name>"), "joe")

    def test_add_anchor(self):
        """add_anchor test"""
        # TODO: More tests
        results = add_anchor("<b>Hello World!</b>")
        assert "Hello World!" in results
        assert 'id="' in results
        assert 'class="anchor-link"' in results
        assert "<b" in results
        assert "</b>" in results

    def test_add_anchor_fail(self):
        """add_anchor does nothing when it fails"""
        html = "<h1>Hello <br>World!</h1>"
        results = add_anchor(html)
        self.assertEqual(html, results)

    def test_add_anchor_valid_url_fragment(self):
        """add_anchor creates a valid URL fragment"""
        results = add_anchor(r"<h1>$\pi$ with #s and unicode 中</h1>")
        match = re.search(r'href="#(.*?)"', results)
        assert match
        assert len(match.groups()) == 1
        href = match.groups()[0]

        assert len(href) > 0
        # No invalid characters should be present
        assert "\\" not in href
        assert "#" not in href
        assert "中" not in href

    def test_strip_dollars(self):
        """strip_dollars test"""
        tests = [
            ("", ""),
            ("  ", "  "),
            ("$$", ""),
            ("$H$", "H"),
            ("$He", "He"),
            ("H$el", "H$el"),
            ("Hell$", "Hell"),
            ("Hello", "Hello"),
            ("W$o$rld", "W$o$rld"),
        ]
        for test in tests:
            self._try_strip_dollars(test[0], test[1])

    def _try_strip_dollars(self, test, result):
        self.assertEqual(strip_dollars(test), result)

    def test_strip_files_prefix(self):
        """strip_files_prefix test"""
        tests = [
            ("", ""),
            ("/files", "/files"),
            ('test="/files"', 'test="/files"'),
            ("My files are in `files/`", "My files are in `files/`"),
            (
                '<a href="files/test.html">files/test.html</a>',
                '<a href="test.html">files/test.html</a>',
            ),
            (
                '<a href="/files/test.html">files/test.html</a>',
                '<a href="test.html">files/test.html</a>',
            ),
            (
                "<a href='files/test.html'>files/test.html</a>",
                "<a href='test.html'>files/test.html</a>",
            ),
            ('<img src="files/url/location.gif">', '<img src="url/location.gif">'),
            ('<img src="/files/url/location.gif">', '<img src="url/location.gif">'),
            ("hello![caption]", "hello![caption]"),
            ("hello![caption](/url/location.gif)", "hello![caption](/url/location.gif)"),
            ("hello![caption](url/location.gif)", "hello![caption](url/location.gif)"),
            ("hello![caption](url/location.gif)", "hello![caption](url/location.gif)"),
            ("hello![caption](files/url/location.gif)", "hello![caption](url/location.gif)"),
            ("hello![caption](/files/url/location.gif)", "hello![caption](url/location.gif)"),
            ("hello [text](/files/url/location.gif)", "hello [text](url/location.gif)"),
            ("hello [text space](files/url/location.gif)", "hello [text space](url/location.gif)"),
        ]
        for test in tests:
            self._try_files_prefix(test[0], test[1])

    def _try_files_prefix(self, test, result):
        self.assertEqual(strip_files_prefix(test), result)

    def test_comment_lines(self):
        """comment_lines test"""
        for line in comment_lines("hello\nworld\n!").split("\n"):
            assert line.startswith("# ")
        for line in comment_lines("hello\nworld\n!", "beep").split("\n"):
            assert line.startswith("beep")

    def test_get_lines(self):
        """get_lines test"""
        text = "hello\nworld\n!"
        self.assertEqual(get_lines(text, start=1), "world\n!")
        self.assertEqual(get_lines(text, end=2), "hello\nworld")
        self.assertEqual(get_lines(text, start=2, end=5), "!")
        self.assertEqual(get_lines(text, start=-2), "world\n!")

    def test_ipython2python(self):
        """ipython2python test"""
        # TODO: More tests
        results = ipython2python('%%pylab\nprint("Hello-World")').replace("u'", "'")
        self.fuzzy_compare(
            results.replace(r"\n", ""),
            "get_ipython().run_cell_magic('pylab', '', 'print(\"Hello-World\")')",
            ignore_spaces=True,
            ignore_newlines=True,
        )

    def test_posix_path(self):
        """posix_path test"""
        path_list = ["foo", "bar"]
        expected = "/".join(path_list)
        native = os.path.join(*path_list)
        filtered = posix_path(native)
        self.assertEqual(filtered, expected)

    def test_add_prompts(self):
        """add_prompts test"""
        text1 = """for i in range(10):\n  i += 1\n  print i"""
        text2 = """>>> for i in range(10):\n...   i += 1\n...   print i"""
        self.assertEqual(text2, add_prompts(text1))

    def test_prevent_list_blocks(self):
        """prevent_list_blocks test"""
        tests = [
            ("1. arabic point", "1\\. arabic point"),
            ("* bullet asterisk", "\\* bullet asterisk"),
            ("+ bullet Plus Sign", "\\+ bullet Plus Sign"),
            ("- bullet Hyphen-Minus", "\\- bullet Hyphen-Minus"),
            ("  1. spaces + arabic point", "  1\\. spaces + arabic point"),
        ]
        for test in tests:
            self.assertEqual(prevent_list_blocks(test[0]), test[1])

    def test_ascii_only(self):
        """ascii only test"""
        tests = [
            ("", ""),
            ("  ", "  "),
            ("Hello", "Hello"),
            ("Hello 中文", "Hello ??"),
        ]
        for test in tests:
            self.assertEqual(test[1], ascii_only(test[0]))
