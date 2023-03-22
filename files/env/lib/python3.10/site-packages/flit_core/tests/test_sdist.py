from io import BytesIO
import os.path as osp
from pathlib import Path
import tarfile
from testpath import assert_isfile

from flit_core import sdist

samples_dir = Path(__file__).parent / 'samples'

def test_make_sdist(tmp_path):
    # Smoke test of making a complete sdist
    builder = sdist.SdistBuilder.from_ini_path(samples_dir / 'package1.toml')
    builder.build(tmp_path)
    assert_isfile(tmp_path / 'package1-0.1.tar.gz')


def test_make_sdist_pep621(tmp_path):
    builder = sdist.SdistBuilder.from_ini_path(samples_dir / 'pep621' / 'pyproject.toml')
    path = builder.build(tmp_path)
    assert path == tmp_path / 'module1-0.1.tar.gz'
    assert_isfile(path)


def test_make_sdist_pep621_nodynamic(tmp_path):
    builder = sdist.SdistBuilder.from_ini_path(
        samples_dir / 'pep621_nodynamic' / 'pyproject.toml'
    )
    path = builder.build(tmp_path)
    assert path == tmp_path / 'module1-0.3.tar.gz'
    assert_isfile(path)


def test_clean_tarinfo():
    with tarfile.open(mode='w', fileobj=BytesIO()) as tf:
        ti = tf.gettarinfo(str(samples_dir / 'module1.py'))
    cleaned = sdist.clean_tarinfo(ti, mtime=42)
    assert cleaned.uid == 0
    assert cleaned.uname == ''
    assert cleaned.mtime == 42


def test_include_exclude():
    builder = sdist.SdistBuilder.from_ini_path(
        samples_dir / 'inclusion' / 'pyproject.toml'
    )
    files = builder.apply_includes_excludes(builder.select_files())

    assert osp.join('doc', 'test.rst') in files
    assert osp.join('doc', 'test.txt') not in files
    assert osp.join('doc', 'subdir', 'test.txt') in files
