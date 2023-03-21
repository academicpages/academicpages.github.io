import numpy as np
from pandas import (
    DataFrame,
    Index,
    Series,
)

from pandas._typing import (
    ArrayLike,
    npt,
)

def hash_pandas_object(
    obj: Index | Series | DataFrame,
    index: bool = ...,
    encoding: str = ...,
    hash_key: str | None = ...,
    categorize: bool = ...,
) -> Series: ...
def hash_array(
    vals: ArrayLike, encoding: str = ..., hash_key: str = ..., categorize: bool = ...
) -> npt.NDArray[np.uint64]: ...
