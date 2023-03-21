from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

class Drawing(Serialisable):
    tagname: str
    id: Incomplete
    def __init__(self, id: Incomplete | None = ...) -> None: ...
