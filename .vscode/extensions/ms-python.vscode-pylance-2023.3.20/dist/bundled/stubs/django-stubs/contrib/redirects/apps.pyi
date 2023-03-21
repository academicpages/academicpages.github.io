from typing import Any

from django.apps import AppConfig as AppConfig

class RedirectsConfig(AppConfig):
    name: str = ...
    verbose_name: Any = ...
