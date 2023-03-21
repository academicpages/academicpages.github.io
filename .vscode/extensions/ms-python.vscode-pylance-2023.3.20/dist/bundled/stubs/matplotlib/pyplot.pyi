import datetime
from matplotlib.contour import QuadContourSet
import numpy as np
from typing import Callable, ContextManager, Literal, Sequence, overload
from matplotlib import rcParams as rcParams
from matplotlib import style as style
from ._typing import *
from .tri.tricontour import TriContourSet
from .transforms import Bbox, Transform
from .text import Text, Annotation
from .container import BarContainer, ErrorbarContainer, StemContainer
from .patches import Polygon, FancyArrow
from .quiver import Quiver
from .colors import Colormap, Normalize
from .backend_bases import FigureCanvasBase, MouseButton, FigureManagerBase
from .collections import (
    LineCollection,
    Collection,
    QuadMesh,
    PathCollection,
    PolyCollection,
    BrokenBarHCollection,
)
from .lines import Line2D
from .legend import Legend
from .image import AxesImage, FigureImage
from .figure import Figure, SubFigure
from .scale import ScaleBase
from .backend_bases import _Backend
from .axes import Axes as Axes
from .artist import Artist
from .table import Table
from .widgets import SubplotTool
from .markers import MarkerStyle
from .streamplot import StreamplotSet

from array import array
import matplotlib
import matplotlib.image
from . import rcParams
from .rcsetup import interactive_bk as _interactive_bk

def install_repl_displayhook()-> None: ...
def uninstall_repl_displayhook()-> None: ...

def draw_all(force: bool = False)-> None: ...

def set_loglevel(*args, **kwargs)-> None: ...
def findobj(o=..., match=..., include_self: bool = ...) -> list: ...
def switch_backend(newbackend: str)-> None:
    class backend_mod(_Backend): ...

def new_figure_manager(*args, **kwargs)-> FigureManagerBase: ...
def draw_if_interactive(*args, **kwargs): ...
def show(*args, **kwargs): ...
def isinteractive() -> bool: ...

class _IoffContext:
    def __init__(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_value, traceback): ...

class _IonContext:
    def __init__(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_value, traceback): ...

def ioff()-> _IoffContext: ...
def ion()-> _IonContext: ...
def pause(interval)-> None: ...
def rc(group, **kwargs)-> None: ...
def rc_context(rc: dict = ..., fname: str | PathLike = ...)-> ContextManager: ...
def rcdefaults()-> None: ...
def getp(obj: Artist, *args, **kwargs): ...
def get(obj: Artist, *args, **kwargs): ...
def setp(obj: Artist | list, *args, **kwargs): ...
def xkcd(scale: float = ..., length: float = ..., randomness: float = ...)-> _xkcd: ...

class _xkcd:
    def __init__(self, scale: float, length: float, randomness: float) -> None: ...
    def __enter__(self)-> _xkcd: ...
    def __exit__(self, *args)-> None: ...

def figure(
    num: int | str | Figure | SubFigure| None = None,
    figsize: Sequence[float]|None = None,
    dpi: float|None = None,
    facecolor: Color|None = None,
    edgecolor: Color|None = None,
    frameon: bool = True,
    FigureClass = ...,
    clear: bool = False,
    **kwargs
) -> Figure: ...
def gcf() -> Figure: ...
def fignum_exists(num) -> bool: ...
def get_fignums() -> list[int]: ...
def get_figlabels(): ...
def get_current_fig_manager() -> FigureManagerBase: ...
def connect(s: str, func: Callable): ...
def disconnect(cid: int): ...
def close(fig: None | int | str | Figure = ...): ...
def clf() -> None: ...
def draw() -> None: ...
def savefig(*args, **kwargs) -> None: ...
def figlegend(*args, **kwargs) -> Legend: ...
def axes(arg: None | tuple = ..., **kwargs) -> Axes: ...
def delaxes(ax: Axes = ...) -> None: ...
def sca(ax: Axes) -> None: ...
def cla() -> None: ...
def subplot(*args, **kwargs) -> Axes: ...


