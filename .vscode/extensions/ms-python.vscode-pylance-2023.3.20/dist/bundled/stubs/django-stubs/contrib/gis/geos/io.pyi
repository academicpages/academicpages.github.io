from typing import Any

from django.contrib.gis.geos.prototypes.io import WKBWriter as WKBWriter  # noqa: F401
from django.contrib.gis.geos.prototypes.io import WKTWriter as WKTWriter
from django.contrib.gis.geos.prototypes.io import _WKBReader, _WKTReader

class WKBReader(_WKBReader):
    def read(self, wkb: Any) -> Any: ...

class WKTReader(_WKTReader):
    def read(self, wkt: Any) -> Any: ...
