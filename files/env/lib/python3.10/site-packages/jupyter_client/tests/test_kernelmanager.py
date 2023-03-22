"""Tests for the KernelManager"""
# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
import asyncio
import concurrent.futures
import json
import os
import signal
import sys
import time
from subprocess import PIPE

import pytest
from jupyter_core import paths
from traitlets.config.loader import Config

from ..manager import _ShutdownStatus
from ..manager import start_new_async_kernel
from ..manager import start_new_kernel
from .utils import AsyncKMSubclass
from .utils import SyncKMSubclass
from jupyter_client import AsyncKernelManager
from jupyter_client import KernelManager

pjoin = os.path.join

TIMEOUT = 30


@pytest.fixture(params=["tcp", "ipc"])
def transport(request):
    if sys.platform == "win32" and request.param == "ipc":  #
        pytest.skip("Transport 'ipc' not supported on Windows.")
    return request.param


@pytest.fixture
def config(transport):
    c = Config()
    c.KernelManager.transport = transport
    if transport == "ipc":
        c.KernelManager.ip = "test"
    return c


def _install_kernel(name="signaltest", extra_env=None):
    if extra_env is None:
        extra_env = {}
    kernel_dir = pjoin(paths.jupyter_data_dir(), "kernels", name)
    os.makedirs(kernel_dir)
    with open(pjoin(kernel_dir, "kernel.json"), "w") as f:
        f.write(
            json.dumps(
                {
                    "argv": [
                        sys.executable,
                        "-m",
                        "jupyter_client.tests.signalkernel",
                        "-f",
                        "{connection_file}",
                    ],
                    "display_name": "Signal Test Kernel",
                    "env": {"TEST_VARS": "${TEST_VARS}:test_var_2", **extra_env},
                }
            )
        )


@pytest.fixture
def install_kernel():
    return _install_kernel()


def install_kernel_dont_shutdown():
    _install_kernel("signaltest-no-shutdown", {"NO_SHUTDOWN_REPLY": "1"})


def install_kernel_dont_terminate():
    return _install_kernel(
        "signaltest-no-terminate", {"NO_SHUTDOWN_REPLY": "1", "NO_SIGTERM_REPLY": "1"}
    )


@pytest.fixture
def start_kernel():
    km, kc = start_new_kernel(kernel_name="signaltest")
    yield km, kc
    kc.stop_channels()
    km.shutdown_kernel()
    assert km.context.closed


@pytest.fixture
def km(config):
    km = KernelManager(config=config)
    return km


@pytest.fixture
def km_subclass(config):
    km = SyncKMSubclass(config=config)
    return km


@pytest.fixture
def zmq_context():
    import zmq

    ctx = zmq.Context()
    yield ctx
    ctx.term()


@pytest.fixture(params=[AsyncKernelManager, AsyncKMSubclass])
def async_km(request, config):
    km = request.param(config=config)
    return km


@pytest.fixture
def async_km_subclass(config):
    km = AsyncKMSubclass(config=config)
    return km


@pytest.fixture
async def start_async_kernel():
    km, kc = await start_new_async_kernel(kernel_name="signaltest")
    yield km, kc
    kc.stop_channels()
    await km.shutdown_kernel()
    assert km.context.closed


