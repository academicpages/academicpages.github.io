from typing import Callable, Sequence
from .patches import Rectangle
from .offsetbox import OffsetBox
from .lines import Line2D
from .legend import Legend
from .container import BarContainer
from .artist import Artist

from collections.abc import Sequence

def update_from_first_child(tgt: Rectangle, src: BarContainer) -> None: ...

class HandlerBase:
    def __init__(
        self,
        xpad: float = ...,
        ypad: float = ...,
        update_func: Callable = ...,
    ) -> None: ...
    def update_prop(
        self, legend_handle: Artist, orig_handle: Artist, legend: Legend
    ): ...
    def adjust_drawing_area(
        self,
        legend: Legend,
        orig_handle: Artist,
        xdescent,
        ydescent,
        width,
        height,
        fontsize: int,
    ): ...
    def legend_artist(
        self, legend: Legend, orig_handle: Artist, fontsize: int, handlebox: OffsetBox
    ): ...
    def create_artists(
        self,
        legend: Legend,
        orig_handle: Artist,
        xdescent,
        ydescent,
        width,
        height,
        fontsize: int,
        trans,
    ): ...

class HandlerNpoints(HandlerBase):
    def __init__(
        self, marker_pad: float = ..., numpoints: None = ..., **kwargs
    ) -> None: ...
    def get_numpoints(self, legend: Legend): ...
    def get_xdata(
        self, legend: Legend, xdescent, ydescent, width, height, fontsize: int
    ): ...

class HandlerNpointsYoffsets(HandlerNpoints):
    def __init__(
        self, numpoints: int = ..., yoffsets: Sequence[float] = ..., **kwargs
    ) -> None: ...
    def get_ydata(
        self, legend: Legend, xdescent, ydescent, width, height, fontsize: int
    ): ...

class HandlerLine2DCompound(HandlerNpoints):
    def create_artists(
        self,
        legend: Legend,
        orig_handle: Artist,
        xdescent,
        ydescent,
        width,
        height,
        fontsize: int,
        trans,
    ): ...

class _Line2DHandleList(Sequence):
    def __init__(self, legline: Line2D) -> None: ...
    def __len__(self): ...
    def __getitem__(self, index: int) -> Line2D: ...

class HandlerLine2D(HandlerNpoints):
    def create_artists(
        self,
        legend: Legend,
        orig_handle: Artist,
        xdescent,
        ydescent,
        width,
        height,
        fontsize: int,
        trans,
    ): ...

class HandlerPatch(HandlerBase):
    def __init__(self, patch_func: None = ..., **kwargs) -> None: ...
    def create_artists(
        self,
        legend: Legend,
        orig_handle: Artist,
        xdescent,
        ydescent,
        width,
        height,
        fontsize: int,
        trans,
    ): ...

class HandlerStepPatch(HandlerBase):
    def create_artists(
        self,
        legend: Legend,
        orig_handle: Artist,
        xdescent,
        ydescent,
        width,
        height,
        fontsize: int,
        trans,
    ): ...

class HandlerLineCollection(HandlerLine2D):
    def get_numpoints(self, legend: Legend): ...
    def create_artists(
        self,
        legend: Legend,
        orig_handle: Artist,
        xdescent,
        ydescent,
        width,
        height,
        fontsize: int,
        trans,
    ): ...

class HandlerRegularPolyCollection(HandlerNpointsYoffsets):
    def __init__(self, yoffsets=..., sizes=..., **kwargs) -> None: ...
    def get_numpoints(self, legend: Legend): ...
    def get_sizes(
        self,
        legend: Legend,
        orig_handle: Artist,
        xdescent,
        ydescent,
        width,
        height,
        fontsize: int,
    ): ...
    def update_prop(
        self, legend_handle: Artist, orig_handle: Artist, legend: Legend
    ): ...
    def create_collection(self, orig_handle, sizes, offsets, offset_transform): ...
    def create_artists(
        self,
        legend: Legend,
        orig_handle: Artist,
        xdescent,
        ydescent,
        width,
        height,
        fontsize: int,
        trans,
    ): ...

class HandlerPathCollection(HandlerRegularPolyCollection):
    def create_collection(
        self, orig_handle: Artist, sizes, offsets, offset_transform
    ): ...

class HandlerCircleCollection(HandlerRegularPolyCollection):
    def create_collection(
        self, orig_handle: Artist, sizes, offsets, offset_transform
    ): ...

class HandlerErrorbar(HandlerLine2D):
    def __init__(
        self,
        xerr_size: float = ...,
        yerr_size: float = ...,
        marker_pad: float = ...,
        numpoints: int = ...,
        **kwargs
    ) -> None: ...
    def get_err_size(
        self, legend: Legend, xdescent, ydescent, width, height, fontsize: int
    ): ...
    def create_artists(
        self,
        legend: Legend,
        orig_handle: Artist,
        xdescent,
        ydescent,
        width,
        height,
        fontsize: int,
        trans,
    ): ...

class HandlerStem(HandlerNpointsYoffsets):
    def __init__(
        self,
        marker_pad: float = 0.3,
        numpoints: int = ...,
        bottom: float = ...,
        yoffsets: Sequence[float] = ...,
        **kwargs
    ) -> None: ...
    def get_ydata(
        self, legend: Legend, xdescent, ydescent, width, height, fontsize: int
    ): ...
    def create_artists(
        self,
        legend: Legend,
        orig_handle: Artist,
        xdescent,
        ydescent,
        width,
        height,
        fontsize: int,
        trans,
    ): ...

class HandlerTuple(HandlerBase):
    def __init__(self, ndivide: int = 1, pad: float = ..., **kwargs) -> None: ...
    def create_artists(
        self,
        legend: Legend,
        orig_handle: Artist,
        xdescent,
        ydescent,
        width,
        height,
        fontsize: int,
        trans,
    ): ...

class HandlerPolyCollection(HandlerBase):
    def create_artists(
        self,
        legend: Legend,
        orig_handle: Artist,
        xdescent,
        ydescent,
        width,
        height,
        fontsize: int,
        trans,
    ): ...
