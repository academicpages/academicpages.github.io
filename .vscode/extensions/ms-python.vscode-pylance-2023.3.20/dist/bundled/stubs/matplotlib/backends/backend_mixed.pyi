from matplotlib.backend_bases import RendererBase
from matplotlib.figure import Figure
from matplotlib._typing import Scalar

class MixedModeRenderer:
    def __init__(
        self,
        figure: Figure,
        width: Scalar,
        height: Scalar,
        dpi: float,
        vector_renderer: RendererBase,
        raster_renderer_class: RendererBase|None = None,
        bbox_inches_restore=None,
    ) -> None: ...
    def __getattr__(self, attr: str): ...
    def start_rasterizing(self) -> None: ...
    def stop_rasterizing(self) -> None: ...
