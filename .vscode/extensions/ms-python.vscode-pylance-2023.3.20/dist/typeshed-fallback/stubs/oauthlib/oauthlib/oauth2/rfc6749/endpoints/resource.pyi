from _typeshed import Incomplete
from typing import Any

from .base import BaseEndpoint as BaseEndpoint

log: Any

class ResourceEndpoint(BaseEndpoint):
    def __init__(self, default_token, token_types) -> None: ...
    @property
    def default_token(self): ...
    @property
    def default_token_type_handler(self): ...
    @property
    def tokens(self): ...
    def verify_request(
        self,
        uri,
        http_method: str = ...,
        body: Incomplete | None = ...,
        headers: Incomplete | None = ...,
        scopes: Incomplete | None = ...,
    ): ...
    def find_token_type(self, request): ...
