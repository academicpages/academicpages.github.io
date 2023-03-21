from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

from .cell_range import CellRange

class MergeCell(CellRange):
    tagname: str
    @property
    def ref(self): ...
    __attrs__: Incomplete
    def __init__(self, ref: Incomplete | None = ...) -> None: ...
    def __copy__(self): ...

class MergeCells(Serialisable):
    tagname: str
    # Overwritten by property below
    # count: Integer
    mergeCell: Incomplete
    __elements__: Incomplete
    __attrs__: Incomplete
    def __init__(self, count: Incomplete | None = ..., mergeCell=...) -> None: ...
    @property
    def count(self): ...

class MergedCellRange(CellRange):
    ws: Incomplete
    start_cell: Incomplete
    def __init__(self, worksheet, coord) -> None: ...
    def format(self) -> None: ...
    def __contains__(self, coord): ...
    def __copy__(self): ...
