"""Tests for the latex preprocessor"""

# Copyright (c) IPython Development Team.
# Distributed under the terms of the Modified BSD License.

from unittest.mock import patch

import pytest

from ..webpdf import WebPDFExporter
from .base import ExportersTestsBase


class TestWebPDFExporter(ExportersTestsBase):
    """Contains test functions for webpdf.py"""

    exporter_class = WebPDFExporter

    @pytest.mark.network
    def test_export(self):
        """
        Can a TemplateExporter export something?
        """
        (output, resources) = WebPDFExporter(allow_chromium_download=True).from_filename(
            self._get_notebook()
        )
        assert len(output) > 0

    @patch("pyppeteer.util.check_chromium", return_value=False)
    def test_webpdf_without_chromium(self, mock_check_chromium):
        """
        Generate PDFs if chromium not present?
        """
        with pytest.raises(RuntimeError):
            WebPDFExporter(allow_chromium_download=False).from_filename(self._get_notebook())

    def test_webpdf_without_pyppeteer(self):
        """
        Generate PDFs if chromium not present?
        """
        with pytest.raises(RuntimeError):
            exporter = WebPDFExporter()
            with open(self._get_notebook(), encoding="utf-8") as f:
                nb = exporter.from_file(f, resources={})
                # Have to do this as the very last action as traitlets do dynamic importing often
                with patch("builtins.__import__", side_effect=ModuleNotFoundError("Fake missing")):
                    exporter.from_notebook_node(nb)
