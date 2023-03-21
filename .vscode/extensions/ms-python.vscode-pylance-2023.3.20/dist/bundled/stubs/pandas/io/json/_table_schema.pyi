from pandas import (
    DataFrame,
    Series,
)

from pandas._typing import JSONSerializable

def build_table_schema(
    data: DataFrame | Series,
    index: bool = ...,
    primary_key: bool | None = ...,
    version: bool = ...,
) -> dict[str, JSONSerializable]: ...
