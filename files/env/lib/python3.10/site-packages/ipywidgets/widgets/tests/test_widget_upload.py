# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

from unittest import TestCase

from traitlets import TraitError

from ipywidgets import FileUpload


class TestFileUpload(TestCase):

    def test_construction(self):
        uploader = FileUpload()
        # Default
        assert uploader.accept == ''
        assert not uploader.multiple
        assert not uploader.disabled

    def test_construction_with_params(self):
        uploader = FileUpload(accept='.txt',
                              multiple=True,
                              disabled=True)
        assert uploader.accept == '.txt'
        assert uploader.multiple
        assert uploader.disabled
