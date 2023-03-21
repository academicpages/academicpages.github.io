from typing import (
    Any,
    Callable,
    Collection,
    Iterable,
    Optional,
    Sequence,
    Set,
    Type,
    Union,
)

from django.db import IntegrityError
from django.db.models.base import Model
from django.db.models.fields import Field
from django.db.models.options import Options

def CASCADE(
    collector: "Collector",
    field: Field[Any, Any],
    sub_objs: Sequence[Model],
    using: str,
) -> None: ...
def SET_NULL(
    collector: "Collector",
    field: Field[Any, Any],
    sub_objs: Sequence[Model],
    using: str,
) -> None: ...
def SET_DEFAULT(
    collector: "Collector",
    field: Field[Any, Any],
    sub_objs: Sequence[Model],
    using: str,
) -> None: ...
def DO_NOTHING(
    collector: "Collector",
    field: Field[Any, Any],
    sub_objs: Sequence[Model],
    using: str,
) -> None: ...
def PROTECT(
    collector: "Collector",
    field: Field[Any, Any],
    sub_objs: Sequence[Model],
    using: str,
) -> None: ...
def RESTRICT(
    collector: "Collector",
    field: Field[Any, Any],
    sub_objs: Sequence[Model],
    using: str,
) -> None: ...
def SET(
    value: Union[Any, Callable[[], Any]]
) -> Callable[["Collector", Field[Any, Any], Sequence[Model], str], None]: ...
def get_candidate_relations_to_delete(
    opts: Options[Any],
) -> Iterable[Field[Any, Any]]: ...

class ProtectedError(IntegrityError):
    protected_objects: Set[Model]
    def __init__(self, msg: str, protected_objects: Set[Model]) -> None: ...

class RestrictedError(IntegrityError):
    restricted_objects: Set[Model]
    def __init__(self, msg: str, restricted_objects: Set[Model]) -> None: ...

class Collector:
    def __init__(self, using: str) -> None: ...
    def collect(
        self,
        objs: Collection[Optional[Model]],
        source: Optional[Type[Model]] = ...,
        source_attr: Optional[str] = ...,
        **kwargs: Any
    ) -> None: ...
    def can_fast_delete(
        self,
        objs: Union[Model, Iterable[Model]],
        from_field: Optional[Field[Any, Any]] = ...,
    ) -> bool: ...
