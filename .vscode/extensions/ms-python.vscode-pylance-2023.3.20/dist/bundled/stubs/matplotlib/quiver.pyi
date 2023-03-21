from .collections import PolyCollection
from typing import Literal
from ._typing import *
from .backend_bases import Event, MouseEvent, RendererBase
from .figure import Figure
from .axes import Axes
from .artist import Artist, allow_rasterization

class QuiverKey(Artist):

    halign = ...
    valign = ...
    pivot = ...
    def __init__(
        self,
        Q: Quiver,
        X: float,
        Y: float,
        U: float,
        label: str,
        *,
        angle: float = 0,
        coordinates: Literal["axes", "figure", "data", "inches"] = "axes",
        color: Color = ...,
        labelsep: float = 0.1,
        labelpos: Literal["N", "S", "E", "W"] = ...,
        labelcolor: Color = ...,
        fontproperties: dict = ...,
        **kwargs
    ) -> None: ...
    @property
    def labelsep(self): ...
    @allow_rasterization
    def draw(self, renderer: RendererBase): ...
    def set_figure(self, fig: Figure): ...
    def contains(self, mouseevent: MouseEvent) -> bool: ...

class Quiver(PolyCollection):
    def __init__(
        self,
        a: Axes,
        *args,
        scale: float = ...,
        headwidth: float = ...,
        headlength: float = ...,
        headaxislength: float = ...,
        minshaft: float = ...,
        minlength: float = ...,
        units=...,
        scale_units=...,
        angles=...,
        width: float = ...,
        color: Color = ...,
        pivot=...,
        **kwargs
    ) -> None: ...
    def get_datalim(self, transData): ...
    @allow_rasterization
    def draw(self, renderer: RendererBase): ...
    def set_UVC(self, U, V, C=...): ...

    quiver_doc = ...

class Barbs(PolyCollection):
    def __init__(
        self,
        ax: Axes,
        *args,
        pivot=...,
        length: float = ...,
        barbcolor: Color = ...,
        flagcolor: Color = ...,
        sizes=...,
        fill_empty=...,
        barb_increments=...,
        rounding=...,
        flip_barb=...,
        **kwargs
    ) -> None: ...
    def set_UVC(self, U, V, C=...): ...
    def set_offsets(self, xy): ...
    barbs_doc = ...
