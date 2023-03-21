from collections.abc import Callable
from typing import (
    Any,
    overload,
)

from pandas import (
    DataFrame,
    Series,
)
from pandas.core.window.rolling import (
    BaseWindowGroupby,
    RollingAndExpandingMixin,
)

from pandas._typing import (
    AggFuncTypeBase,
    AggFuncTypeFrame,
    AggFuncTypeSeriesToFrame,
    NDFrameT,
    QuantileInterpolation,
    WindowingEngine,
    WindowingEngineKwargs,
    WindowingRankType,
)

class Expanding(RollingAndExpandingMixin[NDFrameT]):
    @overload
    def aggregate(
        self: Expanding[Series], func: AggFuncTypeBase, *args: Any, **kwargs: Any
    ) -> Series: ...
    @overload
    def aggregate(
        self: Expanding[Series],
        func: AggFuncTypeSeriesToFrame,
        *args: Any,
        **kwargs: Any,
    ) -> DataFrame: ...
    @overload
    def aggregate(
        self: Expanding[DataFrame],
        func: AggFuncTypeFrame,
        *args: Any,
        **kwargs: Any,
    ) -> DataFrame: ...
    def count(self) -> NDFrameT: ...
    def apply(
        self,
        func: Callable[..., Any],
        raw: bool = ...,
        engine: WindowingEngine = ...,
        engine_kwargs: WindowingEngineKwargs = ...,
        args: tuple[Any, ...] | None = ...,
        kwargs: dict[str, Any] | None = ...,
    ) -> NDFrameT: ...
    def sum(
        self,
        numeric_only: bool = ...,
        *,
        engine: WindowingEngine = ...,
        engine_kwargs: WindowingEngineKwargs = ...,
    ) -> NDFrameT: ...
    def max(
        self,
        numeric_only: bool = ...,
        *,
        engine: WindowingEngine = ...,
        engine_kwargs: WindowingEngineKwargs = ...,
    ) -> NDFrameT: ...
    def min(
        self,
        numeric_only: bool = ...,
        *,
        engine: WindowingEngine = ...,
        engine_kwargs: WindowingEngineKwargs = ...,
    ) -> NDFrameT: ...
    def mean(
        self,
        numeric_only: bool = ...,
        *,
        engine: WindowingEngine = ...,
        engine_kwargs: WindowingEngineKwargs = ...,
    ) -> NDFrameT: ...
    def median(
        self,
        numeric_only: bool = ...,
        engine: WindowingEngine = ...,
        engine_kwargs: WindowingEngineKwargs = ...,
    ) -> NDFrameT: ...
    def std(
        self,
        ddof: int = ...,
        numeric_only: bool = ...,
        *,
        engine: WindowingEngine = ...,
        engine_kwargs: WindowingEngineKwargs = ...,
    ) -> NDFrameT: ...
    def var(
        self,
        ddof: int = ...,
        numeric_only: bool = ...,
        *,
        engine: WindowingEngine = ...,
        engine_kwargs: WindowingEngineKwargs = ...,
    ) -> NDFrameT: ...
    def sem(self, ddof: int = ..., numeric_only: bool = ...) -> NDFrameT: ...
    def skew(
        self,
        numeric_only: bool = ...,
    ) -> NDFrameT: ...
    def kurt(
        self,
        numeric_only: bool = ...,
    ) -> NDFrameT: ...
    def quantile(
        self,
        quantile: float,
        interpolation: QuantileInterpolation = ...,
        numeric_only: bool = ...,
    ) -> NDFrameT: ...
    def rank(
        self,
        method: WindowingRankType = ...,
        ascending: bool = ...,
        pct: bool = ...,
        numeric_only: bool = ...,
    ) -> NDFrameT: ...
    def cov(
        self,
        other: DataFrame | Series | None = ...,
        pairwise: bool | None = ...,
        ddof: int = ...,
        numeric_only: bool = ...,
    ) -> NDFrameT: ...
    def corr(
        self,
        other: DataFrame | Series | None = ...,
        pairwise: bool | None = ...,
        ddof: int = ...,
        numeric_only: bool = ...,
    ) -> NDFrameT: ...

class ExpandingGroupby(BaseWindowGroupby, Expanding): ...
