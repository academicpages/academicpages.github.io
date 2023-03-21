from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

class ExternalReference(Serialisable):
    tagname: str
    id: Incomplete
    def __init__(self, id) -> None: ...
