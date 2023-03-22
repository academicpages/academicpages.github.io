"""Tests for RSTExporter"""

# Copyright (c) IPython Development Team.
# Distributed under the terms of the Modified BSD License.

import re

import nbformat
from nbformat import v4

from ...tests.utils import onlyif_cmds_exist
from ..rst import RSTExporter
from .base import ExportersTestsBase


class TestRSTExporter(ExportersTestsBase):
    """Tests for RSTExporter"""

    exporter_class = RSTExporter
    should_include_raw = ["rst"]

    def test_constructor(self):
        """
        Can a RSTExporter be constructed?
        """
        RSTExporter()

    @onlyif_cmds_exist("pandoc")
    def test_export(self):
        """
        Can a RSTExporter export something?
        """
        (output, resources) = RSTExporter().from_filename(self._get_notebook())
        assert len(output) > 0

    @onlyif_cmds_exist("pandoc")
    def test_empty_code_cell(self):
        """No empty code cells in rst"""
        nbname = self._get_notebook()
        with open(nbname, encoding="utf8") as f:
            nb = nbformat.read(f, 4)

        exporter = self.exporter_class()

        (output, resources) = exporter.from_notebook_node(nb)
        # add an empty code cell
        nb.cells.append(v4.new_code_cell(source=""))
        (output2, resources) = exporter.from_notebook_node(nb)
        # adding an empty code cell shouldn't change output
        self.assertEqual(output.strip(), output2.strip())

    @onlyif_cmds_exist("pandoc")
    def test_png_metadata(self):
        """
        Does RSTExporter treat pngs with width/height metadata correctly?
        """
        (output, resources) = RSTExporter().from_filename(
            self._get_notebook(nb_name="pngmetadata.ipynb")
        )
        assert len(output) > 0
        check_for_png = re.compile(r".. image::.*?\n\s+(.*?)\n\s*\n", re.DOTALL)
        result = check_for_png.search(output)
        assert result is not None
        attr_string = result.group(1)
        assert ":width:" in attr_string
        assert ":height:" in attr_string
        assert "px" in attr_string
