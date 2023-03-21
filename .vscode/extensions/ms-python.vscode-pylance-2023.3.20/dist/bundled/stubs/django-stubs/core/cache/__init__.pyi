from collections import OrderedDict
from typing import Any, Callable, Dict, Union

from .backends.base import BaseCache as BaseCache
from .backends.base import CacheKeyWarning as CacheKeyWarning
from .backends.base import InvalidCacheBackendError as InvalidCacheBackendError

DEFAULT_CACHE_ALIAS: str

class CacheHandler:
    def __init__(self) -> None: ...
    def __getitem__(self, alias: str) -> BaseCache: ...
    def all(self) -> Any: ...

class DefaultCacheProxy:
    def __getattr__(
        self, name: str
    ) -> Union[Callable[..., Any], Dict[str, float], OrderedDict[Any, Any], int]: ...
    def __setattr__(self, name: str, value: Callable[..., Any]) -> None: ...
    def __delattr__(self, name: Any) -> Any: ...
    def __contains__(self, key: str) -> bool: ...

cache: BaseCache
caches: CacheHandler
