from typing import Any

from django.conf import settings as settings
from django.core.management.base import BaseCommand as BaseCommand
from django.core.management.utils import (
    get_command_line_option as get_command_line_option,
)
from django.test.utils import get_runner as get_runner

class Command(BaseCommand):
    test_runner: Any = ...
    def run_from_argv(self, argv: Any) -> None: ...
    def add_arguments(self, parser: Any) -> None: ...
