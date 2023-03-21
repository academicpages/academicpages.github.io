from typing import Any, List

from django.conf import settings as settings
from django.core.cache import caches as caches
from django.core.cache.backends.db import BaseDatabaseCache as BaseDatabaseCache
from django.core.management.base import BaseCommand as BaseCommand
from django.core.management.base import CommandError as CommandError
from django.db import DEFAULT_DB_ALIAS as DEFAULT_DB_ALIAS
from django.db import DatabaseError as DatabaseError
from django.db import connections as connections
from django.db import models as models
from django.db import router as router
from django.db import transaction as transaction

class Command(BaseCommand):
    verbosity: int = ...
    def handle(self, *tablenames: List[str], **options: Any) -> None: ...
    def create_table(self, database: str, tablename: str, dry_run: bool) -> None: ...
