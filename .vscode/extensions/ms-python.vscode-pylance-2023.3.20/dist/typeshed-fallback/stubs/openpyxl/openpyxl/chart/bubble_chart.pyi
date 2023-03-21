from _typeshed import Incomplete

from ._chart import ChartBase

class BubbleChart(ChartBase):
    tagname: str
    varyColors: Incomplete
    ser: Incomplete
    dLbls: Incomplete
    dataLabels: Incomplete
    bubble3D: Incomplete
    bubbleScale: Incomplete
    showNegBubbles: Incomplete
    sizeRepresents: Incomplete
    extLst: Incomplete
    x_axis: Incomplete
    y_axis: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        varyColors: Incomplete | None = ...,
        ser=...,
        dLbls: Incomplete | None = ...,
        bubble3D: Incomplete | None = ...,
        bubbleScale: Incomplete | None = ...,
        showNegBubbles: Incomplete | None = ...,
        sizeRepresents: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
        **kw,
    ) -> None: ...
