"""
Module with tests for the TagRemovePreprocessor.
"""

# Copyright (c) IPython Development Team.
# Distributed under the terms of the Modified BSD License.

from nbformat import v4 as nbformat

from ..tagremove import TagRemovePreprocessor
from .base import PreprocessorTestsBase


class TestTagRemove(PreprocessorTestsBase):
    """Contains test functions for tagremove.py"""

    def build_notebook(self):
        """
        Build a notebook to have metadata tags for cells, output_areas, and
        individual outputs.
        """
        notebook = super().build_notebook()
        # Add a few empty cells
        notebook.cells[0].outputs.extend(
            [
                nbformat.new_output(
                    "display_data", data={"text/plain": "i"}, metadata={"tags": ["hide_one_output"]}
                ),
            ]
        )
        outputs_to_be_removed = [
            nbformat.new_output("display_data", data={"text/plain": "remove_my_output"}),
        ]
        outputs_to_be_kept = [
            nbformat.new_output(
                "stream",
                name="stdout",
                text="remove_my_output",
            ),
        ]
        notebook.cells.extend(
            [
                nbformat.new_code_cell(
                    source="display('remove_my_output')",
                    execution_count=2,
                    outputs=outputs_to_be_removed,
                    metadata={"tags": ["hide_all_outputs"]},
                ),
                nbformat.new_code_cell(
                    source="print('remove this cell')",
                    execution_count=3,
                    outputs=outputs_to_be_kept,
                    metadata={"tags": ["hide_this_cell"]},
                ),
            ]
        )

        return notebook

    def build_preprocessor(self):
        """Make an instance of a preprocessor"""
        preprocessor = TagRemovePreprocessor()
        preprocessor.enabled = True
        return preprocessor

    def test_constructor(self):
        """Can a TagRemovePreprocessor be constructed?"""
        self.build_preprocessor()

    def test_output(self):
        """Test the output of the TagRemovePreprocessor"""
        nb = self.build_notebook()
        res = self.build_resources()
        preprocessor = self.build_preprocessor()
        preprocessor.remove_cell_tags.add("hide_this_cell")
        preprocessor.remove_all_outputs_tags.add("hide_all_outputs")
        preprocessor.remove_single_output_tags.add("hide_one_output")

        nb, res = preprocessor(nb, res)

        # checks that we can remove entire cells
        self.assertEqual(len(nb.cells), 3)

        # checks that we can remove output areas
        self.assertEqual(len(nb.cells[-1].outputs), 0)

        # checks that we can remove individual outputs
        self.assertEqual(len(nb.cells[0].outputs), 8)
