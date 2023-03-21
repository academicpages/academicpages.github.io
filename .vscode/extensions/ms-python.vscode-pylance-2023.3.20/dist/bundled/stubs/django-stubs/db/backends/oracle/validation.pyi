from typing import Any

from django.db.backends.base.validation import (
    BaseDatabaseValidation as BaseDatabaseValidation,
)

class DatabaseValidation(BaseDatabaseValidation):
    def check_field_type(self, field: Any, field_type: Any) -> Any: ...
