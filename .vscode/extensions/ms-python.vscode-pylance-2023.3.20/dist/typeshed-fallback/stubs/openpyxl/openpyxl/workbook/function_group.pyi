from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

class FunctionGroup(Serialisable):
    tagname: str
    name: Incomplete
    def __init__(self, name: Incomplete | None = ...) -> None: ...

class FunctionGroupList(Serialisable):
    tagname: str
    builtInGroupCount: Incomplete
    functionGroup: Incomplete
    __elements__: Incomplete
    def __init__(self, builtInGroupCount: int = ..., functionGroup=...) -> None: ...
