# Python: 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)]
# Library: pandas, version: 1.2.4
# Module: pandas._libs.tslibs.timestamps, version: unspecified
import typing
import builtins as _mod_builtins
import datetime as _mod_datetime
import pandas._libs.tslibs.base as _mod_pandas__libs_tslibs_base
import pandas._libs.tslibs.np_datetime as _mod_pandas__libs_tslibs_np_datetime
import pandas._libs.tslibs.timedeltas as _mod_pandas__libs_tslibs_timedeltas

OutOfBoundsDatetime = _mod_pandas__libs_tslibs_np_datetime.OutOfBoundsDatetime
class RoundTo(_mod_builtins.object):
    '\n    enumeration defining the available rounding modes\n\n    Attributes\n    ----------\n    MINUS_INFTY\n        round towards -∞, or floor [2]_\n    PLUS_INFTY\n        round towards +∞, or ceil [3]_\n    NEAREST_HALF_EVEN\n        round to nearest, tie-break half to even [6]_\n    NEAREST_HALF_MINUS_INFTY\n        round to nearest, tie-break half to -∞ [5]_\n    NEAREST_HALF_PLUS_INFTY\n        round to nearest, tie-break half to +∞ [4]_\n\n\n    References\n    ----------\n    .. [1] "Rounding - Wikipedia"\n           https://en.wikipedia.org/wiki/Rounding\n    .. [2] "Rounding down"\n           https://en.wikipedia.org/wiki/Rounding#Rounding_down\n    .. [3] "Rounding up"\n           https://en.wikipedia.org/wiki/Rounding#Rounding_up\n    .. [4] "Round half up"\n           https://en.wikipedia.org/wiki/Rounding#Round_half_up\n    .. [5] "Round half down"\n           https://en.wikipedia.org/wiki/Rounding#Round_half_down\n    .. [6] "Round half to even"\n           https://en.wikipedia.org/wiki/Rounding#Round_half_to_even\n    '
    MINUS_INFTY: property
    NEAREST_HALF_EVEN: property
    NEAREST_HALF_MINUS_INFTY: property
    NEAREST_HALF_PLUS_INFTY: property
    PLUS_INFTY: property
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, *args, **kwargs) -> None:
        '\n    enumeration defining the available rounding modes\n\n    Attributes\n    ----------\n    MINUS_INFTY\n        round towards -∞, or floor [2]_\n    PLUS_INFTY\n        round towards +∞, or ceil [3]_\n    NEAREST_HALF_EVEN\n        round to nearest, tie-break half to even [6]_\n    NEAREST_HALF_MINUS_INFTY\n        round to nearest, tie-break half to -∞ [5]_\n    NEAREST_HALF_PLUS_INFTY\n        round to nearest, tie-break half to +∞ [4]_\n\n\n    References\n    ----------\n    .. [1] "Rounding - Wikipedia"\n           https://en.wikipedia.org/wiki/Rounding\n    .. [2] "Rounding down"\n           https://en.wikipedia.org/wiki/Rounding#Rounding_down\n    .. [3] "Rounding up"\n           https://en.wikipedia.org/wiki/Rounding#Rounding_up\n    .. [4] "Round half up"\n           https://en.wikipedia.org/wiki/Rounding#Round_half_up\n    .. [5] "Round half down"\n           https://en.wikipedia.org/wiki/Rounding#Round_half_down\n    .. [6] "Round half to even"\n           https://en.wikipedia.org/wiki/Rounding#Round_half_to_even\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __module__: str
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @property
    def __weakref__(self) -> typing.Any:
        'list of weak references to the object (if defined)'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

