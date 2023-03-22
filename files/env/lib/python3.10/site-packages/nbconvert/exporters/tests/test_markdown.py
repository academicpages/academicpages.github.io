"""Tests for MarkdownExporter"""

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

from ..markdown import MarkdownExporter
from .base import ExportersTestsBase

# -----------------------------------------------------------------------------
# Class
# -----------------------------------------------------------------------------


class TestMarkdownExporter(ExportersTestsBase):
    """Tests for MarkdownExporter"""

    exporter_class = MarkdownExporter
    should_include_raw = ["markdown", "html"]

    def test_constructor(self):
        """
        Can a MarkdownExporter be constructed?
        """
        MarkdownExporter()

    def test_export(self):
        """
        Can a MarkdownExporter export something?
        """
        (output, resources) = MarkdownExporter().from_filename(self._get_notebook())
        assert len(output) > 0
