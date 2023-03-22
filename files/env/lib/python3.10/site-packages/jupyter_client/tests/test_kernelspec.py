"""Tests for the KernelSpecManager"""
# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
import copy
import json
import os
import sys
import tempfile
import unittest
from io import StringIO
from logging import StreamHandler
from os.path import join as pjoin
from subprocess import PIPE
from subprocess import Popen
from subprocess import STDOUT
from tempfile import TemporaryDirectory

import pytest
from jupyter_core import paths

from .utils import install_kernel
from .utils import sample_kernel_json
from .utils import test_env
from jupyter_client import kernelspec


class KernelSpecTests(unittest.TestCase):
    def setUp(self):
        self.env_patch = test_env()
        self.env_patch.start()
        self.sample_kernel_dir = install_kernel(
            pjoin(paths.jupyter_data_dir(), "kernels"), name="sample"
        )

        self.ksm = kernelspec.KernelSpecManager()

        td2 = TemporaryDirectory()
        self.addCleanup(td2.cleanup)
        self.installable_kernel = td2.name
        with open(pjoin(self.installable_kernel, "kernel.json"), "w") as f:
            json.dump(sample_kernel_json, f)

    def tearDown(self):
        self.env_patch.stop()

    def test_find_kernel_specs(self):
        kernels = self.ksm.find_kernel_specs()
        self.assertEqual(kernels["sample"], self.sample_kernel_dir)

    def test_allowed_kernel_names(self):
        ksm = kernelspec.KernelSpecManager()
        ksm.allowed_kernelspecs = ["foo"]
        kernels = ksm.find_kernel_specs()
        assert not len(kernels)

    def test_deprecated_whitelist(self):
        ksm = kernelspec.KernelSpecManager()
        ksm.whitelist = ["bar"]
        kernels = ksm.find_kernel_specs()
        assert not len(kernels)

    def test_get_kernel_spec(self):
        ks = self.ksm.get_kernel_spec("SAMPLE")  # Case insensitive
        self.assertEqual(ks.resource_dir, self.sample_kernel_dir)
        self.assertEqual(ks.argv, sample_kernel_json["argv"])
        self.assertEqual(ks.display_name, sample_kernel_json["display_name"])
        self.assertEqual(ks.env, {})
        self.assertEqual(ks.metadata, {})

    def test_find_all_specs(self):
        kernels = self.ksm.get_all_specs()
        self.assertEqual(kernels["sample"]["resource_dir"], self.sample_kernel_dir)
        self.assertIsNotNone(kernels["sample"]["spec"])

    def test_kernel_spec_priority(self):
        td = TemporaryDirectory()
        self.addCleanup(td.cleanup)
        sample_kernel = install_kernel(td.name, name="sample")
        self.ksm.kernel_dirs.append(td.name)
        kernels = self.ksm.find_kernel_specs()
        self.assertEqual(kernels["sample"], self.sample_kernel_dir)
        self.ksm.kernel_dirs.insert(0, td.name)
        kernels = self.ksm.find_kernel_specs()
        self.assertEqual(kernels["sample"], sample_kernel)

    def test_install_kernel_spec(self):
        self.ksm.install_kernel_spec(self.installable_kernel, kernel_name="tstinstalled", user=True)
        self.assertIn("tstinstalled", self.ksm.find_kernel_specs())

        # install again works
        self.ksm.install_kernel_spec(self.installable_kernel, kernel_name="tstinstalled", user=True)

    def test_install_kernel_spec_prefix(self):
        td = TemporaryDirectory()
        self.addCleanup(td.cleanup)
        capture = StringIO()
        handler = StreamHandler(capture)
        self.ksm.log.addHandler(handler)
        self.ksm.install_kernel_spec(
            self.installable_kernel, kernel_name="tstinstalled", prefix=td.name
        )
        captured = capture.getvalue()
        self.ksm.log.removeHandler(handler)
        self.assertIn("may not be found", captured)
        self.assertNotIn("tstinstalled", self.ksm.find_kernel_specs())

        # add prefix to path, so we find the spec
        self.ksm.kernel_dirs.append(pjoin(td.name, "share", "jupyter", "kernels"))
        self.assertIn("tstinstalled", self.ksm.find_kernel_specs())

        # Run it again, no warning this time because we've added it to the path
        capture = StringIO()
        handler = StreamHandler(capture)
        self.ksm.log.addHandler(handler)
        self.ksm.install_kernel_spec(
            self.installable_kernel, kernel_name="tstinstalled", prefix=td.name
        )
        captured = capture.getvalue()
        self.ksm.log.removeHandler(handler)
        self.assertNotIn("may not be found", captured)

    @pytest.mark.skipif(
        not (os.name != "nt" and not os.access("/usr/local/share", os.W_OK)),
        reason="needs Unix system without root privileges",
    )
    def test_cant_install_kernel_spec(self):
        with self.assertRaises(OSError):
            self.ksm.install_kernel_spec(
                self.installable_kernel, kernel_name="tstinstalled", user=False
            )

    def test_remove_kernel_spec(self):
        path = self.ksm.remove_kernel_spec("sample")
        self.assertEqual(path, self.sample_kernel_dir)

    def test_remove_kernel_spec_app(self):
        p = Popen(
            [
                sys.executable,
                "-m",
                "jupyter_client.kernelspecapp",
                "remove",
                "sample",
                "-f",
            ],
            stdout=PIPE,
            stderr=STDOUT,
            env=os.environ,
        )
        out, _ = p.communicate()
        self.assertEqual(p.returncode, 0, out.decode("utf8", "replace"))

    def test_validate_kernel_name(self):
        for good in [
            "julia-0.4",
            "ipython",
            "R",
            "python_3",
            "Haskell-1-2-3",
        ]:
            assert kernelspec._is_valid_kernel_name(good)

        for bad in [
            "has space",
            "ünicode",
            "%percent",
            "question?",
        ]:
            assert not kernelspec._is_valid_kernel_name(bad)

    def test_subclass(self):
        """Test get_all_specs in subclasses that override find_kernel_specs"""
        ksm = self.ksm
        resource_dir = tempfile.gettempdir()
        native_name = kernelspec.NATIVE_KERNEL_NAME
        native_kernel = ksm.get_kernel_spec(native_name)

        class MyKSM(kernelspec.KernelSpecManager):
            def get_kernel_spec(self, name):
                spec = copy.copy(native_kernel)
                if name == "fake":
                    spec.name = name
                    spec.resource_dir = resource_dir
                elif name == native_name:
                    pass
                else:
                    raise KeyError(name)
                return spec

            def find_kernel_specs(self):
                return {
                    "fake": resource_dir,
                    native_name: native_kernel.resource_dir,
                }

        # ensure that get_all_specs doesn't raise if only
        # find_kernel_specs and get_kernel_spec are defined
        myksm = MyKSM()
        specs = myksm.get_all_specs()
        assert sorted(specs) == ["fake", native_name]
