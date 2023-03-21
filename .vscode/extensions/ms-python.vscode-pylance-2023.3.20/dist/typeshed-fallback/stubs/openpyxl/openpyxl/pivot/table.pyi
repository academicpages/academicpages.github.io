from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

class HierarchyUsage(Serialisable):
    tagname: str
    hierarchyUsage: Incomplete
    def __init__(self, hierarchyUsage: Incomplete | None = ...) -> None: ...

class ColHierarchiesUsage(Serialisable):
    tagname: str
    colHierarchyUsage: Incomplete
    __elements__: Incomplete
    __attrs__: Incomplete
    def __init__(self, count: Incomplete | None = ..., colHierarchyUsage=...) -> None: ...
    @property
    def count(self): ...

class RowHierarchiesUsage(Serialisable):
    tagname: str
    rowHierarchyUsage: Incomplete
    __elements__: Incomplete
    __attrs__: Incomplete
    def __init__(self, count: Incomplete | None = ..., rowHierarchyUsage=...) -> None: ...
    @property
    def count(self): ...

class PivotFilter(Serialisable):
    tagname: str
    fld: Incomplete
    mpFld: Incomplete
    type: Incomplete
    evalOrder: Incomplete
    id: Incomplete
    iMeasureHier: Incomplete
    iMeasureFld: Incomplete
    name: Incomplete
    description: Incomplete
    stringValue1: Incomplete
    stringValue2: Incomplete
    autoFilter: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        fld: Incomplete | None = ...,
        mpFld: Incomplete | None = ...,
        type: Incomplete | None = ...,
        evalOrder: Incomplete | None = ...,
        id: Incomplete | None = ...,
        iMeasureHier: Incomplete | None = ...,
        iMeasureFld: Incomplete | None = ...,
        name: Incomplete | None = ...,
        description: Incomplete | None = ...,
        stringValue1: Incomplete | None = ...,
        stringValue2: Incomplete | None = ...,
        autoFilter: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
    ) -> None: ...

class PivotFilters(Serialisable):  # type: ignore[misc]
    count: Incomplete
    filter: Incomplete
    __elements__: Incomplete
    def __init__(self, count: Incomplete | None = ..., filter: Incomplete | None = ...) -> None: ...

class PivotTableStyle(Serialisable):
    tagname: str
    name: Incomplete
    showRowHeaders: Incomplete
    showColHeaders: Incomplete
    showRowStripes: Incomplete
    showColStripes: Incomplete
    showLastColumn: Incomplete
    def __init__(
        self,
        name: Incomplete | None = ...,
        showRowHeaders: Incomplete | None = ...,
        showColHeaders: Incomplete | None = ...,
        showRowStripes: Incomplete | None = ...,
        showColStripes: Incomplete | None = ...,
        showLastColumn: Incomplete | None = ...,
    ) -> None: ...

class MemberList(Serialisable):
    tagname: str
    level: Incomplete
    member: Incomplete
    __elements__: Incomplete
    def __init__(self, count: Incomplete | None = ..., level: Incomplete | None = ..., member=...) -> None: ...
    @property
    def count(self): ...

class MemberProperty(Serialisable):
    tagname: str
    name: Incomplete
    showCell: Incomplete
    showTip: Incomplete
    showAsCaption: Incomplete
    nameLen: Incomplete
    pPos: Incomplete
    pLen: Incomplete
    level: Incomplete
    field: Incomplete
    def __init__(
        self,
        name: Incomplete | None = ...,
        showCell: Incomplete | None = ...,
        showTip: Incomplete | None = ...,
        showAsCaption: Incomplete | None = ...,
        nameLen: Incomplete | None = ...,
        pPos: Incomplete | None = ...,
        pLen: Incomplete | None = ...,
        level: Incomplete | None = ...,
        field: Incomplete | None = ...,
    ) -> None: ...

