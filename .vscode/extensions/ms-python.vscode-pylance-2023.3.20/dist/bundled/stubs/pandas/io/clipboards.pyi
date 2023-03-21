from collections import defaultdict
from collections.abc import (
    Callable,
    Sequence,
)
import csv
from typing import (
    Any,
    Literal,
    overload,
)

from pandas.core.frame import DataFrame
from pandas.core.indexes.base import Index
from pandas.core.series import Series

from pandas._typing import (
    CompressionOptions,
    CSVEngine,
    CSVQuoting,
    DtypeArg,
    StorageOptions,
    npt,
)

from pandas.io.parsers import TextFileReader

@overload
def read_clipboard(
    sep: str | None = ...,
    *,
    delimiter: str | None = ...,
    header: int | Sequence[int] | Literal["infer"] | None = ...,
    names: list[str] = ...,
    index_col: int | str | Sequence[str | int] | Literal[False] | None = ...,
    usecols: list[str]
    | Sequence[int]
    | Series
    | Index
    | npt.NDArray
    | Callable[[str], bool]
    | None = ...,
    dtype: DtypeArg | defaultdict | None = ...,
    engine: CSVEngine | None = ...,
    converters: dict[int | str, Callable[[str], Any]] = ...,
    true_values: list[str] = ...,
    false_values: list[str] = ...,
    skipinitialspace: bool = ...,
    skiprows: int | Sequence[int] | Callable[[int], bool] = ...,
    skipfooter: int = ...,
    nrows: int | None = ...,
    na_values: Sequence[str] | dict[str, Sequence[str]] = ...,
    keep_default_na: bool = ...,
    na_filter: bool = ...,
    verbose: bool = ...,
    skip_blank_lines: bool = ...,
    parse_dates: bool
    | Sequence[int]
    | list[str]
    | Sequence[Sequence[int]]
    | dict[str, Sequence[int]] = ...,
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
    # error_bad_lines: bool | None = ...,  # Deprecated: 1.3.0
    # warn_bad_lines: bool | None = ...,  # Deprecated: 1.3.0
    on_bad_lines: Literal["error", "warn", "skip"]
    | Callable[[list[str]], list[str] | None] = ...,
    delim_whitespace: bool = ...,
    low_memory: bool = ...,
    memory_map: bool = ...,
    float_precision: Literal["high", "legacy", "round_trip"] | None = ...,
    storage_options: StorageOptions | None = ...,
) -> TextFileReader: ...
@overload
def read_clipboard(
    sep: str | None = ...,
    *,
    delimiter: str | None = ...,
    header: int | Sequence[int] | Literal["infer"] | None = ...,
    names: list[str] = ...,
    index_col: int | str | Sequence[str | int] | Literal[False] | None = ...,
    usecols: list[str]
    | Sequence[int]
    | Series
    | Index
    | npt.NDArray
    | Callable[[str], bool]
    | None = ...,
    dtype: DtypeArg | defaultdict | None = ...,
    engine: CSVEngine | None = ...,
    converters: dict[int | str, Callable[[str], Any]] = ...,
    true_values: list[str] = ...,
    false_values: list[str] = ...,
    skipinitialspace: bool = ...,
    skiprows: int | Sequence[int] | Callable[[int], bool] = ...,
    skipfooter: int = ...,
    nrows: int | None = ...,
    na_values: Sequence[str] | dict[str, Sequence[str]] = ...,
    keep_default_na: bool = ...,
    na_filter: bool = ...,
    verbose: bool = ...,
    skip_blank_lines: bool = ...,
    parse_dates: bool
    | Sequence[int]
    | list[str]
    | Sequence[Sequence[int]]
    | dict[str, Sequence[int]] = ...,
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
    # error_bad_lines: bool | None = ...,  # Deprecated: 1.3.0
    # warn_bad_lines: bool | None = ...,  # Deprecated: 1.3.0
    on_bad_lines: Literal["error", "warn", "skip"]
    | Callable[[list[str]], list[str] | None] = ...,
    delim_whitespace: bool = ...,
    low_memory: bool = ...,
    memory_map: bool = ...,
    float_precision: Literal["high", "legacy", "round_trip"] | None = ...,
    storage_options: StorageOptions | None = ...,
) -> TextFileReader: ...
@overload
def read_clipboard(
    sep: str | None = ...,
    *,
    delimiter: str | None = ...,
    header: int | Sequence[int] | Literal["infer"] | None = ...,
    names: list[str] = ...,
    index_col: int | str | Sequence[str | int] | Literal[False] | None = ...,
    usecols: list[str]
    | Sequence[int]
    | Series
    | Index
    | npt.NDArray
    | Callable[[str], bool]
    | None = ...,
    dtype: DtypeArg | defaultdict | None = ...,
    engine: CSVEngine | None = ...,
    converters: dict[int | str, Callable[[str], Any]] = ...,
    true_values: list[str] = ...,
    false_values: list[str] = ...,
    skipinitialspace: bool = ...,
    skiprows: int | Sequence[int] | Callable[[int], bool] = ...,
    skipfooter: int = ...,
    nrows: int | None = ...,
    na_values: Sequence[str] | dict[str, Sequence[str]] = ...,
    keep_default_na: bool = ...,
    na_filter: bool = ...,
    verbose: bool = ...,
    skip_blank_lines: bool = ...,
    parse_dates: bool
    | Sequence[int]
    | list[str]
    | Sequence[Sequence[int]]
    | dict[str, Sequence[int]] = ...,
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
    # error_bad_lines: bool | None = ...,  # Deprecated: 1.3.0
    # warn_bad_lines: bool | None = ...,  # Deprecated: 1.3.0
    on_bad_lines: Literal["error", "warn", "skip"]
    | Callable[[list[str]], list[str] | None] = ...,
    delim_whitespace: bool = ...,
    low_memory: bool = ...,
    memory_map: bool = ...,
    float_precision: Literal["high", "legacy", "round_trip"] | None = ...,
    storage_options: StorageOptions | None = ...,
) -> DataFrame: ...
def to_clipboard(
    obj, excel: bool = ..., sep: str | None = ..., **kwargs: Any
) -> None: ...
