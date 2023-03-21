from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

class FileRecoveryProperties(Serialisable):
    tagname: str
    autoRecover: Incomplete
    crashSave: Incomplete
    dataExtractLoad: Incomplete
    repairLoad: Incomplete
    def __init__(
        self,
        autoRecover: Incomplete | None = ...,
        crashSave: Incomplete | None = ...,
        dataExtractLoad: Incomplete | None = ...,
        repairLoad: Incomplete | None = ...,
    ) -> None: ...

class ChildSheet(Serialisable):
    tagname: str
    name: Incomplete
    sheetId: Incomplete
    state: Incomplete
    id: Incomplete
    def __init__(
        self, name: Incomplete | None = ..., sheetId: Incomplete | None = ..., state: str = ..., id: Incomplete | None = ...
    ) -> None: ...

class PivotCache(Serialisable):
    tagname: str
    cacheId: Incomplete
    id: Incomplete
    def __init__(self, cacheId: Incomplete | None = ..., id: Incomplete | None = ...) -> None: ...

class WorkbookPackage(Serialisable):
    tagname: str
    conformance: Incomplete
    fileVersion: Incomplete
    fileSharing: Incomplete
    workbookPr: Incomplete
    properties: Incomplete
    workbookProtection: Incomplete
    bookViews: Incomplete
    sheets: Incomplete
    functionGroups: Incomplete
    externalReferences: Incomplete
    definedNames: Incomplete
    calcPr: Incomplete
    oleSize: Incomplete
    customWorkbookViews: Incomplete
    pivotCaches: Incomplete
    smartTagPr: Incomplete
    smartTagTypes: Incomplete
    webPublishing: Incomplete
    fileRecoveryPr: Incomplete
    webPublishObjects: Incomplete
    extLst: Incomplete
    Ignorable: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        conformance: Incomplete | None = ...,
        fileVersion: Incomplete | None = ...,
        fileSharing: Incomplete | None = ...,
        workbookPr: Incomplete | None = ...,
        workbookProtection: Incomplete | None = ...,
        bookViews=...,
        sheets=...,
        functionGroups: Incomplete | None = ...,
        externalReferences=...,
        definedNames: Incomplete | None = ...,
        calcPr: Incomplete | None = ...,
        oleSize: Incomplete | None = ...,
        customWorkbookViews=...,
        pivotCaches=...,
        smartTagPr: Incomplete | None = ...,
        smartTagTypes: Incomplete | None = ...,
        webPublishing: Incomplete | None = ...,
        fileRecoveryPr: Incomplete | None = ...,
        webPublishObjects: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
        Ignorable: Incomplete | None = ...,
    ) -> None: ...
    def to_tree(self): ...
    @property
    def active(self): ...
    @property
    def pivot_caches(self): ...
