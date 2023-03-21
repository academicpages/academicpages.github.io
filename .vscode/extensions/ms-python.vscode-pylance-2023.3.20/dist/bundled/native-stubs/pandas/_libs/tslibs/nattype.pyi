# Python: 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)]
# Library: pandas, version: 1.2.4
# Module: pandas._libs.tslibs.nattype, version: unspecified
import typing
import builtins as _mod_builtins
import datetime as _mod_datetime

NaT: NaTType
class NaTType(_NaT):
    '\n    (N)ot-(A)-(T)ime, the time equivalent of NaN.\n    '
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, *args, **kwargs) -> None:
        '\n    (N)ot-(A)-(T)ime, the time equivalent of NaN.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __rdiv__(self, other) -> typing.Any:
        ...
    
    def __reduce__(self) -> typing.Union[str, typing.Tuple[typing.Any, ...]]:
        ...
    
    def __reduce_ex__(self, protocol) -> typing.Union[str, typing.Tuple[typing.Any, ...]]:
        ...
    
    def __rfloordiv__(self, other) -> NaTType:
        ...
    
    def __rmul__(self, other) -> NaTType:
        ...
    
    def __rtruediv__(self, other) -> NaTType:
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @property
    def __weakref__(self) -> typing.Any:
        'list of weak references to the object (if defined)'
        ...
    
    def astimezone(self, *args, **kwargs) -> typing.Any:
        '\n        Convert tz-aware Timestamp to another time zone.\n\n        Parameters\n        ----------\n        tz : str, pytz.timezone, dateutil.tz.tzfile or None\n            Time zone for time which Timestamp will be converted to.\n            None will remove timezone holding UTC time.\n\n        Returns\n        -------\n        converted : Timestamp\n\n        Raises\n        ------\n        TypeError\n            If Timestamp is tz-naive.\n        '
        ...
    
    def ceil(self, *args, **kwargs) -> typing.Any:
        "\n        Return a new Timestamp ceiled to this resolution.\n\n        Parameters\n        ----------\n        freq : str\n            Frequency string indicating the ceiling resolution.\n        ambiguous : bool or {'raise', 'NaT'}, default 'raise'\n            The behavior is as follows:\n\n            * bool contains flags to determine if time is dst or not (note\n              that this flag is only applicable for ambiguous fall dst dates).\n            * 'NaT' will return NaT for an ambiguous time.\n            * 'raise' will raise an AmbiguousTimeError for an ambiguous time.\n\n            .. versionadded:: 0.24.0\n        nonexistent : {'raise', 'shift_forward', 'shift_backward, 'NaT', timedelta}, default 'raise'\n            A nonexistent time does not exist in a particular timezone\n            where clocks moved forward due to DST.\n\n            * 'shift_forward' will shift the nonexistent time forward to the\n              closest existing time.\n            * 'shift_backward' will shift the nonexistent time backward to the\n              closest existing time.\n            * 'NaT' will return NaT where there are nonexistent times.\n            * timedelta objects will shift nonexistent times by the timedelta.\n            * 'raise' will raise an NonExistentTimeError if there are\n              nonexistent times.\n\n            .. versionadded:: 0.24.0\n\n        Raises\n        ------\n        ValueError if the freq cannot be converted.\n        "
        ...
    
    def combine(self, *args, **kwargs) -> typing.Any:
        '\n        Timestamp.combine(date, time)\n\n        Combine date, time into datetime with same date and time fields.\n        '
        ...
    
    def ctime(self, *args, **kwargs) -> typing.Any:
        'Return ctime() style string.'
        ...
    
    def date(self, *args, **kwargs) -> typing.Any:
        'Return date object with same year, month and day.'
        ...
    
    day: property
    def day_name(self, *args, **kwargs) -> typing.Any:
        '\n        Return the day name of the Timestamp with specified locale.\n\n        Parameters\n        ----------\n        locale : str, default None (English locale)\n            Locale determining the language in which to return the day name.\n\n        Returns\n        -------\n        str\n        '
        ...
    
    day_of_week: property
    day_of_year: property
    dayofweek: property
    dayofyear: property
    days: property
    days_in_month: property
    daysinmonth: property
    def dst(self, *args, **kwargs) -> typing.Any:
        'Return self.tzinfo.dst(self).'
        ...
    
    def floor(self, *args, **kwargs) -> typing.Any:
        "\n        Return a new Timestamp floored to this resolution.\n\n        Parameters\n        ----------\n        freq : str\n            Frequency string indicating the flooring resolution.\n        ambiguous : bool or {'raise', 'NaT'}, default 'raise'\n            The behavior is as follows:\n\n            * bool contains flags to determine if time is dst or not (note\n              that this flag is only applicable for ambiguous fall dst dates).\n            * 'NaT' will return NaT for an ambiguous time.\n            * 'raise' will raise an AmbiguousTimeError for an ambiguous time.\n\n            .. versionadded:: 0.24.0\n        nonexistent : {'raise', 'shift_forward', 'shift_backward, 'NaT', timedelta}, default 'raise'\n            A nonexistent time does not exist in a particular timezone\n            where clocks moved forward due to DST.\n\n            * 'shift_forward' will shift the nonexistent time forward to the\n              closest existing time.\n            * 'shift_backward' will shift the nonexistent time backward to the\n              closest existing time.\n            * 'NaT' will return NaT where there are nonexistent times.\n            * timedelta objects will shift nonexistent times by the timedelta.\n            * 'raise' will raise an NonExistentTimeError if there are\n              nonexistent times.\n\n            .. versionadded:: 0.24.0\n\n        Raises\n        ------\n        ValueError if the freq cannot be converted.\n        "
        ...
    
    def fromisocalendar(self, *args, **kwargs) -> typing.Any:
        'int, int, int -> Construct a date from the ISO year, week number and weekday.\n\nThis is the inverse of the date.isocalendar() function'
        ...
    
    @classmethod
    def fromisoformat(cls) -> typing.Any:
        'string -> datetime from datetime.isoformat() output'
        ...
    
    def fromordinal(self, *args, **kwargs) -> typing.Any:
        '\n        Timestamp.fromordinal(ordinal, freq=None, tz=None)\n\n        Passed an ordinal, translate and convert to a ts.\n        Note: by definition there cannot be any tz info on the ordinal itself.\n\n        Parameters\n        ----------\n        ordinal : int\n            Date corresponding to a proleptic Gregorian ordinal.\n        freq : str, DateOffset\n            Offset to apply to the Timestamp.\n        tz : str, pytz.timezone, dateutil.tz.tzfile or None\n            Time zone for the Timestamp.\n        '
        ...
    
    def fromtimestamp(self, *args, **kwargs) -> typing.Any:
        "\n        Timestamp.fromtimestamp(ts)\n\n        Transform timestamp[, tz] to tz's local time from POSIX timestamp.\n        "
        ...
    
    hour: property
    def isocalendar(self, *args, **kwargs) -> typing.Any:
        'Return a named tuple containing ISO year, week number, and weekday.'
        ...
    
    def isoweekday(self, *args, **kwargs) -> typing.Any:
        'Return the day of the week represented by the date.\nMonday == 1 ... Sunday == 7'
        ...
    
    microsecond: property
    microseconds: property
    millisecond: property
    minute: property
    month: property
    def month_name(self, *args, **kwargs) -> typing.Any:
        '\n        Return the month name of the Timestamp with specified locale.\n\n        Parameters\n        ----------\n        locale : str, default None (English locale)\n            Locale determining the language in which to return the month name.\n\n        Returns\n        -------\n        str\n        '
        ...
    
    nanosecond: property
    nanoseconds: property
    def now(self, *args, **kwargs) -> typing.Any:
        '\n        Timestamp.now(tz=None)\n\n        Return new Timestamp object representing current time local to\n        tz.\n\n        Parameters\n        ----------\n        tz : str or timezone object, default None\n            Timezone to localize to.\n        '
        ...
    
    quarter: property
    qyear: property
    def replace(self, *args, **kwargs) -> typing.Any:
        '\n        Implements datetime.replace, handles nanoseconds.\n\n        Parameters\n        ----------\n        year : int, optional\n        month : int, optional\n        day : int, optional\n        hour : int, optional\n        minute : int, optional\n        second : int, optional\n        microsecond : int, optional\n        nanosecond : int, optional\n        tzinfo : tz-convertible, optional\n        fold : int, optional\n\n        Returns\n        -------\n        Timestamp with fields replaced\n        '
        ...
    
    def round(self, *args, **kwargs) -> typing.Any:
        "\n        Round the Timestamp to the specified resolution.\n\n        Parameters\n        ----------\n        freq : str\n            Frequency string indicating the rounding resolution.\n        ambiguous : bool or {'raise', 'NaT'}, default 'raise'\n            The behavior is as follows:\n\n            * bool contains flags to determine if time is dst or not (note\n              that this flag is only applicable for ambiguous fall dst dates).\n            * 'NaT' will return NaT for an ambiguous time.\n            * 'raise' will raise an AmbiguousTimeError for an ambiguous time.\n\n            .. versionadded:: 0.24.0\n        nonexistent : {'raise', 'shift_forward', 'shift_backward, 'NaT', timedelta}, default 'raise'\n            A nonexistent time does not exist in a particular timezone\n            where clocks moved forward due to DST.\n\n            * 'shift_forward' will shift the nonexistent time forward to the\n              closest existing time.\n            * 'shift_backward' will shift the nonexistent time backward to the\n              closest existing time.\n            * 'NaT' will return NaT where there are nonexistent times.\n            * timedelta objects will shift nonexistent times by the timedelta.\n            * 'raise' will raise an NonExistentTimeError if there are\n              nonexistent times.\n\n            .. versionadded:: 0.24.0\n\n        Returns\n        -------\n        a new Timestamp rounded to the given resolution of `freq`\n\n        Raises\n        ------\n        ValueError if the freq cannot be converted\n        "
        ...
    
    second: property
    seconds: property
    def strftime(self, *args, **kwargs) -> typing.Any:
        '\n        Timestamp.strftime(format)\n\n        Return a string representing the given POSIX timestamp\n        controlled by an explicit format string.\n\n        Parameters\n        ----------\n        format : str\n            Format string to convert Timestamp to string.\n            See strftime documentation for more information on the format string:\n            https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior.\n        '
        ...
    
    def strptime(self, *args, **kwargs) -> typing.Any:
        '\n        Timestamp.strptime(string, format)\n\n        Function is not implemented. Use pd.to_datetime().\n        '
        ...
    
    def time(self, *args, **kwargs) -> typing.Any:
        'Return time object with same time but with tzinfo=None.'
        ...
    
    def timestamp(self, *args, **kwargs) -> typing.Any:
        'Return POSIX timestamp as float.'
        ...
    
    def timetuple(self, *args, **kwargs) -> typing.Any:
        'Return time tuple, compatible with time.localtime().'
        ...
    
    def timetz(self, *args, **kwargs) -> typing.Any:
        'Return time object with same time and tzinfo.'
        ...
    
    def to_pydatetime(self, *args, **kwargs) -> typing.Any:
        '\n        Convert a Timestamp object to a native Python datetime object.\n\n        If warn=True, issue a warning if nanoseconds is nonzero.\n        '
        ...
    
    def today(self, *args, **kwargs) -> typing.Any:
        '\n        Timestamp.today(cls, tz=None)\n\n        Return the current time in the local timezone.  This differs\n        from datetime.today() in that it can be localized to a\n        passed timezone.\n\n        Parameters\n        ----------\n        tz : str or timezone object, default None\n            Timezone to localize to.\n        '
        ...
    
    def toordinal(self, *args, **kwargs) -> typing.Any:
        'Return proleptic Gregorian ordinal.  January 1 of year 1 is day 1.'
        ...
    
    def total_seconds(self, *args, **kwargs) -> typing.Any:
        'Total seconds in the duration.'
        ...
    
    def tz_convert(self, *args, **kwargs) -> typing.Any:
        '\n        Convert tz-aware Timestamp to another time zone.\n\n        Parameters\n        ----------\n        tz : str, pytz.timezone, dateutil.tz.tzfile or None\n            Time zone for time which Timestamp will be converted to.\n            None will remove timezone holding UTC time.\n\n        Returns\n        -------\n        converted : Timestamp\n\n        Raises\n        ------\n        TypeError\n            If Timestamp is tz-naive.\n        '
        ...
    
    def tz_localize(self, *args, **kwargs) -> typing.Any:
        "\n        Convert naive Timestamp to local time zone, or remove\n        timezone from tz-aware Timestamp.\n\n        Parameters\n        ----------\n        tz : str, pytz.timezone, dateutil.tz.tzfile or None\n            Time zone for time which Timestamp will be converted to.\n            None will remove timezone holding local time.\n\n        ambiguous : bool, 'NaT', default 'raise'\n            When clocks moved backward due to DST, ambiguous times may arise.\n            For example in Central European Time (UTC+01), when going from\n            03:00 DST to 02:00 non-DST, 02:30:00 local time occurs both at\n            00:30:00 UTC and at 01:30:00 UTC. In such a situation, the\n            `ambiguous` parameter dictates how ambiguous times should be\n            handled.\n\n            The behavior is as follows:\n\n            * bool contains flags to determine if time is dst or not (note\n              that this flag is only applicable for ambiguous fall dst dates).\n            * 'NaT' will return NaT for an ambiguous time.\n            * 'raise' will raise an AmbiguousTimeError for an ambiguous time.\n\n        nonexistent : 'shift_forward', 'shift_backward, 'NaT', timedelta, default 'raise'\n            A nonexistent time does not exist in a particular timezone\n            where clocks moved forward due to DST.\n\n            The behavior is as follows:\n\n            * 'shift_forward' will shift the nonexistent time forward to the\n              closest existing time.\n            * 'shift_backward' will shift the nonexistent time backward to the\n              closest existing time.\n            * 'NaT' will return NaT where there are nonexistent times.\n            * timedelta objects will shift nonexistent times by the timedelta.\n            * 'raise' will raise an NonExistentTimeError if there are\n              nonexistent times.\n\n            .. versionadded:: 0.24.0\n\n        Returns\n        -------\n        localized : Timestamp\n\n        Raises\n        ------\n        TypeError\n            If the Timestamp is tz-aware and tz is not None.\n        "
        ...
    
    def tzname(self, *args, **kwargs) -> typing.Any:
        'Return self.tzinfo.tzname(self).'
        ...
    
    def utcfromtimestamp(self, *args, **kwargs) -> typing.Any:
        '\n        Timestamp.utcfromtimestamp(ts)\n\n        Construct a naive UTC datetime from a POSIX timestamp.\n        '
        ...
    
    def utcnow(self, *args, **kwargs) -> typing.Any:
        '\n        Timestamp.utcnow()\n\n        Return a new Timestamp representing UTC day and time.\n        '
        ...
    
    def utcoffset(self, *args, **kwargs) -> typing.Any:
        'Return self.tzinfo.utcoffset(self).'
        ...
    
    def utctimetuple(self, *args, **kwargs) -> typing.Any:
        'Return UTC time tuple, compatible with time.localtime().'
        ...
    
    week: property
    def weekday(self, *args, **kwargs) -> typing.Any:
        'Return the day of the week represented by the date.\nMonday == 0 ... Sunday == 6'
        ...
    
    weekofyear: property
    year: property
    def __getattr__(self, name) -> typing.Any:
        ...
    

