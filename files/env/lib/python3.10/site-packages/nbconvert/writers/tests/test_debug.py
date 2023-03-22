"""
Module with tests for debug
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

import sys
from io import StringIO

from ...tests.base import TestsBase
from ..debug import DebugWriter

# -----------------------------------------------------------------------------
# Class
# -----------------------------------------------------------------------------


class TestDebug(TestsBase):
    """Contains test functions for debug.py"""

    def test_output(self):
        """Test debug writer output."""

        # Capture the stdout.  Remember original.
        stdout = sys.stdout
        stream = StringIO()
        sys.stdout = stream

        # Create stdout writer, get output
        writer = DebugWriter()
        writer.write("aaa", {"outputs": {"bbb": "ccc"}})
        output = stream.getvalue()

        # Check output.  Make sure resources dictionary is dumped, but nothing
        # else.
        assert "aaa" not in output
        assert "bbb" in output
        assert "ccc" in output

        # Revert stdout
        sys.stdout = stdout
