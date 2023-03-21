from _typeshed import Incomplete
from array import array

from openpyxl.descriptors.serialisable import Serialisable

class ArrayDescriptor:
    key: Incomplete
    def __init__(self, key) -> None: ...
    def __get__(self, instance, cls): ...
    def __set__(self, instance, value) -> None: ...

class StyleArray(array[Incomplete]):
    tagname: str
    fontId: Incomplete
    fillId: Incomplete
    borderId: Incomplete
    numFmtId: Incomplete
    protectionId: Incomplete
    alignmentId: Incomplete
    pivotButton: Incomplete
    quotePrefix: Incomplete
    xfId: Incomplete
    def __new__(cls, args=...): ...
    def __hash__(self) -> int: ...
    def __copy__(self): ...
    def __deepcopy__(self, memo): ...

class CellStyle(Serialisable):
    tagname: str
    numFmtId: Incomplete
    fontId: Incomplete
    fillId: Incomplete
    borderId: Incomplete
    xfId: Incomplete
    quotePrefix: Incomplete
    pivotButton: Incomplete
    applyNumberFormat: Incomplete
    applyFont: Incomplete
    applyFill: Incomplete
    applyBorder: Incomplete
    # Overwritten by properties below
    # applyAlignment: Bool
    # applyProtection: Bool
    alignment: Incomplete
    protection: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    __attrs__: Incomplete
    def __init__(
        self,
        numFmtId: int = ...,
        fontId: int = ...,
        fillId: int = ...,
        borderId: int = ...,
        xfId: Incomplete | None = ...,
        quotePrefix: Incomplete | None = ...,
        pivotButton: Incomplete | None = ...,
        applyNumberFormat: Incomplete | None = ...,
        applyFont: Incomplete | None = ...,
        applyFill: Incomplete | None = ...,
        applyBorder: Incomplete | None = ...,
        applyAlignment: Incomplete | None = ...,
        applyProtection: Incomplete | None = ...,
        alignment: Incomplete | None = ...,
        protection: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
    ) -> None: ...
    def to_array(self): ...
    @classmethod
    def from_array(cls, style): ...
    @property
    def applyProtection(self): ...
    @property
    def applyAlignment(self): ...

class CellStyleList(Serialisable):
    tagname: str
    __attrs__: Incomplete
    # Overwritten by property below
    # count: Integer
    xf: Incomplete
    alignment: Incomplete
    protection: Incomplete
    __elements__: Incomplete
    def __init__(self, count: Incomplete | None = ..., xf=...) -> None: ...
    @property
    def count(self): ...
    def __getitem__(self, idx): ...
