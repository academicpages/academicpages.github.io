# Python: 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)]
# Library: pandas, version: 1.2.4
# Module: pandas._libs.tslibs.fields, version: unspecified
import typing
import builtins as _mod_builtins
import pandas._libs.tslibs.strptime as _mod_pandas__libs_tslibs_strptime

DAYS_FULL: list
LC_TIME: int
LocaleTime = _mod_pandas__libs_tslibs_strptime.LocaleTime
MONTHS_FULL: list
__doc__: str
__file__: str
__name__: str
__package__: str
def __pyx_unpickle_Enum() -> typing.Any:
    ...

__test__: dict
def build_field_sarray() -> typing.Any:
    '\n    Datetime as int64 representation to a structured array of fields\n    '
    ...

def build_isocalendar_sarray() -> typing.Any:
    '\n    Given a int64-based datetime array, return the ISO 8601 year, week, and day\n    as a structured array.\n    '
    ...

def get_date_field() -> typing.Any:
    '\n    Given a int64-based datetime index, extract the year, month, etc.,\n    field and return an array of these values.\n    '
    ...

def get_date_name_field() -> typing.Any:
    '\n    Given a int64-based datetime index, return array of strings of date\n    name based on requested field (e.g. day_name)\n    '
    ...

def get_locale_names() -> typing.Any:
    '\n    Returns an array of localized day or month names.\n\n    Parameters\n    ----------\n    name_type : string, attribute of LocaleTime() in which to return localized\n        names\n    locale : string\n\n    Returns\n    -------\n    list of locale names\n    '
    ...

def get_start_end_field() -> typing.Any:
    '\n    Given an int64-based datetime index return array of indicators\n    of whether timestamps are at the start/end of the month/quarter/year\n    (defined by frequency).\n    '
    ...

def get_timedelta_field() -> typing.Any:
    '\n    Given a int64-based timedelta index, extract the days, hrs, sec.,\n    field and return an array of these values.\n    '
    ...

def isleapyear_arr() -> typing.Any:
    'vectorized version of isleapyear; NaT evaluates as False'
    ...

def month_position_check() -> typing.Any:
    ...

def set_locale(*args, **kwds) -> typing.Any:
    '\n    Context manager for temporarily setting a locale.\n\n    Parameters\n    ----------\n    new_locale : str or tuple\n        A string of the form <language_country>.<encoding>. For example to set\n        the current locale to US English with a UTF8 encoding, you would pass\n        "en_US.UTF-8".\n    lc_var : int, default `locale.LC_ALL`\n        The category of the locale being set.\n\n    Notes\n    -----\n    This is useful when you want to run a particular block of code under a\n    particular locale, without globally setting the locale. This probably isn\'t\n    thread-safe.\n    '
    ...

def __getattr__(name) -> typing.Any:
    ...

