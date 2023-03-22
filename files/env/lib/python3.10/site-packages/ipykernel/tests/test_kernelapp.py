import os
import threading
import time
from unittest.mock import patch

import pytest

from ipykernel.kernelapp import IPKernelApp

from .conftest import MockKernel

try:
    import trio
except ImportError:
    trio = None


@pytest.mark.skipif(os.name == "nt", reason="requires ipc")
def test_init_ipc_socket():
    app = IPKernelApp(transport="ipc")
    app.init_sockets()
    app.cleanup_connection_file()
    app.close()


def test_blackhole():
    app = IPKernelApp()
    app.no_stderr = True
    app.no_stdout = True
    app.init_blackhole()


def test_start_app():
    app = IPKernelApp()
    app.kernel = MockKernel()

    def trigger_stop():
        time.sleep(1)
        app.io_loop.add_callback(app.io_loop.stop)

    thread = threading.Thread(target=trigger_stop)
    thread.start()
    app.init_sockets()
    app.start()
    app.cleanup_connection_file()
    app.kernel.destroy()
    app.close()


@pytest.mark.skipif(trio is None, reason="requires trio")
def test_trio_loop():
    app = IPKernelApp(trio_loop=True)
    app.kernel = MockKernel()
    app.init_sockets()
    with patch("ipykernel.trio_runner.TrioRunner.run", lambda _: None):
        app.start()
    app.cleanup_connection_file()
    app.io_loop.add_callback(app.io_loop.stop)
    app.kernel.destroy()
    app.close()