class PivotHierarchy(Serialisable):
    tagname: str
    outline: Incomplete
    multipleItemSelectionAllowed: Incomplete
    subtotalTop: Incomplete
    showInFieldList: Incomplete
    dragToRow: Incomplete
    dragToCol: Incomplete
    dragToPage: Incomplete
    dragToData: Incomplete
    dragOff: Incomplete
    includeNewItemsInFilter: Incomplete
    caption: Incomplete
    mps: Incomplete
    members: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        outline: Incomplete | None = ...,
        multipleItemSelectionAllowed: Incomplete | None = ...,
        subtotalTop: Incomplete | None = ...,
        showInFieldList: Incomplete | None = ...,
        dragToRow: Incomplete | None = ...,
        dragToCol: Incomplete | None = ...,
        dragToPage: Incomplete | None = ...,
        dragToData: Incomplete | None = ...,
        dragOff: Incomplete | None = ...,
        includeNewItemsInFilter: Incomplete | None = ...,
        caption: Incomplete | None = ...,
        mps=...,
        members: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
    ) -> None: ...

class Reference(Serialisable):
    tagname: str
    field: Incomplete
    selected: Incomplete
    byPosition: Incomplete
    relative: Incomplete
    defaultSubtotal: Incomplete
    sumSubtotal: Incomplete
    countASubtotal: Incomplete
    avgSubtotal: Incomplete
    maxSubtotal: Incomplete
    minSubtotal: Incomplete
    productSubtotal: Incomplete
    countSubtotal: Incomplete
    stdDevSubtotal: Incomplete
    stdDevPSubtotal: Incomplete
    varSubtotal: Incomplete
    varPSubtotal: Incomplete
    x: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        field: Incomplete | None = ...,
        count: Incomplete | None = ...,
        selected: Incomplete | None = ...,
        byPosition: Incomplete | None = ...,
        relative: Incomplete | None = ...,
        defaultSubtotal: Incomplete | None = ...,
        sumSubtotal: Incomplete | None = ...,
        countASubtotal: Incomplete | None = ...,
        avgSubtotal: Incomplete | None = ...,
        maxSubtotal: Incomplete | None = ...,
        minSubtotal: Incomplete | None = ...,
        productSubtotal: Incomplete | None = ...,
        countSubtotal: Incomplete | None = ...,
        stdDevSubtotal: Incomplete | None = ...,
        stdDevPSubtotal: Incomplete | None = ...,
        varSubtotal: Incomplete | None = ...,
        varPSubtotal: Incomplete | None = ...,
        x: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
    ) -> None: ...
    @property
    def count(self): ...

class PivotArea(Serialisable):
    tagname: str
    references: Incomplete
    extLst: Incomplete
    field: Incomplete
    type: Incomplete
    dataOnly: Incomplete
    labelOnly: Incomplete
    grandRow: Incomplete
    grandCol: Incomplete
    cacheIndex: Incomplete
    outline: Incomplete
    offset: Incomplete
    collapsedLevelsAreSubtotals: Incomplete
    axis: Incomplete
    fieldPosition: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        references=...,
        extLst: Incomplete | None = ...,
        field: Incomplete | None = ...,
        type: str = ...,
        dataOnly: bool = ...,
        labelOnly: Incomplete | None = ...,
        grandRow: Incomplete | None = ...,
        grandCol: Incomplete | None = ...,
        cacheIndex: Incomplete | None = ...,
        outline: bool = ...,
        offset: Incomplete | None = ...,
        collapsedLevelsAreSubtotals: Incomplete | None = ...,
        axis: Incomplete | None = ...,
        fieldPosition: Incomplete | None = ...,
    ) -> None: ...

class ChartFormat(Serialisable):
    tagname: str
    chart: Incomplete
    format: Incomplete
    series: Incomplete
    pivotArea: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        chart: Incomplete | None = ...,
        format: Incomplete | None = ...,
        series: Incomplete | None = ...,
        pivotArea: Incomplete | None = ...,
    ) -> None: ...

class ConditionalFormat(Serialisable):
    tagname: str
    scope: Incomplete
    type: Incomplete
    priority: Incomplete
    pivotAreas: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        scope: Incomplete | None = ...,
        type: Incomplete | None = ...,
        priority: Incomplete | None = ...,
        pivotAreas=...,
        extLst: Incomplete | None = ...,
    ) -> None: ...

class Format(Serialisable):
    tagname: str
    action: Incomplete
    dxfId: Incomplete
    pivotArea: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        action: str = ...,
        dxfId: Incomplete | None = ...,
        pivotArea: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
    ) -> None: ...

class DataField(Serialisable):
    tagname: str
    name: Incomplete
    fld: Incomplete
    subtotal: Incomplete
    showDataAs: Incomplete
    baseField: Incomplete
    baseItem: Incomplete
    numFmtId: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        name: Incomplete | None = ...,
        fld: Incomplete | None = ...,
        subtotal: str = ...,
        showDataAs: str = ...,
        baseField: int = ...,
        baseItem: int = ...,
        numFmtId: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
    ) -> None: ...

