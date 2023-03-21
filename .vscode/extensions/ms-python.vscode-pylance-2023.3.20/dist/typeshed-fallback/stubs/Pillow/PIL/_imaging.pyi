from _typeshed import Incomplete
from collections.abc import Sequence
from typing_extensions import Literal

DEFAULT_STRATEGY: Literal[0]
FILTERED: Literal[1]
HUFFMAN_ONLY: Literal[2]
RLE: Literal[3]
FIXED: Literal[4]

class _Path:
    def __getattr__(self, item: str) -> Incomplete: ...

def path(__x: Sequence[tuple[float, float]] | Sequence[float]) -> _Path: ...
def __getattr__(__name: str) -> Incomplete: ...
