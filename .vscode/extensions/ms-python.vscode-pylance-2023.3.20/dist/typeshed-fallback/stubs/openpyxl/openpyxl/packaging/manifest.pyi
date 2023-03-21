from _typeshed import Incomplete
from collections.abc import Generator

from openpyxl.descriptors.serialisable import Serialisable

mimetypes: Incomplete

class FileExtension(Serialisable):
    tagname: str
    Extension: Incomplete
    ContentType: Incomplete
    def __init__(self, Extension, ContentType) -> None: ...

class Override(Serialisable):
    tagname: str
    PartName: Incomplete
    ContentType: Incomplete
    def __init__(self, PartName, ContentType) -> None: ...

DEFAULT_TYPES: Incomplete
DEFAULT_OVERRIDE: Incomplete

class Manifest(Serialisable):
    tagname: str
    Default: Incomplete
    Override: Incomplete
    path: str
    __elements__: Incomplete
    def __init__(self, Default=..., Override=...) -> None: ...
    @property
    def filenames(self): ...
    @property
    def extensions(self): ...
    def to_tree(self): ...
    def __contains__(self, content_type): ...
    def find(self, content_type): ...
    def findall(self, content_type) -> Generator[Incomplete, None, None]: ...
    def append(self, obj) -> None: ...
