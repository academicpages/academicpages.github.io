from logging import Logger
from typing import Any

from ._types import Reader

__version__: str
logger: Logger

def process_file(
    fh: Reader,
    stop_tag: str = ...,
    details: bool = ...,
    strict: bool = ...,
    debug: bool = ...,
    truncate_tags: bool = ...,
    auto_seek: bool = ...,
) -> dict[str, Any]: ...
