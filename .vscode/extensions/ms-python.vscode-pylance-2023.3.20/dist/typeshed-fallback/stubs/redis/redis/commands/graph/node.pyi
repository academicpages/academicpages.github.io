from _typeshed import Incomplete
from typing import Any

class Node:
    id: Any
    alias: Any
    label: Any
    labels: Any
    properties: Any
    def __init__(
        self,
        node_id: Incomplete | None = ...,
        alias: Incomplete | None = ...,
        label: str | list[str] | None = ...,
        properties: Incomplete | None = ...,
    ) -> None: ...
    def to_string(self): ...
    def __eq__(self, rhs): ...
