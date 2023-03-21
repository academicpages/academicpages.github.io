from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

class Protection(Serialisable):
    tagname: str
    locked: Incomplete
    hidden: Incomplete
    def __init__(self, locked: bool = ..., hidden: bool = ...) -> None: ...
