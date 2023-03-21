from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

class PrintPageSetup(Serialisable):
    tagname: str
    orientation: Incomplete
    paperSize: Incomplete
    scale: Incomplete
    fitToHeight: Incomplete
    fitToWidth: Incomplete
    firstPageNumber: Incomplete
    useFirstPageNumber: Incomplete
    paperHeight: Incomplete
    paperWidth: Incomplete
    pageOrder: Incomplete
    usePrinterDefaults: Incomplete
    blackAndWhite: Incomplete
    draft: Incomplete
    cellComments: Incomplete
    errors: Incomplete
    horizontalDpi: Incomplete
    verticalDpi: Incomplete
    copies: Incomplete
    id: Incomplete
    def __init__(
        self,
        worksheet: Incomplete | None = ...,
        orientation: Incomplete | None = ...,
        paperSize: Incomplete | None = ...,
        scale: Incomplete | None = ...,
        fitToHeight: Incomplete | None = ...,
        fitToWidth: Incomplete | None = ...,
        firstPageNumber: Incomplete | None = ...,
        useFirstPageNumber: Incomplete | None = ...,
        paperHeight: Incomplete | None = ...,
        paperWidth: Incomplete | None = ...,
        pageOrder: Incomplete | None = ...,
        usePrinterDefaults: Incomplete | None = ...,
        blackAndWhite: Incomplete | None = ...,
        draft: Incomplete | None = ...,
        cellComments: Incomplete | None = ...,
        errors: Incomplete | None = ...,
        horizontalDpi: Incomplete | None = ...,
        verticalDpi: Incomplete | None = ...,
        copies: Incomplete | None = ...,
        id: Incomplete | None = ...,
    ) -> None: ...
    def __bool__(self) -> bool: ...
    @property
    def sheet_properties(self): ...
    @property
    def fitToPage(self): ...
    @fitToPage.setter
    def fitToPage(self, value) -> None: ...
    @property
    def autoPageBreaks(self): ...
    @autoPageBreaks.setter
    def autoPageBreaks(self, value) -> None: ...
    @classmethod
    def from_tree(cls, node): ...

class PrintOptions(Serialisable):
    tagname: str
    horizontalCentered: Incomplete
    verticalCentered: Incomplete
    headings: Incomplete
    gridLines: Incomplete
    gridLinesSet: Incomplete
    def __init__(
        self,
        horizontalCentered: Incomplete | None = ...,
        verticalCentered: Incomplete | None = ...,
        headings: Incomplete | None = ...,
        gridLines: Incomplete | None = ...,
        gridLinesSet: Incomplete | None = ...,
    ) -> None: ...
    def __bool__(self) -> bool: ...

class PageMargins(Serialisable):
    tagname: str
    left: Incomplete
    right: Incomplete
    top: Incomplete
    bottom: Incomplete
    header: Incomplete
    footer: Incomplete
    def __init__(
        self, left: float = ..., right: float = ..., top: int = ..., bottom: int = ..., header: float = ..., footer: float = ...
    ) -> None: ...
