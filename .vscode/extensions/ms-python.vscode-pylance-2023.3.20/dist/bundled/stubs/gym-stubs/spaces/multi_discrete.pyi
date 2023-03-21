from typing import Sequence
from .space import Space

class MultiDiscrete(Space):
    def __init__(self, nvec: Sequence[int]) -> None: ...
