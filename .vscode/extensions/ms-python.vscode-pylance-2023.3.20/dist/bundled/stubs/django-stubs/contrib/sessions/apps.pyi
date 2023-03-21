from typing import Any

from django.apps import AppConfig as AppConfig

class SessionsConfig(AppConfig):
    name: str = ...
    verbose_name: Any = ...
