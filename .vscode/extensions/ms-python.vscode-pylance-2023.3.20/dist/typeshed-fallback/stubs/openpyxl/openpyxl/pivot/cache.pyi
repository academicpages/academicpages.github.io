from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

class MeasureDimensionMap(Serialisable):
    tagname: str
    measureGroup: Incomplete
    dimension: Incomplete
    def __init__(self, measureGroup: Incomplete | None = ..., dimension: Incomplete | None = ...) -> None: ...

class MeasureGroup(Serialisable):
    tagname: str
    name: Incomplete
    caption: Incomplete
    def __init__(self, name: Incomplete | None = ..., caption: Incomplete | None = ...) -> None: ...

class PivotDimension(Serialisable):
    tagname: str
    measure: Incomplete
    name: Incomplete
    uniqueName: Incomplete
    caption: Incomplete
    def __init__(
        self,
        measure: Incomplete | None = ...,
        name: Incomplete | None = ...,
        uniqueName: Incomplete | None = ...,
        caption: Incomplete | None = ...,
    ) -> None: ...

class CalculatedMember(Serialisable):
    tagname: str
    name: Incomplete
    mdx: Incomplete
    memberName: Incomplete
    hierarchy: Incomplete
    parent: Incomplete
    solveOrder: Incomplete
    set: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        name: Incomplete | None = ...,
        mdx: Incomplete | None = ...,
        memberName: Incomplete | None = ...,
        hierarchy: Incomplete | None = ...,
        parent: Incomplete | None = ...,
        solveOrder: Incomplete | None = ...,
        set: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
    ) -> None: ...

class CalculatedItem(Serialisable):
    tagname: str
    field: Incomplete
    formula: Incomplete
    pivotArea: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        field: Incomplete | None = ...,
        formula: Incomplete | None = ...,
        pivotArea: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
    ) -> None: ...

class ServerFormat(Serialisable):
    tagname: str
    culture: Incomplete
    format: Incomplete
    def __init__(self, culture: Incomplete | None = ..., format: Incomplete | None = ...) -> None: ...

class ServerFormatList(Serialisable):
    tagname: str
    serverFormat: Incomplete
    __elements__: Incomplete
    __attrs__: Incomplete
    def __init__(self, count: Incomplete | None = ..., serverFormat: Incomplete | None = ...) -> None: ...
    @property
    def count(self): ...

class Query(Serialisable):
    tagname: str
    mdx: Incomplete
    tpls: Incomplete
    __elements__: Incomplete
    def __init__(self, mdx: Incomplete | None = ..., tpls: Incomplete | None = ...) -> None: ...

class QueryCache(Serialisable):
    tagname: str
    count: Incomplete
    query: Incomplete
    __elements__: Incomplete
    def __init__(self, count: Incomplete | None = ..., query: Incomplete | None = ...) -> None: ...

class OLAPSet(Serialisable):
    tagname: str
    count: Incomplete
    maxRank: Incomplete
    setDefinition: Incomplete
    sortType: Incomplete
    queryFailed: Incomplete
    tpls: Incomplete
    sortByTuple: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        count: Incomplete | None = ...,
        maxRank: Incomplete | None = ...,
        setDefinition: Incomplete | None = ...,
        sortType: Incomplete | None = ...,
        queryFailed: Incomplete | None = ...,
        tpls: Incomplete | None = ...,
        sortByTuple: Incomplete | None = ...,
    ) -> None: ...

class OLAPSets(Serialisable):  # type: ignore[misc]
    count: Incomplete
    set: Incomplete
    __elements__: Incomplete
    def __init__(self, count: Incomplete | None = ..., set: Incomplete | None = ...) -> None: ...

class PCDSDTCEntries(Serialisable):
    tagname: str
    count: Incomplete
    m: Incomplete
    n: Incomplete
    e: Incomplete
    s: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        count: Incomplete | None = ...,
        m: Incomplete | None = ...,
        n: Incomplete | None = ...,
        e: Incomplete | None = ...,
        s: Incomplete | None = ...,
    ) -> None: ...

class TupleCache(Serialisable):
    tagname: str
    entries: Incomplete
    sets: Incomplete
    queryCache: Incomplete
    serverFormats: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        entries: Incomplete | None = ...,
        sets: Incomplete | None = ...,
        queryCache: Incomplete | None = ...,
        serverFormats: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
    ) -> None: ...

