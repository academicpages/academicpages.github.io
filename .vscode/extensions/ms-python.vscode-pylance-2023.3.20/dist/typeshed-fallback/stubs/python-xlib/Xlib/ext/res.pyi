from collections.abc import Sequence

from Xlib._typing import Unused
from Xlib.display import Display
from Xlib.protocol import rq
from Xlib.xobject import resource

RES_MAJOR_VERSION: int
RES_MINOR_VERSION: int
extname: str
ResQueryVersion: int
ResQueryClients: int
ResQueryClientResources: int
ResQueryClientPixmapBytes: int
ResQueryClientIds: int
ResQueryResourceBytes: int

class QueryVersion(rq.ReplyRequest): ...

def query_version(self: Display | resource.Resource, client_major: int = ..., client_minor: int = ...) -> QueryVersion: ...

Client: rq.Struct

class QueryClients(rq.ReplyRequest): ...

def query_clients(self: Display | resource.Resource) -> QueryClients: ...

Type: rq.Struct

class QueryClientResources(rq.ReplyRequest): ...

def query_client_resources(self: Display | resource.Resource, client: int) -> QueryClientResources: ...

class QueryClientPixmapBytes(rq.ReplyRequest): ...

def query_client_pixmap_bytes(self: Display | resource.Resource, client: int) -> QueryClientPixmapBytes: ...

class SizeOf(rq.LengthOf):
    item_size: int
    def __init__(self, name: str | list[str] | tuple[str, ...], size: int, item_size: int) -> None: ...
    def parse_value(self, length: int, display: Unused) -> int: ...  # type: ignore[override]

ClientXIDMask: int
LocalClientPIDMask: int
ClientIdSpec: rq.Struct
ClientIdValue: rq.Struct

class QueryClientIds(rq.ReplyRequest): ...

def query_client_ids(self: Display | resource.Resource, specs: Sequence[tuple[int, int]]) -> QueryClientIds: ...

ResourceIdSpec: rq.Struct
ResourceSizeSpec: rq.Struct
ResourceSizeValue: rq.Struct

class QueryResourceBytes(rq.ReplyRequest): ...

def query_resource_bytes(
    self: Display | resource.Resource, client: int, specs: Sequence[tuple[int, int]]
) -> QueryResourceBytes: ...
def init(disp: Display, info: Unused) -> None: ...
