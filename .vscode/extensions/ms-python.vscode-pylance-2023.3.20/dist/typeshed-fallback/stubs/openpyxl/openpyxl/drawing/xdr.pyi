from _typeshed import Incomplete

from .geometry import Point2D, PositiveSize2D, Transform2D

class XDRPoint2D(Point2D):
    namespace: Incomplete
    x: Incomplete
    y: Incomplete

class XDRPositiveSize2D(PositiveSize2D):
    namespace: Incomplete
    cx: Incomplete
    cy: Incomplete

class XDRTransform2D(Transform2D):
    namespace: Incomplete
    rot: Incomplete
    flipH: Incomplete
    flipV: Incomplete
    off: Incomplete
    ext: Incomplete
    chOff: Incomplete
    chExt: Incomplete
