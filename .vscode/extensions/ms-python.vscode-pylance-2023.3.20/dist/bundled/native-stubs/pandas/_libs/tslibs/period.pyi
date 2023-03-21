# Python: 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)]
# Library: pandas, version: 1.2.4
# Module: pandas._libs.tslibs.period, version: unspecified
import typing
import builtins as _mod_builtins
import pandas._libs.tslibs.timedeltas as _mod_pandas__libs_tslibs_timedeltas
import pandas._libs.tslibs.timestamps as _mod_pandas__libs_tslibs_timestamps

DIFFERENT_FREQ: str
INVALID_FREQ_ERR_MSG: str
class IncompatibleFrequency(_mod_builtins.ValueError):
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, *args, **kwargs) -> None:
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
    

class Period(_Period):
    "\n    Represents a period of time.\n\n    Parameters\n    ----------\n    value : Period or str, default None\n        The time period represented (e.g., '4Q2005').\n    freq : str, default None\n        One of pandas period strings or corresponding objects.\n    ordinal : int, default None\n        The period offset from the proleptic Gregorian epoch.\n    year : int, default None\n        Year value of the period.\n    month : int, default 1\n        Month value of the period.\n    quarter : int, default None\n        Quarter value of the period.\n    day : int, default 1\n        Day value of the period.\n    hour : int, default 0\n        Hour value of the period.\n    minute : int, default 0\n        Minute value of the period.\n    second : int, default 0\n        Second value of the period.\n    "
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, *args, **kwargs) -> None:
        "\n    Represents a period of time.\n\n    Parameters\n    ----------\n    value : Period or str, default None\n        The time period represented (e.g., '4Q2005').\n    freq : str, default None\n        One of pandas period strings or corresponding objects.\n    ordinal : int, default None\n        The period offset from the proleptic Gregorian epoch.\n    year : int, default None\n        Year value of the period.\n    month : int, default 1\n        Month value of the period.\n    quarter : int, default None\n        Quarter value of the period.\n    day : int, default 1\n        Day value of the period.\n    hour : int, default 0\n        Hour value of the period.\n    minute : int, default 0\n        Minute value of the period.\n    second : int, default 0\n        Second value of the period.\n    "
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
    
    @classmethod
    def _from_ordinal(cls) -> typing.Any:
        '\n        Fast creation from an ordinal and freq that are already validated!\n        '
        ...
    
    @classmethod
    def _maybe_convert_freq(cls) -> typing.Any:
        "\n        Internally we allow integer and tuple representations (for now) that\n        are not recognized by to_offset, so we convert them here.  Also, a\n        Period's freq attribute must have `freq.n > 0`, which we check for here.\n\n        Returns\n        -------\n        DateOffset\n        "
        ...
    
    @classmethod
    def now(cls) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class PeriodMixin(_mod_builtins.object):
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    def __reduce__(self) -> typing.Union[str, typing.Tuple[typing.Any, ...]]:
        ...
    
    def __setstate__(self, state: typing.Any) -> None:
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def _get_to_timestamp_base(self) -> typing.Any:
        '\n        Return frequency code group used for base of to_timestamp against\n        frequency code.\n\n        Return day freq code against longer freq than day.\n        Return second freq code against hour between second.\n\n        Returns\n        -------\n        int\n        '
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

