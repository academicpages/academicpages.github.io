from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

class PictureLocking(Serialisable):
    tagname: str
    namespace: Incomplete
    noCrop: Incomplete
    noGrp: Incomplete
    noSelect: Incomplete
    noRot: Incomplete
    noChangeAspect: Incomplete
    noMove: Incomplete
    noResize: Incomplete
    noEditPoints: Incomplete
    noAdjustHandles: Incomplete
    noChangeArrowheads: Incomplete
    noChangeShapeType: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        noCrop: Incomplete | None = ...,
        noGrp: Incomplete | None = ...,
        noSelect: Incomplete | None = ...,
        noRot: Incomplete | None = ...,
        noChangeAspect: Incomplete | None = ...,
        noMove: Incomplete | None = ...,
        noResize: Incomplete | None = ...,
        noEditPoints: Incomplete | None = ...,
        noAdjustHandles: Incomplete | None = ...,
        noChangeArrowheads: Incomplete | None = ...,
        noChangeShapeType: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
    ) -> None: ...

class NonVisualPictureProperties(Serialisable):
    tagname: str
    preferRelativeResize: Incomplete
    picLocks: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(
        self, preferRelativeResize: Incomplete | None = ..., picLocks: Incomplete | None = ..., extLst: Incomplete | None = ...
    ) -> None: ...

class PictureNonVisual(Serialisable):
    tagname: str
    cNvPr: Incomplete
    cNvPicPr: Incomplete
    __elements__: Incomplete
    def __init__(self, cNvPr: Incomplete | None = ..., cNvPicPr: Incomplete | None = ...) -> None: ...

class PictureFrame(Serialisable):
    tagname: str
    macro: Incomplete
    fPublished: Incomplete
    nvPicPr: Incomplete
    blipFill: Incomplete
    spPr: Incomplete
    graphicalProperties: Incomplete
    style: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        macro: Incomplete | None = ...,
        fPublished: Incomplete | None = ...,
        nvPicPr: Incomplete | None = ...,
        blipFill: Incomplete | None = ...,
        spPr: Incomplete | None = ...,
        style: Incomplete | None = ...,
    ) -> None: ...
