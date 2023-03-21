from _typeshed import Incomplete

from openpyxl.descriptors import Typed
from openpyxl.descriptors.nested import NestedMinMax

class NestedGapAmount(NestedMinMax):
    allow_none: bool
    min: int
    max: int

class NestedOverlap(NestedMinMax):
    allow_none: bool
    min: int
    max: int

class NumberFormatDescriptor(Typed):
    expected_type: Incomplete
    allow_none: bool
    def __set__(self, instance, value) -> None: ...
