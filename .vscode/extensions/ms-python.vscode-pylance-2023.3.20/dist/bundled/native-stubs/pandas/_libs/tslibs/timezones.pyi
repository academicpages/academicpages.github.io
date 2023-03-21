# Python: 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)]
# Library: pandas, version: 1.2.4
# Module: pandas._libs.tslibs.timezones, version: unspecified
import typing
import builtins as _mod_builtins
import datetime as _mod_datetime
import dateutil.tz.tz as _mod_dateutil_tz_tz
import pytz as _mod_pytz
import pytz.tzinfo as _mod_pytz_tzinfo

UTC: _mod_pytz.UTC
__doc__: typing.Any
__file__: str
__name__: str
__package__: str
__pyx_capi__: dict
def __pyx_unpickle_Enum() -> typing.Any:
    ...

__test__: dict
_dateutil_tzfile = _mod_dateutil_tz_tz.tzfile
_dateutil_tzlocal = _mod_dateutil_tz_tz.tzlocal
_dateutil_tzutc = _mod_dateutil_tz_tz.tzutc
def _p_tz_cache_key() -> typing.Any:
    '\n    Python interface for cache function to facilitate testing.\n    '
    ...

_pytz_BaseTzInfo = _mod_pytz_tzinfo.BaseTzInfo
def dateutil_gettz(self, name) -> typing.Any:
    '\n        Retrieve a time zone object from a string representation\n\n        This function is intended to retrieve the :py:class:`tzinfo` subclass\n        that best represents the time zone that would be used if a POSIX\n        `TZ variable`_ were set to the same value.\n\n        If no argument or an empty string is passed to ``gettz``, local time\n        is returned:\n\n        .. code-block:: python3\n\n            >>> gettz()\n            tzfile(\'/etc/localtime\')\n\n        This function is also the preferred way to map IANA tz database keys\n        to :class:`tzfile` objects:\n\n        .. code-block:: python3\n\n            >>> gettz(\'Pacific/Kiritimati\')\n            tzfile(\'/usr/share/zoneinfo/Pacific/Kiritimati\')\n\n        On Windows, the standard is extended to include the Windows-specific\n        zone names provided by the operating system:\n\n        .. code-block:: python3\n\n            >>> gettz(\'Egypt Standard Time\')\n            tzwin(\'Egypt Standard Time\')\n\n        Passing a GNU ``TZ`` style string time zone specification returns a\n        :class:`tzstr` object:\n\n        .. code-block:: python3\n\n            >>> gettz(\'AEST-10AEDT-11,M10.1.0/2,M4.1.0/3\')\n            tzstr(\'AEST-10AEDT-11,M10.1.0/2,M4.1.0/3\')\n\n        :param name:\n            A time zone name (IANA, or, on Windows, Windows keys), location of\n            a ``tzfile(5)`` zoneinfo file or ``TZ`` variable style time zone\n            specifier. An empty string, no argument or ``None`` is interpreted\n            as local time.\n\n        :return:\n            Returns an instance of one of ``dateutil``\'s :py:class:`tzinfo`\n            subclasses.\n\n        .. versionchanged:: 2.7.0\n\n            After version 2.7.0, any two calls to ``gettz`` using the same\n            input strings will return the same object:\n\n            .. code-block:: python3\n\n                >>> tz.gettz(\'America/Chicago\') is tz.gettz(\'America/Chicago\')\n                True\n\n            In addition to improving performance, this ensures that\n            `"same zone" semantics`_ are used for datetimes in the same zone.\n\n\n        .. _`TZ variable`:\n            https://www.gnu.org/software/libc/manual/html_node/TZ-Variable.html\n\n        .. _`"same zone" semantics`:\n            https://blog.ganssle.io/articles/2018/02/aware-datetime-arithmetic.html\n        '
    ...

dst_cache: dict
def get_timezone() -> typing.Any:
    "\n    We need to do several things here:\n    1) Distinguish between pytz and dateutil timezones\n    2) Not be over-specific (e.g. US/Eastern with/without DST is same *zone*\n       but a different tz object)\n    3) Provide something to serialize when we're storing a datetime object\n       in pytables.\n\n    We return a string prefaced with dateutil if it's a dateutil tz, else just\n    the tz name. It needs to be a string so that we can serialize it with\n    UJSON/pytables. maybe_get_tz (below) is the inverse of this process.\n    "
    ...

def infer_tzinfo() -> typing.Any:
    ...

def is_utc() -> typing.Any:
    ...

def maybe_get_tz() -> typing.Any:
    '\n    (Maybe) Construct a timezone object from a string. If tz is a string, use\n    it to construct a timezone object. Otherwise, just return tz.\n    '
    ...

timezone = _mod_datetime.timezone
def tz_compare() -> typing.Any:
    "\n    Compare string representations of timezones\n\n    The same timezone can be represented as different instances of\n    timezones. For example\n    `<DstTzInfo 'Europe/Paris' LMT+0:09:00 STD>` and\n    `<DstTzInfo 'Europe/Paris' CET+1:00:00 STD>` are essentially same\n    timezones but aren't evaluated such, but the string representation\n    for both of these is `'Europe/Paris'`.\n\n    This exists only to add a notion of equality to pytz-style zones\n    that is compatible with the notion of equality expected of tzinfo\n    subclasses.\n\n    Parameters\n    ----------\n    start : tzinfo\n    end : tzinfo\n\n    Returns:\n    -------\n    bool\n    "
    ...

def tz_standardize() -> typing.Any:
    '\n    If the passed tz is a pytz timezone object, "normalize" it to the a\n    consistent version\n\n    Parameters\n    ----------\n    tz : tz object\n\n    Returns:\n    -------\n    tz object\n\n    Examples:\n    --------\n    >>> tz\n    <DstTzInfo \'US/Pacific\' PST-1 day, 16:00:00 STD>\n\n    >>> tz_standardize(tz)\n    <DstTzInfo \'US/Pacific\' LMT-1 day, 16:07:00 STD>\n\n    >>> tz\n    <DstTzInfo \'US/Pacific\' LMT-1 day, 16:07:00 STD>\n\n    >>> tz_standardize(tz)\n    <DstTzInfo \'US/Pacific\' LMT-1 day, 16:07:00 STD>\n\n    >>> tz\n    dateutil.tz.tz.tzutc\n\n    >>> tz_standardize(tz)\n    dateutil.tz.tz.tzutc\n    '
    ...

def __getattr__(name) -> typing.Any:
    ...

