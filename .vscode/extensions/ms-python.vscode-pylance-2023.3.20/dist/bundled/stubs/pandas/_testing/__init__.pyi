from collections.abc import Generator
from contextlib import contextmanager
from typing import (
    Any,
    Literal,
    overload,
)

from pandas import (
    DataFrame,
    Index,
    Series,
)

def getSeriesData(): ...
def assert_almost_equal(
    left,
    right,
    check_dtype: bool | str = ...,
    check_less_precise: bool | int = ...,
    **kwargs,
): ...
def assert_dict_equal(left, right, compare_keys: bool = ...): ...
def assert_index_equal(left: Index, right: Index) -> None: ...
def assert_class_equal(left, right, exact: bool | str = ..., obj=...): ...
def assert_attr_equal(attr, left, right, obj: str = ...): ...
def assert_is_valid_plot_return_object(objs) -> None: ...
def assert_is_sorted(seq) -> None: ...
def assert_categorical_equal(
    left,
    right,
    check_dtype: bool = ...,
    check_category_order: bool = ...,
    obj: str = ...,
) -> None: ...
def assert_interval_array_equal(
    left, right, exact: str = ..., obj: str = ...
) -> None: ...
def assert_period_array_equal(left, right, obj: str = ...) -> None: ...
def assert_datetime_array_equal(left, right, obj: str = ...) -> None: ...
def assert_timedelta_array_equal(left, right, obj: str = ...) -> None: ...
def assert_numpy_array_equal(
    left,
    right,
    strict_nan: bool = ...,
    check_dtype: bool = ...,
    err_msg=...,
    check_same=...,
    obj: str = ...,
): ...
def assert_extension_array_equal(
    left,
    right,
    check_dtype: bool = ...,
    check_less_precise: bool = ...,
    check_exact: bool = ...,
) -> None: ...
@overload
def assert_series_equal(
    left: Series,
    right: Series,
    check_dtype: bool = ...,
    check_index_type: bool | str = ...,
    check_series_type: bool = ...,
    check_names: bool = ...,
    check_exact: bool = ...,
    check_datetimelike_compat: bool = ...,
    check_categorical: bool = ...,
    check_category_order: bool = ...,
    check_freq: bool = ...,
    check_flags: bool = ...,
    rtol: float = ...,
    atol: float = ...,
    obj: str = ...,
    *,
    check_index: Literal[False],
    check_like: Literal[False] = ...,
) -> None: ...
@overload
def assert_series_equal(
    left: Series,
    right: Series,
    check_dtype: bool = ...,
    check_index_type: bool | str = ...,
    check_series_type: bool = ...,
    check_names: bool = ...,
    check_exact: bool = ...,
    check_datetimelike_compat: bool = ...,
    check_categorical: bool = ...,
    check_category_order: bool = ...,
    check_freq: bool = ...,
    check_flags: bool = ...,
    rtol: float = ...,
    atol: float = ...,
    obj: str = ...,
    *,
    check_index: Literal[True] = ...,
    check_like: bool = ...,
) -> None: ...
def assert_frame_equal(
    left: DataFrame,
    right: DataFrame,
    check_dtype: bool | Literal["equiv"] = ...,
    check_index_type: bool | Literal["equiv"] = ...,
    check_column_type: bool | Literal["equiv"] = ...,
    check_frame_type: bool = ...,
    check_less_precise: int | bool = ...,
    check_names: bool = ...,
    by_blocks: bool = ...,
    check_exact: bool = ...,
    check_datetimelike_compat: bool = ...,
    check_categorical: bool = ...,
    check_like: bool = ...,
    check_freq: bool = ...,
    check_flag: bool = ...,
    rtol: float = ...,
    atol: float = ...,
    obj: str = ...,
) -> None: ...
def assert_equal(left, right, **kwargs) -> None: ...
def assert_sp_array_equal(
    left,
    right,
    check_dtype: bool = ...,
    check_kind: bool = ...,
    check_fill_value: bool = ...,
    consolidate_block_indices: bool = ...,
) -> None: ...
def assert_contains_all(iterable, dic) -> None: ...
def assert_copy(iter1, iter2, **eql_kwargs) -> None: ...
def assert_produces_warning(
    expected_warning=...,
    filter_level: str = ...,
    clear=...,
    check_stacklevel: bool = ...,
    raise_on_extra_warnings: bool = ...,
) -> None: ...
@contextmanager
def ensure_clean(
    filename: str | None = ..., return_filelike: bool = ..., **kwargs: Any
) -> Generator[str, None, None]: ...
