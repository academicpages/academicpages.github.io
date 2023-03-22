"""
Module with tests for exporter.py
"""

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
import os
from unittest.mock import patch

from traitlets.config import Config

from ...preprocessors.base import Preprocessor
from ..base import get_export_names
from ..exporter import Exporter
from .base import ExportersTestsBase

# -----------------------------------------------------------------------------
# Class
# -----------------------------------------------------------------------------


class PizzaPreprocessor(Preprocessor):
    """Simple preprocessor that adds a 'pizza' entry to the NotebookNode.  Used
    to test Exporter.
    """

    def preprocess(self, nb, resources):
        nb["pizza"] = "cheese"
        return nb, resources


class TestExporter(ExportersTestsBase):
    """Contains test functions for exporter.py"""

    def test_constructor(self):
        """Can an Exporter be constructed?"""
        Exporter()

    def test_export(self):
        """Can an Exporter export something?"""
        exporter = Exporter()
        (notebook, resources) = exporter.from_filename(self._get_notebook())
        assert isinstance(notebook, dict)

    def test_preprocessor(self):
        """Do preprocessors work?"""
        config = Config({"Exporter": {"preprocessors": [PizzaPreprocessor()]}})
        exporter = Exporter(config=config)
        (notebook, resources) = exporter.from_filename(self._get_notebook())
        self.assertEqual(notebook["pizza"], "cheese")

    def test_get_export_names_disable(self):
        """Can we disable all exporters then enable a single one"""
        config = Config({"Exporter": {"enabled": False}, "NotebookExporter": {"enabled": True}})
        export_names = get_export_names(config=config)
        self.assertEqual(export_names, ["notebook"])

    def test_get_exporter_disable_config_exporters(self):
        """
        Does get_export_names behave correctly with respect to
        NBCONVERT_DISABLE_CONFIG_EXPORTERS being set in the
        environment?
        """
        config = Config({"Exporter": {"enabled": False}, "NotebookExporter": {"enabled": True}})
        os.environ["NBCONVERT_DISABLE_CONFIG_EXPORTERS"] = "1"
        with patch("nbconvert.exporters.base.get_exporter") as exp:
            export_names = get_export_names(config=config)
            # get_export_names should not call get_exporter for
            # any of the entry points because we return before then.
            exp.assert_not_called()

            # We should have all exporters, not just the ones
            # enabled in the config
            self.assertNotEqual(export_names, ["notebook"])

        # In the absence of this variable we should revert to
        # the normal behavior.
        del os.environ["NBCONVERT_DISABLE_CONFIG_EXPORTERS"]
        export_names = get_export_names(config=config)
        self.assertEqual(export_names, ["notebook"])
