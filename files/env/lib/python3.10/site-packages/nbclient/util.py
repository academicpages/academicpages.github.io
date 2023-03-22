"""General utility methods"""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

import asyncio
import inspect
import sys
from typing import Any, Awaitable, Callable, Optional, Union


def check_ipython() -> None:
    # original from vaex/asyncio.py
    IPython = sys.modules.get('IPython')
    if IPython:
        version_str = IPython.__version__  # type: ignore
        # We get rid of any trailing ".dev"
        version_str = version_str.replace(".dev", "")

        IPython_version = tuple(map(int, version_str.split('.')))
        if IPython_version < (7, 0, 0):
            raise RuntimeError(
                f'You are using IPython {IPython.__version__} '  # type: ignore
                'while we require 7.0.0+, please update IPython'
            )


def check_patch_tornado() -> None:
    """If tornado is imported, add the patched asyncio.Future to its tuple of acceptable Futures"""
    # original from vaex/asyncio.py
    if 'tornado' in sys.modules:
        import tornado.concurrent  # type: ignore

        if asyncio.Future not in tornado.concurrent.FUTURES:
            tornado.concurrent.FUTURES = tornado.concurrent.FUTURES + (  # type: ignore
                asyncio.Future,
            )


def just_run(coro: Awaitable) -> Any:
    """Make the coroutine run, even if there is an event loop running (using nest_asyncio)"""
    # original from vaex/asyncio.py
    loop = asyncio._get_running_loop()
    if loop is None:
        had_running_loop = False
        try:
            loop = asyncio.get_event_loop()
        except RuntimeError:
            # we can still get 'There is no current event loop in ...'
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
    else:
        had_running_loop = True
    if had_running_loop:
        # if there is a running loop, we patch using nest_asyncio
        # to have reentrant event loops
        check_ipython()
        import nest_asyncio

        nest_asyncio.apply()
        check_patch_tornado()
    return loop.run_until_complete(coro)


def run_sync(coro: Callable) -> Callable:
    """Runs a coroutine and blocks until it has executed.

    An event loop is created if no one already exists. If an event loop is
    already running, this event loop execution is nested into the already
    running one if `nest_asyncio` is set to True.

    Parameters
    ----------
    coro : coroutine
        The coroutine to be executed.

    Returns
    -------
    result :
        Whatever the coroutine returns.
    """

    def wrapped(*args, **kwargs):
        return just_run(coro(*args, **kwargs))

    wrapped.__doc__ = coro.__doc__
    return wrapped


async def ensure_async(obj: Union[Awaitable, Any]) -> Any:
    """Convert a non-awaitable object to a coroutine if needed,
    and await it if it was not already awaited.
    """
    if inspect.isawaitable(obj):
        try:
            result = await obj
        except RuntimeError as e:
            if str(e) == 'cannot reuse already awaited coroutine':
                # obj is already the coroutine's result
                return obj
            raise
        return result
    # obj doesn't need to be awaited
    return obj


async def run_hook(hook: Optional[Callable], **kwargs) -> None:
    if hook is None:
        return
    res = hook(**kwargs)
    if inspect.isawaitable(res):
        await res
