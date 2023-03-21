import decimal
from datetime import date
from re import Pattern
from typing_extensions import Literal

from babel.core import Locale

long = int
LC_NUMERIC: str | None

class UnknownCurrencyError(Exception):
    identifier: str
    def __init__(self, identifier: str) -> None: ...

def list_currencies(locale: Locale | str | None = ...) -> set[str]: ...
def validate_currency(currency: str, locale: Locale | str | None = ...) -> None: ...
def is_currency(currency: str, locale: Locale | str | None = ...) -> bool: ...
def normalize_currency(currency: str, locale: Locale | str | None = ...) -> str | None: ...
def get_currency_name(currency: str, count: float | decimal.Decimal | None = ..., locale: Locale | str | None = ...) -> str: ...
def get_currency_symbol(currency: str, locale: Locale | str | None = ...) -> str: ...
def get_currency_precision(currency: str) -> int: ...
def get_currency_unit_pattern(currency: str, count: float | None = ..., locale: Locale | str | None = ...) -> str: ...
def get_territory_currencies(
    territory: str,
    start_date: date | None = ...,
    end_date: date | None = ...,
    tender: bool = ...,
    non_tender: bool = ...,
    include_details: bool = ...,
) -> list[str]: ...
def get_decimal_symbol(locale: Locale | str | None = ...) -> str: ...
def get_plus_sign_symbol(locale: Locale | str | None = ...) -> str: ...
def get_minus_sign_symbol(locale: Locale | str | None = ...) -> str: ...
def get_exponential_symbol(locale: Locale | str | None = ...) -> str: ...
def get_group_symbol(locale: Locale | str | None = ...) -> str: ...
def format_number(number: float | decimal.Decimal | str, locale: Locale | str | None = ...) -> str: ...
def get_decimal_precision(number: decimal.Decimal) -> int: ...
def get_decimal_quantum(precision: int | decimal.Decimal) -> decimal.Decimal: ...
def format_decimal(
    number: float | decimal.Decimal | str,
    format: str | None = ...,
    locale: Locale | str | None = ...,
    decimal_quantization: bool = ...,
    group_separator: bool = ...,
): ...
def format_compact_decimal(
    number: float, *, format_type: Literal["short", "long"] = ..., locale: Locale | str | None = ..., fraction_digits: int = ...
) -> str: ...

class UnknownCurrencyFormatError(KeyError): ...

def format_currency(
    number: float | decimal.Decimal | str,
    currency: str,
    format: str | None = ...,
    locale: Locale | str | None = ...,
    currency_digits: bool = ...,
    format_type: Literal["name", "standard", "accounting"] = ...,
    decimal_quantization: bool = ...,
    group_separator: bool = ...,
) -> str: ...
def format_percent(
    number: float | decimal.Decimal | str,
    format: str | None = ...,
    locale: Locale | str | None = ...,
    decimal_quantization: bool = ...,
    group_separator: bool = ...,
) -> str: ...
def format_scientific(
    number: float | decimal.Decimal | str,
    format: str | None = ...,
    locale: Locale | str | None = ...,
    decimal_quantization: bool = ...,
) -> str: ...

class NumberFormatError(ValueError):
    suggestions: str | None
    def __init__(self, message: str, suggestions: str | None = ...) -> None: ...

def parse_number(string: str, locale: Locale | str | None = ...) -> int: ...
def parse_decimal(string: str, locale: Locale | str | None = ..., strict: bool = ...) -> decimal.Decimal: ...

PREFIX_END: str
NUMBER_TOKEN: str
PREFIX_PATTERN: str
NUMBER_PATTERN: str
SUFFIX_PATTERN: str
number_re: Pattern[str]

def parse_grouping(p: str) -> tuple[int, int]: ...
def parse_pattern(pattern: NumberPattern | str) -> NumberPattern: ...

class NumberPattern:
    pattern: str
    prefix: tuple[str, str]
    suffix: tuple[str, str]
    grouping: tuple[int, int]
    int_prec: tuple[int, int]
    frac_prec: tuple[int, int]
    exp_prec: tuple[int, int] | None
    exp_plus: bool | None
    scale: Literal[0, 2, 3]
    def __init__(
        self,
        pattern: str,
        prefix: tuple[str, str],
        suffix: tuple[str, str],
        grouping: tuple[int, int],
        int_prec: tuple[int, int],
        frac_prec: tuple[int, int],
        exp_prec: tuple[int, int] | None,
        exp_plus: bool | None,
    ) -> None: ...
    def compute_scale(self) -> Literal[0, 2, 3]: ...
    def scientific_notation_elements(
        self, value: decimal.Decimal, locale: Locale | str | None
    ) -> tuple[decimal.Decimal, int, str]: ...
    def apply(
        self,
        value: float | decimal.Decimal,
        locale: Locale | str | None,
        currency: str | None = ...,
        currency_digits: bool = ...,
        decimal_quantization: bool = ...,
        force_frac: int | None = ...,
        group_separator: bool = ...,
    ) -> str: ...
