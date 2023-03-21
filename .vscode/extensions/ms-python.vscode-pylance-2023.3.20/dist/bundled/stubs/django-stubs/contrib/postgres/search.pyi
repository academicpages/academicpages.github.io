from typing import Any, Dict, Iterable, Optional, TypeVar, Union

from django.db.models import Field
from django.db.models.expressions import (
    Combinable,
    CombinedExpression,
    Func,
    Value,
    _OutputField,
)
from django.db.models.fields import (
    _ErrorMessagesToOverride,
    _FieldChoices,
    _ValidatorCallable,
)
from django.db.models.lookups import Lookup

_Expression = Union[str, Combinable, "SearchQueryCombinable"]

class SearchVectorExact(Lookup[Any]): ...

class SearchVectorField(Field[Any, Any]):
    def __init__(
        self,
        verbose_name: Optional[Union[str, bytes]] = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: bool = ...,
        db_index: bool = ...,
        default: Any = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Optional[_FieldChoices] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> None: ...

class SearchQueryField(Field[Any, Any]):
    def __init__(
        self,
        verbose_name: Optional[Union[str, bytes]] = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: bool = ...,
        db_index: bool = ...,
        default: Any = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Optional[_FieldChoices] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> None: ...

class SearchVectorCombinable:
    ADD: str = ...

class SearchVector(SearchVectorCombinable, Func):
    config: Optional[Any] = ...
    def __init__(self, *expressions: _Expression, **extra: Any) -> None: ...

class CombinedSearchVector(SearchVectorCombinable, CombinedExpression):
    def __init__(
        self,
        lhs: Any,
        connector: Any,
        rhs: Any,
        config: Optional[_Expression] = ...,
        output_field: Optional[_OutputField] = ...,
    ) -> None: ...

_T = TypeVar("_T", bound="SearchQueryCombinable")

class SearchQueryCombinable:
    BITAND: str = ...
    BITOR: str = ...
    def __or__(self: _T, other: SearchQueryCombinable) -> _T: ...
    def __ror__(self: _T, other: SearchQueryCombinable) -> _T: ...
    def __and__(self: _T, other: SearchQueryCombinable) -> _T: ...
    def __rand__(self: _T, other: SearchQueryCombinable) -> _T: ...

class SearchQuery(SearchQueryCombinable, Value):  # type: ignore
    SEARCH_TYPES: Dict[str, str] = ...
    def __init__(
        self,
        value: str,
        output_field: Optional[_OutputField] = ...,
        *,
        config: Optional[_Expression] = ...,
        invert: bool = ...,
        search_type: str = ...
    ) -> None: ...
    def __invert__(self: _T) -> _T: ...

class CombinedSearchQuery(SearchQueryCombinable, CombinedExpression):  # type: ignore
    def __init__(
        self,
        lhs: Any,
        connector: Any,
        rhs: Any,
        config: Optional[_Expression] = ...,
        output_field: Optional[_OutputField] = ...,
    ) -> None: ...

class SearchRank(Func):
    def __init__(
        self,
        vector: Union[SearchVector, _Expression],
        query: Union[SearchQuery, _Expression],
        **extra: Any
    ) -> None: ...

class TrigramBase(Func):
    def __init__(self, expression: _Expression, string: str, **extra: Any) -> None: ...

class TrigramSimilarity(TrigramBase): ...
class TrigramDistance(TrigramBase): ...
