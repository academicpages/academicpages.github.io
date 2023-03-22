"""Tests for the latex preprocessor"""

# Copyright (c) IPython Development Team.
# Distributed under the terms of the Modified BSD License.

from ..latex import LatexPreprocessor
from .base import PreprocessorTestsBase


class TestLatex(PreprocessorTestsBase):
    """Contains test functions for latex.py"""

    def build_preprocessor(self):
        """Make an instance of a preprocessor"""
        preprocessor = LatexPreprocessor()
        preprocessor.enabled = True
        return preprocessor

    def test_constructor(self):
        """Can a LatexPreprocessor be constructed?"""
        self.build_preprocessor()

    def test_output(self):
        """Test the output of the LatexPreprocessor"""
        nb = self.build_notebook()
        res = self.build_resources()
        preprocessor = self.build_preprocessor()
        nb, res = preprocessor(nb, res)

        # Make sure the code cell wasn't modified.
        self.assertEqual(nb.cells[0].source, "$ e $")

        # Verify that the markdown cell wasn't processed.
        self.assertEqual(nb.cells[1].source, "$ e $")

    def test_highlight(self):
        """Check that highlighting style can be changed"""
        nb = self.build_notebook()
        res = self.build_resources()
        preprocessor = self.build_preprocessor()

        # Set the style to a known builtin that's not the default
        preprocessor.style = "colorful"
        nb, res = preprocessor(nb, res)
        style_defs = res["latex"]["pygments_definitions"]

        # Get the default
        from pygments.formatters import LatexFormatter

        default_defs = LatexFormatter(style="default").get_style_defs()

        # Verify that the style was in fact changed
        assert style_defs != default_defs
