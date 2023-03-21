from typing import Any

from django.db import models
from psycopg2.extras import DateRange, DateTimeTZRange, NumericRange

class RangeField(models.Field[Any, Any]):
    empty_strings_allowed: bool = ...
    base_field: Any = ...
    range_type: Any = ...
    def get_prep_value(self, value: Any) -> Any: ...
    def to_python(self, value: Any) -> Any: ...
    def value_to_string(self, obj: Any) -> Any: ...

class IntegerRangeField(RangeField):
    def __get__(self, instance: Any, owner: Any) -> NumericRange: ...  # type: ignore [override]

class BigIntegerRangeField(RangeField):
    def __get__(self, instance: Any, owner: Any) -> NumericRange: ...  # type: ignore [override]

class DecimalRangeField(RangeField):
    def __get__(self, instance: Any, owner: Any) -> NumericRange: ...  # type: ignore [override]

class FloatRangeField(RangeField):
    def __get__(self, instance: Any, owner: Any) -> NumericRange: ...  # type: ignore [override]

class DateTimeRangeField(RangeField):
    def __get__(self, instance: Any, owner: Any) -> DateTimeTZRange: ...  # type: ignore [override]

class DateRangeField(RangeField):
    def __get__(self, instance: Any, owner: Any) -> DateRange: ...  # type: ignore [override]

class RangeOperators:
    EQUAL: str
    NOT_EQUAL: str
    CONTAINS: str
    CONTAINED_BY: str
    OVERLAPS: str
    FULLY_LT: str
    FULLY_GT: str
    NOT_LT: str
    NOT_GT: str
    ADJACENT_TO: str

class RangeBoundary(models.Expression):
    lower: str
    upper: str
    def __init__(
        self, inclusive_lower: bool = ..., inclusive_upper: bool = ...
    ) -> None: ...
