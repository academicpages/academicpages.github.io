from pandas.core.frame import DataFrame

from pandas._typing import (
    FilePath,
    HashableT,
)

def read_spss(
    path: FilePath,
    usecols: list[HashableT] | None = ...,
    convert_categoricals: bool = ...,
) -> DataFrame: ...
