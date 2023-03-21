from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

class UpDownBars(Serialisable):
    tagname: str
    gapWidth: Incomplete
    upBars: Incomplete
    downBars: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        gapWidth: int = ...,
        upBars: Incomplete | None = ...,
        downBars: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
    ) -> None: ...
