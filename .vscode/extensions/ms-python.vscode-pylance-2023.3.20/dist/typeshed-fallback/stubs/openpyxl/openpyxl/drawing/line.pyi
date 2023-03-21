from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

class LineEndProperties(Serialisable):
    tagname: str
    namespace: Incomplete
    type: Incomplete
    w: Incomplete
    len: Incomplete
    def __init__(self, type: Incomplete | None = ..., w: Incomplete | None = ..., len: Incomplete | None = ...) -> None: ...

class DashStop(Serialisable):
    tagname: str
    namespace: Incomplete
    d: Incomplete
    length: Incomplete
    sp: Incomplete
    space: Incomplete
    def __init__(self, d: int = ..., sp: int = ...) -> None: ...

class DashStopList(Serialisable):
    ds: Incomplete
    def __init__(self, ds: Incomplete | None = ...) -> None: ...

class LineProperties(Serialisable):
    tagname: str
    namespace: Incomplete
    w: Incomplete
    width: Incomplete
    cap: Incomplete
    cmpd: Incomplete
    algn: Incomplete
    noFill: Incomplete
    solidFill: Incomplete
    gradFill: Incomplete
    pattFill: Incomplete
    prstDash: Incomplete
    dashStyle: Incomplete
    custDash: Incomplete
    round: Incomplete
    bevel: Incomplete
    miter: Incomplete
    headEnd: Incomplete
    tailEnd: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        w: Incomplete | None = ...,
        cap: Incomplete | None = ...,
        cmpd: Incomplete | None = ...,
        algn: Incomplete | None = ...,
        noFill: Incomplete | None = ...,
        solidFill: Incomplete | None = ...,
        gradFill: Incomplete | None = ...,
        pattFill: Incomplete | None = ...,
        prstDash: Incomplete | None = ...,
        custDash: Incomplete | None = ...,
        round: Incomplete | None = ...,
        bevel: Incomplete | None = ...,
        miter: Incomplete | None = ...,
        headEnd: Incomplete | None = ...,
        tailEnd: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
    ) -> None: ...
