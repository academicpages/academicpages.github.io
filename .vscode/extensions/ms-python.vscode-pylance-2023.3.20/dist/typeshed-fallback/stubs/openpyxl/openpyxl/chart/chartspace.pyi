from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

class ChartContainer(Serialisable):
    tagname: str
    title: Incomplete
    autoTitleDeleted: Incomplete
    pivotFmts: Incomplete
    view3D: Incomplete
    floor: Incomplete
    sideWall: Incomplete
    backWall: Incomplete
    plotArea: Incomplete
    legend: Incomplete
    plotVisOnly: Incomplete
    dispBlanksAs: Incomplete
    showDLblsOverMax: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        title: Incomplete | None = ...,
        autoTitleDeleted: Incomplete | None = ...,
        pivotFmts=...,
        view3D: Incomplete | None = ...,
        floor: Incomplete | None = ...,
        sideWall: Incomplete | None = ...,
        backWall: Incomplete | None = ...,
        plotArea: Incomplete | None = ...,
        legend: Incomplete | None = ...,
        plotVisOnly: bool = ...,
        dispBlanksAs: str = ...,
        showDLblsOverMax: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
    ) -> None: ...

class Protection(Serialisable):
    tagname: str
    chartObject: Incomplete
    data: Incomplete
    formatting: Incomplete
    selection: Incomplete
    userInterface: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        chartObject: Incomplete | None = ...,
        data: Incomplete | None = ...,
        formatting: Incomplete | None = ...,
        selection: Incomplete | None = ...,
        userInterface: Incomplete | None = ...,
    ) -> None: ...

class ExternalData(Serialisable):
    tagname: str
    autoUpdate: Incomplete
    id: Incomplete
    def __init__(self, autoUpdate: Incomplete | None = ..., id: Incomplete | None = ...) -> None: ...

class ChartSpace(Serialisable):
    tagname: str
    date1904: Incomplete
    lang: Incomplete
    roundedCorners: Incomplete
    style: Incomplete
    clrMapOvr: Incomplete
    pivotSource: Incomplete
    protection: Incomplete
    chart: Incomplete
    spPr: Incomplete
    graphicalProperties: Incomplete
    txPr: Incomplete
    textProperties: Incomplete
    externalData: Incomplete
    printSettings: Incomplete
    userShapes: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        date1904: Incomplete | None = ...,
        lang: Incomplete | None = ...,
        roundedCorners: Incomplete | None = ...,
        style: Incomplete | None = ...,
        clrMapOvr: Incomplete | None = ...,
        pivotSource: Incomplete | None = ...,
        protection: Incomplete | None = ...,
        chart: Incomplete | None = ...,
        spPr: Incomplete | None = ...,
        txPr: Incomplete | None = ...,
        externalData: Incomplete | None = ...,
        printSettings: Incomplete | None = ...,
        userShapes: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
    ) -> None: ...
    def to_tree(self, tagname: Incomplete | None = ..., idx: Incomplete | None = ..., namespace: Incomplete | None = ...): ...
