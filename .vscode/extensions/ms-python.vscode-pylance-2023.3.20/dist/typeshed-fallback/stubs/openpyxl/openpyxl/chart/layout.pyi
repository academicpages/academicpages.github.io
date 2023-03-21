from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

class ManualLayout(Serialisable):
    tagname: str
    layoutTarget: Incomplete
    xMode: Incomplete
    yMode: Incomplete
    wMode: Incomplete
    hMode: Incomplete
    x: Incomplete
    y: Incomplete
    w: Incomplete
    width: Incomplete
    h: Incomplete
    height: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        layoutTarget: Incomplete | None = ...,
        xMode: Incomplete | None = ...,
        yMode: Incomplete | None = ...,
        wMode: str = ...,
        hMode: str = ...,
        x: Incomplete | None = ...,
        y: Incomplete | None = ...,
        w: Incomplete | None = ...,
        h: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
    ) -> None: ...

class Layout(Serialisable):
    tagname: str
    manualLayout: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(self, manualLayout: Incomplete | None = ..., extLst: Incomplete | None = ...) -> None: ...
