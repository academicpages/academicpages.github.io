from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

class TableStyleElement(Serialisable):
    tagname: str
    type: Incomplete
    size: Incomplete
    dxfId: Incomplete
    def __init__(self, type: Incomplete | None = ..., size: Incomplete | None = ..., dxfId: Incomplete | None = ...) -> None: ...

class TableStyle(Serialisable):
    tagname: str
    name: Incomplete
    pivot: Incomplete
    table: Incomplete
    count: Incomplete
    tableStyleElement: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        name: Incomplete | None = ...,
        pivot: Incomplete | None = ...,
        table: Incomplete | None = ...,
        count: Incomplete | None = ...,
        tableStyleElement=...,
    ) -> None: ...

class TableStyleList(Serialisable):
    tagname: str
    defaultTableStyle: Incomplete
    defaultPivotStyle: Incomplete
    tableStyle: Incomplete
    __elements__: Incomplete
    __attrs__: Incomplete
    def __init__(
        self, count: Incomplete | None = ..., defaultTableStyle: str = ..., defaultPivotStyle: str = ..., tableStyle=...
    ) -> None: ...
    @property
    def count(self): ...
