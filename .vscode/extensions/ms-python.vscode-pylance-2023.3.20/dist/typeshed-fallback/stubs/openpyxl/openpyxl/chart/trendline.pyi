from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

class TrendlineLabel(Serialisable):
    tagname: str
    layout: Incomplete
    tx: Incomplete
    numFmt: Incomplete
    spPr: Incomplete
    graphicalProperties: Incomplete
    txPr: Incomplete
    textProperties: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        layout: Incomplete | None = ...,
        tx: Incomplete | None = ...,
        numFmt: Incomplete | None = ...,
        spPr: Incomplete | None = ...,
        txPr: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
    ) -> None: ...

class Trendline(Serialisable):
    tagname: str
    name: Incomplete
    spPr: Incomplete
    graphicalProperties: Incomplete
    trendlineType: Incomplete
    order: Incomplete
    period: Incomplete
    forward: Incomplete
    backward: Incomplete
    intercept: Incomplete
    dispRSqr: Incomplete
    dispEq: Incomplete
    trendlineLbl: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        name: Incomplete | None = ...,
        spPr: Incomplete | None = ...,
        trendlineType: str = ...,
        order: Incomplete | None = ...,
        period: Incomplete | None = ...,
        forward: Incomplete | None = ...,
        backward: Incomplete | None = ...,
        intercept: Incomplete | None = ...,
        dispRSqr: Incomplete | None = ...,
        dispEq: Incomplete | None = ...,
        trendlineLbl: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
    ) -> None: ...
