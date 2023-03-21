from typing import (
    Any,
    Callable,
    Coroutine,
    Dict,
    List,
    Optional,
    Tuple,
    Union,
    overload,
)

from ..conf.urls import IncludedURLConf
from ..http.response import HttpResponseBase
from .resolvers import URLPattern, URLResolver

_ResponseType = Union[
    HttpResponseBase, Coroutine[Any, Any, HttpResponseBase], Coroutine[Any, Any, None]
]

def include(
    arg: Any, namespace: Optional[str] = ...
) -> Tuple[List[URLResolver], Optional[str], Optional[str]]: ...

# path()
@overload
def path(
    route: str,
    view: Callable[..., _ResponseType],
    kwargs: Dict[str, Any] = ...,
    name: str = ...,
) -> URLPattern: ...
@overload
def path(
    route: str, view: IncludedURLConf, kwargs: Dict[str, Any] = ..., name: str = ...
) -> URLResolver: ...
@overload
def path(
    route: str,
    view: List[Union[URLResolver, str]],
    kwargs: Dict[str, Any] = ...,
    name: str = ...,
) -> URLResolver: ...

# re_path()
@overload
def re_path(
    route: str,
    view: Callable[..., _ResponseType],
    kwargs: Dict[str, Any] = ...,
    name: str = ...,
) -> URLPattern: ...
@overload
def re_path(
    route: str, view: IncludedURLConf, kwargs: Dict[str, Any] = ..., name: str = ...
) -> URLResolver: ...
@overload
def re_path(
    route: str,
    view: List[Union[URLResolver, str]],
    kwargs: Dict[str, Any] = ...,
    name: str = ...,
) -> URLResolver: ...
