from typing import Any

from django.core.cache.backends.base import BaseCache

class BaseMemcachedCache(BaseCache):
    def __init__(
        self, server: Any, params: Any, library: Any, value_not_found_exception: Any
    ) -> None: ...

class MemcachedCache(BaseMemcachedCache):
    def __init__(self, server: Any, params: Any) -> None: ...

class PyLibMCCache(BaseMemcachedCache):
    def __init__(self, server: Any, params: Any) -> None: ...
