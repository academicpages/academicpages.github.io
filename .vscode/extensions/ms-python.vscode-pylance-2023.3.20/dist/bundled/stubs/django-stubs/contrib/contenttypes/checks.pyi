from typing import Any, List, Optional, Sequence

from django.apps.config import AppConfig

def check_generic_foreign_keys(
    app_configs: Optional[Sequence[AppConfig]] = ..., **kwargs: Any
) -> List[Any]: ...
def check_model_name_lengths(
    app_configs: Optional[Sequence[AppConfig]] = ..., **kwargs: Any
) -> List[Any]: ...
