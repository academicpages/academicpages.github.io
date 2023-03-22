"""
Module with tests for Highlight
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

import xml

import pytest

from ...tests.base import TestsBase
from ..highlight import Highlight2HTML, Highlight2Latex

# -----------------------------------------------------------------------------
# Class
# -----------------------------------------------------------------------------

highlight2html = Highlight2HTML()
highlight2latex = Highlight2Latex()
highlight2html_ruby = Highlight2HTML(pygments_lexer="ruby")


class TestHighlight(TestsBase):
    """Contains test functions for highlight.py"""

    # Hello world test, magics test, blank string test
    tests = [
        """
        #Hello World Example

        import foo

        def say(text):
            foo.bar(text)

        end

        say('Hello World!')
        """,
        """
        %%pylab
        plot(x,y, 'r')
        """,
    ]

    tokens = [["Hello World Example", "say", "text", "import", "def"], ["pylab", "plot"]]

    def test_highlight2html(self):
        """highlight2html test"""
        for index, test in enumerate(self.tests):
            self._try_highlight(highlight2html, test, self.tokens[index])

    def test_highlight2latex(self):
        """highlight2latex test"""
        for index, test in enumerate(self.tests):
            self._try_highlight(highlight2latex, test, self.tokens[index])

    def test_parse_html_many_lang(self):

        ht = highlight2html(self.tests[0])
        rb = highlight2html_ruby(self.tests[0])

        for lang, tkns in [(ht, ("def",)), (rb, ("def", "end"))]:
            root = xml.etree.ElementTree.fromstring(lang)
            self.assertEqual(self._extract_tokens(root, "k"), set(tkns))

    @pytest.mark.filterwarnings("ignore")
    def test_inject_html(self):
        out = highlight2html(self.tests[0], 'ipython3-foo"><script>alert(1)</script>')
        assert "<script>alert(1)</script>" not in out

    def _extract_tokens(self, root, cls):
        return set(map(lambda x: x.text, root.findall(".//*[@class='" + cls + "']")))

    def _try_highlight(self, method, test, tokens):
        """Try highlighting source, look for key tokens"""
        results = method(test)
        for token in tokens:
            assert token in results
