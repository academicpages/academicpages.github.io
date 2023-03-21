from typing import Literal
from matplotlib._typing import *
from matplotlib.axes import Axes

def tripcolor(
    ax: Axes,
    *args,
    alpha=...,
    norm=...,
    cmap=...,
    vmin=...,
    vmax=...,
    shading: Literal["flat", "gouraud"] = "flat",
    facecolors: ArrayLike = ...,
    **kwargs
): ...
