from typing import Any

from ._distutils.extension import Extension as _Extension

have_pyrex: Any

class Extension(_Extension):
    py_limited_api: Any
    def __init__(self, name, sources, *args, **kw) -> None: ...

class Library(Extension): ...
