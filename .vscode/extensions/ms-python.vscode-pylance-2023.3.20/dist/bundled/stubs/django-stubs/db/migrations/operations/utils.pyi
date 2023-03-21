from typing import Any

from django.db.migrations.state import ProjectState
from django.db.models.fields import Field

def is_referenced_by_foreign_key(
    state: ProjectState, model_name_lower: str, field: Field[Any, Any], field_name: str
) -> bool: ...
