from typing import Any, Callable, Optional, Sequence, Type, TypeVar, Union

from django.contrib.admin import ModelAdmin
from django.db.models import Combinable, QuerySet
from django.db.models.base import Model
from django.db.models.expressions import BaseExpression
from django.http import HttpRequest, HttpResponse

_M = TypeVar("_M", bound=Model)

def action(
    function: Optional[
        Callable[[ModelAdmin[_M], HttpRequest, QuerySet[_M]], Optional[HttpResponse]]
    ] = ...,
    *,
    permissions: Optional[Sequence[str]] = ...,
    description: Optional[str] = ...,
) -> Callable[..., Any]: ...
def display(
    function: Optional[Callable[[_M], Any]] = ...,
    *,
    boolean: Optional[bool] = ...,
    ordering: Optional[Union[str, Combinable, BaseExpression]] = ...,
    description: Optional[str] = ...,
    empty_value: Optional[str] = ...,
) -> Callable[..., Any]: ...
def register(*models: Type[Model], site: Optional[Any] = ...) -> Callable[..., Any]: ...
