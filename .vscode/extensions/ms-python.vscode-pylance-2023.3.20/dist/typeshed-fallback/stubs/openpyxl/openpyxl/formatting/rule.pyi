from _typeshed import Incomplete

from openpyxl.descriptors import Float
from openpyxl.descriptors.serialisable import Serialisable

class ValueDescriptor(Float):
    expected_type: Incomplete
    def __set__(self, instance, value) -> None: ...

class FormatObject(Serialisable):
    tagname: str
    type: Incomplete
    val: Incomplete
    gte: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(
        self, type, val: Incomplete | None = ..., gte: Incomplete | None = ..., extLst: Incomplete | None = ...
    ) -> None: ...

class RuleType(Serialisable):  # type: ignore[misc]
    cfvo: Incomplete

class IconSet(RuleType):
    tagname: str
    iconSet: Incomplete
    showValue: Incomplete
    percent: Incomplete
    reverse: Incomplete
    __elements__: Incomplete
    cfvo: Incomplete
    def __init__(
        self,
        iconSet: Incomplete | None = ...,
        showValue: Incomplete | None = ...,
        percent: Incomplete | None = ...,
        reverse: Incomplete | None = ...,
        cfvo: Incomplete | None = ...,
    ) -> None: ...

class DataBar(RuleType):
    tagname: str
    minLength: Incomplete
    maxLength: Incomplete
    showValue: Incomplete
    color: Incomplete
    __elements__: Incomplete
    cfvo: Incomplete
    def __init__(
        self,
        minLength: Incomplete | None = ...,
        maxLength: Incomplete | None = ...,
        showValue: Incomplete | None = ...,
        cfvo: Incomplete | None = ...,
        color: Incomplete | None = ...,
    ) -> None: ...

class ColorScale(RuleType):
    tagname: str
    color: Incomplete
    __elements__: Incomplete
    cfvo: Incomplete
    def __init__(self, cfvo: Incomplete | None = ..., color: Incomplete | None = ...) -> None: ...

class Rule(Serialisable):
    tagname: str
    type: Incomplete
    dxfId: Incomplete
    priority: Incomplete
    stopIfTrue: Incomplete
    aboveAverage: Incomplete
    percent: Incomplete
    bottom: Incomplete
    operator: Incomplete
    text: Incomplete
    timePeriod: Incomplete
    rank: Incomplete
    stdDev: Incomplete
    equalAverage: Incomplete
    formula: Incomplete
    colorScale: Incomplete
    dataBar: Incomplete
    iconSet: Incomplete
    extLst: Incomplete
    dxf: Incomplete
    __elements__: Incomplete
    __attrs__: Incomplete
    def __init__(
        self,
        type,
        dxfId: Incomplete | None = ...,
        priority: int = ...,
        stopIfTrue: Incomplete | None = ...,
        aboveAverage: Incomplete | None = ...,
        percent: Incomplete | None = ...,
        bottom: Incomplete | None = ...,
        operator: Incomplete | None = ...,
        text: Incomplete | None = ...,
        timePeriod: Incomplete | None = ...,
        rank: Incomplete | None = ...,
        stdDev: Incomplete | None = ...,
        equalAverage: Incomplete | None = ...,
        formula=...,
        colorScale: Incomplete | None = ...,
        dataBar: Incomplete | None = ...,
        iconSet: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
        dxf: Incomplete | None = ...,
    ) -> None: ...

def ColorScaleRule(
    start_type: Incomplete | None = ...,
    start_value: Incomplete | None = ...,
    start_color: Incomplete | None = ...,
    mid_type: Incomplete | None = ...,
    mid_value: Incomplete | None = ...,
    mid_color: Incomplete | None = ...,
    end_type: Incomplete | None = ...,
    end_value: Incomplete | None = ...,
    end_color: Incomplete | None = ...,
): ...
def FormulaRule(
    formula: Incomplete | None = ...,
    stopIfTrue: Incomplete | None = ...,
    font: Incomplete | None = ...,
    border: Incomplete | None = ...,
    fill: Incomplete | None = ...,
): ...
def CellIsRule(
    operator: Incomplete | None = ...,
    formula: Incomplete | None = ...,
    stopIfTrue: Incomplete | None = ...,
    font: Incomplete | None = ...,
    border: Incomplete | None = ...,
    fill: Incomplete | None = ...,
): ...
def IconSetRule(
    icon_style: Incomplete | None = ...,
    type: Incomplete | None = ...,
    values: Incomplete | None = ...,
    showValue: Incomplete | None = ...,
    percent: Incomplete | None = ...,
    reverse: Incomplete | None = ...,
): ...
def DataBarRule(
    start_type: Incomplete | None = ...,
    start_value: Incomplete | None = ...,
    end_type: Incomplete | None = ...,
    end_value: Incomplete | None = ...,
    color: Incomplete | None = ...,
    showValue: Incomplete | None = ...,
    minLength: Incomplete | None = ...,
    maxLength: Incomplete | None = ...,
): ...
