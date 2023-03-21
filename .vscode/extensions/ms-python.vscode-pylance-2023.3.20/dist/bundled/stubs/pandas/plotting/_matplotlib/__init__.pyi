from .boxplot import (
    boxplot as boxplot,
    boxplot_frame as boxplot_frame,
    boxplot_frame_groupby as boxplot_frame_groupby,
)
from .converter import (
    deregister as deregister,
    register as register,
)
from .hist import (
    hist_frame as hist_frame,
    hist_series as hist_series,
)
from .misc import (
    andrews_curves as andrews_curves,
    autocorrelation_plot as autocorrelation_plot,
    bootstrap_plot as bootstrap_plot,
    lag_plot as lag_plot,
    parallel_coordinates as parallel_coordinates,
    radviz as radviz,
    scatter_matrix as scatter_matrix,
)
from .tools import table as table

def plot(data, kind, **kwargs): ...
