from contextlib import contextmanager
import os
import os.path as osp
import tarfile
from testpath import assert_isfile, assert_isdir
from testpath.tempdir import TemporaryDirectory
import zipfile

from flit_core import buildapi

samples_dir = osp.join(osp.dirname(__file__), 'samples')

@contextmanager
def cwd(directory):
    prev = os.getcwd()
    os.chdir(directory)
    try:
        yield
    finally:
        os.chdir(prev)

def test_get_build_requires():
    # This module can be inspected (for docstring & __version__) without
    # importing it, so there are no build dependencies.
    with cwd(osp.join(samples_dir,'pep517')):
        assert buildapi.get_requires_for_build_wheel() == []
        assert buildapi.get_requires_for_build_editable() == []
        assert buildapi.get_requires_for_build_sdist() == []

def test_get_build_requires_pep621_nodynamic():
    # This module isn't inspected because version & description are specified
    # as static metadata in pyproject.toml, so there are no build dependencies
    with cwd(osp.join(samples_dir, 'pep621_nodynamic')):
        assert buildapi.get_requires_for_build_wheel() == []
        assert buildapi.get_requires_for_build_editable() == []
        assert buildapi.get_requires_for_build_sdist() == []

def test_get_build_requires_import():
    # This one has to be imported, so its runtime dependencies are also
    # build dependencies.
    expected = ["numpy >=1.16.0"]
    with cwd(osp.join(samples_dir, 'constructed_version')):
        assert buildapi.get_requires_for_build_wheel() == expected
        assert buildapi.get_requires_for_build_editable() == expected
        assert buildapi.get_requires_for_build_sdist() == expected

def test_build_wheel():
    with TemporaryDirectory() as td, cwd(osp.join(samples_dir,'pep517')):
        filename = buildapi.build_wheel(td)
        assert filename.endswith('.whl'), filename
        assert_isfile(osp.join(td, filename))
        assert zipfile.is_zipfile(osp.join(td, filename))
        with zipfile.ZipFile(osp.join(td, filename)) as zip:
            assert "module1.py" in zip.namelist()
            assert "module1.pth" not in zip.namelist()

def test_build_wheel_pep621():
    with TemporaryDirectory() as td, cwd(osp.join(samples_dir, 'pep621')):
        filename = buildapi.build_wheel(td)
        assert filename.endswith('.whl'), filename
        assert_isfile(osp.join(td, filename))
        assert zipfile.is_zipfile(osp.join(td, filename))

def test_build_editable():
    with TemporaryDirectory() as td, cwd(osp.join(samples_dir,'pep517')):
        filename = buildapi.build_editable(td)
        assert filename.endswith('.whl'), filename
        assert_isfile(osp.join(td, filename))
        assert zipfile.is_zipfile(osp.join(td, filename))
        with zipfile.ZipFile(osp.join(td, filename)) as zip:
            assert "module1.py" not in zip.namelist()
            assert "module1.pth" in zip.namelist()

def test_build_sdist():
    with TemporaryDirectory() as td, cwd(osp.join(samples_dir,'pep517')):
        filename = buildapi.build_sdist(td)
        assert filename.endswith('.tar.gz'), filename
        assert_isfile(osp.join(td, filename))
        assert tarfile.is_tarfile(osp.join(td, filename))

def test_prepare_metadata_for_build_wheel():
    with TemporaryDirectory() as td, cwd(osp.join(samples_dir,'pep517')):
        dirname = buildapi.prepare_metadata_for_build_wheel(td)
        assert dirname.endswith('.dist-info'), dirname
        assert_isdir(osp.join(td, dirname))
        assert_isfile(osp.join(td, dirname, 'METADATA'))

def test_prepare_metadata_for_build_editable():
    with TemporaryDirectory() as td, cwd(osp.join(samples_dir,'pep517')):
        dirname = buildapi.prepare_metadata_for_build_editable(td)
        assert dirname.endswith('.dist-info'), dirname
        assert_isdir(osp.join(td, dirname))
        assert_isfile(osp.join(td, dirname, 'METADATA'))
