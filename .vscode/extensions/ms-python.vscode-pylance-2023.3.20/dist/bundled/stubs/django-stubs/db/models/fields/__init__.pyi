import decimal
import ipaddress
import uuid
from datetime import date, datetime, time, timedelta
from typing import (
    Any,
    Callable,
    Dict,
    Generic,
    Iterable,
    List,
    Optional,
    Sequence,
    Tuple,
    Type,
    TypeVar,
    Union,
    overload,
)

from django.core.checks import CheckMessage
from django.core.exceptions import FieldDoesNotExist as FieldDoesNotExist
from django.db.models import Model
from django.db.models.expressions import Col, Combinable
from django.db.models.query_utils import RegisterLookupMixin
from django.forms import Field as FormField
from django.forms import Widget
from typing_extensions import Literal

BLANK_CHOICE_DASH: List[Tuple[str, str]] = ...

_Choice = Tuple[Any, str]
_ChoiceNamedGroup = Tuple[str, Iterable[_Choice]]
_FieldChoices = Iterable[Union[_Choice, _ChoiceNamedGroup]]

_ValidatorCallable = Callable[..., None]
_ErrorMessagesToOverride = Dict[str, Any]

_T = TypeVar("_T", bound="Field[Any, Any]")
# __set__ value type
_ST = TypeVar("_ST")
# __get__ return type
_GT = TypeVar("_GT")

class NOT_PROVIDED: ...

class Field(RegisterLookupMixin, Generic[_ST, _GT]):

    widget: Widget
    help_text: str
    db_table: str
    attname: str
    auto_created: bool
    primary_key: bool
    remote_field: Field[_ST, _GT]
    is_relation: bool
    related_model: Optional[Any] = ...
    one_to_many: Optional[bool] = ...
    one_to_one: Optional[bool] = ...
    many_to_many: Optional[bool] = ...
    many_to_one: Optional[bool] = ...
    max_length: int
    model: Type[Model]
    name: str
    verbose_name: str
    description: str
    blank: bool = ...
    null: bool = ...
    editable: bool = ...
    empty_strings_allowed: bool = ...
    choices: _FieldChoices = ...
    db_column: Optional[str]
    column: str
    default: Any
    error_messages: _ErrorMessagesToOverride
    def __set__(self, instance: Any, value: _ST) -> None: ...
    # class access
    @overload
    def __get__(self: _T, instance: None, owner: Any) -> _T: ...
    # Model instance access
    @overload
    def __get__(self, instance: Model, owner: Any) -> _GT: ...
    # non-Model instances
    @overload
    def __get__(self: _T, instance: Any, owner: Any) -> _T: ...
    def deconstruct(self) -> Any: ...
    def set_attributes_from_name(self, name: str) -> None: ...
    def db_type(self, connection: Any) -> str: ...
    def db_parameters(self, connection: Any) -> Dict[str, str]: ...
    def pre_save(self, model_instance: Model, add: bool) -> Any: ...
    def get_prep_value(self, value: Any) -> Any: ...
    def get_db_prep_value(self, value: Any, connection: Any, prepared: bool) -> Any: ...
    def get_db_prep_save(self, value: Any, connection: Any) -> Any: ...
    def get_internal_type(self) -> str: ...
    # TODO: plugin support
    def formfield(self, **kwargs: Any) -> Any: ...
    def save_form_data(self, instance: Model, data: Any) -> None: ...
    def contribute_to_class(
        self, cls: Type[Model], name: str, private_only: bool = ...
    ) -> None: ...
    def to_python(self, value: Any) -> Any: ...
    def clean(self, value: Any, model_instance: Optional[Model]) -> Any: ...
    def get_choices(
        self,
        include_blank: bool = ...,
        blank_choice: _Choice = ...,
        limit_choices_to: Optional[Any] = ...,
        ordering: Sequence[str] = ...,
    ) -> Sequence[Union[_Choice, _ChoiceNamedGroup]]: ...
    def has_default(self) -> bool: ...
    def get_default(self) -> Any: ...
    def check(self, **kwargs: Any) -> List[CheckMessage]: ...
    @property
    def validators(self) -> List[_ValidatorCallable]: ...
    def validate(self, value: Any, model_instance: Model) -> None: ...
    def run_validators(self, value: Any) -> None: ...
    def get_col(
        self, alias: str, output_field: Optional[Field[Any, Any]] = ...
    ) -> Col: ...
    @property
    def cached_col(self) -> Col: ...
    def value_from_object(self, obj: Model) -> _GT: ...
    def get_attname(self) -> str: ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

