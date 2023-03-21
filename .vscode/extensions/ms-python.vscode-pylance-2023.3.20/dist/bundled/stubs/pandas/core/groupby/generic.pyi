from collections.abc import (
    Callable,
    Iterable,
    Iterator,
    Sequence,
)
from typing import (
    Any,
    Generic,
    Literal,
    NamedTuple,
    overload,
)

from matplotlib.axes import (
    Axes as PlotAxes,
    SubplotBase as AxesSubplot,
)
from pandas.core.frame import DataFrame
from pandas.core.generic import NDFrame
from pandas.core.groupby.groupby import (  # , get_groupby as get_groupby
    GroupBy as GroupBy,
)
from pandas.core.groupby.grouper import Grouper
from pandas.core.series import Series
from typing_extensions import TypeAlias

from pandas._typing import (
    S1,
    AggFuncTypeBase,
    AggFuncTypeFrame,
    AxisType,
    Level,
    ListLike,
    RandomState,
    Scalar,
)

AggScalar: TypeAlias = str | Callable[..., Any]
ScalarResult = ...

class NamedAgg(NamedTuple):
    column: str = ...
    aggfunc: AggScalar = ...

def generate_property(name: str, klass: type[NDFrame]): ...

class _SeriesGroupByScalar(SeriesGroupBy[S1]):
    def __iter__(self) -> Iterator[tuple[Scalar, Series]]: ...

class _SeriesGroupByNonScalar(SeriesGroupBy[S1]):
    def __iter__(self) -> Iterator[tuple[tuple, Series]]: ...

class SeriesGroupBy(GroupBy, Generic[S1]):
    def any(self, skipna: bool = ...) -> Series[bool]: ...
    def all(self, skipna: bool = ...) -> Series[bool]: ...
    def apply(self, func, *args, **kwargs) -> Series: ...
    @overload
    def aggregate(self, func: list[AggFuncTypeBase], *args, **kwargs) -> DataFrame: ...
    @overload
    def aggregate(self, func: AggFuncTypeBase, *args, **kwargs) -> Series: ...
    @overload
    def agg(self, func: list[AggFuncTypeBase], *args, **kwargs) -> DataFrame: ...
    @overload
    def agg(self, func: AggFuncTypeBase, *args, **kwargs) -> Series: ...
    def transform(self, func: Callable | str, *args, **kwargs) -> Series: ...
    def filter(self, func, dropna: bool = ..., *args, **kwargs): ...
    def nunique(self, dropna: bool = ...) -> Series: ...
    def describe(self, **kwargs) -> DataFrame: ...
    @overload
    def value_counts(
        self,
        normalize: Literal[False] = ...,
        sort: bool = ...,
        ascending: bool = ...,
        bins=...,
        dropna: bool = ...,
    ) -> Series[int]: ...
    @overload
    def value_counts(
        self,
        normalize: Literal[True],
        sort: bool = ...,
        ascending: bool = ...,
        bins=...,
        dropna: bool = ...,
    ) -> Series[float]: ...
    def count(self) -> Series[int]: ...
    def pct_change(
        self,
        periods: int = ...,
        fill_method: str = ...,
        limit=...,
        freq=...,
        axis: AxisType = ...,
    ) -> Series[float]: ...
    # Overrides and others from original pylance stubs
    @property
    def is_monotonic_increasing(self) -> bool: ...
    @property
    def is_monotonic_decreasing(self) -> bool: ...
    def bfill(self, limit: int | None = ...) -> Series[S1]: ...
    def cummax(self, axis: AxisType = ..., **kwargs) -> Series[S1]: ...
    def cummin(self, axis: AxisType = ..., **kwargs) -> Series[S1]: ...
    def cumprod(self, axis: AxisType = ..., **kwargs) -> Series[S1]: ...
    def cumsum(self, axis: AxisType = ..., **kwargs) -> Series[S1]: ...
    def ffill(self, limit: int | None = ...) -> Series[S1]: ...
    def first(self, **kwargs) -> Series[S1]: ...
    def head(self, n: int = ...) -> Series[S1]: ...
    def last(self, **kwargs) -> Series[S1]: ...
    def max(self, **kwargs) -> Series[S1]: ...
    def mean(self, **kwargs) -> Series[S1]: ...
    def median(self, **kwargs) -> Series[S1]: ...
    def min(self, **kwargs) -> Series[S1]: ...
    def nlargest(self, n: int = ..., keep: str = ...) -> Series[S1]: ...
    def nsmallest(self, n: int = ..., keep: str = ...) -> Series[S1]: ...
    def nth(self, n: int | Sequence[int], dropna: str | None = ...) -> Series[S1]: ...
    def sum(
        self,
        numeric_only: bool = ...,
        min_count: int = ...,
        engine=...,
        engine_kwargs=...,
    ) -> Series[S1]: ...
    def prod(self, numeric_only: bool = ..., min_count: int = ...) -> Series[S1]: ...
    def sem(self, ddof: int = ..., numeric_only: bool = ...) -> Series[float]: ...
    def std(self, ddof: int = ..., numeric_only: bool = ...) -> Series[float]: ...
    def var(self, ddof: int = ..., numeric_only: bool = ...) -> Series[float]: ...
    def tail(self, n: int = ...) -> Series[S1]: ...
    def unique(self) -> Series: ...
    def hist(
        self,
        by=...,
        ax: PlotAxes | None = ...,
        grid: bool = ...,
        xlabelsize: int | None = ...,
        xrot: float | None = ...,
        ylabelsize: int | None = ...,
        yrot: float | None = ...,
        figsize: tuple[float, float] | None = ...,
        bins: int | Sequence = ...,
        backend: str | None = ...,
        legend: bool = ...,
        **kwargs,
    ) -> AxesSubplot: ...
    def idxmax(self, axis: AxisType = ..., skipna: bool = ...) -> Series: ...
    def idxmin(self, axis: AxisType = ..., skipna: bool = ...) -> Series: ...

