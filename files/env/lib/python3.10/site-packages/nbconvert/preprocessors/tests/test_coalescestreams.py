"""Tests for the coalescestreams preprocessor"""

# Copyright (c) IPython Development Team.
# Distributed under the terms of the Modified BSD License.

from nbformat import v4 as nbformat

from ..coalescestreams import coalesce_streams
from .base import PreprocessorTestsBase


class TestCoalesceStreams(PreprocessorTestsBase):
    """Contains test functions for coalescestreams.py"""

    def test_coalesce_streams(self):
        """coalesce_streams preprocessor output test"""
        nb = self.build_notebook()
        res = self.build_resources()
        nb, res = coalesce_streams(nb, res)
        outputs = nb.cells[0].outputs
        self.assertEqual(outputs[0].text, "a")
        self.assertEqual(outputs[1].output_type, "display_data")
        self.assertEqual(outputs[2].text, "cd")
        self.assertEqual(outputs[3].text, "ef")

    def test_coalesce_sequenced_streams(self):
        """Can the coalesce streams preprocessor merge a sequence of streams?"""
        outputs = [
            nbformat.new_output(output_type="stream", name="stdout", text="0"),
            nbformat.new_output(output_type="stream", name="stdout", text="1"),
            nbformat.new_output(output_type="stream", name="stdout", text="2"),
            nbformat.new_output(output_type="stream", name="stdout", text="3"),
            nbformat.new_output(output_type="stream", name="stdout", text="4"),
            nbformat.new_output(output_type="stream", name="stdout", text="5"),
            nbformat.new_output(output_type="stream", name="stdout", text="6"),
            nbformat.new_output(output_type="stream", name="stdout", text="7"),
        ]
        cells = [nbformat.new_code_cell(source="# None", execution_count=1, outputs=outputs)]

        nb = nbformat.new_notebook(cells=cells)
        res = self.build_resources()
        nb, res = coalesce_streams(nb, res)
        outputs = nb.cells[0].outputs
        self.assertEqual(outputs[0].text, "01234567")

    def test_coalesce_replace_streams(self):
        """Are \\r characters handled?"""
        outputs = [
            nbformat.new_output(output_type="stream", name="stdout", text="z"),
            nbformat.new_output(output_type="stream", name="stdout", text="\ra"),
            nbformat.new_output(output_type="stream", name="stdout", text="\nz\rb"),
            nbformat.new_output(output_type="stream", name="stdout", text="\nz"),
            nbformat.new_output(output_type="stream", name="stdout", text="\rc\n"),
            nbformat.new_output(output_type="stream", name="stdout", text="z\rz\rd"),
        ]
        cells = [nbformat.new_code_cell(source="# None", execution_count=1, outputs=outputs)]

        nb = nbformat.new_notebook(cells=cells)
        res = self.build_resources()
        nb, res = coalesce_streams(nb, res)
        outputs = nb.cells[0].outputs
        self.assertEqual(outputs[0].text, "a\nb\nc\nd")
