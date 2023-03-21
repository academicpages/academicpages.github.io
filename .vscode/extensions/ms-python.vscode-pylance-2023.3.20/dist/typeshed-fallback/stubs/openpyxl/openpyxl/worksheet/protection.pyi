from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

class _Protected:
    def set_password(self, value: str = ..., already_hashed: bool = ...) -> None: ...
    @property
    def password(self): ...
    @password.setter
    def password(self, value) -> None: ...

class SheetProtection(Serialisable, _Protected):
    tagname: str
    sheet: Incomplete
    enabled: Incomplete
    objects: Incomplete
    scenarios: Incomplete
    formatCells: Incomplete
    formatColumns: Incomplete
    formatRows: Incomplete
    insertColumns: Incomplete
    insertRows: Incomplete
    insertHyperlinks: Incomplete
    deleteColumns: Incomplete
    deleteRows: Incomplete
    selectLockedCells: Incomplete
    selectUnlockedCells: Incomplete
    sort: Incomplete
    autoFilter: Incomplete
    pivotTables: Incomplete
    saltValue: Incomplete
    spinCount: Incomplete
    algorithmName: Incomplete
    hashValue: Incomplete
    __attrs__: Incomplete
    password: Incomplete
    def __init__(
        self,
        sheet: bool = ...,
        objects: bool = ...,
        scenarios: bool = ...,
        formatCells: bool = ...,
        formatRows: bool = ...,
        formatColumns: bool = ...,
        insertColumns: bool = ...,
        insertRows: bool = ...,
        insertHyperlinks: bool = ...,
        deleteColumns: bool = ...,
        deleteRows: bool = ...,
        selectLockedCells: bool = ...,
        selectUnlockedCells: bool = ...,
        sort: bool = ...,
        autoFilter: bool = ...,
        pivotTables: bool = ...,
        password: Incomplete | None = ...,
        algorithmName: Incomplete | None = ...,
        saltValue: Incomplete | None = ...,
        spinCount: Incomplete | None = ...,
        hashValue: Incomplete | None = ...,
    ) -> None: ...
    def set_password(self, value: str = ..., already_hashed: bool = ...) -> None: ...
    def enable(self) -> None: ...
    def disable(self) -> None: ...
    def __bool__(self) -> bool: ...