_I = TypeVar("_I", bound=Optional[int])

class IntegerField(Generic[_I], Field[Union[_I, Combinable], _I]):
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = ...,
        db_index: bool = ...,
        default: Optional[Union[_I, Callable[[], _I]]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[_I, str], Tuple[str, Iterable[Tuple[_I, str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> IntegerField[int]: ...
    @overload
    def __new__(
        cls,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True] = ...,
        db_index: bool = ...,
        default: Union[_I, Callable[[], _I]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[_I, str], Tuple[str, Iterable[Tuple[_I, str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> IntegerField[Optional[int]]: ...

class PositiveIntegerRelDbTypeMixin:
    def rel_db_type(self, connection: Any) -> Any: ...

class PositiveIntegerField(PositiveIntegerRelDbTypeMixin, IntegerField[_I]):
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = ...,
        db_index: bool = ...,
        default: Optional[Union[_I, Callable[[], _I]]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[_I, str], Tuple[str, Iterable[Tuple[_I, str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> PositiveIntegerField[int]: ...
    @overload
    def __new__(
        cls,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True] = ...,
        db_index: bool = ...,
        default: Union[_I, Callable[[], _I]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[_I, str], Tuple[str, Iterable[Tuple[_I, str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> PositiveIntegerField[Optional[int]]: ...

class PositiveSmallIntegerField(PositiveIntegerRelDbTypeMixin, IntegerField[_I]):
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = ...,
        db_index: bool = ...,
        default: Optional[Union[_I, Callable[[], _I]]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[_I, str], Tuple[str, Iterable[Tuple[_I, str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> PositiveSmallIntegerField[int]: ...
    @overload
    def __new__(
        cls,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True] = ...,
        db_index: bool = ...,
        default: Union[_I, Callable[[], _I]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[_I, str], Tuple[str, Iterable[Tuple[_I, str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> PositiveSmallIntegerField[Optional[int]]: ...

class SmallIntegerField(IntegerField[_I]):
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = ...,
        db_index: bool = ...,
        default: Optional[Union[_I, Callable[[], _I]]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[_I, str], Tuple[str, Iterable[Tuple[_I, str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> SmallIntegerField[int]: ...
    @overload
    def __new__(
        cls,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True] = ...,
        db_index: bool = ...,
        default: Union[_I, Callable[[], _I]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[_I, str], Tuple[str, Iterable[Tuple[_I, str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> SmallIntegerField[Optional[int]]: ...

class BigIntegerField(IntegerField[_I]):
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = ...,
        db_index: bool = ...,
        default: Optional[Union[_I, Callable[[], _I]]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[_I, str], Tuple[str, Iterable[Tuple[_I, str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> BigIntegerField[int]: ...
    @overload
    def __new__(
        cls,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True] = ...,
        db_index: bool = ...,
        default: Union[_I, Callable[[], _I]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[_I, str], Tuple[str, Iterable[Tuple[_I, str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> BigIntegerField[Optional[int]]: ...

class PositiveBigIntegerField(IntegerField[_I]):
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = ...,
        db_index: bool = ...,
        default: Optional[Union[_I, Callable[[], _I]]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[_I, str], Tuple[str, Iterable[Tuple[_I, str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> PositiveBigIntegerField[int]: ...
    @overload
    def __new__(
        cls,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True] = ...,
        db_index: bool = ...,
        default: Union[_I, Callable[[], _I]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[_I, str], Tuple[str, Iterable[Tuple[_I, str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> PositiveBigIntegerField[Optional[int]]: ...

_F = TypeVar("_F", bound=Optional[float])

class FloatField(Generic[_F], Field[Union[_F, Combinable], _F]):
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = ...,
        db_index: bool = ...,
        default: Optional[Union[_F, Callable[[], _F]]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[_F, str], Tuple[str, Iterable[Tuple[_F, str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> FloatField[float]: ...
    @overload
    def __new__(
        cls,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True] = ...,
        db_index: bool = ...,
        default: Union[_F, Callable[[], _F]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[_F, str], Tuple[str, Iterable[Tuple[_F, str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> FloatField[Optional[float]]: ...

_DEC = TypeVar("_DEC", bound=Optional[decimal.Decimal])

class DecimalField(Generic[_DEC], Field[Union[_DEC, Combinable], _DEC]):
    # attributes
    max_digits: int = ...
    decimal_places: int = ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        max_digits: int = ...,
        decimal_places: int = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = ...,
        db_index: bool = ...,
        default: Optional[Union[_DEC, Callable[[], _DEC]]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[_DEC, str], Tuple[str, Iterable[Tuple[_DEC, str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> DecimalField[decimal.Decimal]: ...
    @overload
    def __new__(
        cls,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        max_digits: int = ...,
        decimal_places: int = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True] = ...,
        db_index: bool = ...,
        default: Union[_DEC, Callable[[], _DEC]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[_DEC, str], Tuple[str, Iterable[Tuple[_DEC, str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> DecimalField[Optional[decimal.Decimal]]: ...

class AutoFieldMeta(type): ...
class AutoFieldMixin: ...

class AutoField(AutoFieldMixin, IntegerField[int], metaclass=AutoFieldMeta):
    def __new__(
        cls,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        max_digits: int = ...,
        decimal_places: int = ...,
        primary_key: Literal[True] = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: Literal[True] = ...,
        null: bool = ...,
        db_index: bool = ...,
        default: Optional[Union[int, Callable[[], int]]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[int, str], Tuple[str, Iterable[Tuple[int, str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> AutoField: ...

class BigAutoField(AutoFieldMixin, BigIntegerField[int]):
    def __new__(
        cls,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        max_digits: int = ...,
        decimal_places: int = ...,
        primary_key: Literal[True] = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: Literal[True] = ...,
        null: bool = ...,
        db_index: bool = ...,
        default: Optional[Union[int, Callable[[], int]]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[int, str], Tuple[str, Iterable[Tuple[int, str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> BigAutoField: ...

class SmallAutoField(AutoFieldMixin, SmallIntegerField[int]):
    def __new__(
        cls,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        max_digits: int = ...,
        decimal_places: int = ...,
        primary_key: Literal[True] = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: Literal[True] = ...,
        null: bool = ...,
        db_index: bool = ...,
        default: Optional[Union[int, Callable[[], int]]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[int, str], Tuple[str, Iterable[Tuple[int, str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> SmallAutoField: ...

_C = TypeVar("_C", bound=Optional[str])

class CharField(Generic[_C], Field[Union[_C, Combinable], _C]):
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        max_length: int = ...,
        db_collation: Optional[str] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = ...,
        db_index: bool = ...,
        default: Optional[Union[_C, Callable[[], _C]]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[_C, str], Tuple[str, Iterable[Tuple[_C, str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> CharField[str]: ...
    @overload
    def __new__(
        cls,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        max_length: int = ...,
        db_collation: Optional[str] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True] = ...,
        db_index: bool = ...,
        default: Union[_C, Callable[[], _C]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[_C, str], Tuple[str, Iterable[Tuple[_C, str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> CharField[Optional[str]]: ...

class SlugField(CharField[_C]):
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        max_length: int = ...,
        db_collation: Optional[str] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = ...,
        db_index: bool = ...,
        default: Optional[Union[_C, Callable[[], _C]]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[_C, str], Tuple[str, Iterable[Tuple[_C, str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> SlugField[str]: ...
    @overload
    def __new__(
        cls,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        max_length: int = ...,
        db_collation: Optional[str] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True] = ...,
        db_index: bool = ...,
        default: Union[_C, Callable[[], _C]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[_C, str], Tuple[str, Iterable[Tuple[_C, str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> SlugField[Optional[str]]: ...

class EmailField(CharField[_C]):
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        max_length: int = ...,
        db_collation: Optional[str] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = ...,
        db_index: bool = ...,
        default: Optional[Union[_C, Callable[[], _C]]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[_C, str], Tuple[str, Iterable[Tuple[_C, str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> EmailField[str]: ...
    @overload
    def __new__(
        cls,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        max_length: int = ...,
        db_collation: Optional[str] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True] = ...,
        db_index: bool = ...,
        default: Union[_C, Callable[[], _C]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[_C, str], Tuple[str, Iterable[Tuple[_C, str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> EmailField[Optional[str]]: ...

class URLField(CharField[_C]):
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        max_length: int = ...,
        db_collation: Optional[str] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = ...,
        db_index: bool = ...,
        default: Optional[Union[_C, Callable[[], _C]]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[_C, str], Tuple[str, Iterable[Tuple[_C, str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> URLField[str]: ...
    @overload
    def __new__(
        cls,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        max_length: int = ...,
        db_collation: Optional[str] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True] = ...,
        db_index: bool = ...,
        default: Union[_C, Callable[[], _C]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[_C, str], Tuple[str, Iterable[Tuple[_C, str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> URLField[Optional[str]]: ...

class TextField(Generic[_C], Field[Union[_C, Combinable], _C]):
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        db_collation: Optional[str] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = ...,
        db_index: bool = ...,
        default: Optional[Union[_C, Callable[[], _C]]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[_C, str], Tuple[str, Iterable[Tuple[_C, str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> TextField[str]: ...
    @overload
    def __new__(
        cls,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        db_collation: Optional[str] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True] = ...,
        db_index: bool = ...,
        default: Union[_C, Callable[[], _C]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[_C, str], Tuple[str, Iterable[Tuple[_C, str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> TextField[Optional[str]]: ...

_B = TypeVar("_B", bound=Optional[bool])

class BooleanField(Generic[_B], Field[Union[_B, Combinable], _B]):
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        db_collation: Optional[str] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = ...,
        db_index: bool = ...,
        default: Optional[Union[_B, Callable[[], _B]]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[_B, str], Tuple[str, Iterable[Tuple[_B, str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> BooleanField[bool]: ...
    @overload
    def __new__(
        cls,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        db_collation: Optional[str] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True] = ...,
        db_index: bool = ...,
        default: Union[_B, Callable[[], _B]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[_B, str], Tuple[str, Iterable[Tuple[_B, str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> BooleanField[Optional[bool]]: ...

class IPAddressField(Generic[_C], Field[Union[_C, Combinable], _C]):
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = ...,
        db_index: bool = ...,
        default: Optional[Union[_C, Callable[[], _C]]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[_C, str], Tuple[str, Iterable[Tuple[_C, str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> IPAddressField[str]: ...
    @overload
    def __new__(
        cls,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True] = ...,
        db_index: bool = ...,
        default: Union[_C, Callable[[], _C]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[_C, str], Tuple[str, Iterable[Tuple[_C, str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> IPAddressField[Optional[str]]: ...

class GenericIPAddressField(
    Generic[_C],
    Field[Union[_C, ipaddress.IPv4Address, ipaddress.IPv6Address, Combinable], _C],
):
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        protocol: str = ...,
        unpack_ipv4: str = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = ...,
        db_index: bool = ...,
        default: Optional[Union[_C, Callable[[], _C]]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[_C, str], Tuple[str, Iterable[Tuple[_C, str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> GenericIPAddressField[str]: ...
    @overload
    def __new__(
        cls,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        protocol: str = ...,
        unpack_ipv4: str = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True] = ...,
        db_index: bool = ...,
        default: Union[_C, Callable[[], _C]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[_C, str], Tuple[str, Iterable[Tuple[_C, str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> GenericIPAddressField[Optional[str]]: ...

_DD = TypeVar("_DD", bound=Optional[date])

class DateTimeCheckMixin: ...

class DateField(DateTimeCheckMixin, Field[Union[_DD, Combinable], _DD]):
    # attributes
    auto_now: bool = ...
    auto_now_add: bool = ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        auto_now: bool = ...,
        auto_now_add: bool = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = ...,
        db_index: bool = ...,
        default: Optional[Union[_DD, Callable[[], _DD]]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[_DD, str], Tuple[str, Iterable[Tuple[_DD, str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> DateField[date]: ...
    @overload
    def __new__(
        cls,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        auto_now: bool = ...,
        auto_now_add: bool = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True] = ...,
        db_index: bool = ...,
        default: Union[_DD, Callable[[], _DD]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[_DD, str], Tuple[str, Iterable[Tuple[_DD, str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> DateField[Optional[date]]: ...

_TM = TypeVar("_TM", bound=Optional[time])

class TimeField(Generic[_TM], DateTimeCheckMixin, Field[Union[_TM, Combinable], _TM]):
    # attributes
    auto_now: bool = ...
    auto_now_add: bool = ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        auto_now: bool = ...,
        auto_now_add: bool = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = ...,
        db_index: bool = ...,
        default: Optional[Union[_TM, Callable[[], _TM]]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[_TM, str], Tuple[str, Iterable[Tuple[_TM, str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> TimeField[time]: ...
    @overload
    def __new__(
        cls,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        auto_now: bool = ...,
        auto_now_add: bool = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True] = ...,
        db_index: bool = ...,
        default: Union[_TM, Callable[[], _TM]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[_TM, str], Tuple[str, Iterable[Tuple[_TM, str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> TimeField[Optional[time]]: ...

_DT = TypeVar("_DT", bound=Optional[datetime])

class DateTimeField(DateField[_DT]):
    # attributes
    auto_now: bool = ...
    auto_now_add: bool = ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        auto_now: bool = ...,
        auto_now_add: bool = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = ...,
        db_index: bool = ...,
        default: Optional[Union[_DT, Callable[[], _DT]]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[_DT, str], Tuple[str, Iterable[Tuple[_DT, str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> DateTimeField[datetime]: ...
    @overload
    def __new__(
        cls,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        auto_now: bool = ...,
        auto_now_add: bool = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True] = ...,
        db_index: bool = ...,
        default: Union[_DT, Callable[[], _DT]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[_DT, str], Tuple[str, Iterable[Tuple[_DT, str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> DateTimeField[Optional[datetime]]: ...

_U = TypeVar("_U", bound=Optional[uuid.UUID])

class UUIDField(Generic[_U], Field[Union[str, _U], _U]):
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = ...,
        db_index: bool = ...,
        default: Optional[Union[_U, Callable[[], _U]]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[_U, str], Tuple[str, Iterable[Tuple[_U, str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> UUIDField[uuid.UUID]: ...
    @overload
    def __new__(
        cls,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True] = ...,
        db_index: bool = ...,
        default: Union[_U, Callable[[], _U]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[_U, str], Tuple[str, Iterable[Tuple[_U, str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> UUIDField[Optional[uuid.UUID]]: ...

class FilePathField(Generic[_C], Field[_C, _C]):
    path: Union[str, Callable[..., str]] = ...
    match: Optional[str] = ...
    recursive: bool = ...
    allow_files: bool = ...
    allow_folders: bool = ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        path: Union[str, Callable[..., str]] = ...,
        match: Optional[str] = ...,
        recursive: bool = ...,
        allow_filters: bool = ...,
        allow_folders: bool = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = ...,
        db_index: bool = ...,
        default: Optional[Union[_C, Callable[[], _C]]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[_C, str], Tuple[str, Iterable[Tuple[_C, str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> FilePathField[str]: ...
    @overload
    def __new__(
        cls,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        path: Union[str, Callable[..., str]] = ...,
        match: Optional[str] = ...,
        recursive: bool = ...,
        allow_filters: bool = ...,
        allow_folders: bool = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True] = ...,
        db_index: bool = ...,
        default: Union[_C, Callable[[], _C]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[_C, str], Tuple[str, Iterable[Tuple[_C, str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> FilePathField[Optional[str]]: ...

_BIN = TypeVar("_BIN", bound=Optional[bytes])

class BinaryField(Generic[_BIN], Field[Union[_BIN, bytearray, memoryview], _BIN]):
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = ...,
        db_index: bool = ...,
        default: Optional[Union[_BIN, Callable[[], _BIN]]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[_BIN, str], Tuple[str, Iterable[Tuple[_BIN, str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> BinaryField[bytes]: ...
    @overload
    def __new__(
        cls,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True] = ...,
        db_index: bool = ...,
        default: Union[_BIN, Callable[[], _BIN]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[_BIN, str], Tuple[str, Iterable[Tuple[_BIN, str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> BinaryField[Optional[bytes]]: ...

_TD = TypeVar("_TD", bound=Optional[timedelta])

class DurationField(Generic[_TD], Field[_TD, _TD]):
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = ...,
        db_index: bool = ...,
        default: Optional[Union[_TD, Callable[[], _TD]]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[_TD, str], Tuple[str, Iterable[Tuple[_TD, str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> DurationField[timedelta]: ...
    @overload
    def __new__(
        cls,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True] = ...,
        db_index: bool = ...,
        default: Union[_TD, Callable[[], _TD]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[_TD, str], Tuple[str, Iterable[Tuple[_TD, str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> DurationField[Optional[timedelta]]: ...
