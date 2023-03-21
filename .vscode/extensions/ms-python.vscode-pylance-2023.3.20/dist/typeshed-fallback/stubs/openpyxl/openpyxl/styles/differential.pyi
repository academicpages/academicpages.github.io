from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

class DifferentialStyle(Serialisable):
    tagname: str
    __elements__: Incomplete
    font: Incomplete
    numFmt: Incomplete
    fill: Incomplete
    alignment: Incomplete
    border: Incomplete
    protection: Incomplete
    extLst: Incomplete
    def __init__(
        self,
        font: Incomplete | None = ...,
        numFmt: Incomplete | None = ...,
        fill: Incomplete | None = ...,
        alignment: Incomplete | None = ...,
        border: Incomplete | None = ...,
        protection: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
    ) -> None: ...

class DifferentialStyleList(Serialisable):
    tagname: str
    dxf: Incomplete
    styles: Incomplete
    __attrs__: Incomplete
    def __init__(self, dxf=..., count: Incomplete | None = ...) -> None: ...
    def append(self, dxf) -> None: ...
    def add(self, dxf): ...
    def __bool__(self) -> bool: ...
    def __getitem__(self, idx): ...
    @property
    def count(self): ...
