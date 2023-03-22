"""Test the jupyter_client public API
"""
# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
import jupyter_client
from jupyter_client import connect
from jupyter_client import launcher


def test_kms():
    for base in ("", "Async", "Multi"):
        KM = base + "KernelManager"
        assert KM in dir(jupyter_client)


def test_kcs():
    for base in ("", "Blocking", "Async"):
        KM = base + "KernelClient"
        assert KM in dir(jupyter_client)


def test_launcher():
    for name in launcher.__all__:
        assert name in dir(jupyter_client)


def test_connect():
    for name in connect.__all__:
        assert name in dir(jupyter_client)
