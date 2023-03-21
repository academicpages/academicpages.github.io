from typing import Any

from django.db.backends.base.creation import (
    BaseDatabaseCreation as BaseDatabaseCreation,
)

TEST_DATABASE_PREFIX: str

class DatabaseCreation(BaseDatabaseCreation):
    def set_as_test_mirror(self, primary_settings_dict: Any) -> None: ...
    def test_db_signature(self) -> Any: ...
