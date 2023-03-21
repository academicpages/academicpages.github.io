from collections.abc import Sequence
from typing import overload

import numpy as np
from pandas import (
    Categorical,
    CategoricalIndex,
    Index,
    IntervalIndex,
    PeriodIndex,
    Series,
)
from pandas.api.extensions import ExtensionArray

from pandas._typing import (
    AnyArrayLike,
    AxisInt,
    IntervalT,
    TakeIndexer,
)

# These are type: ignored because the Index types overlap due to inheritance but indices
# with extension types return the same type while standard type return ndarray

@overload
def unique(values: PeriodIndex) -> PeriodIndex: ...  # type: ignore[misc] # pyright: ignore[reportOverlappingOverload]
@overload
def unique(values: CategoricalIndex) -> CategoricalIndex: ...  # type: ignore[misc]
@overload
def unique(values: IntervalIndex[IntervalT]) -> IntervalIndex[IntervalT]: ...  # type: ignore[misc]
@overload
def unique(values: Index) -> np.ndarray: ...
@overload
def unique(values: Categorical) -> Categorical: ...
@overload
def unique(values: Series) -> np.ndarray | ExtensionArray: ...
@overload
def unique(values: np.ndarray | list) -> np.ndarray: ...
@overload
def unique(values: ExtensionArray) -> ExtensionArray: ...
@overload
def factorize(
    values: Sequence,
    sort: bool = ...,
    use_na_sentinel: bool = ...,
    size_hint: int | None = ...,
) -> tuple[np.ndarray, np.ndarray]:
    """
Encode the object as an enumerated type or categorical variable.

This method is useful for obtaining a numeric representation of an
array when all that matters is identifying distinct values. `factorize`
is available as both a top-level function :func:`pandas.factorize`,
and as a method :meth:`Series.factorize` and :meth:`Index.factorize`.

Parameters
----------
values : sequence
    A 1-D sequence. Sequences that aren't pandas objects are
    coerced to ndarrays before factorization.
sort : bool, default False
    Sort `uniques` and shuffle `codes` to maintain the
    relationship.

na_sentinel : int or None, default -1
    Value to mark "not found". If None, will not drop the NaN
    from the uniques of the values.

    .. deprecated:: 1.5.0
        The na_sentinel argument is deprecated and
        will be removed in a future version of pandas. Specify use_na_sentinel as
        either True or False.

    .. versionchanged:: 1.1.2

use_na_sentinel : bool, default True
    If True, the sentinel -1 will be used for NaN values. If False,
    NaN values will be encoded as non-negative integers and will not drop the
    NaN from the uniques of the values.

    .. versionadded:: 1.5.0
size_hint : int, optional
    Hint to the hashtable sizer.

Returns
-------
codes : ndarray
    An integer ndarray that's an indexer into `uniques`.
    ``uniques.take(codes)`` will have the same values as `values`.
uniques : ndarray, Index, or Categorical
    The unique valid values. When `values` is Categorical, `uniques`
    is a Categorical. When `values` is some other pandas object, an
    `Index` is returned. Otherwise, a 1-D ndarray is returned.

    .. note::

       Even if there's a missing value in `values`, `uniques` will
       *not* contain an entry for it.

See Also
--------
cut : Discretize continuous-valued array.
unique : Find the unique value in an array.

Notes
-----
Reference :ref:`the user guide <reshaping.factorize>` for more examples.

Examples
--------
These examples all show factorize as a top-level method like
``pd.factorize(values)``. The results are identical for methods like
:meth:`Series.factorize`.

>>> codes, uniques = pd.factorize(['b', 'b', 'a', 'c', 'b'])
>>> codes
array([0, 0, 1, 2, 0]...)
>>> uniques
array(['b', 'a', 'c'], dtype=object)

With ``sort=True``, the `uniques` will be sorted, and `codes` will be
shuffled so that the relationship is the maintained.

>>> codes, uniques = pd.factorize(['b', 'b', 'a', 'c', 'b'], sort=True)
>>> codes
array([1, 1, 0, 2, 1]...)
>>> uniques
array(['a', 'b', 'c'], dtype=object)

When ``use_na_sentinel=True`` (the default), missing values are indicated in
the `codes` with the sentinel value ``-1`` and missing values are not
included in `uniques`.

>>> codes, uniques = pd.factorize(['b', None, 'a', 'c', 'b'])
>>> codes
array([ 0, -1,  1,  2,  0]...)
>>> uniques
array(['b', 'a', 'c'], dtype=object)

Thus far, we've only factorized lists (which are internally coerced to
NumPy arrays). When factorizing pandas objects, the type of `uniques`
will differ. For Categoricals, a `Categorical` is returned.

>>> cat = pd.Categorical(['a', 'a', 'c'], categories=['a', 'b', 'c'])
>>> codes, uniques = pd.factorize(cat)
>>> codes
array([0, 0, 1]...)
>>> uniques
['a', 'c']
Categories (3, object): ['a', 'b', 'c']

Notice that ``'b'`` is in ``uniques.categories``, despite not being
present in ``cat.values``.

For all other pandas objects, an Index of the appropriate type is
returned.

>>> cat = pd.Series(['a', 'a', 'c'])
>>> codes, uniques = pd.factorize(cat)
>>> codes
array([0, 0, 1]...)
>>> uniques
Index(['a', 'c'], dtype='object')

If NaN is in the values, and we want to include NaN in the uniques of the
values, it can be achieved by setting ``use_na_sentinel=False``.

>>> values = np.array([1, 2, 1, np.nan])
>>> codes, uniques = pd.factorize(values)  # default: use_na_sentinel=True
>>> codes
array([ 0,  1,  0, -1])
>>> uniques
array([1., 2.])

>>> codes, uniques = pd.factorize(values, use_na_sentinel=False)
>>> codes
array([0, 1, 0, 2])
>>> uniques
array([ 1.,  2., nan])
    """
    pass
@overload
def factorize(
    values: Index | Series,
    sort: bool = ...,
    # Not actually positional-only, used to handle deprecations in 1.5.0
    *,
    use_na_sentinel: bool = ...,
    size_hint: int | None = ...,
) -> tuple[np.ndarray, Index]: ...
@overload
def factorize(
    values: Categorical,
    sort: bool = ...,
    # Not actually positional-only, used to handle deprecations in 1.5.0
    *,
    use_na_sentinel: bool = ...,
    size_hint: int | None = ...,
) -> tuple[np.ndarray, Categorical]: ...
def value_counts(
    values: AnyArrayLike | list | tuple,
    sort: bool = ...,
    ascending: bool = ...,
    normalize: bool = ...,
    bins: int | None = ...,
    dropna: bool = ...,
) -> Series: ...
def take(
    arr,
    indices: TakeIndexer,
    axis: AxisInt = 0,
    allow_fill: bool = False,
    fill_value=None,
): ...
