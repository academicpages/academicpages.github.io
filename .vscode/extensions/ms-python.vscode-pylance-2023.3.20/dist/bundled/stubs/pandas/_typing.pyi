from builtins import type as type_t
from collections.abc import (
    Callable,
    Hashable,
    Iterator,
    Mapping,
    MutableSequence,
    Sequence,
)
import datetime
from os import PathLike
from typing import (
    Any,
    Literal,
    Protocol,
    TypedDict,
    TypeVar,
)

import numpy as np
from numpy import typing as npt
import pandas as pd
from pandas.core.arrays import ExtensionArray
from pandas.core.frame import DataFrame
from pandas.core.generic import NDFrame
from pandas.core.groupby.grouper import Grouper
from pandas.core.indexes.base import Index
from pandas.core.series import Series
from typing_extensions import TypeAlias

from pandas._libs.interval import Interval
from pandas._libs.tslibs import (
    Period,
    Timedelta,
    Timestamp,
)

from pandas.core.dtypes.dtypes import (
    CategoricalDtype,
    ExtensionDtype,
)

from pandas.io.formats.format import EngFormatter

ArrayLike: TypeAlias = ExtensionArray | np.ndarray
AnyArrayLike: TypeAlias = Index | Series | np.ndarray
PythonScalar: TypeAlias = str | bool | complex
DatetimeLikeScalar = TypeVar("DatetimeLikeScalar", Period, Timestamp, Timedelta)
PandasScalar: TypeAlias = bytes | datetime.date | datetime.datetime | datetime.timedelta
# Scalar: TypeAlias = PythonScalar | PandasScalar

DatetimeLike: TypeAlias = datetime.datetime | np.datetime64 | Timestamp
DateAndDatetimeLike: TypeAlias = datetime.date | DatetimeLike

DatetimeDictArg: TypeAlias = (
    Sequence[int] | Sequence[float] | list[str] | tuple[Scalar, ...] | AnyArrayLike
)
DictConvertible: TypeAlias = FulldatetimeDict | DataFrame

class YearMonthDayDict(TypedDict, total=True):
    year: DatetimeDictArg
    month: DatetimeDictArg
    day: DatetimeDictArg

class FulldatetimeDict(YearMonthDayDict, total=False):
    hour: DatetimeDictArg
    hours: DatetimeDictArg
    minute: DatetimeDictArg
    minutes: DatetimeDictArg
    second: DatetimeDictArg
    seconds: DatetimeDictArg
    ms: DatetimeDictArg
    us: DatetimeDictArg
    ns: DatetimeDictArg

# dtypes
NpDtype: TypeAlias = str | np.dtype[np.generic] | type[str | complex | bool | object]
Dtype: TypeAlias = ExtensionDtype | NpDtype
DtypeArg: TypeAlias = Dtype | dict[Any, Dtype]
BooleanDtypeArg: TypeAlias = (
    # Builtin bool type and its string alias
    type[bool]  # noqa: Y030
    | Literal["bool"]
    # Pandas nullable boolean type and its string alias
    | pd.BooleanDtype
    | Literal["boolean"]
    # Numpy bool type
    | type[np.bool_]
)
IntDtypeArg: TypeAlias = (
    # Builtin integer type and its string alias
    type[int]  # noqa: Y030
    | Literal["int"]
    # Pandas nullable integer types and their string aliases
    | pd.Int8Dtype
    | pd.Int16Dtype
    | pd.Int32Dtype
    | pd.Int64Dtype
    | Literal["Int8", "Int16", "Int32", "Int64"]
    # Numpy signed integer types and their string aliases
    | type[np.byte]
    | type[np.int8]
    | type[np.int16]
    | type[np.int32]
    | type[np.int64]
    | type[np.intp]
    | Literal["byte", "int8", "int16", "int32", "int64", "intp"]
    # Numpy unsigned integer types and their string aliases
    | type[np.ubyte]
    | type[np.uint8]
    | type[np.uint16]
    | type[np.uint32]
    | type[np.uint64]
    | type[np.uintp]
    | Literal["ubyte", "uint8", "uint16", "uint32", "uint64", "uintp"]
)
StrDtypeArg: TypeAlias = (
    # Builtin str type and its string alias
    type[str]  # noqa: Y030
    | Literal["str"]
    # Pandas nullable string type and its string alias
    | pd.StringDtype
    | Literal["string"]
)
BytesDtypeArg: TypeAlias = type[bytes]
FloatDtypeArg: TypeAlias = (
    # Builtin float type and its string alias
    type[float]  # noqa: Y030
    | Literal["float"]
    # Pandas nullable float types and their string aliases
    | pd.Float32Dtype
    | pd.Float64Dtype
    | Literal["Float32", "Float64"]
    # Numpy float types and their string aliases
    | type[np.float16]
    | type[np.float32]
    | type[np.float64]
    | Literal["float16", "float32", "float64"]
)
ComplexDtypeArg: TypeAlias = (
    # Builtin complex type and its string alias
    type[complex]  # noqa: Y030
    | Literal["complex"]
    # Numpy complex types and their aliases
    | type[np.complex64]
    | type[np.complex128]
    | Literal["complex64", "complex128"]
)
TimedeltaDtypeArg: TypeAlias = Literal["timedelta64[ns]"]
TimestampDtypeArg: TypeAlias = Literal["datetime64[ns]"]
CategoryDtypeArg: TypeAlias = Literal["category"]

