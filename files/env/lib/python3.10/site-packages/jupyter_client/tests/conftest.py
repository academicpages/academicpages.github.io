import asyncio
import os
import sys

import pytest
from jupyter_core import paths

from .utils import test_env

try:
    import resource
except ImportError:
    # Windows
    resource = None

pjoin = os.path.join


# Handle resource limit
# Ensure a minimal soft limit of DEFAULT_SOFT if the current hard limit is at least that much.
if resource is not None:
    soft, hard = resource.getrlimit(resource.RLIMIT_NOFILE)

    DEFAULT_SOFT = 4096
    if hard >= DEFAULT_SOFT:
        soft = DEFAULT_SOFT

    if hard < soft:
        hard = soft

    resource.setrlimit(resource.RLIMIT_NOFILE, (soft, hard))


if os.name == "nt" and sys.version_info >= (3, 7):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


@pytest.fixture
def event_loop():
    # Make sure we test against a selector event loop
    # since pyzmq doesn't like the proactor loop.
    # This fixture is picked up by pytest-asyncio
    if os.name == "nt" and sys.version_info >= (3, 7):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    loop = asyncio.SelectorEventLoop()
    try:
        yield loop
    finally:
        loop.close()


@pytest.fixture(autouse=True)
def env():
    env_patch = test_env()
    env_patch.start()
    yield
    env_patch.stop()


@pytest.fixture()
def kernel_dir():
    return pjoin(paths.jupyter_data_dir(), 'kernels')