class _DataFrameGroupByScalar(DataFrameGroupBy):
    def __iter__(self) -> Iterator[tuple[Scalar, DataFrame]]: ...

class _DataFrameGroupByNonScalar(DataFrameGroupBy):
    def __iter__(self) -> Iterator[tuple[tuple, DataFrame]]: ...

class DataFrameGroupBy(GroupBy):
    def any(self, skipna: bool = ...) -> DataFrame: ...
    def all(self, skipna: bool = ...) -> DataFrame: ...
    # error: Overload 3 for "apply" will never be used because its parameters overlap overload 1
    @overload
    def apply(  # type: ignore[misc]
        self, func: Callable[[DataFrame], Scalar | list | dict], *args, **kwargs
    ) -> Series: ...
    @overload
    def apply(
        self, func: Callable[[DataFrame], Series | DataFrame], *args, **kwargs
    ) -> DataFrame: ...
    @overload
    def apply(  # pyright: ignore[reportOverlappingOverload]
        self, func: Callable[[Iterable], float], *args, **kwargs
    ) -> DataFrame: ...
    def aggregate(self, arg: AggFuncTypeFrame = ..., *args, **kwargs) -> DataFrame:
        """
Aggregate using one or more operations over the specified axis.

Parameters
----------
func : function, str, list or dict
    Function to use for aggregating the data. If a function, must either
    work when passed a DataFrame or when passed to DataFrame.apply.

    Accepted combinations are:

    - function
    - string function name
    - list of functions and/or function names, e.g. ``[np.sum, 'mean']``
    - dict of axis labels -> functions, function names or list of such.

    Can also accept a Numba JIT function with
    ``engine='numba'`` specified. Only passing a single function is supported
    with this engine.

    If the ``'numba'`` engine is chosen, the function must be
    a user defined function with ``values`` and ``index`` as the
    first and second arguments respectively in the function signature.
    Each group's index will be passed to the user defined function
    and optionally available for use.

    .. versionchanged:: 1.1.0
*args
    Positional arguments to pass to func.
engine : str, default None
    * ``'cython'`` : Runs the function through C-extensions from cython.
    * ``'numba'`` : Runs the function through JIT compiled code from numba.
    * ``None`` : Defaults to ``'cython'`` or globally setting ``compute.use_numba``

    .. versionadded:: 1.1.0
engine_kwargs : dict, default None
    * For ``'cython'`` engine, there are no accepted ``engine_kwargs``
    * For ``'numba'`` engine, the engine can accept ``nopython``, ``nogil``
      and ``parallel`` dictionary keys. The values must either be ``True`` or
      ``False``. The default ``engine_kwargs`` for the ``'numba'`` engine is
      ``{'nopython': True, 'nogil': False, 'parallel': False}`` and will be
      applied to the function

    .. versionadded:: 1.1.0
**kwargs
    Keyword arguments to be passed into func.

Returns
-------
DataFrame

See Also
--------
DataFrame.groupby.apply : Apply function func group-wise
    and combine the results together.
DataFrame.groupby.transform : Aggregate using one or more
    operations over the specified axis.
DataFrame.aggregate : Transforms the Series on each group
    based on the given function.

Notes
-----
When using ``engine='numba'``, there will be no "fall back" behavior internally.
The group data and group index will be passed as numpy arrays to the JITed
user defined function, and no alternative execution attempts will be tried.

Functions that mutate the passed object can produce unexpected
behavior or errors and are not supported. See :ref:`gotchas.udf-mutation`
for more details.

.. versionchanged:: 1.3.0

    The resulting dtype will reflect the return value of the passed ``func``,
    see the examples below.

Examples
--------
>>> df = pd.DataFrame(
...     {
...         "A": [1, 1, 2, 2],
...         "B": [1, 2, 3, 4],
...         "C": [0.362838, 0.227877, 1.267767, -0.562860],
...     }
... )

>>> df
   A  B         C
0  1  1  0.362838
1  1  2  0.227877
2  2  3  1.267767
3  2  4 -0.562860

The aggregation is for each column.

>>> df.groupby('A').agg('min')
   B         C
A
1  1  0.227877
2  3 -0.562860

Multiple aggregations

>>> df.groupby('A').agg(['min', 'max'])
    B             C
  min max       min       max
A
1   1   2  0.227877  0.362838
2   3   4 -0.562860  1.267767

Select a column for aggregation

>>> df.groupby('A').B.agg(['min', 'max'])
   min  max
A
1    1    2
2    3    4

User-defined function for aggregation

>>> df.groupby('A').agg(lambda x: sum(x) + 2)
    B          C
A
1       5       2.590715
2       9       2.704907

Different aggregations per column

>>> df.groupby('A').agg({'B': ['min', 'max'], 'C': 'sum'})
    B             C
  min max       sum
A
1   1   2  0.590715
2   3   4  0.704907

To control the output names with different aggregations per column,
pandas supports "named aggregation"

>>> df.groupby("A").agg(
...     b_min=pd.NamedAgg(column="B", aggfunc="min"),
...     c_sum=pd.NamedAgg(column="C", aggfunc="sum"))
   b_min     c_sum
A
1      1  0.590715
2      3  0.704907

- The keywords are the *output* column names
- The values are tuples whose first element is the column to select
  and the second element is the aggregation to apply to that column.
  Pandas provides the ``pandas.NamedAgg`` namedtuple with the fields
  ``['column', 'aggfunc']`` to make it clearer what the arguments are.
  As usual, the aggregation can be a callable or a string alias.

See :ref:`groupby.aggregate.named` for more.

.. versionchanged:: 1.3.0

    The resulting dtype will reflect the return value of the aggregating function.

>>> df.groupby("A")[["B"]].agg(lambda x: x.astype(float).min())
      B
A
1   1.0
2   3.0
        """
        pass
    agg = aggregate
    def transform(self, func: Callable | str, *args, **kwargs) -> DataFrame: ...
    def filter(
        self, func: Callable, dropna: bool = ..., *args, **kwargs
    ) -> DataFrame: ...
    def nunique(self, dropna: bool = ...) -> DataFrame: ...
    @overload
    def __getitem__(self, item: str) -> SeriesGroupBy: ...
    @overload
    def __getitem__(self, item: list[str]) -> DataFrameGroupBy: ...
    def count(self) -> DataFrame: ...
    def boxplot(
        self,
        grouped: DataFrame,
        subplots: bool = ...,
        column: str | Sequence | None = ...,
        fontsize: float | str = ...,
        rot: float = ...,
        grid: bool = ...,
        ax: PlotAxes | None = ...,
        figsize: tuple[float, float] | None = ...,
        layout: tuple[int, int] | None = ...,
        sharex: bool = ...,
        sharey: bool = ...,
        bins: int | Sequence = ...,
        backend: str | None = ...,
        **kwargs,
    ) -> AxesSubplot | Sequence[AxesSubplot]:
        """
Make box plots from DataFrameGroupBy data.

Parameters
----------
grouped : Grouped DataFrame
subplots : bool
    * ``False`` - no subplots will be used
    * ``True`` - create a subplot for each group.

column : column name or list of names, or vector
    Can be any valid input to groupby.
fontsize : int or str
rot : label rotation angle
grid : Setting this to True will show the grid
ax : Matplotlib axis object, default None
figsize : A tuple (width, height) in inches
layout : tuple (optional)
    The layout of the plot: (rows, columns).
sharex : bool, default False
    Whether x-axes will be shared among subplots.
sharey : bool, default True
    Whether y-axes will be shared among subplots.
backend : str, default None
    Backend to use instead of the backend specified in the option
    ``plotting.backend``. For instance, 'matplotlib'. Alternatively, to
    specify the ``plotting.backend`` for the whole session, set
    ``pd.options.plotting.backend``.

    .. versionadded:: 1.0.0

**kwargs
    All other plotting keyword arguments to be passed to
    matplotlib's boxplot function.

Returns
-------
dict of key/value = group key/DataFrame.boxplot return value
or DataFrame.boxplot return value in case subplots=figures=False

Examples
--------
You can create boxplots for grouped data and show them as separate subplots:

.. plot::
    :context: close-figs

    >>> import itertools
    >>> tuples = [t for t in itertools.product(range(1000), range(4))]
    >>> index = pd.MultiIndex.from_tuples(tuples, names=['lvl0', 'lvl1'])
    >>> data = np.random.randn(len(index),4)
    >>> df = pd.DataFrame(data, columns=list('ABCD'), index=index)
    >>> grouped = df.groupby(level='lvl1')
    >>> grouped.boxplot(rot=45, fontsize=12, figsize=(8,10))  # doctest: +SKIP

The ``subplots=False`` option shows the boxplots in a single figure.

.. plot::
    :context: close-figs

    >>> grouped.boxplot(subplots=False, rot=45, fontsize=12)  # doctest: +SKIP
        """
        pass
    # Overrides and others from original pylance stubs
    # These are "properties" but properties can't have all these arguments?!
    def corr(self, method: str | Callable, min_periods: int = ...) -> DataFrame: ...
    def cov(self, min_periods: int = ...) -> DataFrame: ...
    def diff(self, periods: int = ..., axis: AxisType = ...) -> DataFrame: ...
    def bfill(self, limit: int | None = ...) -> DataFrame: ...
    def corrwith(
        self,
        other: DataFrame,
        axis: AxisType = ...,
        drop: bool = ...,
        method: str = ...,
    ) -> Series: ...
    def cummax(
        self, axis: AxisType = ..., numeric_only: bool = ..., **kwargs
    ) -> DataFrame: ...
    def cummin(
        self, axis: AxisType = ..., numeric_only: bool = ..., **kwargs
    ) -> DataFrame: ...
    def cumprod(self, axis: AxisType = ..., **kwargs) -> DataFrame: ...
    def cumsum(self, axis: AxisType = ..., **kwargs) -> DataFrame: ...
    def describe(self, **kwargs) -> DataFrame: ...
    def ffill(self, limit: int | None = ...) -> DataFrame: ...
    @overload
    def fillna(
        self,
        value,
        method: str | None = ...,
        axis: AxisType = ...,
        limit: int | None = ...,
        downcast: dict | None = ...,
        *,
        inplace: Literal[True],
    ) -> None:
        """
Fill NA/NaN values using the specified method.

Parameters
----------
value : scalar, dict, Series, or DataFrame
    Value to use to fill holes (e.g. 0), alternately a
    dict/Series/DataFrame of values specifying which value to use for
    each index (for a Series) or column (for a DataFrame).  Values not
    in the dict/Series/DataFrame will not be filled. This value cannot
    be a list.
method : {'backfill', 'bfill', 'pad', 'ffill', None}, default None
    Method to use for filling holes in reindexed Series
    pad / ffill: propagate last valid observation forward to next valid
    backfill / bfill: use next valid observation to fill gap.
axis : {0 or 'index', 1 or 'columns'}
    Axis along which to fill missing values. For `Series`
    this parameter is unused and defaults to 0.
inplace : bool, default False
    If True, fill in-place. Note: this will modify any
    other views on this object (e.g., a no-copy slice for a column in a
    DataFrame).
limit : int, default None
    If method is specified, this is the maximum number of consecutive
    NaN values to forward/backward fill. In other words, if there is
    a gap with more than this number of consecutive NaNs, it will only
    be partially filled. If method is not specified, this is the
    maximum number of entries along the entire axis where NaNs will be
    filled. Must be greater than 0 if not None.
downcast : dict, default is None
    A dict of item->dtype of what to downcast if possible,
    or the string 'infer' which will try to downcast to an appropriate
    equal type (e.g. float64 to int64 if possible).

Returns
-------
DataFrame or None
    Object with missing values filled or None if ``inplace=True``.

See Also
--------
interpolate : Fill NaN values using interpolation.
reindex : Conform object to new index.
asfreq : Convert TimeSeries to specified frequency.

Examples
--------
>>> df = pd.DataFrame([[np.nan, 2, np.nan, 0],
...                    [3, 4, np.nan, 1],
...                    [np.nan, np.nan, np.nan, np.nan],
...                    [np.nan, 3, np.nan, 4]],
...                   columns=list("ABCD"))
>>> df
     A    B   C    D
0  NaN  2.0 NaN  0.0
1  3.0  4.0 NaN  1.0
2  NaN  NaN NaN  NaN
3  NaN  3.0 NaN  4.0

Replace all NaN elements with 0s.

>>> df.fillna(0)
     A    B    C    D
0  0.0  2.0  0.0  0.0
1  3.0  4.0  0.0  1.0
2  0.0  0.0  0.0  0.0
3  0.0  3.0  0.0  4.0

We can also propagate non-null values forward or backward.

>>> df.fillna(method="ffill")
     A    B   C    D
0  NaN  2.0 NaN  0.0
1  3.0  4.0 NaN  1.0
2  3.0  4.0 NaN  1.0
3  3.0  3.0 NaN  4.0

Replace all NaN elements in column 'A', 'B', 'C', and 'D', with 0, 1,
2, and 3 respectively.

>>> values = {"A": 0, "B": 1, "C": 2, "D": 3}
>>> df.fillna(value=values)
     A    B    C    D
0  0.0  2.0  2.0  0.0
1  3.0  4.0  2.0  1.0
2  0.0  1.0  2.0  3.0
3  0.0  3.0  2.0  4.0

Only replace the first NaN element.

>>> df.fillna(value=values, limit=1)
     A    B    C    D
0  0.0  2.0  2.0  0.0
1  3.0  4.0  NaN  1.0
2  NaN  1.0  NaN  3.0
3  NaN  3.0  NaN  4.0

When filling using a DataFrame, replacement happens along
the same column names and same indices

>>> df2 = pd.DataFrame(np.zeros((4, 4)), columns=list("ABCE"))
>>> df.fillna(df2)
     A    B    C    D
0  0.0  2.0  0.0  0.0
1  3.0  4.0  0.0  1.0
2  0.0  0.0  0.0  NaN
3  0.0  3.0  0.0  4.0

Note that column D is not affected since it is not present in df2.
        """
        pass
    @overload
    def fillna(
        self,
        value,
        method: str | None = ...,
        axis: AxisType = ...,
        limit: int | None = ...,
        downcast: dict | None = ...,
        *,
        inplace: Literal[False],
    ) -> DataFrame: ...
    @overload
    def fillna(
        self,
        value,
        method: str | None = ...,
        axis: AxisType = ...,
        inplace: bool = ...,
        limit: int | None = ...,
        downcast: dict | None = ...,
    ) -> DataFrame | None: ...
    def first(self, **kwargs) -> DataFrame: ...
    def head(self, n: int = ...) -> DataFrame: ...
    def hist(
        self,
        data: DataFrame,
        column: str | Sequence | None = ...,
        by=...,
        grid: bool = ...,
        xlabelsize: int | None = ...,
        xrot: float | None = ...,
        ylabelsize: int | None = ...,
        yrot: float | None = ...,
        ax: PlotAxes | None = ...,
        sharex: bool = ...,
        sharey: bool = ...,
        figsize: tuple[float, float] | None = ...,
        layout: tuple[int, int] | None = ...,
        bins: int | Sequence = ...,
        backend: str | None = ...,
        **kwargs,
    ) -> AxesSubplot | Sequence[AxesSubplot]:
        """
Make a histogram of the DataFrame's columns.

A `histogram`_ is a representation of the distribution of data.
This function calls :meth:`matplotlib.pyplot.hist`, on each series in
the DataFrame, resulting in one histogram per column.

.. _histogram: https://en.wikipedia.org/wiki/Histogram

Parameters
----------
data : DataFrame
    The pandas object holding the data.
column : str or sequence, optional
    If passed, will be used to limit data to a subset of columns.
by : object, optional
    If passed, then used to form histograms for separate groups.
grid : bool, default True
    Whether to show axis grid lines.
xlabelsize : int, default None
    If specified changes the x-axis label size.
xrot : float, default None
    Rotation of x axis labels. For example, a value of 90 displays the
    x labels rotated 90 degrees clockwise.
ylabelsize : int, default None
    If specified changes the y-axis label size.
yrot : float, default None
    Rotation of y axis labels. For example, a value of 90 displays the
    y labels rotated 90 degrees clockwise.
ax : Matplotlib axes object, default None
    The axes to plot the histogram on.
sharex : bool, default True if ax is None else False
    In case subplots=True, share x axis and set some x axis labels to
    invisible; defaults to True if ax is None otherwise False if an ax
    is passed in.
    Note that passing in both an ax and sharex=True will alter all x axis
    labels for all subplots in a figure.
sharey : bool, default False
    In case subplots=True, share y axis and set some y axis labels to
    invisible.
figsize : tuple, optional
    The size in inches of the figure to create. Uses the value in
    `matplotlib.rcParams` by default.
layout : tuple, optional
    Tuple of (rows, columns) for the layout of the histograms.
bins : int or sequence, default 10
    Number of histogram bins to be used. If an integer is given, bins + 1
    bin edges are calculated and returned. If bins is a sequence, gives
    bin edges, including left edge of first bin and right edge of last
    bin. In this case, bins is returned unmodified.

backend : str, default None
    Backend to use instead of the backend specified in the option
    ``plotting.backend``. For instance, 'matplotlib'. Alternatively, to
    specify the ``plotting.backend`` for the whole session, set
    ``pd.options.plotting.backend``.

    .. versionadded:: 1.0.0

legend : bool, default False
    Whether to show the legend.

    .. versionadded:: 1.1.0

**kwargs
    All other plotting keyword arguments to be passed to
    :meth:`matplotlib.pyplot.hist`.

Returns
-------
matplotlib.AxesSubplot or numpy.ndarray of them

See Also
--------
matplotlib.pyplot.hist : Plot a histogram using matplotlib.

Examples
--------
This example draws a histogram based on the length and width of
some animals, displayed in three bins

.. plot::
    :context: close-figs

    >>> df = pd.DataFrame({
    ...     'length': [1.5, 0.5, 1.2, 0.9, 3],
    ...     'width': [0.7, 0.2, 0.15, 0.2, 1.1]
    ...     }, index=['pig', 'rabbit', 'duck', 'chicken', 'horse'])
    >>> hist = df.hist(bins=3)
        """
        pass
    def idxmax(
        self, axis: AxisType = ..., skipna: bool = ..., numeric_only: bool = ...
    ) -> DataFrame:
        """
Return index of first occurrence of maximum over requested axis.

NA/null values are excluded.

Parameters
----------
axis : {0 or 'index', 1 or 'columns'}, default 0
    The axis to use. 0 or 'index' for row-wise, 1 or 'columns' for column-wise.
skipna : bool, default True
    Exclude NA/null values. If an entire row/column is NA, the result
    will be NA.
numeric_only : bool, default True for axis=0, False for axis=1
    Include only `float`, `int` or `boolean` data.

    .. versionadded:: 1.5.0

Returns
-------
Series
    Indexes of maxima along the specified axis.

Raises
------
ValueError
    * If the row/column is empty

See Also
--------
Series.idxmax : Return index of the maximum element.

Notes
-----
This method is the DataFrame version of ``ndarray.argmax``.

Examples
--------
Consider a dataset containing food consumption in Argentina.

>>> df = pd.DataFrame({'consumption': [10.51, 103.11, 55.48],
...                    'co2_emissions': [37.2, 19.66, 1712]},
...                    index=['Pork', 'Wheat Products', 'Beef'])

>>> df
                consumption  co2_emissions
Pork                  10.51         37.20
Wheat Products       103.11         19.66
Beef                  55.48       1712.00

By default, it returns the index for the maximum value in each column.

>>> df.idxmax()
consumption     Wheat Products
co2_emissions             Beef
dtype: object

To return the index for the maximum value in each row, use ``axis="columns"``.

>>> df.idxmax(axis="columns")
Pork              co2_emissions
Wheat Products     consumption
Beef              co2_emissions
dtype: object
        """
        pass
    def idxmin(
        self, axis: AxisType = ..., skipna: bool = ..., numeric_only: bool = ...
    ) -> DataFrame:
        """
Return index of first occurrence of minimum over requested axis.

NA/null values are excluded.

Parameters
----------
axis : {0 or 'index', 1 or 'columns'}, default 0
    The axis to use. 0 or 'index' for row-wise, 1 or 'columns' for column-wise.
skipna : bool, default True
    Exclude NA/null values. If an entire row/column is NA, the result
    will be NA.
numeric_only : bool, default True for axis=0, False for axis=1
    Include only `float`, `int` or `boolean` data.

    .. versionadded:: 1.5.0

Returns
-------
Series
    Indexes of minima along the specified axis.

Raises
------
ValueError
    * If the row/column is empty

See Also
--------
Series.idxmin : Return index of the minimum element.

Notes
-----
This method is the DataFrame version of ``ndarray.argmin``.

Examples
--------
Consider a dataset containing food consumption in Argentina.

>>> df = pd.DataFrame({'consumption': [10.51, 103.11, 55.48],
...                    'co2_emissions': [37.2, 19.66, 1712]},
...                    index=['Pork', 'Wheat Products', 'Beef'])

>>> df
                consumption  co2_emissions
Pork                  10.51         37.20
Wheat Products       103.11         19.66
Beef                  55.48       1712.00

By default, it returns the index for the minimum value in each column.

>>> df.idxmin()
consumption                Pork
co2_emissions    Wheat Products
dtype: object

To return the index for the minimum value in each row, use ``axis="columns"``.

>>> df.idxmin(axis="columns")
Pork                consumption
Wheat Products    co2_emissions
Beef                consumption
dtype: object
        """
        pass
    def last(self, **kwargs) -> DataFrame: ...
    def max(self, **kwargs) -> DataFrame: ...
    def mean(self, **kwargs) -> DataFrame: ...
    def median(self, **kwargs) -> DataFrame: ...
    def min(self, **kwargs) -> DataFrame: ...
    def nth(self, n: int | Sequence[int], dropna: str | None = ...) -> DataFrame: ...
    def pct_change(
        self,
        periods: int = ...,
        fill_method: str = ...,
        limit=...,
        freq=...,
        axis: AxisType = ...,
    ) -> DataFrame: ...
    def prod(self, numeric_only: bool = ..., min_count: int = ...) -> DataFrame: ...
    def quantile(
        self, q: float = ..., interpolation: str = ..., numeric_only: bool = ...
    ) -> DataFrame: ...
    def resample(self, rule, *args, **kwargs) -> Grouper: ...
    def sample(
        self,
        n: int | None = ...,
        frac: float | None = ...,
        replace: bool = ...,
        weights: ListLike | None = ...,
        random_state: RandomState | None = ...,
    ) -> DataFrame: ...
    def sem(self, ddof: int = ..., numeric_only: bool = ...) -> DataFrame: ...
    def shift(
        self,
        periods: int = ...,
        freq: str = ...,
        axis: AxisType = ...,
        fill_value=...,
    ) -> DataFrame: ...
    @overload
    def skew(
        self,
        axis: AxisType = ...,
        skipna: bool = ...,
        numeric_only: bool = ...,
        *,
        level: Level,
        **kwargs,
    ) -> DataFrame:
        """
Return unbiased skew over requested axis.

Normalized by N-1.

Parameters
----------
axis : {index (0), columns (1)}
    Axis for the function to be applied on.
    For `Series` this parameter is unused and defaults to 0.
skipna : bool, default True
    Exclude NA/null values when computing the result.
level : int or level name, default None
    If the axis is a MultiIndex (hierarchical), count along a
    particular level, collapsing into a Series.

    .. deprecated:: 1.3.0
        The level keyword is deprecated. Use groupby instead.
numeric_only : bool, default None
    Include only float, int, boolean columns. If None, will attempt to use
    everything, then use only numeric data. Not implemented for Series.

    .. deprecated:: 1.5.0
        Specifying ``numeric_only=None`` is deprecated. The default value will be
        ``False`` in a future version of pandas.

**kwargs
    Additional keyword arguments to be passed to the function.

Returns
-------
Series or DataFrame (if level specified)
        """
        pass
    @overload
    def skew(
        self,
        axis: AxisType = ...,
        skipna: bool = ...,
        level: None = ...,
        numeric_only: bool = ...,
        **kwargs,
    ) -> Series: ...
    def std(self, ddof: int = ..., numeric_only: bool = ...) -> DataFrame: ...
    def sum(
        self,
        numeric_only: bool = ...,
        min_count: int = ...,
        engine=...,
        engine_kwargs=...,
    ) -> DataFrame: ...
    def tail(self, n: int = ...) -> DataFrame: ...
    def take(self, indices: Sequence, axis: AxisType = ..., **kwargs) -> DataFrame:
        """
Return the elements in the given *positional* indices along an axis.

This means that we are not indexing according to actual values in
the index attribute of the object. We are indexing according to the
actual position of the element in the object.

Parameters
----------
indices : array-like
    An array of ints indicating which positions to take.
axis : {0 or 'index', 1 or 'columns', None}, default 0
    The axis on which to select elements. ``0`` means that we are
    selecting rows, ``1`` means that we are selecting columns.
    For `Series` this parameter is unused and defaults to 0.
is_copy : bool
    Before pandas 1.0, ``is_copy=False`` can be specified to ensure
    that the return value is an actual copy. Starting with pandas 1.0,
    ``take`` always returns a copy, and the keyword is therefore
    deprecated.

    .. deprecated:: 1.0.0
**kwargs
    For compatibility with :meth:`numpy.take`. Has no effect on the
    output.

Returns
-------
taken : same type as caller
    An array-like containing the elements taken from the object.

See Also
--------
DataFrame.loc : Select a subset of a DataFrame by labels.
DataFrame.iloc : Select a subset of a DataFrame by positions.
numpy.take : Take elements from an array along an axis.

Examples
--------
>>> df = pd.DataFrame([('falcon', 'bird', 389.0),
...                    ('parrot', 'bird', 24.0),
...                    ('lion', 'mammal', 80.5),
...                    ('monkey', 'mammal', np.nan)],
...                   columns=['name', 'class', 'max_speed'],
...                   index=[0, 2, 3, 1])
>>> df
     name   class  max_speed
0  falcon    bird      389.0
2  parrot    bird       24.0
3    lion  mammal       80.5
1  monkey  mammal        NaN

Take elements at positions 0 and 3 along the axis 0 (default).

Note how the actual indices selected (0 and 1) do not correspond to
our selected indices 0 and 3. That's because we are selecting the 0th
and 3rd rows, not rows whose indices equal 0 and 3.

>>> df.take([0, 3])
     name   class  max_speed
0  falcon    bird      389.0
1  monkey  mammal        NaN

Take elements at indices 1 and 2 along the axis 1 (column selection).

>>> df.take([1, 2], axis=1)
    class  max_speed
0    bird      389.0
2    bird       24.0
3  mammal       80.5
1  mammal        NaN

We may take elements using negative integers for positive indices,
starting from the end of the object, just like with Python lists.

>>> df.take([-1, -2])
     name   class  max_speed
1  monkey  mammal        NaN
3    lion  mammal       80.5
        """
        pass
    def tshift(self, periods: int, freq=..., axis: AxisType = ...) -> DataFrame: ...
    def var(self, ddof: int = ..., numeric_only: bool = ...) -> DataFrame: ...
    @overload
    def value_counts(
        self,
        subset: ListLike | None = ...,
        normalize: Literal[False] = ...,
        sort: bool = ...,
        ascending: bool = ...,
        dropna: bool = ...,
    ) -> Series[int]: ...
    @overload
    def value_counts(
        self,
        subset: ListLike | None,
        normalize: Literal[True],
        sort: bool = ...,
        ascending: bool = ...,
        dropna: bool = ...,
    ) -> Series[float]: ...
    def __getattr__(self, name: str) -> SeriesGroupBy: ...
