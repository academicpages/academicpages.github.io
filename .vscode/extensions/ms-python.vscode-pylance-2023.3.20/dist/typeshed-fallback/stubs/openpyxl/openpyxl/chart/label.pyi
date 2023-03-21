from _typeshed import Incomplete
from abc import abstractmethod

from openpyxl.descriptors.serialisable import Serialisable as Serialisable

class _DataLabelBase(Serialisable):
    numFmt: Incomplete
    spPr: Incomplete
    graphicalProperties: Incomplete
    txPr: Incomplete
    textProperties: Incomplete
    dLblPos: Incomplete
    position: Incomplete
    showLegendKey: Incomplete
    showVal: Incomplete
    showCatName: Incomplete
    showSerName: Incomplete
    showPercent: Incomplete
    showBubbleSize: Incomplete
    showLeaderLines: Incomplete
    separator: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        numFmt: Incomplete | None = ...,
        spPr: Incomplete | None = ...,
        txPr: Incomplete | None = ...,
        dLblPos: Incomplete | None = ...,
        showLegendKey: Incomplete | None = ...,
        showVal: Incomplete | None = ...,
        showCatName: Incomplete | None = ...,
        showSerName: Incomplete | None = ...,
        showPercent: Incomplete | None = ...,
        showBubbleSize: Incomplete | None = ...,
        showLeaderLines: Incomplete | None = ...,
        separator: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
    ) -> None: ...
    @property
    @abstractmethod
    def tagname(self) -> str: ...

class DataLabel(_DataLabelBase):
    tagname: str
    idx: Incomplete
    numFmt: Incomplete
    spPr: Incomplete
    txPr: Incomplete
    dLblPos: Incomplete
    showLegendKey: Incomplete
    showVal: Incomplete
    showCatName: Incomplete
    showSerName: Incomplete
    showPercent: Incomplete
    showBubbleSize: Incomplete
    showLeaderLines: Incomplete
    separator: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(self, idx: int = ..., **kw) -> None: ...

class DataLabelList(_DataLabelBase):
    tagname: str
    dLbl: Incomplete
    delete: Incomplete
    numFmt: Incomplete
    spPr: Incomplete
    txPr: Incomplete
    dLblPos: Incomplete
    showLegendKey: Incomplete
    showVal: Incomplete
    showCatName: Incomplete
    showSerName: Incomplete
    showPercent: Incomplete
    showBubbleSize: Incomplete
    showLeaderLines: Incomplete
    separator: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(self, dLbl=..., delete: Incomplete | None = ..., **kw) -> None: ...
