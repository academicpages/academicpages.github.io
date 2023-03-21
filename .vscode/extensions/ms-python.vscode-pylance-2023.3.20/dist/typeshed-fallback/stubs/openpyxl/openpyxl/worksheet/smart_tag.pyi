from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

class CellSmartTagPr(Serialisable):
    tagname: str
    key: Incomplete
    val: Incomplete
    def __init__(self, key: Incomplete | None = ..., val: Incomplete | None = ...) -> None: ...

class CellSmartTag(Serialisable):
    tagname: str
    cellSmartTagPr: Incomplete
    type: Incomplete
    deleted: Incomplete
    xmlBased: Incomplete
    __elements__: Incomplete
    def __init__(self, cellSmartTagPr=..., type: Incomplete | None = ..., deleted: bool = ..., xmlBased: bool = ...) -> None: ...

class CellSmartTags(Serialisable):
    tagname: str
    cellSmartTag: Incomplete
    r: Incomplete
    __elements__: Incomplete
    def __init__(self, cellSmartTag=..., r: Incomplete | None = ...) -> None: ...

class SmartTags(Serialisable):
    tagname: str
    cellSmartTags: Incomplete
    __elements__: Incomplete
    def __init__(self, cellSmartTags=...) -> None: ...
