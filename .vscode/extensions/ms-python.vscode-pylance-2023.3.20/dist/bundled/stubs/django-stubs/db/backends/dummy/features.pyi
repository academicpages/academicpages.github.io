from django.db.backends.base.features import (
    BaseDatabaseFeatures as BaseDatabaseFeatures,
)

class DummyDatabaseFeatures(BaseDatabaseFeatures):
    supports_transactions: bool = ...  # type: ignore [assignment]
    uses_savepoints: bool = ...
