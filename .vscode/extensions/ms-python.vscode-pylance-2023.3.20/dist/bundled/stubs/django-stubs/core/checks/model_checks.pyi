from typing import Any, List, Optional, Sequence

from django.apps.config import AppConfig
from django.core.checks.messages import Warning

def check_all_models(
    app_configs: Optional[Sequence[AppConfig]] = ..., **kwargs: Any
) -> List[Warning]: ...
def check_lazy_references(
    app_configs: Optional[Sequence[AppConfig]] = ..., **kwargs: Any
) -> List[Any]: ...
