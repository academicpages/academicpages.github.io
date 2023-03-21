from _typeshed import Incomplete
from collections.abc import Generator

CELL_TAG: Incomplete
VALUE_TAG: Incomplete
FORMULA_TAG: Incomplete
MERGE_TAG: Incomplete
INLINE_STRING: Incomplete
COL_TAG: Incomplete
ROW_TAG: Incomplete
CF_TAG: Incomplete
LEGACY_TAG: Incomplete
PROT_TAG: Incomplete
EXT_TAG: Incomplete
HYPERLINK_TAG: Incomplete
TABLE_TAG: Incomplete
PRINT_TAG: Incomplete
MARGINS_TAG: Incomplete
PAGE_TAG: Incomplete
HEADER_TAG: Incomplete
FILTER_TAG: Incomplete
VALIDATION_TAG: Incomplete
PROPERTIES_TAG: Incomplete
VIEWS_TAG: Incomplete
FORMAT_TAG: Incomplete
ROW_BREAK_TAG: Incomplete
COL_BREAK_TAG: Incomplete
SCENARIOS_TAG: Incomplete
DATA_TAG: Incomplete
DIMENSION_TAG: Incomplete
CUSTOM_VIEWS_TAG: Incomplete

class WorkSheetParser:
    min_row: Incomplete
    epoch: Incomplete
    source: Incomplete
    shared_strings: Incomplete
    data_only: Incomplete
    shared_formulae: Incomplete
    array_formulae: Incomplete
    row_counter: int
    tables: Incomplete
    date_formats: Incomplete
    timedelta_formats: Incomplete
    row_dimensions: Incomplete
    column_dimensions: Incomplete
    number_formats: Incomplete
    keep_vba: bool
    hyperlinks: Incomplete
    formatting: Incomplete
    legacy_drawing: Incomplete
    merged_cells: Incomplete
    row_breaks: Incomplete
    col_breaks: Incomplete
    def __init__(
        self, src, shared_strings, data_only: bool = ..., epoch=..., date_formats=..., timedelta_formats=...
    ) -> None: ...
    def parse(self) -> Generator[Incomplete, None, None]: ...
    def parse_dimensions(self): ...
    col_counter: Incomplete
    def parse_cell(self, element): ...
    def parse_formula(self, element): ...
    def parse_column_dimensions(self, col) -> None: ...
    def parse_row(self, row): ...
    def parse_formatting(self, element) -> None: ...
    protection: Incomplete
    def parse_sheet_protection(self, element) -> None: ...
    def parse_extensions(self, element) -> None: ...
    def parse_legacy(self, element) -> None: ...
    def parse_row_breaks(self, element) -> None: ...
    def parse_col_breaks(self, element) -> None: ...
    def parse_custom_views(self, element) -> None: ...

class WorksheetReader:
    ws: Incomplete
    parser: Incomplete
    tables: Incomplete
    def __init__(self, ws, xml_source, shared_strings, data_only) -> None: ...
    def bind_cells(self) -> None: ...
    def bind_formatting(self) -> None: ...
    def bind_tables(self) -> None: ...
    def bind_merged_cells(self) -> None: ...
    def bind_hyperlinks(self) -> None: ...
    def normalize_merged_cell_link(self, coord): ...
    def bind_col_dimensions(self) -> None: ...
    def bind_row_dimensions(self) -> None: ...
    def bind_properties(self) -> None: ...
    def bind_all(self) -> None: ...
