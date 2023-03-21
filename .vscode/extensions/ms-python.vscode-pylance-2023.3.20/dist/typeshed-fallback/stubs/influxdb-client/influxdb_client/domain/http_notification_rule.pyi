from _typeshed import Incomplete

from influxdb_client.domain.http_notification_rule_base import HTTPNotificationRuleBase

class HTTPNotificationRule(HTTPNotificationRuleBase):
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self,
        type: str = ...,
        url: Incomplete | None = ...,
        latest_completed: Incomplete | None = ...,
        last_run_status: Incomplete | None = ...,
        last_run_error: Incomplete | None = ...,
        id: Incomplete | None = ...,
        endpoint_id: Incomplete | None = ...,
        org_id: Incomplete | None = ...,
        task_id: Incomplete | None = ...,
        owner_id: Incomplete | None = ...,
        created_at: Incomplete | None = ...,
        updated_at: Incomplete | None = ...,
        status: Incomplete | None = ...,
        name: Incomplete | None = ...,
        sleep_until: Incomplete | None = ...,
        every: Incomplete | None = ...,
        offset: Incomplete | None = ...,
        runbook_link: Incomplete | None = ...,
        limit_every: Incomplete | None = ...,
        limit: Incomplete | None = ...,
        tag_rules: Incomplete | None = ...,
        description: Incomplete | None = ...,
        status_rules: Incomplete | None = ...,
        labels: Incomplete | None = ...,
        links: Incomplete | None = ...,
    ) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