class _NaT(_mod_datetime.datetime):
    def __add__(self, value) -> _NaT:
        'Return self+value.'
        ...
    
    __array_priority__: int
    def __eq__(self, value) -> bool:
        'Return self==value.'
        ...
    
    def __floordiv__(self, value) -> int:
        'Return self//value.'
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
    
    def __int__(self) -> int:
        'int(self)'
        ...
    
    def __le__(self, value) -> bool:
        'Return self<=value.'
        ...
    
    def __lt__(self, value) -> bool:
        'Return self<value.'
        ...
    
    def __mul__(self, value) -> _NaT:
        'Return self*value.'
        ...
    
    def __ne__(self, value) -> bool:
        'Return self!=value.'
        ...
    
    def __neg__(self) -> _NaT:
        '-self'
        ...
    
    def __pos__(self) -> _NaT:
        '+self'
        ...
    
    def __radd__(self, value) -> _NaT:
        'Return value+self.'
        ...
    
    def __reduce_cython__(self) -> typing.Any:
        ...
    
    def __repr__(self) -> str:
        'Return repr(self).'
        ...
    
    def __rfloordiv__(self, value) -> _NaT:
        'Return value//self.'
        ...
    
    def __rmul__(self, value) -> _NaT:
        'Return value*self.'
        ...
    
    def __rsub__(self, value) -> _NaT:
        'Return value-self.'
        ...
    
    def __rtruediv__(self, value) -> _NaT:
        'Return value/self.'
        ...
    
    def __setstate_cython__(self) -> typing.Any:
        ...
    
    def __str__(self) -> str:
        'Return str(self).'
        ...
    
    def __sub__(self, value) -> _NaT:
        'Return self-value.'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __truediv__(self, value) -> float:
        'Return self/value.'
        ...
    
    @property
    def asm8(self) -> typing.Any:
        ...
    
    @classmethod
    def combine(cls) -> typing.Any:
        'date, time -> datetime with same date and time fields'
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
        ...
    
    @property
    def is_month_end(self) -> typing.Any:
        ...
    
    @property
    def is_month_start(self) -> typing.Any:
        ...
    
    @property
    def is_quarter_end(self) -> typing.Any:
        ...
    
    @property
    def is_quarter_start(self) -> typing.Any:
        ...
    
    @property
    def is_year_end(self) -> typing.Any:
        ...
    
    @property
    def is_year_start(self) -> typing.Any:
        ...
    
    def isoformat(self) -> typing.Any:
        ...
    
    @classmethod
    def now(cls, type, tz) -> typing.Any:
        'Returns new datetime object representing current time local to tz.\n\n  tz\n    Timezone object.\n\nIf no tz is specified, uses local timezone.'
        ...
    
    @classmethod
    def strptime(cls) -> typing.Any:
        'string, format -> new datetime parsed from a string (like time.strptime()).'
        ...
    
    def to_datetime64(self) -> typing.Any:
        "\n        Return a numpy.datetime64 object with 'ns' precision.\n        "
        ...
    
    def to_numpy(self) -> typing.Any:
        '\n        Convert the Timestamp to a NumPy datetime64.\n\n        .. versionadded:: 0.25.0\n\n        This is an alias method for `Timestamp.to_datetime64()`. The dtype and\n        copy parameters are available here only for compatibility. Their values\n        will not affect the return value.\n\n        Returns\n        -------\n        numpy.datetime64\n\n        See Also\n        --------\n        DatetimeIndex.to_numpy : Similar method for DatetimeIndex.\n        '
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
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

__doc__: typing.Any
__file__: str
__name__: str
def __nat_unpickle() -> typing.Any:
    ...

__package__: str
__pyx_capi__: dict
def __pyx_unpickle__NaT() -> typing.Any:
    ...

__test__: dict
def _make_error_func() -> typing.Any:
    ...

def _make_nan_func() -> typing.Any:
    ...

def _make_nat_func() -> typing.Any:
    ...

iNaT: int
def is_null_datetimelike() -> typing.Any:
    '\n    Determine if we have a null for a timedelta/datetime (or integer versions).\n\n    Parameters\n    ----------\n    val : object\n    inat_is_null : bool, default True\n        Whether to treat integer iNaT value as null\n\n    Returns\n    -------\n    bool\n    '
    ...

nat_strings: set
def __getattr__(name) -> typing.Any:
    ...

