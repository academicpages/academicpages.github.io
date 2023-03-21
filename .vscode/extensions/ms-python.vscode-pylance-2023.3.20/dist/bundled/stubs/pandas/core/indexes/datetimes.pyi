from collections.abc import (
    Hashable,
    Sequence,
)
from datetime import (
    timedelta,
    tzinfo,
)
from typing import overload

import numpy as np
from pandas import (
    DataFrame,
    Timedelta,
    TimedeltaIndex,
    Timestamp,
)
from pandas.core.indexes.accessors import DatetimeIndexProperties
from pandas.core.indexes.api import Float64Index
from pandas.core.indexes.base import _IndexGetitemMixin
from pandas.core.indexes.datetimelike import DatetimeTimedeltaMixin
from pandas.core.series import (
    TimedeltaSeries,
    TimestampSeries,
)

from pandas._typing import (
    AnyArrayLike,
    ArrayLike,
    DateAndDatetimeLike,
    IntervalClosedType,
)

from pandas.core.dtypes.dtypes import DatetimeTZDtype

from pandas.tseries.offsets import BaseOffset

# type ignore needed because of __getitem__()
class DatetimeIndex(  # type: ignore[misc]
    _IndexGetitemMixin[Timestamp],
    DatetimeTimedeltaMixin,
    DatetimeIndexProperties,
):
    def __init__(
        self,
        data: ArrayLike | AnyArrayLike | list | tuple,
        freq=...,
        tz=...,
        normalize: bool = ...,
        closed=...,
        ambiguous: str = ...,
        dayfirst: bool = ...,
        yearfirst: bool = ...,
        dtype=...,
        copy: bool = ...,
        name=...,
    ): ...
    def __array__(self, dtype=...) -> np.ndarray: ...
    def __reduce__(self): ...
    # various ignores needed for mypy, as we do want to restrict what can be used in
    # arithmetic for these types
    @overload
    def __add__(self, other: TimedeltaSeries) -> TimestampSeries: ...
    @overload
    def __add__(self, other: Timedelta | TimedeltaIndex) -> DatetimeIndex: ...
    @overload
    def __sub__(self, other: TimedeltaSeries) -> TimestampSeries: ...
    @overload
    def __sub__(self, other: Timedelta | TimedeltaIndex) -> DatetimeIndex: ...
    @overload
    def __sub__(self, other: Timestamp | DatetimeIndex) -> TimedeltaIndex: ...
    # overload needed because Index.to_series() and DatetimeIndex.to_series() have
    # different arguments
    def to_series(self, keep_tz=..., index=..., name=...) -> TimestampSeries: ...  # type: ignore[override]
    def snap(self, freq: str = ...): ...
    def get_value(self, series, key): ...
    def get_loc(self, key, tolerance=...): ...
    def slice_indexer(self, start=..., end=..., step=...): ...
    def searchsorted(self, value, side: str = ..., sorter=...): ...
    def is_type_compatible(self, typ) -> bool: ...
    @property
    def inferred_type(self) -> str: ...
    def insert(self, loc, item): ...
    def indexer_at_time(self, time, asof: bool = ...): ...
    def indexer_between_time(
        self, start_time, end_time, include_start: bool = ..., include_end: bool = ...
    ): ...
    def to_perioddelta(self, freq) -> TimedeltaIndex: ...
    def to_julian_date(self) -> Float64Index: ...
    def isocalendar(self) -> DataFrame: ...
    @property
    def tzinfo(self) -> tzinfo | None: ...
    @property
    def dtype(self) -> np.dtype | DatetimeTZDtype: ...

def date_range(
    start: str | DateAndDatetimeLike | None = ...,
    end: str | DateAndDatetimeLike | None = ...,
    periods: int | None = ...,
    freq: str | timedelta | Timedelta | BaseOffset = ...,
    tz: str | tzinfo = ...,
    normalize: bool = ...,
    name: Hashable | None = ...,
    inclusive: IntervalClosedType = ...,
) -> DatetimeIndex: ...
@overload
def bdate_range(
    start: str | DateAndDatetimeLike | None = ...,
    end: str | DateAndDatetimeLike | None = ...,
    periods: int | None = ...,
    freq: str | timedelta | Timedelta | BaseOffset = ...,
    tz: str | tzinfo = ...,
    normalize: bool = ...,
    name: Hashable | None = ...,
    weekmask: str | None = ...,
    holidays: None = ...,
    inclusive: IntervalClosedType = ...,
) -> DatetimeIndex: ...
@overload
def bdate_range(
    start: str | DateAndDatetimeLike | None = ...,
    end: str | DateAndDatetimeLike | None = ...,
    periods: int | None = ...,
    *,
    freq: str | timedelta | Timedelta | BaseOffset,
    tz: str | tzinfo = ...,
    normalize: bool = ...,
    name: Hashable | None = ...,
    weekmask: str | None = ...,
    holidays: Sequence[str | DateAndDatetimeLike],
    inclusive: IntervalClosedType = ...,
) -> DatetimeIndex: ...
