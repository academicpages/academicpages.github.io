from _typeshed import Incomplete

from openpyxl.descriptors import Strict
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.styles.styleable import StyleableObject
from openpyxl.utils.bound_dictionary import BoundDictionary

class Dimension(Strict, StyleableObject):
    __fields__: Incomplete
    index: Incomplete
    hidden: Incomplete
    outlineLevel: Incomplete
    outline_level: Incomplete
    collapsed: Incomplete
    style: Incomplete
    def __init__(
        self, index, hidden, outlineLevel, collapsed, worksheet, visible: bool = ..., style: Incomplete | None = ...
    ) -> None: ...
    def __iter__(self): ...
    def __copy__(self): ...

class RowDimension(Dimension):
    __fields__: Incomplete
    r: Incomplete
    s: Incomplete
    ht: Incomplete
    height: Incomplete
    thickBot: Incomplete
    thickTop: Incomplete
    def __init__(
        self,
        worksheet,
        index: int = ...,
        ht: Incomplete | None = ...,
        customHeight: Incomplete | None = ...,
        s: Incomplete | None = ...,
        customFormat: Incomplete | None = ...,
        hidden: bool = ...,
        outlineLevel: int = ...,
        outline_level: Incomplete | None = ...,
        collapsed: bool = ...,
        visible: Incomplete | None = ...,
        height: Incomplete | None = ...,
        r: Incomplete | None = ...,
        spans: Incomplete | None = ...,
        thickBot: Incomplete | None = ...,
        thickTop: Incomplete | None = ...,
        **kw,
    ) -> None: ...
    @property
    def customFormat(self): ...
    @property
    def customHeight(self): ...

class ColumnDimension(Dimension):
    width: Incomplete
    bestFit: Incomplete
    auto_size: Incomplete
    index: Incomplete
    min: Incomplete
    max: Incomplete
    collapsed: Incomplete
    __fields__: Incomplete
    def __init__(
        self,
        worksheet,
        index: str = ...,
        width=...,
        bestFit: bool = ...,
        hidden: bool = ...,
        outlineLevel: int = ...,
        outline_level: Incomplete | None = ...,
        collapsed: bool = ...,
        style: Incomplete | None = ...,
        min: Incomplete | None = ...,
        max: Incomplete | None = ...,
        customWidth: bool = ...,
        visible: Incomplete | None = ...,
        auto_size: Incomplete | None = ...,
    ) -> None: ...
    @property
    def customWidth(self): ...
    def reindex(self) -> None: ...
    def to_tree(self): ...

class DimensionHolder(BoundDictionary):
    worksheet: Incomplete
    max_outline: Incomplete
    default_factory: Incomplete
    def __init__(self, worksheet, reference: str = ..., default_factory: Incomplete | None = ...) -> None: ...
    def group(self, start, end: Incomplete | None = ..., outline_level: int = ..., hidden: bool = ...) -> None: ...
    def to_tree(self): ...

class SheetFormatProperties(Serialisable):
    tagname: str
    baseColWidth: Incomplete
    defaultColWidth: Incomplete
    defaultRowHeight: Incomplete
    customHeight: Incomplete
    zeroHeight: Incomplete
    thickTop: Incomplete
    thickBottom: Incomplete
    outlineLevelRow: Incomplete
    outlineLevelCol: Incomplete
    def __init__(
        self,
        baseColWidth: int = ...,
        defaultColWidth: Incomplete | None = ...,
        defaultRowHeight: int = ...,
        customHeight: Incomplete | None = ...,
        zeroHeight: Incomplete | None = ...,
        thickTop: Incomplete | None = ...,
        thickBottom: Incomplete | None = ...,
        outlineLevelRow: Incomplete | None = ...,
        outlineLevelCol: Incomplete | None = ...,
    ) -> None: ...

class SheetDimension(Serialisable):
    tagname: str
    ref: Incomplete
    def __init__(self, ref: Incomplete | None = ...) -> None: ...
    @property
    def boundaries(self): ...