class PCDKPI(Serialisable):
    tagname: str
    uniqueName: Incomplete
    caption: Incomplete
    displayFolder: Incomplete
    measureGroup: Incomplete
    parent: Incomplete
    value: Incomplete
    goal: Incomplete
    status: Incomplete
    trend: Incomplete
    weight: Incomplete
    time: Incomplete
    def __init__(
        self,
        uniqueName: Incomplete | None = ...,
        caption: Incomplete | None = ...,
        displayFolder: Incomplete | None = ...,
        measureGroup: Incomplete | None = ...,
        parent: Incomplete | None = ...,
        value: Incomplete | None = ...,
        goal: Incomplete | None = ...,
        status: Incomplete | None = ...,
        trend: Incomplete | None = ...,
        weight: Incomplete | None = ...,
        time: Incomplete | None = ...,
    ) -> None: ...

class GroupMember(Serialisable):
    tagname: str
    uniqueName: Incomplete
    group: Incomplete
    def __init__(self, uniqueName: Incomplete | None = ..., group: Incomplete | None = ...) -> None: ...

class GroupMembers(Serialisable):  # type: ignore[misc]
    count: Incomplete
    groupMember: Incomplete
    __elements__: Incomplete
    def __init__(self, count: Incomplete | None = ..., groupMember: Incomplete | None = ...) -> None: ...

class LevelGroup(Serialisable):
    tagname: str
    name: Incomplete
    uniqueName: Incomplete
    caption: Incomplete
    uniqueParent: Incomplete
    id: Incomplete
    groupMembers: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        name: Incomplete | None = ...,
        uniqueName: Incomplete | None = ...,
        caption: Incomplete | None = ...,
        uniqueParent: Incomplete | None = ...,
        id: Incomplete | None = ...,
        groupMembers: Incomplete | None = ...,
    ) -> None: ...

class Groups(Serialisable):
    tagname: str
    count: Incomplete
    group: Incomplete
    __elements__: Incomplete
    def __init__(self, count: Incomplete | None = ..., group: Incomplete | None = ...) -> None: ...

class GroupLevel(Serialisable):
    tagname: str
    uniqueName: Incomplete
    caption: Incomplete
    user: Incomplete
    customRollUp: Incomplete
    groups: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        uniqueName: Incomplete | None = ...,
        caption: Incomplete | None = ...,
        user: Incomplete | None = ...,
        customRollUp: Incomplete | None = ...,
        groups: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
    ) -> None: ...

class GroupLevels(Serialisable):  # type: ignore[misc]
    count: Incomplete
    groupLevel: Incomplete
    __elements__: Incomplete
    def __init__(self, count: Incomplete | None = ..., groupLevel: Incomplete | None = ...) -> None: ...

class FieldUsage(Serialisable):
    tagname: str
    x: Incomplete
    def __init__(self, x: Incomplete | None = ...) -> None: ...

class FieldsUsage(Serialisable):  # type: ignore[misc]
    count: Incomplete
    fieldUsage: Incomplete
    __elements__: Incomplete
    def __init__(self, count: Incomplete | None = ..., fieldUsage: Incomplete | None = ...) -> None: ...

class CacheHierarchy(Serialisable):
    tagname: str
    uniqueName: Incomplete
    caption: Incomplete
    measure: Incomplete
    set: Incomplete
    parentSet: Incomplete
    iconSet: Incomplete
    attribute: Incomplete
    time: Incomplete
    keyAttribute: Incomplete
    defaultMemberUniqueName: Incomplete
    allUniqueName: Incomplete
    allCaption: Incomplete
    dimensionUniqueName: Incomplete
    displayFolder: Incomplete
    measureGroup: Incomplete
    measures: Incomplete
    count: Incomplete
    oneField: Incomplete
    memberValueDatatype: Incomplete
    unbalanced: Incomplete
    unbalancedGroup: Incomplete
    hidden: Incomplete
    fieldsUsage: Incomplete
    groupLevels: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        uniqueName: str = ...,
        caption: Incomplete | None = ...,
        measure: Incomplete | None = ...,
        set: Incomplete | None = ...,
        parentSet: Incomplete | None = ...,
        iconSet: int = ...,
        attribute: Incomplete | None = ...,
        time: Incomplete | None = ...,
        keyAttribute: Incomplete | None = ...,
        defaultMemberUniqueName: Incomplete | None = ...,
        allUniqueName: Incomplete | None = ...,
        allCaption: Incomplete | None = ...,
        dimensionUniqueName: Incomplete | None = ...,
        displayFolder: Incomplete | None = ...,
        measureGroup: Incomplete | None = ...,
        measures: Incomplete | None = ...,
        count: Incomplete | None = ...,
        oneField: Incomplete | None = ...,
        memberValueDatatype: Incomplete | None = ...,
        unbalanced: Incomplete | None = ...,
        unbalancedGroup: Incomplete | None = ...,
        hidden: Incomplete | None = ...,
        fieldsUsage: Incomplete | None = ...,
        groupLevels: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
    ) -> None: ...