class PageField(Serialisable):
    tagname: str
    fld: Incomplete
    item: Incomplete
    hier: Incomplete
    name: Incomplete
    cap: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        fld: Incomplete | None = ...,
        item: Incomplete | None = ...,
        hier: Incomplete | None = ...,
        name: Incomplete | None = ...,
        cap: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
    ) -> None: ...

class RowColItem(Serialisable):
    tagname: str
    t: Incomplete
    r: Incomplete
    i: Incomplete
    x: Incomplete
    __elements__: Incomplete
    def __init__(self, t: str = ..., r: int = ..., i: int = ..., x=...) -> None: ...

class RowColField(Serialisable):
    tagname: str
    x: Incomplete
    def __init__(self, x: Incomplete | None = ...) -> None: ...

class AutoSortScope(Serialisable):  # type: ignore[misc]
    pivotArea: Incomplete
    __elements__: Incomplete
    def __init__(self, pivotArea: Incomplete | None = ...) -> None: ...

class FieldItem(Serialisable):
    tagname: str
    n: Incomplete
    t: Incomplete
    h: Incomplete
    s: Incomplete
    sd: Incomplete
    f: Incomplete
    m: Incomplete
    c: Incomplete
    x: Incomplete
    d: Incomplete
    e: Incomplete
    def __init__(
        self,
        n: Incomplete | None = ...,
        t: str = ...,
        h: Incomplete | None = ...,
        s: Incomplete | None = ...,
        sd: bool = ...,
        f: Incomplete | None = ...,
        m: Incomplete | None = ...,
        c: Incomplete | None = ...,
        x: Incomplete | None = ...,
        d: Incomplete | None = ...,
        e: Incomplete | None = ...,
    ) -> None: ...

class PivotField(Serialisable):
    tagname: str
    items: Incomplete
    autoSortScope: Incomplete
    extLst: Incomplete
    name: Incomplete
    axis: Incomplete
    dataField: Incomplete
    subtotalCaption: Incomplete
    showDropDowns: Incomplete
    hiddenLevel: Incomplete
    uniqueMemberProperty: Incomplete
    compact: Incomplete
    allDrilled: Incomplete
    numFmtId: Incomplete
    outline: Incomplete
    subtotalTop: Incomplete
    dragToRow: Incomplete
    dragToCol: Incomplete
    multipleItemSelectionAllowed: Incomplete
    dragToPage: Incomplete
    dragToData: Incomplete
    dragOff: Incomplete
    showAll: Incomplete
    insertBlankRow: Incomplete
    serverField: Incomplete
    insertPageBreak: Incomplete
    autoShow: Incomplete
    topAutoShow: Incomplete
    hideNewItems: Incomplete
    measureFilter: Incomplete
    includeNewItemsInFilter: Incomplete
    itemPageCount: Incomplete
    sortType: Incomplete
    dataSourceSort: Incomplete
    nonAutoSortDefault: Incomplete
    rankBy: Incomplete
    defaultSubtotal: Incomplete
    sumSubtotal: Incomplete
    countASubtotal: Incomplete
    avgSubtotal: Incomplete
    maxSubtotal: Incomplete
    minSubtotal: Incomplete
    productSubtotal: Incomplete
    countSubtotal: Incomplete
    stdDevSubtotal: Incomplete
    stdDevPSubtotal: Incomplete
    varSubtotal: Incomplete
    varPSubtotal: Incomplete
    showPropCell: Incomplete
    showPropTip: Incomplete
    showPropAsCaption: Incomplete
    defaultAttributeDrillState: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        items=...,
        autoSortScope: Incomplete | None = ...,
        name: Incomplete | None = ...,
        axis: Incomplete | None = ...,
        dataField: Incomplete | None = ...,
        subtotalCaption: Incomplete | None = ...,
        showDropDowns: bool = ...,
        hiddenLevel: Incomplete | None = ...,
        uniqueMemberProperty: Incomplete | None = ...,
        compact: bool = ...,
        allDrilled: Incomplete | None = ...,
        numFmtId: Incomplete | None = ...,
        outline: bool = ...,
        subtotalTop: bool = ...,
        dragToRow: bool = ...,
        dragToCol: bool = ...,
        multipleItemSelectionAllowed: Incomplete | None = ...,
        dragToPage: bool = ...,
        dragToData: bool = ...,
        dragOff: bool = ...,
        showAll: bool = ...,
        insertBlankRow: Incomplete | None = ...,
        serverField: Incomplete | None = ...,
        insertPageBreak: Incomplete | None = ...,
        autoShow: Incomplete | None = ...,
        topAutoShow: bool = ...,
        hideNewItems: Incomplete | None = ...,
        measureFilter: Incomplete | None = ...,
        includeNewItemsInFilter: Incomplete | None = ...,
        itemPageCount: int = ...,
        sortType: str = ...,
        dataSourceSort: Incomplete | None = ...,
        nonAutoSortDefault: Incomplete | None = ...,
        rankBy: Incomplete | None = ...,
        defaultSubtotal: bool = ...,
        sumSubtotal: Incomplete | None = ...,
        countASubtotal: Incomplete | None = ...,
        avgSubtotal: Incomplete | None = ...,
        maxSubtotal: Incomplete | None = ...,
        minSubtotal: Incomplete | None = ...,
        productSubtotal: Incomplete | None = ...,
        countSubtotal: Incomplete | None = ...,
        stdDevSubtotal: Incomplete | None = ...,
        stdDevPSubtotal: Incomplete | None = ...,
        varSubtotal: Incomplete | None = ...,
        varPSubtotal: Incomplete | None = ...,
        showPropCell: Incomplete | None = ...,
        showPropTip: Incomplete | None = ...,
        showPropAsCaption: Incomplete | None = ...,
        defaultAttributeDrillState: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
    ) -> None: ...

