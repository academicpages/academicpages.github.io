from typing import Literal, Sequence, Type
from libcst import For
from .backend_bases import RendererBase
from .gridspec import SubplotSpec
from .text import Text
from .cm import ScalarMappable
from .colors import Colormap, Normalize
from .collections import LineCollection
from .ticker import Formatter, Locator
from .axes import Axes
from .axis import Tick
from .spines import Spine

class _ColorbarSpine(Spine):
    def __init__(self, axes) -> None: ...
    def get_window_extent(self, renderer: RendererBase=...): ...
    def set_xy(self, xy: Sequence[float])-> None: ...
    def draw(self, renderer)-> None: ...

class _ColorbarAxesLocator:
    def __init__(self, cbar) -> None: ...
    def __call__(self, ax, renderer): ...
    def get_subplotspec(self)-> SubplotSpec: ...

class Colorbar:
    ax: Axes
    lines: list[LineCollection]
    dividers: LineCollection
    n_rasterize: int = ...

    def __init__(
        self,
        ax: Axes,
        mappable: ScalarMappable = ...,
        *,
        cmap: Colormap = ...,
        norm: Normalize = ...,
        alpha: float = ...,
        values: None = ...,
        boundaries: None = ...,
        orientation: Literal["vertical", "horizontal"] = 'vertical',
        ticklocation: Literal["auto", "left", "right", "top", "bottom"] = 'auto',
        extend: Literal["neither", "both", "min", "max"]|None = None,
        spacing: Literal["uniform", "proportional"] = 'uniform',
        ticks: None | Sequence[Tick] | Locator = None,
        format: None | str | Formatter = None,
        drawedges: bool = False,
        filled: bool = True,
        extendfrac=None,
        extendrect: bool = False,
        label: str = ''
    ) -> None: ...
    @property
    def locator(self)-> Locator: ...
    @locator.setter
    def locator(self, loc: Locator)-> None: ...
    @property
    def minorlocator(self)-> Locator: ...
    @minorlocator.setter
    def minorlocator(self, loc: Locator)-> None: ...
    @property
    def formatter(self)-> Formatter: ...
    @formatter.setter
    def formatter(self, fmt: Formatter)-> None: ...
    @property
    def minorformatter(self)-> Formatter: ...
    @minorformatter.setter
    def minorformatter(self, fmt: Formatter)-> None: ...

    def update_normal(self, mappable)-> None: ...
    def draw_all(self)-> None: ...
    def add_lines(self, *args, **kwargs)-> None: ...
    def update_ticks(self)-> None: ...
    def set_ticks(
        self,
        ticks: list[float],
        update_ticks: bool=True,
        labels: list[str]|None = None,
        *,
        minor: bool = False,
        **kwargs
    )-> None: ...
    def get_ticks(self, minor: bool = False)-> list: ...
    def set_ticklabels(
        self, ticklabels: Text, update_ticks: bool = True, *, minor: bool=False, **kwargs
    )-> None: ...
    def minorticks_on(self)-> None: ...
    def minorticks_off(self)-> None: ...
    def set_label(self, label: str, *, loc: str|None = None, **kwargs)-> None: ...
    def set_alpha(self, alpha: float)-> None: ...
    def remove(self)-> None: ...
    def drag_pan(self, button, key, x, y)-> None: ...

ColorbarBase: Type[Colorbar] = Colorbar

def make_axes(
    parents: Axes | list[Axes],
    location: None | Literal["left", "right", "top", "bottom"] = None,
    orientation: None | Literal["vertical", "horizontal"] = None,
    fraction: float = 0.15,
    shrink: float = 1.0,
    aspect: float = 20,
    **kwargs
)-> tuple[Axes, dict]: ...
def make_axes_gridspec(
    parent: Axes,
    *,
    location: None | Literal["left", "right", "top", "bottom"] = None,
    orientation: None | Literal["vertical", "horizontal"] = None,
    fraction: float = 0.15,
    shrink: float = 1.0,
    aspect: float = 20,
    **kwargs
)-> tuple[Axes, dict]: ...