class TestKernelManagerShutDownGracefully:
    parameters = (
        "name, install, expected",
        [
            ("signaltest", _install_kernel, _ShutdownStatus.ShutdownRequest),
            (
                "signaltest-no-shutdown",
                install_kernel_dont_shutdown,
                _ShutdownStatus.SigtermRequest,
            ),
            (
                "signaltest-no-terminate",
                install_kernel_dont_terminate,
                _ShutdownStatus.SigkillRequest,
            ),
        ],
    )

    @pytest.mark.skipif(sys.platform == "win32", reason="Windows doesn't support signals")
    @pytest.mark.parametrize(*parameters)
    def test_signal_kernel_subprocesses(self, name, install, expected):
        # ipykernel doesn't support 3.6 and this test uses async shutdown_request
        if expected == _ShutdownStatus.ShutdownRequest and sys.version_info < (3, 7):
            pytest.skip()
        install()
        km, kc = start_new_kernel(kernel_name=name)
        assert km._shutdown_status == _ShutdownStatus.Unset
        assert km.is_alive()
        # kc.execute("1")
        kc.stop_channels()
        km.shutdown_kernel()

        if expected == _ShutdownStatus.ShutdownRequest:
            expected = [expected, _ShutdownStatus.SigtermRequest]
        else:
            expected = [expected]

        assert km._shutdown_status in expected

    @pytest.mark.asyncio
    @pytest.mark.skipif(sys.platform == "win32", reason="Windows doesn't support signals")
    @pytest.mark.parametrize(*parameters)
    async def test_async_signal_kernel_subprocesses(self, name, install, expected):
        install()
        km, kc = await start_new_async_kernel(kernel_name=name)
        assert km._shutdown_status == _ShutdownStatus.Unset
        assert await km.is_alive()
        # kc.execute("1")
        kc.stop_channels()
        await km.shutdown_kernel()

        if expected == _ShutdownStatus.ShutdownRequest:
            expected = [expected, _ShutdownStatus.SigtermRequest]
        else:
            expected = [expected]

        assert km._shutdown_status in expected


