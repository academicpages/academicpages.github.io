from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

class Marker(Serialisable):
    tagname: str
    symbol: Incomplete
    size: Incomplete
    spPr: Incomplete
    graphicalProperties: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        symbol: Incomplete | None = ...,
        size: Incomplete | None = ...,
        spPr: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
    ) -> None: ...

class DataPoint(Serialisable):
    tagname: str
    idx: Incomplete
    invertIfNegative: Incomplete
    marker: Incomplete
    bubble3D: Incomplete
    explosion: Incomplete
    spPr: Incomplete
    graphicalProperties: Incomplete
    pictureOptions: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        idx: Incomplete | None = ...,
        invertIfNegative: Incomplete | None = ...,
        marker: Incomplete | None = ...,
        bubble3D: Incomplete | None = ...,
        explosion: Incomplete | None = ...,
        spPr: Incomplete | None = ...,
        pictureOptions: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
    ) -> None: ...
