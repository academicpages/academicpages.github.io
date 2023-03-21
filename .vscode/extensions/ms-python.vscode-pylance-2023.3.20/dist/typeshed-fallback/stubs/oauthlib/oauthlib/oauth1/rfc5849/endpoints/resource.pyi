from _typeshed import Incomplete
from typing import Any

from .base import BaseEndpoint as BaseEndpoint

log: Any

class ResourceEndpoint(BaseEndpoint):
    def validate_protected_resource_request(
        self,
        uri,
        http_method: str = ...,
        body: Incomplete | None = ...,
        headers: Incomplete | None = ...,
        realms: Incomplete | None = ...,
    ): ...
