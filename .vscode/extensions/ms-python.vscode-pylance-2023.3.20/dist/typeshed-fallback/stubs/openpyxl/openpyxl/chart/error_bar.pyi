from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

class ErrorBars(Serialisable):
    tagname: str
    errDir: Incomplete
    direction: Incomplete
    errBarType: Incomplete
    style: Incomplete
    errValType: Incomplete
    size: Incomplete
    noEndCap: Incomplete
    plus: Incomplete
    minus: Incomplete
    val: Incomplete
    spPr: Incomplete
    graphicalProperties: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        errDir: Incomplete | None = ...,
        errBarType: str = ...,
        errValType: str = ...,
        noEndCap: Incomplete | None = ...,
        plus: Incomplete | None = ...,
        minus: Incomplete | None = ...,
        val: Incomplete | None = ...,
        spPr: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
    ) -> None: ...
