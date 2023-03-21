from collections.abc import Sequence

from pandas.core.frame import DataFrame

from pandas._typing import (
    CompressionOptions,
    ConvertersArg,
    DtypeArg,
    FilePath,
    ParseDatesArg,
    ReadBuffer,
    StorageOptions,
    XMLParsers,
)

def read_xml(
    path_or_buffer: FilePath | ReadBuffer[bytes] | ReadBuffer[str],
    *,
    xpath: str = ...,
    namespaces: dict[str, str] | None = ...,
    elems_only: bool = ...,
    attrs_only: bool = ...,
    names: Sequence[str] | None = ...,
    dtype: DtypeArg | None = ...,
    converters: ConvertersArg | None = ...,
    parse_dates: ParseDatesArg | None = ...,
    # encoding can not be None for lxml and StringIO input
    encoding: str | None = ...,
    parser: XMLParsers = ...,
    stylesheet: FilePath | ReadBuffer[bytes] | ReadBuffer[str] | None = ...,
    iterparse: dict[str, list[str]] | None = ...,
    compression: CompressionOptions = ...,
    storage_options: StorageOptions = ...,
) -> DataFrame: ...
