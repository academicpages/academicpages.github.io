from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

class LegendEntry(Serialisable):
    tagname: str
    idx: Incomplete
    delete: Incomplete
    txPr: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(
        self, idx: int = ..., delete: bool = ..., txPr: Incomplete | None = ..., extLst: Incomplete | None = ...
    ) -> None: ...

class Legend(Serialisable):
    tagname: str
    legendPos: Incomplete
    position: Incomplete
    legendEntry: Incomplete
    layout: Incomplete
    overlay: Incomplete
    spPr: Incomplete
    graphicalProperties: Incomplete
    txPr: Incomplete
    textProperties: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        legendPos: str = ...,
        legendEntry=...,
        layout: Incomplete | None = ...,
        overlay: Incomplete | None = ...,
        spPr: Incomplete | None = ...,
        txPr: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
    ) -> None: ...
