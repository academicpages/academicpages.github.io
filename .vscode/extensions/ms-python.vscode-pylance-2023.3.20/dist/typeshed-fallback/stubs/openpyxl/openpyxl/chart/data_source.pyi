from _typeshed import Incomplete

from openpyxl.descriptors.nested import NestedText
from openpyxl.descriptors.serialisable import Serialisable

class NumFmt(Serialisable):  # type: ignore[misc]
    formatCode: Incomplete
    sourceLinked: Incomplete
    def __init__(self, formatCode: Incomplete | None = ..., sourceLinked: bool = ...) -> None: ...

class NumberValueDescriptor(NestedText):
    allow_none: bool
    expected_type: Incomplete
    def __set__(self, instance, value) -> None: ...

class NumVal(Serialisable):  # type: ignore[misc]
    idx: Incomplete
    formatCode: Incomplete
    v: Incomplete
    def __init__(self, idx: Incomplete | None = ..., formatCode: Incomplete | None = ..., v: Incomplete | None = ...) -> None: ...

class NumData(Serialisable):  # type: ignore[misc]
    formatCode: Incomplete
    ptCount: Incomplete
    pt: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(
        self, formatCode: Incomplete | None = ..., ptCount: Incomplete | None = ..., pt=..., extLst: Incomplete | None = ...
    ) -> None: ...

class NumRef(Serialisable):  # type: ignore[misc]
    f: Incomplete
    ref: Incomplete
    numCache: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(
        self, f: Incomplete | None = ..., numCache: Incomplete | None = ..., extLst: Incomplete | None = ...
    ) -> None: ...

class StrVal(Serialisable):
    tagname: str
    idx: Incomplete
    v: Incomplete
    def __init__(self, idx: int = ..., v: Incomplete | None = ...) -> None: ...

class StrData(Serialisable):
    tagname: str
    ptCount: Incomplete
    pt: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(self, ptCount: Incomplete | None = ..., pt=..., extLst: Incomplete | None = ...) -> None: ...

class StrRef(Serialisable):
    tagname: str
    f: Incomplete
    strCache: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(
        self, f: Incomplete | None = ..., strCache: Incomplete | None = ..., extLst: Incomplete | None = ...
    ) -> None: ...

class NumDataSource(Serialisable):  # type: ignore[misc]
    numRef: Incomplete
    numLit: Incomplete
    def __init__(self, numRef: Incomplete | None = ..., numLit: Incomplete | None = ...) -> None: ...

class Level(Serialisable):
    tagname: str
    pt: Incomplete
    __elements__: Incomplete
    def __init__(self, pt=...) -> None: ...

class MultiLevelStrData(Serialisable):
    tagname: str
    ptCount: Incomplete
    lvl: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(self, ptCount: Incomplete | None = ..., lvl=..., extLst: Incomplete | None = ...) -> None: ...

class MultiLevelStrRef(Serialisable):
    tagname: str
    f: Incomplete
    multiLvlStrCache: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(
        self, f: Incomplete | None = ..., multiLvlStrCache: Incomplete | None = ..., extLst: Incomplete | None = ...
    ) -> None: ...

class AxDataSource(Serialisable):
    tagname: str
    numRef: Incomplete
    numLit: Incomplete
    strRef: Incomplete
    strLit: Incomplete
    multiLvlStrRef: Incomplete
    def __init__(
        self,
        numRef: Incomplete | None = ...,
        numLit: Incomplete | None = ...,
        strRef: Incomplete | None = ...,
        strLit: Incomplete | None = ...,
        multiLvlStrRef: Incomplete | None = ...,
    ) -> None: ...
