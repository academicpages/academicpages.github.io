import builtins
import collections
import contextlib
import itertools
import operator
import pickle as pickle
import threading as threading
from _typeshed import Incomplete, Unused
from abc import ABC as ABC
from datetime import timezone as timezone
from functools import reduce as reduce
from io import BytesIO as BytesIO, StringIO as StringIO
from itertools import zip_longest as zip_longest
from time import perf_counter as perf_counter
from typing import TYPE_CHECKING as TYPE_CHECKING, Any, NamedTuple
from typing_extensions import Literal
from urllib.parse import (
    parse_qsl as parse_qsl,
    quote as quote,
    quote_plus as quote_plus,
    unquote as unquote,
    unquote_plus as unquote_plus,
)

byte_buffer = BytesIO

py39: bool
py38: bool
py37: bool
py3k: Literal[True]
py2k: Literal[False]
pypy: bool
cpython: bool
win32: bool
osx: bool
arm: bool
has_refcount_gc: bool
contextmanager = contextlib.contextmanager
dottedgetter = operator.attrgetter
namedtuple = collections.namedtuple  # noqa: Y024
next = builtins.next

class FullArgSpec(NamedTuple):
    args: Any
    varargs: Any
    varkw: Any
    defaults: Any
    kwonlyargs: Any
    kwonlydefaults: Any
    annotations: Any

class nullcontext:
    enter_result: Any
    def __init__(self, enter_result: Incomplete | None = ...) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *excinfo: Unused) -> None: ...

def inspect_getfullargspec(func): ...
def importlib_metadata_get(group): ...

string_types: tuple[type, ...]
binary_types: tuple[type, ...]
binary_type = bytes
text_type = str
int_types: tuple[type, ...]
iterbytes = iter
long_type = int
itertools_filterfalse = itertools.filterfalse
itertools_filter = filter
itertools_imap = map
exec_: Any
import_: Any
print_: Any

def b(s): ...
def b64decode(x): ...
def b64encode(x): ...
def decode_backslashreplace(text, encoding): ...
def cmp(a, b): ...
def raise_(
    exception, with_traceback: Incomplete | None = ..., replace_context: Incomplete | None = ..., from_: bool = ...
) -> None: ...
def u(s): ...
def ue(s): ...

callable = builtins.callable

def safe_bytestring(text): ...
def inspect_formatargspec(
    args,
    varargs: Incomplete | None = ...,
    varkw: Incomplete | None = ...,
    defaults: Incomplete | None = ...,
    kwonlyargs=...,
    kwonlydefaults=...,
    annotations=...,
    formatarg=...,
    formatvarargs=...,
    formatvarkw=...,
    formatvalue=...,
    formatreturns=...,
    formatannotation=...,
): ...
def dataclass_fields(cls): ...
def local_dataclass_fields(cls): ...
def raise_from_cause(exception, exc_info: Incomplete | None = ...) -> None: ...
def reraise(tp, value, tb: Incomplete | None = ..., cause: Incomplete | None = ...) -> None: ...
def with_metaclass(meta, *bases, **kw): ...
