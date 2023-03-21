from _typeshed import Incomplete
from abc import abstractmethod

from openpyxl.descriptors.serialisable import Serialisable

class ChartLines(Serialisable):
    tagname: str
    spPr: Incomplete
    graphicalProperties: Incomplete
    def __init__(self, spPr: Incomplete | None = ...) -> None: ...

class Scaling(Serialisable):
    tagname: str
    logBase: Incomplete
    orientation: Incomplete
    max: Incomplete
    min: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        logBase: Incomplete | None = ...,
        orientation: str = ...,
        max: Incomplete | None = ...,
        min: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
    ) -> None: ...

class _BaseAxis(Serialisable):
    axId: Incomplete
    scaling: Incomplete
    delete: Incomplete
    axPos: Incomplete
    majorGridlines: Incomplete
    minorGridlines: Incomplete
    title: Incomplete
    numFmt: Incomplete
    number_format: Incomplete
    majorTickMark: Incomplete
    minorTickMark: Incomplete
    tickLblPos: Incomplete
    spPr: Incomplete
    graphicalProperties: Incomplete
    txPr: Incomplete
    textProperties: Incomplete
    crossAx: Incomplete
    crosses: Incomplete
    crossesAt: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        axId: Incomplete | None = ...,
        scaling: Incomplete | None = ...,
        delete: Incomplete | None = ...,
        axPos: str = ...,
        majorGridlines: Incomplete | None = ...,
        minorGridlines: Incomplete | None = ...,
        title: Incomplete | None = ...,
        numFmt: Incomplete | None = ...,
        majorTickMark: Incomplete | None = ...,
        minorTickMark: Incomplete | None = ...,
        tickLblPos: Incomplete | None = ...,
        spPr: Incomplete | None = ...,
        txPr: Incomplete | None = ...,
        crossAx: Incomplete | None = ...,
        crosses: Incomplete | None = ...,
        crossesAt: Incomplete | None = ...,
    ) -> None: ...
    @property
    @abstractmethod
    def tagname(self) -> str: ...

class DisplayUnitsLabel(Serialisable):
    tagname: str
    layout: Incomplete
    tx: Incomplete
    text: Incomplete
    spPr: Incomplete
    graphicalProperties: Incomplete
    txPr: Incomplete
    textPropertes: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        layout: Incomplete | None = ...,
        tx: Incomplete | None = ...,
        spPr: Incomplete | None = ...,
        txPr: Incomplete | None = ...,
    ) -> None: ...

class DisplayUnitsLabelList(Serialisable):
    tagname: str
    custUnit: Incomplete
    builtInUnit: Incomplete
    dispUnitsLbl: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        custUnit: Incomplete | None = ...,
        builtInUnit: Incomplete | None = ...,
        dispUnitsLbl: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
    ) -> None: ...

class NumericAxis(_BaseAxis):
    tagname: str
    axId: Incomplete
    scaling: Incomplete
    delete: Incomplete
    axPos: Incomplete
    majorGridlines: Incomplete
    minorGridlines: Incomplete
    title: Incomplete
    numFmt: Incomplete
    majorTickMark: Incomplete
    minorTickMark: Incomplete
    tickLblPos: Incomplete
    spPr: Incomplete
    txPr: Incomplete
    crossAx: Incomplete
    crosses: Incomplete
    crossesAt: Incomplete
    crossBetween: Incomplete
    majorUnit: Incomplete
    minorUnit: Incomplete
    dispUnits: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        crossBetween: Incomplete | None = ...,
        majorUnit: Incomplete | None = ...,
        minorUnit: Incomplete | None = ...,
        dispUnits: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
        **kw,
    ) -> None: ...
    @classmethod
    def from_tree(cls, node): ...

class TextAxis(_BaseAxis):
    tagname: str
    axId: Incomplete
    scaling: Incomplete
    delete: Incomplete
    axPos: Incomplete
    majorGridlines: Incomplete
    minorGridlines: Incomplete
    title: Incomplete
    numFmt: Incomplete
    majorTickMark: Incomplete
    minorTickMark: Incomplete
    tickLblPos: Incomplete
    spPr: Incomplete
    txPr: Incomplete
    crossAx: Incomplete
    crosses: Incomplete
    crossesAt: Incomplete
    auto: Incomplete
    lblAlgn: Incomplete
    lblOffset: Incomplete
    tickLblSkip: Incomplete
    tickMarkSkip: Incomplete
    noMultiLvlLbl: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        auto: Incomplete | None = ...,
        lblAlgn: Incomplete | None = ...,
        lblOffset: int = ...,
        tickLblSkip: Incomplete | None = ...,
        tickMarkSkip: Incomplete | None = ...,
        noMultiLvlLbl: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
        **kw,
    ) -> None: ...

class DateAxis(TextAxis):
    tagname: str
    axId: Incomplete
    scaling: Incomplete
    delete: Incomplete
    axPos: Incomplete
    majorGridlines: Incomplete
    minorGridlines: Incomplete
    title: Incomplete
    numFmt: Incomplete
    majorTickMark: Incomplete
    minorTickMark: Incomplete
    tickLblPos: Incomplete
    spPr: Incomplete
    txPr: Incomplete
    crossAx: Incomplete
    crosses: Incomplete
    crossesAt: Incomplete
    auto: Incomplete
    lblOffset: Incomplete
    baseTimeUnit: Incomplete
    majorUnit: Incomplete
    majorTimeUnit: Incomplete
    minorUnit: Incomplete
    minorTimeUnit: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        auto: Incomplete | None = ...,
        lblOffset: Incomplete | None = ...,
        baseTimeUnit: Incomplete | None = ...,
        majorUnit: Incomplete | None = ...,
        majorTimeUnit: Incomplete | None = ...,
        minorUnit: Incomplete | None = ...,
        minorTimeUnit: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
        **kw,
    ) -> None: ...

class SeriesAxis(_BaseAxis):
    tagname: str
    axId: Incomplete
    scaling: Incomplete
    delete: Incomplete
    axPos: Incomplete
    majorGridlines: Incomplete
    minorGridlines: Incomplete
    title: Incomplete
    numFmt: Incomplete
    majorTickMark: Incomplete
    minorTickMark: Incomplete
    tickLblPos: Incomplete
    spPr: Incomplete
    txPr: Incomplete
    crossAx: Incomplete
    crosses: Incomplete
    crossesAt: Incomplete
    tickLblSkip: Incomplete
    tickMarkSkip: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(
        self, tickLblSkip: Incomplete | None = ..., tickMarkSkip: Incomplete | None = ..., extLst: Incomplete | None = ..., **kw
    ) -> None: ...
