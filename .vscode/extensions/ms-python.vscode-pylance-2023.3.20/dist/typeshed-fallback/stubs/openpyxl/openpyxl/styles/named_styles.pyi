from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

class NamedStyle(Serialisable):  # type: ignore[misc]
    font: Incomplete
    fill: Incomplete
    border: Incomplete
    alignment: Incomplete
    number_format: Incomplete
    protection: Incomplete
    builtinId: Incomplete
    hidden: Incomplete
    # Overwritten by property below
    # xfId: Integer
    name: Incomplete
    def __init__(
        self,
        name: str = ...,
        font=...,
        fill=...,
        border=...,
        alignment=...,
        number_format: Incomplete | None = ...,
        protection=...,
        builtinId: Incomplete | None = ...,
        hidden: bool = ...,
        xfId: Incomplete | None = ...,
    ) -> None: ...
    def __setattr__(self, attr: str, value) -> None: ...
    def __iter__(self): ...
    @property
    def xfId(self): ...
    def bind(self, wb) -> None: ...
    def as_tuple(self): ...
    def as_xf(self): ...
    def as_name(self): ...

class NamedStyleList(list[Incomplete]):
    @property
    def names(self): ...
    def __getitem__(self, key): ...
    def append(self, style) -> None: ...

class _NamedCellStyle(Serialisable):
    tagname: str
    name: Incomplete
    xfId: Incomplete
    builtinId: Incomplete
    iLevel: Incomplete
    hidden: Incomplete
    customBuiltin: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        name: Incomplete | None = ...,
        xfId: Incomplete | None = ...,
        builtinId: Incomplete | None = ...,
        iLevel: Incomplete | None = ...,
        hidden: Incomplete | None = ...,
        customBuiltin: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
    ) -> None: ...

class _NamedCellStyleList(Serialisable):
    tagname: str
    # Overwritten by property below
    # count: Integer
    cellStyle: Incomplete
    __attrs__: Incomplete
    def __init__(self, count: Incomplete | None = ..., cellStyle=...) -> None: ...
    @property
    def count(self): ...
    @property
    def names(self): ...
