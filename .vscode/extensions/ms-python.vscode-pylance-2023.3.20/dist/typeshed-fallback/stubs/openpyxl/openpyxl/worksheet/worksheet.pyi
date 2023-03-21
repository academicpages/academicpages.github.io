from _typeshed import Incomplete
from collections.abc import Generator, Iterable, Iterator
from datetime import datetime
from typing import overload
from typing_extensions import Literal

from openpyxl.cell.cell import Cell
from openpyxl.workbook.child import _WorkbookChild
from openpyxl.workbook.workbook import Workbook
from openpyxl.worksheet.cell_range import CellRange
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.worksheet.pagebreak import ColBreak, RowBreak
from openpyxl.worksheet.table import Table, TableList
from openpyxl.worksheet.views import SheetView

class Worksheet(_WorkbookChild):
    mime_type: str
    BREAK_NONE: int
    BREAK_ROW: int
    BREAK_COLUMN: int
    SHEETSTATE_VISIBLE: str
    SHEETSTATE_HIDDEN: str
    SHEETSTATE_VERYHIDDEN: str
    PAPERSIZE_LETTER: str
    PAPERSIZE_LETTER_SMALL: str
    PAPERSIZE_TABLOID: str
    PAPERSIZE_LEDGER: str
    PAPERSIZE_LEGAL: str
    PAPERSIZE_STATEMENT: str
    PAPERSIZE_EXECUTIVE: str
    PAPERSIZE_A3: str
    PAPERSIZE_A4: str
    PAPERSIZE_A4_SMALL: str
    PAPERSIZE_A5: str
    ORIENTATION_PORTRAIT: str
    ORIENTATION_LANDSCAPE: str
    def __init__(self, parent: Workbook, title: str | None = ...) -> None: ...
    @property
    def sheet_view(self) -> SheetView: ...
    @property
    def selected_cell(self) -> Cell: ...
    @property
    def active_cell(self) -> Cell: ...
    @property
    def page_breaks(self) -> tuple[RowBreak, ColBreak]: ...
    @property
    def show_gridlines(self) -> bool: ...
    @property
    def show_summary_below(self) -> bool: ...
    @property
    def show_summary_right(self) -> bool: ...
    @property
    def freeze_panes(self) -> str | None: ...
    @freeze_panes.setter
    def freeze_panes(self, topLeftCell: Incomplete | None = ...) -> None: ...
    def cell(self, row: int, column: int, value: str | None = ...) -> Cell: ...
    def __getitem__(self, key: str | int | slice) -> Cell | tuple[Cell, ...]: ...
    def __setitem__(self, key: str, value: str) -> None: ...
    def __iter__(self) -> Iterator[Cell]: ...
    def __delitem__(self, key: str) -> None: ...
    @property
    def min_row(self) -> int: ...
    @property
    def max_row(self) -> int: ...
    @property
    def min_column(self) -> int: ...
    @property
    def max_column(self) -> int: ...
    def calculate_dimension(self) -> str: ...
    @property
    def dimensions(self) -> str: ...
    @overload
    def iter_rows(
        self, min_row: int | None, max_row: int | None, min_col: int | None, max_col: int | None, values_only: Literal[True]
    ) -> Generator[tuple[str | float | datetime | None, ...], None, None]: ...
    @overload
    def iter_rows(
        self,
        min_row: int | None = None,
        max_row: int | None = None,
        min_col: int | None = None,
        max_col: int | None = None,
        *,
        values_only: Literal[True],
    ) -> Generator[tuple[str | float | datetime | None, ...], None, None]: ...
    @overload
    def iter_rows(
        self,
        min_row: int | None = ...,
        max_row: int | None = ...,
        min_col: int | None = ...,
        max_col: int | None = ...,
        values_only: Literal[False] = False,
    ) -> Generator[tuple[Cell, ...], None, None]: ...
    @overload
    def iter_rows(
        self, min_row: int | None, max_row: int | None, min_col: int | None, max_col: int | None, values_only: bool
    ) -> Generator[tuple[Cell | str | float | datetime | None, ...], None, None]: ...
    @overload
    def iter_rows(
        self,
        min_row: int | None = None,
        max_row: int | None = None,
        min_col: int | None = None,
        max_col: int | None = None,
        *,
        values_only: bool,
    ) -> Generator[tuple[Cell | str | float | datetime | None, ...], None, None]: ...
    @property
    def rows(self) -> Generator[Cell, None, None]: ...
    @property
    def values(self) -> Generator[str | float | datetime | None, None, None]: ...
    @overload
    def iter_cols(
        self, min_col: int | None, max_col: int | None, min_row: int | None, max_row: int | None, values_only: Literal[True]
    ) -> Generator[tuple[str | float | datetime | None, ...], None, None]: ...
    @overload
    def iter_cols(
        self,
        min_col: int | None = None,
        max_col: int | None = None,
        min_row: int | None = None,
        max_row: int | None = None,
        *,
        values_only: Literal[True],
    ) -> Generator[tuple[str | float | datetime | None, ...], None, None]: ...
    @overload
    def iter_cols(
        self,
        min_col: int | None = ...,
        max_col: int | None = ...,
        min_row: int | None = ...,
        max_row: int | None = ...,
        values_only: Literal[False] = False,
    ) -> Generator[tuple[Cell, ...], None, None]: ...
    @overload
    def iter_cols(
        self, min_col: int | None, max_col: int | None, min_row: int | None, max_row: int | None, values_only: bool
    ) -> Generator[tuple[Cell | str | float | datetime | None, ...], None, None]: ...
    @overload
    def iter_cols(
        self,
        min_col: int | None = None,
        max_col: int | None = None,
        min_row: int | None = None,
        max_row: int | None = None,
        *,
        values_only: bool,
    ) -> Generator[tuple[Cell | str | float | datetime | None, ...], None, None]: ...
    @property
    def columns(self) -> Generator[Cell, None, None]: ...
    def set_printer_settings(
        self, paper_size: int | None, orientation: None | Literal["default", "portrait", "landscape"]
    ) -> None: ...
    def add_data_validation(self, data_validation: DataValidation) -> None: ...
    def add_chart(self, chart, anchor: Incomplete | None = ...) -> None: ...
    def add_image(self, img, anchor: Incomplete | None = ...) -> None: ...
    def add_table(self, table: Table) -> None: ...
    @property
    def tables(self) -> TableList: ...
    def add_pivot(self, pivot) -> None: ...
    def merge_cells(
        self,
        range_string: str | None = ...,
        start_row: int | None = ...,
        start_column: int | None = ...,
        end_row: int | None = ...,
        end_column: int | None = ...,
    ) -> None: ...
    @property
    def merged_cell_ranges(self) -> list[CellRange]: ...
    def unmerge_cells(
        self,
        range_string: str | None = ...,
        start_row: int | None = ...,
        start_column: int | None = ...,
        end_row: int | None = ...,
        end_column: int | None = ...,
    ) -> None: ...
    def append(self, iterable: Iterable[Incomplete]) -> None: ...
    def insert_rows(self, idx: int, amount: int = ...) -> None: ...
    def insert_cols(self, idx: int, amount: int = ...) -> None: ...
    def delete_rows(self, idx: int, amount: int = ...) -> None: ...
    def delete_cols(self, idx: int, amount: int = ...) -> None: ...
    def move_range(self, cell_range: CellRange | str, rows: int = ..., cols: int = ..., translate: bool = ...) -> None: ...
    @property
    def print_title_rows(self) -> str | None: ...
    @print_title_rows.setter
    def print_title_rows(self, rows: str | None) -> None: ...
    @property
    def print_title_cols(self) -> str | None: ...
    @print_title_cols.setter
    def print_title_cols(self, cols: str | None) -> None: ...
    @property
    def print_titles(self) -> str | None: ...
    @property
    def print_area(self) -> list[str]: ...
    @print_area.setter
    def print_area(self, value: str | Iterable[str]) -> None: ...
