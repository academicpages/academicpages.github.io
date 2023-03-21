from functools import partial
from typing import Any

def cubehelix(
    gamma: float = 1, s: float = 0.5, r: float = -1.5, h: float = 1
) -> dict[str, partial]: ...

gfunc: dict[int, Any] = ...

datad: dict[str, tuple[float, ...]] = ...
