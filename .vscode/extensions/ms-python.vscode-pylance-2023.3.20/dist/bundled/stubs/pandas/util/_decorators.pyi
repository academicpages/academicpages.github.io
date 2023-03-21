from collections.abc import (
    Callable,
    Mapping,
)
from typing import Any

from pandas._libs.properties import cache_readonly as cache_readonly
from pandas._typing import F

def deprecate(
    name: str,
    alternative: Callable[..., Any],
    version: str,
    alt_name: str | None = ...,
    klass: type[Warning] | None = ...,
    stacklevel: int = ...,
    msg: str | None = ...,
) -> Callable[..., Any]: ...
def deprecate_kwarg(
    old_arg_name: str,
    new_arg_name: str | None,
    mapping: Mapping[Any, Any] | Callable[[Any], Any] | None = ...,
    stacklevel: int = ...,
) -> Callable[..., Any]: ...
def rewrite_axis_style_signature(
    name: str, extra_params: list[tuple[str, Any]]
) -> Callable[..., Any]: ...

class Substitution:
    params = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __call__(self, func: F) -> F: ...
    def update(self, *args, **kwargs) -> None: ...

class Appender:
    addendum: str | None
    join = ...
    def __init__(
        self, addendum: str | None, join: str = ..., indents: int = ...
    ) -> None: ...
    def __call__(self, func: F) -> F: ...

def indent(text: str | None, indents: int = ...) -> str: ...
