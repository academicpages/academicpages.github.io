from _typeshed import Incomplete

from influxdb_client.domain.notification_rule_discriminator import NotificationRuleDiscriminator

class TelegramNotificationRuleBase(NotificationRuleDiscriminator):
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self,
        type: Incomplete | None = ...,
        message_template: Incomplete | None = ...,
        parse_mode: Incomplete | None = ...,
        disable_web_page_preview: Incomplete | None = ...,
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
    @property
    def type(self): ...
    @type.setter
    def type(self, type) -> None: ...
    @property
    def message_template(self): ...
    @message_template.setter
    def message_template(self, message_template) -> None: ...
    @property
    def parse_mode(self): ...
    @parse_mode.setter
    def parse_mode(self, parse_mode) -> None: ...
    @property
    def disable_web_page_preview(self): ...
    @disable_web_page_preview.setter
    def disable_web_page_preview(self, disable_web_page_preview) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
