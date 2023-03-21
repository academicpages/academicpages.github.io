from _typeshed import Incomplete

from openpyxl.workbook.child import _WorkbookChild

class WriteOnlyWorksheet(_WorkbookChild):
    mime_type: Incomplete
    add_chart: Incomplete
    add_image: Incomplete
    add_table: Incomplete
    @property
    def tables(self): ...
    @property
    def print_titles(self): ...
    print_title_cols: Incomplete
    print_title_rows: Incomplete
    freeze_panes: Incomplete
    print_area: Incomplete
    @property
    def sheet_view(self): ...
    def __init__(self, parent, title) -> None: ...
    @property
    def closed(self): ...
    def close(self) -> None: ...
    def append(self, row) -> None: ...
