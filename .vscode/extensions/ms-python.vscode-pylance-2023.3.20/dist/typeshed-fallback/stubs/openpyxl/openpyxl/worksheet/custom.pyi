from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

class CustomProperty(Serialisable):
    tagname: str
    name: Incomplete
    def __init__(self, name: Incomplete | None = ...) -> None: ...

class CustomProperties(Serialisable):
    tagname: str
    customPr: Incomplete
    __elements__: Incomplete
    def __init__(self, customPr=...) -> None: ...
