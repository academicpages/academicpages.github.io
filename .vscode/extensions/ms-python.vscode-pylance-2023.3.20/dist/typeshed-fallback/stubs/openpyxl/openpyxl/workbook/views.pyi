from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

class BookView(Serialisable):
    tagname: str
    visibility: Incomplete
    minimized: Incomplete
    showHorizontalScroll: Incomplete
    showVerticalScroll: Incomplete
    showSheetTabs: Incomplete
    xWindow: Incomplete
    yWindow: Incomplete
    windowWidth: Incomplete
    windowHeight: Incomplete
    tabRatio: Incomplete
    firstSheet: Incomplete
    activeTab: Incomplete
    autoFilterDateGrouping: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        visibility: str = ...,
        minimized: bool = ...,
        showHorizontalScroll: bool = ...,
        showVerticalScroll: bool = ...,
        showSheetTabs: bool = ...,
        xWindow: Incomplete | None = ...,
        yWindow: Incomplete | None = ...,
        windowWidth: Incomplete | None = ...,
        windowHeight: Incomplete | None = ...,
        tabRatio: int = ...,
        firstSheet: int = ...,
        activeTab: int = ...,
        autoFilterDateGrouping: bool = ...,
        extLst: Incomplete | None = ...,
    ) -> None: ...

class CustomWorkbookView(Serialisable):
    tagname: str
    name: Incomplete
    guid: Incomplete
    autoUpdate: Incomplete
    mergeInterval: Incomplete
    changesSavedWin: Incomplete
    onlySync: Incomplete
    personalView: Incomplete
    includePrintSettings: Incomplete
    includeHiddenRowCol: Incomplete
    maximized: Incomplete
    minimized: Incomplete
    showHorizontalScroll: Incomplete
    showVerticalScroll: Incomplete
    showSheetTabs: Incomplete
    xWindow: Incomplete
    yWindow: Incomplete
    windowWidth: Incomplete
    windowHeight: Incomplete
    tabRatio: Incomplete
    activeSheetId: Incomplete
    showFormulaBar: Incomplete
    showStatusbar: Incomplete
    showComments: Incomplete
    showObjects: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        name: Incomplete | None = ...,
        guid: Incomplete | None = ...,
        autoUpdate: Incomplete | None = ...,
        mergeInterval: Incomplete | None = ...,
        changesSavedWin: Incomplete | None = ...,
        onlySync: Incomplete | None = ...,
        personalView: Incomplete | None = ...,
        includePrintSettings: Incomplete | None = ...,
        includeHiddenRowCol: Incomplete | None = ...,
        maximized: Incomplete | None = ...,
        minimized: Incomplete | None = ...,
        showHorizontalScroll: Incomplete | None = ...,
        showVerticalScroll: Incomplete | None = ...,
        showSheetTabs: Incomplete | None = ...,
        xWindow: Incomplete | None = ...,
        yWindow: Incomplete | None = ...,
        windowWidth: Incomplete | None = ...,
        windowHeight: Incomplete | None = ...,
        tabRatio: Incomplete | None = ...,
        activeSheetId: Incomplete | None = ...,
        showFormulaBar: Incomplete | None = ...,
        showStatusbar: Incomplete | None = ...,
        showComments: str = ...,
        showObjects: str = ...,
        extLst: Incomplete | None = ...,
    ) -> None: ...
