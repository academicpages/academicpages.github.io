from typing import (
    ClassVar,
    Literal,
)

from pandas.core.arrays import ExtensionArray

from pandas._typing import type_t

class ExtensionDtype:
    type: ClassVar[type_t]
    name: ClassVar[str]

    @property
    def na_value(self) -> object: ...
    @property
    def kind(
        self,
    ) -> Literal["b", "i", "u", "f", "c", "m", "M", "O", "S", "U", "V"]: ...
    @property
    def names(self) -> list[str] | None: ...
    def empty(self, size: int | tuple[int, ...]) -> type_t[ExtensionArray]: ...
    @classmethod
    def construct_array_type(cls) -> type_t[ExtensionArray]: ...
    @classmethod
    def construct_from_string(cls, string: str) -> ExtensionDtype: ...
    @classmethod
    def is_dtype(cls, dtype: object) -> bool: ...

class StorageExtensionDtype(ExtensionDtype): ...
