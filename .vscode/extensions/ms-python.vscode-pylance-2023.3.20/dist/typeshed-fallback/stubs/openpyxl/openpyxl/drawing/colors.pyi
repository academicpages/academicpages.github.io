from _typeshed import Incomplete

from openpyxl.descriptors import Typed
from openpyxl.descriptors.serialisable import Serialisable

PRESET_COLORS: Incomplete
SCHEME_COLORS: Incomplete

class Transform(Serialisable): ...

class SystemColor(Serialisable):
    tagname: str
    namespace: Incomplete
    tint: Incomplete
    shade: Incomplete
    comp: Incomplete
    inv: Incomplete
    gray: Incomplete
    alpha: Incomplete
    alphaOff: Incomplete
    alphaMod: Incomplete
    hue: Incomplete
    hueOff: Incomplete
    hueMod: Incomplete
    sat: Incomplete
    satOff: Incomplete
    satMod: Incomplete
    lum: Incomplete
    lumOff: Incomplete
    lumMod: Incomplete
    red: Incomplete
    redOff: Incomplete
    redMod: Incomplete
    green: Incomplete
    greenOff: Incomplete
    greenMod: Incomplete
    blue: Incomplete
    blueOff: Incomplete
    blueMod: Incomplete
    gamma: Incomplete
    invGamma: Incomplete
    val: Incomplete
    lastClr: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        val: str = ...,
        lastClr: Incomplete | None = ...,
        tint: Incomplete | None = ...,
        shade: Incomplete | None = ...,
        comp: Incomplete | None = ...,
        inv: Incomplete | None = ...,
        gray: Incomplete | None = ...,
        alpha: Incomplete | None = ...,
        alphaOff: Incomplete | None = ...,
        alphaMod: Incomplete | None = ...,
        hue: Incomplete | None = ...,
        hueOff: Incomplete | None = ...,
        hueMod: Incomplete | None = ...,
        sat: Incomplete | None = ...,
        satOff: Incomplete | None = ...,
        satMod: Incomplete | None = ...,
        lum: Incomplete | None = ...,
        lumOff: Incomplete | None = ...,
        lumMod: Incomplete | None = ...,
        red: Incomplete | None = ...,
        redOff: Incomplete | None = ...,
        redMod: Incomplete | None = ...,
        green: Incomplete | None = ...,
        greenOff: Incomplete | None = ...,
        greenMod: Incomplete | None = ...,
        blue: Incomplete | None = ...,
        blueOff: Incomplete | None = ...,
        blueMod: Incomplete | None = ...,
        gamma: Incomplete | None = ...,
        invGamma: Incomplete | None = ...,
    ) -> None: ...

class HSLColor(Serialisable):
    tagname: str
    hue: Incomplete
    sat: Incomplete
    lum: Incomplete
    def __init__(self, hue: Incomplete | None = ..., sat: Incomplete | None = ..., lum: Incomplete | None = ...) -> None: ...

class RGBPercent(Serialisable):
    tagname: str
    r: Incomplete
    g: Incomplete
    b: Incomplete
    def __init__(self, r: Incomplete | None = ..., g: Incomplete | None = ..., b: Incomplete | None = ...) -> None: ...

class SchemeColor(Serialisable):
    tagname: str
    namespace: Incomplete
    tint: Incomplete
    shade: Incomplete
    comp: Incomplete
    inv: Incomplete
    gray: Incomplete
    alpha: Incomplete
    alphaOff: Incomplete
    alphaMod: Incomplete
    hue: Incomplete
    hueOff: Incomplete
    hueMod: Incomplete
    sat: Incomplete
    satOff: Incomplete
    satMod: Incomplete
    lum: Incomplete
    lumOff: Incomplete
    lumMod: Incomplete
    red: Incomplete
    redOff: Incomplete
    redMod: Incomplete
    green: Incomplete
    greenOff: Incomplete
    greenMod: Incomplete
    blue: Incomplete
    blueOff: Incomplete
    blueMod: Incomplete
    gamma: Incomplete
    invGamma: Incomplete
    val: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        tint: Incomplete | None = ...,
        shade: Incomplete | None = ...,
        comp: Incomplete | None = ...,
        inv: Incomplete | None = ...,
        gray: Incomplete | None = ...,
        alpha: Incomplete | None = ...,
        alphaOff: Incomplete | None = ...,
        alphaMod: Incomplete | None = ...,
        hue: Incomplete | None = ...,
        hueOff: Incomplete | None = ...,
        hueMod: Incomplete | None = ...,
        sat: Incomplete | None = ...,
        satOff: Incomplete | None = ...,
        satMod: Incomplete | None = ...,
        lum: Incomplete | None = ...,
        lumOff: Incomplete | None = ...,
        lumMod: Incomplete | None = ...,
        red: Incomplete | None = ...,
        redOff: Incomplete | None = ...,
        redMod: Incomplete | None = ...,
        green: Incomplete | None = ...,
        greenOff: Incomplete | None = ...,
        greenMod: Incomplete | None = ...,
        blue: Incomplete | None = ...,
        blueOff: Incomplete | None = ...,
        blueMod: Incomplete | None = ...,
        gamma: Incomplete | None = ...,
        invGamma: Incomplete | None = ...,
        val: Incomplete | None = ...,
    ) -> None: ...

class ColorChoice(Serialisable):
    tagname: str
    namespace: Incomplete
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

class ColorMapping(Serialisable):
    tagname: str
    bg1: Incomplete
    tx1: Incomplete
    bg2: Incomplete
    tx2: Incomplete
    accent1: Incomplete
    accent2: Incomplete
    accent3: Incomplete
    accent4: Incomplete
    accent5: Incomplete
    accent6: Incomplete
    hlink: Incomplete
    folHlink: Incomplete
    extLst: Incomplete
    def __init__(
        self,
        bg1: str = ...,
        tx1: str = ...,
        bg2: str = ...,
        tx2: str = ...,
        accent1: str = ...,
        accent2: str = ...,
        accent3: str = ...,
        accent4: str = ...,
        accent5: str = ...,
        accent6: str = ...,
        hlink: str = ...,
        folHlink: str = ...,
        extLst: Incomplete | None = ...,
    ) -> None: ...

class ColorChoiceDescriptor(Typed):
    expected_type: Incomplete
    allow_none: bool
    def __set__(self, instance, value) -> None: ...
