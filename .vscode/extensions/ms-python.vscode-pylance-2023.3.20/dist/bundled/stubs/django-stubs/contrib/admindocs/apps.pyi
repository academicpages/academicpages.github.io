from typing import Any

from django.apps import AppConfig as AppConfig

class AdminDocsConfig(AppConfig):
    name: str = ...
    verbose_name: Any = ...
