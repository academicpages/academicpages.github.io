from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

class GroupShapeProperties(Serialisable):
    tagname: str
    bwMode: Incomplete
    xfrm: Incomplete
    scene3d: Incomplete
    extLst: Incomplete
    def __init__(
        self,
        bwMode: Incomplete | None = ...,
        xfrm: Incomplete | None = ...,
        scene3d: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
    ) -> None: ...

class GroupLocking(Serialisable):
    tagname: str
    namespace: Incomplete
    noGrp: Incomplete
    noUngrp: Incomplete
    noSelect: Incomplete
    noRot: Incomplete
    noChangeAspect: Incomplete
    noMove: Incomplete
    noResize: Incomplete
    noChangeArrowheads: Incomplete
    noEditPoints: Incomplete
    noAdjustHandles: Incomplete
    noChangeShapeType: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        noGrp: Incomplete | None = ...,
        noUngrp: Incomplete | None = ...,
        noSelect: Incomplete | None = ...,
        noRot: Incomplete | None = ...,
        noChangeAspect: Incomplete | None = ...,
        noChangeArrowheads: Incomplete | None = ...,
        noMove: Incomplete | None = ...,
        noResize: Incomplete | None = ...,
        noEditPoints: Incomplete | None = ...,
        noAdjustHandles: Incomplete | None = ...,
        noChangeShapeType: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
    ) -> None: ...

class NonVisualGroupDrawingShapeProps(Serialisable):
    tagname: str
    grpSpLocks: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(self, grpSpLocks: Incomplete | None = ..., extLst: Incomplete | None = ...) -> None: ...

class NonVisualDrawingShapeProps(Serialisable):
    tagname: str
    spLocks: Incomplete
    txBax: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    txBox: Incomplete
    def __init__(
        self, spLocks: Incomplete | None = ..., txBox: Incomplete | None = ..., extLst: Incomplete | None = ...
    ) -> None: ...

class NonVisualDrawingProps(Serialisable):
    tagname: str
    id: Incomplete
    name: Incomplete
    descr: Incomplete
    hidden: Incomplete
    title: Incomplete
    hlinkClick: Incomplete
    hlinkHover: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        id: Incomplete | None = ...,
        name: Incomplete | None = ...,
        descr: Incomplete | None = ...,
        hidden: Incomplete | None = ...,
        title: Incomplete | None = ...,
        hlinkClick: Incomplete | None = ...,
        hlinkHover: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
    ) -> None: ...

class NonVisualGroupShape(Serialisable):
    tagname: str
    cNvPr: Incomplete
    cNvGrpSpPr: Incomplete
    __elements__: Incomplete
    def __init__(self, cNvPr: Incomplete | None = ..., cNvGrpSpPr: Incomplete | None = ...) -> None: ...
