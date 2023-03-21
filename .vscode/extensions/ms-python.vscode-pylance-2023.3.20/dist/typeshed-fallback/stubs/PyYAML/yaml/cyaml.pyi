from _typeshed import Incomplete, SupportsRead
from collections.abc import Mapping, Sequence
from typing import IO, Any
from typing_extensions import TypeAlias

from ._yaml import CEmitter, CParser
from .constructor import BaseConstructor, FullConstructor, SafeConstructor, UnsafeConstructor
from .representer import BaseRepresenter, SafeRepresenter
from .resolver import BaseResolver, Resolver

__all__ = ["CBaseLoader", "CSafeLoader", "CFullLoader", "CUnsafeLoader", "CLoader", "CBaseDumper", "CSafeDumper", "CDumper"]

_Readable: TypeAlias = SupportsRead[str | bytes]
_CLoader: TypeAlias = CLoader | CBaseLoader | CFullLoader | CSafeLoader | CUnsafeLoader  # noqa: Y047  # Used in other modules

class CBaseLoader(CParser, BaseConstructor, BaseResolver):
    def __init__(self, stream: str | bytes | _Readable) -> None: ...

class CLoader(CParser, SafeConstructor, Resolver):
    def __init__(self, stream: str | bytes | _Readable) -> None: ...

class CSafeLoader(CParser, SafeConstructor, Resolver):
    def __init__(self, stream: str | bytes | _Readable) -> None: ...

class CFullLoader(CParser, FullConstructor, Resolver):
    def __init__(self, stream: str | bytes | _Readable) -> None: ...

class CUnsafeLoader(CParser, UnsafeConstructor, Resolver):
    def __init__(self, stream: str | bytes | _Readable) -> None: ...

class CBaseDumper(CEmitter, BaseRepresenter, BaseResolver):
    def __init__(
        self,
        stream: IO[Any],
        default_style: str | None = ...,
        default_flow_style: bool | None = ...,
        canonical: Incomplete | None = ...,
        indent: int | None = ...,
        width: int | None = ...,
        allow_unicode: Incomplete | None = ...,
        line_break: str | None = ...,
        encoding: str | None = ...,
        explicit_start: Incomplete | None = ...,
        explicit_end: Incomplete | None = ...,
        version: Sequence[int] | None = ...,
        tags: Mapping[str, str] | None = ...,
        sort_keys: bool = ...,
    ) -> None: ...

class CDumper(CEmitter, SafeRepresenter, Resolver):
    def __init__(
        self,
        stream: IO[Any],
        default_style: str | None = ...,
        default_flow_style: bool = ...,
        canonical: Incomplete | None = ...,
        indent: int | None = ...,
        width: int | None = ...,
        allow_unicode: Incomplete | None = ...,
        line_break: str | None = ...,
        encoding: str | None = ...,
        explicit_start: Incomplete | None = ...,
        explicit_end: Incomplete | None = ...,
        version: Sequence[int] | None = ...,
        tags: Mapping[str, str] | None = ...,
        sort_keys: bool = ...,
    ) -> None: ...

CSafeDumper = CDumper
