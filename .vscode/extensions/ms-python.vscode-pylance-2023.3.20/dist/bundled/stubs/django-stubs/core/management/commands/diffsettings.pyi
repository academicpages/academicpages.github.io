from typing import Any, Callable, Dict, List

from django.core.management.base import BaseCommand as BaseCommand

def module_to_dict(
    module: Any, omittable: Callable[[str], bool] = ...
) -> Dict[str, str]: ...

class Command(BaseCommand):
    def output_hash(
        self,
        user_settings: Dict[str, str],
        default_settings: Dict[str, str],
        **options: Any
    ) -> List[str]: ...
    def output_unified(
        self,
        user_settings: Dict[str, str],
        default_settings: Dict[str, str],
        **options: Any
    ) -> List[str]: ...
