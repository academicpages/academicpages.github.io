from typing import Any, List, Optional, Sequence

from django.apps.config import AppConfig
from django.core.checks.messages import Error

E001: Any
E002: Any

def check_setting_app_dirs_loaders(
    app_configs: Optional[Sequence[AppConfig]] = ..., **kwargs: Any
) -> List[Error]: ...
def check_string_if_invalid_is_string(
    app_configs: Optional[Sequence[AppConfig]] = ..., **kwargs: Any
) -> List[Error]: ...
