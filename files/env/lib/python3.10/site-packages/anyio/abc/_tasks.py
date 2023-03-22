import typing
from abc import ABCMeta, abstractmethod
from types import TracebackType
from typing import Any, Callable, Coroutine, Optional, Type, TypeVar
from warnings import warn

if typing.TYPE_CHECKING:
    from anyio._core._tasks import CancelScope

T_Retval = TypeVar('T_Retval')


class TaskStatus(metaclass=ABCMeta):
    @abstractmethod
    def started(self, value: object = None) -> None:
        """
        Signal that the task has started.

        :param value: object passed back to the starter of the task
        """


class TaskGroup(metaclass=ABCMeta):
    """
    Groups several asynchronous tasks together.

    :ivar cancel_scope: the cancel scope inherited by all child tasks
    :vartype cancel_scope: CancelScope
    """

    cancel_scope: 'CancelScope'

    async def spawn(self, func: Callable[..., Coroutine[Any, Any, Any]],
                    *args: object, name: object = None) -> None:
        """
        Start a new task in this task group.

        :param func: a coroutine function
        :param args: positional arguments to call the function with
        :param name: name of the task, for the purposes of introspection and debugging

        .. deprecated:: 3.0
           Use :meth:`start_soon` instead. If your code needs AnyIO 2 compatibility, you
           can keep using this until AnyIO 4.

        """
        warn('spawn() is deprecated -- use start_soon() (without the "await") instead',
             DeprecationWarning)
        self.start_soon(func, *args, name=name)

    @abstractmethod
    def start_soon(self, func: Callable[..., Coroutine[Any, Any, Any]],
                   *args: object, name: object = None) -> None:
        """
        Start a new task in this task group.

        :param func: a coroutine function
        :param args: positional arguments to call the function with
        :param name: name of the task, for the purposes of introspection and debugging

        .. versionadded:: 3.0
        """

    @abstractmethod
    async def start(self, func: Callable[..., Coroutine[Any, Any, Any]],
                    *args: object, name: object = None) -> object:
        """
        Start a new task and wait until it signals for readiness.

        :param func: a coroutine function
        :param args: positional arguments to call the function with
        :param name: name of the task, for the purposes of introspection and debugging
        :return: the value passed to ``task_status.started()``
        :raises RuntimeError: if the task finishes without calling ``task_status.started()``

        .. versionadded:: 3.0
        """

    @abstractmethod
    async def __aenter__(self) -> 'TaskGroup':
        """Enter the task group context and allow starting new tasks."""

    @abstractmethod
    async def __aexit__(self, exc_type: Optional[Type[BaseException]],
                        exc_val: Optional[BaseException],
                        exc_tb: Optional[TracebackType]) -> Optional[bool]:
        """Exit the task group context waiting for all tasks to finish."""
