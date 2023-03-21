from _typeshed import Incomplete
from abc import abstractmethod

from openpyxl.descriptors.serialisable import Serialisable

from ._chart import ChartBase

class _PieChartBase(ChartBase):
    varyColors: Incomplete
    ser: Incomplete
    dLbls: Incomplete
    dataLabels: Incomplete
    __elements__: Incomplete
    def __init__(self, varyColors: bool = ..., ser=..., dLbls: Incomplete | None = ...) -> None: ...
    @property
    @abstractmethod
    def tagname(self) -> str: ...

class PieChart(_PieChartBase):
    tagname: str
    varyColors: Incomplete
    ser: Incomplete
    dLbls: Incomplete
    firstSliceAng: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(self, firstSliceAng: int = ..., extLst: Incomplete | None = ..., **kw) -> None: ...

class PieChart3D(_PieChartBase):
    tagname: str
    varyColors: Incomplete
    ser: Incomplete
    dLbls: Incomplete
    extLst: Incomplete
    __elements__: Incomplete

class DoughnutChart(_PieChartBase):
    tagname: str
    varyColors: Incomplete
    ser: Incomplete
    dLbls: Incomplete
    firstSliceAng: Incomplete
    holeSize: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(self, firstSliceAng: int = ..., holeSize: int = ..., extLst: Incomplete | None = ..., **kw) -> None: ...

class CustomSplit(Serialisable):
    tagname: str
    secondPiePt: Incomplete
    __elements__: Incomplete
    def __init__(self, secondPiePt=...) -> None: ...

class ProjectedPieChart(_PieChartBase):
    tagname: str
    varyColors: Incomplete
    ser: Incomplete
    dLbls: Incomplete
    ofPieType: Incomplete
    type: Incomplete
    gapWidth: Incomplete
    splitType: Incomplete
    splitPos: Incomplete
    custSplit: Incomplete
    secondPieSize: Incomplete
    serLines: Incomplete
    join_lines: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        ofPieType: str = ...,
        gapWidth: Incomplete | None = ...,
        splitType: str = ...,
        splitPos: Incomplete | None = ...,
        custSplit: Incomplete | None = ...,
        secondPieSize: int = ...,
        serLines: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
        **kw,
    ) -> None: ...