Timedelta = _mod_pandas__libs_tslibs_timedeltas.Timedelta
class Timestamp(_Timestamp):
    "\n    Pandas replacement for python datetime.datetime object.\n\n    Timestamp is the pandas equivalent of python's Datetime\n    and is interchangeable with it in most cases. It's the type used\n    for the entries that make up a DatetimeIndex, and other timeseries\n    oriented data structures in pandas.\n\n    Parameters\n    ----------\n    ts_input : datetime-like, str, int, float\n        Value to be converted to Timestamp.\n    freq : str, DateOffset\n        Offset which Timestamp will have.\n    tz : str, pytz.timezone, dateutil.tz.tzfile or None\n        Time zone for time which Timestamp will have.\n    unit : str\n        Unit used for conversion if ts_input is of type int or float. The\n        valid values are 'D', 'h', 'm', 's', 'ms', 'us', and 'ns'. For\n        example, 's' means seconds and 'ms' means milliseconds.\n    year, month, day : int\n    hour, minute, second, microsecond : int, optional, default 0\n    nanosecond : int, optional, default 0\n    tzinfo : datetime.tzinfo, optional, default None\n    fold : {0, 1}, default None, keyword-only\n        Due to daylight saving time, one wall clock time can occur twice\n        when shifting from summer to winter time; fold describes whether the\n        datetime-like corresponds  to the first (0) or the second time (1)\n        the wall clock hits the ambiguous time\n\n        .. versionadded:: 1.1.0\n\n    Notes\n    -----\n    There are essentially three calling conventions for the constructor. The\n    primary form accepts four parameters. They can be passed by position or\n    keyword.\n\n    The other two forms mimic the parameters from ``datetime.datetime``. They\n    can be passed by either position or keyword, but not both mixed together.\n\n    Examples\n    --------\n    Using the primary calling convention:\n\n    This converts a datetime-like string\n\n    >>> pd.Timestamp('2017-01-01T12')\n    Timestamp('2017-01-01 12:00:00')\n\n    This converts a float representing a Unix epoch in units of seconds\n\n    >>> pd.Timestamp(1513393355.5, unit='s')\n    Timestamp('2017-12-16 03:02:35.500000')\n\n    This converts an int representing a Unix-epoch in units of seconds\n    and for a particular timezone\n\n    >>> pd.Timestamp(1513393355, unit='s', tz='US/Pacific')\n    Timestamp('2017-12-15 19:02:35-0800', tz='US/Pacific')\n\n    Using the other two forms that mimic the API for ``datetime.datetime``:\n\n    >>> pd.Timestamp(2017, 1, 1, 12)\n    Timestamp('2017-01-01 12:00:00')\n\n    >>> pd.Timestamp(year=2017, month=1, day=1, hour=12)\n    Timestamp('2017-01-01 12:00:00')\n    "
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, *args, **kwargs) -> None:
        "\n    Pandas replacement for python datetime.datetime object.\n\n    Timestamp is the pandas equivalent of python's Datetime\n    and is interchangeable with it in most cases. It's the type used\n    for the entries that make up a DatetimeIndex, and other timeseries\n    oriented data structures in pandas.\n\n    Parameters\n    ----------\n    ts_input : datetime-like, str, int, float\n        Value to be converted to Timestamp.\n    freq : str, DateOffset\n        Offset which Timestamp will have.\n    tz : str, pytz.timezone, dateutil.tz.tzfile or None\n        Time zone for time which Timestamp will have.\n    unit : str\n        Unit used for conversion if ts_input is of type int or float. The\n        valid values are 'D', 'h', 'm', 's', 'ms', 'us', and 'ns'. For\n        example, 's' means seconds and 'ms' means milliseconds.\n    year, month, day : int\n    hour, minute, second, microsecond : int, optional, default 0\n    nanosecond : int, optional, default 0\n    tzinfo : datetime.tzinfo, optional, default None\n    fold : {0, 1}, default None, keyword-only\n        Due to daylight saving time, one wall clock time can occur twice\n        when shifting from summer to winter time; fold describes whether the\n        datetime-like corresponds  to the first (0) or the second time (1)\n        the wall clock hits the ambiguous time\n\n        .. versionadded:: 1.1.0\n\n    Notes\n    -----\n    There are essentially three calling conventions for the constructor. The\n    primary form accepts four parameters. They can be passed by position or\n    keyword.\n\n    The other two forms mimic the parameters from ``datetime.datetime``. They\n    can be passed by either position or keyword, but not both mixed together.\n\n    Examples\n    --------\n    Using the primary calling convention:\n\n    This converts a datetime-like string\n\n    >>> pd.Timestamp('2017-01-01T12')\n    Timestamp('2017-01-01 12:00:00')\n\n    This converts a float representing a Unix epoch in units of seconds\n\n    >>> pd.Timestamp(1513393355.5, unit='s')\n    Timestamp('2017-12-16 03:02:35.500000')\n\n    This converts an int representing a Unix-epoch in units of seconds\n    and for a particular timezone\n\n    >>> pd.Timestamp(1513393355, unit='s', tz='US/Pacific')\n    Timestamp('2017-12-15 19:02:35-0800', tz='US/Pacific')\n\n    Using the other two forms that mimic the API for ``datetime.datetime``:\n\n    >>> pd.Timestamp(2017, 1, 1, 12)\n    Timestamp('2017-01-01 12:00:00')\n\n    >>> pd.Timestamp(year=2017, month=1, day=1, hour=12)\n    Timestamp('2017-01-01 12:00:00')\n    "
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @property
    def __weakref__(self) -> typing.Any:
        'list of weak references to the object (if defined)'
        ...
    
    def _round(self, freq, mode, ambiguous, nonexistent) -> typing.Any:
        ...
    
    def astimezone(self, tz) -> typing.Any:
        '\n        Convert tz-aware Timestamp to another time zone.\n\n        Parameters\n        ----------\n        tz : str, pytz.timezone, dateutil.tz.tzfile or None\n            Time zone for time which Timestamp will be converted to.\n            None will remove timezone holding UTC time.\n\n        Returns\n        -------\n        converted : Timestamp\n\n        Raises\n        ------\n        TypeError\n            If Timestamp is tz-naive.\n        '
        ...
    
    def ceil(self, freq, ambiguous, nonexistent) -> typing.Any:
        "\n        Return a new Timestamp ceiled to this resolution.\n\n        Parameters\n        ----------\n        freq : str\n            Frequency string indicating the ceiling resolution.\n        ambiguous : bool or {'raise', 'NaT'}, default 'raise'\n            The behavior is as follows:\n\n            * bool contains flags to determine if time is dst or not (note\n              that this flag is only applicable for ambiguous fall dst dates).\n            * 'NaT' will return NaT for an ambiguous time.\n            * 'raise' will raise an AmbiguousTimeError for an ambiguous time.\n\n            .. versionadded:: 0.24.0\n        nonexistent : {'raise', 'shift_forward', 'shift_backward, 'NaT', timedelta}, default 'raise'\n            A nonexistent time does not exist in a particular timezone\n            where clocks moved forward due to DST.\n\n            * 'shift_forward' will shift the nonexistent time forward to the\n              closest existing time.\n            * 'shift_backward' will shift the nonexistent time backward to the\n              closest existing time.\n            * 'NaT' will return NaT where there are nonexistent times.\n            * timedelta objects will shift nonexistent times by the timedelta.\n            * 'raise' will raise an NonExistentTimeError if there are\n              nonexistent times.\n\n            .. versionadded:: 0.24.0\n\n        Raises\n        ------\n        ValueError if the freq cannot be converted.\n        "
        ...
    
    def combine(self, cls, date, time) -> typing.Any:
        '\n        Timestamp.combine(date, time)\n\n        Combine date, time into datetime with same date and time fields.\n        '
        ...
    
    @property
    def daysinmonth(self) -> typing.Any:
        '\n        Return the number of days in the month.\n        '
        ...
    
    def floor(self, freq, ambiguous, nonexistent) -> typing.Any:
        "\n        Return a new Timestamp floored to this resolution.\n\n        Parameters\n        ----------\n        freq : str\n            Frequency string indicating the flooring resolution.\n        ambiguous : bool or {'raise', 'NaT'}, default 'raise'\n            The behavior is as follows:\n\n            * bool contains flags to determine if time is dst or not (note\n              that this flag is only applicable for ambiguous fall dst dates).\n            * 'NaT' will return NaT for an ambiguous time.\n            * 'raise' will raise an AmbiguousTimeError for an ambiguous time.\n\n            .. versionadded:: 0.24.0\n        nonexistent : {'raise', 'shift_forward', 'shift_backward, 'NaT', timedelta}, default 'raise'\n            A nonexistent time does not exist in a particular timezone\n            where clocks moved forward due to DST.\n\n            * 'shift_forward' will shift the nonexistent time forward to the\n              closest existing time.\n            * 'shift_backward' will shift the nonexistent time backward to the\n              closest existing time.\n            * 'NaT' will return NaT where there are nonexistent times.\n            * timedelta objects will shift nonexistent times by the timedelta.\n            * 'raise' will raise an NonExistentTimeError if there are\n              nonexistent times.\n\n            .. versionadded:: 0.24.0\n\n        Raises\n        ------\n        ValueError if the freq cannot be converted.\n        "
        ...
    
    freqstr: property
    @classmethod
    def fromisocalendar(cls) -> typing.Any:
        'int, int, int -> Construct a date from the ISO year, week number and weekday.\n\nThis is the inverse of the date.isocalendar() function'
        ...
    
    @classmethod
    def fromisoformat(cls) -> typing.Any:
        'string -> datetime from datetime.isoformat() output'
        ...
    
    def fromordinal(self, cls, ordinal, freq, tz) -> typing.Any:
        '\n        Timestamp.fromordinal(ordinal, freq=None, tz=None)\n\n        Passed an ordinal, translate and convert to a ts.\n        Note: by definition there cannot be any tz info on the ordinal itself.\n\n        Parameters\n        ----------\n        ordinal : int\n            Date corresponding to a proleptic Gregorian ordinal.\n        freq : str, DateOffset\n            Offset to apply to the Timestamp.\n        tz : str, pytz.timezone, dateutil.tz.tzfile or None\n            Time zone for the Timestamp.\n        '
        ...
    
    def fromtimestamp(self, cls, ts) -> typing.Any:
        "\n        Timestamp.fromtimestamp(ts)\n\n        Transform timestamp[, tz] to tz's local time from POSIX timestamp.\n        "
        ...
    
    max: Timestamp
    min: Timestamp
    def now(self, cls, tz) -> typing.Any:
        '\n        Timestamp.now(tz=None)\n\n        Return new Timestamp object representing current time local to\n        tz.\n\n        Parameters\n        ----------\n        tz : str or timezone object, default None\n            Timezone to localize to.\n        '
        ...
    
    def replace(self, year, month, day, hour, minute, second, microsecond, nanosecond, tzinfo, fold) -> typing.Any:
        '\n        Implements datetime.replace, handles nanoseconds.\n\n        Parameters\n        ----------\n        year : int, optional\n        month : int, optional\n        day : int, optional\n        hour : int, optional\n        minute : int, optional\n        second : int, optional\n        microsecond : int, optional\n        nanosecond : int, optional\n        tzinfo : tz-convertible, optional\n        fold : int, optional\n\n        Returns\n        -------\n        Timestamp with fields replaced\n        '
        ...
    
    resolution: _mod_pandas__libs_tslibs_timedeltas.Timedelta
    def round(self, freq, ambiguous, nonexistent) -> typing.Any:
        "\n        Round the Timestamp to the specified resolution.\n\n        Parameters\n        ----------\n        freq : str\n            Frequency string indicating the rounding resolution.\n        ambiguous : bool or {'raise', 'NaT'}, default 'raise'\n            The behavior is as follows:\n\n            * bool contains flags to determine if time is dst or not (note\n              that this flag is only applicable for ambiguous fall dst dates).\n            * 'NaT' will return NaT for an ambiguous time.\n            * 'raise' will raise an AmbiguousTimeError for an ambiguous time.\n\n            .. versionadded:: 0.24.0\n        nonexistent : {'raise', 'shift_forward', 'shift_backward, 'NaT', timedelta}, default 'raise'\n            A nonexistent time does not exist in a particular timezone\n            where clocks moved forward due to DST.\n\n            * 'shift_forward' will shift the nonexistent time forward to the\n              closest existing time.\n            * 'shift_backward' will shift the nonexistent time backward to the\n              closest existing time.\n            * 'NaT' will return NaT where there are nonexistent times.\n            * timedelta objects will shift nonexistent times by the timedelta.\n            * 'raise' will raise an NonExistentTimeError if there are\n              nonexistent times.\n\n            .. versionadded:: 0.24.0\n\n        Returns\n        -------\n        a new Timestamp rounded to the given resolution of `freq`\n\n        Raises\n        ------\n        ValueError if the freq cannot be converted\n        "
        ...
    
    def strftime(self, format) -> typing.Any:
        '\n        Timestamp.strftime(format)\n\n        Return a string representing the given POSIX timestamp\n        controlled by an explicit format string.\n\n        Parameters\n        ----------\n        format : str\n            Format string to convert Timestamp to string.\n            See strftime documentation for more information on the format string:\n            https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior.\n        '
        ...
    
    def strptime(self, cls, date_string, format) -> typing.Any:
        '\n        Timestamp.strptime(string, format)\n\n        Function is not implemented. Use pd.to_datetime().\n        '
        ...
    
    def to_julian_date(self) -> numpy.float64:
        '\n        Convert TimeStamp to a Julian Date.\n        0 Julian date is noon January 1, 4713 BC.\n        '
        ...
    
    def today(self, cls, tz) -> typing.Any:
        '\n        Timestamp.today(cls, tz=None)\n\n        Return the current time in the local timezone.  This differs\n        from datetime.today() in that it can be localized to a\n        passed timezone.\n\n        Parameters\n        ----------\n        tz : str or timezone object, default None\n            Timezone to localize to.\n        '
        ...
    
    tz: property
    def tz_convert(self, tz) -> typing.Any:
        '\n        Convert tz-aware Timestamp to another time zone.\n\n        Parameters\n        ----------\n        tz : str, pytz.timezone, dateutil.tz.tzfile or None\n            Time zone for time which Timestamp will be converted to.\n            None will remove timezone holding UTC time.\n\n        Returns\n        -------\n        converted : Timestamp\n\n        Raises\n        ------\n        TypeError\n            If Timestamp is tz-naive.\n        '
        ...
    
    def tz_localize(self, tz, ambiguous, nonexistent) -> typing.Any:
        "\n        Convert naive Timestamp to local time zone, or remove\n        timezone from tz-aware Timestamp.\n\n        Parameters\n        ----------\n        tz : str, pytz.timezone, dateutil.tz.tzfile or None\n            Time zone for time which Timestamp will be converted to.\n            None will remove timezone holding local time.\n\n        ambiguous : bool, 'NaT', default 'raise'\n            When clocks moved backward due to DST, ambiguous times may arise.\n            For example in Central European Time (UTC+01), when going from\n            03:00 DST to 02:00 non-DST, 02:30:00 local time occurs both at\n            00:30:00 UTC and at 01:30:00 UTC. In such a situation, the\n            `ambiguous` parameter dictates how ambiguous times should be\n            handled.\n\n            The behavior is as follows:\n\n            * bool contains flags to determine if time is dst or not (note\n              that this flag is only applicable for ambiguous fall dst dates).\n            * 'NaT' will return NaT for an ambiguous time.\n            * 'raise' will raise an AmbiguousTimeError for an ambiguous time.\n\n        nonexistent : 'shift_forward', 'shift_backward, 'NaT', timedelta, default 'raise'\n            A nonexistent time does not exist in a particular timezone\n            where clocks moved forward due to DST.\n\n            The behavior is as follows:\n\n            * 'shift_forward' will shift the nonexistent time forward to the\n              closest existing time.\n            * 'shift_backward' will shift the nonexistent time backward to the\n              closest existing time.\n            * 'NaT' will return NaT where there are nonexistent times.\n            * timedelta objects will shift nonexistent times by the timedelta.\n            * 'raise' will raise an NonExistentTimeError if there are\n              nonexistent times.\n\n            .. versionadded:: 0.24.0\n\n        Returns\n        -------\n        localized : Timestamp\n\n        Raises\n        ------\n        TypeError\n            If the Timestamp is tz-aware and tz is not None.\n        "
        ...
    
    def utcfromtimestamp(self, cls, ts) -> typing.Any:
        '\n        Timestamp.utcfromtimestamp(ts)\n\n        Construct a naive UTC datetime from a POSIX timestamp.\n        '
        ...
    
    def utcnow(self, cls) -> typing.Any:
        '\n        Timestamp.utcnow()\n\n        Return a new Timestamp representing UTC day and time.\n        '
        ...
    
    @property
    def weekofyear(self) -> typing.Any:
        '\n        Return the week number of the year.\n        '
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class _Timestamp(_mod_pandas__libs_tslibs_base.ABCTimestamp):
    def __add__(self, value) -> _Timestamp:
        'Return self+value.'
        ...
    
    __array_priority__: int
    def __eq__(self, value) -> bool:
        'Return self==value.'
        ...
    
    def __ge__(self, value) -> bool:
        'Return self>=value.'
        ...
    
    def __gt__(self, value) -> bool:
        'Return self>value.'
        ...
    
    def __hash__(self) -> int:
        'Return hash(self).'
        ...
    
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __le__(self, value) -> bool:
        'Return self<=value.'
        ...
    
    def __lt__(self, value) -> bool:
        'Return self<value.'
        ...
    
    def __ne__(self, value) -> bool:
        'Return self!=value.'
        ...
    
    __pyx_vtable__: PyCapsule
    def __radd__(self, value) -> _Timestamp:
        'Return value+self.'
        ...
    
    def __reduce__(self) -> typing.Union[str, typing.Tuple[typing.Any, ...]]:
        ...
    
    def __reduce_ex__(self, protocol: int) -> typing.Union[str, typing.Tuple[typing.Any, ...]]:
        ...
    
    def __repr__(self) -> str:
        'Return repr(self).'
        ...
    
    def __rsub__(self, value) -> _Timestamp:
        'Return value-self.'
        ...
    
    def __setstate__(self, state: typing.Any) -> None:
        ...
    
    def __sub__(self, value) -> _Timestamp:
        'Return self-value.'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @property
    def _date_repr(self) -> typing.Any:
        ...
    
    @property
    def _repr_base(self) -> typing.Any:
        ...
    
    @property
    def _short_repr(self) -> typing.Any:
        ...
    
    @property
    def _time_repr(self) -> typing.Any:
        ...
    
    @property
    def asm8(self) -> typing.Any:
        '\n        Return numpy datetime64 format in nanoseconds.\n        '
        ...
    
    @classmethod
    def combine(cls) -> typing.Any:
        'date, time -> datetime with same date and time fields'
        ...
    
    def day_name(self) -> typing.Any:
        '\n        Return the day name of the Timestamp with specified locale.\n\n        Parameters\n        ----------\n        locale : str, default None (English locale)\n            Locale determining the language in which to return the day name.\n\n        Returns\n        -------\n        str\n        '
        ...
    
    @property
    def day_of_week(self) -> typing.Any:
        '\n        Return day of the week.\n        '
        ...
    
    @property
    def day_of_year(self) -> typing.Any:
        '\n        Return the day of the year.\n        '
        ...
    
    @property
    def dayofweek(self) -> typing.Any:
        '\n        Return day of the week.\n        '
        ...
    
    @property
    def dayofyear(self) -> typing.Any:
        '\n        Return the day of the year.\n        '
        ...
    
    @property
    def days_in_month(self) -> typing.Any:
        '\n        Return the number of days in the month.\n        '
        ...
    
    @property
    def freq(self) -> typing.Any:
        ...
    
    @classmethod
    def fromisocalendar(cls) -> typing.Any:
        'int, int, int -> Construct a date from the ISO year, week number and weekday.\n\nThis is the inverse of the date.isocalendar() function'
        ...
    
    @classmethod
    def fromisoformat(cls) -> typing.Any:
        'string -> datetime from datetime.isoformat() output'
        ...
    
    @classmethod
    def fromordinal(cls) -> typing.Any:
        'int -> date corresponding to a proleptic Gregorian ordinal.'
        ...
    
    @classmethod
    def fromtimestamp(cls) -> typing.Any:
        "timestamp[, tz] -> tz's local time from POSIX timestamp."
        ...
    
    @property
    def is_leap_year(self) -> typing.Any:
        '\n        Return True if year is a leap year.\n        '
        ...
    
    @property
    def is_month_end(self) -> typing.Any:
        '\n        Return True if date is last day of month.\n        '
        ...
    
    @property
    def is_month_start(self) -> typing.Any:
        '\n        Return True if date is first day of month.\n        '
        ...
    
    @property
    def is_quarter_end(self) -> typing.Any:
        '\n        Return True if date is last day of the quarter.\n        '
        ...
    
    @property
    def is_quarter_start(self) -> typing.Any:
        '\n        Return True if date is first day of the quarter.\n        '
        ...
    
    @property
    def is_year_end(self) -> typing.Any:
        '\n        Return True if date is last day of the year.\n        '
        ...
    
    @property
    def is_year_start(self) -> typing.Any:
        '\n        Return True if date is first day of the year.\n        '
        ...
    
    def isoformat(self) -> typing.Any:
        ...
    
    def month_name(self) -> typing.Any:
        '\n        Return the month name of the Timestamp with specified locale.\n\n        Parameters\n        ----------\n        locale : str, default None (English locale)\n            Locale determining the language in which to return the month name.\n\n        Returns\n        -------\n        str\n        '
        ...
    
    @property
    def nanosecond(self) -> typing.Any:
        ...
    
    def normalize(self) -> typing.Any:
        '\n        Normalize Timestamp to midnight, preserving tz information.\n        '
        ...
    
    @classmethod
    def now(cls, type, tz) -> typing.Any:
        'Returns new datetime object representing current time local to tz.\n\n  tz\n    Timezone object.\n\nIf no tz is specified, uses local timezone.'
        ...
    
    @property
    def quarter(self) -> typing.Any:
        '\n        Return the quarter of the year.\n        '
        ...
    
    @classmethod
    def strptime(cls) -> typing.Any:
        'string, format -> new datetime parsed from a string (like time.strptime()).'
        ...
    
    def timestamp(self) -> typing.Any:
        'Return POSIX timestamp as float.'
        ...
    
    def to_datetime64(self) -> typing.Any:
        "\n        Return a numpy.datetime64 object with 'ns' precision.\n        "
        ...
    
    def to_numpy(self) -> typing.Any:
        '\n        Convert the Timestamp to a NumPy datetime64.\n\n        .. versionadded:: 0.25.0\n\n        This is an alias method for `Timestamp.to_datetime64()`. The dtype and\n        copy parameters are available here only for compatibility. Their values\n        will not affect the return value.\n\n        Returns\n        -------\n        numpy.datetime64\n\n        See Also\n        --------\n        DatetimeIndex.to_numpy : Similar method for DatetimeIndex.\n        '
        ...
    
    def to_period(self) -> typing.Any:
        '\n        Return an period of which this timestamp is an observation.\n        '
        ...
    
    def to_pydatetime(self) -> typing.Any:
        '\n        Convert a Timestamp object to a native Python datetime object.\n\n        If warn=True, issue a warning if nanoseconds is nonzero.\n        '
        ...
    
    @classmethod
    def today(cls) -> typing.Any:
        'Current date or datetime:  same as self.__class__.fromtimestamp(time.time()).'
        ...
    
    @classmethod
    def utcfromtimestamp(cls) -> typing.Any:
        'Construct a naive UTC datetime from a POSIX timestamp.'
        ...
    
    @classmethod
    def utcnow(cls) -> typing.Any:
        'Return a new datetime representing UTC day and time.'
        ...
    
    @property
    def value(self) -> typing.Any:
        ...
    
    @property
    def week(self) -> typing.Any:
        '\n        Return the week number of the year.\n        '
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

__doc__: str
__file__: str
__name__: str
__package__: str
__pyx_capi__: dict
def __pyx_unpickle_Enum() -> typing.Any:
    ...

__test__: dict
_no_input: object
_zero_time: _mod_datetime.time
def get_date_name_field() -> typing.Any:
    '\n    Given a int64-based datetime index, return array of strings of date\n    name based on requested field (e.g. day_name)\n    '
    ...

def get_start_end_field() -> typing.Any:
    '\n    Given an int64-based datetime index return array of indicators\n    of whether timestamps are at the start/end of the month/quarter/year\n    (defined by frequency).\n    '
    ...

def integer_op_not_supported() -> typing.Any:
    ...

def round_nsint64() -> typing.Any:
    '\n    Applies rounding mode at given frequency\n\n    Parameters\n    ----------\n    values : :obj:`ndarray`\n    mode : instance of `RoundTo` enumeration\n    freq : str, obj\n\n    Returns\n    -------\n    :obj:`ndarray`\n    '
    ...

def __getattr__(name) -> typing.Any:
    ...