@overload
def subplots(
    nrows: int = ...,
    ncols: int = ...,
    *,
    squeeze: Literal[False],
    sharex: bool | Literal["none", "all", "row", "col"] = ...,
    sharey: bool | Literal["none", "all", "row", "col"] = ...,
    subplot_kw: dict = ...,
    gridspec_kw: dict = ...,
    **fig_kw
) -> tuple[Figure, list[list[Axes]]]: ...
@overload
def subplots(
    nrows: Literal[1],
    ncols: Literal[1],
    *,
    sharex: bool | Literal["none", "all", "row", "col"] = ...,
    sharey: bool | Literal["none", "all", "row", "col"] = ...,
    squeeze: Literal[True] = ...,
    subplot_kw: dict = ...,
    gridspec_kw: dict = ...,
    **fig_kw
) -> tuple[Figure, Axes]: ...

##

@overload
def subplots(
    nrows: Literal[1],
    ncols: int,
    *,
    sharex: bool | Literal["none", "all", "row", "col"] = ...,
    sharey: bool | Literal["none", "all", "row", "col"] = ...,
    squeeze: Literal[True] = ...,
    subplot_kw: dict = ...,
    gridspec_kw: dict = ...,
    **fig_kw
) -> tuple[Figure, list[Axes]]: ...
@overload
def subplots(
    nrows: int,
    ncols: Literal[1],
    *,
    sharex: bool | Literal["none", "all", "row", "col"] = ...,
    sharey: bool | Literal["none", "all", "row", "col"] = ...,
    squeeze: Literal[True] = ...,
    subplot_kw: dict = ...,
    gridspec_kw: dict = ...,
    **fig_kw
) -> tuple[Figure, list[Axes]]: ...
@overload
def subplots(
    *,
    nrows: int,
    ncols: int,
    sharex: bool | Literal["none", "all", "row", "col"] = ...,
    sharey: bool | Literal["none", "all", "row", "col"] = ...,
    squeeze: Literal[True] = ...,
    subplot_kw: dict = ...,
    gridspec_kw: dict = ...,
    **fig_kw
) -> tuple[Figure, list[list[Axes]]]: ...
@overload
def subplots(
    *,
    ncols: int,
    sharex: bool | Literal["none", "all", "row", "col"] = ...,
    sharey: bool | Literal["none", "all", "row", "col"] = ...,
    squeeze: Literal[True] = ...,
    subplot_kw: dict = ...,
    gridspec_kw: dict = ...,
    **fig_kw
) -> tuple[Figure, list[Axes]]: ...
@overload
def subplots(
    nrows: int,
    *,
    sharex: bool | Literal["none", "all", "row", "col"] = ...,
    sharey: bool | Literal["none", "all", "row", "col"] = ...,
    squeeze: Literal[True] = ...,
    subplot_kw: dict = ...,
    gridspec_kw: dict = ...,
    **fig_kw
) -> tuple[Figure, list[Axes]]: ...

@overload
def subplots(
    *,
    sharex: bool | Literal["none", "all", "row", "col"] = ...,
    sharey: bool | Literal["none", "all", "row", "col"] = ...,
    squeeze: Literal[True] = ...,
    subplot_kw: dict = ...,
    gridspec_kw: dict = ...,
    **fig_kw
) -> tuple[Figure, Axes]: ...

