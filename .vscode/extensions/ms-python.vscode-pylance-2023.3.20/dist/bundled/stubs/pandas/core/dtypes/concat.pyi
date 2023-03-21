from typing import TypeVar

from pandas import (
    Categorical,
    CategoricalIndex,
    Series,
)

_CatT = TypeVar("_CatT", Categorical, CategoricalIndex, Series)

def union_categoricals(
    to_union: list[_CatT], sort_categories: bool = ..., ignore_order: bool = ...
) -> Categorical: ...