class GroupItems(Serialisable):
    tagname: str
    m: Incomplete
    n: Incomplete
    b: Incomplete
    e: Incomplete
    s: Incomplete
    d: Incomplete
    __elements__: Incomplete
    __attrs__: Incomplete
    def __init__(self, count: Incomplete | None = ..., m=..., n=..., b=..., e=..., s=..., d=...) -> None: ...
    @property
    def count(self): ...

class DiscretePr(Serialisable):
    tagname: str
    count: Incomplete
    x: Incomplete
    __elements__: Incomplete
    def __init__(self, count: Incomplete | None = ..., x: Incomplete | None = ...) -> None: ...

class RangePr(Serialisable):
    tagname: str
    autoStart: Incomplete
    autoEnd: Incomplete
    groupBy: Incomplete
    startNum: Incomplete
    endNum: Incomplete
    startDate: Incomplete
    endDate: Incomplete
    groupInterval: Incomplete
    def __init__(
        self,
        autoStart: bool = ...,
        autoEnd: bool = ...,
        groupBy: str = ...,
        startNum: Incomplete | None = ...,
        endNum: Incomplete | None = ...,
        startDate: Incomplete | None = ...,
        endDate: Incomplete | None = ...,
        groupInterval: int = ...,
    ) -> None: ...

class FieldGroup(Serialisable):
    tagname: str
    par: Incomplete
    base: Incomplete
    rangePr: Incomplete
    discretePr: Incomplete
    groupItems: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        par: Incomplete | None = ...,
        base: Incomplete | None = ...,
        rangePr: Incomplete | None = ...,
        discretePr: Incomplete | None = ...,
        groupItems: Incomplete | None = ...,
    ) -> None: ...

class SharedItems(Serialisable):
    tagname: str
    m: Incomplete
    n: Incomplete
    b: Incomplete
    e: Incomplete
    s: Incomplete
    d: Incomplete
    containsSemiMixedTypes: Incomplete
    containsNonDate: Incomplete
    containsDate: Incomplete
    containsString: Incomplete
    containsBlank: Incomplete
    containsMixedTypes: Incomplete
    containsNumber: Incomplete
    containsInteger: Incomplete
    minValue: Incomplete
    maxValue: Incomplete
    minDate: Incomplete
    maxDate: Incomplete
    longText: Incomplete
    __attrs__: Incomplete
    def __init__(
        self,
        _fields=...,
        containsSemiMixedTypes: Incomplete | None = ...,
        containsNonDate: Incomplete | None = ...,
        containsDate: Incomplete | None = ...,
        containsString: Incomplete | None = ...,
        containsBlank: Incomplete | None = ...,
        containsMixedTypes: Incomplete | None = ...,
        containsNumber: Incomplete | None = ...,
        containsInteger: Incomplete | None = ...,
        minValue: Incomplete | None = ...,
        maxValue: Incomplete | None = ...,
        minDate: Incomplete | None = ...,
        maxDate: Incomplete | None = ...,
        count: Incomplete | None = ...,
        longText: Incomplete | None = ...,
    ) -> None: ...
    @property
    def count(self): ...

class CacheField(Serialisable):
    tagname: str
    sharedItems: Incomplete
    fieldGroup: Incomplete
    mpMap: Incomplete
    extLst: Incomplete
    name: Incomplete
    caption: Incomplete
    propertyName: Incomplete
    serverField: Incomplete
    uniqueList: Incomplete
    numFmtId: Incomplete
    formula: Incomplete
    sqlType: Incomplete
    hierarchy: Incomplete
    level: Incomplete
    databaseField: Incomplete
    mappingCount: Incomplete
    memberPropertyField: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        sharedItems: Incomplete | None = ...,
        fieldGroup: Incomplete | None = ...,
        mpMap: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
        name: Incomplete | None = ...,
        caption: Incomplete | None = ...,
        propertyName: Incomplete | None = ...,
        serverField: Incomplete | None = ...,
        uniqueList: bool = ...,
        numFmtId: Incomplete | None = ...,
        formula: Incomplete | None = ...,
        sqlType: int = ...,
        hierarchy: int = ...,
        level: int = ...,
        databaseField: bool = ...,
        mappingCount: Incomplete | None = ...,
        memberPropertyField: Incomplete | None = ...,
    ) -> None: ...

