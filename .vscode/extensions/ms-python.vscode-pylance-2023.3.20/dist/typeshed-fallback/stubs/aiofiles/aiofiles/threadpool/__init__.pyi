from _typeshed import (
    FileDescriptorOrPath,
    Incomplete,
    OpenBinaryMode,
    OpenBinaryModeReading,
    OpenBinaryModeUpdating,
    OpenBinaryModeWriting,
    OpenTextMode,
)
from asyncio import AbstractEventLoop
from collections.abc import Callable
from typing import overload
from typing_extensions import Literal, TypeAlias

from ..base import AiofilesContextManager
from .binary import AsyncBufferedIOBase, AsyncBufferedReader, AsyncFileIO, _UnknownAsyncBinaryIO
from .text import AsyncTextIOWrapper

_Opener: TypeAlias = Callable[[str, int], int]

# Text mode: always returns AsyncTextIOWrapper
@overload
def open(
    file: FileDescriptorOrPath,
    mode: OpenTextMode = ...,
    buffering: int = ...,
    encoding: str | None = ...,
    errors: str | None = ...,
    newline: str | None = ...,
    closefd: bool = ...,
    opener: _Opener | None = ...,
    *,
    loop: AbstractEventLoop | None = ...,
    executor: Incomplete | None = ...,
) -> AiofilesContextManager[None, None, AsyncTextIOWrapper]: ...

# Unbuffered binary: returns a FileIO
@overload
def open(
    file: FileDescriptorOrPath,
    mode: OpenBinaryMode,
    buffering: Literal[0],
    encoding: None = ...,
    errors: None = ...,
    newline: None = ...,
    closefd: bool = ...,
    opener: _Opener | None = ...,
    *,
    loop: AbstractEventLoop | None = ...,
    executor: Incomplete | None = ...,
) -> AiofilesContextManager[None, None, AsyncFileIO]: ...

# Buffered binary reading/updating: AsyncBufferedReader
@overload
def open(
    file: FileDescriptorOrPath,
    mode: OpenBinaryModeReading | OpenBinaryModeUpdating,
    buffering: Literal[-1, 1] = ...,
    encoding: None = ...,
    errors: None = ...,
    newline: None = ...,
    closefd: bool = ...,
    opener: _Opener | None = ...,
    *,
    loop: AbstractEventLoop | None = ...,
    executor: Incomplete | None = ...,
) -> AiofilesContextManager[None, None, AsyncBufferedReader]: ...

# Buffered binary writing: AsyncBufferedIOBase
@overload
def open(
    file: FileDescriptorOrPath,
    mode: OpenBinaryModeWriting,
    buffering: Literal[-1, 1] = ...,
    encoding: None = ...,
    errors: None = ...,
    newline: None = ...,
    closefd: bool = ...,
    opener: _Opener | None = ...,
    *,
    loop: AbstractEventLoop | None = ...,
    executor: Incomplete | None = ...,
) -> AiofilesContextManager[None, None, AsyncBufferedIOBase]: ...

# Buffering cannot be determined: fall back to _UnknownAsyncBinaryIO
@overload
def open(
    file: FileDescriptorOrPath,
    mode: OpenBinaryMode,
    buffering: int = ...,
    encoding: None = ...,
    errors: None = ...,
    newline: None = ...,
    closefd: bool = ...,
    opener: _Opener | None = ...,
    *,
    loop: AbstractEventLoop | None = ...,
    executor: Incomplete | None = ...,
) -> AiofilesContextManager[None, None, _UnknownAsyncBinaryIO]: ...
