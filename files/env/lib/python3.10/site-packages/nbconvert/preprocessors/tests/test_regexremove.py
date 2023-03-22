"""
Module with tests for the RegexRemovePreprocessor.
"""

# Copyright (c) IPython Development Team.
# Distributed under the terms of the Modified BSD License.

import re

from nbformat import v4 as nbformat

from ..regexremove import RegexRemovePreprocessor
from .base import PreprocessorTestsBase


class TestRegexRemove(PreprocessorTestsBase):
    """Contains test functions for regexremove.py"""

    def build_notebook(self):
        notebook = super().build_notebook()
        # Add a few empty cells
        notebook.cells.extend(
            [
                nbformat.new_code_cell(""),
                nbformat.new_markdown_cell(" "),
                nbformat.new_raw_cell("\n"),
                nbformat.new_raw_cell("\t"),
            ]
        )

        return notebook

    def build_preprocessor(self):
        """Make an instance of a preprocessor"""
        preprocessor = RegexRemovePreprocessor()
        preprocessor.enabled = True
        return preprocessor

    def test_constructor(self):
        """Can a RegexRemovePreprocessor be constructed?"""
        self.build_preprocessor()

    def test_output(self):
        """Test the output of the RegexRemovePreprocessor"""
        pattern_lookup = {
            "disallow_whitespace": [r"\s*\Z"],
            "disallow_tab_newline": [r"\t\Z", r"\n\Z"],
        }
        expected_cell_count = {
            "default": 6,  # nothing is removed
            "disallow_whitespace": 2,  # all "empty" cells are removed
            "disallow_tab_newline": 4,  # cells with tab and newline are removed
            "none": 6,
        }
        for method in ["default", "disallow_whitespace", "disallow_tab_newline", "none"]:
            nb = self.build_notebook()
            res = self.build_resources()

            # Build the preprocessor and extend the list of patterns or use an empty list
            preprocessor = self.build_preprocessor()
            if method == "none":
                preprocessor.patterns = []
            else:
                preprocessor.patterns.extend(pattern_lookup.get(method, []))
            nb, res = preprocessor(nb, res)

            self.assertEqual(len(nb.cells), expected_cell_count[method])

            # Make sure none of the cells match the pattern
            patterns = list(map(re.compile, preprocessor.patterns))
            for cell in nb.cells:
                for pattern in patterns:
                    self.assertFalse(pattern.match(cell.source))
