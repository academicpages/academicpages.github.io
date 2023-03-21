from _typeshed import Incomplete
from abc import abstractmethod

from openpyxl.descriptors.serialisable import Serialisable

from ._3d import _3DBase
from ._chart import ChartBase

class BandFormat(Serialisable):
    tagname: str
    idx: Incomplete
    spPr: Incomplete
    graphicalProperties: Incomplete
    __elements__: Incomplete
    def __init__(self, idx: int = ..., spPr: Incomplete | None = ...) -> None: ...

class BandFormatList(Serialisable):
    tagname: str
    bandFmt: Incomplete
    __elements__: Incomplete
    def __init__(self, bandFmt=...) -> None: ...

class _SurfaceChartBase(ChartBase):
    wireframe: Incomplete
    ser: Incomplete
    bandFmts: Incomplete
    __elements__: Incomplete
    def __init__(self, wireframe: Incomplete | None = ..., ser=..., bandFmts: Incomplete | None = ..., **kw) -> None: ...
    @property
    @abstractmethod
    def tagname(self) -> str: ...

class SurfaceChart3D(_SurfaceChartBase, _3DBase):
    tagname: str
    wireframe: Incomplete
    ser: Incomplete
    bandFmts: Incomplete
    extLst: Incomplete
    x_axis: Incomplete
    y_axis: Incomplete
    z_axis: Incomplete
    __elements__: Incomplete
    def __init__(self, **kw) -> None: ...

class SurfaceChart(SurfaceChart3D):
    tagname: str
    wireframe: Incomplete
    ser: Incomplete
    bandFmts: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(self, **kw) -> None: ...
