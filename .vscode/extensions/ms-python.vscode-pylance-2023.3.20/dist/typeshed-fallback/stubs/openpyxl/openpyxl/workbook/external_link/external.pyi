from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

class ExternalCell(Serialisable):  # type: ignore[misc]
    r: Incomplete
    t: Incomplete
    vm: Incomplete
    v: Incomplete
    def __init__(
        self, r: Incomplete | None = ..., t: Incomplete | None = ..., vm: Incomplete | None = ..., v: Incomplete | None = ...
    ) -> None: ...

class ExternalRow(Serialisable):  # type: ignore[misc]
    r: Incomplete
    cell: Incomplete
    __elements__: Incomplete
    def __init__(self, r=..., cell: Incomplete | None = ...) -> None: ...

class ExternalSheetData(Serialisable):  # type: ignore[misc]
    sheetId: Incomplete
    refreshError: Incomplete
    row: Incomplete
    __elements__: Incomplete
    def __init__(self, sheetId: Incomplete | None = ..., refreshError: Incomplete | None = ..., row=...) -> None: ...

class ExternalSheetDataSet(Serialisable):  # type: ignore[misc]
    sheetData: Incomplete
    __elements__: Incomplete
    def __init__(self, sheetData: Incomplete | None = ...) -> None: ...

class ExternalSheetNames(Serialisable):  # type: ignore[misc]
    sheetName: Incomplete
    __elements__: Incomplete
    def __init__(self, sheetName=...) -> None: ...

class ExternalDefinedName(Serialisable):
    tagname: str
    name: Incomplete
    refersTo: Incomplete
    sheetId: Incomplete
    def __init__(
        self, name: Incomplete | None = ..., refersTo: Incomplete | None = ..., sheetId: Incomplete | None = ...
    ) -> None: ...

class ExternalBook(Serialisable):
    tagname: str
    sheetNames: Incomplete
    definedNames: Incomplete
    sheetDataSet: Incomplete
    id: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        sheetNames: Incomplete | None = ...,
        definedNames=...,
        sheetDataSet: Incomplete | None = ...,
        id: Incomplete | None = ...,
    ) -> None: ...

class ExternalLink(Serialisable):
    tagname: str
    mime_type: str
    externalBook: Incomplete
    file_link: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        externalBook: Incomplete | None = ...,
        ddeLink: Incomplete | None = ...,
        oleLink: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
    ) -> None: ...
    def to_tree(self): ...
    @property
    def path(self): ...

def read_external_link(archive, book_path): ...
