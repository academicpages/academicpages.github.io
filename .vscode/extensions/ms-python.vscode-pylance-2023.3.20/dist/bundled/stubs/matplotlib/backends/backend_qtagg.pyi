from .backend_agg import FigureCanvasAgg
from .backend_qt import FigureCanvasQT, _BackendQT

class FigureCanvasQTAgg(FigureCanvasAgg, FigureCanvasQT):
    def __init__(self, figure=...) -> None: ...
    def paintEvent(self, event)-> None: ...
    def print_figure(self, *args, **kwargs)-> None: ...

class _BackendQTAgg(_BackendQT):
    FigureCanvas = FigureCanvasQTAgg
