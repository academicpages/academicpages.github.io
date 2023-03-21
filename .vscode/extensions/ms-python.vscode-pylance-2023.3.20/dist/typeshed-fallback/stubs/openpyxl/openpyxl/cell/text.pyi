from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.styles.fonts import Font

class PhoneticProperties(Serialisable):
    tagname: str
    fontId: Incomplete
    type: Incomplete
    alignment: Incomplete
    def __init__(
        self, fontId: Incomplete | None = ..., type: Incomplete | None = ..., alignment: Incomplete | None = ...
    ) -> None: ...

class PhoneticText(Serialisable):
    tagname: str
    sb: Incomplete
    eb: Incomplete
    t: Incomplete
    text: Incomplete
    def __init__(self, sb: Incomplete | None = ..., eb: Incomplete | None = ..., t: Incomplete | None = ...) -> None: ...

class InlineFont(Font):
    tagname: str
    rFont: Incomplete
    charset: Incomplete
    family: Incomplete
    b: Incomplete
    i: Incomplete
    strike: Incomplete
    outline: Incomplete
    shadow: Incomplete
    condense: Incomplete
    extend: Incomplete
    color: Incomplete
    sz: Incomplete
    u: Incomplete
    vertAlign: Incomplete
    scheme: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        rFont: Incomplete | None = ...,
        charset: Incomplete | None = ...,
        family: Incomplete | None = ...,
        b: Incomplete | None = ...,
        i: Incomplete | None = ...,
        strike: Incomplete | None = ...,
        outline: Incomplete | None = ...,
        shadow: Incomplete | None = ...,
        condense: Incomplete | None = ...,
        extend: Incomplete | None = ...,
        color: Incomplete | None = ...,
        sz: Incomplete | None = ...,
        u: Incomplete | None = ...,
        vertAlign: Incomplete | None = ...,
        scheme: Incomplete | None = ...,
    ) -> None: ...

class RichText(Serialisable):
    tagname: str
    rPr: Incomplete
    font: Incomplete
    t: Incomplete
    text: Incomplete
    __elements__: Incomplete
    def __init__(self, rPr: Incomplete | None = ..., t: Incomplete | None = ...) -> None: ...

class Text(Serialisable):
    tagname: str
    t: Incomplete
    plain: Incomplete
    r: Incomplete
    formatted: Incomplete
    rPh: Incomplete
    phonetic: Incomplete
    phoneticPr: Incomplete
    PhoneticProperties: Incomplete
    __elements__: Incomplete
    def __init__(self, t: Incomplete | None = ..., r=..., rPh=..., phoneticPr: Incomplete | None = ...) -> None: ...
    @property
    def content(self): ...
