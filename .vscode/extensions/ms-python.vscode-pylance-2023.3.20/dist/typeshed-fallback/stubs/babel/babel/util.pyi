import collections
import textwrap
from collections.abc import Generator, Iterable
from datetime import timedelta, tzinfo
from re import Pattern
from typing import IO, Any, TypeVar

from babel import localtime as localtime
from pytz import BaseTzInfo

missing: object

_T = TypeVar("_T")

def distinct(iterable: Iterable[_T]) -> Generator[_T, None, None]: ...

PYTHON_MAGIC_COMMENT_re: Pattern[bytes]

def parse_encoding(fp: IO[bytes]) -> str | None: ...

PYTHON_FUTURE_IMPORT_re: Pattern[str]

def parse_future_flags(fp: IO[bytes], encoding: str = ...) -> int: ...
def pathmatch(pattern: str, filename: str) -> bool: ...

class TextWrapper(textwrap.TextWrapper):
    wordsep_re: Pattern[str]

def wraptext(text, width: int = ..., initial_indent: str = ..., subsequent_indent: str = ...): ...

odict = collections.OrderedDict

class FixedOffsetTimezone(tzinfo):
    zone: str
    def __init__(self, offset: float, name: str | None = ...) -> None: ...
    def utcoffset(self, dt: Any) -> timedelta: ...
    def tzname(self, dt: Any) -> str: ...
    def dst(self, dt: Any) -> timedelta: ...

UTC: BaseTzInfo
LOCALTZ: BaseTzInfo
get_localzone = localtime.get_localzone
STDOFFSET: timedelta
DSTOFFSET: timedelta
DSTDIFF: timedelta
ZERO: timedelta
