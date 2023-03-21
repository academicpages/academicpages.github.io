from _typeshed import Incomplete, StrOrBytesPath
from collections.abc import Sequence
from tarfile import TarInfo

def rebuild(
    filename: StrOrBytesPath,
    tag: Incomplete | None = ...,
    format: str = ...,
    zonegroups: Sequence[str | TarInfo] = ...,
    metadata: Incomplete | None = ...,
) -> None: ...
