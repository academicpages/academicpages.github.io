from typing import (
    Literal,
    overload,
)

import numpy as np
import pandas as pd
from typing_extensions import TypeAlias

from pandas._typing import (
    IgnoreRaiseCoerce,
    Scalar,
    npt,
)

_Downcast: TypeAlias = Literal["integer", "signed", "unsigned", "float"] | None

@overload
def to_numeric(
    arg: Scalar,
    errors: Literal["raise", "coerce"] = ...,
    downcast: _Downcast = ...,
) -> float: ...
@overload
def to_numeric(
    arg: Scalar,
    errors: Literal["ignore"],
    downcast: _Downcast = ...,
) -> Scalar: ...
@overload
def to_numeric(
    arg: list | tuple | np.ndarray,
    errors: IgnoreRaiseCoerce = ...,
    downcast: _Downcast = ...,
) -> npt.NDArray: ...
@overload
def to_numeric(
    arg: pd.Series,
    errors: IgnoreRaiseCoerce = ...,
    downcast: _Downcast = ...,
) -> pd.Series: ...
