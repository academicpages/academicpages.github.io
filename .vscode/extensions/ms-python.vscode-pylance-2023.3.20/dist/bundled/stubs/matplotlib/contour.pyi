from tkinter import Label
from matplotlib.collections import Collection
from typing import Callable, Iterable, Literal, Sequence
from ._typing import *
from .transforms import Transform
from .text import Text
from .cm import ScalarMappable
from .ticker import Formatter
from .axes import Axes
from .artist import Artist

class ClabelText(Text):
    def get_rotation(self) -> float: ...

class ContourLabeler:
    def clabel(
        self,
        levels: ArrayLike = ...,
        *,
        fontsize: str | float = ...,
        inline: bool = ...,
        inline_spacing: float = ...,
        fmt: Formatter | str | Callable | dict = ...,
        colors: Color | Sequence[Color] | None = ...,
        use_clabeltext: bool = ...,
        manual: bool | Iterable = ...,
        rightside_up: bool = ...,
        zorder: float | None = ...
    ) -> list[Label]: ...
    def print_label(self, linecontour, labelwidth) -> bool: ...
    def too_close(self, x, y, lw) -> bool: ...
    def get_label_width(self, lev, fmt, fsize) -> float: ...
    def set_label_props(self, label, text, color) -> None: ...
    def get_text(self, lev, fmt): ...
    def locate_label(self, linecontour, labelwidth): ...
    def calc_label_rot_and_inline(self, slc, ind, lw, lc=..., spacing=...): ...
    def add_label(self, x, y, rotation, lev, cvalue): ...
    def add_label_clabeltext(self, x, y, rotation, lev, cvalue): ...
    def add_label_near(
        self,
        x: float,
        y: float,
        inline: bool = ...,
        inline_spacing: int = ...,
        transform: Transform | Literal[False] = ...,
    ): ...
    def pop_label(self, index=...): ...
    def labels(self, inline, inline_spacing): ...

class ContourSet(ScalarMappable, ContourLabeler):
    def __init__(
        self,
        ax: Axes,
        *args,
        levels: Sequence[float] = ...,
        filled=...,
        linewidths=...,
        linestyles=...,
        hatches=...,
        alpha=...,
        origin=...,
        extent=...,
        cmap=...,
        colors=...,
        norm=...,
        vmin=...,
        vmax=...,
        extend=...,
        antialiased=...,
        nchunk=...,
        locator=...,
        transform=...,
        **kwargs
    ) -> None: ...
    def get_transform(self) -> Transform: ...
    def __getstate__(self): ...
    def legend_elements(
        self, variable_name: str = ..., str_format: Callable = ...
    ) -> tuple[list[Artist], list[str]]: ...
    def changed(self) -> bool: ...
    def get_alpha(self) -> float: ...
    def set_alpha(self, alpha: float) -> None: ...
    def find_nearest_contour(
        self, x: float, y: float, indices: list[int] | None = ..., pixel: bool = ...
    ) -> tuple[Collection, int, int, tuple[float, float], float]: ...

class QuadContourSet(ContourSet): ...
