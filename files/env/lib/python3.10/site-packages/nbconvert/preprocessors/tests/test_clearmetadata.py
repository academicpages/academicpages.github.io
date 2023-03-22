"""
Module with tests for the clearmetadata preprocessor.
"""

# Copyright (c) IPython Development Team.
# Distributed under the terms of the Modified BSD License.

from ..clearmetadata import ClearMetadataPreprocessor
from .base import PreprocessorTestsBase


class TestClearMetadata(PreprocessorTestsBase):
    """Contains test functions for clearmetadata.py"""

    def build_notebook(self):
        notebook = super().build_notebook()
        notebook.metadata = {
            "language_info": {"name": "python", "version": "3.6.7"},
            "kernelspec": {"language": "python", "name": "python3"},
        }
        # Add a test field to the first cell
        if "metadata" not in notebook.cells[0]:
            notebook.cells[0].metadata = {}
        notebook.cells[0].metadata["test_field"] = "test_value"
        notebook.cells[0].metadata["test_nested"] = {"test_keep": "keep", "test_filtered": "filter"}
        notebook.cells[0].metadata["executeTime"] = dict(
            [("end_time", "09:31:50"), ("start_time", "09:31:49")]
        )
        return notebook

    def build_preprocessor(self, **kwargs):
        """Make an instance of a preprocessor"""
        preprocessor = ClearMetadataPreprocessor(**kwargs)
        preprocessor.enabled = True
        return preprocessor

    def test_constructor(self):
        """Can a ClearMetadataPreprocessor be constructed?"""
        self.build_preprocessor()

    def test_default_output(self):
        """Test the output of the ClearMetadataPreprocessor"""
        nb = self.build_notebook()
        res = self.build_resources()
        preprocessor = self.build_preprocessor()
        nb, res = preprocessor(nb, res)

        assert not nb.cells[0].metadata
        # By default we only perserve the langauge name
        assert nb.metadata == {"language_info": {"name": "python"}}

    def test_cell_only(self):
        """Test the output of the ClearMetadataPreprocessor"""
        nb = self.build_notebook()
        res = self.build_resources()
        preprocessor = self.build_preprocessor(clear_notebook_metadata=False)
        nb, res = preprocessor(nb, res)

        assert not nb.cells[0].metadata
        assert nb.metadata

    def test_notebook_only(self):
        """Test the output of the ClearMetadataPreprocessor"""
        nb = self.build_notebook()
        res = self.build_resources()
        preprocessor = self.build_preprocessor(
            clear_cell_metadata=False, preserve_nb_metadata_mask=set()
        )
        nb, res = preprocessor(nb, res)

        assert nb.cells[0].metadata
        assert not nb.metadata

    def test_selective_cell_metadata(self):
        """Test the output of the ClearMetadataPreprocessor"""
        nb = self.build_notebook()
        res = self.build_resources()
        preprocessor = self.build_preprocessor(
            preserve_cell_metadata_mask=["test_field"], preserve_nb_metadata_mask=set()
        )
        nb, res = preprocessor(nb, res)

        assert nb.cells[0].metadata == {"test_field": "test_value"}
        assert not nb.metadata

    def test_selective_cell_tuple_metadata(self):
        """Test the output of the ClearMetadataPreprocessor"""
        nb = self.build_notebook()
        res = self.build_resources()
        # Ensure that a tuple length 1 works as well as a string key
        preprocessor = self.build_preprocessor(
            preserve_cell_metadata_mask=[("test_field",)], preserve_nb_metadata_mask=set()
        )
        nb, res = preprocessor(nb, res)

        assert nb.cells[0].metadata == {"test_field": "test_value"}
        assert not nb.metadata

    def test_nested_cell_metadata(self):
        """Test the output of the ClearMetadataPreprocessor"""
        nb = self.build_notebook()
        res = self.build_resources()
        preprocessor = self.build_preprocessor(
            preserve_cell_metadata_mask=[("test_nested", "test_keep")],
            preserve_nb_metadata_mask=set(),
        )
        nb, res = preprocessor(nb, res)

        assert nb.cells[0].metadata == {"test_nested": {"test_keep": "keep"}}
        assert not nb.metadata

    def test_nested_cell_tuple_metadata(self):
        """Test the output of the ClearMetadataPreprocessor"""
        nb = self.build_notebook()
        res = self.build_resources()
        # Ensure that a tuple length 1 works as well as a string key
        preprocessor = self.build_preprocessor(
            preserve_cell_metadata_mask=[("test_nested", ("test_keep",))],
            preserve_nb_metadata_mask=set(),
        )
        nb, res = preprocessor(nb, res)

        assert nb.cells[0].metadata == {"test_nested": {"test_keep": "keep"}}
        assert not nb.metadata

    def test_selective_notebook_metadata(self):
        """Test the output of the ClearMetadataPreprocessor"""
        nb = self.build_notebook()
        res = self.build_resources()
        preprocessor = self.build_preprocessor(preserve_nb_metadata_mask=["kernelspec"])
        nb, res = preprocessor(nb, res)

        assert not nb.cells[0].metadata
        assert nb.metadata == {"kernelspec": {"language": "python", "name": "python3"}}
