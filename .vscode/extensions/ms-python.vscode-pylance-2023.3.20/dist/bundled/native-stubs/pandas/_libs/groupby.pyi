# Python: 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)]
# Library: pandas, version: 1.2.4
# Module: pandas._libs.groupby, version: unspecified
import typing
import builtins as _mod_builtins

__doc__: typing.Any
__file__: str
__name__: str
__package__: str
def __pyx_unpickle_Enum() -> typing.Any:
    ...

__test__: dict
def _group_add() -> typing.Any:
    '\n    Only aggregates on axis=0\n    '
    ...

def _group_mean() -> typing.Any:
    ...

def _group_ohlc() -> typing.Any:
    '\n    Only aggregates on axis=0\n    '
    ...

def _group_prod() -> typing.Any:
    '\n    Only aggregates on axis=0\n    '
    ...

def _group_var() -> typing.Any:
    ...

_int64_max: int
def group_add_complex128() -> typing.Any:
    '\n    Only aggregates on axis=0\n    '
    ...

def group_add_complex64() -> typing.Any:
    '\n    Only aggregates on axis=0\n    '
    ...

def group_add_float32() -> typing.Any:
    '\n    Only aggregates on axis=0\n    '
    ...

def group_add_float64() -> typing.Any:
    '\n    Only aggregates on axis=0\n    '
    ...

def group_any_all() -> typing.Any:
    "\n    Aggregated boolean values to show truthfulness of group elements.\n\n    Parameters\n    ----------\n    out : array of values which this method will write its results to\n    labels : array containing unique label for each group, with its\n        ordering matching up to the corresponding record in `values`\n    values : array containing the truth value of each element\n    mask : array indicating whether a value is na or not\n    val_test : str {'any', 'all'}\n        String object dictating whether to use any or all truth testing\n    skipna : boolean\n        Flag to ignore nan values during truth testing\n\n    Notes\n    -----\n    This method modifies the `out` parameter rather than returning an object.\n    The returned values will either be 0 or 1 (False or True, respectively).\n    "
    ...

def group_cummax(out, values, labels, ngroups, is_datetimelike) -> typing.Any:
    '\n    Cumulative maximum of columns of `values`, in row groups `labels`.\n\n    Parameters\n    ----------\n    out : array\n        Array to store cummax in.\n    values : array\n        Values to take cummax of.\n    labels : int64 array\n        Labels to group by.\n    ngroups : int\n        Number of groups, larger than all entries of `labels`.\n    is_datetimelike : bool\n        True if `values` contains datetime-like entries.\n\n    Notes\n    -----\n    This method modifies the `out` parameter, rather than returning an object.\n    '
    ...

def group_cummin(out, values, labels, ngroups, is_datetimelike) -> typing.Any:
    '\n    Cumulative minimum of columns of `values`, in row groups `labels`.\n\n    Parameters\n    ----------\n    out : array\n        Array to store cummin in.\n    values : array\n        Values to take cummin of.\n    labels : int64 array\n        Labels to group by.\n    ngroups : int\n        Number of groups, larger than all entries of `labels`.\n    is_datetimelike : bool\n        True if `values` contains datetime-like entries.\n\n    Notes\n    -----\n    This method modifies the `out` parameter, rather than returning an object.\n    '
    ...

def group_cumprod_float64() -> typing.Any:
    '\n    Cumulative product of columns of `values`, in row groups `labels`.\n\n    Parameters\n    ----------\n    out : float64 array\n        Array to store cumprod in.\n    values : float64 array\n        Values to take cumprod of.\n    labels : int64 array\n        Labels to group by.\n    ngroups : int\n        Number of groups, larger than all entries of `labels`.\n    is_datetimelike : bool\n        Always false, `values` is never datetime-like.\n    skipna : bool\n        If true, ignore nans in `values`.\n\n    Notes\n    -----\n    This method modifies the `out` parameter, rather than returning an object.\n    '
    ...

def group_cumsum() -> typing.Any:
    '\n    Cumulative sum of columns of `values`, in row groups `labels`.\n\n    Parameters\n    ----------\n    out : array\n        Array to store cumsum in.\n    values : array\n        Values to take cumsum of.\n    labels : int64 array\n        Labels to group by.\n    ngroups : int\n        Number of groups, larger than all entries of `labels`.\n    is_datetimelike : bool\n        True if `values` contains datetime-like entries.\n    skipna : bool\n        If true, ignore nans in `values`.\n\n    Notes\n    -----\n    This method modifies the `out` parameter, rather than returning an object.\n    '
    ...

