from _typeshed import Incomplete
from typing import Any

AUTH_HEADER: str
URI_QUERY: str
BODY: str
FORM_ENC_HEADERS: Any

class Client:
    refresh_token_key: str
    client_id: Any
    default_token_placement: Any
    token_type: Any
    access_token: Any
    refresh_token: Any
    mac_key: Any
    mac_algorithm: Any
    token: Any
    scope: Any
    state_generator: Any
    state: Any
    redirect_url: Any
    code: Any
    expires_in: Any
    code_verifier: str
    code_challenge: str
    code_challenge_method: str
    def __init__(
        self,
        client_id,
        default_token_placement=...,
        token_type: str = ...,
        access_token: Incomplete | None = ...,
        refresh_token: Incomplete | None = ...,
        mac_key: Incomplete | None = ...,
        mac_algorithm: Incomplete | None = ...,
        token: Incomplete | None = ...,
        scope: Incomplete | None = ...,
        state: Incomplete | None = ...,
        redirect_url: Incomplete | None = ...,
        state_generator=...,
        code_verifier: str | None = ...,
        code_challenge: str | None = ...,
        code_challenge_method: str | None = ...,
        **kwargs,
    ) -> None: ...
    @property
    def token_types(self): ...
    def prepare_request_uri(self, *args, **kwargs) -> None: ...
    def prepare_request_body(self, *args, **kwargs) -> None: ...
    def parse_request_uri_response(self, *args, **kwargs) -> None: ...
    def add_token(
        self,
        uri,
        http_method: str = ...,
        body: Incomplete | None = ...,
        headers: Incomplete | None = ...,
        token_placement: Incomplete | None = ...,
        **kwargs,
    ): ...
    def prepare_authorization_request(
        self,
        authorization_url,
        state: Incomplete | None = ...,
        redirect_url: Incomplete | None = ...,
        scope: Incomplete | None = ...,
        **kwargs,
    ): ...
    def prepare_token_request(
        self,
        token_url,
        authorization_response: Incomplete | None = ...,
        redirect_url: Incomplete | None = ...,
        state: Incomplete | None = ...,
        body: str = ...,
        **kwargs,
    ): ...
    def prepare_refresh_token_request(
        self, token_url, refresh_token: Incomplete | None = ..., body: str = ..., scope: Incomplete | None = ..., **kwargs
    ): ...
    def prepare_token_revocation_request(
        self, revocation_url, token, token_type_hint: str = ..., body: str = ..., callback: Incomplete | None = ..., **kwargs
    ): ...
    def parse_request_body_response(self, body, scope: Incomplete | None = ..., **kwargs): ...
    def prepare_refresh_body(
        self, body: str = ..., refresh_token: Incomplete | None = ..., scope: Incomplete | None = ..., **kwargs
    ): ...
    def create_code_verifier(self, length: int) -> str: ...
    def create_code_challenge(self, code_verifier: str, code_challenge_method: str | None = ...) -> str: ...
    def populate_code_attributes(self, response) -> None: ...
    def populate_token_attributes(self, response) -> None: ...
