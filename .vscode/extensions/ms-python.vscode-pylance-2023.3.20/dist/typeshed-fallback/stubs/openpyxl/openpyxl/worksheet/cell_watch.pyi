from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

class CellWatch(Serialisable):
    tagname: str
    r: Incomplete
    def __init__(self, r: Incomplete | None = ...) -> None: ...

class CellWatches(Serialisable):
    tagname: str
    cellWatch: Incomplete
    __elements__: Incomplete
    def __init__(self, cellWatch=...) -> None: ...
