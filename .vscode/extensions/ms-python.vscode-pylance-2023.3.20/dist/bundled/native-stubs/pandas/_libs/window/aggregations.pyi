# Python: 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)]
# Library: pandas, version: 1.2.4
# Module: pandas._libs.window.aggregations, version: unspecified
import typing
import builtins as _mod_builtins

__doc__: typing.Any
__file__: str
__name__: str
__package__: str
def __pyx_unpickle_Enum() -> typing.Any:
    ...

__test__: dict
def ewma() -> typing.Any:
    '\n    Compute exponentially-weighted moving average using center-of-mass.\n\n    Parameters\n    ----------\n    vals : ndarray (float64 type)\n    start: ndarray (int64 type)\n    end: ndarray (int64 type)\n    minp : int\n    com : float64\n    adjust : int\n    ignore_na : bool\n\n    Returns\n    -------\n    ndarray\n    '
    ...

def ewma_time() -> typing.Any:
    '\n    Compute exponentially-weighted moving average using halflife and time\n    distances.\n\n    Parameters\n    ----------\n    vals : ndarray[float_64]\n    start: ndarray[int_64]\n    end: ndarray[int_64]\n    minp : int\n    times : ndarray[int64]\n    halflife : int64\n\n    Returns\n    -------\n    ndarray\n    '
    ...

def ewmcov() -> typing.Any:
    '\n    Compute exponentially-weighted moving variance using center-of-mass.\n\n    Parameters\n    ----------\n    input_x : ndarray (float64 type)\n    start: ndarray (int64 type)\n    end: ndarray (int64 type)\n    minp : int\n    input_y : ndarray (float64 type)\n    com : float64\n    adjust : int\n    ignore_na : bool\n    bias : int\n\n    Returns\n    -------\n    ndarray\n    '
    ...

interpolation_types: dict
def is_monotonic(arr, timelike) -> typing.Any:
    '\n    Returns\n    -------\n    tuple\n        is_monotonic_inc : bool\n        is_monotonic_dec : bool\n        is_unique : bool\n    '
    ...

def roll_apply() -> typing.Any:
    ...

def roll_kurt() -> typing.Any:
    ...

def roll_max() -> typing.Any:
    "\n    Moving max of 1d array of any numeric type along axis=0 ignoring NaNs.\n\n    Parameters\n    ----------\n    values : np.ndarray[np.float64]\n    window : int, size of rolling window\n    minp : if number of observations in window\n          is below this, output a NaN\n    index : ndarray, optional\n       index for window computation\n    closed : 'right', 'left', 'both', 'neither'\n            make the interval closed on the right, left,\n            both or neither endpoints\n    "
    ...

def roll_mean() -> typing.Any:
    ...

def roll_median_c() -> typing.Any:
    ...

def roll_min() -> typing.Any:
    '\n    Moving min of 1d array of any numeric type along axis=0 ignoring NaNs.\n\n    Parameters\n    ----------\n    values : np.ndarray[np.float64]\n    window : int, size of rolling window\n    minp : if number of observations in window\n          is below this, output a NaN\n    index : ndarray, optional\n       index for window computation\n    '
    ...

def roll_quantile() -> typing.Any:
    '\n    O(N log(window)) implementation using skip list\n    '
    ...

def roll_skew() -> typing.Any:
    ...

def roll_sum() -> typing.Any:
    ...

def roll_var() -> typing.Any:
    "\n    Numerically stable implementation using Welford's method.\n    "
    ...

def roll_weighted_mean() -> typing.Any:
    ...

def roll_weighted_sum() -> typing.Any:
    ...

def roll_weighted_var() -> typing.Any:
    "\n    Calculates weighted rolling variance using West's online algorithm.\n\n    Paper: https://dl.acm.org/citation.cfm?id=359153\n\n    Parameters\n    ----------\n    values: float64_t[:]\n        values to roll window over\n    weights: float64_t[:]\n        array of weights whose length is window size\n    minp: int64_t\n        minimum number of observations to calculate\n        variance of a window\n    ddof: unsigned int\n         the divisor used in variance calculations\n         is the window size - ddof\n\n    Returns\n    -------\n    output: float64_t[:]\n        weighted variances of windows\n    "
    ...

def __getattr__(name) -> typing.Any:
    ...

