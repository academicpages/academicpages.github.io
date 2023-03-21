from pandas.plotting._core import (
    PlotAccessor as PlotAccessor,
    boxplot as boxplot,
)
from pandas.plotting._misc import (
    andrews_curves as andrews_curves,
    autocorrelation_plot as autocorrelation_plot,
    bootstrap_plot as bootstrap_plot,
    deregister,
    lag_plot as lag_plot,
    parallel_coordinates as parallel_coordinates,
    plot_params as plot_params,
    radviz as radviz,
    register,
    scatter_matrix as scatter_matrix,
    table as table,
)

deregister_matplotlib_converters = deregister
register_matplotlib_converters = register
