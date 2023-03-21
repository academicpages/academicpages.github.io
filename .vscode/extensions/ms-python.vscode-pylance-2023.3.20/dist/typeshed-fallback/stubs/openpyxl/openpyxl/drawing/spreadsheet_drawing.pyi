from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

class AnchorClientData(Serialisable):
    fLocksWithSheet: Incomplete
    fPrintsWithSheet: Incomplete
    def __init__(self, fLocksWithSheet: Incomplete | None = ..., fPrintsWithSheet: Incomplete | None = ...) -> None: ...

class AnchorMarker(Serialisable):
    tagname: str
    col: Incomplete
    colOff: Incomplete
    row: Incomplete
    rowOff: Incomplete
    def __init__(self, col: int = ..., colOff: int = ..., row: int = ..., rowOff: int = ...) -> None: ...

class _AnchorBase(Serialisable):
    sp: Incomplete
    shape: Incomplete
    grpSp: Incomplete
    groupShape: Incomplete
    graphicFrame: Incomplete
    cxnSp: Incomplete
    connectionShape: Incomplete
    pic: Incomplete
    contentPart: Incomplete
    clientData: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        clientData: Incomplete | None = ...,
        sp: Incomplete | None = ...,
        grpSp: Incomplete | None = ...,
        graphicFrame: Incomplete | None = ...,
        cxnSp: Incomplete | None = ...,
        pic: Incomplete | None = ...,
        contentPart: Incomplete | None = ...,
    ) -> None: ...

class AbsoluteAnchor(_AnchorBase):
    tagname: str
    pos: Incomplete
    ext: Incomplete
    sp: Incomplete
    grpSp: Incomplete
    graphicFrame: Incomplete
    cxnSp: Incomplete
    pic: Incomplete
    contentPart: Incomplete
    clientData: Incomplete
    __elements__: Incomplete
    def __init__(self, pos: Incomplete | None = ..., ext: Incomplete | None = ..., **kw) -> None: ...

class OneCellAnchor(_AnchorBase):
    tagname: str
    ext: Incomplete
    sp: Incomplete
    grpSp: Incomplete
    graphicFrame: Incomplete
    cxnSp: Incomplete
    pic: Incomplete
    contentPart: Incomplete
    clientData: Incomplete
    __elements__: Incomplete
    def __init__(self, _from: Incomplete | None = ..., ext: Incomplete | None = ..., **kw) -> None: ...

class TwoCellAnchor(_AnchorBase):
    tagname: str
    editAs: Incomplete
    to: Incomplete
    sp: Incomplete
    grpSp: Incomplete
    graphicFrame: Incomplete
    cxnSp: Incomplete
    pic: Incomplete
    contentPart: Incomplete
    clientData: Incomplete
    __elements__: Incomplete
    def __init__(
        self, editAs: Incomplete | None = ..., _from: Incomplete | None = ..., to: Incomplete | None = ..., **kw
    ) -> None: ...

class SpreadsheetDrawing(Serialisable):
    tagname: str
    mime_type: str
    PartName: str
    twoCellAnchor: Incomplete
    oneCellAnchor: Incomplete
    absoluteAnchor: Incomplete
    __elements__: Incomplete
    charts: Incomplete
    images: Incomplete
    def __init__(self, twoCellAnchor=..., oneCellAnchor=..., absoluteAnchor=...) -> None: ...
    def __hash__(self) -> int: ...
    def __bool__(self) -> bool: ...
    @property
    def path(self): ...
