from typing import Literal

from matplotlib.artist import Artist
from ._typing import *
from .collections import LineCollection
from .lines import Line2D
from .patches import Rectangle
from typing import Type

class Container(tuple):
    def __repr__(self) -> str: ...
    def __new__(cls: Type[Container], *args, **kwargs) -> Container: ...
    def __init__(self, kl: list[Rectangle], label: str = ...) -> None: ...
    def remove(self) -> None: ...
    def get_children(self) -> list[Rectangle]: ...

    get_label = Artist.get_label
    set_label = Artist.set_label
    add_callback = Artist.add_callback
    remove_callback = Artist.remove_callback
    pchanged = Artist.pchanged

class BarContainer(Container):

    patches: list[Rectangle]
    errorbar: None | ErrorbarContainer
    datavalues: None | ArrayLike
    orientation: None | Literal["horizontal", "vertical"]

    def __init__(
        self,
        patches: list[Rectangle],
        errorbar: ErrorbarContainer | None = ...,
        *,
        datavalues=...,
        orientation=...,
        **kwargs
    ) -> None: ...

class ErrorbarContainer(Container):

    lines: tuple[Line2D, tuple[Line2D, ...], list[LineCollection]]
    has_xerr: bool
    has_yerr: bool

    def __init__(
        self,
        lines: tuple[Line2D, tuple[Line2D, ...], list[LineCollection]],
        has_xerr: bool = ...,
        has_yerr: bool = ...,
        **kwargs
    ) -> None: ...

class StemContainer(Container):

    markerline: Line2D
    stemlines: list[Line2D]
    baseline: Line2D

    def __init__(
        self,
        markerline_stemlines_baseline: tuple[Line2D, list[Line2D], Line2D],
        **kwargs
    ) -> None: ...
