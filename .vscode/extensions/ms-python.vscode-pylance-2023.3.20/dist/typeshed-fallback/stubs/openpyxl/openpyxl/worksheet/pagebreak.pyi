from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

class Break(Serialisable):
    tagname: str
    id: Incomplete
    min: Incomplete
    max: Incomplete
    man: Incomplete
    pt: Incomplete
    def __init__(self, id: int = ..., min: int = ..., max: int = ..., man: bool = ..., pt: Incomplete | None = ...) -> None: ...

class RowBreak(Serialisable):
    tagname: str
    # Overwritten by properties below
    # count: Integer
    # manualBreakCount: Integer
    brk: Incomplete
    __elements__: Incomplete
    __attrs__: Incomplete
    def __init__(self, count: Incomplete | None = ..., manualBreakCount: Incomplete | None = ..., brk=...) -> None: ...
    def __bool__(self) -> bool: ...
    def __len__(self) -> int: ...
    @property
    def count(self): ...
    @property
    def manualBreakCount(self): ...
    def append(self, brk: Incomplete | None = ...) -> None: ...

PageBreak = RowBreak

class ColBreak(RowBreak):
    tagname: str
    @property
    def count(self): ...
    @property
    def manualBreakCount(self): ...
    brk: Incomplete
    __attrs__: Incomplete
