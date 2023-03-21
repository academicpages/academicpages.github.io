from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

class Pane(Serialisable):  # type: ignore[misc]
    xSplit: Incomplete
    ySplit: Incomplete
    topLeftCell: Incomplete
    activePane: Incomplete
    state: Incomplete
    def __init__(
        self,
        xSplit: Incomplete | None = ...,
        ySplit: Incomplete | None = ...,
        topLeftCell: Incomplete | None = ...,
        activePane: str = ...,
        state: str = ...,
    ) -> None: ...

class Selection(Serialisable):  # type: ignore[misc]
    pane: Incomplete
    activeCell: Incomplete
    activeCellId: Incomplete
    sqref: Incomplete
    def __init__(
        self, pane: Incomplete | None = ..., activeCell: str = ..., activeCellId: Incomplete | None = ..., sqref: str = ...
    ) -> None: ...

class SheetView(Serialisable):
    tagname: str
    windowProtection: Incomplete
    showFormulas: Incomplete
    showGridLines: Incomplete
    showRowColHeaders: Incomplete
    showZeros: Incomplete
    rightToLeft: Incomplete
    tabSelected: Incomplete
    showRuler: Incomplete
    showOutlineSymbols: Incomplete
    defaultGridColor: Incomplete
    showWhiteSpace: Incomplete
    view: Incomplete
    topLeftCell: Incomplete
    colorId: Incomplete
    zoomScale: Incomplete
    zoomScaleNormal: Incomplete
    zoomScaleSheetLayoutView: Incomplete
    zoomScalePageLayoutView: Incomplete
    zoomToFit: Incomplete
    workbookViewId: Incomplete
    selection: Incomplete
    pane: Incomplete
    def __init__(
        self,
        windowProtection: Incomplete | None = ...,
        showFormulas: Incomplete | None = ...,
        showGridLines: Incomplete | None = ...,
        showRowColHeaders: Incomplete | None = ...,
        showZeros: Incomplete | None = ...,
        rightToLeft: Incomplete | None = ...,
        tabSelected: Incomplete | None = ...,
        showRuler: Incomplete | None = ...,
        showOutlineSymbols: Incomplete | None = ...,
        defaultGridColor: Incomplete | None = ...,
        showWhiteSpace: Incomplete | None = ...,
        view: Incomplete | None = ...,
        topLeftCell: Incomplete | None = ...,
        colorId: Incomplete | None = ...,
        zoomScale: Incomplete | None = ...,
        zoomScaleNormal: Incomplete | None = ...,
        zoomScaleSheetLayoutView: Incomplete | None = ...,
        zoomScalePageLayoutView: Incomplete | None = ...,
        zoomToFit: Incomplete | None = ...,
        workbookViewId: int = ...,
        selection: Incomplete | None = ...,
        pane: Incomplete | None = ...,
    ) -> None: ...

class SheetViewList(Serialisable):
    tagname: str
    sheetView: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(self, sheetView: Incomplete | None = ..., extLst: Incomplete | None = ...) -> None: ...
