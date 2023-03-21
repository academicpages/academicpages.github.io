from typing import NamedTuple

from matplotlib.axes import Axes as PlotAxes
from matplotlib.lines import Line2D

from pandas.plotting._matplotlib.core import LinePlot as LinePlot

class BoxPlot(LinePlot):
    class BP(NamedTuple):
        ax: PlotAxes
        lines: dict[str, list[Line2D]]
    return_type = ...
    def __init__(self, data, return_type: str = ..., **kwargs) -> None: ...
    def maybe_color_bp(self, bp) -> None: ...
    @property
    def orientation(self): ...
    @property
    def result(self): ...

def boxplot(
    data,
    column=...,
    by=...,
    ax=...,
    fontsize=...,
    rot: int = ...,
    grid: bool = ...,
    figsize=...,
    layout=...,
    return_type=...,
    **kwds,
): ...
def boxplot_frame(
    self,
    column=...,
    by=...,
    ax=...,
    fontsize=...,
    rot: int = ...,
    grid: bool = ...,
    figsize=...,
    layout=...,
    return_type=...,
    **kwds,
): ...
def boxplot_frame_groupby(
    grouped,
    subplots: bool = ...,
    column=...,
    fontsize=...,
    rot: int = ...,
    grid: bool = ...,
    ax=...,
    figsize=...,
    layout=...,
    sharex: bool = ...,
    sharey: bool = ...,
    **kwds,
): ...
