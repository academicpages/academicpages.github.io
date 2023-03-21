from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

class PatternFillProperties(Serialisable):
    tagname: str
    namespace: Incomplete
    prst: Incomplete
    preset: Incomplete
    fgClr: Incomplete
    foreground: Incomplete
    bgClr: Incomplete
    background: Incomplete
    __elements__: Incomplete
    def __init__(self, prst: Incomplete | None = ..., fgClr: Incomplete | None = ..., bgClr: Incomplete | None = ...) -> None: ...

class RelativeRect(Serialisable):
    tagname: str
    namespace: Incomplete
    l: Incomplete
    left: Incomplete
    t: Incomplete
    top: Incomplete
    r: Incomplete
    right: Incomplete
    b: Incomplete
    bottom: Incomplete
    def __init__(
        self, l: Incomplete | None = ..., t: Incomplete | None = ..., r: Incomplete | None = ..., b: Incomplete | None = ...
    ) -> None: ...

class StretchInfoProperties(Serialisable):
    tagname: str
    namespace: Incomplete
    fillRect: Incomplete
    def __init__(self, fillRect=...) -> None: ...

class GradientStop(Serialisable):
    tagname: str
    namespace: Incomplete
    pos: Incomplete
    scrgbClr: Incomplete
    RGBPercent: Incomplete
    srgbClr: Incomplete
    RGB: Incomplete
    hslClr: Incomplete
    sysClr: Incomplete
    schemeClr: Incomplete
    prstClr: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        pos: Incomplete | None = ...,
        scrgbClr: Incomplete | None = ...,
        srgbClr: Incomplete | None = ...,
        hslClr: Incomplete | None = ...,
        sysClr: Incomplete | None = ...,
        schemeClr: Incomplete | None = ...,
        prstClr: Incomplete | None = ...,
    ) -> None: ...

class LinearShadeProperties(Serialisable):
    tagname: str
    namespace: Incomplete
    ang: Incomplete
    scaled: Incomplete
    def __init__(self, ang: Incomplete | None = ..., scaled: Incomplete | None = ...) -> None: ...

class PathShadeProperties(Serialisable):
    tagname: str
    namespace: Incomplete
    path: Incomplete
    fillToRect: Incomplete
    def __init__(self, path: Incomplete | None = ..., fillToRect: Incomplete | None = ...) -> None: ...

class GradientFillProperties(Serialisable):
    tagname: str
    namespace: Incomplete
    flip: Incomplete
    rotWithShape: Incomplete
    gsLst: Incomplete
    stop_list: Incomplete
    lin: Incomplete
    linear: Incomplete
    path: Incomplete
    tileRect: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        flip: Incomplete | None = ...,
        rotWithShape: Incomplete | None = ...,
        gsLst=...,
        lin: Incomplete | None = ...,
        path: Incomplete | None = ...,
        tileRect: Incomplete | None = ...,
    ) -> None: ...

class SolidColorFillProperties(Serialisable):
    tagname: str
    scrgbClr: Incomplete
    RGBPercent: Incomplete
    srgbClr: Incomplete
    RGB: Incomplete
    hslClr: Incomplete
    sysClr: Incomplete
    schemeClr: Incomplete
    prstClr: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        scrgbClr: Incomplete | None = ...,
        srgbClr: Incomplete | None = ...,
        hslClr: Incomplete | None = ...,
        sysClr: Incomplete | None = ...,
        schemeClr: Incomplete | None = ...,
        prstClr: Incomplete | None = ...,
    ) -> None: ...

class Blip(Serialisable):
    tagname: str
    namespace: Incomplete
    cstate: Incomplete
    embed: Incomplete
    link: Incomplete
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
    alphaBiLevel: Incomplete
    alphaCeiling: Incomplete
    alphaFloor: Incomplete
    alphaInv: Incomplete
    alphaMod: Incomplete
    alphaModFix: Incomplete
    alphaRepl: Incomplete
    biLevel: Incomplete
    blur: Incomplete
    clrChange: Incomplete
    clrRepl: Incomplete
    duotone: Incomplete
    fillOverlay: Incomplete
    grayscl: Incomplete
    hsl: Incomplete
    lum: Incomplete
    tint: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        cstate: Incomplete | None = ...,
        embed: Incomplete | None = ...,
        link: Incomplete | None = ...,
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
        alphaBiLevel: Incomplete | None = ...,
        alphaCeiling: Incomplete | None = ...,
        alphaFloor: Incomplete | None = ...,
        alphaInv: Incomplete | None = ...,
        alphaMod: Incomplete | None = ...,
        alphaModFix: Incomplete | None = ...,
        alphaRepl: Incomplete | None = ...,
        biLevel: Incomplete | None = ...,
        blur: Incomplete | None = ...,
        clrChange: Incomplete | None = ...,
        clrRepl: Incomplete | None = ...,
        duotone: Incomplete | None = ...,
        fillOverlay: Incomplete | None = ...,
        grayscl: Incomplete | None = ...,
        hsl: Incomplete | None = ...,
        lum: Incomplete | None = ...,
        tint: Incomplete | None = ...,
    ) -> None: ...

class TileInfoProperties(Serialisable):
    tx: Incomplete
    ty: Incomplete
    sx: Incomplete
    sy: Incomplete
    flip: Incomplete
    algn: Incomplete
    def __init__(
        self,
        tx: Incomplete | None = ...,
        ty: Incomplete | None = ...,
        sx: Incomplete | None = ...,
        sy: Incomplete | None = ...,
        flip: Incomplete | None = ...,
        algn: Incomplete | None = ...,
    ) -> None: ...

class BlipFillProperties(Serialisable):
    tagname: str
    dpi: Incomplete
    rotWithShape: Incomplete
    blip: Incomplete
    srcRect: Incomplete
    tile: Incomplete
    stretch: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        dpi: Incomplete | None = ...,
        rotWithShape: Incomplete | None = ...,
        blip: Incomplete | None = ...,
        tile: Incomplete | None = ...,
        stretch=...,
        srcRect: Incomplete | None = ...,
    ) -> None: ...
