from pandas.plotting._matplotlib.core import LinePlot as LinePlot

class HistPlot(LinePlot):
    bins = ...
    bottom = ...
    def __init__(self, data, bins: int = ..., bottom: int = ..., **kwargs) -> None: ...
    @property
    def orientation(self): ...

class KdePlot(HistPlot):
    orientation: str = ...
    bw_method = ...
    ind = ...
    def __init__(self, data, bw_method=..., ind=..., **kwargs) -> None: ...

def hist_series(
    self,
    by=...,
    ax=...,
    grid: bool = ...,
    xlabelsize=...,
    xrot=...,
    ylabelsize=...,
    yrot=...,
    figsize=...,
    bins: int = ...,
    **kwds,
): ...
def hist_frame(
    data,
    column=...,
    by=...,
    grid: bool = ...,
    xlabelsize=...,
    xrot=...,
    ylabelsize=...,
    yrot=...,
    ax=...,
    sharex: bool = ...,
    sharey: bool = ...,
    figsize=...,
    layout=...,
    bins: int = ...,
    **kwds,
): ...
