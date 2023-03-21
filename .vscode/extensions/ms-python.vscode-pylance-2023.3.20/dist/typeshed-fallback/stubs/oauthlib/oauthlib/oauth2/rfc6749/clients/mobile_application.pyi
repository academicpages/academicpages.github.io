from _typeshed import Incomplete
from typing import Any

from .base import Client as Client

class MobileApplicationClient(Client):
    response_type: str
    def prepare_request_uri(
        self, uri, redirect_uri: Incomplete | None = ..., scope: Incomplete | None = ..., state: Incomplete | None = ..., **kwargs
    ): ...
    token: Any
    def parse_request_uri_response(self, uri, state: Incomplete | None = ..., scope: Incomplete | None = ...): ...
