from _typeshed import Incomplete
from collections.abc import Generator

from openpyxl.descriptors.serialisable import Serialisable

class Properties(Serialisable):
    locked: Incomplete
    defaultSize: Incomplete
    disabled: Incomplete
    uiObject: Incomplete
    autoFill: Incomplete
    autoLine: Incomplete
    altText: Incomplete
    textHAlign: Incomplete
    textVAlign: Incomplete
    lockText: Incomplete
    justLastX: Incomplete
    autoScale: Incomplete
    rowHidden: Incomplete
    colHidden: Incomplete
    __elements__: Incomplete
    anchor: Incomplete
    def __init__(
        self,
        locked: Incomplete | None = ...,
        defaultSize: Incomplete | None = ...,
        _print: Incomplete | None = ...,
        disabled: Incomplete | None = ...,
        uiObject: Incomplete | None = ...,
        autoFill: Incomplete | None = ...,
        autoLine: Incomplete | None = ...,
        altText: Incomplete | None = ...,
        textHAlign: Incomplete | None = ...,
        textVAlign: Incomplete | None = ...,
        lockText: Incomplete | None = ...,
        justLastX: Incomplete | None = ...,
        autoScale: Incomplete | None = ...,
        rowHidden: Incomplete | None = ...,
        colHidden: Incomplete | None = ...,
        anchor: Incomplete | None = ...,
    ) -> None: ...

class CommentRecord(Serialisable):
    tagname: str
    ref: Incomplete
    authorId: Incomplete
    guid: Incomplete
    shapeId: Incomplete
    text: Incomplete
    commentPr: Incomplete
    author: Incomplete
    __elements__: Incomplete
    __attrs__: Incomplete
    height: Incomplete
    width: Incomplete
    def __init__(
        self,
        ref: str = ...,
        authorId: int = ...,
        guid: Incomplete | None = ...,
        shapeId: int = ...,
        text: Incomplete | None = ...,
        commentPr: Incomplete | None = ...,
        author: Incomplete | None = ...,
        height: int = ...,
        width: int = ...,
    ) -> None: ...
    @classmethod
    def from_cell(cls, cell): ...
    @property
    def content(self): ...

class CommentSheet(Serialisable):
    tagname: str
    authors: Incomplete
    commentList: Incomplete
    extLst: Incomplete
    mime_type: str
    __elements__: Incomplete
    def __init__(
        self, authors: Incomplete | None = ..., commentList: Incomplete | None = ..., extLst: Incomplete | None = ...
    ) -> None: ...
    def to_tree(self): ...
    @property
    def comments(self) -> Generator[Incomplete, None, None]: ...
    @classmethod
    def from_comments(cls, comments): ...
    def write_shapes(self, vml: Incomplete | None = ...): ...
    @property
    def path(self): ...
