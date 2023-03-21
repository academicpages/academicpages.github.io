from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

class WebPublishItem(Serialisable):
    tagname: str
    id: Incomplete
    divId: Incomplete
    sourceType: Incomplete
    sourceRef: Incomplete
    sourceObject: Incomplete
    destinationFile: Incomplete
    title: Incomplete
    autoRepublish: Incomplete
    def __init__(
        self,
        id: Incomplete | None = ...,
        divId: Incomplete | None = ...,
        sourceType: Incomplete | None = ...,
        sourceRef: Incomplete | None = ...,
        sourceObject: Incomplete | None = ...,
        destinationFile: Incomplete | None = ...,
        title: Incomplete | None = ...,
        autoRepublish: Incomplete | None = ...,
    ) -> None: ...

class WebPublishItems(Serialisable):
    tagname: str
    count: Incomplete
    webPublishItem: Incomplete
    __elements__: Incomplete
    def __init__(self, count: Incomplete | None = ..., webPublishItem: Incomplete | None = ...) -> None: ...
