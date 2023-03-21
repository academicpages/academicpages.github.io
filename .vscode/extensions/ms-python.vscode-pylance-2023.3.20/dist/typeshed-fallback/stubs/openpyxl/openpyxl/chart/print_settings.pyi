from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

class PageMargins(Serialisable):
    tagname: str
    l: Incomplete
    left: Incomplete
    r: Incomplete
    right: Incomplete
    t: Incomplete
    top: Incomplete
    b: Incomplete
    bottom: Incomplete
    header: Incomplete
    footer: Incomplete
    def __init__(
        self, l: float = ..., r: float = ..., t: int = ..., b: int = ..., header: float = ..., footer: float = ...
    ) -> None: ...

class PrintSettings(Serialisable):
    tagname: str
    headerFooter: Incomplete
    pageMargins: Incomplete
    pageSetup: Incomplete
    __elements__: Incomplete
    def __init__(
        self, headerFooter: Incomplete | None = ..., pageMargins: Incomplete | None = ..., pageSetup: Incomplete | None = ...
    ) -> None: ...
