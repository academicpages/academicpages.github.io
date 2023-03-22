"""Module with tests for DataTypeFilter"""

# Copyright (c) IPython Development Team.
# Distributed under the terms of the Modified BSD License.
import pytest

from ...tests.base import TestsBase
from ..datatypefilter import DataTypeFilter


class TestDataTypeFilter(TestsBase):
    """Contains test functions for datatypefilter.py"""

    def test_constructor(self):
        """Can an instance of a DataTypeFilter be created?"""
        DataTypeFilter()

    def test_junk_types(self):
        """Can the DataTypeFilter pickout a useful type from a dict with junk types as keys?"""
        filter = DataTypeFilter()
        assert "image/png" in filter({"hair": "1", "water": 2, "image/png": 3, "rock": 4.0})
        assert "application/pdf" in filter(
            {
                "application/pdf": "file_path",
                "hair": 2,
                "water": "yay",
                "png": "not a png",
                "rock": "is a rock",
            }
        )

        with pytest.warns(UserWarning):
            self.assertEqual(
                filter(
                    {"hair": "this is not", "water": "going to return anything", "rock": "or is it"}
                ),
                [],
            )

    def test_null(self):
        """Will the DataTypeFilter fail if no types are passed in?"""
        filter = DataTypeFilter()
        with pytest.warns(UserWarning):
            self.assertEqual(filter({}), [])
