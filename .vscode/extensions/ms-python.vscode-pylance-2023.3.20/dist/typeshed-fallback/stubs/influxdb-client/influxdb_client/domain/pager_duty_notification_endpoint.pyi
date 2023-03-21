from _typeshed import Incomplete

from influxdb_client.domain.notification_endpoint_discriminator import NotificationEndpointDiscriminator

class PagerDutyNotificationEndpoint(NotificationEndpointDiscriminator):
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self,
        client_url: Incomplete | None = ...,
        routing_key: Incomplete | None = ...,
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
        type: str = ...,
    ) -> None: ...
    @property
    def client_url(self): ...
    @client_url.setter
    def client_url(self, client_url) -> None: ...
    @property
    def routing_key(self): ...
    @routing_key.setter
    def routing_key(self, routing_key) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
