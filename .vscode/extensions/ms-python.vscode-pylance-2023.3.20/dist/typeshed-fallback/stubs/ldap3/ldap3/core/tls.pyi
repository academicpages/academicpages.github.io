from _typeshed import Incomplete
from typing import Any

use_ssl_context: bool

class Tls:
    ssl_options: Any
    validate: Any
    ca_certs_file: Any
    ca_certs_path: Any
    ca_certs_data: Any
    private_key_password: Any
    version: Any
    private_key_file: Any
    certificate_file: Any
    valid_names: Any
    ciphers: Any
    sni: Any
    def __init__(
        self,
        local_private_key_file: Incomplete | None = ...,
        local_certificate_file: Incomplete | None = ...,
        validate=...,
        version: Incomplete | None = ...,
        ssl_options: Incomplete | None = ...,
        ca_certs_file: Incomplete | None = ...,
        valid_names: Incomplete | None = ...,
        ca_certs_path: Incomplete | None = ...,
        ca_certs_data: Incomplete | None = ...,
        local_private_key_password: Incomplete | None = ...,
        ciphers: Incomplete | None = ...,
        sni: Incomplete | None = ...,
    ) -> None: ...
    def wrap_socket(self, connection, do_handshake: bool = ...) -> None: ...
    def start_tls(self, connection): ...

def check_hostname(sock, server_name, additional_names) -> None: ...
