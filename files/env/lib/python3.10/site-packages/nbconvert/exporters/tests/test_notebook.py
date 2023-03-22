"""Tests for notebook.py"""

# Copyright (c) IPython Development Team.
# Distributed under the terms of the Modified BSD License.

import json

from nbformat import validate

from nbconvert.tests.base import assert_big_text_equal

from ..notebook import NotebookExporter
from .base import ExportersTestsBase


class TestNotebookExporter(ExportersTestsBase):
    """Contains test functions for notebook.py"""

    exporter_class = NotebookExporter

    def test_export(self):
        """
        Does the NotebookExporter return the file unchanged?
        """
        with open(self._get_notebook()) as f:
            file_contents = f.read()
        (output, resources) = self.exporter_class().from_filename(self._get_notebook())
        assert len(output) > 0
        assert_big_text_equal(output, file_contents)

    def test_downgrade_3(self):
        exporter = self.exporter_class(nbformat_version=3)
        (output, resources) = exporter.from_filename(self._get_notebook())
        nb = json.loads(output)
        validate(nb)

    def test_downgrade_2(self):
        exporter = self.exporter_class(nbformat_version=2)
        (output, resources) = exporter.from_filename(self._get_notebook())
        nb = json.loads(output)
        self.assertEqual(nb["nbformat"], 2)
