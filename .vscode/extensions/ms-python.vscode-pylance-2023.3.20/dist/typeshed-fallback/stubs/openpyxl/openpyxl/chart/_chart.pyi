from _typeshed import Incomplete
from abc import abstractmethod

from openpyxl.descriptors.serialisable import Serialisable

class AxId(Serialisable):  # type: ignore[misc]
    val: Incomplete
    def __init__(self, val) -> None: ...

def PlotArea(): ...

class ChartBase(Serialisable):
    legend: Incomplete
    layout: Incomplete
    roundedCorners: Incomplete
    axId: Incomplete
    visible_cells_only: Incomplete
    display_blanks: Incomplete
    ser: Incomplete
    series: Incomplete
    title: Incomplete
    anchor: str
    width: int
    height: float
    style: Incomplete
    mime_type: str
    graphical_properties: Incomplete
    __elements__: Incomplete
    plot_area: Incomplete
    pivotSource: Incomplete
    pivotFormats: Incomplete
    idx_base: int
    def __init__(self, axId=..., **kw) -> None: ...
    def __hash__(self) -> int: ...
    def __iadd__(self, other): ...
    def to_tree(self, namespace: Incomplete | None = ..., tagname: Incomplete | None = ..., idx: Incomplete | None = ...): ...  # type: ignore[override]
    def set_categories(self, labels) -> None: ...
    def add_data(self, data, from_rows: bool = ..., titles_from_data: bool = ...) -> None: ...
    def append(self, value) -> None: ...
    @property
    def path(self): ...
    @property
    @abstractmethod
    def tagname(self) -> str: ...
