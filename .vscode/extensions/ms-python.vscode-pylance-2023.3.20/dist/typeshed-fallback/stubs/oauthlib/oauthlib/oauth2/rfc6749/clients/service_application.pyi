from _typeshed import Incomplete
from typing import Any

from .base import Client as Client

class ServiceApplicationClient(Client):
    grant_type: str
    private_key: Any
    subject: Any
    issuer: Any
    audience: Any
    def __init__(
        self,
        client_id,
        private_key: Incomplete | None = ...,
        subject: Incomplete | None = ...,
        issuer: Incomplete | None = ...,
        audience: Incomplete | None = ...,
        **kwargs,
    ) -> None: ...
    def prepare_request_body(
        self,
        private_key: Incomplete | None = ...,
        subject: Incomplete | None = ...,
        issuer: Incomplete | None = ...,
        audience: Incomplete | None = ...,
        expires_at: Incomplete | None = ...,
        issued_at: Incomplete | None = ...,
        extra_claims: Incomplete | None = ...,
        body: str = ...,
        scope: Incomplete | None = ...,
        include_client_id: bool = ...,
        **kwargs,
    ): ...