@overload
def subplots(
    nrows: int = ...,
    ncols: int = ...,
    *,
    sharex: bool | Literal["none", "all", "row", "col"] = ...,
    sharey: bool | Literal["none", "all", "row", "col"] = ...,
    squeeze: bool = ...,
    subplot_kw: dict = ...,
    gridspec_kw: dict = ...,
    **fig_kw
) -> tuple[Figure, list[list[Axes]]]: ...
def subplot_mosaic(
    mosaic: list | str,
    *,
    sharex: bool = ...,
    sharey: bool = ...,
    subplot_kw: dict = ...,
    gridspec_kw: dict = ...,
    empty_sentinel: object = ...,
    **fig_kw
) -> dict[Text, Axes]: ...
def subplot2grid(
    shape: Sequence[int],
    loc: Sequence[int],
    rowspan: int = ...,
    colspan: int = ...,
    fig: Figure = ...,
    **kwargs
) -> Axes: ...
def twinx(ax: Axes = ...) -> Axes: ...
def twiny(ax: Axes = ...) -> Axes: ...
def subplot_tool(targetfig: Figure = ...) -> SubplotTool: ...
def box(on: bool | None = ...): ...
def xlim(*args, **kwargs) -> tuple[float, float]: ...
def ylim(*args, **kwargs) -> tuple[float, float]: ...
def xticks(
    ticks: ArrayLike = ..., labels: ArrayLike = ..., **kwargs
) -> tuple[list, list[Text]]: ...
def yticks(
    ticks: ArrayLike = ..., labels: ArrayLike = ..., **kwargs
) -> tuple[list, list[Text]]: ...
def rgrids(
    radii: Sequence[float] = ...,
    labels: Sequence[str] | None = ...,
    angle: float = ...,
    fmt: str | None = ...,
    **kwargs
) -> tuple[list[Line2D], list[Text]]: ...
def thetagrids(
    angles: Sequence[float] = ...,
    labels: Sequence[str] | None = ...,
    fmt: str | None = ...,
    **kwargs
) -> tuple[list[Line2D], list[Text]]: ...
def get_plot_commands() -> list: ...
def colorbar(mappable=..., cax: Axes = ..., ax: Axes = ..., **kwargs): ...
def clim(vmin: float | None = ..., vmax: float | None = ...): ...
def set_cmap(cmap: Colormap | str): ...
def imread(fname: str | FileLike, format: str = ...) -> np.ndarray: ...
def imsave(fname: str | PathLike | FileLike, arr: ArrayLike, **kwargs): ...
def matshow(
    A: ArrayLike, fignum: None | int | Literal[False] = ..., **kwargs
) -> AxesImage: ...
def polar(*args, **kwargs): ...
def figimage(
    X: ArrayLike,
    xo: float = ...,
    yo: float = ...,
    alpha: None | float = ...,
    norm: Normalize = ...,
    cmap: str | Colormap = ...,
    vmin: float = ...,
    vmax: float = ...,
    origin: Literal["upper", "lower"] = ...,
    resize: bool = ...,
    **kwargs
) -> FigureImage: ...
def figtext(
    x: float, y: float, s: str, fontdict: dict = ..., **kwargs
) -> text.Text: ...
def gca(): ...
def gci(): ...
def ginput(
    n: int = ...,
    timeout: float = ...,
    show_clicks: bool = ...,
    mouse_add: MouseButton | None = ...,
    mouse_pop: MouseButton | None = ...,
    mouse_stop: MouseButton | None = ...,
) -> list[tuple]: ...
def subplots_adjust(
    left: float = ...,
    bottom: float = ...,
    right: float = ...,
    top: float = ...,
    wspace: float = ...,
    hspace: float = ...,
): ...
def suptitle(t: str, **kwargs) -> Text: ...
def tight_layout(
    *,
    pad: float = ...,
    h_pad: float = ...,
    w_pad: float = ...,
    rect: Sequence[float] = ...
): ...
def waitforbuttonpress(timeout=...): ...
def acorr(x: ArrayLike, *, data=..., **kwargs): ...
def angle_spectrum(
    x: Sequence[float],
    Fs: float = ...,
    Fc: float = ...,
    window: Callable | np.ndarray = ...,
    pad_to: float = ...,
    sides: Literal["default", "onesided", "twosided"] = ...,
    *,
    data=...,
    **kwargs
): ...
def annotate(
    text: str,
    xy: Sequence[float],
    xytext: Sequence[float] = ...,
    xycoords: str | Artist | Transform | Callable = ...,
    textcoords: str | Artist | Transform | Callable = ...,
    arrowprops: dict = ...,
    annotation_clip: bool | None = ...,
    **kwargs
) -> Annotation: ...
def arrow(x: float, y: float, dx: float, dy: float, **kwargs) -> FancyArrow: ...
def autoscale(
    enable: bool | None = ...,
    axis: Literal["both", "x", "y"] = ...,
    tight: bool | None = ...,
): ...
def axhline(
    y: float = ..., xmin: float = ..., xmax: float = ..., **kwargs
) -> Line2D: ...
def axhspan(
    ymin: float, ymax: float, xmin: float = ..., xmax: float = ..., **kwargs
) -> Polygon: ...
def axis(*args, emit: bool = ..., **kwargs): ...
def axline(
    xy1: Sequence[float], xy2: Sequence[float] = ..., *, slope: float = ..., **kwargs
) -> Line2D: ...
def axvline(
    x: float = ..., ymin: float = ..., ymax: float = ..., **kwargs
) -> Line2D: ...
def axvspan(
    xmin: float, xmax: float, ymin: float = ..., ymax: float = ..., **kwargs
) -> Polygon: ...
def bar(
    x: float | ArrayLike,
    height: float | ArrayLike,
    width: float | ArrayLike = ...,
    bottom: float | ArrayLike = ...,
    *,
    align: Literal["center", "edge"] = ...,
    data=...,
    **kwargs
) -> BarContainer: ...
def barbs(*args, data=..., **kwargs): ...
def barh(
    y: float | ArrayLike,
    width: float | ArrayLike,
    height: float | ArrayLike = ...,
    left: float | ArrayLike = ...,
    *,
    align: Literal["center", "edge"] = ...,
    **kwargs
) -> BarContainer: ...
def bar_label(
    container: BarContainer,
    labels: ArrayLike = ...,
    *,
    fmt: str = ...,
    label_type: Literal["edge", "center"] = ...,
    padding: float = ...,
    **kwargs
) -> list: ...
def boxplot(
    x: ArrayLike,
    notch: bool = ...,
    sym: str = ...,
    vert: bool = ...,
    whis: float = ...,
    positions: ArrayLike = ...,
    widths: float | ArrayLike = ...,
    patch_artist: bool = ...,
    bootstrap: int = ...,
    usermedians=...,
    conf_intervals: ArrayLike = ...,
    meanline: bool = ...,
    showmeans=...,
    showcaps=...,
    showbox=...,
    showfliers=...,
    boxprops=...,
    labels: Sequence = ...,
    flierprops=...,
    medianprops=...,
    meanprops=...,
    capprops=...,
    whiskerprops=...,
    manage_ticks: bool = ...,
    autorange: bool = ...,
    zorder: float = ...,
    capwidths=...,
    *,
    data=...
) -> dict: ...
def broken_barh(xranges, yrange, *, data=..., **kwargs) -> BrokenBarHCollection: ...
def clabel(CS, levels: ArrayLike = ..., **kwargs): ...
def cohere(
    x,
    y,
    NFFT: int = ...,
    Fs: float = ...,
    Fc: float = ...,
    detrend: Literal["none", "mean", "linear"] | Callable = ...,
    window: Callable | np.ndarray = ...,
    noverlap: float = ...,
    pad_to: float = ...,
    sides: Literal["default", "onesided", "twosided"] = ...,
    scale_by_freq: bool = ...,
    *,
    data=...,
    **kwargs
): ...
def contour(*args, data=..., **kwargs) -> QuadContourSet: ...
def contourf(*args, data=..., **kwargs) -> QuadContourSet: ...
def csd(
    x: Sequence[float],
    y: Sequence[float],
    NFFT: int = ...,
    Fs: float = ...,
    Fc: float = ...,
    detrend: Literal["none", "mean", "linear"] | Callable = ...,
    window: Callable | np.ndarray = ...,
    noverlap: float = ...,
    pad_to: float = ...,
    sides: Literal["default", "onesided", "twosided"] = ...,
    scale_by_freq: bool = ...,
    return_line: bool = ...,
    *,
    data=...,
    **kwargs
): ...
def errorbar(
    x: float | ArrayLike,
    y: float | ArrayLike,
    yerr: float | ArrayLike = ...,
    xerr: float | ArrayLike = ...,
    fmt: str = ...,
    ecolor: Color = ...,
    elinewidth: float = ...,
    capsize: float = ...,
    barsabove: bool = ...,
    lolims: bool = ...,
    uplims: bool = ...,
    xlolims: bool = ...,
    xuplims: bool = ...,
    errorevery: int = ...,
    capthick: float = ...,
    *,
    data=...,
    **kwargs
) -> ErrorbarContainer: ...
def eventplot(
    positions: ArrayLike | Sequence[ArrayLike],
    orientation: Literal["horizontal", "vertical"] = ...,
    lineoffsets: float | ArrayLike = ...,
    linelengths: float | ArrayLike = ...,
    linewidths: float | ArrayLike = ...,
    colors: Color | list[Color] = ...,
    linestyles: str | tuple | list = ...,
    *,
    data=...,
    **kwargs
) -> list: ...
def fill(*args, data=..., **kwargs) -> list[Polygon]: ...
def fill_between(
    x,
    y1: Scalar,
    y2: Scalar = ...,
    where: ArrayLike = ...,
    interpolate: bool = ...,
    step: Literal["pre", "post", "mid"] = ...,
    *,
    data=...,
    **kwargs
) -> PolyCollection: ...
def fill_betweenx(
    y,
    x1: Scalar,
    x2: Scalar = ...,
    where: ArrayLike = ...,
    step: Literal["pre", "post", "mid"] = ...,
    interpolate: bool = ...,
    *,
    data=...,
    **kwargs
) -> PolyCollection: ...
def grid(
    visible: bool | None = ...,
    which: Literal["major", "minor", "both"] = ...,
    axis: Literal["both", "x", "y"] = ...,
    **kwargs
): ...
def hexbin(
    x: ArrayLike,
    y: ArrayLike,
    C: ArrayLike = ...,
    gridsize: int = ...,
    bins: Literal["log"] | int | Sequence = ...,
    xscale: Literal["linear", "log"] = ...,
    yscale: Literal["linear", "log"] = ...,
    extent=...,
    cmap=...,
    norm=...,
    vmin=...,
    vmax=...,
    alpha=...,
    linewidths=...,
    edgecolors=...,
    reduce_C_function=...,
    mincnt: int = ...,
    marginals: bool = ...,
    *,
    data=...,
    **kwargs
) -> PolyCollection: ...
def hist(
    x,
    bins: int | Sequence | str = ...,
    range: tuple | None = ...,
    density: bool = ...,
    weights=...,
    cumulative: bool | Literal[-1] = ...,
    bottom=...,
    histtype: Literal["bar", "barstacked", "step", "stepfilled"] = ...,
    align: Literal["left", "mid", "right"] = ...,
    orientation: Literal["vertical", "horizontal"] = ...,
    rwidth: float | None = ...,
    log: bool = ...,
    color: Color | None = ...,
    label: str | None = ...,
    stacked: bool = ...,
    *,
    data=...,
    **kwargs
): ...
def stairs(
    values: ArrayLike,
    edges: ArrayLike = ...,
    *,
    orientation: Literal["vertical", "horizontal"] = ...,
    baseline: float | ArrayLike | None = ...,
    fill: bool = ...,
    data=...,
    **kwargs
): ...
def hist2d(
    x,
    y,
    bins: None | int | ArrayLike = ...,
    range=...,
    density: bool = ...,
    weights=...,
    cmin: float = ...,
    cmax: float = ...,
    *,
    data=...,
    **kwargs
): ...
def hlines(
    y: float | ArrayLike,
    xmin: float | ArrayLike,
    xmax: float | ArrayLike,
    colors: list[Color] = ...,
    linestyles: Literal["solid", "dashed", "dashdot", "dotted"] = ...,
    label: str = ...,
    *,
    data=...,
    **kwargs
) -> LineCollection: ...
def imshow(
    X: ArrayLike,
    cmap: str | Colormap = ...,
    norm: Normalize = ...,
    aspect: Literal["equal", "auto"] | float = ...,
    interpolation: str = ...,
    alpha: float | ArrayLike = ...,
    vmin: float = ...,
    vmax: float = ...,
    origin: Literal["upper", "lower"] = ...,
    extent: Sequence[float] = ...,
    *,
    interpolation_stage: Literal["data", "rgba"] = ...,
    filternorm: bool = ...,
    filterrad: float = ...,
    resample: bool = ...,
    url: str = ...,
    data=...,
    **kwargs
) -> AxesImage: ...
def legend(*args, **kwargs) -> Legend: ...
def locator_params(
    axis: Literal["both", "x", "y"] = ..., tight: bool | None = ..., **kwargs
): ...
def loglog(*args, **kwargs) -> list: ...
def magnitude_spectrum(
    x: Sequence,
    Fs: float = ...,
    Fc: float = ...,
    window: Callable | np.ndarray = ...,
    pad_to: float = ...,
    sides: Literal["default", "onesided", "twosided"] = ...,
    scale: Literal["default", "linear", "dB"] = ...,
    *,
    data=...,
    **kwargs
): ...
def margins(*margins, x: float = ..., y: float = ..., tight: bool | None = ...): ...
def minorticks_off(): ...
def minorticks_on(): ...
def pcolor(
    *args,
    shading: Literal["flat", "nearest", "auto"] = ...,
    alpha: float = ...,
    norm: Normalize = ...,
    cmap: str | Colormap = ...,
    vmin: float = ...,
    vmax: float = ...,
    data=...,
    **kwargs
) -> Collection: ...
def pcolormesh(
    *args,
    alpha: float = ...,
    norm: Normalize = ...,
    cmap: str | Colormap = ...,
    vmin: float = ...,
    vmax: float = ...,
    shading: Literal["flat", "nearest", "gouraud", "auto"] = ...,
    antialiased=...,
    data=...,
    **kwargs
) -> QuadMesh: ...
def phase_spectrum(
    x: Sequence,
    Fs: float = ...,
    Fc: float = ...,
    window: Callable | np.ndarray = ...,
    pad_to: float = ...,
    sides: Literal["default", "onesided", "twosided"] = ...,
    *,
    data=...,
    **kwargs
): ...
def pie(
    x,
    explode: ArrayLike = ...,
    labels: Sequence[str] = ...,
    colors: ArrayLike = ...,
    autopct: None | str | Callable = ...,
    pctdistance: float = ...,
    shadow: bool = ...,
    labeldistance: float | None = ...,
    startangle: float = ...,
    radius: float = ...,
    counterclock: bool = ...,
    wedgeprops: dict = ...,
    textprops: dict = ...,
    center: tuple[float, float] = ...,
    frame: bool = ...,
    rotatelabels: bool = ...,
    *,
    normalize: bool = ...,
    data=...
): ...
def plot(*args, scalex=..., scaley=..., data=..., **kwargs) -> list: ...
def plot_date(
    x: ArrayLike,
    y: ArrayLike,
    fmt: str = ...,
    tz: datetime.tzinfo = ...,
    xdate: bool = ...,
    ydate: bool = ...,
    *,
    data=...,
    **kwargs
) -> list: ...
def psd(
    x: Sequence,
    NFFT: int = ...,
    Fs: float = ...,
    Fc: float = ...,
    detrend: Literal["none", "mean", "linear"] | Callable = ...,
    window: Callable | np.ndarray = ...,
    noverlap: float = ...,
    pad_to: float = ...,
    sides: Literal["default", "onesided", "twosided"] = ...,
    scale_by_freq: bool = ...,
    return_line: bool = ...,
    *,
    data=...,
    **kwargs
): ...
def quiver(*args, data=..., **kwargs) -> Quiver: ...
def quiverkey(Q: Quiver, X: float, Y: float, U: float, label: str, **kwargs): ...
def scatter(
    x: float | ArrayLike,
    y: float | ArrayLike,
    s: float | ArrayLike = ...,
    c: ArrayLike | list[Color] | Color = ...,
    marker: MarkerStyle = ...,
    cmap: str | Colormap = ...,
    norm: Normalize = ...,
    vmin: float = ...,
    vmax: float = ...,
    alpha: float = ...,
    linewidths: float | ArrayLike = ...,
    *,
    edgecolors: Color = ...,
    plotnonfinite: bool = ...,
    data=...,
    **kwargs
) -> PathCollection: ...
def semilogx(*args, **kwargs) -> list: ...
def semilogy(*args, **kwargs) -> list: ...
def specgram(
    x: Sequence,
    NFFT: int = ...,
    Fs: float = ...,
    Fc: float = ...,
    detrend: Literal["none", "mean", "linear"] | Callable = ...,
    window: Callable | np.ndarray = ...,
    noverlap: int = ...,
    cmap: Colormap = ...,
    xextent=...,
    pad_to: float = ...,
    sides: Literal["default", "onesided", "twosided"] = ...,
    scale_by_freq: bool = ...,
    mode: Literal["default", "psd", "magnitude", "angle", "phase"] = ...,
    scale: Literal["default", "linear", "dB"] = ...,
    vmin=...,
    vmax=...,
    *,
    data=...,
    **kwargs
): ...
def spy(
    Z,
    precision: float | Literal["present"] = ...,
    marker=...,
    markersize=...,
    aspect: Literal["equal", "auto", None] | float = ...,
    origin: Literal["upper", "lower"] = ...,
    **kwargs
) -> tuple[AxesImage, Line2D]: ...
def stackplot(
    x,
    *args,
    labels: list[str] = ...,
    colors: list[Color] = ...,
    baseline: Literal["zero", "sym", "wiggle", "weighted_wiggle"] = ...,
    data=...,
    **kwargs
) -> list: ...
def stem(
    *args,
    linefmt: str = ...,
    markerfmt: str = ...,
    basefmt: str = ...,
    bottom: float = ...,
    label: str = ...,
    use_line_collection: bool = ...,
    orientation: str = ...,
    data=...
) -> StemContainer: ...
def step(
    x: ArrayLike,
    y: ArrayLike,
    *args,
    where: Literal["pre", "post", "mid"] = ...,
    data=...,
    **kwargs
) -> list: ...
def streamplot(
    x,
    y,
    u,
    v,
    density: float = ...,
    linewidth: float = ...,
    color: Color = ...,
    cmap: Colormap = ...,
    norm: Normalize = ...,
    arrowsize: float = ...,
    arrowstyle: str = ...,
    minlength: float = ...,
    transform=...,
    zorder: int = ...,
    start_points=...,
    maxlength: float = ...,
    integration_direction: Literal["forward", "backward", "both"] = ...,
    broken_streamlines: bool = ...,
    *,
    data=...
) -> StreamplotSet: ...
def table(
    cellText=...,
    cellColours=...,
    cellLoc: Literal["left", "center", "right"] = ...,
    colWidths: list[float] = ...,
    rowLabels: list[str] = ...,
    rowColours: list[Color] = ...,
    rowLoc: Literal["left", "center", "right"] = ...,
    colLabels: list[str] = ...,
    colColours: list[Color] = ...,
    colLoc: Literal["left", "center", "right"] = ...,
    loc: str = ...,
    bbox: Bbox = ...,
    edges: Literal["open", "closed", "horizontal", "vertical"] = ...,
    **kwargs
) -> Table: ...
def text(x: float, y: float, s: str, fontdict: dict = ..., **kwargs) -> Text: ...
def tick_params(axis: Literal["x", "y", "both"] = ..., **kwargs): ...
def ticklabel_format(
    *,
    axis: Literal["x", "y", "both"] = ...,
    style: Literal["sci", "scientific", "plain"] = ...,
    scilimits=...,
    useOffset: bool | float = ...,
    useLocale: bool = ...,
    useMathText: bool = ...
): ...
def tricontour(*args, **kwargs) -> TriContourSet: ...
def tricontourf(*args, **kwargs) -> TriContourSet: ...
def tripcolor(
    *args,
    alpha=...,
    norm=...,
    cmap=...,
    vmin: float = ...,
    vmax: float = ...,
    shading: Literal["flat", "gouraud"] = ...,
    facecolors: ArrayLike = ...,
    **kwargs
): ...
def triplot(*args, **kwargs): ...
def violinplot(
    dataset: ArrayLike,
    positions: ArrayLike = ...,
    vert: bool = ...,
    widths: ArrayLike = ...,
    showmeans: bool = ...,
    showextrema: bool = ...,
    showmedians: bool = ...,
    quantiles: ArrayLike = ...,
    points: int = ...,
    bw_method: str | Scalar | Callable = ...,
    *,
    data=...
) -> dict: ...
def vlines(
    x: float | ArrayLike,
    ymin: float | ArrayLike,
    ymax: float | ArrayLike,
    colors: list[Color] = ...,
    linestyles: Literal["solid", "dashed", "dashdot", "dotted"] = ...,
    label: str = ...,
    *,
    data=...,
    **kwargs
) -> LineCollection: ...
def xcorr(
    x,
    y,
    normed: bool = ...,
    detrend: Callable = ...,
    usevlines: bool = ...,
    maxlags: int = ...,
    *,
    data=...,
    **kwargs
): ...
def sci(im): ...
def title(
    label: str,
    fontdict: dict = ...,
    loc: Literal["center", "left", "right"] = ...,
    pad: float = ...,
    *,
    y: float = ...,
    **kwargs
) -> Text: ...
def xlabel(
    xlabel: str,
    fontdict=...,
    labelpad: float = ...,
    *,
    loc: Literal["left", "center", "right"] = ...,
    **kwargs
): ...
def ylabel(
    ylabel: str,
    fontdict=...,
    labelpad: float = ...,
    *,
    loc: Literal["bottom", "center", "top"] = ...,
    **kwargs
): ...
def xscale(
    value: Literal["linear", "log", "symlog", "logit"] | ScaleBase, **kwargs
): ...
def yscale(
    value: Literal["linear", "log", "symlog", "logit"] | ScaleBase, **kwargs
): ...
def autumn(): ...
def bone(): ...
def cool(): ...
def copper(): ...
def flag(): ...
def gray(): ...
def hot(): ...
def hsv(): ...
def jet(): ...
def pink(): ...
def prism(): ...
def spring(): ...
def summer(): ...
def winter(): ...
def magma(): ...
def inferno(): ...
def plasma(): ...
def viridis(): ...
def nipy_spectral(): ...
