# Python: 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)]
# Library: pandas, version: 1.2.4
# Module: pandas._libs.tslibs.vectorized, version: unspecified
import typing
import builtins as _mod_builtins
import pandas._libs.tslibs.dtypes as _mod_pandas__libs_tslibs_dtypes

Resolution = _mod_pandas__libs_tslibs_dtypes.Resolution
__doc__: typing.Any
__file__: str
__name__: str
__package__: str
def __pyx_unpickle_Enum() -> typing.Any:
    ...

__test__: dict
def dt64arr_to_periodarr() -> typing.Any:
    ...

def get_resolution() -> typing.Any:
    ...

def ints_to_pydatetime() -> typing.Any:
    "\n    Convert an i8 repr to an ndarray of datetimes, date, time or Timestamp.\n\n    Parameters\n    ----------\n    arr : array of i8\n    tz : str, optional\n         convert to this timezone\n    freq : str/Offset, optional\n         freq to convert\n    fold : bint, default is 0\n        Due to daylight saving time, one wall clock time can occur twice\n        when shifting from summer to winter time; fold describes whether the\n        datetime-like corresponds  to the first (0) or the second time (1)\n        the wall clock hits the ambiguous time\n\n        .. versionadded:: 1.1.0\n    box : {'datetime', 'timestamp', 'date', 'time'}, default 'datetime'\n        * If datetime, convert to datetime.datetime\n        * If date, convert to datetime.date\n        * If time, convert to datetime.time\n        * If Timestamp, convert to pandas.Timestamp\n\n    Returns\n    -------\n    ndarray of dtype specified by box\n    "
    ...

def is_date_array_normalized() -> typing.Any:
    '\n    Check if all of the given (nanosecond) timestamps are normalized to\n    midnight, i.e. hour == minute == second == 0.  If the optional timezone\n    `tz` is not None, then this is midnight for this timezone.\n\n    Parameters\n    ----------\n    stamps : int64 ndarray\n    tz : tzinfo or None\n\n    Returns\n    -------\n    is_normalized : bool True if all stamps are normalized\n    '
    ...

def normalize_i8_timestamps() -> typing.Any:
    '\n    Normalize each of the (nanosecond) timezone aware timestamps in the given\n    array by rounding down to the beginning of the day (i.e. midnight).\n    This is midnight for timezone, `tz`.\n\n    Parameters\n    ----------\n    stamps : int64 ndarray\n    tz : tzinfo or None\n\n    Returns\n    -------\n    result : int64 ndarray of converted of normalized nanosecond timestamps\n    '
    ...

def __getattr__(name) -> typing.Any:
    ...