class TestKernelManager:
    def test_lifecycle(self, km):
        km.start_kernel(stdout=PIPE, stderr=PIPE)
        kc = km.client()
        assert km.is_alive()
        is_done = km.ready.done()
        assert is_done
        km.restart_kernel(now=True)
        assert km.is_alive()
        km.interrupt_kernel()
        assert isinstance(km, KernelManager)
        kc.stop_channels()
        km.shutdown_kernel(now=True)
        assert km.context.closed

    def test_get_connect_info(self, km):
        cinfo = km.get_connection_info()
        keys = sorted(cinfo.keys())
        expected = sorted(
            [
                "ip",
                "transport",
                "hb_port",
                "shell_port",
                "stdin_port",
                "iopub_port",
                "control_port",
                "key",
                "signature_scheme",
            ]
        )
        assert keys == expected

    @pytest.mark.skipif(sys.platform == "win32", reason="Windows doesn't support signals")
    def test_signal_kernel_subprocesses(self, install_kernel, start_kernel):

        km, kc = start_kernel

        def execute(cmd):
            request_id = kc.execute(cmd)
            while True:
                reply = kc.get_shell_msg(TIMEOUT)
                if reply["parent_header"]["msg_id"] == request_id:
                    break
            content = reply["content"]
            assert content["status"] == "ok"
            return content

        N = 5
        for i in range(N):
            execute("start")
        time.sleep(1)  # make sure subprocs stay up
        reply = execute("check")
        assert reply["user_expressions"]["poll"] == [None] * N

        # start a job on the kernel to be interrupted
        kc.execute("sleep")
        time.sleep(1)  # ensure sleep message has been handled before we interrupt
        km.interrupt_kernel()
        reply = kc.get_shell_msg(TIMEOUT)
        content = reply["content"]
        assert content["status"] == "ok"
        assert content["user_expressions"]["interrupted"]
        # wait up to 10s for subprocesses to handle signal
        for i in range(100):
            reply = execute("check")
            if reply["user_expressions"]["poll"] != [-signal.SIGINT] * N:
                time.sleep(0.1)
            else:
                break
        # verify that subprocesses were interrupted
        assert reply["user_expressions"]["poll"] == [-signal.SIGINT] * N

    def test_start_new_kernel(self, install_kernel, start_kernel):
        km, kc = start_kernel
        assert km.is_alive()
        assert kc.is_alive()
        assert km.context.closed is False

    def _env_test_body(self, kc):
        def execute(cmd):
            request_id = kc.execute(cmd)
            while True:
                reply = kc.get_shell_msg(TIMEOUT)
                if reply["parent_header"]["msg_id"] == request_id:
                    break
            content = reply["content"]
            assert content["status"] == "ok"
            return content

        reply = execute("env")
        assert reply is not None
        assert reply["user_expressions"]["env"] == "test_var_1:test_var_2"

    def test_templated_kspec_env(self, install_kernel, start_kernel):
        km, kc = start_kernel
        assert km.is_alive()
        assert kc.is_alive()
        assert km.context.closed is False
        self._env_test_body(kc)

    def test_cleanup_context(self, km):
        assert km.context is not None
        km.cleanup_resources(restart=False)
        assert km.context.closed

    def test_no_cleanup_shared_context(self, zmq_context):
        """kernel manager does not terminate shared context"""
        km = KernelManager(context=zmq_context)
        assert km.context == zmq_context
        assert km.context is not None

        km.cleanup_resources(restart=False)
        assert km.context.closed is False
        assert zmq_context.closed is False

    def test_subclass_callables(self, km_subclass):
        km_subclass.reset_counts()

        km_subclass.start_kernel(stdout=PIPE, stderr=PIPE)
        assert km_subclass.call_count("start_kernel") == 1
        assert km_subclass.call_count("_launch_kernel") == 1

        is_alive = km_subclass.is_alive()
        assert is_alive
        km_subclass.reset_counts()

        km_subclass.restart_kernel(now=True)
        assert km_subclass.call_count("restart_kernel") == 1
        assert km_subclass.call_count("shutdown_kernel") == 1
        assert km_subclass.call_count("interrupt_kernel") == 1
        assert km_subclass.call_count("_kill_kernel") == 1
        assert km_subclass.call_count("cleanup_resources") == 1
        assert km_subclass.call_count("start_kernel") == 1
        assert km_subclass.call_count("_launch_kernel") == 1
        assert km_subclass.call_count("signal_kernel") == 1

        is_alive = km_subclass.is_alive()
        assert is_alive
        assert km_subclass.call_count("is_alive") >= 1
        km_subclass.reset_counts()

        km_subclass.interrupt_kernel()
        assert km_subclass.call_count("interrupt_kernel") == 1
        assert km_subclass.call_count("signal_kernel") == 1

        assert isinstance(km_subclass, KernelManager)
        km_subclass.reset_counts()

        km_subclass.shutdown_kernel(now=False)
        assert km_subclass.call_count("shutdown_kernel") == 1
        assert km_subclass.call_count("interrupt_kernel") == 1
        assert km_subclass.call_count("request_shutdown") == 1
        assert km_subclass.call_count("finish_shutdown") == 1
        assert km_subclass.call_count("cleanup_resources") == 1
        assert km_subclass.call_count("signal_kernel") == 1
        assert km_subclass.call_count("is_alive") >= 1

        is_alive = km_subclass.is_alive()
        assert is_alive is False
        assert km_subclass.call_count("is_alive") >= 1
        assert km_subclass.context.closed


