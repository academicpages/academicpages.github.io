from typing import (
    Callable,
    Iterable,
    Mapping,
    Sequence,
    Union,
)

EscapeChars = Union[Mapping[str, str], Iterable[str]]

def adjoin(space: int, *lists: list[str], **kwargs) -> str: ...
def justify(texts: Iterable[str], max_len: int, mode: str = ...) -> list[str]: ...
def pprint_thing(
    thing,
    _nest_lvl: int = ...,
    escape_chars: EscapeChars | None = ...,
    default_escapes: bool = ...,
    quote_strings: bool = ...,
    max_seq_items: int | None = ...,
) -> str: ...
def pprint_thing_encoded(object, encoding: str = ..., errors: str = ...) -> bytes: ...

default_pprint = ...

def format_object_summary(
    obj,
    formatter: Callable,
    is_justify: bool = ...,
    name: str | None = ...,
    indent_for_name: bool = ...,
    line_break_each_value: bool = ...,
) -> str: ...
def format_object_attrs(
    obj: Sequence, include_dtype: bool = ...
) -> list[tuple[str, str | int]]: ...
