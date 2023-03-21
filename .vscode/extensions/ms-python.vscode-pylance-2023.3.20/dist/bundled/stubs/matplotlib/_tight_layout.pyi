from typing import Sequence
from .gridspec import SubplotSpec
from .backend_bases import RendererBase
from .figure import Figure
from .axes import Axes, SubplotBase

def auto_adjust_subplotpars(
    fig,
    renderer,
    nrows_ncols: tuple[int, int],
    num1num2_list: Sequence[tuple[int, int]],
    subplot_list: Sequence[SubplotBase],
    ax_bbox_list=None,
    pad: float = 1.08,
    h_pad: float|None = None,
    w_pad: float|None = None,
    rect: tuple[float, float, float, float]|None = None,
) -> dict | None: ...
def get_renderer(fig: Figure) -> RendererBase: ...
def get_subplotspec_list(axes_list, grid_spec=None) -> list[SubplotSpec]: ...
def get_tight_layout_figure(
    fig: Figure,
    axes_list: list[Axes],
    subplotspec_list: list,
    renderer: RendererBase,
    pad: float = 1.08,
    h_pad: float|None = None,
    w_pad: float|None = None,
    rect: tuple[float, float, float, float]|None = None,
) -> SubplotSpec | None: ...
