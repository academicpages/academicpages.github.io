from typing import Any

from pandas import DataFrame

from pandas._typing import (
    FilePath,
    ParquetEngine,
    ReadBuffer,
    StorageOptions,
)

def read_parquet(
    path: FilePath | ReadBuffer[bytes],
    engine: ParquetEngine = ...,
    columns: list[str] | None = ...,
    storage_options: StorageOptions = ...,
    use_nullable_dtypes: bool = ...,
    **kwargs: Any,
) -> DataFrame: ...
