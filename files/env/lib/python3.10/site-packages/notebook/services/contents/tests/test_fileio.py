"""Tests for file IO"""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

import os.path
import unittest
import pytest
import stat
import sys

from ..fileio import atomic_writing

from ipython_genutils.tempdir import TemporaryDirectory

umask = 0

def test_atomic_writing():
    class CustomExc(Exception):
        pass

    with TemporaryDirectory() as td:
        f1 = os.path.join(td, 'penguin')
        with open(f1, 'w') as f:
            f.write('Before')

        if os.name != 'nt':
            os.chmod(f1, 0o701)
            orig_mode = stat.S_IMODE(os.stat(f1).st_mode)

        f2 = os.path.join(td, 'flamingo')
        try:
            os.symlink(f1, f2)
            have_symlink = True
        except (AttributeError, NotImplementedError, OSError):
            # AttributeError: Python doesn't support it
            # NotImplementedError: The system doesn't support it
            # OSError: The user lacks the privilege (Windows)
            have_symlink = False

        with pytest.raises(CustomExc):
            with atomic_writing(f1) as f:
                f.write('Failing write')
                raise CustomExc

        # Because of the exception, the file should not have been modified
        with open(f1) as f:
            assert f.read() == 'Before'

        with atomic_writing(f1) as f:
            f.write('Overwritten')

        with open(f1) as f:
            assert f.read() == 'Overwritten'

        if os.name != 'nt':
            mode = stat.S_IMODE(os.stat(f1).st_mode)
            assert mode == orig_mode

        if have_symlink:
            # Check that writing over a file preserves a symlink
            with atomic_writing(f2) as f:
                f.write('written from symlink')

            with open(f1) as f:
                assert f.read() == 'written from symlink'

class TestWithSetUmask(unittest.TestCase):
    def setUp(self):
        # save umask
        global umask
        umask = os.umask(0)
        os.umask(umask)

    def tearDown(self):
        # restore umask
        os.umask(umask)

    @pytest.mark.skipif(sys.platform == "win32", reason="do not run on windows")
    def test_atomic_writing_umask(self):
        with TemporaryDirectory() as td:
            os.umask(0o022)
            f1 = os.path.join(td, '1')
            with atomic_writing(f1) as f:
                f.write('1')
            mode = stat.S_IMODE(os.stat(f1).st_mode)
            assert mode == 0o644

            os.umask(0o057)
            f2 = os.path.join(td, '2')
            with atomic_writing(f2) as f:
                f.write('2')
            mode = stat.S_IMODE(os.stat(f2).st_mode)
            assert mode == 0o620


def test_atomic_writing_newlines():
    with TemporaryDirectory() as td:
        path = os.path.join(td, 'testfile')

        lf = 'a\nb\nc\n'
        plat = lf.replace('\n', os.linesep)
        crlf = lf.replace('\n', '\r\n')

        # test default
        with open(path, 'w') as f:
            f.write(lf)
        with open(path, newline='') as f:
            read = f.read()
        assert read == plat

        # test newline=LF
        with open(path, 'w', newline='\n') as f:
            f.write(lf)
        with open(path, newline='') as f:
            read = f.read()
        assert read == lf

        # test newline=CRLF
        with atomic_writing(path, newline='\r\n') as f:
            f.write(lf)
        with open(path, newline='') as f:
            read = f.read()
        assert read == crlf

        # test newline=no convert
        text = 'crlf\r\ncr\rlf\n'
        with atomic_writing(path, newline='') as f:
            f.write(text)
        with open(path, newline='') as f:
            read = f.read()
        assert read == text
