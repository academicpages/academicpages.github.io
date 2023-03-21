from typing import (
    Any,
    Dict,
    Generic,
    Iterable,
    List,
    MutableMapping,
    Optional,
    Tuple,
    Type,
    TypeVar,
    Union,
)

from django.db.models.base import Model
from django.db.models.query import QuerySet

_T = TypeVar("_T", bound=Model)
_V = TypeVar("_V", bound=Model)
_M = TypeVar("_M", bound="BaseManager[Any]")

class BaseManager(QuerySet[_T]):
    creation_counter: int = ...
    auto_created: bool = ...
    use_in_migrations: bool = ...
    name: str = ...
    model: Type[_T] = ...
    db: str
    _db: Optional[str]
    def __init__(self) -> None: ...
    def deconstruct(
        self,
    ) -> Tuple[bool, str, None, Tuple[Any, ...], Dict[str, int]]: ...
    def check(self, **kwargs: Any) -> List[Any]: ...
    @classmethod
    def from_queryset(
        cls, queryset_class: Type[QuerySet[Any]], class_name: Optional[str] = ...
    ) -> Any: ...
    @classmethod
    def _get_queryset_methods(cls, queryset_class: type) -> Dict[str, Any]: ...
    def contribute_to_class(self, model: Type[Model], name: str) -> None: ...
    def db_manager(
        self: _M, using: Optional[str] = ..., hints: Optional[Dict[str, Model]] = ...
    ) -> _M: ...
    def get_queryset(self) -> QuerySet[_T]: ...

class Manager(BaseManager[_T]): ...

class RelatedManager(Manager[_T]):
    related_val: Tuple[int, ...]
    def add(self, *objs: Union[QuerySet[_T], _T], bulk: bool = ...) -> None: ...
    def remove(self, *objs: Union[QuerySet[_T], _T], bulk: bool = ...) -> None: ...
    def set(
        self,
        objs: Union[QuerySet[_T], Iterable[_T]],
        *,
        bulk: bool = ...,
        clear: bool = ...,
    ) -> None: ...
    def clear(self) -> None: ...

class ManyToManyRelatedManager(Generic[_T, _V], Manager[_T]):
    through: Type[_V]
    def add(
        self,
        *objs: Union[QuerySet[_T], _T, _V],
        through_defaults: MutableMapping[str, Any] = ...,
    ) -> None: ...
    def remove(self, *objs: Union[QuerySet[_T], _T, _V]) -> None: ...
    def set(
        self,
        objs: Union[QuerySet[_T], Iterable[_T]],
        *,
        clear: bool = ...,
        through_defaults: MutableMapping[str, Any] = ...,
    ) -> None: ...
    def clear(self) -> None: ...
    def create(
        self,
        defaults: Optional[MutableMapping[str, Any]] = ...,
        through_defaults: Optional[MutableMapping[str, Any]] = ...,
        **kwargs: Any,
    ) -> _T: ...
    def get_or_create(
        self,
        defaults: Optional[MutableMapping[str, Any]] = ...,
        *,
        through_defaults: MutableMapping[str, Any] = ...,
        **kwargs: Any,
    ) -> Tuple[_T, bool]: ...
    def update_or_create(
        self,
        defaults: Optional[MutableMapping[str, Any]] = ...,
        *,
        through_defaults: MutableMapping[str, Any] = ...,
        **kwargs: Any,
    ) -> Tuple[_T, bool]: ...

class ManagerDescriptor:
    manager: Manager[Any] = ...
    def __init__(self, manager: Manager[Any]) -> None: ...
    def __get__(
        self, instance: Optional[Model], cls: Type[Model] = ...
    ) -> Manager[Any]: ...

class EmptyManager(Manager[Any]):
    def __init__(self, model: Type[Model]) -> None: ...
