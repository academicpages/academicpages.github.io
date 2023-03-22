from contextvars import ContextVar
from typing import Optional
import sys

current_async_library_cvar = ContextVar(
    "current_async_library_cvar", default=None
)  # type: ContextVar[Optional[str]]


class AsyncLibraryNotFoundError(RuntimeError):
    pass


def current_async_library() -> str:
    """Detect which async library is currently running.

    The following libraries are currently supported:

    ================   ===========  ============================
    Library             Requires     Magic string
    ================   ===========  ============================
    **Trio**            Trio v0.6+   ``"trio"``
    **Curio**           -            ``"curio"``
    **asyncio**                      ``"asyncio"``
    **Trio-asyncio**    v0.8.2+     ``"trio"`` or ``"asyncio"``,
                                    depending on current mode
    ================   ===========  ============================

    Returns:
      A string like ``"trio"``.

    Raises:
      AsyncLibraryNotFoundError: if called from synchronous context,
        or if the current async library was not recognized.

    Examples:

        .. code-block:: python3

           from sniffio import current_async_library

           async def generic_sleep(seconds):
               library = current_async_library()
               if library == "trio":
                   import trio
                   await trio.sleep(seconds)
               elif library == "asyncio":
                   import asyncio
                   await asyncio.sleep(seconds)
               # ... and so on ...
               else:
                   raise RuntimeError(f"Unsupported library {library!r}")

    """
    value = current_async_library_cvar.get()
    if value is not None:
        return value

    # Sniff for curio (for now)
    if 'curio' in sys.modules:
        from curio.meta import curio_running
        if curio_running():
            return 'curio'

    # Need to sniff for asyncio
    if "asyncio" in sys.modules:
        import asyncio
        try:
            current_task = asyncio.current_task  # type: ignore[attr-defined]
        except AttributeError:
            current_task = asyncio.Task.current_task  # type: ignore[attr-defined]
        try:
            if current_task() is not None:
                if (3, 7) <= sys.version_info:
                    # asyncio has contextvars support, and we're in a task, so
                    # we can safely cache the sniffed value
                    current_async_library_cvar.set("asyncio")
                return "asyncio"
        except RuntimeError:
            pass
    raise AsyncLibraryNotFoundError(
        "unknown async library, or not in async context"
    )
