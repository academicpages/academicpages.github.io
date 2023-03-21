from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

class WebPublishObject(Serialisable):
    tagname: str
    id: Incomplete
    divId: Incomplete
    sourceObject: Incomplete
    destinationFile: Incomplete
    title: Incomplete
    autoRepublish: Incomplete
    def __init__(
        self,
        id: Incomplete | None = ...,
        divId: Incomplete | None = ...,
        sourceObject: Incomplete | None = ...,
        destinationFile: Incomplete | None = ...,
        title: Incomplete | None = ...,
        autoRepublish: Incomplete | None = ...,
    ) -> None: ...

class WebPublishObjectList(Serialisable):
    tagname: str
    # Overwritten by property below
    # count: Integer
    webPublishObject: Incomplete
    __elements__: Incomplete
    def __init__(self, count: Incomplete | None = ..., webPublishObject=...) -> None: ...
    @property
    def count(self): ...

class WebPublishing(Serialisable):
    tagname: str
    css: Incomplete
    thicket: Incomplete
    longFileNames: Incomplete
    vml: Incomplete
    allowPng: Incomplete
    targetScreenSize: Incomplete
    dpi: Incomplete
    codePage: Incomplete
    characterSet: Incomplete
    def __init__(
        self,
        css: Incomplete | None = ...,
        thicket: Incomplete | None = ...,
        longFileNames: Incomplete | None = ...,
        vml: Incomplete | None = ...,
        allowPng: Incomplete | None = ...,
        targetScreenSize: str = ...,
        dpi: Incomplete | None = ...,
        codePage: Incomplete | None = ...,
        characterSet: Incomplete | None = ...,
    ) -> None: ...