class TestParallel:
    @pytest.mark.timeout(TIMEOUT)
    def test_start_sequence_kernels(self, config, install_kernel):
        """Ensure that a sequence of kernel startups doesn't break anything."""
        self._run_signaltest_lifecycle(config)
        self._run_signaltest_lifecycle(config)
        self._run_signaltest_lifecycle(config)

    @pytest.mark.timeout(TIMEOUT + 10)
    def test_start_parallel_thread_kernels(self, config, install_kernel):
        if config.KernelManager.transport == "ipc":  # FIXME
            pytest.skip("IPC transport is currently not working for this test!")
        self._run_signaltest_lifecycle(config)

        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as thread_executor:
            future1 = thread_executor.submit(self._run_signaltest_lifecycle, config)
            future2 = thread_executor.submit(self._run_signaltest_lifecycle, config)
            future1.result()
            future2.result()

    @pytest.mark.timeout(TIMEOUT)
    @pytest.mark.skipif(
        (sys.platform == "darwin") and (sys.version_info >= (3, 6)) and (sys.version_info < (3, 8)),
        reason='"Bad file descriptor" error',
    )
    def test_start_parallel_process_kernels(self, config, install_kernel):
        if config.KernelManager.transport == "ipc":  # FIXME
            pytest.skip("IPC transport is currently not working for this test!")
        self._run_signaltest_lifecycle(config)
        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as thread_executor:
            future1 = thread_executor.submit(self._run_signaltest_lifecycle, config)
            with concurrent.futures.ProcessPoolExecutor(max_workers=1) as process_executor:
                future2 = process_executor.submit(self._run_signaltest_lifecycle, config)
                future2.result()
            future1.result()

    @pytest.mark.timeout(TIMEOUT)
    @pytest.mark.skipif(
        (sys.platform == "darwin") and (sys.version_info >= (3, 6)) and (sys.version_info < (3, 8)),
        reason='"Bad file descriptor" error',
    )
    def test_start_sequence_process_kernels(self, config, install_kernel):
        if config.KernelManager.transport == "ipc":  # FIXME
            pytest.skip("IPC transport is currently not working for this test!")
        self._run_signaltest_lifecycle(config)
        with concurrent.futures.ProcessPoolExecutor(max_workers=1) as pool_executor:
            future = pool_executor.submit(self._run_signaltest_lifecycle, config)
            future.result()

    def _prepare_kernel(self, km, startup_timeout=TIMEOUT, **kwargs):
        km.start_kernel(**kwargs)
        kc = km.client()
        kc.start_channels()
        try:
            kc.wait_for_ready(timeout=startup_timeout)
        except RuntimeError:
            kc.stop_channels()
            km.shutdown_kernel()
            raise

        return kc

    def _run_signaltest_lifecycle(self, config=None):
        km = KernelManager(config=config, kernel_name="signaltest")
        kc = self._prepare_kernel(km, stdout=PIPE, stderr=PIPE)

        def execute(cmd):
            request_id = kc.execute(cmd)
            while True:
                reply = kc.get_shell_msg(TIMEOUT)
                if reply["parent_header"]["msg_id"] == request_id:
                    break
            content = reply["content"]
            assert content["status"] == "ok"
            return content

        execute("start")
        assert km.is_alive()
        execute("check")
        assert km.is_alive()

        km.restart_kernel(now=True)
        assert km.is_alive()
        execute("check")

        km.shutdown_kernel()
        assert km.context.closed
        kc.stop_channels()


