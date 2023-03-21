from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

class View3D(Serialisable):
    tagname: str
    rotX: Incomplete
    x_rotation: Incomplete
    hPercent: Incomplete
    height_percent: Incomplete
    rotY: Incomplete
    y_rotation: Incomplete
    depthPercent: Incomplete
    rAngAx: Incomplete
    right_angle_axes: Incomplete
    perspective: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        rotX: int = ...,
        hPercent: Incomplete | None = ...,
        rotY: int = ...,
        depthPercent: Incomplete | None = ...,
        rAngAx: bool = ...,
        perspective: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
    ) -> None: ...

class Surface(Serialisable):
    tagname: str
    thickness: Incomplete
    spPr: Incomplete
    graphicalProperties: Incomplete
    pictureOptions: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        thickness: Incomplete | None = ...,
        spPr: Incomplete | None = ...,
        pictureOptions: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
    ) -> None: ...

class _3DBase(Serialisable):
    tagname: str
    view3D: Incomplete
    floor: Incomplete
    sideWall: Incomplete
    backWall: Incomplete
    def __init__(
        self,
        view3D: Incomplete | None = ...,
        floor: Incomplete | None = ...,
        sideWall: Incomplete | None = ...,
        backWall: Incomplete | None = ...,
    ) -> None: ...