AstypeArg: TypeAlias = (
    BooleanDtypeArg
    | IntDtypeArg
    | StrDtypeArg
    | BytesDtypeArg
    | FloatDtypeArg
    | ComplexDtypeArg
    | TimedeltaDtypeArg
    | TimestampDtypeArg
    | CategoricalDtype
    | ExtensionDtype
)
# DtypeArg specifies all allowable dtypes in a functions its dtype argument
DtypeObj: TypeAlias = np.dtype[np.generic] | ExtensionDtype

# filenames and file-like-objects
AnyStr_cov = TypeVar("AnyStr_cov", str, bytes, covariant=True)
AnyStr_con = TypeVar("AnyStr_con", str, bytes, contravariant=True)

class BaseBuffer(Protocol):
    @property
    def mode(self) -> str: ...
    def seek(self, __offset: int, __whence: int = ...) -> int: ...
    def seekable(self) -> bool: ...
    def tell(self) -> int: ...

class ReadBuffer(BaseBuffer, Protocol[AnyStr_cov]):
    def read(self, __n: int = ...) -> AnyStr_cov: ...

class WriteBuffer(BaseBuffer, Protocol[AnyStr_con]):
    def write(self, __b: AnyStr_con) -> Any: ...
    def flush(self) -> Any: ...

class ReadPickleBuffer(ReadBuffer[bytes], Protocol):
    def readline(self) -> bytes: ...

class ReadCsvBuffer(ReadBuffer[AnyStr_cov], Protocol[AnyStr_cov]):
    def __iter__(self) -> Iterator[AnyStr_cov]: ...
    def fileno(self) -> int: ...
    def readline(self) -> AnyStr_cov: ...
    @property
    def closed(self) -> bool: ...

class WriteExcelBuffer(WriteBuffer[bytes], Protocol):
    def truncate(self, size: int | None = ...) -> int: ...

FilePath: TypeAlias = str | PathLike[str]

AxisInt: TypeAlias = Literal[0, 1]
Axis: TypeAlias = AxisInt | Literal["index", "columns", "rows"]
IndexLabel: TypeAlias = Hashable | Sequence[Hashable]
Label: TypeAlias = Hashable | None
Level: TypeAlias = Hashable | int
Suffixes: TypeAlias = tuple[str | None, str | None]
Ordered: TypeAlias = bool | None
JSONSerializable: TypeAlias = PythonScalar | list | dict
Axes: TypeAlias = AnyArrayLike | list | dict | range | tuple
Renamer: TypeAlias = Mapping[Any, Label] | Callable[[Any], Label]
T = TypeVar("T")
FuncType: TypeAlias = Callable[..., Any]
F = TypeVar("F", bound=FuncType)
HashableT = TypeVar("HashableT", bound=Hashable)
HashableT1 = TypeVar("HashableT1", bound=Hashable)
HashableT2 = TypeVar("HashableT2", bound=Hashable)
HashableT3 = TypeVar("HashableT3", bound=Hashable)
HashableT4 = TypeVar("HashableT4", bound=Hashable)
HashableT5 = TypeVar("HashableT5", bound=Hashable)

AggFuncTypeBase: TypeAlias = Callable | str | np.ufunc
AggFuncTypeDictSeries: TypeAlias = Mapping[HashableT, AggFuncTypeBase]
AggFuncTypeDictFrame: TypeAlias = Mapping[
    HashableT, AggFuncTypeBase | list[AggFuncTypeBase]
]
AggFuncTypeSeriesToFrame: TypeAlias = list[AggFuncTypeBase] | AggFuncTypeDictSeries
AggFuncTypeFrame: TypeAlias = (
    AggFuncTypeBase | list[AggFuncTypeBase] | AggFuncTypeDictFrame
)

