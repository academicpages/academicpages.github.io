from typing import Any, List, Optional, Sequence

from django.apps.config import AppConfig
from django.core.checks.messages import Warning

W003: Any
W016: Any

def check_csrf_middleware(
    app_configs: Optional[Sequence[AppConfig]] = ..., **kwargs: Any
) -> List[Warning]: ...
def check_csrf_cookie_secure(
    app_configs: Optional[Sequence[AppConfig]] = ..., **kwargs: Any
) -> List[Warning]: ...
