from typing import Any

from pandas import DataFrame

from pandas._typing import (
    FilePath,
    HashableT,
    ReadBuffer,
)

def read_orc(
    path: FilePath | ReadBuffer[bytes],
    columns: list[HashableT] | None = ...,
    **kwargs: Any,
) -> DataFrame: ...
