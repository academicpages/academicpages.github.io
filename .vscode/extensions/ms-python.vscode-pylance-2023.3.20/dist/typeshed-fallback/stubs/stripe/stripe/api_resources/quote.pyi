from _typeshed import Incomplete

from stripe import api_requestor as api_requestor
from stripe.api_resources.abstract import (
    CreateableAPIResource as CreateableAPIResource,
    ListableAPIResource as ListableAPIResource,
    UpdateableAPIResource as UpdateableAPIResource,
    custom_method as custom_method,
)

class Quote(CreateableAPIResource, ListableAPIResource, UpdateableAPIResource):
    OBJECT_NAME: str
    def accept(self, idempotency_key: str | None = ..., **params): ...
    def cancel(self, idempotency_key: str | None = ..., **params): ...
    def finalize_quote(self, idempotency_key: str | None = ..., **params): ...
    def list_line_items(self, idempotency_key: str | None = ..., **params): ...
    def pdf(
        self,
        api_key: Incomplete | None = ...,
        api_version: Incomplete | None = ...,
        stripe_version: Incomplete | None = ...,
        stripe_account: Incomplete | None = ...,
        **params,
    ): ...
