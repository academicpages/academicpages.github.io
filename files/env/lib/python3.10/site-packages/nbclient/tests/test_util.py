import asyncio
from unittest.mock import MagicMock

import pytest
import tornado

from nbclient.util import run_hook, run_sync


@run_sync
async def some_async_function():
    await asyncio.sleep(0.01)
    return 42


def test_nested_asyncio_with_existing_ioloop():
    ioloop = asyncio.new_event_loop()
    try:
        asyncio.set_event_loop(ioloop)
        assert some_async_function() == 42
        assert asyncio.get_event_loop() is ioloop
    finally:
        asyncio._set_running_loop(None)  # it seems nest_asyncio doesn't reset this


def test_nested_asyncio_with_no_ioloop():
    asyncio.set_event_loop(None)
    try:
        assert some_async_function() == 42
    finally:
        asyncio._set_running_loop(None)  # it seems nest_asyncio doesn't reset this


def test_nested_asyncio_with_tornado():
    # This tests if tornado accepts the pure-Python Futures, see
    # https://github.com/tornadoweb/tornado/issues/2753
    # https://github.com/erdewit/nest_asyncio/issues/23
    asyncio.set_event_loop(asyncio.new_event_loop())
    ioloop = tornado.ioloop.IOLoop.current()

    async def some_async_function():
        future = asyncio.ensure_future(asyncio.sleep(0.1))
        # this future is a different future after nested-asyncio has patched
        # the asyncio module, check if tornado likes it:
        ioloop.add_future(future, lambda f: f.result())
        await future
        return 42

    def some_sync_function():
        return run_sync(some_async_function)()

    async def run():
        # calling some_async_function directly should work
        assert await some_async_function() == 42
        # but via a sync function (using nested-asyncio) can lead to issues:
        # https://github.com/tornadoweb/tornado/issues/2753
        assert some_sync_function() == 42

    ioloop.run_sync(run)


@pytest.mark.asyncio
async def test_run_hook_sync():
    some_sync_function = MagicMock()
    await run_hook(some_sync_function)
    assert some_sync_function.call_count == 1


@pytest.mark.asyncio
async def test_run_hook_async():
    hook = MagicMock(return_value=some_async_function())
    await run_hook(hook)
    assert hook.call_count == 1
