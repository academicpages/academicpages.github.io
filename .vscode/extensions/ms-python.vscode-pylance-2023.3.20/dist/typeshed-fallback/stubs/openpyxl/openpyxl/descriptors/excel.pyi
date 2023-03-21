from _typeshed import Incomplete

from . import Integer, MatchPattern, MinMax, String
from .serialisable import Serialisable

class HexBinary(MatchPattern):
    pattern: str

class UniversalMeasure(MatchPattern):
    pattern: str

class TextPoint(MinMax):
    expected_type: Incomplete
    min: int
    max: int

Coordinate = Integer

class Percentage(MinMax):
    pattern: str
    min: int
    max: int
    def __set__(self, instance, value) -> None: ...

class Extension(Serialisable):
    uri: Incomplete
    def __init__(self, uri: Incomplete | None = ...) -> None: ...

class ExtensionList(Serialisable):
    ext: Incomplete
    def __init__(self, ext=...) -> None: ...

class Relation(String):
    namespace: Incomplete
    allow_none: bool

class Base64Binary(MatchPattern):
    pattern: str

class Guid(MatchPattern):
    pattern: str

class CellRange(MatchPattern):
    pattern: str
    allow_none: bool
    def __set__(self, instance, value) -> None: ...
