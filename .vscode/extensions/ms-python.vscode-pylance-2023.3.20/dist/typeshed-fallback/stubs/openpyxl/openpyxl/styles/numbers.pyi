from _typeshed import Incomplete

from openpyxl.descriptors import String
from openpyxl.descriptors.serialisable import Serialisable

BUILTIN_FORMATS: Incomplete
BUILTIN_FORMATS_MAX_SIZE: int
BUILTIN_FORMATS_REVERSE: Incomplete
FORMAT_GENERAL: Incomplete
FORMAT_TEXT: Incomplete
FORMAT_NUMBER: Incomplete
FORMAT_NUMBER_00: Incomplete
FORMAT_NUMBER_COMMA_SEPARATED1: Incomplete
FORMAT_NUMBER_COMMA_SEPARATED2: str
FORMAT_PERCENTAGE: Incomplete
FORMAT_PERCENTAGE_00: Incomplete
FORMAT_DATE_YYYYMMDD2: str
FORMAT_DATE_YYMMDD: str
FORMAT_DATE_DDMMYY: str
FORMAT_DATE_DMYSLASH: str
FORMAT_DATE_DMYMINUS: str
FORMAT_DATE_DMMINUS: str
FORMAT_DATE_MYMINUS: str
FORMAT_DATE_XLSX14: Incomplete
FORMAT_DATE_XLSX15: Incomplete
FORMAT_DATE_XLSX16: Incomplete
FORMAT_DATE_XLSX17: Incomplete
FORMAT_DATE_XLSX22: Incomplete
FORMAT_DATE_DATETIME: str
FORMAT_DATE_TIME1: Incomplete
FORMAT_DATE_TIME2: Incomplete
FORMAT_DATE_TIME3: Incomplete
FORMAT_DATE_TIME4: Incomplete
FORMAT_DATE_TIME5: Incomplete
FORMAT_DATE_TIME6: Incomplete
FORMAT_DATE_TIME7: str
FORMAT_DATE_TIME8: str
FORMAT_DATE_TIMEDELTA: str
FORMAT_DATE_YYMMDDSLASH: str
FORMAT_CURRENCY_USD_SIMPLE: str
FORMAT_CURRENCY_USD: str
FORMAT_CURRENCY_EUR_SIMPLE: str
COLORS: str
LITERAL_GROUP: str
LOCALE_GROUP: str
STRIP_RE: Incomplete
TIMEDELTA_RE: Incomplete

def is_date_format(fmt): ...
def is_timedelta_format(fmt): ...
def is_datetime(fmt): ...
def is_builtin(fmt): ...
def builtin_format_code(index): ...
def builtin_format_id(fmt): ...

class NumberFormatDescriptor(String):
    def __set__(self, instance, value) -> None: ...

class NumberFormat(Serialisable):  # type: ignore[misc]
    numFmtId: Incomplete
    formatCode: Incomplete
    def __init__(self, numFmtId: Incomplete | None = ..., formatCode: Incomplete | None = ...) -> None: ...

class NumberFormatList(Serialisable):  # type: ignore[misc]
    # Overwritten by property below
    # count: Integer
    numFmt: Incomplete
    __elements__: Incomplete
    __attrs__: Incomplete
    def __init__(self, count: Incomplete | None = ..., numFmt=...) -> None: ...
    @property
    def count(self): ...
    def __getitem__(self, idx): ...
