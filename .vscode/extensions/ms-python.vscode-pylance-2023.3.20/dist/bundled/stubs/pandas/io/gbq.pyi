from typing import (
    Any,
    Literal,
)

from pandas.core.frame import DataFrame

def read_gbq(
    query: str,
    project_id: str | None = ...,
    index_col: str | None = ...,
    col_order: list[str] | None = ...,
    reauth: bool = ...,
    auth_local_webserver: bool = ...,
    dialect: Literal["legacy", "standard"] | None = ...,
    location: str | None = ...,
    configuration: dict[str, Any] | None = ...,
    # Google type, not available
    credentials: Any = ...,
    use_bqstorage_api: bool | None = ...,
    max_results: int | None = ...,
    progress_bar_type: Literal["tqdm", "tqdm_notebook", "tqdm_gui"] | None = ...,
) -> DataFrame: ...
