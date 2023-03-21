from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

class ObjectAnchor(Serialisable):
    tagname: str
    to: Incomplete
    moveWithCells: Incomplete
    sizeWithCells: Incomplete
    z_order: Incomplete
    def __init__(
        self,
        _from: Incomplete | None = ...,
        to: Incomplete | None = ...,
        moveWithCells: bool = ...,
        sizeWithCells: bool = ...,
        z_order: Incomplete | None = ...,
    ) -> None: ...

class ObjectPr(Serialisable):
    tagname: str
    anchor: Incomplete
    locked: Incomplete
    defaultSize: Incomplete
    disabled: Incomplete
    uiObject: Incomplete
    autoFill: Incomplete
    autoLine: Incomplete
    autoPict: Incomplete
    macro: Incomplete
    altText: Incomplete
    dde: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        anchor: Incomplete | None = ...,
        locked: bool = ...,
        defaultSize: bool = ...,
        _print: bool = ...,
        disabled: bool = ...,
        uiObject: bool = ...,
        autoFill: bool = ...,
        autoLine: bool = ...,
        autoPict: bool = ...,
        macro: Incomplete | None = ...,
        altText: Incomplete | None = ...,
        dde: bool = ...,
    ) -> None: ...

class OleObject(Serialisable):
    tagname: str
    objectPr: Incomplete
    progId: Incomplete
    dvAspect: Incomplete
    link: Incomplete
    oleUpdate: Incomplete
    autoLoad: Incomplete
    shapeId: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        objectPr: Incomplete | None = ...,
        progId: Incomplete | None = ...,
        dvAspect: str = ...,
        link: Incomplete | None = ...,
        oleUpdate: Incomplete | None = ...,
        autoLoad: bool = ...,
        shapeId: Incomplete | None = ...,
    ) -> None: ...

class OleObjects(Serialisable):
    tagname: str
    oleObject: Incomplete
    __elements__: Incomplete
    def __init__(self, oleObject=...) -> None: ...
