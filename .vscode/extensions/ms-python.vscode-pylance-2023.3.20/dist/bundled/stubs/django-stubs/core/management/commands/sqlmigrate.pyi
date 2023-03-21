from typing import Any

from django.apps import apps as apps
from django.core.management.base import BaseCommand as BaseCommand
from django.core.management.base import CommandError as CommandError
from django.db import DEFAULT_DB_ALIAS as DEFAULT_DB_ALIAS
from django.db import connections as connections
from django.db.migrations.loader import AmbiguityError as AmbiguityError
from django.db.migrations.loader import MigrationLoader as MigrationLoader

class Command(BaseCommand):
    output_transaction: bool = ...
    def execute(self, *args: Any, **options: Any) -> Any: ...
