"""Tests for the KernelManager"""
# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
import asyncio
import json
import os
import sys

import pytest
from jupyter_core import paths
from traitlets.config.loader import Config
from traitlets.log import get_logger

from jupyter_client.ioloop import AsyncIOLoopKernelManager
from jupyter_client.ioloop import IOLoopKernelManager

pjoin = os.path.join


def _install_kernel(name="problemtest", extra_env=None):
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
                        "jupyter_client.tests.problemkernel",
                        "-f",
                        "{connection_file}",
                    ],
                    "display_name": "Problematic Test Kernel",
                    "env": {"TEST_VARS": "${TEST_VARS}:test_var_2", **extra_env},
                }
            )
        )
    return name


@pytest.fixture
def install_kernel():
    return _install_kernel("problemtest")


@pytest.fixture
def install_fail_kernel():
    return _install_kernel("problemtest-fail", extra_env={"FAIL_ON_START": "1"})


@pytest.fixture
def install_slow_fail_kernel():
    return _install_kernel(
        "problemtest-slow", extra_env={"STARTUP_DELAY": "5", "FAIL_ON_START": "1"}
    )


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


@pytest.fixture
def debug_logging():
    get_logger().setLevel("DEBUG")


@pytest.mark.asyncio
async def test_restart_check(config, install_kernel, debug_logging):
    """Test that the kernel is restarted and recovers"""
    # If this test failes, run it with --log-cli-level=DEBUG to inspect
    N_restarts = 1
    config.KernelRestarter.restart_limit = N_restarts
    config.KernelRestarter.debug = True
    km = IOLoopKernelManager(kernel_name=install_kernel, config=config)

    cbs = 0
    restarts = [asyncio.Future() for i in range(N_restarts)]

    def cb():
        nonlocal cbs
        if cbs >= N_restarts:
            raise RuntimeError("Kernel restarted more than %d times!" % N_restarts)
        restarts[cbs].set_result(True)
        cbs += 1

    try:
        km.start_kernel()
        km.add_restart_callback(cb, 'restart')
    except BaseException:
        if km.has_kernel:
            km.shutdown_kernel()
        raise

    try:
        for i in range(N_restarts + 1):
            kc = km.client()
            kc.start_channels()
            kc.wait_for_ready(timeout=60)
            kc.stop_channels()
            if i < N_restarts:
                # Kill without cleanup to simulate crash:
                await km.provisioner.kill()
                await restarts[i]
                # Wait for kill + restart
                max_wait = 10.0
                waited = 0.0
                while waited < max_wait and km.is_alive():
                    await asyncio.sleep(0.1)
                    waited += 0.1
                while waited < max_wait and not km.is_alive():
                    await asyncio.sleep(0.1)
                    waited += 0.1

        assert cbs == N_restarts
        assert km.is_alive()

    finally:

        km.shutdown_kernel(now=True)
        assert km.context.closed


@pytest.mark.asyncio
async def test_restarter_gives_up(config, install_fail_kernel, debug_logging):
    """Test that the restarter gives up after reaching the restart limit"""
    # If this test failes, run it with --log-cli-level=DEBUG to inspect
    N_restarts = 1
    config.KernelRestarter.restart_limit = N_restarts
    config.KernelRestarter.debug = True
    km = IOLoopKernelManager(kernel_name=install_fail_kernel, config=config)

    cbs = 0
    restarts = [asyncio.Future() for i in range(N_restarts)]

    def cb():
        nonlocal cbs
        if cbs >= N_restarts:
            raise RuntimeError("Kernel restarted more than %d times!" % N_restarts)
        restarts[cbs].set_result(True)
        cbs += 1

    died = asyncio.Future()

    def on_death():
        died.set_result(True)

    try:
        km.start_kernel()
        km.add_restart_callback(cb, 'restart')
        km.add_restart_callback(on_death, 'dead')
    except BaseException:
        if km.has_kernel:
            km.shutdown_kernel()
        raise

    try:
        for i in range(N_restarts):
            await restarts[i]

        assert await died
        assert cbs == N_restarts

    finally:

        km.shutdown_kernel(now=True)
        assert km.context.closed


@pytest.mark.asyncio
async def test_async_restart_check(config, install_kernel, debug_logging):
    """Test that the kernel is restarted and recovers"""
    # If this test failes, run it with --log-cli-level=DEBUG to inspect
    N_restarts = 1
    config.KernelRestarter.restart_limit = N_restarts
    config.KernelRestarter.debug = True
    km = AsyncIOLoopKernelManager(kernel_name=install_kernel, config=config)

    cbs = 0
    restarts = [asyncio.Future() for i in range(N_restarts)]

    def cb():
        nonlocal cbs
        if cbs >= N_restarts:
            raise RuntimeError("Kernel restarted more than %d times!" % N_restarts)
        restarts[cbs].set_result(True)
        cbs += 1

    try:
        await km.start_kernel()
        km.add_restart_callback(cb, 'restart')
    except BaseException:
        if km.has_kernel:
            await km.shutdown_kernel()
        raise

    try:
        for i in range(N_restarts + 1):
            kc = km.client()
            kc.start_channels()
            await kc.wait_for_ready(timeout=60)
            kc.stop_channels()
            if i < N_restarts:
                # Kill without cleanup to simulate crash:
                await km.provisioner.kill()
                await restarts[i]
                # Wait for kill + restart
                max_wait = 10.0
                waited = 0.0
                while waited < max_wait and await km.is_alive():
                    await asyncio.sleep(0.1)
                    waited += 0.1
                while waited < max_wait and not await km.is_alive():
                    await asyncio.sleep(0.1)
                    waited += 0.1

        assert cbs == N_restarts
        assert await km.is_alive()

    finally:

        await km.shutdown_kernel(now=True)
        assert km.context.closed


@pytest.mark.asyncio
async def test_async_restarter_gives_up(config, install_slow_fail_kernel, debug_logging):
    """Test that the restarter gives up after reaching the restart limit"""
    # If this test failes, run it with --log-cli-level=DEBUG to inspect
    N_restarts = 2
    config.KernelRestarter.restart_limit = N_restarts
    config.KernelRestarter.debug = True
    config.KernelRestarter.stable_start_time = 30.0
    km = AsyncIOLoopKernelManager(kernel_name=install_slow_fail_kernel, config=config)

    cbs = 0
    restarts = [asyncio.Future() for i in range(N_restarts)]

    def cb():
        nonlocal cbs
        if cbs >= N_restarts:
            raise RuntimeError("Kernel restarted more than %d times!" % N_restarts)
        restarts[cbs].set_result(True)
        cbs += 1

    died = asyncio.Future()

    def on_death():
        died.set_result(True)

    try:
        await km.start_kernel()
        km.add_restart_callback(cb, 'restart')
        km.add_restart_callback(on_death, 'dead')
    except BaseException:
        if km.has_kernel:
            await km.shutdown_kernel()
        raise

    try:
        await asyncio.gather(*restarts)

        assert await died
        assert cbs == N_restarts

    finally:

        await km.shutdown_kernel(now=True)
        assert km.context.closed
