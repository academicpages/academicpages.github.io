from collections.abc import (
    Iterable,
    Mapping,
    Sequence,
)
from typing import (
    Literal,
    overload,
)

from pandas import (
    DataFrame,
    Series,
)

from pandas._typing import (
    HashableT1,
    HashableT2,
    HashableT3,
    HashableT4,
)

@overload
def concat(
    objs: Iterable[DataFrame] | Mapping[HashableT1, DataFrame],
    *,
    axis: Literal[0, "index"] = ...,
    join: Literal["inner", "outer"] = ...,
    ignore_index: bool = ...,
    keys: list[HashableT2] = ...,
    levels: Sequence[list[HashableT3] | tuple[HashableT3, ...]] = ...,
    names: list[HashableT4] = ...,
    verify_integrity: bool = ...,
    sort: bool = ...,
    copy: bool = ...,
) -> DataFrame: ...
@overload
def concat(
    objs: Iterable[Series] | Mapping[HashableT1, Series],
    *,
    axis: Literal[0, "index"] = ...,
    join: Literal["inner", "outer"] = ...,
    ignore_index: bool = ...,
    keys: list[HashableT2] = ...,
    levels: Sequence[list[HashableT3] | tuple[HashableT3, ...]] = ...,
    names: list[HashableT4] = ...,
    verify_integrity: bool = ...,
    sort: bool = ...,
    copy: bool = ...,
) -> Series: ...
@overload
def concat(
    objs: Iterable[Series | DataFrame] | Mapping[HashableT1, Series | DataFrame],
    *,
    axis: Literal[1, "columns"],
    join: Literal["inner", "outer"] = ...,
    ignore_index: bool = ...,
    keys: list[HashableT2] = ...,
    levels: Sequence[list[HashableT3] | tuple[HashableT3, ...]] = ...,
    names: list[HashableT4] = ...,
    verify_integrity: bool = ...,
    sort: bool = ...,
    copy: bool = ...,
) -> DataFrame: ...

# Including either of the next 2 overloads causes mypy to complain about
# test_pandas.py:test_types_concat() in assert_type(pd.concat([s, s2]), "pd.Series")
# It thinks that pd.concat([s, s2]) is Any .  May be due to Series being
# Generic, or the axis argument being unspecified, and then there is partial
# overlap with the first 2 overloads.
#
# @overload
# def concat(
#     objs: Union[
#         Iterable[Union[Series, DataFrame]], Mapping[HashableT, Union[Series, DataFrame]]
#     ],
#     axis: Literal[0, "index"] = ...,
#     join: str = ...,
#     ignore_index: bool = ...,
#     keys=...,
#     levels=...,
#     names=...,
#     verify_integrity: bool = ...,
#     sort: bool = ...,
#     copy: bool = ...,
# ) -> Union[DataFrame, Series]: ...

# @overload
# def concat(
#     objs: Union[
#         Iterable[Union[Series, DataFrame]], Mapping[HashableT, Union[Series, DataFrame]]
#     ],
#     axis: Axis = ...,
#     join: str = ...,
#     ignore_index: bool = ...,
#     keys=...,
#     levels=...,
#     names=...,
#     verify_integrity: bool = ...,
#     sort: bool = ...,
#     copy: bool = ...,
# ) -> Union[DataFrame, Series]: ...
