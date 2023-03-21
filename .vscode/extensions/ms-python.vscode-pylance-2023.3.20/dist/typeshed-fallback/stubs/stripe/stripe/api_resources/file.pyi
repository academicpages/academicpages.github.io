from _typeshed import Incomplete

from stripe import api_requestor as api_requestor
from stripe.api_resources.abstract import ListableAPIResource as ListableAPIResource

class File(ListableAPIResource):
    OBJECT_NAME: str
    OBJECT_NAME_ALT: str
    @classmethod
    def class_url(cls): ...
    @classmethod
    def create(
        cls,
        api_key: Incomplete | None = ...,
        api_version: Incomplete | None = ...,
        stripe_version: Incomplete | None = ...,
        stripe_account: Incomplete | None = ...,
        **params,
    ): ...

FileUpload = File
