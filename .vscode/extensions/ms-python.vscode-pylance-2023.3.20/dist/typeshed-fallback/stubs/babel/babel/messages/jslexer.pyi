from collections.abc import Generator, Sequence
from re import Pattern
from typing import NamedTuple

operators: Sequence[str]
escapes: dict[str, str]
name_re: Pattern[str]
dotted_name_re: Pattern[str]
division_re: Pattern[str]
regex_re: Pattern[str]
line_re: Pattern[str]
line_join_re: Pattern[str]
uni_escape_re: Pattern[str]

class Token(NamedTuple):
    type: str
    value: str
    lineno: int

# Documented as private
def get_rules(jsx: bool, dotted: bool, template_string: bool) -> list[tuple[str | None, Pattern[str]]]: ...  # undocumented
def indicates_division(token: Token) -> bool: ...
def unquote_string(string: str) -> str: ...
def tokenize(source: str, jsx: bool = ..., dotted: bool = ..., template_string: bool = ...) -> Generator[Token, None, None]: ...
