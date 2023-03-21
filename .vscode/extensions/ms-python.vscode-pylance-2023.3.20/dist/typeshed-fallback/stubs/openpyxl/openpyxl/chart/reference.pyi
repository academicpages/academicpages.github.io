from _typeshed import Incomplete
from collections.abc import Generator

from openpyxl.descriptors import Strict

class DummyWorksheet:
    title: Incomplete
    def __init__(self, title) -> None: ...

class Reference(Strict):
    min_row: Incomplete
    max_row: Incomplete
    min_col: Incomplete
    max_col: Incomplete
    range_string: Incomplete
    worksheet: Incomplete
    def __init__(
        self,
        worksheet: Incomplete | None = ...,
        min_col: Incomplete | None = ...,
        min_row: Incomplete | None = ...,
        max_col: Incomplete | None = ...,
        max_row: Incomplete | None = ...,
        range_string: Incomplete | None = ...,
    ) -> None: ...
    def __len__(self) -> int: ...
    def __eq__(self, other): ...
    @property
    def rows(self) -> Generator[Incomplete, None, None]: ...
    @property
    def cols(self) -> Generator[Incomplete, None, None]: ...
    def pop(self): ...
    @property
    def sheetname(self): ...
