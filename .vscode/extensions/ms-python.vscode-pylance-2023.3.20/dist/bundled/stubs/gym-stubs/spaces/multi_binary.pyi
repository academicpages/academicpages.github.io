from typing import Union, Sequence

from .space import Space

class MultiBinary(Space):
    def __init__(self, n: Union[int, Sequence[int]]) -> None: ...
