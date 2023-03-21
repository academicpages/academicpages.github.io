from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

class WorkbookProperties(Serialisable):
    tagname: str
    date1904: Incomplete
    dateCompatibility: Incomplete
    showObjects: Incomplete
    showBorderUnselectedTables: Incomplete
    filterPrivacy: Incomplete
    promptedSolutions: Incomplete
    showInkAnnotation: Incomplete
    backupFile: Incomplete
    saveExternalLinkValues: Incomplete
    updateLinks: Incomplete
    codeName: Incomplete
    hidePivotFieldList: Incomplete
    showPivotChartFilter: Incomplete
    allowRefreshQuery: Incomplete
    publishItems: Incomplete
    checkCompatibility: Incomplete
    autoCompressPictures: Incomplete
    refreshAllConnections: Incomplete
    defaultThemeVersion: Incomplete
    def __init__(
        self,
        date1904: Incomplete | None = ...,
        dateCompatibility: Incomplete | None = ...,
        showObjects: Incomplete | None = ...,
        showBorderUnselectedTables: Incomplete | None = ...,
        filterPrivacy: Incomplete | None = ...,
        promptedSolutions: Incomplete | None = ...,
        showInkAnnotation: Incomplete | None = ...,
        backupFile: Incomplete | None = ...,
        saveExternalLinkValues: Incomplete | None = ...,
        updateLinks: Incomplete | None = ...,
        codeName: Incomplete | None = ...,
        hidePivotFieldList: Incomplete | None = ...,
        showPivotChartFilter: Incomplete | None = ...,
        allowRefreshQuery: Incomplete | None = ...,
        publishItems: Incomplete | None = ...,
        checkCompatibility: Incomplete | None = ...,
        autoCompressPictures: Incomplete | None = ...,
        refreshAllConnections: Incomplete | None = ...,
        defaultThemeVersion: Incomplete | None = ...,
    ) -> None: ...

class CalcProperties(Serialisable):
    tagname: str
    calcId: Incomplete
    calcMode: Incomplete
    fullCalcOnLoad: Incomplete
    refMode: Incomplete
    iterate: Incomplete
    iterateCount: Incomplete
    iterateDelta: Incomplete
    fullPrecision: Incomplete
    calcCompleted: Incomplete
    calcOnSave: Incomplete
    concurrentCalc: Incomplete
    concurrentManualCount: Incomplete
    forceFullCalc: Incomplete
    def __init__(
        self,
        calcId: int = ...,
        calcMode: Incomplete | None = ...,
        fullCalcOnLoad: bool = ...,
        refMode: Incomplete | None = ...,
        iterate: Incomplete | None = ...,
        iterateCount: Incomplete | None = ...,
        iterateDelta: Incomplete | None = ...,
        fullPrecision: Incomplete | None = ...,
        calcCompleted: Incomplete | None = ...,
        calcOnSave: Incomplete | None = ...,
        concurrentCalc: Incomplete | None = ...,
        concurrentManualCount: Incomplete | None = ...,
        forceFullCalc: Incomplete | None = ...,
    ) -> None: ...

class FileVersion(Serialisable):
    tagname: str
    appName: Incomplete
    lastEdited: Incomplete
    lowestEdited: Incomplete
    rupBuild: Incomplete
    codeName: Incomplete
    def __init__(
        self,
        appName: Incomplete | None = ...,
        lastEdited: Incomplete | None = ...,
        lowestEdited: Incomplete | None = ...,
        rupBuild: Incomplete | None = ...,
        codeName: Incomplete | None = ...,
    ) -> None: ...
