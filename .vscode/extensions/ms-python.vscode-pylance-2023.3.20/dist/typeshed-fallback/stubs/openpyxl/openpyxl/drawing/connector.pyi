from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

class Connection(Serialisable):
    id: Incomplete
    idx: Incomplete
    def __init__(self, id: Incomplete | None = ..., idx: Incomplete | None = ...) -> None: ...

class ConnectorLocking(Serialisable):
    extLst: Incomplete
    def __init__(self, extLst: Incomplete | None = ...) -> None: ...

class NonVisualConnectorProperties(Serialisable):
    cxnSpLocks: Incomplete
    stCxn: Incomplete
    endCxn: Incomplete
    extLst: Incomplete
    def __init__(
        self,
        cxnSpLocks: Incomplete | None = ...,
        stCxn: Incomplete | None = ...,
        endCxn: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
    ) -> None: ...

class ConnectorNonVisual(Serialisable):
    cNvPr: Incomplete
    cNvCxnSpPr: Incomplete
    __elements__: Incomplete
    def __init__(self, cNvPr: Incomplete | None = ..., cNvCxnSpPr: Incomplete | None = ...) -> None: ...

class ConnectorShape(Serialisable):
    tagname: str
    nvCxnSpPr: Incomplete
    spPr: Incomplete
    style: Incomplete
    macro: Incomplete
    fPublished: Incomplete
    def __init__(
        self,
        nvCxnSpPr: Incomplete | None = ...,
        spPr: Incomplete | None = ...,
        style: Incomplete | None = ...,
        macro: Incomplete | None = ...,
        fPublished: Incomplete | None = ...,
    ) -> None: ...

class ShapeMeta(Serialisable):
    tagname: str
    cNvPr: Incomplete
    cNvSpPr: Incomplete
    def __init__(self, cNvPr: Incomplete | None = ..., cNvSpPr: Incomplete | None = ...) -> None: ...

class Shape(Serialisable):
    macro: Incomplete
    textlink: Incomplete
    fPublished: Incomplete
    fLocksText: Incomplete
    nvSpPr: Incomplete
    meta: Incomplete
    spPr: Incomplete
    graphicalProperties: Incomplete
    style: Incomplete
    txBody: Incomplete
    def __init__(
        self,
        macro: Incomplete | None = ...,
        textlink: Incomplete | None = ...,
        fPublished: Incomplete | None = ...,
        fLocksText: Incomplete | None = ...,
        nvSpPr: Incomplete | None = ...,
        spPr: Incomplete | None = ...,
        style: Incomplete | None = ...,
        txBody: Incomplete | None = ...,
    ) -> None: ...
