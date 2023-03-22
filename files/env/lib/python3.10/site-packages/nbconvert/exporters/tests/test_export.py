"""
Module with tests for export.py
"""

# Copyright (c) IPython Development Team.
# Distributed under the terms of the Modified BSD License.

import os
import sys

import nbformat
import pytest
from traitlets.config import Config

import nbconvert.tests

from ..base import (
    ExporterDisabledError,
    ExporterNameError,
    export,
    get_export_names,
    get_exporter,
)
from ..exporter import Exporter
from ..python import PythonExporter
from .base import ExportersTestsBase


class TestExport(ExportersTestsBase):
    """Contains test functions for export.py"""

    def test_export_wrong_name(self):
        """
        Is the right error thrown when a bad template name is used?
        """
        try:
            exporter = get_exporter("not_a_name")
            export(exporter, self._get_notebook())
        except ExporterNameError as e:
            pass

    def test_export_disabled(self):
        """
        Trying to use a disabled exporter should raise ExporterDisbledError
        """
        config = Config({"NotebookExporter": {"enabled": False}})
        with pytest.raises(ExporterDisabledError):
            get_exporter("notebook", config=config)

    def test_export_filename(self):
        """
        Can a notebook be exported by filename?
        """
        exporter = get_exporter("python")
        (output, resources) = export(exporter, self._get_notebook())
        assert len(output) > 0

    def test_export_nbnode(self):
        """
        Can a notebook be exported by a notebook node handle?
        """
        with open(self._get_notebook()) as f:
            notebook = nbformat.read(f, 4)
            exporter = get_exporter("python")
            (output, resources) = export(exporter, notebook)
        assert len(output) > 0

    def test_export_filestream(self):
        """
        Can a notebook be exported by a filesteam?
        """
        with open(self._get_notebook()) as f:
            exporter = get_exporter("python")
            (output, resources) = export(exporter, f)
        assert len(output) > 0

    def test_export_using_exporter(self):
        """
        Can a notebook be exported using an instanciated exporter?
        """
        (output, resources) = export(PythonExporter(), self._get_notebook())
        assert len(output) > 0

    def test_export_using_exporter_class(self):
        """
        Can a notebook be exported using an exporter class type?
        """
        (output, resources) = export(PythonExporter, self._get_notebook())
        assert len(output) > 0

    def test_export_resources(self):
        """
        Can a notebook be exported along with a custom resources dict?
        """
        (output, resources) = export(PythonExporter, self._get_notebook(), resources={})
        assert len(output) > 0

    def test_no_exporter(self):
        """
        Is the right error thrown if no exporter is provided?
        """
        try:
            (output, resources) = export(None, self._get_notebook())
        except TypeError:
            pass


def test_get_exporter_entrypoint():
    p = os.path.join(os.path.dirname(nbconvert.tests.__file__), "exporter_entrypoint")
    sys.path.insert(0, p)
    assert "entrypoint_test" in get_export_names()
    try:
        cls = get_exporter("entrypoint_test")
        assert issubclass(cls, Exporter), cls
    finally:
        del sys.path[0]
