from _typeshed import Incomplete

from influxdb_client.domain.check_base import CheckBase

class CheckDiscriminator(CheckBase):
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self,
        id: Incomplete | None = ...,
        name: Incomplete | None = ...,
        org_id: Incomplete | None = ...,
        task_id: Incomplete | None = ...,
        owner_id: Incomplete | None = ...,
        created_at: Incomplete | None = ...,
        updated_at: Incomplete | None = ...,
        query: Incomplete | None = ...,
        status: Incomplete | None = ...,
        description: Incomplete | None = ...,
        latest_completed: Incomplete | None = ...,
        last_run_status: Incomplete | None = ...,
        last_run_error: Incomplete | None = ...,
        labels: Incomplete | None = ...,
        links: Incomplete | None = ...,
    ) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
