from typing import Sequence
from ._layoutgrid import LayoutGrid
from .figure import Figure, FigureBase
from .gridspec import GridSpecBase

class LayoutEngine:
    def __init__(self, **kwargs) -> None: ...
    def set(self, **kwargs)-> None: ...
    @property
    def colorbar_gridspec(self) -> bool: ...
    @property
    def adjust_compatible(self) -> bool: ...
    def get(self): ...
    def execute(self, fig: Figure): ...

class TightLayoutEngine(LayoutEngine):
    def __init__(
        self,
        *,
        pad: float = 1.08,
        h_pad: float = ...,
        w_pad: float = ...,
        rect: Sequence[float] = ...,
        **kwargs
    ) -> None: ...
    def execute(self, fig: Figure) -> None: ...
    def set(
        self,
        *,
        pad: float = 1.08,
        w_pad: float = ...,
        h_pad: float = ...,
        rect: Sequence[float] = ...
    ) -> None: ...

class ConstrainedLayoutEngine(LayoutEngine):
    def __init__(
        self,
        *,
        h_pad: float = ...,
        w_pad: float = ...,
        hspace: float = ...,
        wspace: float = ...,
        rect: Sequence[float] = ...,
        compress: bool = ...,
        **kwargs
    ) -> None: ...
    def execute(
        self, fig: Figure
    ) -> dict[str | FigureBase | GridSpecBase, bool | LayoutGrid]: ...
    def set(
        self,
        *,
        h_pad: float = ...,
        w_pad: float = ...,
        hspace: float = ...,
        wspace: float = ...,
        rect: tuple = ...
    ) -> None: ...
