from _typeshed import Incomplete

from openpyxl.descriptors import Sequence
from openpyxl.descriptors.serialisable import Serialisable

FILL_NONE: str
FILL_SOLID: str
FILL_PATTERN_DARKDOWN: str
FILL_PATTERN_DARKGRAY: str
FILL_PATTERN_DARKGRID: str
FILL_PATTERN_DARKHORIZONTAL: str
FILL_PATTERN_DARKTRELLIS: str
FILL_PATTERN_DARKUP: str
FILL_PATTERN_DARKVERTICAL: str
FILL_PATTERN_GRAY0625: str
FILL_PATTERN_GRAY125: str
FILL_PATTERN_LIGHTDOWN: str
FILL_PATTERN_LIGHTGRAY: str
FILL_PATTERN_LIGHTGRID: str
FILL_PATTERN_LIGHTHORIZONTAL: str
FILL_PATTERN_LIGHTTRELLIS: str
FILL_PATTERN_LIGHTUP: str
FILL_PATTERN_LIGHTVERTICAL: str
FILL_PATTERN_MEDIUMGRAY: str
fills: Incomplete

class Fill(Serialisable):
    tagname: str
    @classmethod
    def from_tree(cls, el): ...

class PatternFill(Fill):
    tagname: str
    __elements__: Incomplete
    patternType: Incomplete
    fill_type: Incomplete
    fgColor: Incomplete
    start_color: Incomplete
    bgColor: Incomplete
    end_color: Incomplete
    def __init__(
        self,
        patternType: Incomplete | None = ...,
        fgColor=...,
        bgColor=...,
        fill_type: Incomplete | None = ...,
        start_color: Incomplete | None = ...,
        end_color: Incomplete | None = ...,
    ) -> None: ...
    def to_tree(self, tagname: Incomplete | None = ..., idx: Incomplete | None = ...): ...  # type: ignore[override]

DEFAULT_EMPTY_FILL: Incomplete
DEFAULT_GRAY_FILL: Incomplete

class Stop(Serialisable):
    tagname: str
    position: Incomplete
    color: Incomplete
    def __init__(self, color, position) -> None: ...

class StopList(Sequence):
    expected_type: Incomplete
    def __set__(self, obj, values) -> None: ...

class GradientFill(Fill):
    tagname: str
    type: Incomplete
    fill_type: Incomplete
    degree: Incomplete
    left: Incomplete
    right: Incomplete
    top: Incomplete
    bottom: Incomplete
    stop: Incomplete
    def __init__(
        self, type: str = ..., degree: int = ..., left: int = ..., right: int = ..., top: int = ..., bottom: int = ..., stop=...
    ) -> None: ...
    def __iter__(self): ...
    def to_tree(self, tagname: Incomplete | None = ..., namespace: Incomplete | None = ..., idx: Incomplete | None = ...): ...  # type: ignore[override]
