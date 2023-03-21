from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

class PictureOptions(Serialisable):
    tagname: str
    applyToFront: Incomplete
    applyToSides: Incomplete
    applyToEnd: Incomplete
    pictureFormat: Incomplete
    pictureStackUnit: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        applyToFront: Incomplete | None = ...,
        applyToSides: Incomplete | None = ...,
        applyToEnd: Incomplete | None = ...,
        pictureFormat: Incomplete | None = ...,
        pictureStackUnit: Incomplete | None = ...,
    ) -> None: ...
