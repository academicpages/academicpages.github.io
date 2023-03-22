"""Test Pandoc module"""
# -----------------------------------------------------------------------------
#  Copyright (C) 2014 The IPython Development Team
#
#  Distributed under the terms of the BSD License.  The full license is in
#  the file COPYING, distributed as part of this software.
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------
import os
import warnings

from nbconvert.tests.base import TestsBase

from ...tests.utils import onlyif_cmds_exist
from .. import pandoc

# -----------------------------------------------------------------------------
# Classes and functions
# -----------------------------------------------------------------------------


class TestPandoc(TestsBase):
    """Collection of Pandoc tests"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_env = os.environ.copy()

    def setUp(self):
        super().setUp()
        pandoc.check_pandoc_version._cached = None

    @onlyif_cmds_exist("pandoc")
    def test_pandoc_available(self):
        """Test behaviour that pandoc functions raise PandocMissing as documented"""
        pandoc.clean_cache()

        os.environ["PATH"] = ""
        with self.assertRaises(pandoc.PandocMissing):
            pandoc.get_pandoc_version()
        with self.assertRaises(pandoc.PandocMissing):
            pandoc.check_pandoc_version()
        with self.assertRaises(pandoc.PandocMissing):
            pandoc.pandoc("", "markdown", "html")

        # original_env["PATH"] should contain pandoc
        os.environ["PATH"] = self.original_env["PATH"]
        with warnings.catch_warnings(record=True) as w:
            pandoc.get_pandoc_version()
            pandoc.check_pandoc_version()
            pandoc.pandoc("", "markdown", "html")
        self.assertEqual(w, [])

    @onlyif_cmds_exist("pandoc")
    def test_minimal_version(self):
        original_minversion = pandoc._minimal_version

        pandoc._minimal_version = "120.0"
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            # call it twice to verify the cached value is used
            assert not pandoc.check_pandoc_version()
            assert not pandoc.check_pandoc_version()
        # only one warning after two calls, due to cache
        self.assertEqual(len(w), 1)
        # clear cache
        pandoc.check_pandoc_version._cached = None
        pandoc._minimal_version = pandoc.get_pandoc_version()
        assert pandoc.check_pandoc_version()


def pandoc_function_raised_missing(f, *args, **kwargs):
    try:
        f(*args, **kwargs)
    except pandoc.PandocMissing:
        return True
    else:
        return False
