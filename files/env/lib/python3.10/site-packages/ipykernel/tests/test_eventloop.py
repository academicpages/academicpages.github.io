"""Test eventloop integration"""

import asyncio
import os
import sys
import threading
import time

import pytest
import tornado

from ipykernel.eventloops import enable_gui, loop_asyncio, loop_cocoa, loop_tk

from .utils import execute, flush_channels, start_new_kernel

KC = KM = None


def setup():
    """start the global kernel (if it isn't running) and return its client"""
    global KM, KC
    KM, KC = start_new_kernel()
    flush_channels(KC)


def teardown():
    assert KM is not None
    assert KC is not None
    KC.stop_channels()
    KM.shutdown_kernel(now=True)


async_code = """
from ipykernel.tests._asyncio_utils import async_func
async_func()
"""


@pytest.mark.skipif(tornado.version_info < (5,), reason="only relevant on tornado 5")
def test_asyncio_interrupt():
    assert KM is not None
    assert KC is not None
    flush_channels(KC)
    msg_id, content = execute("%gui asyncio", KC)
    assert content["status"] == "ok", content

    flush_channels(KC)
    msg_id, content = execute(async_code, KC)
    assert content["status"] == "ok", content

    KM.interrupt_kernel()

    flush_channels(KC)
    msg_id, content = execute(async_code, KC)
    assert content["status"] == "ok"


windows_skip = pytest.mark.skipif(os.name == "nt", reason="causing failures on windows")


@windows_skip
@pytest.mark.skipif(sys.platform == "darwin", reason="hangs on macos")
def test_tk_loop(kernel):
    def do_thing():
        time.sleep(1)
        try:
            kernel.app_wrapper.app.quit()
        # guard for tk failing to start (if there is no display)
        except AttributeError:
            pass

    t = threading.Thread(target=do_thing)
    t.start()
    # guard for tk failing to start (if there is no display)
    try:
        loop_tk(kernel)
    except Exception:
        pass
    t.join()


@windows_skip
def test_asyncio_loop(kernel):
    def do_thing():
        loop.call_soon(loop.stop)

    loop = asyncio.get_event_loop()
    loop.call_soon(do_thing)
    loop_asyncio(kernel)


@windows_skip
def test_enable_gui(kernel):
    enable_gui("tk", kernel)


@pytest.mark.skipif(sys.platform != "darwin", reason="MacOS-only")
def test_cocoa_loop(kernel):
    loop_cocoa(kernel)
