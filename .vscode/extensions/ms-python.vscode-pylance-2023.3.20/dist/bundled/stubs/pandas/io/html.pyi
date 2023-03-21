from collections.abc import (
    Callable,
    Hashable,
    Mapping,
    Sequence,
)
from re import Pattern
from typing import (
    Any,
    Literal,
)

from pandas.core.frame import DataFrame

from pandas._typing import (
    FilePath,
    HashableT1,
    HashableT2,
    HashableT3,
    HashableT4,
    HashableT5,
    ReadBuffer,
)

def read_html(
    io: FilePath | ReadBuffer[str],
    *,
    match: str | Pattern = ...,
    flavor: str | None = ...,
    header: int | Sequence[int] | None = ...,
    index_col: int | Sequence[int] | list[HashableT1] | None = ...,
    skiprows: int | Sequence[int] | slice | None = ...,
    attrs: dict[str, str] | None = ...,
    parse_dates: bool
    | Sequence[int]
    | list[HashableT2]  # Cannot be Sequence[Hashable] to prevent str
    | Sequence[Sequence[Hashable]]
    | dict[str, Sequence[int]]
    | dict[str, list[HashableT3]] = ...,
    thousands: str = ...,
    encoding: str | None = ...,
    decimal: str = ...,
    converters: Mapping[int | HashableT4, Callable[[str], Any]] | None = ...,
    na_values: str
    | list[str]
    | dict[HashableT5, str]
    | dict[HashableT5, list[str]]
    | None = ...,
    keep_default_na: bool = ...,
    displayed_only: bool = ...,
    extract_links: Literal["header", "footer", "body", "all"] | None = ...,
) -> list[DataFrame]: ...
