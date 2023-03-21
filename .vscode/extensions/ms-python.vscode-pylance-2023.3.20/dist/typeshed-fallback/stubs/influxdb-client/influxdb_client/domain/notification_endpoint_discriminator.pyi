from _typeshed import Incomplete

from influxdb_client.domain.notification_endpoint_base import NotificationEndpointBase

class NotificationEndpointDiscriminator(NotificationEndpointBase):
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self,
        id: Incomplete | None = ...,
        org_id: Incomplete | None = ...,
        user_id: Incomplete | None = ...,
        created_at: Incomplete | None = ...,
        updated_at: Incomplete | None = ...,
        description: Incomplete | None = ...,
        name: Incomplete | None = ...,
        status: str = ...,
        labels: Incomplete | None = ...,
        links: Incomplete | None = ...,
        type: Incomplete | None = ...,
    ) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
