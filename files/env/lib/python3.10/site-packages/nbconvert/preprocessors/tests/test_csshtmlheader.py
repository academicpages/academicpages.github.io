"""
Module with tests for the csshtmlheader preprocessor
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

from ..csshtmlheader import CSSHTMLHeaderPreprocessor
from .base import PreprocessorTestsBase

# -----------------------------------------------------------------------------
# Class
# -----------------------------------------------------------------------------


class TestCSSHTMLHeader(PreprocessorTestsBase):
    """Contains test functions for csshtmlheader.py"""

    def build_preprocessor(self):
        """Make an instance of a preprocessor"""
        preprocessor = CSSHTMLHeaderPreprocessor()
        preprocessor.enabled = True
        return preprocessor

    def test_constructor(self):
        """Can a CSSHTMLHeaderPreprocessor be constructed?"""
        self.build_preprocessor()

    def test_output(self):
        """Test the output of the CSSHTMLHeaderPreprocessor"""
        nb = self.build_notebook()
        res = self.build_resources()
        preprocessor = self.build_preprocessor()
        nb, res = preprocessor(nb, res)
        assert "css" in res["inlining"]
