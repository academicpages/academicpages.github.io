from _typeshed import Incomplete
from typing import Any

from .base import BaseEndpoint as BaseEndpoint

log: Any

class SignatureOnlyEndpoint(BaseEndpoint):
    def validate_request(self, uri, http_method: str = ..., body: Incomplete | None = ..., headers: Incomplete | None = ...): ...
