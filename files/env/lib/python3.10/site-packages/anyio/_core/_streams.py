import math
from typing import Any, Optional, Tuple, Type, TypeVar, overload

from ..streams.memory import (
    MemoryObjectReceiveStream, MemoryObjectSendStream, MemoryObjectStreamState)

T_Item = TypeVar('T_Item')


@overload
def create_memory_object_stream(
    max_buffer_size: float, item_type: Type[T_Item]
) -> Tuple[MemoryObjectSendStream[T_Item], MemoryObjectReceiveStream[T_Item]]:
    ...


@overload
def create_memory_object_stream(
    max_buffer_size: float = 0
) -> Tuple[MemoryObjectSendStream[Any], MemoryObjectReceiveStream[Any]]:
    ...


def create_memory_object_stream(
    max_buffer_size: float = 0, item_type: Optional[Type[T_Item]] = None
) -> Tuple[MemoryObjectSendStream[Any], MemoryObjectReceiveStream[Any]]:
    """
    Create a memory object stream.

    :param max_buffer_size: number of items held in the buffer until ``send()`` starts blocking
    :param item_type: type of item, for marking the streams with the right generic type for
        static typing (not used at run time)
    :return: a tuple of (send stream, receive stream)

    """
    if max_buffer_size != math.inf and not isinstance(max_buffer_size, int):
        raise ValueError('max_buffer_size must be either an integer or math.inf')
    if max_buffer_size < 0:
        raise ValueError('max_buffer_size cannot be negative')

    state: MemoryObjectStreamState = MemoryObjectStreamState(max_buffer_size)
    return MemoryObjectSendStream(state), MemoryObjectReceiveStream(state)
