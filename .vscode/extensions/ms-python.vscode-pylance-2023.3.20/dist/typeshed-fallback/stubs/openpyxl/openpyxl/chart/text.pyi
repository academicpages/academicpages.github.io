from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

class RichText(Serialisable):
    tagname: str
    bodyPr: Incomplete
    properties: Incomplete
    lstStyle: Incomplete
    p: Incomplete
    paragraphs: Incomplete
    __elements__: Incomplete
    def __init__(
        self, bodyPr: Incomplete | None = ..., lstStyle: Incomplete | None = ..., p: Incomplete | None = ...
    ) -> None: ...

class Text(Serialisable):
    tagname: str
    strRef: Incomplete
    rich: Incomplete
    __elements__: Incomplete
    def __init__(self, strRef: Incomplete | None = ..., rich: Incomplete | None = ...) -> None: ...
    def to_tree(self, tagname: Incomplete | None = ..., idx: Incomplete | None = ..., namespace: Incomplete | None = ...): ...