def group_fillna_indexer() -> typing.Any:
    "\n    Indexes how to fill values forwards or backwards within a group.\n\n    Parameters\n    ----------\n    out : array of int64_t values which this method will write its results to\n        Missing values will be written to with a value of -1\n    labels : array containing unique label for each group, with its ordering\n        matching up to the corresponding record in `values`\n    mask : array of int64_t values where a 1 indicates a missing value\n    direction : {'ffill', 'bfill'}\n        Direction for fill to be applied (forwards or backwards, respectively)\n    limit : Consecutive values to fill before stopping, or -1 for no limit\n    dropna : Flag to indicate if NaN groups should return all NaN values\n\n    Notes\n    -----\n    This method modifies the `out` parameter rather than returning an object\n    "
    ...

def group_last() -> typing.Any:
    '\n    Only aggregates on axis=0\n    '
    ...

def group_max() -> typing.Any:
    '\n    Only aggregates on axis=0\n    '
    ...

def group_mean_float32() -> typing.Any:
    ...

def group_mean_float64() -> typing.Any:
    ...

def group_median_float64() -> typing.Any:
    '\n    Only aggregates on axis=0\n    '
    ...

def group_min() -> typing.Any:
    '\n    Only aggregates on axis=0\n    '
    ...

def group_nth() -> typing.Any:
    '\n    Only aggregates on axis=0\n    '
    ...

def group_ohlc_float32() -> typing.Any:
    '\n    Only aggregates on axis=0\n    '
    ...

def group_ohlc_float64() -> typing.Any:
    '\n    Only aggregates on axis=0\n    '
    ...

def group_prod_float32() -> typing.Any:
    '\n    Only aggregates on axis=0\n    '
    ...

def group_prod_float64() -> typing.Any:
    '\n    Only aggregates on axis=0\n    '
    ...

def group_quantile(out, values, labels, mask, q, interpolation) -> typing.Any:
    '\n    Calculate the quantile per group.\n\n    Parameters\n    ----------\n    out : ndarray\n        Array of aggregated values that will be written to.\n    labels : ndarray\n        Array containing the unique group labels.\n    values : ndarray\n        Array containing the values to apply the function against.\n    q : float\n        The quantile value to search for.\n\n    Notes\n    -----\n    Rather than explicitly returning a value, this function modifies the\n    provided `out` parameter.\n    '
    ...

def group_rank() -> typing.Any:
    "\n    Provides the rank of values within each group.\n\n    Parameters\n    ----------\n    out : array of float64_t values which this method will write its results to\n    values : array of rank_t values to be ranked\n    labels : array containing unique label for each group, with its ordering\n        matching up to the corresponding record in `values`\n    ngroups : int\n        This parameter is not used, is needed to match signatures of other\n        groupby functions.\n    is_datetimelike : bool, default False\n        unused in this method but provided for call compatibility with other\n        Cython transformations\n    ties_method : {'average', 'min', 'max', 'first', 'dense'}, default\n        'average'\n        * average: average rank of group\n        * min: lowest rank in group\n        * max: highest rank in group\n        * first: ranks assigned in order they appear in the array\n        * dense: like 'min', but rank always increases by 1 between groups\n    ascending : boolean, default True\n        False for ranks by high (1) to low (N)\n        na_option : {'keep', 'top', 'bottom'}, default 'keep'\n    pct : boolean, default False\n        Compute percentage rank of data within each group\n    na_option : {'keep', 'top', 'bottom'}, default 'keep'\n        * keep: leave NA values where they are\n        * top: smallest rank if ascending\n        * bottom: smallest rank if descending\n\n    Notes\n    -----\n    This method modifies the `out` parameter rather than returning an object\n    "
    ...

def group_shift_indexer() -> typing.Any:
    ...

def group_var_float32() -> typing.Any:
    ...

def group_var_float64() -> typing.Any:
    ...

def groupsort_indexer() -> typing.Any:
    '\n    Compute a 1-d indexer.\n\n    The indexer is an ordering of the passed index,\n    ordered by the groups.\n\n    Parameters\n    ----------\n    index: int64 ndarray\n        Mappings from group -> position.\n    ngroups: int64\n        Number of groups.\n\n    Returns\n    -------\n    tuple\n        1-d indexer ordered by groups, group counts.\n\n    Notes\n    -----\n    This is a reverse of the label factorization process.\n    '
    ...

def take_2d_axis1_float64_float64() -> typing.Any:
    ...

tiebreakers: dict
def __getattr__(name) -> typing.Any:
    ...

