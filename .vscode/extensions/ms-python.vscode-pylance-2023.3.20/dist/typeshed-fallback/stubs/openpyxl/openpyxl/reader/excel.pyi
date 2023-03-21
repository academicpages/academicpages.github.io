from _typeshed import Incomplete, StrPath, SupportsRead

from openpyxl.chartsheet.chartsheet import Chartsheet
from openpyxl.packaging.relationship import Relationship
from openpyxl.workbook.workbook import Workbook

SUPPORTED_FORMATS: Incomplete

class ExcelReader:
    archive: Incomplete
    valid_files: Incomplete
    read_only: Incomplete
    keep_vba: Incomplete
    data_only: Incomplete
    keep_links: Incomplete
    shared_strings: Incomplete
    def __init__(
        self, fn: SupportsRead[bytes] | str, read_only: bool = ..., keep_vba=..., data_only: bool = ..., keep_links: bool = ...
    ) -> None: ...
    package: Incomplete
    def read_manifest(self) -> None: ...
    def read_strings(self) -> None: ...
    parser: Incomplete
    wb: Incomplete
    def read_workbook(self) -> None: ...
    def read_properties(self) -> None: ...
    def read_theme(self) -> None: ...
    def read_chartsheet(self, sheet: Chartsheet, rel: Relationship) -> None: ...
    def read_worksheets(self) -> None: ...
    def read(self) -> None: ...

def load_workbook(
    filename: SupportsRead[bytes] | StrPath,
    read_only: bool = ...,
    keep_vba: bool = ...,
    data_only: bool = ...,
    keep_links: bool = ...,
) -> Workbook: ...
