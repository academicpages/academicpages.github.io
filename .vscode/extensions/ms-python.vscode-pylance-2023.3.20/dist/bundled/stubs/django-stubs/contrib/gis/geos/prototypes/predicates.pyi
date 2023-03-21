from typing import Any

from django.contrib.gis.geos.libgeos import GEOSFuncFactory as GEOSFuncFactory

class UnaryPredicate(GEOSFuncFactory):
    argtypes: Any = ...
    restype: Any = ...
    errcheck: Any = ...

class BinaryPredicate(UnaryPredicate):
    argtypes: Any = ...

geos_hasz: Any
geos_isclosed: Any
geos_isempty: Any
geos_isring: Any
geos_issimple: Any
geos_isvalid: Any
geos_contains: Any
geos_covers: Any
geos_crosses: Any
geos_disjoint: Any
geos_equals: Any
geos_equalsexact: Any
geos_intersects: Any
geos_overlaps: Any
geos_relatepattern: Any
geos_touches: Any
geos_within: Any
