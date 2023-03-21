from typing import Any

from django.contrib.gis.db.backends.base.adapter import WKTAdapter as WKTAdapter

class SpatiaLiteAdapter(WKTAdapter):
    def __conform__(self, protocol: Any) -> Any: ...
