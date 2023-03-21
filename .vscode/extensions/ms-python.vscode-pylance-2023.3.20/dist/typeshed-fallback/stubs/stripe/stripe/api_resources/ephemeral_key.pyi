from _typeshed import Incomplete

from stripe import api_requestor as api_requestor
from stripe.api_resources.abstract import DeletableAPIResource as DeletableAPIResource

class EphemeralKey(DeletableAPIResource):
    OBJECT_NAME: str
    @classmethod
    def create(
        cls,
        api_key: Incomplete | None = ...,
        idempotency_key: str | None = ...,
        stripe_version: Incomplete | None = ...,
        stripe_account: Incomplete | None = ...,
        **params,
    ): ...
