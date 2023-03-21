from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

class GraphicFrameLocking(Serialisable):
    noGrp: Incomplete
    noDrilldown: Incomplete
    noSelect: Incomplete
    noChangeAspect: Incomplete
    noMove: Incomplete
    noResize: Incomplete
    extLst: Incomplete
    def __init__(
        self,
        noGrp: Incomplete | None = ...,
        noDrilldown: Incomplete | None = ...,
        noSelect: Incomplete | None = ...,
        noChangeAspect: Incomplete | None = ...,
        noMove: Incomplete | None = ...,
        noResize: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
    ) -> None: ...

class NonVisualGraphicFrameProperties(Serialisable):
    tagname: str
    graphicFrameLocks: Incomplete
    extLst: Incomplete
    def __init__(self, graphicFrameLocks: Incomplete | None = ..., extLst: Incomplete | None = ...) -> None: ...

class NonVisualGraphicFrame(Serialisable):
    tagname: str
    cNvPr: Incomplete
    cNvGraphicFramePr: Incomplete
    __elements__: Incomplete
    def __init__(self, cNvPr: Incomplete | None = ..., cNvGraphicFramePr: Incomplete | None = ...) -> None: ...

class GraphicData(Serialisable):
    tagname: str
    namespace: Incomplete
    uri: Incomplete
    chart: Incomplete
    def __init__(self, uri=..., chart: Incomplete | None = ...) -> None: ...

class GraphicObject(Serialisable):
    tagname: str
    namespace: Incomplete
    graphicData: Incomplete
    def __init__(self, graphicData: Incomplete | None = ...) -> None: ...

class GraphicFrame(Serialisable):
    tagname: str
    nvGraphicFramePr: Incomplete
    xfrm: Incomplete
    graphic: Incomplete
    macro: Incomplete
    fPublished: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        nvGraphicFramePr: Incomplete | None = ...,
        xfrm: Incomplete | None = ...,
        graphic: Incomplete | None = ...,
        macro: Incomplete | None = ...,
        fPublished: Incomplete | None = ...,
    ) -> None: ...

class GroupShape(Serialisable):
    nvGrpSpPr: Incomplete
    nonVisualProperties: Incomplete
    grpSpPr: Incomplete
    visualProperties: Incomplete
    pic: Incomplete
    __elements__: Incomplete
    def __init__(
        self, nvGrpSpPr: Incomplete | None = ..., grpSpPr: Incomplete | None = ..., pic: Incomplete | None = ...
    ) -> None: ...
