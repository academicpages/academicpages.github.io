from collections.abc import Iterable
from typing_extensions import Literal

from babel.core import Locale

DEFAULT_LOCALE: str | None

def format_list(
    lst: Iterable[str],
    style: Literal["standard", "standard-short", "or", "or-short", "unit", "unit-short", "unit-narrow"] = ...,
    locale: Locale | str | None = ...,
) -> str: ...
