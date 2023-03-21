from typing import Any

from django.db.backends.base.creation import (
    BaseDatabaseCreation as BaseDatabaseCreation,
)

class DatabaseCreation(BaseDatabaseCreation):
    def sql_table_creation_suffix(self) -> Any: ...
