"""Tests of flit_core building itself"""
import os
import os.path as osp
import pytest
import tarfile
from testpath import assert_isdir, assert_isfile
import zipfile

from flit_core import buildapi

@pytest.fixture()
def cwd_project():
    proj_dir = osp.dirname(osp.dirname(osp.abspath(buildapi.__file__)))
    if not osp.isfile(osp.join(proj_dir, 'pyproject.toml')):
        pytest.skip("need flit_core source directory")

    old_cwd = os.getcwd()
    try:
        os.chdir(proj_dir)
        yield
    finally:
        os.chdir(old_cwd)


def test_prepare_metadata(tmp_path, cwd_project):
    tmp_path = str(tmp_path)
    dist_info = buildapi.prepare_metadata_for_build_wheel(tmp_path)

    assert dist_info.endswith('.dist-info')
    assert dist_info.startswith('flit_core')
    dist_info = osp.join(tmp_path, dist_info)
    assert_isdir(dist_info)

    assert_isfile(osp.join(dist_info, 'WHEEL'))
    assert_isfile(osp.join(dist_info, 'METADATA'))


def test_wheel(tmp_path, cwd_project):
    tmp_path = str(tmp_path)
    filename = buildapi.build_wheel(tmp_path)

    assert filename.endswith('.whl')
    assert filename.startswith('flit_core')
    path = osp.join(tmp_path, filename)
    assert_isfile(path)
    assert zipfile.is_zipfile(path)


def test_sdist(tmp_path, cwd_project):
    tmp_path = str(tmp_path)
    filename = buildapi.build_sdist(tmp_path)

    assert filename.endswith('.tar.gz')
    assert filename.startswith('flit_core')
    path = osp.join(tmp_path, filename)
    assert_isfile(path)
    assert tarfile.is_tarfile(path)