class Location(Serialisable):
    tagname: str
    ref: Incomplete
    firstHeaderRow: Incomplete
    firstDataRow: Incomplete
    firstDataCol: Incomplete
    rowPageCount: Incomplete
    colPageCount: Incomplete
    def __init__(
        self,
        ref: Incomplete | None = ...,
        firstHeaderRow: Incomplete | None = ...,
        firstDataRow: Incomplete | None = ...,
        firstDataCol: Incomplete | None = ...,
        rowPageCount: Incomplete | None = ...,
        colPageCount: Incomplete | None = ...,
    ) -> None: ...

class TableDefinition(Serialisable):
    mime_type: str
    rel_type: str
    tagname: str
    cache: Incomplete
    name: Incomplete
    cacheId: Incomplete
    dataOnRows: Incomplete
    dataPosition: Incomplete
    dataCaption: Incomplete
    grandTotalCaption: Incomplete
    errorCaption: Incomplete
    showError: Incomplete
    missingCaption: Incomplete
    showMissing: Incomplete
    pageStyle: Incomplete
    pivotTableStyle: Incomplete
    vacatedStyle: Incomplete
    tag: Incomplete
    updatedVersion: Incomplete
    minRefreshableVersion: Incomplete
    asteriskTotals: Incomplete
    showItems: Incomplete
    editData: Incomplete
    disableFieldList: Incomplete
    showCalcMbrs: Incomplete
    visualTotals: Incomplete
    showMultipleLabel: Incomplete
    showDataDropDown: Incomplete
    showDrill: Incomplete
    printDrill: Incomplete
    showMemberPropertyTips: Incomplete
    showDataTips: Incomplete
    enableWizard: Incomplete
    enableDrill: Incomplete
    enableFieldProperties: Incomplete
    preserveFormatting: Incomplete
    useAutoFormatting: Incomplete
    pageWrap: Incomplete
    pageOverThenDown: Incomplete
    subtotalHiddenItems: Incomplete
    rowGrandTotals: Incomplete
    colGrandTotals: Incomplete
    fieldPrintTitles: Incomplete
    itemPrintTitles: Incomplete
    mergeItem: Incomplete
    showDropZones: Incomplete
    createdVersion: Incomplete
    indent: Incomplete
    showEmptyRow: Incomplete
    showEmptyCol: Incomplete
    showHeaders: Incomplete
    compact: Incomplete
    outline: Incomplete
    outlineData: Incomplete
    compactData: Incomplete
    published: Incomplete
    gridDropZones: Incomplete
    immersive: Incomplete
    multipleFieldFilters: Incomplete
    chartFormat: Incomplete
    rowHeaderCaption: Incomplete
    colHeaderCaption: Incomplete
    fieldListSortAscending: Incomplete
    mdxSubqueries: Incomplete
    customListSort: Incomplete
    autoFormatId: Incomplete
    applyNumberFormats: Incomplete
    applyBorderFormats: Incomplete
    applyFontFormats: Incomplete
    applyPatternFormats: Incomplete
    applyAlignmentFormats: Incomplete
    applyWidthHeightFormats: Incomplete
    location: Incomplete
    pivotFields: Incomplete
    rowFields: Incomplete
    rowItems: Incomplete
    colFields: Incomplete
    colItems: Incomplete
    pageFields: Incomplete
    dataFields: Incomplete
    formats: Incomplete
    conditionalFormats: Incomplete
    chartFormats: Incomplete
    pivotHierarchies: Incomplete
    pivotTableStyleInfo: Incomplete
    filters: Incomplete
    rowHierarchiesUsage: Incomplete
    colHierarchiesUsage: Incomplete
    extLst: Incomplete
    id: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        name: Incomplete | None = ...,
        cacheId: Incomplete | None = ...,
        dataOnRows: bool = ...,
        dataPosition: Incomplete | None = ...,
        dataCaption: Incomplete | None = ...,
        grandTotalCaption: Incomplete | None = ...,
        errorCaption: Incomplete | None = ...,
        showError: bool = ...,
        missingCaption: Incomplete | None = ...,
        showMissing: bool = ...,
        pageStyle: Incomplete | None = ...,
        pivotTableStyle: Incomplete | None = ...,
        vacatedStyle: Incomplete | None = ...,
        tag: Incomplete | None = ...,
        updatedVersion: int = ...,
        minRefreshableVersion: int = ...,
        asteriskTotals: bool = ...,
        showItems: bool = ...,
        editData: bool = ...,
        disableFieldList: bool = ...,
        showCalcMbrs: bool = ...,
        visualTotals: bool = ...,
        showMultipleLabel: bool = ...,
        showDataDropDown: bool = ...,
        showDrill: bool = ...,
        printDrill: bool = ...,
        showMemberPropertyTips: bool = ...,
        showDataTips: bool = ...,
        enableWizard: bool = ...,
        enableDrill: bool = ...,
        enableFieldProperties: bool = ...,
        preserveFormatting: bool = ...,
        useAutoFormatting: bool = ...,
        pageWrap: int = ...,
        pageOverThenDown: bool = ...,
        subtotalHiddenItems: bool = ...,
        rowGrandTotals: bool = ...,
        colGrandTotals: bool = ...,
        fieldPrintTitles: bool = ...,
        itemPrintTitles: bool = ...,
        mergeItem: bool = ...,
        showDropZones: bool = ...,
        createdVersion: int = ...,
        indent: int = ...,
        showEmptyRow: bool = ...,
        showEmptyCol: bool = ...,
        showHeaders: bool = ...,
        compact: bool = ...,
        outline: bool = ...,
        outlineData: bool = ...,
        compactData: bool = ...,
        published: bool = ...,
        gridDropZones: bool = ...,
        immersive: bool = ...,
        multipleFieldFilters: Incomplete | None = ...,
        chartFormat: int = ...,
        rowHeaderCaption: Incomplete | None = ...,
        colHeaderCaption: Incomplete | None = ...,
        fieldListSortAscending: Incomplete | None = ...,
        mdxSubqueries: Incomplete | None = ...,
        customListSort: Incomplete | None = ...,
        autoFormatId: Incomplete | None = ...,
        applyNumberFormats: bool = ...,
        applyBorderFormats: bool = ...,
        applyFontFormats: bool = ...,
        applyPatternFormats: bool = ...,
        applyAlignmentFormats: bool = ...,
        applyWidthHeightFormats: bool = ...,
        location: Incomplete | None = ...,
        pivotFields=...,
        rowFields=...,
        rowItems=...,
        colFields=...,
        colItems=...,
        pageFields=...,
        dataFields=...,
        formats=...,
        conditionalFormats=...,
        chartFormats=...,
        pivotHierarchies=...,
        pivotTableStyleInfo: Incomplete | None = ...,
        filters=...,
        rowHierarchiesUsage: Incomplete | None = ...,
        colHierarchiesUsage: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
        id: Incomplete | None = ...,
    ) -> None: ...
    def to_tree(self): ...
    @property
    def path(self): ...
