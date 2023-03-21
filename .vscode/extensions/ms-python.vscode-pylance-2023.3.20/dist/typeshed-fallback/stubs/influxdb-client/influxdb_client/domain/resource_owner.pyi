from _typeshed import Incomplete

from influxdb_client.domain.user_response import UserResponse

class ResourceOwner(UserResponse):
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self,
        role: str = ...,
        id: Incomplete | None = ...,
        oauth_id: Incomplete | None = ...,
        name: Incomplete | None = ...,
        status: str = ...,
        links: Incomplete | None = ...,
    ) -> None: ...
    @property
    def role(self): ...
    @role.setter
    def role(self, role) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
