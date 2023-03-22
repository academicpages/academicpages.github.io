from abc import ABCMeta, abstractmethod
from types import TracebackType
from typing import Optional, Type, TypeVar

T = TypeVar("T")


class AsyncResource(metaclass=ABCMeta):
    """
    Abstract base class for all closeable asynchronous resources.

    Works as an asynchronous context manager which returns the instance itself on enter, and calls
    :meth:`aclose` on exit.
    """

    async def __aenter__(self: T) -> T:
        return self

    async def __aexit__(self, exc_type: Optional[Type[BaseException]],
                        exc_val: Optional[BaseException],
                        exc_tb: Optional[TracebackType]) -> None:
        await self.aclose()

    @abstractmethod
    async def aclose(self) -> None:
        """Close the resource."""
