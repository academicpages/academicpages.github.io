from collections.abc import Sequence

import numpy as np
from pandas.core.indexes.api import Index
from pandas.core.series import Series

from pandas._typing import (
    ArrayLike,
    Dtype,
)

from pandas.core.dtypes.dtypes import ExtensionDtype
from pandas.core.dtypes.generic import ABCExtensionArray

def array(
    data: Sequence[object],
    dtype: str | np.dtype | ExtensionDtype | None = ...,
    copy: bool = ...,
) -> ABCExtensionArray: ...
def extract_array(obj, extract_numpy: bool = ...): ...
def sanitize_array(
    data, index, dtype=..., copy: bool = ..., raise_cast_failure: bool = ...
): ...
def is_empty_data(data) -> bool: ...
def create_series_with_explicit_dtype(
    data=...,
    index: ArrayLike | Index | None = ...,
    dtype: Dtype | None = ...,
    name: str | None = ...,
    copy: bool = ...,
    fastpath: bool = ...,
    dtype_if_empty: Dtype = ...,
) -> Series: ...
