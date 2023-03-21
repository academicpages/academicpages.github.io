from _typeshed import Incomplete

from openpyxl.descriptors import Strict
from openpyxl.descriptors.serialisable import Serialisable

FONT_PATTERN: str
COLOR_PATTERN: str
SIZE_REGEX: str
FORMAT_REGEX: Incomplete

class _HeaderFooterPart(Strict):
    text: Incomplete
    font: Incomplete
    size: Incomplete
    RGB: str
    color: Incomplete
    def __init__(
        self,
        text: Incomplete | None = ...,
        font: Incomplete | None = ...,
        size: Incomplete | None = ...,
        color: Incomplete | None = ...,
    ) -> None: ...
    def __bool__(self) -> bool: ...
    @classmethod
    def from_str(cls, text): ...

class HeaderFooterItem(Strict):
    left: Incomplete
    center: Incomplete
    centre: Incomplete
    right: Incomplete
    def __init__(
        self, left: Incomplete | None = ..., right: Incomplete | None = ..., center: Incomplete | None = ...
    ) -> None: ...
    def __bool__(self) -> bool: ...
    def to_tree(self, tagname): ...
    @classmethod
    def from_tree(cls, node): ...

class HeaderFooter(Serialisable):
    tagname: str
    differentOddEven: Incomplete
    differentFirst: Incomplete
    scaleWithDoc: Incomplete
    alignWithMargins: Incomplete
    oddHeader: Incomplete
    oddFooter: Incomplete
    evenHeader: Incomplete
    evenFooter: Incomplete
    firstHeader: Incomplete
    firstFooter: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        differentOddEven: Incomplete | None = ...,
        differentFirst: Incomplete | None = ...,
        scaleWithDoc: Incomplete | None = ...,
        alignWithMargins: Incomplete | None = ...,
        oddHeader: Incomplete | None = ...,
        oddFooter: Incomplete | None = ...,
        evenHeader: Incomplete | None = ...,
        evenFooter: Incomplete | None = ...,
        firstHeader: Incomplete | None = ...,
        firstFooter: Incomplete | None = ...,
    ) -> None: ...
    def __bool__(self) -> bool: ...
