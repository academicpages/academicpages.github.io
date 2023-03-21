import ssl
from collections.abc import Iterable
from typing_extensions import NotRequired, TypeAlias, TypedDict

_Payload: TypeAlias = str | bytes | bytearray | float

class _Msg(TypedDict):
    topic: str
    payload: NotRequired[_Payload | None]
    qos: NotRequired[int]
    retain: NotRequired[int]

class _Auth(TypedDict):
    username: str
    password: NotRequired[str]

class _TLS(TypedDict):
    ca_certs: str
    certfile: NotRequired[str]
    keyfile: NotRequired[str]
    tls_version: NotRequired[ssl._SSLMethod]
    ciphers: NotRequired[str]
    insecure: NotRequired[str]
    cert_reqs: NotRequired[ssl.VerifyMode]
    keyfile_password: NotRequired[ssl._PasswordType]

class _Proxy(TypedDict):
    proxy_type: int
    proxy_addr: str
    proxy_rdns: NotRequired[bool]
    proxy_username: NotRequired[str]
    proxy_passwor: NotRequired[str]

def multiple(
    msgs: Iterable[_Msg],
    hostname: str = ...,
    port: int = ...,
    client_id: str = ...,
    keepalive: int = ...,
    will: _Msg | None = ...,
    auth: _Auth | None = ...,
    tls: _TLS | None = ...,
    protocol: int = ...,
    transport: str = ...,
    proxy_args: _Proxy | None = ...,
) -> None: ...
def single(
    topic: str,
    payload: _Payload | None = ...,
    qos: int | None = ...,
    retain: bool | None = ...,
    hostname: str = ...,
    port: int = ...,
    client_id: str = ...,
    keepalive: int = ...,
    will: _Msg | None = ...,
    auth: _Auth | None = ...,
    tls: _TLS | None = ...,
    protocol: int = ...,
    transport: str = ...,
    proxy_args: _Proxy | None = ...,
) -> None: ...
