from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

class Outline(Serialisable):
    tagname: str
    applyStyles: Incomplete
    summaryBelow: Incomplete
    summaryRight: Incomplete
    showOutlineSymbols: Incomplete
    def __init__(
        self,
        applyStyles: Incomplete | None = ...,
        summaryBelow: Incomplete | None = ...,
        summaryRight: Incomplete | None = ...,
        showOutlineSymbols: Incomplete | None = ...,
    ) -> None: ...

class PageSetupProperties(Serialisable):
    tagname: str
    autoPageBreaks: Incomplete
    fitToPage: Incomplete
    def __init__(self, autoPageBreaks: Incomplete | None = ..., fitToPage: Incomplete | None = ...) -> None: ...

class WorksheetProperties(Serialisable):
    tagname: str
    codeName: Incomplete
    enableFormatConditionsCalculation: Incomplete
    filterMode: Incomplete
    published: Incomplete
    syncHorizontal: Incomplete
    syncRef: Incomplete
    syncVertical: Incomplete
    transitionEvaluation: Incomplete
    transitionEntry: Incomplete
    tabColor: Incomplete
    outlinePr: Incomplete
    pageSetUpPr: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        codeName: Incomplete | None = ...,
        enableFormatConditionsCalculation: Incomplete | None = ...,
        filterMode: Incomplete | None = ...,
        published: Incomplete | None = ...,
        syncHorizontal: Incomplete | None = ...,
        syncRef: Incomplete | None = ...,
        syncVertical: Incomplete | None = ...,
        transitionEvaluation: Incomplete | None = ...,
        transitionEntry: Incomplete | None = ...,
        tabColor: Incomplete | None = ...,
        outlinePr: Incomplete | None = ...,
        pageSetUpPr: Incomplete | None = ...,
    ) -> None: ...
