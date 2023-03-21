from pandas._typing import (
    Dtype,
    Scalar,
    npt,
)

from pandas.core.dtypes.base import ExtensionDtype
from pandas.core.dtypes.dtypes import (
    register_extension_dtype as register_extension_dtype,
)

class SparseDtype(ExtensionDtype):
    def __init__(
        self, dtype: Dtype | npt.DTypeLike = ..., fill_value: Scalar | None = ...
    ) -> None: ...
    @property
    def fill_value(self) -> Scalar | None: ...
