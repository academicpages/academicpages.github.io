from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

class ControlProperty(Serialisable):
    tagname: str
    anchor: Incomplete
    locked: Incomplete
    defaultSize: Incomplete
    disabled: Incomplete
    recalcAlways: Incomplete
    uiObject: Incomplete
    autoFill: Incomplete
    autoLine: Incomplete
    autoPict: Incomplete
    macro: Incomplete
    altText: Incomplete
    linkedCell: Incomplete
    listFillRange: Incomplete
    cf: Incomplete
    id: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        anchor: Incomplete | None = ...,
        locked: bool = ...,
        defaultSize: bool = ...,
        _print: bool = ...,
        disabled: bool = ...,
        recalcAlways: bool = ...,
        uiObject: bool = ...,
        autoFill: bool = ...,
        autoLine: bool = ...,
        autoPict: bool = ...,
        macro: Incomplete | None = ...,
        altText: Incomplete | None = ...,
        linkedCell: Incomplete | None = ...,
        listFillRange: Incomplete | None = ...,
        cf: str = ...,
        id: Incomplete | None = ...,
    ) -> None: ...

class Control(Serialisable):
    tagname: str
    controlPr: Incomplete
    shapeId: Incomplete
    name: Incomplete
    __elements__: Incomplete
    def __init__(
        self, controlPr: Incomplete | None = ..., shapeId: Incomplete | None = ..., name: Incomplete | None = ...
    ) -> None: ...

class Controls(Serialisable):
    tagname: str
    control: Incomplete
    __elements__: Incomplete
    def __init__(self, control=...) -> None: ...
