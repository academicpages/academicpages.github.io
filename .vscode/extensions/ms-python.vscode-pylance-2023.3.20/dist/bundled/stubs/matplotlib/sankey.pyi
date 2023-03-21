from typing import Sequence
from .axes import Axes
from types import SimpleNamespace

RIGHT = ...
UP = ...
DOWN = ...

class Sankey:
    def __init__(
        self,
        ax: Axes | None = ...,
        scale: float = ...,
        unit: str = ...,
        format: str = ...,
        gap: float = ...,
        radius: float = ...,
        shoulder: float = ...,
        offset: float = ...,
        head_angle: int = ...,
        margin: float = ...,
        tolerance: float = ...,
        **kwargs
    ) -> None: ...
    def add(
        self,
        patchlabel: str = ...,
        flows: Sequence[float] = ...,
        orientations: Sequence[int] = ...,
        labels: Sequence[str | None] = ...,
        trunklength: float = ...,
        pathlengths: Sequence[float] = ...,
        prior: int = ...,
        connect: Sequence[int] = ...,
        rotation: float = ...,
        **kwargs
    ) -> Sankey: ...
    def finish(self) -> list[SimpleNamespace]: ...
