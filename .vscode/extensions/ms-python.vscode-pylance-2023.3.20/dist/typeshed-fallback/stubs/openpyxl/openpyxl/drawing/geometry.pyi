from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

class Point2D(Serialisable):
    tagname: str
    namespace: Incomplete
    x: Incomplete
    y: Incomplete
    def __init__(self, x: Incomplete | None = ..., y: Incomplete | None = ...) -> None: ...

class PositiveSize2D(Serialisable):
    tagname: str
    namespace: Incomplete
    cx: Incomplete
    width: Incomplete
    cy: Incomplete
    height: Incomplete
    def __init__(self, cx: Incomplete | None = ..., cy: Incomplete | None = ...) -> None: ...

class Transform2D(Serialisable):
    tagname: str
    namespace: Incomplete
    rot: Incomplete
    flipH: Incomplete
    flipV: Incomplete
    off: Incomplete
    ext: Incomplete
    chOff: Incomplete
    chExt: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        rot: Incomplete | None = ...,
        flipH: Incomplete | None = ...,
        flipV: Incomplete | None = ...,
        off: Incomplete | None = ...,
        ext: Incomplete | None = ...,
        chOff: Incomplete | None = ...,
        chExt: Incomplete | None = ...,
    ) -> None: ...

class GroupTransform2D(Serialisable):
    tagname: str
    namespace: Incomplete
    rot: Incomplete
    flipH: Incomplete
    flipV: Incomplete
    off: Incomplete
    ext: Incomplete
    chOff: Incomplete
    chExt: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        rot: int = ...,
        flipH: Incomplete | None = ...,
        flipV: Incomplete | None = ...,
        off: Incomplete | None = ...,
        ext: Incomplete | None = ...,
        chOff: Incomplete | None = ...,
        chExt: Incomplete | None = ...,
    ) -> None: ...

class SphereCoords(Serialisable):
    tagname: str
    lat: Incomplete
    lon: Incomplete
    rev: Incomplete
    def __init__(self, lat: Incomplete | None = ..., lon: Incomplete | None = ..., rev: Incomplete | None = ...) -> None: ...

class Camera(Serialisable):
    tagname: str
    prst: Incomplete
    fov: Incomplete
    zoom: Incomplete
    rot: Incomplete
    def __init__(
        self,
        prst: Incomplete | None = ...,
        fov: Incomplete | None = ...,
        zoom: Incomplete | None = ...,
        rot: Incomplete | None = ...,
    ) -> None: ...

class LightRig(Serialisable):
    tagname: str
    rig: Incomplete
    dir: Incomplete
    rot: Incomplete
    def __init__(self, rig: Incomplete | None = ..., dir: Incomplete | None = ..., rot: Incomplete | None = ...) -> None: ...

class Vector3D(Serialisable):
    tagname: str
    dx: Incomplete
    dy: Incomplete
    dz: Incomplete
    def __init__(self, dx: Incomplete | None = ..., dy: Incomplete | None = ..., dz: Incomplete | None = ...) -> None: ...

class Point3D(Serialisable):
    tagname: str
    x: Incomplete
    y: Incomplete
    z: Incomplete
    def __init__(self, x: Incomplete | None = ..., y: Incomplete | None = ..., z: Incomplete | None = ...) -> None: ...

class Backdrop(Serialisable):
    anchor: Incomplete
    norm: Incomplete
    up: Incomplete
    extLst: Incomplete
    def __init__(
        self,
        anchor: Incomplete | None = ...,
        norm: Incomplete | None = ...,
        up: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
    ) -> None: ...

class Scene3D(Serialisable):
    camera: Incomplete
    lightRig: Incomplete
    backdrop: Incomplete
    extLst: Incomplete
    def __init__(
        self,
        camera: Incomplete | None = ...,
        lightRig: Incomplete | None = ...,
        backdrop: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
    ) -> None: ...

class Bevel(Serialisable):
    tagname: str
    w: Incomplete
    h: Incomplete
    prst: Incomplete
    def __init__(self, w: Incomplete | None = ..., h: Incomplete | None = ..., prst: Incomplete | None = ...) -> None: ...

