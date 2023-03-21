# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: scipy, version: 1.6.2
# Module: scipy.stats._stats, version: unspecified
import typing
import builtins as _mod_builtins

__doc__: typing.Any
__file__: str
__name__: str
__package__: str
__pyx_capi__: dict
def __pyx_unpickle_Enum() -> typing.Any:
    ...

__test__: dict
def _center_distance_matrix() -> typing.Any:
    ...

def _kendall_dis() -> typing.Any:
    ...

def _local_correlations() -> typing.Any:
    ...

def _local_covariance() -> typing.Any:
    ...

def _rank_distance_matrix() -> typing.Any:
    ...

def _toint64() -> typing.Any:
    ...

def _transform_distance_matrix() -> typing.Any:
    ...

def _weightedrankedtau(x, y, rank, weigher, additive) -> typing.Any:
    ...

def gaussian_kernel_estimate() -> typing.Any:
    '\n    def gaussian_kernel_estimate(points, real[:, :] values, xi, precision)\n\n    Evaluate a multivariate Gaussian kernel estimate.\n\n    Parameters\n    ----------\n    points : array_like with shape (n, d)\n        Data points to estimate from in d dimenions.\n    values : real[:, :] with shape (n, p)\n        Multivariate values associated with the data points.\n    xi : array_like with shape (m, d)\n        Coordinates to evaluate the estimate at in d dimensions.\n    precision : array_like with shape (d, d)\n        Precision matrix for the Gaussian kernel.\n\n    Returns\n    -------\n    estimate : double[:, :] with shape (m, p)\n        Multivariate Gaussian kernel estimate evaluated at the input coordinates.\n    '
    ...

def geninvgauss_logpdf() -> typing.Any:
    ...

def von_mises_cdf() -> typing.Any:
    ...

def __getattr__(name) -> typing.Any:
    ...

