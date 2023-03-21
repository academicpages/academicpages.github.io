from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

attribute_mapping: Incomplete

class SeriesLabel(Serialisable):
    tagname: str
    strRef: Incomplete
    v: Incomplete
    value: Incomplete
    __elements__: Incomplete
    def __init__(self, strRef: Incomplete | None = ..., v: Incomplete | None = ...) -> None: ...

class Series(Serialisable):
    tagname: str
    idx: Incomplete
    order: Incomplete
    tx: Incomplete
    title: Incomplete
    spPr: Incomplete
    graphicalProperties: Incomplete
    pictureOptions: Incomplete
    dPt: Incomplete
    data_points: Incomplete
    dLbls: Incomplete
    labels: Incomplete
    trendline: Incomplete
    errBars: Incomplete
    cat: Incomplete
    identifiers: Incomplete
    val: Incomplete
    extLst: Incomplete
    invertIfNegative: Incomplete
    shape: Incomplete
    xVal: Incomplete
    yVal: Incomplete
    bubbleSize: Incomplete
    zVal: Incomplete
    bubble3D: Incomplete
    marker: Incomplete
    smooth: Incomplete
    explosion: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        idx: int = ...,
        order: int = ...,
        tx: Incomplete | None = ...,
        spPr: Incomplete | None = ...,
        pictureOptions: Incomplete | None = ...,
        dPt=...,
        dLbls: Incomplete | None = ...,
        trendline: Incomplete | None = ...,
        errBars: Incomplete | None = ...,
        cat: Incomplete | None = ...,
        val: Incomplete | None = ...,
        invertIfNegative: Incomplete | None = ...,
        shape: Incomplete | None = ...,
        xVal: Incomplete | None = ...,
        yVal: Incomplete | None = ...,
        bubbleSize: Incomplete | None = ...,
        bubble3D: Incomplete | None = ...,
        marker: Incomplete | None = ...,
        smooth: Incomplete | None = ...,
        explosion: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
    ) -> None: ...
    def to_tree(self, tagname: Incomplete | None = ..., idx: Incomplete | None = ...): ...  # type: ignore[override]

class XYSeries(Series):
    idx: Incomplete
    order: Incomplete
    tx: Incomplete
    spPr: Incomplete
    dPt: Incomplete
    dLbls: Incomplete
    trendline: Incomplete
    errBars: Incomplete
    xVal: Incomplete
    yVal: Incomplete
    invertIfNegative: Incomplete
    bubbleSize: Incomplete
    bubble3D: Incomplete
    marker: Incomplete
    smooth: Incomplete
