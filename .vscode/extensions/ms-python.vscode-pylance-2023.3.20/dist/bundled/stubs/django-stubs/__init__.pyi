from typing import Any

from .utils.version import get_version as get_version

VERSION: Any
__version__: str

def setup(set_prefix: bool = ...) -> None: ...
