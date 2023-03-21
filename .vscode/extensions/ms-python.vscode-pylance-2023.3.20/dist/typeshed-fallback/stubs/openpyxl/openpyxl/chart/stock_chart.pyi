from _typeshed import Incomplete

from ._chart import ChartBase

class StockChart(ChartBase):
    tagname: str
    ser: Incomplete
    dLbls: Incomplete
    dataLabels: Incomplete
    dropLines: Incomplete
    hiLowLines: Incomplete
    upDownBars: Incomplete
    extLst: Incomplete
    x_axis: Incomplete
    y_axis: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        ser=...,
        dLbls: Incomplete | None = ...,
        dropLines: Incomplete | None = ...,
        hiLowLines: Incomplete | None = ...,
        upDownBars: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
        **kw,
    ) -> None: ...
