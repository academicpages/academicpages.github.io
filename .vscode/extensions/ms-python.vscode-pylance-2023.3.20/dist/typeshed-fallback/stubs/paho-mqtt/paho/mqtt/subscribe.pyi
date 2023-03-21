from collections.abc import Callable

from .client import Client, MQTTMessage, _UserData
from .publish import _TLS, _Auth, _Msg, _Proxy

def callback(
    callback: Callable[[Client, _UserData, MQTTMessage], None],
    topics: list[str],
    qos: int = ...,
    userdata: _UserData | None = ...,
    hostname: str = ...,
    port: int = ...,
    client_id: str = ...,
    keepalive: int = ...,
    will: _Msg | None = ...,
    auth: _Auth | None = ...,
    tls: _TLS | None = ...,
    protocol: int = ...,
    transport: str = ...,
    clean_session: bool = ...,
    proxy_args: _Proxy | None = ...,
) -> None: ...
def simple(
    topics: str | list[str],
    qos: int = ...,
    msg_count: int = ...,
    retained: bool = ...,
    hostname: str = ...,
    port: int = ...,
    client_id: str = ...,
    keepalive: int = ...,
    will: _Msg | None = ...,
    auth: _Auth | None = ...,
    tls: _TLS | None = ...,
    protocol: int = ...,
    transport: str = ...,
    clean_session: bool = ...,
    proxy_args: _Proxy | None = ...,
) -> list[MQTTMessage] | MQTTMessage: ...
