from typing import Mapping, Optional
from .space import Space

class Dict(Space):
    def __init__(
        self, spaces: Optional[Mapping[str, Space]] = ..., **spaces_kwargs: Space
    ) -> None: ...
