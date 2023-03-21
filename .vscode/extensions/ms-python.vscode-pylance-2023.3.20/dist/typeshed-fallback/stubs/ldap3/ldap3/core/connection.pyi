from _collections_abc import Generator, dict_keys
from _typeshed import Incomplete, ReadableBuffer
from types import TracebackType
from typing_extensions import Literal, Self, TypeAlias

from pyasn1.type.base import Asn1Item

from .pooling import ServerPool
from .server import Server

SASL_AVAILABLE_MECHANISMS: Incomplete
CLIENT_STRATEGIES: Incomplete

_ServerSequence: TypeAlias = (
    set[Server] | list[Server] | tuple[Server, ...] | Generator[Server, None, None] | dict_keys[Server, Incomplete]
)

class Connection:
    connection_lock: Incomplete
    last_error: str
    strategy_type: Incomplete
    user: Incomplete
    password: Incomplete
    authentication: Incomplete
    version: Incomplete
    auto_referrals: Incomplete
    request: Incomplete
    response: Incomplete | None
    result: Incomplete
    bound: bool
    listening: bool
    closed: bool
    auto_bind: Incomplete
    sasl_mechanism: Incomplete
    sasl_credentials: Incomplete
    socket: Incomplete
    tls_started: bool
    sasl_in_progress: bool
    read_only: Incomplete
    lazy: Incomplete
    pool_name: Incomplete
    pool_size: int | None
    cred_store: Incomplete
    pool_lifetime: Incomplete
    pool_keepalive: Incomplete
    starting_tls: bool
    check_names: Incomplete
    raise_exceptions: Incomplete
    auto_range: Incomplete
    extend: Incomplete
    fast_decoder: Incomplete
    receive_timeout: Incomplete
    empty_attributes: Incomplete
    use_referral_cache: Incomplete
    auto_escape: Incomplete
    auto_encode: Incomplete
    source_address: Incomplete
    source_port_list: Incomplete
    server_pool: Incomplete | None
    server: Incomplete
    strategy: Incomplete
    send: Incomplete
    open: Incomplete
    get_response: Incomplete
    post_send_single_response: Incomplete
    post_send_search: Incomplete
    def __init__(
        self,
        server: Server | str | _ServerSequence | ServerPool,
        user: str | None = ...,
        password: str | None = ...,
        auto_bind: Literal["DEFAULT", "NONE", "NO_TLS", "TLS_BEFORE_BIND", "TLS_AFTER_BIND"] = ...,
        version: int = ...,
        authentication: Literal["ANONYMOUS", "SIMPLE", "SASL", "NTLM"] | None = ...,
        client_strategy: Literal[
            "SYNC",
            "SAFE_RESTARTABLE",
            "SAFE_SYNC",
            "ASYNC",
            "LDIF",
            "RESTARTABLE",
            "REUSABLE",
            "MOCK_SYNC",
            "MOCK_ASYNC",
            "ASYNC_STREAM",
        ] = ...,
        auto_referrals: bool = ...,
        auto_range: bool = ...,
        sasl_mechanism: str | None = ...,
        sasl_credentials: Incomplete | None = ...,
        check_names: bool = ...,
        collect_usage: bool = ...,
        read_only: bool = ...,
        lazy: bool = ...,
        raise_exceptions: bool = ...,
        pool_name: str | None = ...,
        pool_size: int | None = ...,
        pool_lifetime: int | None = ...,
        cred_store: Incomplete | None = ...,
        fast_decoder: bool = ...,
        receive_timeout: Incomplete | None = ...,
        return_empty_attributes: bool = ...,
        use_referral_cache: bool = ...,
        auto_escape: bool = ...,
        auto_encode: bool = ...,
        pool_keepalive: Incomplete | None = ...,
        source_address: str | None = ...,
        source_port: int | None = ...,
        source_port_list: Incomplete | None = ...,
    ) -> None: ...
    def repr_with_sensitive_data_stripped(self): ...
    @property
    def stream(self): ...
    @stream.setter
    def stream(self, value) -> None: ...
    @property
    def usage(self): ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> Literal[False] | None: ...
    def bind(self, read_server_info: bool = ..., controls: Incomplete | None = ...): ...
    def rebind(
        self,
        user: Incomplete | None = ...,
        password: Incomplete | None = ...,
        authentication: Incomplete | None = ...,
        sasl_mechanism: Incomplete | None = ...,
        sasl_credentials: Incomplete | None = ...,
        read_server_info: bool = ...,
        controls: Incomplete | None = ...,
    ): ...
    def unbind(self, controls: Incomplete | None = ...): ...
    def search(
        self,
        search_base: str,
        search_filter: str,
        search_scope: Literal["BASE", "LEVEL", "SUBTREE"] = ...,
        dereference_aliases: Literal["NEVER", "SEARCH", "FINDING_BASE", "ALWAYS"] = ...,
        attributes: Incomplete | None = ...,
        size_limit: int = ...,
        time_limit: int = ...,
        types_only: bool = ...,
        get_operational_attributes: bool = ...,
        controls: Incomplete | None = ...,
        paged_size: int | None = ...,
        paged_criticality: bool = ...,
        paged_cookie: str | bytes | None = ...,
        auto_escape: bool | None = ...,
    ): ...
    def compare(self, dn, attribute, value, controls: Incomplete | None = ...): ...
    def add(
        self, dn, object_class: Incomplete | None = ..., attributes: Incomplete | None = ..., controls: Incomplete | None = ...
    ): ...
    def delete(self, dn, controls: Incomplete | None = ...): ...
    def modify(self, dn, changes, controls: Incomplete | None = ...): ...
    def modify_dn(
        self, dn, relative_dn, delete_old_dn: bool = ..., new_superior: Incomplete | None = ..., controls: Incomplete | None = ...
    ): ...
    def abandon(self, message_id, controls: Incomplete | None = ...): ...
    def extended(
        self,
        request_name,
        request_value: Asn1Item | ReadableBuffer | None = ...,
        controls: Incomplete | None = ...,
        no_encode: bool | None = ...,
    ): ...
    def start_tls(self, read_server_info: bool = ...): ...
    def do_sasl_bind(self, controls): ...
    def do_ntlm_bind(self, controls): ...
    def refresh_server_info(self) -> None: ...
    def response_to_ldif(
        self,
        search_result: Incomplete | None = ...,
        all_base64: bool = ...,
        line_separator: Incomplete | None = ...,
        sort_order: Incomplete | None = ...,
        stream: Incomplete | None = ...,
    ): ...
    def response_to_json(
        self,
        raw: bool = ...,
        search_result: Incomplete | None = ...,
        indent: int = ...,
        sort: bool = ...,
        stream: Incomplete | None = ...,
        checked_attributes: bool = ...,
        include_empty: bool = ...,
    ): ...
    def response_to_file(self, target, raw: bool = ..., indent: int = ..., sort: bool = ...) -> None: ...
    @property
    def entries(self): ...
