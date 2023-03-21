# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: scipy, version: 1.6.2
# Module: scipy.cluster._vq, version: unspecified
import typing
import builtins as _mod_builtins

__doc__: str
__file__: str
__name__: str
__package__: str
__test__: dict
def update_cluster_means() -> typing.Any:
    '\n    The update-step of K-means. Calculate the mean of observations in each\n    cluster.\n\n    Parameters\n    ----------\n    obs : ndarray\n        The observation matrix. Each row is an observation. Its dtype must be\n        float32 or float64.\n    labels : ndarray\n        The label of each observation. Must be an 1d array.\n    nc : int\n        The number of centroids.\n\n    Returns\n    -------\n    cb : ndarray\n        The new code book.\n    has_members : ndarray\n        A boolean array indicating which clusters have members.\n\n    Notes\n    -----\n    The empty clusters will be set to all zeros and the corresponding elements\n    in `has_members` will be `False`. The upper level function should decide\n    how to deal with them.\n    '
    ...

def vq() -> typing.Any:
    '\n    Vector quantization ndarray wrapper. Only support float32 and float64.\n\n    Parameters\n    ----------\n    obs : ndarray\n        The observation matrix. Each row is an observation.\n    codes : ndarray\n        The code book matrix.\n\n    Notes\n    -----\n    The observation matrix and code book matrix should have same ndim and\n    same number of columns (features). Only 1-dimensional and 2-dimensional\n    arrays are supported.\n    '
    ...

def __getattr__(name) -> typing.Any:
    ...

