from collections.abc import Callable, Sequence, Sized
from typing import Any, TypeVar
from typing_extensions import Literal

from Xlib._typing import Unused
from Xlib.display import Display
from Xlib.protocol import display, rq
from Xlib.xobject import resource

_T = TypeVar("_T")
_S = TypeVar("_S", bound=Sized)

extname: str
FromServerTime: int
FromClientTime: int
FromClientSequence: int
CurrentClients: int
FutureClients: int
AllClients: int
FromServer: int
FromClient: int
ClientStarted: int
ClientDied: int
StartOfData: int
EndOfData: int
Record_Range8: rq.Struct
Record_Range16: rq.Struct
Record_ExtRange: rq.Struct
Record_Range: rq.Struct
Record_ClientInfo: rq.Struct

class RawField(rq.ValueField):
    structcode: None
    def pack_value(self, val: _S) -> tuple[_S, int, None]: ...  # type: ignore[override]
    def parse_binary_value(self, data: _T, display: Unused, length: Unused, format: Unused) -> tuple[_T, Literal[""]]: ...  # type: ignore[override]  # See: https://github.com/python-xlib/python-xlib/pull/249

class GetVersion(rq.ReplyRequest): ...

def get_version(self: Display | resource.Resource, major: int, minor: int) -> GetVersion: ...

class CreateContext(rq.Request): ...

def create_context(
    self: Display | resource.Resource,
    datum_flags: int,
    clients: Sequence[int],
    ranges: Sequence[
        tuple[
            tuple[int, int],
            tuple[int, int],
            tuple[int, int],
            tuple[int, int],
            tuple[int, int],
            tuple[int, int],
            tuple[int, int],
            bool,
            bool,
        ]
    ],
) -> int: ...

class RegisterClients(rq.Request): ...

def register_clients(
    self: Display | resource.Resource,
    context: int,
    element_header: int,
    clients: int,
    ranges: Sequence[
        tuple[
            tuple[int, int],
            tuple[int, int],
            tuple[int, int],
            tuple[int, int],
            tuple[int, int],
            tuple[int, int],
            tuple[int, int],
            bool,
            bool,
        ]
    ],
) -> None: ...

class UnregisterClients(rq.Request): ...

def unregister_clients(self: Display | resource.Resource, context: int, clients: Sequence[int]) -> None: ...

class GetContext(rq.ReplyRequest): ...

def get_context(self: Display | resource.Resource, context: int) -> GetContext: ...

class EnableContext(rq.ReplyRequest):
    def __init__(
        self,
        callback: Callable[[rq.DictWrapper | dict[str, Any]], Any],
        display: display.Display,
        defer: bool = ...,
        *args: object | bool,
        **keys: object | bool,
    ) -> None: ...

def enable_context(
    self: Display | resource.Resource, context: int, callback: Callable[[rq.DictWrapper | dict[str, Any]], Any]
) -> None: ...

class DisableContext(rq.Request): ...

def disable_context(self: Display | resource.Resource, context: int) -> None: ...

class FreeContext(rq.Request): ...

def free_context(self: Display | resource.Resource, context: int) -> None: ...
def init(disp: Display, info: Unused) -> None: ...
