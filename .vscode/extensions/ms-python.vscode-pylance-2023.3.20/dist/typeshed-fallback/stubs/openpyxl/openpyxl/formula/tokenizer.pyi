from _typeshed import Incomplete

class TokenizerError(Exception): ...

class Tokenizer:
    SN_RE: Incomplete
    WSPACE_RE: Incomplete
    STRING_REGEXES: Incomplete
    ERROR_CODES: Incomplete
    TOKEN_ENDERS: str
    formula: Incomplete
    items: Incomplete
    token_stack: Incomplete
    offset: int
    token: Incomplete
    def __init__(self, formula) -> None: ...
    def check_scientific_notation(self): ...
    def assert_empty_token(self, can_follow=...) -> None: ...
    def save_token(self) -> None: ...
    def render(self): ...

class Token:
    LITERAL: str
    OPERAND: str
    FUNC: str
    ARRAY: str
    PAREN: str
    SEP: str
    OP_PRE: str
    OP_IN: str
    OP_POST: str
    WSPACE: str
    value: Incomplete
    type: Incomplete
    subtype: Incomplete
    def __init__(self, value, type_, subtype: str = ...) -> None: ...
    TEXT: str
    NUMBER: str
    LOGICAL: str
    ERROR: str
    RANGE: str
    @classmethod
    def make_operand(cls, value): ...
    OPEN: str
    CLOSE: str
    @classmethod
    def make_subexp(cls, value, func: bool = ...): ...
    def get_closer(self): ...
    ARG: str
    ROW: str
    @classmethod
    def make_separator(cls, value): ...
