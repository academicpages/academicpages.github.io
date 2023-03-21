from Xlib._typing import Unused
from Xlib.display import Display
from Xlib.protocol import rq
from Xlib.xobject import resource

extname: str
SecurityClientTrusted: int
SecurityClientUntrusted: int
SecurityAuthorizationRevokedMask: int
AUTHID = rq.Card32

class QueryVersion(rq.ReplyRequest): ...

def query_version(self: Display | resource.Resource) -> QueryVersion: ...

class SecurityGenerateAuthorization(rq.ReplyRequest): ...

def generate_authorization(
    self: Display | resource.Resource,
    auth_proto: str,
    auth_data: bytes | bytearray = ...,
    timeout: int | None = ...,
    trust_level: int | None = ...,
    group: int | None = ...,
    event_mask: int | None = ...,
) -> SecurityGenerateAuthorization: ...

class SecurityRevokeAuthorization(rq.Request): ...

def revoke_authorization(self: Display | resource.Resource, authid: int) -> SecurityRevokeAuthorization: ...
def init(disp: Display, info: Unused) -> None: ...
