from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

class AuthorList(Serialisable):
    tagname: str
    author: Incomplete
    authors: Incomplete
    def __init__(self, author=...) -> None: ...
