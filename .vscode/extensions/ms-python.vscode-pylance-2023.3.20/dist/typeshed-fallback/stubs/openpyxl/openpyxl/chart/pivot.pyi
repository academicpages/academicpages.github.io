from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

class PivotSource(Serialisable):
    tagname: str
    name: Incomplete
    fmtId: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(
        self, name: Incomplete | None = ..., fmtId: Incomplete | None = ..., extLst: Incomplete | None = ...
    ) -> None: ...

class PivotFormat(Serialisable):
    tagname: str
    idx: Incomplete
    spPr: Incomplete
    graphicalProperties: Incomplete
    txPr: Incomplete
    TextBody: Incomplete
    marker: Incomplete
    dLbl: Incomplete
    DataLabel: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        idx: int = ...,
        spPr: Incomplete | None = ...,
        txPr: Incomplete | None = ...,
        marker: Incomplete | None = ...,
        dLbl: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
    ) -> None: ...
