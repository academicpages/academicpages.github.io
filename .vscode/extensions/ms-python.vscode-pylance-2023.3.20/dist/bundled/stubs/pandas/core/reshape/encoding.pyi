from collections.abc import (
    Hashable,
    Iterable,
)

from pandas import (
    DataFrame,
    Series,
)

from pandas._typing import (
    ArrayLike,
    Dtype,
    HashableT1,
    HashableT2,
)

def get_dummies(
    data: ArrayLike | DataFrame | Series,
    prefix: str | Iterable[str] | dict[HashableT1, str] | None = ...,
    prefix_sep: str = ...,
    dummy_na: bool = ...,
    columns: list[HashableT2] | None = ...,
    sparse: bool = ...,
    drop_first: bool = ...,
    dtype: Dtype | None = ...,
) -> DataFrame: ...
def from_dummies(
    data: DataFrame,
    sep: str | None = ...,
    default_category: Hashable | dict[str, Hashable] | None = ...,
) -> DataFrame: ...
