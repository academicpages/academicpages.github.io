from collections import (
    abc,
    defaultdict,
)
from collections.abc import (
    Callable,
    Mapping,
    Sequence,
)
import csv
from types import TracebackType
from typing import (
    Any,
    Literal,
    overload,
)

from pandas.core.frame import DataFrame
from pandas.core.indexes.base import Index
from pandas.core.series import Series
from typing_extensions import Self

from pandas._typing import (
    CompressionOptions,
    CSVEngine,
    CSVQuoting,
    DtypeArg,
    FilePath,
    ReadCsvBuffer,
    StorageOptions,
    npt,
)

from pandas.io.common import IOHandles

@overload
def read_csv(
    filepath_or_buffer: FilePath | ReadCsvBuffer[bytes] | ReadCsvBuffer[str],
    *,
    sep: str | None = ...,
    delimiter: str | None = ...,
    header: int | Sequence[int] | Literal["infer"] | None = ...,
    names: list[str] | None = ...,
    index_col: int | str | Sequence[str | int] | Literal[False] | None = ...,
    usecols: list[str]
    | tuple[str, ...]
    | Sequence[int]
    | Series
    | Index
    | npt.NDArray
    | Callable[[str], bool]
    | None = ...,
    dtype: DtypeArg | defaultdict | None = ...,
    engine: CSVEngine | None = ...,
    converters: Mapping[int | str, Callable[[str], Any]]
    | Mapping[int, Callable[[str], Any]]
    | Mapping[str, Callable[[str], Any]]
    | None = ...,
    true_values: list[str] = ...,
    false_values: list[str] = ...,
    skipinitialspace: bool = ...,
    skiprows: int | Sequence[int] | Callable[[int], bool] = ...,
    skipfooter: int = ...,
    nrows: int | None = ...,
    na_values: Sequence[str] | Mapping[str, Sequence[str]] = ...,
    keep_default_na: bool = ...,
    na_filter: bool = ...,
    verbose: bool = ...,
    skip_blank_lines: bool = ...,
    parse_dates: bool
    | list[int]
    | list[str]
    | Sequence[Sequence[int]]
    | Mapping[str, Sequence[int | str]] = ...,
    infer_datetime_format: bool = ...,
    keep_date_col: bool = ...,
    date_parser: Callable = ...,
    dayfirst: bool = ...,
    cache_dates: bool = ...,
    iterator: Literal[True],
    chunksize: int | None = ...,
    compression: CompressionOptions = ...,
    thousands: str | None = ...,
    decimal: str = ...,
    lineterminator: str | None = ...,
    quotechar: str = ...,
    quoting: CSVQuoting = ...,
    doublequote: bool = ...,
    escapechar: str | None = ...,
    comment: str | None = ...,
    encoding: str | None = ...,
    encoding_errors: str | None = ...,
    dialect: str | csv.Dialect = ...,
    on_bad_lines: Literal["error", "warn", "skip"]
    | Callable[[list[str]], list[str] | None] = ...,
    delim_whitespace: bool = ...,
    low_memory: bool = ...,
    memory_map: bool = ...,
    float_precision: Literal["high", "legacy", "round_trip"] | None = ...,
    storage_options: StorageOptions | None = ...,
) -> TextFileReader: ...
@overload
def read_csv(
    filepath_or_buffer: FilePath | ReadCsvBuffer[bytes] | ReadCsvBuffer[str],
    *,
    sep: str | None = ...,
    delimiter: str | None = ...,
    header: int | Sequence[int] | Literal["infer"] | None = ...,
    names: list[str] | None = ...,
    index_col: int | str | Sequence[str | int] | Literal[False] | None = ...,
    usecols: list[str]
    | tuple[str, ...]
    | Sequence[int]
    | Series
    | Index
    | npt.NDArray
    | Callable[[str], bool]
    | None = ...,
    dtype: DtypeArg | defaultdict | None = ...,
    engine: CSVEngine | None = ...,
    converters: Mapping[int | str, Callable[[str], Any]]
    | Mapping[int, Callable[[str], Any]]
    | Mapping[str, Callable[[str], Any]]
    | None = ...,
    true_values: list[str] = ...,
    false_values: list[str] = ...,
    skipinitialspace: bool = ...,
    skiprows: int | Sequence[int] | Callable[[int], bool] = ...,
    skipfooter: int = ...,
    nrows: int | None = ...,
    na_values: Sequence[str] | Mapping[str, Sequence[str]] = ...,
    keep_default_na: bool = ...,
    na_filter: bool = ...,
    verbose: bool = ...,
    skip_blank_lines: bool = ...,
    parse_dates: bool
    | list[int]
    | list[str]
    | Sequence[Sequence[int]]
    | Mapping[str, Sequence[int | str]] = ...,
    infer_datetime_format: bool = ...,
    keep_date_col: bool = ...,
    date_parser: Callable = ...,
    dayfirst: bool = ...,
    cache_dates: bool = ...,
    iterator: bool = ...,
    chunksize: int,
    compression: CompressionOptions = ...,
    thousands: str | None = ...,
    decimal: str = ...,
    lineterminator: str | None = ...,
    quotechar: str = ...,
    quoting: CSVQuoting = ...,
    doublequote: bool = ...,
    escapechar: str | None = ...,
    comment: str | None = ...,
    encoding: str | None = ...,
    encoding_errors: str | None = ...,
    dialect: str | csv.Dialect = ...,
    on_bad_lines: Literal["error", "warn", "skip"]
    | Callable[[list[str]], list[str] | None] = ...,
    delim_whitespace: bool = ...,
    low_memory: bool = ...,
    memory_map: bool = ...,
    float_precision: Literal["high", "legacy", "round_trip"] | None = ...,
    storage_options: StorageOptions | None = ...,
) -> TextFileReader: ...
@overload
def read_csv(
    filepath_or_buffer: FilePath | ReadCsvBuffer[bytes] | ReadCsvBuffer[str],
    *,
    sep: str | None = ...,
    delimiter: str | None = ...,
    header: int | Sequence[int] | Literal["infer"] | None = ...,
    names: list[str] | None = ...,
    index_col: int | str | Sequence[str | int] | Literal[False] | None = ...,
    usecols: list[str]
    | tuple[str, ...]
    | Sequence[int]
    | Series
    | Index
    | npt.NDArray
    | Callable[[str], bool]
    | None = ...,
    dtype: DtypeArg | defaultdict | None = ...,
    engine: CSVEngine | None = ...,
    converters: Mapping[int | str, Callable[[str], Any]]
    | Mapping[int, Callable[[str], Any]]
    | Mapping[str, Callable[[str], Any]]
    | None = ...,
    true_values: list[str] = ...,
    false_values: list[str] = ...,
    skipinitialspace: bool = ...,
    skiprows: int | Sequence[int] | Callable[[int], bool] = ...,
    skipfooter: int = ...,
    nrows: int | None = ...,
    na_values: Sequence[str] | Mapping[str, Sequence[str]] = ...,
    keep_default_na: bool = ...,
    na_filter: bool = ...,
    verbose: bool = ...,
    skip_blank_lines: bool = ...,
    parse_dates: bool
    | list[int]
    | list[str]
    | Sequence[Sequence[int]]
    | Mapping[str, Sequence[int | str]] = ...,
    infer_datetime_format: bool = ...,
    keep_date_col: bool = ...,
    date_parser: Callable = ...,
    dayfirst: bool = ...,
    cache_dates: bool = ...,
    iterator: Literal[False] = ...,
    chunksize: None = ...,
    compression: CompressionOptions = ...,
    thousands: str | None = ...,
    decimal: str = ...,
    lineterminator: str | None = ...,
    quotechar: str = ...,
    quoting: CSVQuoting = ...,
    doublequote: bool = ...,
    escapechar: str | None = ...,
    comment: str | None = ...,
    encoding: str | None = ...,
    encoding_errors: str | None = ...,
    dialect: str | csv.Dialect = ...,
    on_bad_lines: Literal["error", "warn", "skip"]
    | Callable[[list[str]], list[str] | None] = ...,
    delim_whitespace: bool = ...,
    low_memory: bool = ...,
    memory_map: bool = ...,
    float_precision: Literal["high", "legacy", "round_trip"] | None = ...,
    storage_options: StorageOptions | None = ...,
) -> DataFrame: ...
@overload
def read_table(
    filepath_or_buffer: FilePath | ReadCsvBuffer[bytes] | ReadCsvBuffer[str],
    *,
    sep: str | None = ...,
    delimiter: str | None = ...,
    header: int | Sequence[int] | Literal["infer"] | None = ...,
    names: list[str] | None = ...,
    index_col: int | str | Sequence[str | int] | Literal[False] | None = ...,
    usecols: list[str]
    | tuple[str, ...]
    | Sequence[int]
    | Series
    | Index
    | npt.NDArray
    | Callable[[str], bool]
    | None = ...,
    dtype: DtypeArg | defaultdict | None = ...,
    engine: CSVEngine | None = ...,
    converters: Mapping[int | str, Callable[[str], Any]]
    | Mapping[int, Callable[[str], Any]]
    | Mapping[str, Callable[[str], Any]]
    | None = ...,
    true_values: list[str] = ...,
    false_values: list[str] = ...,
    skipinitialspace: bool = ...,
    skiprows: int | Sequence[int] | Callable[[int], bool] = ...,
    skipfooter: int = ...,
    nrows: int | None = ...,
    na_values: Sequence[str] | Mapping[str, Sequence[str]] = ...,
    keep_default_na: bool = ...,
    na_filter: bool = ...,
    verbose: bool = ...,
    skip_blank_lines: bool = ...,
    parse_dates: bool
    | list[int]
    | list[str]
    | Sequence[Sequence[int]]
    | Mapping[str, Sequence[int | str]] = ...,
    infer_datetime_format: bool = ...,
    keep_date_col: bool = ...,
    date_parser: Callable = ...,
    dayfirst: bool = ...,
    cache_dates: bool = ...,
    iterator: Literal[True],
    chunksize: int | None = ...,
    compression: CompressionOptions = ...,
    thousands: str | None = ...,
    decimal: str = ...,
    lineterminator: str | None = ...,
    quotechar: str = ...,
    quoting: CSVQuoting = ...,
    doublequote: bool = ...,
    escapechar: str | None = ...,
    comment: str | None = ...,
    encoding: str | None = ...,
    encoding_errors: str | None = ...,
    dialect: str | csv.Dialect = ...,
    on_bad_lines: Literal["error", "warn", "skip"]
    | Callable[[list[str]], list[str] | None] = ...,
    delim_whitespace: bool = ...,
    low_memory: bool = ...,
    memory_map: bool = ...,
    float_precision: Literal["high", "legacy", "round_trip"] | None = ...,
    storage_options: StorageOptions | None = ...,
) -> TextFileReader: ...
@overload
def read_table(
    filepath_or_buffer: FilePath | ReadCsvBuffer[bytes] | ReadCsvBuffer[str],
    *,
    sep: str | None = ...,
    delimiter: str | None = ...,
    header: int | Sequence[int] | Literal["infer"] | None = ...,
    names: list[str] | None = ...,
    index_col: int | str | Sequence[str | int] | Literal[False] | None = ...,
    usecols: list[str]
    | tuple[str, ...]
    | Sequence[int]
    | Series
    | Index
    | npt.NDArray
    | Callable[[str], bool]
    | None = ...,
    dtype: DtypeArg | defaultdict | None = ...,
    engine: CSVEngine | None = ...,
    converters: Mapping[int | str, Callable[[str], Any]]
    | Mapping[int, Callable[[str], Any]]
    | Mapping[str, Callable[[str], Any]]
    | None = ...,
    true_values: list[str] = ...,
    false_values: list[str] = ...,
    skipinitialspace: bool = ...,
    skiprows: int | Sequence[int] | Callable[[int], bool] = ...,
    skipfooter: int = ...,
    nrows: int | None = ...,
    na_values: Sequence[str] | Mapping[str, Sequence[str]] = ...,
    keep_default_na: bool = ...,
    na_filter: bool = ...,
    verbose: bool = ...,
    skip_blank_lines: bool = ...,
    parse_dates: bool
    | list[int]
    | list[str]
    | Sequence[Sequence[int]]
    | Mapping[str, Sequence[int | str]] = ...,
    infer_datetime_format: bool = ...,
    keep_date_col: bool = ...,
    date_parser: Callable = ...,
    dayfirst: bool = ...,
    cache_dates: bool = ...,
    iterator: bool = ...,
    chunksize: int,
    compression: CompressionOptions = ...,
    thousands: str | None = ...,
    decimal: str = ...,
    lineterminator: str | None = ...,
    quotechar: str = ...,
    quoting: CSVQuoting = ...,
    doublequote: bool = ...,
    escapechar: str | None = ...,
    comment: str | None = ...,
    encoding: str | None = ...,
    encoding_errors: str | None = ...,
    dialect: str | csv.Dialect = ...,
    on_bad_lines: Literal["error", "warn", "skip"]
    | Callable[[list[str]], list[str] | None] = ...,
    delim_whitespace: bool = ...,
    low_memory: bool = ...,
    memory_map: bool = ...,
    float_precision: Literal["high", "legacy", "round_trip"] | None = ...,
    storage_options: StorageOptions | None = ...,
) -> TextFileReader: ...
@overload
def read_table(
    filepath_or_buffer: FilePath | ReadCsvBuffer[bytes] | ReadCsvBuffer[str],
    *,
    sep: str | None = ...,
    delimiter: str | None = ...,
    header: int | Sequence[int] | Literal["infer"] | None = ...,
    names: list[str] | None = ...,
    index_col: int | str | Sequence[str | int] | Literal[False] | None = ...,
    usecols: list[str]
    | tuple[str, ...]
    | Sequence[int]
    | Series
    | Index
    | npt.NDArray
    | Callable[[str], bool]
    | None = ...,
    dtype: DtypeArg | defaultdict | None = ...,
    engine: CSVEngine | None = ...,
    converters: Mapping[int | str, Callable[[str], Any]]
    | Mapping[int, Callable[[str], Any]]
    | Mapping[str, Callable[[str], Any]]
    | None = ...,
    true_values: list[str] = ...,
    false_values: list[str] = ...,
    skipinitialspace: bool = ...,
    skiprows: int | Sequence[int] | Callable[[int], bool] = ...,
    skipfooter: int = ...,
    nrows: int | None = ...,
    na_values: Sequence[str] | Mapping[str, Sequence[str]] = ...,
    keep_default_na: bool = ...,
    na_filter: bool = ...,
    verbose: bool = ...,
    skip_blank_lines: bool = ...,
    parse_dates: bool
    | list[int]
    | list[str]
    | Sequence[Sequence[int]]
    | Mapping[str, Sequence[int | str]] = ...,
    infer_datetime_format: bool = ...,
    keep_date_col: bool = ...,
    date_parser: Callable = ...,
    dayfirst: bool = ...,
    cache_dates: bool = ...,
    iterator: Literal[False] = ...,
    chunksize: None = ...,
    compression: CompressionOptions = ...,
    thousands: str | None = ...,
    decimal: str = ...,
    lineterminator: str | None = ...,
    quotechar: str = ...,
    quoting: CSVQuoting = ...,
    doublequote: bool = ...,
    escapechar: str | None = ...,
    comment: str | None = ...,
    encoding: str | None = ...,
    encoding_errors: str | None = ...,
    dialect: str | csv.Dialect = ...,
    on_bad_lines: Literal["error", "warn", "skip"]
    | Callable[[list[str]], list[str] | None] = ...,
    delim_whitespace: bool = ...,
    low_memory: bool = ...,
    memory_map: bool = ...,
    float_precision: Literal["high", "legacy", "round_trip"] | None = ...,
    storage_options: StorageOptions | None = ...,
) -> DataFrame: ...
@overload
def read_fwf(
    filepath_or_buffer: FilePath | ReadCsvBuffer[bytes] | ReadCsvBuffer[str],
    *,
    colspecs: Sequence[tuple[int, int]] | Literal["infer"] | None = ...,
    widths: Sequence[int] | None = ...,
    infer_nrows: int = ...,
    iterator: Literal[True],
    chunksize: int | None = ...,
    **kwds: Any,
) -> TextFileReader: ...
@overload
def read_fwf(
    filepath_or_buffer: FilePath | ReadCsvBuffer[bytes] | ReadCsvBuffer[str],
    *,
    colspecs: Sequence[tuple[int, int]] | Literal["infer"] | None = ...,
    widths: Sequence[int] | None = ...,
    infer_nrows: int = ...,
    iterator: bool = ...,
    chunksize: int,
    **kwds: Any,
) -> TextFileReader: ...
@overload
def read_fwf(
    filepath_or_buffer: FilePath | ReadCsvBuffer[bytes] | ReadCsvBuffer[str],
    *,
    colspecs: Sequence[tuple[int, int]] | Literal["infer"] | None = ...,
    widths: Sequence[int] | None = ...,
    infer_nrows: int = ...,
    iterator: Literal[False] = ...,
    chunksize: None = ...,
    **kwds: Any,
) -> DataFrame: ...

class TextFileReader(abc.Iterator):
    engine: CSVEngine
    orig_options: Mapping[str, Any]
    chunksize: int | None
    nrows: int | None
    squeeze: bool
    handles: IOHandles | None
    def __init__(
        self,
        f: FilePath | ReadCsvBuffer[bytes] | ReadCsvBuffer[str] | list,
        engine: CSVEngine | None = ...,
        **kwds: Any,
    ) -> None: ...
    def close(self) -> None: ...
    def read(self, nrows: int | None = ...) -> DataFrame: ...
    def get_chunk(self, size: int | None = ...) -> DataFrame: ...
    def __next__(self) -> DataFrame: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None: ...
