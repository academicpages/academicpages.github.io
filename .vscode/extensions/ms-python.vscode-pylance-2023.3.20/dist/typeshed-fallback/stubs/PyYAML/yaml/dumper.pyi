from collections.abc import Mapping
from typing import Any
from typing_extensions import TypeAlias

from yaml.emitter import Emitter
from yaml.representer import BaseRepresenter, Representer, SafeRepresenter
from yaml.resolver import BaseResolver, Resolver
from yaml.serializer import Serializer

from .emitter import _WriteStream

# Ideally, there would be a way to limit these values to only +/- float("inf"),
# but that's not possible at the moment (https://github.com/python/typing/issues/1160).
_Inf: TypeAlias = float

class BaseDumper(Emitter, Serializer, BaseRepresenter, BaseResolver):
    def __init__(
        self,
        stream: _WriteStream[Any],
        default_style: str | None = ...,
        default_flow_style: bool | None = ...,
        canonical: bool | None = ...,
        indent: int | None = ...,
        width: int | _Inf | None = ...,
        allow_unicode: bool | None = ...,
        line_break: str | None = ...,
        encoding: str | None = ...,
        explicit_start: bool | None = ...,
        explicit_end: bool | None = ...,
        version: tuple[int, int] | None = ...,
        tags: Mapping[str, str] | None = ...,
        sort_keys: bool = ...,
    ) -> None: ...

class SafeDumper(Emitter, Serializer, SafeRepresenter, Resolver):
    def __init__(
        self,
        stream: _WriteStream[Any],
        default_style: str | None = ...,
        default_flow_style: bool | None = ...,
        canonical: bool | None = ...,
        indent: int | None = ...,
        width: int | _Inf | None = ...,
        allow_unicode: bool | None = ...,
        line_break: str | None = ...,
        encoding: str | None = ...,
        explicit_start: bool | None = ...,
        explicit_end: bool | None = ...,
        version: tuple[int, int] | None = ...,
        tags: Mapping[str, str] | None = ...,
        sort_keys: bool = ...,
    ) -> None: ...

class Dumper(Emitter, Serializer, Representer, Resolver):
    def __init__(
        self,
        stream: _WriteStream[Any],
        default_style: str | None = ...,
        default_flow_style: bool | None = ...,
        canonical: bool | None = ...,
        indent: int | None = ...,
        width: int | _Inf | None = ...,
        allow_unicode: bool | None = ...,
        line_break: str | None = ...,
        encoding: str | None = ...,
        explicit_start: bool | None = ...,
        explicit_end: bool | None = ...,
        version: tuple[int, int] | None = ...,
        tags: Mapping[str, str] | None = ...,
        sort_keys: bool = ...,
    ) -> None: ...