class Shape3D(Serialisable):
    namespace: Incomplete
    z: Incomplete
    extrusionH: Incomplete
    contourW: Incomplete
    prstMaterial: Incomplete
    bevelT: Incomplete
    bevelB: Incomplete
    extrusionClr: Incomplete
    contourClr: Incomplete
    extLst: Incomplete
    def __init__(
        self,
        z: Incomplete | None = ...,
        extrusionH: Incomplete | None = ...,
        contourW: Incomplete | None = ...,
        prstMaterial: Incomplete | None = ...,
        bevelT: Incomplete | None = ...,
        bevelB: Incomplete | None = ...,
        extrusionClr: Incomplete | None = ...,
        contourClr: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
    ) -> None: ...

class Path2D(Serialisable):
    w: Incomplete
    h: Incomplete
    fill: Incomplete
    stroke: Incomplete
    extrusionOk: Incomplete
    def __init__(
        self,
        w: Incomplete | None = ...,
        h: Incomplete | None = ...,
        fill: Incomplete | None = ...,
        stroke: Incomplete | None = ...,
        extrusionOk: Incomplete | None = ...,
    ) -> None: ...

class Path2DList(Serialisable):
    path: Incomplete
    def __init__(self, path: Incomplete | None = ...) -> None: ...

class GeomRect(Serialisable):
    l: Incomplete
    t: Incomplete
    r: Incomplete
    b: Incomplete
    def __init__(
        self, l: Incomplete | None = ..., t: Incomplete | None = ..., r: Incomplete | None = ..., b: Incomplete | None = ...
    ) -> None: ...

class AdjPoint2D(Serialisable):
    x: Incomplete
    y: Incomplete
    def __init__(self, x: Incomplete | None = ..., y: Incomplete | None = ...) -> None: ...

class ConnectionSite(Serialisable):
    ang: Incomplete
    pos: Incomplete
    def __init__(self, ang: Incomplete | None = ..., pos: Incomplete | None = ...) -> None: ...

class ConnectionSiteList(Serialisable):
    cxn: Incomplete
    def __init__(self, cxn: Incomplete | None = ...) -> None: ...

class AdjustHandleList(Serialisable): ...

class GeomGuide(Serialisable):
    name: Incomplete
    fmla: Incomplete
    def __init__(self, name: Incomplete | None = ..., fmla: Incomplete | None = ...) -> None: ...

class GeomGuideList(Serialisable):
    gd: Incomplete
    def __init__(self, gd: Incomplete | None = ...) -> None: ...

class CustomGeometry2D(Serialisable):
    avLst: Incomplete
    gdLst: Incomplete
    ahLst: Incomplete
    cxnLst: Incomplete
    pathLst: Incomplete
    rect: Incomplete
    def __init__(
        self,
        avLst: Incomplete | None = ...,
        gdLst: Incomplete | None = ...,
        ahLst: Incomplete | None = ...,
        cxnLst: Incomplete | None = ...,
        rect: Incomplete | None = ...,
        pathLst: Incomplete | None = ...,
    ) -> None: ...

class PresetGeometry2D(Serialisable):
    namespace: Incomplete
    prst: Incomplete
    avLst: Incomplete
    def __init__(self, prst: Incomplete | None = ..., avLst: Incomplete | None = ...) -> None: ...

class FontReference(Serialisable):
    idx: Incomplete
    def __init__(self, idx: Incomplete | None = ...) -> None: ...

class StyleMatrixReference(Serialisable):
    idx: Incomplete
    def __init__(self, idx: Incomplete | None = ...) -> None: ...

class ShapeStyle(Serialisable):
    lnRef: Incomplete
    fillRef: Incomplete
    effectRef: Incomplete
    fontRef: Incomplete
    def __init__(
        self,
        lnRef: Incomplete | None = ...,
        fillRef: Incomplete | None = ...,
        effectRef: Incomplete | None = ...,
        fontRef: Incomplete | None = ...,
    ) -> None: ...