@pytest.mark.asyncio
class TestAsyncKernelManager:
    async def test_lifecycle(self, async_km):
        await async_km.start_kernel(stdout=PIPE, stderr=PIPE)
        is_alive = await async_km.is_alive()
        assert is_alive
        is_ready = async_km.ready.done()
        assert is_ready
        await async_km.restart_kernel(now=True)
        is_alive = await async_km.is_alive()
        assert is_alive
        await async_km.interrupt_kernel()
        assert isinstance(async_km, AsyncKernelManager)
        await async_km.shutdown_kernel(now=True)
        is_alive = await async_km.is_alive()
        assert is_alive is False
        assert async_km.context.closed

    async def test_get_connect_info(self, async_km):
        cinfo = async_km.get_connection_info()
        keys = sorted(cinfo.keys())
        expected = sorted(
            [
                "ip",
                "transport",
                "hb_port",
                "shell_port",
                "stdin_port",
                "iopub_port",
                "control_port",
                "key",
                "signature_scheme",
            ]
        )
        assert keys == expected

    @pytest.mark.timeout(10)
    @pytest.mark.skipif(sys.platform == "win32", reason="Windows doesn't support signals")
    async def test_signal_kernel_subprocesses(self, install_kernel, start_async_kernel):

        km, kc = start_async_kernel

        async def execute(cmd):
            request_id = kc.execute(cmd)
            while True:
                reply = await kc.get_shell_msg(TIMEOUT)
                if reply["parent_header"]["msg_id"] == request_id:
                    break
            content = reply["content"]
            assert content["status"] == "ok"
            return content

        # Ensure that shutdown_kernel and stop_channels are called at the end of the test.
        # Note: we cannot use addCleanup(<func>) for these since it doesn't prpperly handle
        # coroutines - which km.shutdown_kernel now is.
        N = 5
        for i in range(N):
            await execute("start")
        await asyncio.sleep(1)  # make sure subprocs stay up
        reply = await execute("check")
        assert reply["user_expressions"]["poll"] == [None] * N

        # start a job on the kernel to be interrupted
        request_id = kc.execute("sleep")
        await asyncio.sleep(1)  # ensure sleep message has been handled before we interrupt
        await km.interrupt_kernel()
        while True:
            reply = await kc.get_shell_msg(TIMEOUT)
            if reply["parent_header"]["msg_id"] == request_id:
                break
        content = reply["content"]
        assert content["status"] == "ok"
        assert content["user_expressions"]["interrupted"] is True
        # wait up to 5s for subprocesses to handle signal
        for i in range(50):
            reply = await execute("check")
            if reply["user_expressions"]["poll"] != [-signal.SIGINT] * N:
                await asyncio.sleep(0.1)
            else:
                break
        # verify that subprocesses were interrupted
        assert reply["user_expressions"]["poll"] == [-signal.SIGINT] * N

    @pytest.mark.timeout(10)
    async def test_start_new_async_kernel(self, install_kernel, start_async_kernel):
        km, kc = start_async_kernel
        is_alive = await km.is_alive()
        assert is_alive
        is_alive = await kc.is_alive()
        assert is_alive

    async def test_subclass_callables(self, async_km_subclass):
        async_km_subclass.reset_counts()

        await async_km_subclass.start_kernel(stdout=PIPE, stderr=PIPE)
        assert async_km_subclass.call_count("start_kernel") == 1
        assert async_km_subclass.call_count("_launch_kernel") == 1

        is_alive = await async_km_subclass.is_alive()
        assert is_alive
        assert async_km_subclass.call_count("is_alive") >= 1
        async_km_subclass.reset_counts()

        await async_km_subclass.restart_kernel(now=True)
        assert async_km_subclass.call_count("restart_kernel") == 1
        assert async_km_subclass.call_count("shutdown_kernel") == 1
        assert async_km_subclass.call_count("interrupt_kernel") == 1
        assert async_km_subclass.call_count("_kill_kernel") == 1
        assert async_km_subclass.call_count("cleanup_resources") == 1
        assert async_km_subclass.call_count("start_kernel") == 1
        assert async_km_subclass.call_count("_launch_kernel") == 1
        assert async_km_subclass.call_count("signal_kernel") == 1

        is_alive = await async_km_subclass.is_alive()
        assert is_alive
        assert async_km_subclass.call_count("is_alive") >= 1
        async_km_subclass.reset_counts()

        await async_km_subclass.interrupt_kernel()
        assert async_km_subclass.call_count("interrupt_kernel") == 1
        assert async_km_subclass.call_count("signal_kernel") == 1

        assert isinstance(async_km_subclass, AsyncKernelManager)
        async_km_subclass.reset_counts()

        await async_km_subclass.shutdown_kernel(now=False)
        assert async_km_subclass.call_count("shutdown_kernel") == 1
        assert async_km_subclass.call_count("interrupt_kernel") == 1
        assert async_km_subclass.call_count("request_shutdown") == 1
        assert async_km_subclass.call_count("finish_shutdown") == 1
        assert async_km_subclass.call_count("cleanup_resources") == 1
        assert async_km_subclass.call_count("signal_kernel") == 1
        assert async_km_subclass.call_count("is_alive") >= 1

        is_alive = await async_km_subclass.is_alive()
        assert is_alive is False
        assert async_km_subclass.call_count("is_alive") >= 1
        assert async_km_subclass.context.closed
