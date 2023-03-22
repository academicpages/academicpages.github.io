"""Tests for utils.io"""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

import io as stdlib_io
import sys
from io import StringIO

from ..io import unicode_std_stream


def test_UnicodeStdStream():
    # Test wrapping a bytes-level stdout
    stdoutb = stdlib_io.BytesIO()
    stdout = stdlib_io.TextIOWrapper(stdoutb, encoding="ascii")

    orig_stdout = sys.stdout
    sys.stdout = stdout
    try:
        sample = "@łe¶ŧ←"
        unicode_std_stream().write(sample)

        output = stdoutb.getvalue().decode("utf-8")
        assert output == sample
        assert not stdout.closed
    finally:
        sys.stdout = orig_stdout


def test_UnicodeStdStream_nowrap():
    # If we replace stdout with a StringIO, it shouldn't get wrapped.
    orig_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        assert unicode_std_stream() is sys.stdout
        assert not sys.stdout.closed
    finally:
        sys.stdout = orig_stdout
