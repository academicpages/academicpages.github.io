"""Tests for ScriptExporter"""

# Copyright (c) IPython Development Team.
# Distributed under the terms of the Modified BSD License.

import os
import sys

from nbformat import v4

import nbconvert

from ..script import ScriptExporter
from .base import ExportersTestsBase


class TestScriptExporter(ExportersTestsBase):
    """Tests for ScriptExporter"""

    exporter_class = ScriptExporter

    def test_constructor(self):
        """Construct ScriptExporter"""
        e = self.exporter_class()

    def test_export(self):
        """ScriptExporter can export something"""
        (output, resources) = self.exporter_class().from_filename(self._get_notebook())
        assert len(output) > 0

    def test_export_python(self):
        """delegate to custom exporter from language_info"""
        exporter = self.exporter_class()

        pynb = v4.new_notebook()
        (output, resources) = self.exporter_class().from_notebook_node(pynb)
        self.assertNotIn("# coding: utf-8", output)

        pynb.metadata.language_info = {
            "name": "python",
            "mimetype": "text/x-python",
            "nbconvert_exporter": "python",
        }
        (output, resources) = self.exporter_class().from_notebook_node(pynb)
        self.assertIn("# coding: utf-8", output)

    def test_export_config_transfer(self):
        """delegate config to custom exporter from language_info"""
        nb = v4.new_notebook()
        nb.metadata.language_info = {
            "name": "python",
            "mimetype": "text/x-python",
            "nbconvert_exporter": "python",
        }

        exporter = self.exporter_class()
        exporter.from_notebook_node(nb)
        assert exporter._exporters["python"] != exporter
        assert exporter._exporters["python"].config == exporter.config


def test_script_exporter_entrypoint():
    nb = v4.new_notebook()
    nb.metadata.language_info = {
        "name": "dummy",
        "mimetype": "text/x-dummy",
    }

    p = os.path.join(os.path.dirname(nbconvert.tests.__file__), "exporter_entrypoint")
    sys.path.insert(0, p)
    try:
        output, _ = ScriptExporter().from_notebook_node(nb)
        assert output == "dummy-script-exported"
    finally:
        sys.path.remove(p)
