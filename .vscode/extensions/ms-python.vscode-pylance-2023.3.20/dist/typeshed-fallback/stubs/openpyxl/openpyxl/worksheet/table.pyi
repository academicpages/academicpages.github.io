from _typeshed import Incomplete

from openpyxl.descriptors import String
from openpyxl.descriptors.serialisable import Serialisable

TABLESTYLES: Incomplete
PIVOTSTYLES: Incomplete

class TableStyleInfo(Serialisable):
    tagname: str
    name: Incomplete
    showFirstColumn: Incomplete
    showLastColumn: Incomplete
    showRowStripes: Incomplete
    showColumnStripes: Incomplete
    def __init__(
        self,
        name: Incomplete | None = ...,
        showFirstColumn: Incomplete | None = ...,
        showLastColumn: Incomplete | None = ...,
        showRowStripes: Incomplete | None = ...,
        showColumnStripes: Incomplete | None = ...,
    ) -> None: ...

class XMLColumnProps(Serialisable):
    tagname: str
    mapId: Incomplete
    xpath: Incomplete
    denormalized: Incomplete
    xmlDataType: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        mapId: Incomplete | None = ...,
        xpath: Incomplete | None = ...,
        denormalized: Incomplete | None = ...,
        xmlDataType: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
    ) -> None: ...

class TableFormula(Serialisable):
    tagname: str
    array: Incomplete
    attr_text: Incomplete
    text: Incomplete
    def __init__(self, array: Incomplete | None = ..., attr_text: Incomplete | None = ...) -> None: ...

class TableColumn(Serialisable):
    tagname: str
    id: Incomplete
    uniqueName: Incomplete
    name: Incomplete
    totalsRowFunction: Incomplete
    totalsRowLabel: Incomplete
    queryTableFieldId: Incomplete
    headerRowDxfId: Incomplete
    dataDxfId: Incomplete
    totalsRowDxfId: Incomplete
    headerRowCellStyle: Incomplete
    dataCellStyle: Incomplete
    totalsRowCellStyle: Incomplete
    calculatedColumnFormula: Incomplete
    totalsRowFormula: Incomplete
    xmlColumnPr: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        id: Incomplete | None = ...,
        uniqueName: Incomplete | None = ...,
        name: Incomplete | None = ...,
        totalsRowFunction: Incomplete | None = ...,
        totalsRowLabel: Incomplete | None = ...,
        queryTableFieldId: Incomplete | None = ...,
        headerRowDxfId: Incomplete | None = ...,
        dataDxfId: Incomplete | None = ...,
        totalsRowDxfId: Incomplete | None = ...,
        headerRowCellStyle: Incomplete | None = ...,
        dataCellStyle: Incomplete | None = ...,
        totalsRowCellStyle: Incomplete | None = ...,
        calculatedColumnFormula: Incomplete | None = ...,
        totalsRowFormula: Incomplete | None = ...,
        xmlColumnPr: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
    ) -> None: ...
    def __iter__(self): ...
    @classmethod
    def from_tree(cls, node): ...

class TableNameDescriptor(String):
    def __set__(self, instance, value) -> None: ...

class Table(Serialisable):
    mime_type: str
    tagname: str
    id: Incomplete
    name: Incomplete
    displayName: Incomplete
    comment: Incomplete
    ref: Incomplete
    tableType: Incomplete
    headerRowCount: Incomplete
    insertRow: Incomplete
    insertRowShift: Incomplete
    totalsRowCount: Incomplete
    totalsRowShown: Incomplete
    published: Incomplete
    headerRowDxfId: Incomplete
    dataDxfId: Incomplete
    totalsRowDxfId: Incomplete
    headerRowBorderDxfId: Incomplete
    tableBorderDxfId: Incomplete
    totalsRowBorderDxfId: Incomplete
    headerRowCellStyle: Incomplete
    dataCellStyle: Incomplete
    totalsRowCellStyle: Incomplete
    connectionId: Incomplete
    autoFilter: Incomplete
    sortState: Incomplete
    tableColumns: Incomplete
    tableStyleInfo: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        id: int = ...,
        displayName: Incomplete | None = ...,
        ref: Incomplete | None = ...,
        name: Incomplete | None = ...,
        comment: Incomplete | None = ...,
        tableType: Incomplete | None = ...,
        headerRowCount: int = ...,
        insertRow: Incomplete | None = ...,
        insertRowShift: Incomplete | None = ...,
        totalsRowCount: Incomplete | None = ...,
        totalsRowShown: Incomplete | None = ...,
        published: Incomplete | None = ...,
        headerRowDxfId: Incomplete | None = ...,
        dataDxfId: Incomplete | None = ...,
        totalsRowDxfId: Incomplete | None = ...,
        headerRowBorderDxfId: Incomplete | None = ...,
        tableBorderDxfId: Incomplete | None = ...,
        totalsRowBorderDxfId: Incomplete | None = ...,
        headerRowCellStyle: Incomplete | None = ...,
        dataCellStyle: Incomplete | None = ...,
        totalsRowCellStyle: Incomplete | None = ...,
        connectionId: Incomplete | None = ...,
        autoFilter: Incomplete | None = ...,
        sortState: Incomplete | None = ...,
        tableColumns=...,
        tableStyleInfo: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
    ) -> None: ...
    def to_tree(self): ...
    @property
    def path(self): ...
    @property
    def column_names(self): ...

class TablePartList(Serialisable):
    tagname: str
    # Overwritten by property below
    # count: Integer
    tablePart: Incomplete
    __elements__: Incomplete
    __attrs__: Incomplete
    def __init__(self, count: Incomplete | None = ..., tablePart=...) -> None: ...
    def append(self, part) -> None: ...
    @property
    def count(self): ...
    def __bool__(self) -> bool: ...

class TableList(dict[Incomplete, Incomplete]):
    def add(self, table) -> None: ...
    def get(self, name: Incomplete | None = ..., table_range: Incomplete | None = ...): ...
    def items(self): ...
