from _typeshed import Incomplete
from typing import Any
from typing_extensions import Literal

unix_socket_available: bool

class Server:
    ipc: bool
    host: Any
    port: Any
    allowed_referral_hosts: Any
    ssl: Any
    tls: Any
    name: Any
    get_info: Any
    dit_lock: Any
    custom_formatter: Any
    custom_validator: Any
    current_address: Any
    connect_timeout: Any
    mode: Any
    def __init__(
        self,
        host: str,
        port: int | None = ...,
        use_ssl: bool = ...,
        allowed_referral_hosts: Incomplete | None = ...,
        get_info: Literal["NO_INFO", "DSA", "SCHEMA", "ALL"] = ...,
        tls: Incomplete | None = ...,
        formatter: Incomplete | None = ...,
        connect_timeout: Incomplete | None = ...,
        mode: Literal["IP_SYSTEM_DEFAULT", "IP_V4_ONLY", "IP_V6_ONLY", "IP_V4_PREFERRED", "IP_V6_PREFERRED"] = ...,
        validator: Incomplete | None = ...,
    ) -> None: ...
    @property
    def address_info(self): ...
    def update_availability(self, address, available) -> None: ...
    def reset_availability(self) -> None: ...
    def check_availability(
        self,
        source_address: Incomplete | None = ...,
        source_port: Incomplete | None = ...,
        source_port_list: Incomplete | None = ...,
    ): ...
    @staticmethod
    def next_message_id(): ...
    def get_info_from_server(self, connection) -> None: ...
    def attach_dsa_info(self, dsa_info: Incomplete | None = ...) -> None: ...
    def attach_schema_info(self, dsa_schema: Incomplete | None = ...) -> None: ...
    @property
    def info(self): ...
    @property
    def schema(self): ...
    @staticmethod
    def from_definition(
        host,
        dsa_info,
        dsa_schema,
        port: Incomplete | None = ...,
        use_ssl: bool = ...,
        formatter: Incomplete | None = ...,
        validator: Incomplete | None = ...,
    ): ...
    def candidate_addresses(self): ...
    def has_control(self, control): ...
    def has_extension(self, extension): ...
    def has_feature(self, feature): ...
