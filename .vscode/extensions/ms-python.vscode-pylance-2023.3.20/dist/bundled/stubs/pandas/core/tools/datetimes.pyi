from collections.abc import Sequence
from datetime import (
    date,
    datetime,
)
from typing import (
    Literal,
    overload,
)

import numpy as np
from pandas import (
    Index,
    Timestamp,
)
from pandas.core.arrays import ExtensionArray
from pandas.core.indexes.datetimes import DatetimeIndex
from pandas.core.series import (
    Series,
    TimestampSeries,
)
from typing_extensions import TypeAlias

from pandas._libs.tslibs import NaTType
from pandas._typing import (
    AnyArrayLike,
    DictConvertible,
    IgnoreRaise,
    IgnoreRaiseCoerce,
    TimestampConvertibleTypes,
    npt,
)

ArrayConvertible: TypeAlias = list | tuple | AnyArrayLike
Scalar: TypeAlias = float | str
DatetimeScalar: TypeAlias = Scalar | datetime | np.datetime64 | date

DatetimeScalarOrArrayConvertible: TypeAlias = DatetimeScalar | ArrayConvertible

@overload
def to_datetime(
    arg: DatetimeScalar,
    errors: IgnoreRaise = ...,
    dayfirst: bool = ...,
    yearfirst: bool = ...,
    utc: bool | None = ...,
    format: str | None = ...,
    exact: bool = ...,
    unit: str | None = ...,
    infer_datetime_format: bool = ...,
    origin: Literal["julian", "unix"] | TimestampConvertibleTypes = ...,
    cache: bool = ...,
) -> Timestamp: ...
@overload
def to_datetime(
    arg: DatetimeScalar,
    errors: Literal["coerce"],
    dayfirst: bool = ...,
    yearfirst: bool = ...,
    utc: bool | None = ...,
    format: str | None = ...,
    exact: bool = ...,
    unit: str | None = ...,
    infer_datetime_format: bool = ...,
    origin: Literal["julian", "unix"] | TimestampConvertibleTypes = ...,
    cache: bool = ...,
) -> Timestamp | NaTType: ...
@overload
def to_datetime(
    arg: Series | DictConvertible,
    errors: IgnoreRaiseCoerce = ...,
    dayfirst: bool = ...,
    yearfirst: bool = ...,
    utc: bool | None = ...,
    format: str | None = ...,
    exact: bool = ...,
    unit: str | None = ...,
    infer_datetime_format: bool = ...,
    origin: Literal["julian", "unix"] | TimestampConvertibleTypes = ...,
    cache: bool = ...,
) -> TimestampSeries: ...
@overload
def to_datetime(
    arg: Sequence[float | datetime]
    | list[str]
    | tuple[float | str | datetime, ...]
    | npt.NDArray[np.datetime64]
    | npt.NDArray[np.str_]
    | npt.NDArray[np.int_]
    | Index
    | ExtensionArray,
    errors: IgnoreRaiseCoerce = ...,
    dayfirst: bool = ...,
    yearfirst: bool = ...,
    utc: bool | None = ...,
    format: str | None = ...,
    exact: bool = ...,
    unit: str | None = ...,
    infer_datetime_format: bool = ...,
    origin: Literal["julian", "unix"] | TimestampConvertibleTypes = ...,
    cache: bool = ...,
) -> DatetimeIndex: ...
