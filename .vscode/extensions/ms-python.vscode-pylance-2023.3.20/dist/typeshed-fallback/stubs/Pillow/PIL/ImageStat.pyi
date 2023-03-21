from _typeshed import Incomplete
from typing import Any

class Stat:
    h: Any
    bands: Any
    def __init__(self, image_or_list, mask: Incomplete | None = ...) -> None: ...
    def __getattr__(self, id: str): ...

Global = Stat
