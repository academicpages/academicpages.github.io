from typing import Any, Optional

from django.db import models

class CurrentSiteManager(models.Manager[Any]):
    def __init__(self, field_name: Optional[str] = ...) -> None: ...
