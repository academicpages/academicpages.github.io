from typing import Any, List

from django.apps import apps as apps
from django.core import checks as checks
from django.core.checks.registry import registry as registry
from django.core.management.base import BaseCommand as BaseCommand
from django.core.management.base import CommandError as CommandError

class Command(BaseCommand):
    def handle(self, *app_labels: List[str], **options: Any) -> None: ...
