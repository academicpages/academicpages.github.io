import datetime as dt
from datetime import timedelta
from typing import (
    ClassVar,
    Literal,
    NamedTuple,
    overload,
)

import numpy as np
import pandas as pd
from pandas import (
    DatetimeIndex,
    Float64Index,
    Int64Index,
    PeriodIndex,
    Series,
    TimedeltaIndex,
)
from pandas.core.series import (
    TimedeltaSeries,
    TimestampSeries,
)
from typing_extensions import (
    Self,
    TypeAlias,
)

from pandas._libs.tslibs import (
    BaseOffset,
    NaTType,
)
from pandas._libs.tslibs.period import Period
from pandas._libs.tslibs.timestamps import Timestamp
from pandas._typing import npt

class Components(NamedTuple):
    days: int
    hours: int
    minutes: int
    seconds: int
    milliseconds: int
    microseconds: int
    nanoseconds: int

# This should be kept consistent with the keys in the dict timedelta_abbrevs
# in pandas/_libs/tslibs/timedeltas.pyx
TimeDeltaUnitChoices: TypeAlias = Literal[
    "H",
    "T",
    "S",
    "L",
    "U",
    "N",
    "W",
    "w",
    "D",
    "d",
    "days",
    "day",
    "hours",
    "hour",
    "hr",
    "h",
    "m",
    "minute",
    "min",
    "minutes",
    "t",
    "s",
    "seconds",
    "sec",
    "second",
    "ms",
    "milliseconds",
    "millisecond",
    "milli",
    "millis",
    "l",
    "us",
    "microseconds",
    "microsecond",
    "µs",
    "micro",
    "micros",
    "u",
    "ns",
    "nanoseconds",
    "nano",
    "nanos",
    "nanosecond",
    "n",
]

UnitChoices: TypeAlias = (
    TimeDeltaUnitChoices
    | Literal[
        "Y",
        "y",
        "M",
    ]
)

