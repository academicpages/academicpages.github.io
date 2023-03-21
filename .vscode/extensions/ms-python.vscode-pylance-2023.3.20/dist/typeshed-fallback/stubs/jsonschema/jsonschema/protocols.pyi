from collections.abc import Iterator, Mapping, Sequence
from typing import Any, ClassVar, Protocol
from typing_extensions import TypeAlias

from jsonschema._format import FormatChecker
from jsonschema._types import TypeChecker
from jsonschema.exceptions import ValidationError
from jsonschema.validators import RefResolver

_JsonParameter: TypeAlias = str | int | float | bool | None | Mapping[str, _JsonParameter] | Sequence[_JsonParameter]

class Validator(Protocol):
    META_SCHEMA: ClassVar[dict[Any, Any]]
    VALIDATORS: ClassVar[dict[Any, Any]]
    TYPE_CHECKER: ClassVar[TypeChecker]
    FORMAT_CHECKER: ClassVar[FormatChecker]
    schema: dict[Any, Any] | bool
    def __init__(
        self, schema: dict[Any, Any] | bool, resolver: RefResolver | None = ..., format_checker: FormatChecker | None = ...
    ) -> None: ...
    @classmethod
    def check_schema(cls, schema: dict[Any, Any]) -> None: ...
    def is_type(self, instance: _JsonParameter, type: str) -> bool: ...
    def is_valid(self, instance: _JsonParameter) -> bool: ...
    def iter_errors(self, instance: _JsonParameter) -> Iterator[ValidationError]: ...
    def validate(self, instance: _JsonParameter) -> None: ...
    def evolve(self, **kwargs) -> Validator: ...
