"""Tests for KernelManager"""
# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
import os
import tempfile
from unittest import mock

from jupyter_client.kernelspec import KernelSpec
from jupyter_client.manager import KernelManager


def test_connection_file_real_path():
    """Verify realpath is used when formatting connection file"""
    with mock.patch("os.path.realpath") as patched_realpath:
        patched_realpath.return_value = "foobar"
        km = KernelManager(
            connection_file=os.path.join(tempfile.gettempdir(), "kernel-test.json"),
            kernel_name="test_kernel",
        )

        # KernelSpec and launch args have to be mocked as we don't have an actual kernel on disk
        km._kernel_spec = KernelSpec(
            resource_dir="test",
            **{
                "argv": ["python.exe", "-m", "test_kernel", "-f", "{connection_file}"],
                "env": {},
                "display_name": "test_kernel",
                "language": "python",
                "metadata": {},
            },
        )
        km._launch_args = {}
        cmds = km.format_kernel_cmd()
        assert cmds[4] == "foobar"
