from pandas import DataFrame

from pandas._typing import IgnoreRaise

def json_normalize(
    data: dict | list[dict],
    record_path: str | list | None = ...,
    meta: str | list[str | list[str]] | None = ...,
    meta_prefix: str | None = ...,
    record_prefix: str | None = ...,
    errors: IgnoreRaise = ...,
    sep: str = ...,
    max_level: int | None = ...,
) -> DataFrame: ...
