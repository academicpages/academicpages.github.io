from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

BORDER_NONE: Incomplete
BORDER_DASHDOT: str
BORDER_DASHDOTDOT: str
BORDER_DASHED: str
BORDER_DOTTED: str
BORDER_DOUBLE: str
BORDER_HAIR: str
BORDER_MEDIUM: str
BORDER_MEDIUMDASHDOT: str
BORDER_MEDIUMDASHDOTDOT: str
BORDER_MEDIUMDASHED: str
BORDER_SLANTDASHDOT: str
BORDER_THICK: str
BORDER_THIN: str

class Side(Serialisable):  # type: ignore[misc]
    __fields__: Incomplete
    color: Incomplete
    style: Incomplete
    border_style: Incomplete
    def __init__(
        self, style: Incomplete | None = ..., color: Incomplete | None = ..., border_style: Incomplete | None = ...
    ) -> None: ...

class Border(Serialisable):
    tagname: str
    __fields__: Incomplete
    __elements__: Incomplete
    start: Incomplete
    end: Incomplete
    left: Incomplete
    right: Incomplete
    top: Incomplete
    bottom: Incomplete
    diagonal: Incomplete
    vertical: Incomplete
    horizontal: Incomplete
    outline: Incomplete
    diagonalUp: Incomplete
    diagonalDown: Incomplete
    diagonal_direction: Incomplete
    def __init__(
        self,
        left: Incomplete | None = ...,
        right: Incomplete | None = ...,
        top: Incomplete | None = ...,
        bottom: Incomplete | None = ...,
        diagonal: Incomplete | None = ...,
        diagonal_direction: Incomplete | None = ...,
        vertical: Incomplete | None = ...,
        horizontal: Incomplete | None = ...,
        diagonalUp: bool = ...,
        diagonalDown: bool = ...,
        outline: bool = ...,
        start: Incomplete | None = ...,
        end: Incomplete | None = ...,
    ) -> None: ...
    def __iter__(self): ...

DEFAULT_BORDER: Incomplete
