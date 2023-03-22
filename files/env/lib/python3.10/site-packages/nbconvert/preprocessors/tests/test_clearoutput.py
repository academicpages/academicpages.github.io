"""
Module with tests for the clearoutput preprocessor.
"""

# Copyright (c) IPython Development Team.
# Distributed under the terms of the Modified BSD License.

from ..clearoutput import ClearOutputPreprocessor
from .base import PreprocessorTestsBase


class TestClearOutput(PreprocessorTestsBase):
    """Contains test functions for clearoutput.py"""

    def build_notebook(self):
        notebook = super().build_notebook()
        # Add a test field to the first cell
        if "metadata" not in notebook.cells[0]:
            notebook.cells[0].metadata = {}
        notebook.cells[0].metadata["test_field"] = "test_value"
        return notebook

    def build_preprocessor(self):
        """Make an instance of a preprocessor"""
        preprocessor = ClearOutputPreprocessor()
        preprocessor.enabled = True
        return preprocessor

    def test_constructor(self):
        """Can a ClearOutputPreprocessor be constructed?"""
        self.build_preprocessor()

    def test_output(self):
        """Test the output of the ClearOutputPreprocessor"""
        for remove_test_field in [False, True]:
            nb = self.build_notebook()
            res = self.build_resources()
            preprocessor = self.build_preprocessor()
            # Also remove the test field in addition to defaults
            if remove_test_field:
                preprocessor.remove_metadata_fields.add("test_field")
            nb, res = preprocessor(nb, res)
            assert nb.cells[0].outputs == []
            assert nb.cells[0].execution_count is None
            if "metadata" in nb.cells[0]:
                for field in preprocessor.remove_metadata_fields:
                    assert field not in nb.cells[0].metadata
                # Ensure the test field is only removed when added to the traitlet
                assert remove_test_field or "test_field" in nb.cells[0].metadata
