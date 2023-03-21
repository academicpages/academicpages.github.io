from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

from .colors import ColorChoice

class TintEffect(Serialisable):
    tagname: str
    hue: Incomplete
    amt: Incomplete
    def __init__(self, hue: int = ..., amt: int = ...) -> None: ...

class LuminanceEffect(Serialisable):
    tagname: str
    bright: Incomplete
    contrast: Incomplete
    def __init__(self, bright: int = ..., contrast: int = ...) -> None: ...

class HSLEffect(Serialisable):
    hue: Incomplete
    sat: Incomplete
    lum: Incomplete
    def __init__(self, hue: Incomplete | None = ..., sat: Incomplete | None = ..., lum: Incomplete | None = ...) -> None: ...

class GrayscaleEffect(Serialisable):
    tagname: str

class FillOverlayEffect(Serialisable):
    blend: Incomplete
    def __init__(self, blend: Incomplete | None = ...) -> None: ...

class DuotoneEffect(Serialisable): ...
class ColorReplaceEffect(Serialisable): ...
class Color(Serialisable): ...

class ColorChangeEffect(Serialisable):
    useA: Incomplete
    clrFrom: Incomplete
    clrTo: Incomplete
    def __init__(
        self, useA: Incomplete | None = ..., clrFrom: Incomplete | None = ..., clrTo: Incomplete | None = ...
    ) -> None: ...

class BlurEffect(Serialisable):
    rad: Incomplete
    grow: Incomplete
    def __init__(self, rad: Incomplete | None = ..., grow: Incomplete | None = ...) -> None: ...

class BiLevelEffect(Serialisable):
    thresh: Incomplete
    def __init__(self, thresh: Incomplete | None = ...) -> None: ...

class AlphaReplaceEffect(Serialisable):
    a: Incomplete
    def __init__(self, a: Incomplete | None = ...) -> None: ...

class AlphaModulateFixedEffect(Serialisable):
    amt: Incomplete
    def __init__(self, amt: Incomplete | None = ...) -> None: ...

class EffectContainer(Serialisable):
    type: Incomplete
    name: Incomplete
    def __init__(self, type: Incomplete | None = ..., name: Incomplete | None = ...) -> None: ...

class AlphaModulateEffect(Serialisable):
    cont: Incomplete
    def __init__(self, cont: Incomplete | None = ...) -> None: ...

class AlphaInverseEffect(Serialisable): ...
class AlphaFloorEffect(Serialisable): ...
class AlphaCeilingEffect(Serialisable): ...

class AlphaBiLevelEffect(Serialisable):
    thresh: Incomplete
    def __init__(self, thresh: Incomplete | None = ...) -> None: ...

class GlowEffect(ColorChoice):
    rad: Incomplete
    scrgbClr: Incomplete
    srgbClr: Incomplete
    hslClr: Incomplete
    sysClr: Incomplete
    schemeClr: Incomplete
    prstClr: Incomplete
    __elements__: Incomplete
    def __init__(self, rad: Incomplete | None = ..., **kw) -> None: ...

class InnerShadowEffect(ColorChoice):
    blurRad: Incomplete
    dist: Incomplete
    dir: Incomplete
    scrgbClr: Incomplete
    srgbClr: Incomplete
    hslClr: Incomplete
    sysClr: Incomplete
    schemeClr: Incomplete
    prstClr: Incomplete
    __elements__: Incomplete
    def __init__(
        self, blurRad: Incomplete | None = ..., dist: Incomplete | None = ..., dir: Incomplete | None = ..., **kw
    ) -> None: ...

class OuterShadow(ColorChoice):
    tagname: str
    blurRad: Incomplete
    dist: Incomplete
    dir: Incomplete
    sx: Incomplete
    sy: Incomplete
    kx: Incomplete
    ky: Incomplete
    algn: Incomplete
    rotWithShape: Incomplete
    scrgbClr: Incomplete
    srgbClr: Incomplete
    hslClr: Incomplete
    sysClr: Incomplete
    schemeClr: Incomplete
    prstClr: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        blurRad: Incomplete | None = ...,
        dist: Incomplete | None = ...,
        dir: Incomplete | None = ...,
        sx: Incomplete | None = ...,
        sy: Incomplete | None = ...,
        kx: Incomplete | None = ...,
        ky: Incomplete | None = ...,
        algn: Incomplete | None = ...,
        rotWithShape: Incomplete | None = ...,
        **kw,
    ) -> None: ...

class PresetShadowEffect(ColorChoice):
    prst: Incomplete
    dist: Incomplete
    dir: Incomplete
    scrgbClr: Incomplete
    srgbClr: Incomplete
    hslClr: Incomplete
    sysClr: Incomplete
    schemeClr: Incomplete
    prstClr: Incomplete
    __elements__: Incomplete
    def __init__(
        self, prst: Incomplete | None = ..., dist: Incomplete | None = ..., dir: Incomplete | None = ..., **kw
    ) -> None: ...

class ReflectionEffect(Serialisable):
    blurRad: Incomplete
    stA: Incomplete
    stPos: Incomplete
    endA: Incomplete
    endPos: Incomplete
    dist: Incomplete
    dir: Incomplete
    fadeDir: Incomplete
    sx: Incomplete
    sy: Incomplete
    kx: Incomplete
    ky: Incomplete
    algn: Incomplete
    rotWithShape: Incomplete
    def __init__(
        self,
        blurRad: Incomplete | None = ...,
        stA: Incomplete | None = ...,
        stPos: Incomplete | None = ...,
        endA: Incomplete | None = ...,
        endPos: Incomplete | None = ...,
        dist: Incomplete | None = ...,
        dir: Incomplete | None = ...,
        fadeDir: Incomplete | None = ...,
        sx: Incomplete | None = ...,
        sy: Incomplete | None = ...,
        kx: Incomplete | None = ...,
        ky: Incomplete | None = ...,
        algn: Incomplete | None = ...,
        rotWithShape: Incomplete | None = ...,
    ) -> None: ...

class SoftEdgesEffect(Serialisable):
    rad: Incomplete
    def __init__(self, rad: Incomplete | None = ...) -> None: ...

class EffectList(Serialisable):
    blur: Incomplete
    fillOverlay: Incomplete
    glow: Incomplete
    innerShdw: Incomplete
    outerShdw: Incomplete
    prstShdw: Incomplete
    reflection: Incomplete
    softEdge: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        blur: Incomplete | None = ...,
        fillOverlay: Incomplete | None = ...,
        glow: Incomplete | None = ...,
        innerShdw: Incomplete | None = ...,
        outerShdw: Incomplete | None = ...,
        prstShdw: Incomplete | None = ...,
        reflection: Incomplete | None = ...,
        softEdge: Incomplete | None = ...,
    ) -> None: ...
