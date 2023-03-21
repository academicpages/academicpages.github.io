# Python: 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)]
# Library: pandas, version: 1.2.4
# Module: pandas._libs.tslibs.ccalendar, version: unspecified
import typing
import builtins as _mod_builtins

DAYS: list
DAYS_FULL: list
DAY_SECONDS: int
HOUR_SECONDS: int
MONTHS: list
MONTHS_FULL: list
MONTH_ALIASES: dict
MONTH_NUMBERS: dict
MONTH_TO_CAL_NUM: dict
__doc__: str
__file__: str
__name__: str
__package__: str
__pyx_capi__: dict
__test__: dict
def get_day_of_year() -> typing.Any:
    '\n    Return the ordinal day-of-year for the given day.\n\n    Parameters\n    ----------\n    year : int\n    month : int\n    day : int\n\n    Returns\n    -------\n    day_of_year : int32_t\n\n    Notes\n    -----\n    Assumes the inputs describe a valid date.\n    '
    ...

def get_days_in_month() -> typing.Any:
    '\n    Return the number of days in the given month of the given year.\n\n    Parameters\n    ----------\n    year : int\n    month : int\n\n    Returns\n    -------\n    days_in_month : int\n\n    Notes\n    -----\n    Assumes that the arguments are valid.  Passing a month not between 1 and 12\n    risks a segfault.\n    '
    ...

def get_firstbday() -> typing.Any:
    '\n    Find the first day of the month that is a business day.\n\n    Parameters\n    ----------\n    year : int\n    month : int\n\n    Returns\n    -------\n    first_bday : int\n    '
    ...

def get_iso_calendar() -> typing.Any:
    '\n    Return the year, week, and day of year corresponding to ISO 8601\n\n    Parameters\n    ----------\n    year : int\n    month : int\n    day : int\n\n    Returns\n    -------\n    year : int32_t\n    week : int32_t\n    day : int32_t\n\n    Notes\n    -----\n    Assumes the inputs describe a valid date.\n    '
    ...

def get_lastbday() -> typing.Any:
    '\n    Find the last day of the month that is a business day.\n\n    Parameters\n    ----------\n    year : int\n    month : int\n\n    Returns\n    -------\n    last_bday : int\n    '
    ...

def get_week_of_year() -> typing.Any:
    '\n    Return the ordinal week-of-year for the given day.\n\n    Parameters\n    ----------\n    year : int\n    month : int\n    day : int\n\n    Returns\n    -------\n    week_of_year : int32_t\n\n    Notes\n    -----\n    Assumes the inputs describe a valid date.\n    '
    ...

int_to_weekday: dict
weekday_to_int: dict
def __getattr__(name) -> typing.Any:
    ...

