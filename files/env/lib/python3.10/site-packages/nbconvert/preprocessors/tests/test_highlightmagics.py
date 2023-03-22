"""Tests for the HighlightMagics preprocessor"""

from ..highlightmagics import HighlightMagicsPreprocessor
from .base import PreprocessorTestsBase


class TestHighlightMagics(PreprocessorTestsBase):
    """Contains test functions for highlightmagics.py"""

    def build_preprocessor(self):
        """Make an instance of a preprocessor"""
        preprocessor = HighlightMagicsPreprocessor()
        preprocessor.enabled = True
        return preprocessor

    def test_constructor(self):
        """Can a HighlightMagicsPreprocessor be constructed?"""
        self.build_preprocessor()

    def test_tagging(self):
        """Test the HighlightMagicsPreprocessor tagging"""
        nb = self.build_notebook()
        res = self.build_resources()
        preprocessor = self.build_preprocessor()
        nb.cells[
            0
        ].source = """%%R -i x,y -o XYcoef
            lm.fit <- lm(y~x)
            par(mfrow=c(2,2))
            print(summary(lm.fit))
            plot(lm.fit)
            XYcoef <- coef(lm.fit)"""

        nb, res = preprocessor(nb, res)

        assert "magics_language" in nb.cells[0]["metadata"]

        self.assertEqual(nb.cells[0]["metadata"]["magics_language"], "r")

    def test_no_false_positive(self):
        """Test that HighlightMagicsPreprocessor does not tag false positives"""
        nb = self.build_notebook()
        res = self.build_resources()
        preprocessor = self.build_preprocessor()
        nb.cells[
            0
        ].source = """# this should not be detected
                print(\"""
                %%R -i x, y
                \""")"""
        nb, res = preprocessor(nb, res)

        assert "magics_language" not in nb.cells[0]["metadata"]
