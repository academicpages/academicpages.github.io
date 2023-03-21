from collections.abc import (
    Hashable,
    Sequence,
)
from typing import (
    Any,
    Literal,
)

from matplotlib.axes import Axes
from matplotlib.colors import Colormap
from matplotlib.figure import Figure
from matplotlib.table import Table
import numpy as np
from pandas.core.frame import DataFrame
from pandas.core.series import Series
from typing_extensions import TypeAlias

from pandas._typing import (
    HashableT,
    npt,
)

_Color: TypeAlias = str | Sequence[float]

def table(
    ax: Axes,
    data: DataFrame | Series,
    **kwargs,
) -> Table: ...
def register() -> None: ...
def deregister() -> None: ...
def scatter_matrix(
    frame: DataFrame,
    alpha: float = ...,
    figsize: tuple[float, float] | None = ...,
    ax: Axes | None = ...,
    grid: bool = ...,
    diagonal: Literal["hist", "kde"] = ...,
    marker: str = ...,
    density_kwds: dict[str, Any] | None = ...,
    hist_kwds: dict[str, Any] | None = ...,
    range_padding: float = ...,
    **kwargs,
) -> npt.NDArray[np.object_]: ...
def radviz(
    frame: DataFrame,
    class_column: Hashable,
    ax: Axes | None = ...,
    color: _Color | Sequence[_Color] | None = ...,
    colormap: str | Colormap | None = ...,
    **kwds,
) -> Axes: ...
def andrews_curves(
    frame: DataFrame,
    class_column: Hashable,
    ax: Axes | None = ...,
    samples: int = ...,
    color: _Color | Sequence[_Color] | None = ...,
    colormap: str | Colormap | None = ...,
    **kwargs,
) -> Axes: ...
def bootstrap_plot(
    series: Series,
    fig: Figure | None = ...,
    size: int = ...,
    samples: int = ...,
    **kwds,
) -> Figure: ...
def parallel_coordinates(
    frame: DataFrame,
    class_column: Hashable,
    cols: list[HashableT] | None = ...,
    ax: Axes | None = ...,
    color: _Color | Sequence[_Color] | None = ...,
    use_columns: bool = ...,
    xticks: Sequence[float] | None = ...,
    colormap: str | Colormap | None = ...,
    axvlines: bool = ...,
    axvlines_kwds: dict[str, Any] | None = ...,
    sort_labels: bool = ...,
    **kwargs,
) -> Axes: ...
def lag_plot(series: Series, lag: int = ..., ax: Axes | None = ..., **kwds) -> Axes: ...
def autocorrelation_plot(series: Series, ax: Axes | None = ..., **kwargs) -> Axes: ...

plot_params: dict[str, Any]
