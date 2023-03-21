from typing import Any

from django.db.backends.oracle.introspection import (
    DatabaseIntrospection as DatabaseIntrospection,
)

class OracleIntrospection(DatabaseIntrospection):
    def data_types_reverse(self) -> Any: ...
    def get_geometry_type(self, table_name: Any, description: Any) -> Any: ...
