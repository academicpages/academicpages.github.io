from typing import (
    IO,
    AnyStr,
    Generic,
)

from pandas._typing import CompressionDict

class IOHandles(Generic[AnyStr]):
    handle: IO[AnyStr]
    compression: CompressionDict
    created_handles: list[IO[AnyStr]]
    is_wrapped: bool
    def close(self) -> None: ...
    def __enter__(self) -> IOHandles[AnyStr]: ...
    def __exit__(self, *args: object) -> None: ...
    def __init__(self, handle, compression, created_handles, is_wrapped) -> None: ...
