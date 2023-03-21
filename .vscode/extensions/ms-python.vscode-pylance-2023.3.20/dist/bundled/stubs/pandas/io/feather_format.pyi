from pandas import DataFrame

from pandas._typing import (
    FilePath,
    HashableT,
    ReadBuffer,
    StorageOptions,
)

def read_feather(
    path: FilePath | ReadBuffer[bytes],
    columns: list[HashableT] | None = ...,
    use_threads: bool = ...,
    storage_options: StorageOptions = ...,
) -> DataFrame: ...
