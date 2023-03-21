from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

class Font(Serialisable):
    UNDERLINE_DOUBLE: str
    UNDERLINE_DOUBLE_ACCOUNTING: str
    UNDERLINE_SINGLE: str
    UNDERLINE_SINGLE_ACCOUNTING: str
    name: Incomplete
    charset: Incomplete
    family: Incomplete
    sz: Incomplete
    size: Incomplete
    b: Incomplete
    bold: Incomplete
    i: Incomplete
    italic: Incomplete
    strike: Incomplete
    strikethrough: Incomplete
    outline: Incomplete
    shadow: Incomplete
    condense: Incomplete
    extend: Incomplete
    u: Incomplete
    underline: Incomplete
    vertAlign: Incomplete
    color: Incomplete
    scheme: Incomplete
    tagname: str
    __elements__: Incomplete
    def __init__(
        self,
        name: Incomplete | None = ...,
        sz: Incomplete | None = ...,
        b: Incomplete | None = ...,
        i: Incomplete | None = ...,
        charset: Incomplete | None = ...,
        u: Incomplete | None = ...,
        strike: Incomplete | None = ...,
        color: Incomplete | None = ...,
        scheme: Incomplete | None = ...,
        family: Incomplete | None = ...,
        size: Incomplete | None = ...,
        bold: Incomplete | None = ...,
        italic: Incomplete | None = ...,
        strikethrough: Incomplete | None = ...,
        underline: Incomplete | None = ...,
        vertAlign: Incomplete | None = ...,
        outline: Incomplete | None = ...,
        shadow: Incomplete | None = ...,
        condense: Incomplete | None = ...,
        extend: Incomplete | None = ...,
    ) -> None: ...
    @classmethod
    def from_tree(cls, node): ...

DEFAULT_FONT: Incomplete