class Timedelta(timedelta):
    min: ClassVar[Timedelta]
    max: ClassVar[Timedelta]
    resolution: ClassVar[Timedelta]
    value: int
    def __new__(
        cls,
        value: str | int | Timedelta | timedelta | np.timedelta64 = ...,
        unit: TimeDeltaUnitChoices = ...,
        *,
        days: float | np.integer | np.floating = ...,
        seconds: float | np.integer | np.floating = ...,
        microseconds: float | np.integer | np.floating = ...,
        milliseconds: float | np.integer | np.floating = ...,
        minutes: float | np.integer | np.floating = ...,
        hours: float | np.integer | np.floating = ...,
        weeks: float | np.integer | np.floating = ...,
    ) -> Self: ...
    # GH 46171
    # While Timedelta can return pd.NaT, having the constructor return
    # a Union with NaTType makes things awkward for users of pandas
    @property
    def days(self) -> int: ...
    @property
    def nanoseconds(self) -> int: ...
    @property
    def seconds(self) -> int: ...
    @property
    def microseconds(self) -> int: ...
    def total_seconds(self) -> float: ...
    def to_pytimedelta(self) -> timedelta: ...
    def to_timedelta64(self) -> np.timedelta64: ...
    @property
    def asm8(self) -> np.timedelta64: ...
    # TODO: round/floor/ceil could return NaT?
    def round(self, freq: str | BaseOffset) -> Self: ...
    def floor(self, freq: str | BaseOffset) -> Self: ...
    def ceil(self, freq: str | BaseOffset) -> Self: ...
    @property
    def resolution_string(self) -> str: ...
    # Override due to more types supported than dt.timedelta
    @overload  # type: ignore[override]
    def __add__(self, other: timedelta | Timedelta | np.timedelta64) -> Timedelta: ...
    @overload
    def __add__(self, other: dt.datetime | np.datetime64 | Timestamp) -> Timestamp: ...
    @overload
    def __add__(self, other: NaTType) -> NaTType: ...
    @overload
    def __add__(self, other: Period) -> Period: ...
    @overload
    def __add__(self, other: dt.date) -> dt.date: ...
    @overload
    def __add__(self, other: PeriodIndex) -> PeriodIndex: ...
    @overload
    def __add__(self, other: DatetimeIndex) -> DatetimeIndex: ...
    @overload
    def __add__(
        self, other: npt.NDArray[np.timedelta64]
    ) -> npt.NDArray[np.timedelta64]: ...
    @overload
    def __add__(
        self, other: npt.NDArray[np.datetime64]
    ) -> npt.NDArray[np.datetime64]: ...
    @overload
    def __add__(self, other: pd.TimedeltaIndex) -> pd.TimedeltaIndex: ...
    @overload
    def __add__(
        self,
        other: TimedeltaSeries,
    ) -> TimedeltaSeries: ...
    @overload
    def __add__(self, other: TimestampSeries) -> TimestampSeries: ...
    @overload
    def __radd__(self, other: np.datetime64) -> Timestamp: ...
    @overload
    def __radd__(self, other: timedelta | Timedelta | np.timedelta64) -> Timedelta: ...
    @overload
    def __radd__(self, other: NaTType) -> NaTType: ...
    @overload
    def __radd__(
        self, other: npt.NDArray[np.timedelta64]
    ) -> npt.NDArray[np.timedelta64]: ...
    @overload
    def __radd__(
        self, other: npt.NDArray[np.datetime64]
    ) -> npt.NDArray[np.datetime64]: ...
    @overload
    def __radd__(self, other: pd.TimedeltaIndex) -> pd.TimedeltaIndex: ...
    @overload
    def __radd__(self, other: pd.PeriodIndex) -> pd.PeriodIndex: ...
    # Override due to more types supported than dt.timedelta
    @overload  # type: ignore[override]
    def __sub__(self, other: timedelta | Timedelta | np.timedelta64) -> Timedelta: ...
    @overload
    def __sub__(self, other: NaTType) -> NaTType: ...
    @overload
    def __sub__(
        self, other: npt.NDArray[np.timedelta64]
    ) -> npt.NDArray[np.timedelta64]: ...
    @overload
    def __sub__(self, other: pd.TimedeltaIndex) -> TimedeltaIndex: ...
    @overload
    def __sub__(
        self, other: TimedeltaSeries | Series[pd.Timedelta]
    ) -> TimedeltaSeries: ...
    @overload
    def __rsub__(self, other: timedelta | Timedelta | np.timedelta64) -> Timedelta: ...
    @overload
    def __rsub__(self, other: Timestamp | np.datetime64) -> Timestamp: ...
    @overload
    def __rsub__(self, other: NaTType) -> NaTType: ...
    @overload
    def __rsub__(self, other: Period) -> Period: ...
    @overload
    def __rsub__(self, other: PeriodIndex) -> PeriodIndex: ...
    @overload
    def __rsub__(self, other: DatetimeIndex) -> DatetimeIndex: ...
    @overload
    def __rsub__(
        self, other: npt.NDArray[np.datetime64]
    ) -> npt.NDArray[np.datetime64]: ...
    @overload
    def __rsub__(
        self, other: npt.NDArray[np.timedelta64]
    ) -> npt.NDArray[np.timedelta64]: ...
    @overload
    def __rsub__(self, other: pd.TimedeltaIndex) -> pd.TimedeltaIndex: ...
    def __neg__(self) -> Timedelta: ...
    def __pos__(self) -> Timedelta: ...
    def __abs__(self) -> Timedelta: ...
    # Override due to more types supported than dt.timedelta
    @overload  # type: ignore[override]
    def __mul__(self, other: float) -> Timedelta: ...
    @overload
    def __mul__(
        self, other: npt.NDArray[np.integer] | npt.NDArray[np.floating]
    ) -> npt.NDArray[np.timedelta64]: ...
    @overload
    def __mul__(self, other: Series[int]) -> TimedeltaSeries: ...
    @overload
    def __mul__(self, other: Series[float]) -> TimedeltaSeries: ...
    @overload
    def __mul__(self, other: Int64Index | Float64Index) -> TimedeltaIndex: ...
    @overload
    def __rmul__(self, other: float) -> Timedelta: ...
    @overload
    def __rmul__(self, other: np.ndarray) -> np.ndarray: ...
    @overload
    def __rmul__(self, other: Series[int]) -> TimedeltaSeries: ...
    @overload
    def __rmul__(self, other: Series[float]) -> TimedeltaSeries: ...
    @overload
    def __rmul__(self, other: Int64Index | Float64Index) -> TimedeltaIndex: ...
    # Override due to more types supported than dt.timedelta
    # error: Signature of "__floordiv__" incompatible with supertype "timedelta"
    @overload  # type: ignore[override]
    def __floordiv__(self, other: timedelta | Timedelta | np.timedelta64) -> int: ...
    @overload
    def __floordiv__(self, other: float) -> Timedelta: ...
    @overload
    def __floordiv__(
        self, other: npt.NDArray[np.integer] | npt.NDArray[np.floating]
    ) -> npt.NDArray[np.timedelta64]: ...
    @overload
    def __floordiv__(
        self, other: npt.NDArray[np.timedelta64]
    ) -> npt.NDArray[np.int_]: ...
    @overload
    def __floordiv__(self, other: Int64Index | Float64Index) -> TimedeltaIndex: ...
    @overload
    def __floordiv__(self, other: Series[int]) -> TimedeltaSeries: ...
    @overload
    def __floordiv__(self, other: Series[float]) -> TimedeltaSeries: ...
    @overload
    def __floordiv__(self, other: TimedeltaSeries) -> Series[int]: ...
    @overload
    def __floordiv__(self, other: NaTType | None) -> float: ...
    @overload
    def __rfloordiv__(self, other: timedelta | Timedelta | str) -> int: ...
    @overload
    def __rfloordiv__(self, other: NaTType | None) -> float: ...
    @overload
    def __rfloordiv__(
        self, other: npt.NDArray[np.timedelta64]
    ) -> npt.NDArray[np.int_]: ...
    # Override due to more types supported than dt.timedelta
    @overload  # type: ignore[override]
    def __truediv__(self, other: timedelta | Timedelta | NaTType) -> float: ...
    @overload
    def __truediv__(self, other: float) -> Timedelta: ...
    @overload
    def __truediv__(
        self, other: npt.NDArray[np.integer] | npt.NDArray[np.floating]
    ) -> npt.NDArray[np.timedelta64]: ...
    @overload
    def __truediv__(self, other: TimedeltaSeries) -> Series[float]: ...
    @overload
    def __truediv__(self, other: Series[int]) -> TimedeltaSeries: ...
    @overload
    def __truediv__(self, other: Series[float]) -> TimedeltaSeries: ...
    @overload
    def __truediv__(self, other: Int64Index | Float64Index) -> TimedeltaIndex: ...
    def __rtruediv__(self, other: timedelta | Timedelta | NaTType) -> float: ...
    # Override due to more types supported than dt.timedelta
    @overload
    def __eq__(self, other: timedelta | Timedelta | np.timedelta64) -> bool: ...  # type: ignore[misc] # pyright: ignore[reportOverlappingOverload]
    @overload
    def __eq__(self, other: TimedeltaSeries | Series[pd.Timedelta]) -> Series[bool]: ...  # type: ignore[misc]
    @overload
    def __eq__(  # type: ignore[misc]
        self, other: TimedeltaIndex | npt.NDArray[np.timedelta64]
    ) -> npt.NDArray[np.bool_]: ...
    @overload
    def __eq__(self, other: object) -> Literal[False]: ...
    # Override due to more types supported than dt.timedelta
    @overload
    def __ne__(self, other: timedelta | Timedelta | np.timedelta64) -> bool: ...  # type: ignore[misc] # pyright: ignore[reportOverlappingOverload]
    @overload
    def __ne__(self, other: TimedeltaSeries | Series[pd.Timedelta]) -> Series[bool]: ...  # type: ignore[misc]
    @overload
    def __ne__(  # type: ignore[misc]
        self, other: TimedeltaIndex | npt.NDArray[np.timedelta64]
    ) -> npt.NDArray[np.bool_]: ...
    @overload
    def __ne__(self, other: object) -> Literal[True]: ...
    # Override due to more types supported than dt.timedelta
    @overload  # type: ignore[override]
    def __mod__(self, other: timedelta) -> Timedelta: ...
    @overload
    def __mod__(self, other: float) -> Timedelta: ...
    @overload
    def __mod__(self, other: Series[int] | Series[float]) -> TimedeltaSeries: ...
    @overload
    def __mod__(self, other: Int64Index | Float64Index) -> TimedeltaIndex: ...
    @overload
    def __mod__(
        self, other: npt.NDArray[np.integer] | npt.NDArray[np.floating]
    ) -> npt.NDArray[np.timedelta64]: ...
    @overload
    def __mod__(
        self, other: Series[int] | Series[float] | TimedeltaSeries
    ) -> TimedeltaSeries: ...
    def __divmod__(self, other: timedelta) -> tuple[int, Timedelta]: ...
    # Mypy complains Forward operator "<inequality op>" is not callable, so ignore misc
    # for le, lt ge and gt
    # Override due to more types supported than dt.timedelta
    @overload  # type: ignore[override]
    def __le__(self, other: timedelta | Timedelta | np.timedelta64) -> bool: ...  # type: ignore[misc]
    @overload
    def __le__(
        self, other: TimedeltaIndex | npt.NDArray[np.timedelta64]
    ) -> npt.NDArray[np.bool_]: ...
    @overload
    def __le__(self, other: TimedeltaSeries | Series[pd.Timedelta]) -> Series[bool]: ...
    # Override due to more types supported than dt.timedelta
    @overload  # type: ignore[override]
    def __lt__(self, other: timedelta | Timedelta | np.timedelta64) -> bool: ...  # type: ignore[misc]
    @overload
    def __lt__(
        self, other: TimedeltaIndex | npt.NDArray[np.timedelta64]
    ) -> npt.NDArray[np.bool_]: ...
    @overload
    def __lt__(self, other: TimedeltaSeries | Series[pd.Timedelta]) -> Series[bool]: ...
    # Override due to more types supported than dt.timedelta
    @overload  # type: ignore[override]
    def __ge__(self, other: timedelta | Timedelta | np.timedelta64) -> bool: ...  # type: ignore[misc]
    @overload
    def __ge__(
        self, other: TimedeltaIndex | npt.NDArray[np.timedelta64]
    ) -> npt.NDArray[np.bool_]: ...
    @overload
    def __ge__(self, other: TimedeltaSeries | Series[pd.Timedelta]) -> Series[bool]: ...
    # Override due to more types supported than dt.timedelta
    @overload  # type: ignore[override]
    def __gt__(self, other: timedelta | Timedelta | np.timedelta64) -> bool: ...  # type: ignore[misc]
    @overload
    def __gt__(
        self, other: TimedeltaIndex | npt.NDArray[np.timedelta64]
    ) -> npt.NDArray[np.bool_]: ...
    @overload
    def __gt__(self, other: TimedeltaSeries | Series[pd.Timedelta]) -> Series[bool]: ...
    def isoformat(self) -> str: ...
    def to_numpy(self) -> np.timedelta64: ...
    @property
    def components(self) -> Components: ...
    def view(self, dtype: npt.DTypeLike = ...) -> object: ...
