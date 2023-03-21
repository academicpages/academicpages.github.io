from _typeshed import Incomplete
from typing_extensions import Self

from stripe import api_requestor as api_requestor
from stripe.api_resources.abstract.api_resource import APIResource as APIResource

class CreateableAPIResource(APIResource):
    @classmethod
    def create(
        cls,
        api_key: Incomplete | None = ...,
        idempotency_key: str | None = ...,
        stripe_version: Incomplete | None = ...,
        stripe_account: Incomplete | None = ...,
        **params,
    ) -> Self: ...
