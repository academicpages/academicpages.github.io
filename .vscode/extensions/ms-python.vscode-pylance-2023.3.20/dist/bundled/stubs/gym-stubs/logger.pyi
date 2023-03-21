from typing import Any

DEBUG = 10
INFO = 20
WARN = 30
ERROR = 40
DISABLED = 50

MIN_LEVEL = 30

def set_level(level: int) -> None: ...
def debug(msg: str, *args: Any) -> None: ...
def info(msg: str, *args: Any) -> None: ...
def warn(msg: str, *args: Any) -> None: ...
def error(msg: str, *args: Any) -> None: ...

# DEPRECATED:
setLevel = set_level
