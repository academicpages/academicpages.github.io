from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

class SheetBackgroundPicture(Serialisable):
    tagname: str
    id: Incomplete
    def __init__(self, id) -> None: ...

class DrawingHF(Serialisable):
    id: Incomplete
    lho: Incomplete
    leftHeaderOddPages: Incomplete
    lhe: Incomplete
    leftHeaderEvenPages: Incomplete
    lhf: Incomplete
    leftHeaderFirstPage: Incomplete
    cho: Incomplete
    centerHeaderOddPages: Incomplete
    che: Incomplete
    centerHeaderEvenPages: Incomplete
    chf: Incomplete
    centerHeaderFirstPage: Incomplete
    rho: Incomplete
    rightHeaderOddPages: Incomplete
    rhe: Incomplete
    rightHeaderEvenPages: Incomplete
    rhf: Incomplete
    rightHeaderFirstPage: Incomplete
    lfo: Incomplete
    leftFooterOddPages: Incomplete
    lfe: Incomplete
    leftFooterEvenPages: Incomplete
    lff: Incomplete
    leftFooterFirstPage: Incomplete
    cfo: Incomplete
    centerFooterOddPages: Incomplete
    cfe: Incomplete
    centerFooterEvenPages: Incomplete
    cff: Incomplete
    centerFooterFirstPage: Incomplete
    rfo: Incomplete
    rightFooterOddPages: Incomplete
    rfe: Incomplete
    rightFooterEvenPages: Incomplete
    rff: Incomplete
    rightFooterFirstPage: Incomplete
    def __init__(
        self,
        id: Incomplete | None = ...,
        lho: Incomplete | None = ...,
        lhe: Incomplete | None = ...,
        lhf: Incomplete | None = ...,
        cho: Incomplete | None = ...,
        che: Incomplete | None = ...,
        chf: Incomplete | None = ...,
        rho: Incomplete | None = ...,
        rhe: Incomplete | None = ...,
        rhf: Incomplete | None = ...,
        lfo: Incomplete | None = ...,
        lfe: Incomplete | None = ...,
        lff: Incomplete | None = ...,
        cfo: Incomplete | None = ...,
        cfe: Incomplete | None = ...,
        cff: Incomplete | None = ...,
        rfo: Incomplete | None = ...,
        rfe: Incomplete | None = ...,
        rff: Incomplete | None = ...,
    ) -> None: ...
