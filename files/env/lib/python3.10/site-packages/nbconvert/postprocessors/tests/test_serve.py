"""
Module with tests for the serve post-processor
"""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

import pytest

from ...tests.base import TestsBase


class TestServe(TestsBase):
    """Contains test functions for serve.py"""

    def test_constructor(self):
        """Can a ServePostProcessor be constructed?"""
        pytest.importorskip("tornado")
        try:
            from ..serve import ServePostProcessor
        except ImportError:
            print("Something weird is happening.\nTornado is sometimes present, sometimes not.")
            raise
        ServePostProcessor()
