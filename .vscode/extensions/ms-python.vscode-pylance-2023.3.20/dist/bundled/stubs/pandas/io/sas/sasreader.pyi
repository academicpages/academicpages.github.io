from abc import (
    ABCMeta,
    abstractmethod,
)
from collections.abc import Hashable
from typing import (
    Literal,
    overload,
)

from pandas import DataFrame
from typing_extensions import Self

from pandas._typing import (
    CompressionOptions as CompressionOptions,
    FilePath as FilePath,
    ReadBuffer,
)

from pandas.io.sas.sas7bdat import SAS7BDATReader
from pandas.io.sas.sas_xport import XportReader

class ReaderBase(metaclass=ABCMeta):
    @abstractmethod
    def read(self, nrows: int | None = ...) -> DataFrame: ...
    @abstractmethod
    def close(self) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(self, exc_type, exc_value, traceback) -> None: ...

@overload
def read_sas(
    filepath_or_buffer: FilePath | ReadBuffer[bytes],
    *,
    format: Literal["sas7bdat"],
    index: Hashable | None = ...,
    encoding: str | None = ...,
    chunksize: int,
    iterator: bool = ...,
    compression: CompressionOptions = ...,
) -> SAS7BDATReader: ...
@overload
def read_sas(
    filepath_or_buffer: FilePath | ReadBuffer[bytes],
    *,
    format: Literal["xport"],
    index: Hashable | None = ...,
    encoding: str | None = ...,
    chunksize: int,
    iterator: bool = ...,
    compression: CompressionOptions = ...,
) -> XportReader: ...
@overload
def read_sas(
    filepath_or_buffer: FilePath | ReadBuffer[bytes],
    *,
    format: None = ...,
    index: Hashable | None = ...,
    encoding: str | None = ...,
    chunksize: int,
    iterator: bool = ...,
    compression: CompressionOptions = ...,
) -> XportReader | SAS7BDATReader: ...
@overload
def read_sas(
    filepath_or_buffer: FilePath | ReadBuffer[bytes],
    *,
    format: Literal["sas7bdat"],
    index: Hashable | None = ...,
    encoding: str | None = ...,
    chunksize: int | None = ...,
    iterator: Literal[True],
    compression: CompressionOptions = ...,
) -> SAS7BDATReader: ...
@overload
def read_sas(
    filepath_or_buffer: FilePath | ReadBuffer[bytes],
    *,
    format: Literal["xport"],
    index: Hashable | None = ...,
    encoding: str | None = ...,
    chunksize: int | None = ...,
    iterator: Literal[True],
    compression: CompressionOptions = ...,
) -> XportReader: ...
@overload
def read_sas(
    filepath_or_buffer: FilePath | ReadBuffer[bytes],
    *,
    format: None = ...,
    index: Hashable | None = ...,
    encoding: str | None = ...,
    chunksize: int | None = ...,
    iterator: Literal[True],
    compression: CompressionOptions = ...,
) -> XportReader | SAS7BDATReader: ...
@overload
def read_sas(
    filepath_or_buffer: FilePath | ReadBuffer[bytes],
    *,
    format: Literal["xport", "sas7bdat"] | None = ...,
    index: Hashable | None = ...,
    encoding: str | None = ...,
    chunksize: None = ...,
    iterator: Literal[False] = ...,
    compression: CompressionOptions = ...,
) -> DataFrame: ...
