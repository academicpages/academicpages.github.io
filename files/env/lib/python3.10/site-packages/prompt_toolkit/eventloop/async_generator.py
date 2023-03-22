"""
Implementation for async generators.
"""
from queue import Empty, Full, Queue
from threading import Event
from typing import (
    TYPE_CHECKING,
    AsyncGenerator,
    Awaitable,
    Callable,
    Iterable,
    TypeVar,
    Union,
)

from .async_context_manager import asynccontextmanager
from .utils import get_event_loop, run_in_executor_with_context

__all__ = [
    "aclosing",
    "generator_to_async_generator",
]


if TYPE_CHECKING:
    # Thanks: https://github.com/python/typeshed/blob/main/stdlib/contextlib.pyi
    from typing_extensions import Protocol

    class _SupportsAclose(Protocol):
        def aclose(self) -> Awaitable[object]:
            ...

    _SupportsAcloseT = TypeVar("_SupportsAcloseT", bound=_SupportsAclose)


@asynccontextmanager
async def aclosing(
    thing: "_SupportsAcloseT",
) -> AsyncGenerator["_SupportsAcloseT", None]:
    "Similar to `contextlib.aclosing`, in Python 3.10."
    try:
        yield thing
    finally:
        await thing.aclose()


# By default, choose a buffer size that's a good balance between having enough
# throughput, but not consuming too much memory. We use this to consume a sync
# generator of completions as an async generator. If the queue size is very
# small (like 1), consuming the completions goes really slow (when there are a
# lot of items). If the queue size would be unlimited or too big, this can
# cause overconsumption of memory, and cause CPU time spent producing items
# that are no longer needed (if the consumption of the async generator stops at
# some point). We need a fixed size in order to get some back pressure from the
# async consumer to the sync producer. We choose 1000 by default here. If we
# have around 50k completions, measurements show that 1000 is still
# significantly faster than a buffer of 100.
DEFAULT_BUFFER_SIZE: int = 1000

_T = TypeVar("_T")


class _Done:
    pass


async def generator_to_async_generator(
    get_iterable: Callable[[], Iterable[_T]],
    buffer_size: int = DEFAULT_BUFFER_SIZE,
) -> AsyncGenerator[_T, None]:
    """
    Turn a generator or iterable into an async generator.

    This works by running the generator in a background thread.

    :param get_iterable: Function that returns a generator or iterable when
        called.
    :param buffer_size: Size of the queue between the async consumer and the
        synchronous generator that produces items.
    """
    quitting = False
    # NOTE: We are limiting the queue size in order to have back-pressure.
    q: Queue[Union[_T, _Done]] = Queue(maxsize=buffer_size)
    loop = get_event_loop()

    def runner() -> None:
        """
        Consume the generator in background thread.
        When items are received, they'll be pushed to the queue.
        """
        try:
            for item in get_iterable():
                # When this async generator was cancelled (closed), stop this
                # thread.
                if quitting:
                    return

                while True:
                    try:
                        q.put(item, timeout=1)
                    except Full:
                        if quitting:
                            return
                        continue
                    else:
                        break

        finally:
            while True:
                try:
                    q.put(_Done(), timeout=1)
                except Full:
                    if quitting:
                        return
                    continue
                else:
                    break

    # Start background thread.
    runner_f = run_in_executor_with_context(runner)

    try:
        while True:
            try:
                item = q.get_nowait()
            except Empty:
                item = await loop.run_in_executor(None, q.get)
            if isinstance(item, _Done):
                break
            else:
                yield item
    finally:
        # When this async generator is closed (GeneratorExit exception, stop
        # the background thread as well. - we don't need that anymore.)
        quitting = True

        # Wait for the background thread to finish. (should happen right after
        # the last item is yielded).
        await runner_f
