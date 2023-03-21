from .collections import PolyCollection
from typing import Literal, Sequence
from ._typing import *

__all__ = ["stackplot"]

def stackplot(
    axes,
    x: ArrayLike,
    *args,
    labels: Sequence[str] = ...,
    colors: Sequence[Color] = ...,
    baseline: Literal["zero", "sym", "wiggle", "weighted_wiggle"] = ...,
    **kwargs
) -> list[PolyCollection]: ...
