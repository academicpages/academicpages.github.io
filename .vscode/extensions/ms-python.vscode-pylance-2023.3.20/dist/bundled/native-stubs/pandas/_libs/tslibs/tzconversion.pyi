# Python: 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)]
# Library: pandas, version: 1.2.4
# Module: pandas._libs.tslibs.tzconversion, version: unspecified
import typing
import builtins as _mod_builtins
import dateutil.tz.tz as _mod_dateutil_tz_tz

__doc__: str
__file__: str
__name__: str
__package__: str
__pyx_capi__: dict
def __pyx_unpickle_Enum() -> typing.Any:
    ...

__test__: dict
def tz_convert_from_utc() -> typing.Any:
    '\n    Convert the values (in i8) from UTC to tz\n\n    Parameters\n    ----------\n    vals : int64 ndarray\n    tz : tzinfo\n\n    Returns\n    -------\n    int64 ndarray of converted\n    '
    ...

def tz_convert_from_utc_single() -> typing.Any:
    '\n    Convert the val (in i8) from UTC to tz\n\n    This is a single value version of tz_convert_from_utc.\n\n    Parameters\n    ----------\n    val : int64\n    tz : tzinfo\n\n    Returns\n    -------\n    converted: int64\n    '
    ...

def tz_localize_to_utc() -> typing.Any:
    '\n    Localize tzinfo-naive i8 to given time zone (using pytz). If\n    there are ambiguities in the values, raise AmbiguousTimeError.\n\n    Parameters\n    ----------\n    vals : ndarray[int64_t]\n    tz : tzinfo or None\n    ambiguous : str, bool, or arraylike\n        When clocks moved backward due to DST, ambiguous times may arise.\n        For example in Central European Time (UTC+01), when going from 03:00\n        DST to 02:00 non-DST, 02:30:00 local time occurs both at 00:30:00 UTC\n        and at 01:30:00 UTC. In such a situation, the `ambiguous` parameter\n        dictates how ambiguous times should be handled.\n\n        - \'infer\' will attempt to infer fall dst-transition hours based on\n          order\n        - bool-ndarray where True signifies a DST time, False signifies a\n          non-DST time (note that this flag is only applicable for ambiguous\n          times, but the array must have the same length as vals)\n        - bool if True, treat all vals as DST. If False, treat them as non-DST\n        - \'NaT\' will return NaT where there are ambiguous times\n\n    nonexistent : {None, "NaT", "shift_forward", "shift_backward", "raise", timedelta-like}\n        How to handle non-existent times when converting wall times to UTC\n\n        .. versionadded:: 0.24.0\n\n    Returns\n    -------\n    localized : ndarray[int64_t]\n    '
    ...

tzutc = _mod_dateutil_tz_tz.tzutc
def __getattr__(name) -> typing.Any:
    ...

