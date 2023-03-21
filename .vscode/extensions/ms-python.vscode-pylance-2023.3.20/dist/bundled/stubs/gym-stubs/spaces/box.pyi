from typing import Any, Optional, Sequence, Type, Union

from .space import Space

class Box(Space):
    def __init__(
        self,
        low: Union[float, Sequence[float]],
        high: Union[float, Sequence[float]],
        shape: Optional[Any] = ...,
        dtype: Optional[Type[Any]] = ...,
    ) -> None: ...
    def is_bounded(self, manner: str = ...) -> bool: ...
