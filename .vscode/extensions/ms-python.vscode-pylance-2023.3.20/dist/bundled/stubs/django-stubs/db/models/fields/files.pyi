from typing import (
    Any,
    Callable,
    Iterable,
    Optional,
    Tuple,
    Type,
    TypeVar,
    Union,
    overload,
)

from django.core.files.base import File
from django.core.files.images import ImageFile
from django.core.files.storage import FileSystemStorage, Storage
from django.db.models.base import Model
from django.db.models.fields import (
    _GT,
    Field,
    _ErrorMessagesToOverride,
    _ValidatorCallable,
)

class FieldFile(File):
    instance: Model = ...
    field: FileField = ...
    storage: FileSystemStorage = ...
    def __init__(
        self, instance: Model, field: FileField, name: Optional[str]
    ) -> None: ...
    file: Any = ...
    @property
    def path(self) -> str: ...
    @property
    def url(self) -> str: ...
    @property
    def size(self) -> int: ...
    def save(self, name: str, content: File, save: bool = ...) -> None: ...
    def delete(self, save: bool = ...) -> None: ...
    @property
    def closed(self) -> bool: ...

class FileDescriptor:
    field: FileField = ...
    def __init__(self, field: FileField) -> None: ...
    def __set__(self, instance: Model, value: Optional[Any]) -> None: ...
    def __get__(
        self, instance: Optional[Model], cls: Type[Model] = ...
    ) -> Union[FieldFile, FileDescriptor]: ...

_T = TypeVar("_T", bound="Field[Any, Any]")

class FileField(Field[FileDescriptor, FileDescriptor]):
    storage: Any = ...
    upload_to: Union[str, Callable[[Any, str], str]] = ...
    def __new__(
        cls,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        upload_to: Union[str, Callable[[Any, str], str]] = ...,
        storage: Optional[Union[Storage, Callable[[], Storage]]] = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: bool = ...,
        db_index: bool = ...,
        default: Optional[Union[_GT, Callable[[], _GT]]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[_GT, str], Tuple[str, Iterable[Tuple[_GT, str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> FileField: ...
    # class access
    @overload  # type: ignore
    def __get__(self, instance: None, owner: Any) -> FileDescriptor: ...
    # Model instance access
    @overload
    def __get__(self, instance: Model, owner: Any) -> FieldFile: ...
    # non-Model instances
    @overload
    def __get__(self: _T, instance: Any, owner: Any) -> _T: ...
    def generate_filename(self, instance: Optional[Model], filename: str) -> str: ...

class ImageFileDescriptor(FileDescriptor):
    field: ImageField
    def __set__(self, instance: Model, value: Optional[str]) -> None: ...

class ImageFieldFile(ImageFile, FieldFile):
    field: ImageField
    def delete(self, save: bool = ...) -> None: ...

class ImageField(FileField):
    def __new__(
        cls,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        width_field: str = ...,
        height_field: str = ...,
        upload_to: Union[str, Callable[[Model, str], Any]] = ...,
        storage: Optional[Union[Storage, Callable[[], Storage]]] = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: bool = ...,
        db_index: bool = ...,
        default: Optional[Union[_GT, Callable[[], _GT]]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[_GT, str], Tuple[str, Iterable[Tuple[_GT, str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> ImageField: ...
    # class access
    @overload  # type: ignore
    def __get__(self, instance: None, owner: Any) -> ImageFileDescriptor: ...
    # Model instance access
    @overload
    def __get__(self, instance: Model, owner: Any) -> ImageFieldFile: ...
    # non-Model instances
    @overload
    def __get__(self: _T, instance: Any, owner: Any) -> _T: ...
    def update_dimension_fields(
        self, instance: Model, force: bool = ..., *args: Any, **kwargs: Any
    ) -> None: ...
