from Xlib._typing import ErrorHandler
from Xlib.display import Display
from Xlib.protocol import request, rq
from Xlib.xobject import drawable

extname: str
NotifyMask: int
CycleMask: int
StateOff: int
StateOn: int
StateCycle: int
KindBlanked: int
KindInternal: int
KindExternal: int

class QueryVersion(rq.ReplyRequest): ...

def query_version(self: drawable.Drawable) -> QueryVersion: ...

class QueryInfo(rq.ReplyRequest): ...

def query_info(self: drawable.Drawable) -> QueryInfo: ...

class SelectInput(rq.Request): ...

def select_input(self: drawable.Drawable, mask: int) -> SelectInput: ...

class SetAttributes(rq.Request): ...

def set_attributes(
    self: drawable.Drawable,
    x: int,
    y: int,
    width: int,
    height: int,
    border_width: int,
    window_class: int = ...,
    depth: int = ...,
    visual: int = ...,
    onerror: ErrorHandler[object] | None = ...,
    **keys: object,
) -> SetAttributes: ...

class UnsetAttributes(rq.Request): ...

def unset_attributes(self: drawable.Drawable, onerror: ErrorHandler[object] | None = ...) -> UnsetAttributes: ...

class Notify(rq.Event): ...

def init(disp: Display, info: request.QueryExtension) -> None: ...
