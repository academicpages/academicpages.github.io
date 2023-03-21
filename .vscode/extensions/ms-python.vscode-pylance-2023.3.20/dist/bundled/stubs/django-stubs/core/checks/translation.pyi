from typing import Any, List, Optional, Sequence

from django.apps.config import AppConfig

from . import Error

E001: Error = ...

def check_setting_language_code(
    app_configs: Optional[Sequence[AppConfig]] = ..., **kwargs: Any
) -> List[Error]: ...
