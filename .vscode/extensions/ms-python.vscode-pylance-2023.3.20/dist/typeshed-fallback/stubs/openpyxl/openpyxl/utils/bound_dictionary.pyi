from _typeshed import Incomplete
from collections import defaultdict

class BoundDictionary(defaultdict[Incomplete, Incomplete]):
    reference: Incomplete
    def __init__(self, reference: Incomplete | None = ..., *args, **kw) -> None: ...
    def __getitem__(self, key): ...