Timedelta = _mod_pandas__libs_tslibs_timedeltas.Timedelta
Timestamp = _mod_pandas__libs_tslibs_timestamps.Timestamp
class _Period(PeriodMixin):
    def __add__(self, value) -> _Period:
        'Return self+value.'
        ...
    
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
    def __radd__(self, value) -> _Period:
        'Return value+self.'
        ...
    
    def __reduce__(self) -> typing.Union[str, typing.Tuple[typing.Any, ...]]:
        ...
    
    def __repr__(self) -> str:
        'Return repr(self).'
        ...
    
    def __rsub__(self, value) -> _Period:
        'Return value-self.'
        ...
    
    def __setstate__(self, state: typing.Any) -> None:
        ...
    
    def __str__(self) -> str:
        '\n        Return a string representation for a particular DataFrame\n        '
        ...
    
    def __sub__(self, value) -> _Period:
        'Return self-value.'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def _add_delta(self) -> typing.Any:
        ...
    
    def _add_offset(self) -> typing.Any:
        ...
    
    @property
    def _dtype(self) -> typing.Any:
        ...
    
    @classmethod
    def _from_ordinal(cls) -> typing.Any:
        '\n        Fast creation from an ordinal and freq that are already validated!\n        '
        ...
    
    @classmethod
    def _maybe_convert_freq(cls) -> typing.Any:
        "\n        Internally we allow integer and tuple representations (for now) that\n        are not recognized by to_offset, so we convert them here.  Also, a\n        Period's freq attribute must have `freq.n > 0`, which we check for here.\n\n        Returns\n        -------\n        DateOffset\n        "
        ...
    
    def asfreq(self) -> typing.Any:
        "\n        Convert Period to desired frequency, at the start or end of the interval.\n\n        Parameters\n        ----------\n        freq : str\n            The desired frequency.\n        how : {'E', 'S', 'end', 'start'}, default 'end'\n            Start or end of the timespan.\n\n        Returns\n        -------\n        resampled : Period\n        "
        ...
    
    @property
    def day(self) -> typing.Any:
        '\n        Get day of the month that a Period falls on.\n\n        Returns\n        -------\n        int\n\n        See Also\n        --------\n        Period.dayofweek : Get the day of the week.\n        Period.dayofyear : Get the day of the year.\n\n        Examples\n        --------\n        >>> p = pd.Period("2018-03-11", freq=\'H\')\n        >>> p.day\n        11\n        '
        ...
    
    @property
    def day_of_week(self) -> typing.Any:
        "\n        Day of the week the period lies in, with Monday=0 and Sunday=6.\n\n        If the period frequency is lower than daily (e.g. hourly), and the\n        period spans over multiple days, the day at the start of the period is\n        used.\n\n        If the frequency is higher than daily (e.g. monthly), the last day\n        of the period is used.\n\n        Returns\n        -------\n        int\n            Day of the week.\n\n        See Also\n        --------\n        Period.day_of_week : Day of the week the period lies in.\n        Period.weekday : Alias of Period.day_of_week.\n        Period.day : Day of the month.\n        Period.dayofyear : Day of the year.\n\n        Examples\n        --------\n        >>> per = pd.Period('2017-12-31 22:00', 'H')\n        >>> per.day_of_week\n        6\n\n        For periods that span over multiple days, the day at the beginning of\n        the period is returned.\n\n        >>> per = pd.Period('2017-12-31 22:00', '4H')\n        >>> per.day_of_week\n        6\n        >>> per.start_time.day_of_week\n        6\n\n        For periods with a frequency higher than days, the last day of the\n        period is returned.\n\n        >>> per = pd.Period('2018-01', 'M')\n        >>> per.day_of_week\n        2\n        >>> per.end_time.day_of_week\n        2\n        "
        ...
    
    @property
    def day_of_year(self) -> typing.Any:
        '\n        Return the day of the year.\n\n        This attribute returns the day of the year on which the particular\n        date occurs. The return value ranges between 1 to 365 for regular\n        years and 1 to 366 for leap years.\n\n        Returns\n        -------\n        int\n            The day of year.\n\n        See Also\n        --------\n        Period.day : Return the day of the month.\n        Period.day_of_week : Return the day of week.\n        PeriodIndex.day_of_year : Return the day of year of all indexes.\n\n        Examples\n        --------\n        >>> period = pd.Period("2015-10-23", freq=\'H\')\n        >>> period.day_of_year\n        296\n        >>> period = pd.Period("2012-12-31", freq=\'D\')\n        >>> period.day_of_year\n        366\n        >>> period = pd.Period("2013-01-01", freq=\'D\')\n        >>> period.day_of_year\n        1\n        '
        ...
    
    @property
    def dayofweek(self) -> typing.Any:
        "\n        Day of the week the period lies in, with Monday=0 and Sunday=6.\n\n        If the period frequency is lower than daily (e.g. hourly), and the\n        period spans over multiple days, the day at the start of the period is\n        used.\n\n        If the frequency is higher than daily (e.g. monthly), the last day\n        of the period is used.\n\n        Returns\n        -------\n        int\n            Day of the week.\n\n        See Also\n        --------\n        Period.day_of_week : Day of the week the period lies in.\n        Period.weekday : Alias of Period.day_of_week.\n        Period.day : Day of the month.\n        Period.dayofyear : Day of the year.\n\n        Examples\n        --------\n        >>> per = pd.Period('2017-12-31 22:00', 'H')\n        >>> per.day_of_week\n        6\n\n        For periods that span over multiple days, the day at the beginning of\n        the period is returned.\n\n        >>> per = pd.Period('2017-12-31 22:00', '4H')\n        >>> per.day_of_week\n        6\n        >>> per.start_time.day_of_week\n        6\n\n        For periods with a frequency higher than days, the last day of the\n        period is returned.\n\n        >>> per = pd.Period('2018-01', 'M')\n        >>> per.day_of_week\n        2\n        >>> per.end_time.day_of_week\n        2\n        "
        ...
    
    @property
    def dayofyear(self) -> typing.Any:
        '\n        Return the day of the year.\n\n        This attribute returns the day of the year on which the particular\n        date occurs. The return value ranges between 1 to 365 for regular\n        years and 1 to 366 for leap years.\n\n        Returns\n        -------\n        int\n            The day of year.\n\n        See Also\n        --------\n        Period.day : Return the day of the month.\n        Period.day_of_week : Return the day of week.\n        PeriodIndex.day_of_year : Return the day of year of all indexes.\n\n        Examples\n        --------\n        >>> period = pd.Period("2015-10-23", freq=\'H\')\n        >>> period.day_of_year\n        296\n        >>> period = pd.Period("2012-12-31", freq=\'D\')\n        >>> period.day_of_year\n        366\n        >>> period = pd.Period("2013-01-01", freq=\'D\')\n        >>> period.day_of_year\n        1\n        '
        ...
    
    @property
    def days_in_month(self) -> typing.Any:
        "\n        Get the total number of days in the month that this period falls on.\n\n        Returns\n        -------\n        int\n\n        See Also\n        --------\n        Period.daysinmonth : Gets the number of days in the month.\n        DatetimeIndex.daysinmonth : Gets the number of days in the month.\n        calendar.monthrange : Returns a tuple containing weekday\n            (0-6 ~ Mon-Sun) and number of days (28-31).\n\n        Examples\n        --------\n        >>> p = pd.Period('2018-2-17')\n        >>> p.days_in_month\n        28\n\n        >>> pd.Period('2018-03-01').days_in_month\n        31\n\n        Handles the leap year case as well:\n\n        >>> p = pd.Period('2016-2-17')\n        >>> p.days_in_month\n        29\n        "
        ...
    
    @property
    def daysinmonth(self) -> typing.Any:
        '\n        Get the total number of days of the month that the Period falls in.\n\n        Returns\n        -------\n        int\n\n        See Also\n        --------\n        Period.days_in_month : Return the days of the month.\n        Period.dayofyear : Return the day of the year.\n\n        Examples\n        --------\n        >>> p = pd.Period("2018-03-11", freq=\'H\')\n        >>> p.daysinmonth\n        31\n        '
        ...
    
    @property
    def end_time(self) -> typing.Any:
        ...
    
    @property
    def freq(self) -> typing.Any:
        ...
    
    @property
    def freqstr(self) -> typing.Any:
        ...
    
    @property
    def hour(self) -> typing.Any:
        '\n        Get the hour of the day component of the Period.\n\n        Returns\n        -------\n        int\n            The hour as an integer, between 0 and 23.\n\n        See Also\n        --------\n        Period.second : Get the second component of the Period.\n        Period.minute : Get the minute component of the Period.\n\n        Examples\n        --------\n        >>> p = pd.Period("2018-03-11 13:03:12.050000")\n        >>> p.hour\n        13\n\n        Period longer than a day\n\n        >>> p = pd.Period("2018-03-11", freq="M")\n        >>> p.hour\n        0\n        '
        ...
    
    @property
    def is_leap_year(self) -> typing.Any:
        ...
    
    @property
    def minute(self) -> typing.Any:
        '\n        Get minute of the hour component of the Period.\n\n        Returns\n        -------\n        int\n            The minute as an integer, between 0 and 59.\n\n        See Also\n        --------\n        Period.hour : Get the hour component of the Period.\n        Period.second : Get the second component of the Period.\n\n        Examples\n        --------\n        >>> p = pd.Period("2018-03-11 13:03:12.050000")\n        >>> p.minute\n        3\n        '
        ...
    
    @property
    def month(self) -> typing.Any:
        ...
    
    @classmethod
    def now(cls) -> typing.Any:
        ...
    
    @property
    def ordinal(self) -> typing.Any:
        ...
    
    @property
    def quarter(self) -> typing.Any:
        ...
    
    @property
    def qyear(self) -> typing.Any:
        "\n        Fiscal year the Period lies in according to its starting-quarter.\n\n        The `year` and the `qyear` of the period will be the same if the fiscal\n        and calendar years are the same. When they are not, the fiscal year\n        can be different from the calendar year of the period.\n\n        Returns\n        -------\n        int\n            The fiscal year of the period.\n\n        See Also\n        --------\n        Period.year : Return the calendar year of the period.\n\n        Examples\n        --------\n        If the natural and fiscal year are the same, `qyear` and `year` will\n        be the same.\n\n        >>> per = pd.Period('2018Q1', freq='Q')\n        >>> per.qyear\n        2018\n        >>> per.year\n        2018\n\n        If the fiscal year starts in April (`Q-MAR`), the first quarter of\n        2018 will start in April 2017. `year` will then be 2018, but `qyear`\n        will be the fiscal year, 2018.\n\n        >>> per = pd.Period('2018Q1', freq='Q-MAR')\n        >>> per.start_time\n        Timestamp('2017-04-01 00:00:00')\n        >>> per.qyear\n        2018\n        >>> per.year\n        2017\n        "
        ...
    
    @property
    def second(self) -> typing.Any:
        '\n        Get the second component of the Period.\n\n        Returns\n        -------\n        int\n            The second of the Period (ranges from 0 to 59).\n\n        See Also\n        --------\n        Period.hour : Get the hour component of the Period.\n        Period.minute : Get the minute component of the Period.\n\n        Examples\n        --------\n        >>> p = pd.Period("2018-03-11 13:03:12.050000")\n        >>> p.second\n        12\n        '
        ...
    
    @property
    def start_time(self) -> typing.Any:
        "\n        Get the Timestamp for the start of the period.\n\n        Returns\n        -------\n        Timestamp\n\n        See Also\n        --------\n        Period.end_time : Return the end Timestamp.\n        Period.dayofyear : Return the day of year.\n        Period.daysinmonth : Return the days in that month.\n        Period.dayofweek : Return the day of the week.\n\n        Examples\n        --------\n        >>> period = pd.Period('2012-1-1', freq='D')\n        >>> period\n        Period('2012-01-01', 'D')\n\n        >>> period.start_time\n        Timestamp('2012-01-01 00:00:00')\n\n        >>> period.end_time\n        Timestamp('2012-01-01 23:59:59.999999999')\n        "
        ...
    
    def strftime(self) -> typing.Any:
        "\n        Returns the string representation of the :class:`Period`, depending\n        on the selected ``fmt``. ``fmt`` must be a string\n        containing one or several directives.  The method recognizes the same\n        directives as the :func:`time.strftime` function of the standard Python\n        distribution, as well as the specific additional directives ``%f``,\n        ``%F``, ``%q``. (formatting & docs originally from scikits.timeries).\n\n        +-----------+--------------------------------+-------+\n        | Directive | Meaning                        | Notes |\n        +===========+================================+=======+\n        | ``%a``    | Locale's abbreviated weekday   |       |\n        |           | name.                          |       |\n        +-----------+--------------------------------+-------+\n        | ``%A``    | Locale's full weekday name.    |       |\n        +-----------+--------------------------------+-------+\n        | ``%b``    | Locale's abbreviated month     |       |\n        |           | name.                          |       |\n        +-----------+--------------------------------+-------+\n        | ``%B``    | Locale's full month name.      |       |\n        +-----------+--------------------------------+-------+\n        | ``%c``    | Locale's appropriate date and  |       |\n        |           | time representation.           |       |\n        +-----------+--------------------------------+-------+\n        | ``%d``    | Day of the month as a decimal  |       |\n        |           | number [01,31].                |       |\n        +-----------+--------------------------------+-------+\n        | ``%f``    | 'Fiscal' year without a        | \\(1)  |\n        |           | century  as a decimal number   |       |\n        |           | [00,99]                        |       |\n        +-----------+--------------------------------+-------+\n        | ``%F``    | 'Fiscal' year with a century   | \\(2)  |\n        |           | as a decimal number            |       |\n        +-----------+--------------------------------+-------+\n        | ``%H``    | Hour (24-hour clock) as a      |       |\n        |           | decimal number [00,23].        |       |\n        +-----------+--------------------------------+-------+\n        | ``%I``    | Hour (12-hour clock) as a      |       |\n        |           | decimal number [01,12].        |       |\n        +-----------+--------------------------------+-------+\n        | ``%j``    | Day of the year as a decimal   |       |\n        |           | number [001,366].              |       |\n        +-----------+--------------------------------+-------+\n        | ``%m``    | Month as a decimal number      |       |\n        |           | [01,12].                       |       |\n        +-----------+--------------------------------+-------+\n        | ``%M``    | Minute as a decimal number     |       |\n        |           | [00,59].                       |       |\n        +-----------+--------------------------------+-------+\n        | ``%p``    | Locale's equivalent of either  | \\(3)  |\n        |           | AM or PM.                      |       |\n        +-----------+--------------------------------+-------+\n        | ``%q``    | Quarter as a decimal number    |       |\n        |           | [01,04]                        |       |\n        +-----------+--------------------------------+-------+\n        | ``%S``    | Second as a decimal number     | \\(4)  |\n        |           | [00,61].                       |       |\n        +-----------+--------------------------------+-------+\n        | ``%U``    | Week number of the year        | \\(5)  |\n        |           | (Sunday as the first day of    |       |\n        |           | the week) as a decimal number  |       |\n        |           | [00,53].  All days in a new    |       |\n        |           | year preceding the first       |       |\n        |           | Sunday are considered to be in |       |\n        |           | week 0.                        |       |\n        +-----------+--------------------------------+-------+\n        | ``%w``    | Weekday as a decimal number    |       |\n        |           | [0(Sunday),6].                 |       |\n        +-----------+--------------------------------+-------+\n        | ``%W``    | Week number of the year        | \\(5)  |\n        |           | (Monday as the first day of    |       |\n        |           | the week) as a decimal number  |       |\n        |           | [00,53].  All days in a new    |       |\n        |           | year preceding the first       |       |\n        |           | Monday are considered to be in |       |\n        |           | week 0.                        |       |\n        +-----------+--------------------------------+-------+\n        | ``%x``    | Locale's appropriate date      |       |\n        |           | representation.                |       |\n        +-----------+--------------------------------+-------+\n        | ``%X``    | Locale's appropriate time      |       |\n        |           | representation.                |       |\n        +-----------+--------------------------------+-------+\n        | ``%y``    | Year without century as a      |       |\n        |           | decimal number [00,99].        |       |\n        +-----------+--------------------------------+-------+\n        | ``%Y``    | Year with century as a decimal |       |\n        |           | number.                        |       |\n        +-----------+--------------------------------+-------+\n        | ``%Z``    | Time zone name (no characters  |       |\n        |           | if no time zone exists).       |       |\n        +-----------+--------------------------------+-------+\n        | ``%%``    | A literal ``'%'`` character.   |       |\n        +-----------+--------------------------------+-------+\n\n        Notes\n        -----\n\n        (1)\n            The ``%f`` directive is the same as ``%y`` if the frequency is\n            not quarterly.\n            Otherwise, it corresponds to the 'fiscal' year, as defined by\n            the :attr:`qyear` attribute.\n\n        (2)\n            The ``%F`` directive is the same as ``%Y`` if the frequency is\n            not quarterly.\n            Otherwise, it corresponds to the 'fiscal' year, as defined by\n            the :attr:`qyear` attribute.\n\n        (3)\n            The ``%p`` directive only affects the output hour field\n            if the ``%I`` directive is used to parse the hour.\n\n        (4)\n            The range really is ``0`` to ``61``; this accounts for leap\n            seconds and the (very rare) double leap seconds.\n\n        (5)\n            The ``%U`` and ``%W`` directives are only used in calculations\n            when the day of the week and the year are specified.\n\n        Examples\n        --------\n\n        >>> a = Period(freq='Q-JUL', year=2006, quarter=1)\n        >>> a.strftime('%F-Q%q')\n        '2006-Q1'\n        >>> # Output the last month in the quarter of this date\n        >>> a.strftime('%b-%Y')\n        'Oct-2005'\n        >>>\n        >>> a = Period(freq='D', year=2001, month=1, day=1)\n        >>> a.strftime('%d-%b-%Y')\n        '01-Jan-2006'\n        >>> a.strftime('%b. %d, %Y was a %A')\n        'Jan. 01, 2001 was a Monday'\n        "
        ...
    
    def to_timestamp(self) -> typing.Any:
        "\n        Return the Timestamp representation of the Period.\n\n        Uses the target frequency specified at the part of the period specified\n        by `how`, which is either `Start` or `Finish`.\n\n        Parameters\n        ----------\n        freq : str or DateOffset\n            Target frequency. Default is 'D' if self.freq is week or\n            longer and 'S' otherwise.\n        how : str, default 'S' (start)\n            One of 'S', 'E'. Can be aliased as case insensitive\n            'Start', 'Finish', 'Begin', 'End'.\n\n        Returns\n        -------\n        Timestamp\n        "
        ...
    
    @property
    def week(self) -> typing.Any:
        '\n        Get the week of the year on the given Period.\n\n        Returns\n        -------\n        int\n\n        See Also\n        --------\n        Period.dayofweek : Get the day component of the Period.\n        Period.weekday : Get the day component of the Period.\n\n        Examples\n        --------\n        >>> p = pd.Period("2018-03-11", "H")\n        >>> p.week\n        10\n\n        >>> p = pd.Period("2018-02-01", "D")\n        >>> p.week\n        5\n\n        >>> p = pd.Period("2018-01-06", "D")\n        >>> p.week\n        1\n        '
        ...
    
    @property
    def weekday(self) -> typing.Any:
        "\n        Day of the week the period lies in, with Monday=0 and Sunday=6.\n\n        If the period frequency is lower than daily (e.g. hourly), and the\n        period spans over multiple days, the day at the start of the period is\n        used.\n\n        If the frequency is higher than daily (e.g. monthly), the last day\n        of the period is used.\n\n        Returns\n        -------\n        int\n            Day of the week.\n\n        See Also\n        --------\n        Period.dayofweek : Day of the week the period lies in.\n        Period.weekday : Alias of Period.dayofweek.\n        Period.day : Day of the month.\n        Period.dayofyear : Day of the year.\n\n        Examples\n        --------\n        >>> per = pd.Period('2017-12-31 22:00', 'H')\n        >>> per.dayofweek\n        6\n\n        For periods that span over multiple days, the day at the beginning of\n        the period is returned.\n\n        >>> per = pd.Period('2017-12-31 22:00', '4H')\n        >>> per.dayofweek\n        6\n        >>> per.start_time.dayofweek\n        6\n\n        For periods with a frequency higher than days, the last day of the\n        period is returned.\n\n        >>> per = pd.Period('2018-01', 'M')\n        >>> per.dayofweek\n        2\n        >>> per.end_time.dayofweek\n        2\n        "
        ...
    
    @property
    def weekofyear(self) -> typing.Any:
        ...
    
    @property
    def year(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

__doc__: typing.Any
__file__: str
__name__: str
__package__: str
__pyx_capi__: dict
def __pyx_unpickle_Enum() -> typing.Any:
    ...

def __pyx_unpickle_PeriodMixin() -> typing.Any:
    ...

__test__: dict
def ensure_datetime64ns() -> typing.Any:
    "\n    Ensure a np.datetime64 array has dtype specifically 'datetime64[ns]'\n\n    Parameters\n    ----------\n    arr : ndarray\n    copy : bool, default True\n\n    Returns\n    -------\n    ndarray with dtype datetime64[ns]\n    "
    ...

def extract_freq() -> typing.Any:
    ...

def extract_ordinals() -> typing.Any:
    ...

def freq_to_dtype_code() -> typing.Any:
    ...

def get_period_field_arr() -> typing.Any:
    ...

def parse_time_string() -> typing.Any:
    '\n    Try hard to parse datetime string, leveraging dateutil plus some extra\n    goodies like quarter recognition.\n\n    Parameters\n    ----------\n    arg : str\n    freq : str or DateOffset, default None\n        Helps with interpreting time string if supplied\n    dayfirst : bool, default None\n        If None uses default from print_config\n    yearfirst : bool, default None\n        If None uses default from print_config\n\n    Returns\n    -------\n    datetime, datetime/dateutil.parser._result, str\n    '
    ...

def period_asfreq() -> typing.Any:
    "\n    Convert period ordinal from one frequency to another, and if upsampling,\n    choose to use start ('S') or end ('E') of period.\n    "
    ...

def period_asfreq_arr() -> typing.Any:
    "\n    Convert int64-array of period ordinals from one frequency to another, and\n    if upsampling, choose to use start ('S') or end ('E') of period.\n    "
    ...

def period_ordinal() -> typing.Any:
    '\n    Find the ordinal representation of the given datetime components at the\n    frequency `freq`.\n\n    Parameters\n    ----------\n    y : int\n    m : int\n    d : int\n    h : int\n    min : int\n    s : int\n    us : int\n    ps : int\n\n    Returns\n    -------\n    ordinal : int64_t\n    '
    ...

def periodarr_to_dt64arr() -> typing.Any:
    '\n    Convert array to datetime64 values from a set of ordinals corresponding to\n    periods per period convention.\n    '
    ...

def quarter_to_myear() -> typing.Any:
    '\n    A quarterly frequency defines a "year" which may not coincide with\n    the calendar-year.  Find the calendar-year and calendar-month associated\n    with the given year and quarter under the `freq`-derived calendar.\n\n    Parameters\n    ----------\n    year : int\n    quarter : int\n    freqstr : str\n        Equivalent to freq.freqstr\n\n    Returns\n    -------\n    year : int\n    month : int\n\n    See Also\n    --------\n    Period.qyear\n    '
    ...

def validate_end_alias() -> typing.Any:
    ...

def __getattr__(name) -> typing.Any:
    ...

