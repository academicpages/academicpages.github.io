from typing import (
    IO,
    Any,
)

from pandas._typing import FilePathOrBuffer

s3fs = ...

def get_file_and_filesystem(
    filepath_or_buffer: FilePathOrBuffer, mode: str | None = ...
) -> tuple[IO, Any]: ...
def get_filepath_or_buffer(
    filepath_or_buffer: FilePathOrBuffer,
    encoding: str | None = ...,
    compression: str | None = ...,
    mode: str | None = ...,
) -> tuple[IO, str | None, str | None, bool]: ...
