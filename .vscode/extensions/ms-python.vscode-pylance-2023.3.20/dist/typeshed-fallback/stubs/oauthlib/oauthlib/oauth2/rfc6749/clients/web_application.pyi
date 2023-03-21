from _typeshed import Incomplete
from typing import Any

from .base import Client as Client

class WebApplicationClient(Client):
    grant_type: str
    code: Any
    def __init__(self, client_id, code: Incomplete | None = ..., **kwargs) -> None: ...
    def prepare_request_uri(
        self,
        uri,
        redirect_uri: Incomplete | None = ...,
        scope: Incomplete | None = ...,
        state: Incomplete | None = ...,
        code_challenge: str | None = ...,
        code_challenge_method: str | None = ...,
        **kwargs,
    ): ...
    def prepare_request_body(
        self,
        code: Incomplete | None = ...,
        redirect_uri: Incomplete | None = ...,
        body: str = ...,
        include_client_id: bool = ...,
        code_verifier: str | None = ...,
        **kwargs,
    ): ...
    def parse_request_uri_response(self, uri, state: Incomplete | None = ...): ...