num: TypeAlias = complex
SeriesAxisType: TypeAlias = Literal[
    "index", 0
]  # Restricted subset of _AxisType for series
AxisTypeIndex: TypeAlias = Literal["index", 0]
AxisTypeColumn: TypeAlias = Literal["columns", 1]
AxisType: TypeAlias = AxisTypeIndex | AxisTypeColumn
DtypeNp = TypeVar("DtypeNp", bound=np.dtype[np.generic])
KeysArgType: TypeAlias = Any
ListLike = TypeVar("ListLike", Sequence, np.ndarray, "Series", "Index")
ListLikeExceptSeriesAndStr = TypeVar(
    "ListLikeExceptSeriesAndStr", MutableSequence, np.ndarray, tuple, "Index"
)
ListLikeU: TypeAlias = Sequence | np.ndarray | Series | Index
StrLike: TypeAlias = str | np.str_
IndexIterScalar: TypeAlias = (
    str
    | bytes
    | datetime.date
    | datetime.datetime
    | datetime.timedelta
    | np.datetime64
    | np.timedelta64
    | bool
    | int
    | float
    | Timestamp
    | Timedelta
)
Scalar: TypeAlias = IndexIterScalar | complex
ScalarT = TypeVar("ScalarT", bound=Scalar)
# Refine the definitions below in 3.9 to use the specialized type.
np_ndarray_int64: TypeAlias = npt.NDArray[np.int64]
np_ndarray_int: TypeAlias = npt.NDArray[np.signedinteger]
np_ndarray_anyint: TypeAlias = npt.NDArray[np.integer]
np_ndarray_bool: TypeAlias = npt.NDArray[np.bool_]
np_ndarray_str: TypeAlias = npt.NDArray[np.str_]

IndexType: TypeAlias = slice | np_ndarray_anyint | Index | list[int] | Series[int]
MaskType: TypeAlias = Series[bool] | np_ndarray_bool | list[bool]
# Scratch types for generics
S1 = TypeVar(
    "S1",
    str,
    bytes,
    datetime.date,
    datetime.time,
    bool,
    int,
    float,
    complex,
    Timestamp,
    Timedelta,
    Period,
    Interval[int],
    Interval[float],
    Interval[Timestamp],
    Interval[Timedelta],
    CategoricalDtype,
)
T1 = TypeVar(
    "T1", str, int, np.int64, np.uint64, np.float64, float, np.dtype[np.generic]
)
T2 = TypeVar("T2", str, int)

IndexingInt: TypeAlias = (
    int | np.int_ | np.integer | np.unsignedinteger | np.signedinteger | np.int8
)
TimestampConvertibleTypes: TypeAlias = (
    Timestamp
    | datetime.datetime
    | datetime.date
    | np.datetime64
    | np.int64
    | float
    | str
)
TimedeltaConvertibleTypes: TypeAlias = (
    Timedelta | datetime.timedelta | np.timedelta64 | np.int64 | float | str
)
# NDFrameT is stricter and ensures that the same subclass of NDFrame always is
# used. E.g. `def func(a: NDFrameT) -> NDFrameT: ...` means that if a
# Series is passed into a function, a Series is always returned and if a DataFrame is
# passed in, a DataFrame is always returned.
NDFrameT = TypeVar("NDFrameT", bound=NDFrame)

IndexT = TypeVar("IndexT", bound=Index)

# Interval closed type
IntervalT = TypeVar(
    "IntervalT",
    Interval[int],
    Interval[float],
    Interval[Timestamp],
    Interval[Timedelta],
)
IntervalClosedType: TypeAlias = Literal["left", "right", "both", "neither"]

TakeIndexer: TypeAlias = Sequence[int] | Sequence[np.integer] | npt.NDArray[np.integer]

IgnoreRaiseCoerce: TypeAlias = Literal["ignore", "raise", "coerce"]

# Shared by functions such as drop and astype
IgnoreRaise: TypeAlias = Literal["ignore", "raise"]

# for arbitrary kwargs passed during reading/writing files
StorageOptions: TypeAlias = dict[str, Any] | None

