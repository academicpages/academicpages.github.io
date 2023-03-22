"""Tests for PDF export"""

# Copyright (c) IPython Development Team.
# Distributed under the terms of the Modified BSD License.

import os
import shutil
from tempfile import TemporaryDirectory

from ...tests.utils import onlyif_cmds_exist
from ..pdf import PDFExporter
from .base import ExportersTestsBase

# -----------------------------------------------------------------------------
# Class
# -----------------------------------------------------------------------------


class TestPDF(ExportersTestsBase):
    """Test PDF export"""

    exporter_class = PDFExporter

    def test_constructor(self):
        """Can a PDFExporter be constructed?"""
        self.exporter_class()

    @onlyif_cmds_exist("xelatex", "pandoc")
    def test_export(self):
        """Smoke test PDFExporter"""
        with TemporaryDirectory() as td:
            file_name = os.path.basename(self._get_notebook())
            newpath = os.path.join(td, file_name)
            shutil.copy(self._get_notebook(), newpath)
            (output, resources) = self.exporter_class(latex_count=1).from_filename(newpath)
            self.assertIsInstance(output, bytes)
            assert len(output) > 0
            # all temporary file should be cleaned up
            assert {file_name} == set(os.listdir(td))
