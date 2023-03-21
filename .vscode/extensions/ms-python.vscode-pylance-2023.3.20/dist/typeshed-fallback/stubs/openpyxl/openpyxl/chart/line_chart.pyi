from _typeshed import Incomplete
from abc import abstractmethod

from ._chart import ChartBase

class _LineChartBase(ChartBase):
    grouping: Incomplete
    varyColors: Incomplete
    ser: Incomplete
    dLbls: Incomplete
    dataLabels: Incomplete
    dropLines: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        grouping: str = ...,
        varyColors: Incomplete | None = ...,
        ser=...,
        dLbls: Incomplete | None = ...,
        dropLines: Incomplete | None = ...,
        **kw,
    ) -> None: ...
    @property
    @abstractmethod
    def tagname(self) -> str: ...

class LineChart(_LineChartBase):
    tagname: str
    grouping: Incomplete
    varyColors: Incomplete
    ser: Incomplete
    dLbls: Incomplete
    dropLines: Incomplete
    hiLowLines: Incomplete
    upDownBars: Incomplete
    marker: Incomplete
    smooth: Incomplete
    extLst: Incomplete
    x_axis: Incomplete
    y_axis: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        hiLowLines: Incomplete | None = ...,
        upDownBars: Incomplete | None = ...,
        marker: Incomplete | None = ...,
        smooth: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
        **kw,
    ) -> None: ...

class LineChart3D(_LineChartBase):
    tagname: str
    grouping: Incomplete
    varyColors: Incomplete
    ser: Incomplete
    dLbls: Incomplete
    dropLines: Incomplete
    gapDepth: Incomplete
    hiLowLines: Incomplete
    upDownBars: Incomplete
    marker: Incomplete
    smooth: Incomplete
    extLst: Incomplete
    x_axis: Incomplete
    y_axis: Incomplete
    z_axis: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        gapDepth: Incomplete | None = ...,
        hiLowLines: Incomplete | None = ...,
        upDownBars: Incomplete | None = ...,
        marker: Incomplete | None = ...,
        smooth: Incomplete | None = ...,
        **kw,
    ) -> None: ...