class RangeSet(Serialisable):
    tagname: str
    i1: Incomplete
    i2: Incomplete
    i3: Incomplete
    i4: Incomplete
    ref: Incomplete
    name: Incomplete
    sheet: Incomplete
    def __init__(
        self,
        i1: Incomplete | None = ...,
        i2: Incomplete | None = ...,
        i3: Incomplete | None = ...,
        i4: Incomplete | None = ...,
        ref: Incomplete | None = ...,
        name: Incomplete | None = ...,
        sheet: Incomplete | None = ...,
    ) -> None: ...

class PageItem(Serialisable):
    tagname: str
    name: Incomplete
    def __init__(self, name: Incomplete | None = ...) -> None: ...

class Page(Serialisable):
    tagname: str
    pageItem: Incomplete
    __elements__: Incomplete
    def __init__(self, count: Incomplete | None = ..., pageItem: Incomplete | None = ...) -> None: ...
    @property
    def count(self): ...

class Consolidation(Serialisable):
    tagname: str
    autoPage: Incomplete
    pages: Incomplete
    rangeSets: Incomplete
    __elements__: Incomplete
    def __init__(self, autoPage: Incomplete | None = ..., pages=..., rangeSets=...) -> None: ...

class WorksheetSource(Serialisable):
    tagname: str
    ref: Incomplete
    name: Incomplete
    sheet: Incomplete
    def __init__(self, ref: Incomplete | None = ..., name: Incomplete | None = ..., sheet: Incomplete | None = ...) -> None: ...

class CacheSource(Serialisable):
    tagname: str
    type: Incomplete
    connectionId: Incomplete
    worksheetSource: Incomplete
    consolidation: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        type: Incomplete | None = ...,
        connectionId: Incomplete | None = ...,
        worksheetSource: Incomplete | None = ...,
        consolidation: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
    ) -> None: ...

class CacheDefinition(Serialisable):
    mime_type: str
    rel_type: str
    records: Incomplete
    tagname: str
    invalid: Incomplete
    saveData: Incomplete
    refreshOnLoad: Incomplete
    optimizeMemory: Incomplete
    enableRefresh: Incomplete
    refreshedBy: Incomplete
    refreshedDate: Incomplete
    refreshedDateIso: Incomplete
    backgroundQuery: Incomplete
    missingItemsLimit: Incomplete
    createdVersion: Incomplete
    refreshedVersion: Incomplete
    minRefreshableVersion: Incomplete
    recordCount: Incomplete
    upgradeOnRefresh: Incomplete
    tupleCache: Incomplete
    supportSubquery: Incomplete
    supportAdvancedDrill: Incomplete
    cacheSource: Incomplete
    cacheFields: Incomplete
    cacheHierarchies: Incomplete
    kpis: Incomplete
    calculatedItems: Incomplete
    calculatedMembers: Incomplete
    dimensions: Incomplete
    measureGroups: Incomplete
    maps: Incomplete
    extLst: Incomplete
    id: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        invalid: Incomplete | None = ...,
        saveData: Incomplete | None = ...,
        refreshOnLoad: Incomplete | None = ...,
        optimizeMemory: Incomplete | None = ...,
        enableRefresh: Incomplete | None = ...,
        refreshedBy: Incomplete | None = ...,
        refreshedDate: Incomplete | None = ...,
        refreshedDateIso: Incomplete | None = ...,
        backgroundQuery: Incomplete | None = ...,
        missingItemsLimit: Incomplete | None = ...,
        createdVersion: Incomplete | None = ...,
        refreshedVersion: Incomplete | None = ...,
        minRefreshableVersion: Incomplete | None = ...,
        recordCount: Incomplete | None = ...,
        upgradeOnRefresh: Incomplete | None = ...,
        tupleCache: Incomplete | None = ...,
        supportSubquery: Incomplete | None = ...,
        supportAdvancedDrill: Incomplete | None = ...,
        cacheSource: Incomplete | None = ...,
        cacheFields=...,
        cacheHierarchies=...,
        kpis=...,
        calculatedItems=...,
        calculatedMembers=...,
        dimensions=...,
        measureGroups=...,
        maps=...,
        extLst: Incomplete | None = ...,
        id: Incomplete | None = ...,
    ) -> None: ...
    def to_tree(self): ...
    @property
    def path(self): ...
