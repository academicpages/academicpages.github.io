from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

horizontal_alignments: Incomplete
vertical_aligments: Incomplete

class Alignment(Serialisable):
    tagname: str
    __fields__: Incomplete
    horizontal: Incomplete
    vertical: Incomplete
    textRotation: Incomplete
    text_rotation: Incomplete
    wrapText: Incomplete
    wrap_text: Incomplete
    shrinkToFit: Incomplete
    shrink_to_fit: Incomplete
    indent: Incomplete
    relativeIndent: Incomplete
    justifyLastLine: Incomplete
    readingOrder: Incomplete
    def __init__(
        self,
        horizontal: Incomplete | None = ...,
        vertical: Incomplete | None = ...,
        textRotation: int = ...,
        wrapText: Incomplete | None = ...,
        shrinkToFit: Incomplete | None = ...,
        indent: int = ...,
        relativeIndent: int = ...,
        justifyLastLine: Incomplete | None = ...,
        readingOrder: int = ...,
        text_rotation: Incomplete | None = ...,
        wrap_text: Incomplete | None = ...,
        shrink_to_fit: Incomplete | None = ...,
        mergeCell: Incomplete | None = ...,
    ) -> None: ...
    def __iter__(self): ...
