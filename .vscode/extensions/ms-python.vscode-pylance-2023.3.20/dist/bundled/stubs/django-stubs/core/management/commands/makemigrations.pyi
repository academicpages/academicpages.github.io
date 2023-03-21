from typing import Any, Dict

from django.apps import apps as apps
from django.conf import settings as settings
from django.core.management.base import BaseCommand as BaseCommand
from django.core.management.base import CommandError as CommandError
from django.core.management.base import no_translations as no_translations
from django.db import DEFAULT_DB_ALIAS as DEFAULT_DB_ALIAS
from django.db import OperationalError as OperationalError
from django.db import connections as connections
from django.db import router as router
from django.db.migrations import Migration as Migration
from django.db.migrations.autodetector import (
    MigrationAutodetector as MigrationAutodetector,
)
from django.db.migrations.loader import MigrationLoader as MigrationLoader
from django.db.migrations.questioner import (
    InteractiveMigrationQuestioner as InteractiveMigrationQuestioner,
)
from django.db.migrations.questioner import MigrationQuestioner as MigrationQuestioner
from django.db.migrations.questioner import (
    NonInteractiveMigrationQuestioner as NonInteractiveMigrationQuestioner,
)
from django.db.migrations.state import ProjectState as ProjectState
from django.db.migrations.utils import (
    get_migration_name_timestamp as get_migration_name_timestamp,
)
from django.db.migrations.writer import MigrationWriter as MigrationWriter

class Command(BaseCommand):
    verbosity: int = ...
    interactive: bool = ...
    dry_run: bool = ...
    merge: bool = ...
    empty: bool = ...
    migration_name: str = ...
    include_header: bool = ...
    def write_migration_files(self, changes: Dict[str, Any]) -> None: ...
    def handle_merge(
        self, loader: MigrationLoader, conflicts: Dict[str, Any]
    ) -> None: ...
