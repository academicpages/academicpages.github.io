"""Test installation of notebook extensions"""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

import glob
import os
import pytest
import sys
import tarfile
import zipfile
from io import BytesIO, StringIO
from os.path import basename, join as pjoin
from traitlets.tests.utils import check_help_all_output
from unittest import TestCase

from unittest.mock import patch

from ipython_genutils import py3compat
from ipython_genutils.tempdir import TemporaryDirectory
from notebook import nbextensions
from notebook.nbextensions import (install_nbextension, check_nbextension,
    enable_nbextension, disable_nbextension,
    install_nbextension_python, uninstall_nbextension_python,
    enable_nbextension_python, disable_nbextension_python, _get_config_dir,
    validate_nbextension, validate_nbextension_python
)

from notebook.config_manager import BaseJSONConfigManager


def touch(file_name, mtime=None):
    """ensure a file exists, and set its modification time

    returns the modification time of the file
    """
    open(file_name, 'a').close()
    # set explicit mtime
    if mtime:
        atime = os.stat(file_name).st_atime
        os.utime(file_name, (atime, mtime))
    return os.stat(file_name).st_mtime


def test_help_output():
    check_help_all_output('notebook.nbextensions')
    check_help_all_output('notebook.nbextensions', ['enable'])
    check_help_all_output('notebook.nbextensions', ['disable'])
    check_help_all_output('notebook.nbextensions', ['install'])
    check_help_all_output('notebook.nbextensions', ['uninstall'])


