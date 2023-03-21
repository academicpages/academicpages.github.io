from typing import Any, TypeVar, overload

_SD = TypeVar("_SD", bound="SafeData")

class SafeData:
    def __html__(self: _SD) -> _SD: ...

class SafeText(str, SafeData):
    @overload
    def __add__(self, rhs: SafeText) -> SafeText: ...
    @overload
    def __add__(self, rhs: str) -> str: ...
    @overload
    def __iadd__(self, rhs: SafeText) -> SafeText: ...
    @overload
    def __iadd__(self, rhs: str) -> str: ...

SafeString = SafeText

def mark_safe(s: Any) -> SafeText: ...
