import types
from abc import ABCMeta, abstractmethod
from typing import Any, Awaitable, Callable, Dict, Optional, Type, TypeVar

_T = TypeVar("_T")


class TestRunner(metaclass=ABCMeta):
    """
    Encapsulates a running event loop. Every call made through this object will use the same event
    loop.
    """

    def __enter__(self) -> 'TestRunner':
        return self

    def __exit__(self, exc_type: Optional[Type[BaseException]],
                 exc_val: Optional[BaseException],
                 exc_tb: Optional[types.TracebackType]) -> Optional[bool]:
        self.close()
        return None

    @abstractmethod
    def close(self) -> None:
        """Close the event loop."""

    @abstractmethod
    def call(self, func: Callable[..., Awaitable[_T]],
             *args: object, **kwargs: Dict[str, Any]) -> _T:
        """
        Call the given function within the backend's event loop.

        :param func: a callable returning an awaitable
        :param args: positional arguments to call ``func`` with
        :param kwargs: keyword arguments to call ``func`` with
        :return: the return value of ``func``
        """