class TestInstallNBExtension(TestCase):

    def tempdir(self):
        td = TemporaryDirectory()
        self.tempdirs.append(td)
        return py3compat.cast_unicode(td.name)

    def setUp(self):
        # Any TemporaryDirectory objects appended to this list will be cleaned
        # up at the end of the test run.
        self.tempdirs = []

        @self.addCleanup
        def cleanup_tempdirs():
            for d in self.tempdirs:
                d.cleanup()

        self.src = self.tempdir()
        self.files = files = [
            pjoin('ƒile'),
            pjoin('∂ir', 'ƒile1'),
            pjoin('∂ir', '∂ir2', 'ƒile2'),
        ]
        for file_name in files:
            fullpath = os.path.join(self.src, file_name)
            parent = os.path.dirname(fullpath)
            if not os.path.exists(parent):
                os.makedirs(parent)
            touch(fullpath)

        self.test_dir = self.tempdir()
        self.data_dir = os.path.join(self.test_dir, 'data')
        self.config_dir = os.path.join(self.test_dir, 'config')
        self.system_data_dir = os.path.join(self.test_dir, 'system_data')
        self.system_path = [self.system_data_dir]
        self.system_nbext = os.path.join(self.system_data_dir, 'nbextensions')

        # Patch out os.environ so that tests are isolated from the real OS
        # environment.
        self.patch_env = patch.dict('os.environ', {
            'JUPYTER_CONFIG_DIR': self.config_dir,
            'JUPYTER_DATA_DIR': self.data_dir,
        })
        self.patch_env.start()
        self.addCleanup(self.patch_env.stop)

        # Patch out the system path os that we consistently use our own
        # temporary directory instead.
        self.patch_system_path = patch.object(
            nbextensions, 'SYSTEM_JUPYTER_PATH', self.system_path
        )
        self.patch_system_path.start()
        self.addCleanup(self.patch_system_path.stop)

    def assert_dir_exists(self, path):
        if not os.path.exists(path):
            do_exist = os.listdir(os.path.dirname(path))
            self.fail(f"{path} should exist (found {do_exist})")

    def assert_not_dir_exists(self, path):
        if os.path.exists(path):
            self.fail(f"{path} should not exist")

    def assert_installed(self, relative_path, user=False):
        if user:
            nbext = pjoin(self.data_dir, 'nbextensions')
        else:
            nbext = self.system_nbext
        self.assert_dir_exists(
            pjoin(nbext, relative_path)
        )

    def assert_not_installed(self, relative_path, user=False):
        if user:
            nbext = pjoin(self.data_dir, 'nbextensions')
        else:
            nbext = self.system_nbext
        self.assert_not_dir_exists(
            pjoin(nbext, relative_path)
        )

    def test_create_data_dir(self):
        """install_nbextension when data_dir doesn't exist"""
        with TemporaryDirectory() as td:
            data_dir = os.path.join(td, self.data_dir)
            with patch.dict('os.environ', {
                'JUPYTER_DATA_DIR': data_dir,
            }):
                install_nbextension(self.src, user=True)
                self.assert_dir_exists(data_dir)
                for file_name in self.files:
                    self.assert_installed(
                        pjoin(basename(self.src), file_name),
                        user=True,
                    )

    def test_create_nbextensions_user(self):
        with TemporaryDirectory() as td:
            install_nbextension(self.src, user=True)
            self.assert_installed(
                pjoin(basename(self.src), 'ƒile'),
                user=True
            )

    def test_create_nbextensions_system(self):
        with TemporaryDirectory() as td:
            self.system_nbext = pjoin(td, 'nbextensions')
            with patch.object(nbextensions, 'SYSTEM_JUPYTER_PATH', [td]):
                install_nbextension(self.src, user=False)
                self.assert_installed(
                    pjoin(basename(self.src), 'ƒile'),
                    user=False
                )

    def test_single_file(self):
        file_name = self.files[0]
        install_nbextension(pjoin(self.src, file_name))
        self.assert_installed(file_name)

    def test_single_dir(self):
        d = '∂ir'
        install_nbextension(pjoin(self.src, d))
        self.assert_installed(self.files[-1])

    def test_single_dir_trailing_slash(self):
        d = '∂ir/'
        install_nbextension(pjoin(self.src, d))
        self.assert_installed(self.files[-1])
        if os.name == 'nt':
            d = '∂ir\\'
            install_nbextension(pjoin(self.src, d))
            self.assert_installed(self.files[-1])

    def test_destination_file(self):
        file_name = self.files[0]
        install_nbextension(pjoin(self.src, file_name), destination = 'ƒiledest')
        self.assert_installed('ƒiledest')

    def test_destination_dir(self):
        d = '∂ir'
        install_nbextension(pjoin(self.src, d), destination = 'ƒiledest2')
        self.assert_installed(pjoin('ƒiledest2', '∂ir2', 'ƒile2'))

    def test_install_nbextension(self):
        with self.assertRaises(TypeError):
            install_nbextension(glob.glob(pjoin(self.src, '*')))

    def test_overwrite_file(self):
        with TemporaryDirectory() as d:
            fname = 'ƒ.js'
            src = pjoin(d, fname)
            with open(src, 'w') as f:
                f.write('first')
            mtime = touch(src)
            dest = pjoin(self.system_nbext, fname)
            install_nbextension(src)
            with open(src, 'w') as f:
                f.write('overwrite')
            mtime = touch(src, mtime - 100)
            install_nbextension(src, overwrite=True)
            with open(dest) as f:
                self.assertEqual(f.read(), 'overwrite')

    def test_overwrite_dir(self):
        with TemporaryDirectory() as src:
            base = basename(src)
            fname = 'ƒ.js'
            touch(pjoin(src, fname))
            install_nbextension(src)
            self.assert_installed(pjoin(base, fname))
            os.remove(pjoin(src, fname))
            fname2 = '∂.js'
            touch(pjoin(src, fname2))
            install_nbextension(src, overwrite=True)
            self.assert_installed(pjoin(base, fname2))
            self.assert_not_installed(pjoin(base, fname))

    def test_update_file(self):
        with TemporaryDirectory() as d:
            fname = 'ƒ.js'
            src = pjoin(d, fname)
            with open(src, 'w') as f:
                f.write('first')
            mtime = touch(src)
            install_nbextension(src)
            self.assert_installed(fname)
            dest = pjoin(self.system_nbext, fname)
            os.stat(dest).st_mtime
            with open(src, 'w') as f:
                f.write('overwrite')
            touch(src, mtime + 10)
            install_nbextension(src)
            with open(dest) as f:
                self.assertEqual(f.read(), 'overwrite')

    def test_skip_old_file(self):
        with TemporaryDirectory() as d:
            fname = 'ƒ.js'
            src = pjoin(d, fname)
            mtime = touch(src)
            install_nbextension(src)
            self.assert_installed(fname)
            dest = pjoin(self.system_nbext, fname)
            old_mtime = os.stat(dest).st_mtime

            mtime = touch(src, mtime - 100)
            install_nbextension(src)
            new_mtime = os.stat(dest).st_mtime
            self.assertEqual(new_mtime, old_mtime)

    def test_quiet(self):
        stdout = StringIO()
        stderr = StringIO()
        with patch.object(sys, 'stdout', stdout), \
             patch.object(sys, 'stderr', stderr):
            install_nbextension(self.src)
        self.assertEqual(stdout.getvalue(), '')
        self.assertEqual(stderr.getvalue(), '')

    def test_install_zip(self):
        path = pjoin(self.src, "myjsext.zip")
        with zipfile.ZipFile(path, 'w') as f:
            f.writestr("a.js", b"b();")
            f.writestr("foo/a.js", b"foo();")
        install_nbextension(path)
        self.assert_installed("a.js")
        self.assert_installed(pjoin("foo", "a.js"))

    def test_install_tar(self):
        def _add_file(f, fname, buf):
            info = tarfile.TarInfo(fname)
            info.size = len(buf)
            f.addfile(info, BytesIO(buf))

        for i,ext in enumerate((".tar.gz", ".tgz", ".tar.bz2")):
            path = pjoin(self.src, "myjsext" + ext)
            with tarfile.open(path, 'w') as f:
                _add_file(f, f"b{i}.js", b"b();")
                _add_file(f, f"foo/b{i}.js", b"foo();")
            install_nbextension(path)
            self.assert_installed(f"b{i}.js")
            self.assert_installed(pjoin("foo", f"b{i}.js"))

    def test_install_url(self):
        def fake_urlretrieve(url, dest):
            touch(dest)
        save_urlretrieve = nbextensions.urlretrieve
        nbextensions.urlretrieve = fake_urlretrieve
        try:
            install_nbextension("http://example.com/path/to/foo.js")
            self.assert_installed("foo.js")
            install_nbextension("https://example.com/path/to/another/bar.js")
            self.assert_installed("bar.js")
            install_nbextension("https://example.com/path/to/another/bar.js",
                                destination = 'foobar.js')
            self.assert_installed("foobar.js")
        finally:
            nbextensions.urlretrieve = save_urlretrieve

    def test_check_nbextension(self):
        with TemporaryDirectory() as d:
            f = 'ƒ.js'
            src = pjoin(d, f)
            touch(src)
            install_nbextension(src, user=True)

        assert check_nbextension(f, user=True)
        assert check_nbextension([f], user=True)
        assert not check_nbextension([f, pjoin('dne', f)], user=True)

    @pytest.mark.skipif(sys.platform == "win32", reason="do not run on windows")
    def test_install_symlink(self):
        with TemporaryDirectory() as d:
            f = 'ƒ.js'
            src = pjoin(d, f)
            touch(src)
            install_nbextension(src, symlink=True)
        dest = pjoin(self.system_nbext, f)
        assert os.path.islink(dest)
        link = os.readlink(dest)
        self.assertEqual(link, src)

    @pytest.mark.skipif(sys.platform == "win32", reason="do not run on windows")
    def test_overwrite_broken_symlink(self):
        with TemporaryDirectory() as d:
            f = 'ƒ.js'
            f2 = 'ƒ2.js'
            src = pjoin(d, f)
            src2 = pjoin(d, f2)
            touch(src)
            install_nbextension(src, symlink=True)
            os.rename(src, src2)
            install_nbextension(src2, symlink=True, overwrite=True, destination=f)
        dest = pjoin(self.system_nbext, f)
        assert os.path.islink(dest)
        link = os.readlink(dest)
        self.assertEqual(link, src2)

    @pytest.mark.skipif(sys.platform == "win32", reason="do not run on windows")
    def test_install_symlink_destination(self):
        with TemporaryDirectory() as d:
            f = 'ƒ.js'
            flink = 'ƒlink.js'
            src = pjoin(d, f)
            touch(src)
            install_nbextension(src, symlink=True, destination=flink)
        dest = pjoin(self.system_nbext, flink)
        assert os.path.islink(dest)
        link = os.readlink(dest)
        self.assertEqual(link, src)

    @pytest.mark.skipif(sys.platform == "win32", reason="do not run on windows")
    def test_install_symlink_bad(self):
        with self.assertRaises(ValueError):
            install_nbextension("http://example.com/foo.js", symlink=True)

        with TemporaryDirectory() as d:
            zf = 'ƒ.zip'
            zsrc = pjoin(d, zf)
            with zipfile.ZipFile(zsrc, 'w') as z:
                z.writestr("a.js", b"b();")

            with self.assertRaises(ValueError):
                install_nbextension(zsrc, symlink=True)

    def test_install_destination_bad(self):
        with TemporaryDirectory() as d:
            zf = 'ƒ.zip'
            zsrc = pjoin(d, zf)
            with zipfile.ZipFile(zsrc, 'w') as z:
                z.writestr("a.js", b"b();")

            with self.assertRaises(ValueError):
                install_nbextension(zsrc, destination='foo')

    def test_nbextension_enable(self):
        with TemporaryDirectory() as d:
            f = 'ƒ.js'
            src = pjoin(d, f)
            touch(src)
            install_nbextension(src, user=True)
            enable_nbextension(section='notebook', require='ƒ')

        config_dir = os.path.join(_get_config_dir(user=True), 'nbconfig')
        cm = BaseJSONConfigManager(config_dir=config_dir)
        enabled = cm.get('notebook').get('load_extensions', {}).get('ƒ', False)
        assert enabled

    def test_nbextension_disable(self):
        self.test_nbextension_enable()
        disable_nbextension(section='notebook', require='ƒ')

        config_dir = os.path.join(_get_config_dir(user=True), 'nbconfig')
        cm = BaseJSONConfigManager(config_dir=config_dir)
        enabled = cm.get('notebook').get('load_extensions', {}).get('ƒ', False)
        assert not enabled


    def _mock_extension_spec_meta(self, section='notebook'):
        return {
            'section': section,
            'src': 'mockextension',
            'dest': '_mockdestination',
            'require': '_mockdestination/index'
        }

    def _inject_mock_extension(self, section='notebook'):
        outer_file = __file__

        meta = self._mock_extension_spec_meta(section)

        class mock():
            __file__ = outer_file

            @staticmethod
            def _jupyter_nbextension_paths():
                return [meta]

        import sys
        sys.modules['mockextension'] = mock

    def test_nbextensionpy_files(self):
        self._inject_mock_extension()
        install_nbextension_python('mockextension')

        assert check_nbextension('_mockdestination/index.js')
        assert check_nbextension(['_mockdestination/index.js'])

    def test_nbextensionpy_user_files(self):
        self._inject_mock_extension()
        install_nbextension_python('mockextension', user=True)

        assert check_nbextension('_mockdestination/index.js', user=True)
        assert check_nbextension(['_mockdestination/index.js'], user=True)

    def test_nbextensionpy_uninstall_files(self):
        self._inject_mock_extension()
        install_nbextension_python('mockextension', user=True)
        uninstall_nbextension_python('mockextension', user=True)

        assert not check_nbextension('_mockdestination/index.js')
        assert not check_nbextension(['_mockdestination/index.js'])

    def test_nbextensionpy_enable(self):
        self._inject_mock_extension('notebook')
        install_nbextension_python('mockextension', user=True)
        enable_nbextension_python('mockextension')

        config_dir = os.path.join(_get_config_dir(user=True), 'nbconfig')
        cm = BaseJSONConfigManager(config_dir=config_dir)
        enabled = cm.get('notebook').get('load_extensions', {}).get('_mockdestination/index', False)
        assert enabled

    def test_nbextensionpy_disable(self):
        self._inject_mock_extension('notebook')
        install_nbextension_python('mockextension', user=True)
        enable_nbextension_python('mockextension')
        disable_nbextension_python('mockextension', user=True)

        config_dir = os.path.join(_get_config_dir(user=True), 'nbconfig')
        cm = BaseJSONConfigManager(config_dir=config_dir)
        enabled = cm.get('notebook').get('load_extensions', {}).get('_mockdestination/index', False)
        assert not enabled

    def test_nbextensionpy_validate(self):
        self._inject_mock_extension('notebook')

        paths = install_nbextension_python('mockextension', user=True)
        enable_nbextension_python('mockextension')

        meta = self._mock_extension_spec_meta()
        warnings = validate_nbextension_python(meta, paths[0])
        self.assertEqual([], warnings, warnings)

    def test_nbextensionpy_validate_bad(self):
        # Break the metadata (correct file will still be copied)
        self._inject_mock_extension('notebook')

        paths = install_nbextension_python('mockextension', user=True)

        enable_nbextension_python('mockextension')

        meta = self._mock_extension_spec_meta()
        meta.update(require="bad-require")

        warnings = validate_nbextension_python(meta, paths[0])
        self.assertNotEqual([], warnings, warnings)

    def test_nbextension_validate(self):
        # Break the metadata (correct file will still be copied)
        self._inject_mock_extension('notebook')

        install_nbextension_python('mockextension', user=True)
        enable_nbextension_python('mockextension')

        warnings = validate_nbextension("_mockdestination/index")
        self.assertEqual([], warnings, warnings)

    def test_nbextension_validate_bad(self):
        warnings = validate_nbextension("this-doesn't-exist")
        self.assertNotEqual([], warnings, warnings)

