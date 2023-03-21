from datetime import date
from datetime import datetime as datetime
from typing import Any, Callable, Dict, Optional, SupportsInt, Tuple, Type, Union

from django import template

register: template.Library

def ordinal(value: Optional[Union[str, SupportsInt]]) -> Optional[str]: ...
def intcomma(value: Optional[Union[str, SupportsInt]], use_l10n: bool = ...) -> str: ...

intword_converters: Tuple[Tuple[int, Callable[..., Any]]]

def intword(value: Optional[Union[str, SupportsInt]]) -> Optional[Union[int, str]]: ...
def apnumber(value: Optional[Union[str, SupportsInt]]) -> Optional[Union[int, str]]: ...
def naturalday(value: Optional[Union[date, str]], arg: None = ...) -> Optional[str]: ...
def naturaltime(value: datetime) -> str: ...

class NaturalTimeFormatter:
    time_strings: Dict[str, str]
    past_substrings: Dict[str, str]
    future_substrings: Dict[str, str]
    @classmethod
    def string_for(cls: Type[NaturalTimeFormatter], value: Any) -> Any: ...