# compression keywords and compression
CompressionDict: TypeAlias = dict[str, Any]
CompressionOptions: TypeAlias = (
    None | Literal["infer", "gzip", "bz2", "zip", "xz", "zstd"] | CompressionDict
)
FormattersType: TypeAlias = (
    list[Callable] | tuple[Callable, ...] | Mapping[str | int, Callable]
)
FloatFormatType: TypeAlias = str | Callable | EngFormatter
# converters
ConvertersArg: TypeAlias = dict[Hashable, Callable[[Dtype], Dtype]]

# parse_dates
ParseDatesArg: TypeAlias = (
    bool | list[Hashable] | list[list[Hashable]] | dict[Hashable, list[Hashable]]
)

# read_xml parsers
XMLParsers: TypeAlias = Literal["lxml", "etree"]

# Any plain Python or numpy function
Function: TypeAlias = np.ufunc | Callable[..., Any]
# Use a distinct HashableT in shared types to avoid conflicts with
# shared HashableT and HashableT#. This one can be used if the identical
# type is need in a function that uses GroupByObjectNonScalar
_HashableTa = TypeVar("_HashableTa", bound=Hashable)
GroupByObjectNonScalar: TypeAlias = (
    tuple
    | list[_HashableTa]
    | Function
    | list[Function]
    | Series
    | list[Series]
    | np.ndarray
    | list[np.ndarray]
    | Mapping[Label, Any]
    | list[Mapping[Label, Any]]
    | Index
    | list[Index]
    | Grouper
    | list[Grouper]
)
GroupByObject: TypeAlias = Scalar | GroupByObjectNonScalar

StataDateFormat: TypeAlias = Literal[
    "tc",
    "%tc",
    "td",
    "%td",
    "tw",
    "%tw",
    "tm",
    "%tm",
    "tq",
    "%tq",
    "th",
    "%th",
    "ty",
    "%ty",
]

FillnaOptions: TypeAlias = Literal["backfill", "bfill", "ffill", "pad"]
ReplaceMethod: TypeAlias = Literal["pad", "ffill", "bfill"]
SortKind: TypeAlias = Literal["quicksort", "mergesort", "heapsort", "stable"]
NaPosition: TypeAlias = Literal["first", "last"]
JoinHow: TypeAlias = Literal["left", "right", "outer", "inner"]
MergeHow: TypeAlias = JoinHow | Literal["cross"]
JsonFrameOrient: TypeAlias = Literal[
    "split", "records", "index", "columns", "values", "table"
]
JsonSeriesOrient: TypeAlias = Literal["split", "records", "index", "table"]

TimestampConvention: TypeAlias = Literal["start", "end", "s", "e"]

CSVEngine: TypeAlias = Literal["c", "python", "pyarrow", "python-fwf"]
CSVQuoting: TypeAlias = Literal[0, 1, 2, 3]

HDFCompLib: TypeAlias = Literal["zlib", "lzo", "bzip2", "blosc"]
ParquetEngine: TypeAlias = Literal["auto", "pyarrow", "fastparquet"]
FileWriteMode: TypeAlias = Literal[
    "a", "w", "x", "at", "wt", "xt", "ab", "wb", "xb", "w+", "w+b", "a+", "a+b"
]
ColspaceArgType: TypeAlias = (
    str | int | Sequence[int | str] | Mapping[Hashable, str | int]
)

# Windowing rank methods
WindowingRankType: TypeAlias = Literal["average", "min", "max"]
WindowingEngine: TypeAlias = Literal["cython", "numba"] | None

class _WindowingNumbaKwargs(TypedDict, total=False):
    nopython: bool
    nogil: bool
    parallel: bool

WindowingEngineKwargs: TypeAlias = _WindowingNumbaKwargs | None
QuantileInterpolation: TypeAlias = Literal[
    "linear", "lower", "higher", "midpoint", "nearest"
]

class StyleExportDict(TypedDict, total=False):
    apply: Any
    table_attributes: Any
    table_styles: Any
    hide_index: bool
    hide_columns: bool
    hide_index_names: bool
    hide_column_names: bool
    css: dict[str, str | int]

CalculationMethod: TypeAlias = Literal["single", "table"]

ValidationOptions: TypeAlias = Literal[
    "one_to_one",
    "1:1",
    "one_to_many",
    "1:m",
    "many_to_one",
    "m:1",
    "many_to_many",
    "m:m",
]

RandomState: TypeAlias = (
    int
    | ArrayLike
    | np.random.Generator
    | np.random.BitGenerator
    | np.random.RandomState
)

__all__ = ["npt", "type_t"]
