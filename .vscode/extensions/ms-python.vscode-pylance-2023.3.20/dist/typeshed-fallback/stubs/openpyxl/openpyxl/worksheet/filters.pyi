from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

class SortCondition(Serialisable):
    tagname: str
    descending: Incomplete
    sortBy: Incomplete
    ref: Incomplete
    customList: Incomplete
    dxfId: Incomplete
    iconSet: Incomplete
    iconId: Incomplete
    def __init__(
        self,
        ref: Incomplete | None = ...,
        descending: Incomplete | None = ...,
        sortBy: Incomplete | None = ...,
        customList: Incomplete | None = ...,
        dxfId: Incomplete | None = ...,
        iconSet: Incomplete | None = ...,
        iconId: Incomplete | None = ...,
    ) -> None: ...

class SortState(Serialisable):
    tagname: str
    columnSort: Incomplete
    caseSensitive: Incomplete
    sortMethod: Incomplete
    ref: Incomplete
    sortCondition: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        columnSort: Incomplete | None = ...,
        caseSensitive: Incomplete | None = ...,
        sortMethod: Incomplete | None = ...,
        ref: Incomplete | None = ...,
        sortCondition=...,
        extLst: Incomplete | None = ...,
    ) -> None: ...
    def __bool__(self) -> bool: ...

class IconFilter(Serialisable):
    tagname: str
    iconSet: Incomplete
    iconId: Incomplete
    def __init__(self, iconSet: Incomplete | None = ..., iconId: Incomplete | None = ...) -> None: ...

class ColorFilter(Serialisable):
    tagname: str
    dxfId: Incomplete
    cellColor: Incomplete
    def __init__(self, dxfId: Incomplete | None = ..., cellColor: Incomplete | None = ...) -> None: ...

class DynamicFilter(Serialisable):
    tagname: str
    type: Incomplete
    val: Incomplete
    valIso: Incomplete
    maxVal: Incomplete
    maxValIso: Incomplete
    def __init__(
        self,
        type: Incomplete | None = ...,
        val: Incomplete | None = ...,
        valIso: Incomplete | None = ...,
        maxVal: Incomplete | None = ...,
        maxValIso: Incomplete | None = ...,
    ) -> None: ...

class CustomFilter(Serialisable):
    tagname: str
    operator: Incomplete
    val: Incomplete
    def __init__(self, operator: Incomplete | None = ..., val: Incomplete | None = ...) -> None: ...

class CustomFilters(Serialisable):
    tagname: str
    customFilter: Incomplete
    __elements__: Incomplete
    def __init__(self, _and: Incomplete | None = ..., customFilter=...) -> None: ...

class Top10(Serialisable):
    tagname: str
    top: Incomplete
    percent: Incomplete
    val: Incomplete
    filterVal: Incomplete
    def __init__(
        self,
        top: Incomplete | None = ...,
        percent: Incomplete | None = ...,
        val: Incomplete | None = ...,
        filterVal: Incomplete | None = ...,
    ) -> None: ...

class DateGroupItem(Serialisable):
    tagname: str
    year: Incomplete
    month: Incomplete
    day: Incomplete
    hour: Incomplete
    minute: Incomplete
    second: Incomplete
    dateTimeGrouping: Incomplete
    def __init__(
        self,
        year: Incomplete | None = ...,
        month: Incomplete | None = ...,
        day: Incomplete | None = ...,
        hour: Incomplete | None = ...,
        minute: Incomplete | None = ...,
        second: Incomplete | None = ...,
        dateTimeGrouping: Incomplete | None = ...,
    ) -> None: ...

class Filters(Serialisable):
    tagname: str
    blank: Incomplete
    calendarType: Incomplete
    filter: Incomplete
    dateGroupItem: Incomplete
    __elements__: Incomplete
    def __init__(
        self, blank: Incomplete | None = ..., calendarType: Incomplete | None = ..., filter=..., dateGroupItem=...
    ) -> None: ...

class FilterColumn(Serialisable):
    tagname: str
    colId: Incomplete
    col_id: Incomplete
    hiddenButton: Incomplete
    showButton: Incomplete
    filters: Incomplete
    top10: Incomplete
    customFilters: Incomplete
    dynamicFilter: Incomplete
    colorFilter: Incomplete
    iconFilter: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        colId: Incomplete | None = ...,
        hiddenButton: Incomplete | None = ...,
        showButton: Incomplete | None = ...,
        filters: Incomplete | None = ...,
        top10: Incomplete | None = ...,
        customFilters: Incomplete | None = ...,
        dynamicFilter: Incomplete | None = ...,
        colorFilter: Incomplete | None = ...,
        iconFilter: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
        blank: Incomplete | None = ...,
        vals: Incomplete | None = ...,
    ) -> None: ...

class AutoFilter(Serialisable):
    tagname: str
    ref: Incomplete
    filterColumn: Incomplete
    sortState: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(
        self, ref: Incomplete | None = ..., filterColumn=..., sortState: Incomplete | None = ..., extLst: Incomplete | None = ...
    ) -> None: ...
    def __bool__(self) -> bool: ...
    def add_filter_column(self, col_id, vals, blank: bool = ...) -> None: ...
    def add_sort_condition(self, ref, descending: bool = ...) -> None: ...
