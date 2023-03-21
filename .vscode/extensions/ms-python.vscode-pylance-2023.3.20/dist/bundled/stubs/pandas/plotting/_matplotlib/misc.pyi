def scatter_matrix(
    frame,
    alpha: float = ...,
    figsize=...,
    ax=...,
    grid: bool = ...,
    diagonal: str = ...,
    marker: str = ...,
    density_kwds=...,
    hist_kwds=...,
    range_padding: float = ...,
    **kwds,
): ...
def radviz(frame, class_column, ax=..., color=..., colormap=..., **kwds): ...
def andrews_curves(
    frame, class_column, ax=..., samples: int = ..., color=..., colormap=..., **kwds
): ...
def bootstrap_plot(series, fig=..., size: int = ..., samples: int = ..., **kwds): ...
def parallel_coordinates(
    frame,
    class_column,
    cols=...,
    ax=...,
    color=...,
    use_columns: bool = ...,
    xticks=...,
    colormap=...,
    axvlines: bool = ...,
    axvlines_kwds=...,
    sort_labels: bool = ...,
    **kwds,
): ...
def lag_plot(series, lag: int = ..., ax=..., **kwds): ...
def autocorrelation_plot(series, ax=..., **kwds): ...
