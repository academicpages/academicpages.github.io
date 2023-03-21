# Python: 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)]
# Library: pandas, version: 1.2.4
# Module: pandas._libs.tslibs.offsets, version: unspecified
import typing
import builtins as _mod_builtins
import dateutil.relativedelta as _mod_dateutil_relativedelta
import pandas._libs.properties as _mod_pandas__libs_properties
import pandas._libs.tslibs.timedeltas as _mod_pandas__libs_tslibs_timedeltas
import pandas._libs.tslibs.timestamps as _mod_pandas__libs_tslibs_timestamps
import re as _mod_re

def Any(self, *args, **kwds) -> typing.Any:
    'Special type indicating an unconstrained type.\n\n    - Any is compatible with every type.\n    - Any assumed to have all methods.\n    - All values assumed to be instances of Any.\n\n    Note that all the above statements are true from the point of view of\n    static type checkers. At runtime, Any should not be used with instance\n    or class checks.\n    '
    ...

class ApplyTypeError(_mod_builtins.TypeError):
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
    

BDay: BusinessDay
BMonthBegin: BusinessMonthBegin
BMonthEnd: BusinessMonthEnd
class BQuarterBegin(QuarterOffset):
    "\n    DateOffset increments between the first business day of each Quarter.\n\n    startingMonth = 1 corresponds to dates like 1/01/2007, 4/01/2007, ...\n    startingMonth = 2 corresponds to dates like 2/01/2007, 5/01/2007, ...\n    startingMonth = 3 corresponds to dates like 3/01/2007, 6/01/2007, ...\n\n    Examples\n    --------\n    >>> from pandas.tseries.offset import BQuarterBegin\n    >>> ts = pd.Timestamp('2020-05-24 05:01:15')\n    >>> ts + BQuarterBegin()\n    Timestamp('2020-06-01 05:01:15')\n    >>> ts + BQuarterBegin(2)\n    Timestamp('2020-09-01 05:01:15')\n    >>> ts + BQuarterBegin(startingMonth=2)\n    Timestamp('2020-08-03 05:01:15')\n    >>> ts + BQuarterBegin(-1)\n    Timestamp('2020-03-02 05:01:15')\n    "
    def __init__(self, *args, **kwargs) -> None:
        "\n    DateOffset increments between the first business day of each Quarter.\n\n    startingMonth = 1 corresponds to dates like 1/01/2007, 4/01/2007, ...\n    startingMonth = 2 corresponds to dates like 2/01/2007, 5/01/2007, ...\n    startingMonth = 3 corresponds to dates like 3/01/2007, 6/01/2007, ...\n\n    Examples\n    --------\n    >>> from pandas.tseries.offset import BQuarterBegin\n    >>> ts = pd.Timestamp('2020-05-24 05:01:15')\n    >>> ts + BQuarterBegin()\n    Timestamp('2020-06-01 05:01:15')\n    >>> ts + BQuarterBegin(2)\n    Timestamp('2020-09-01 05:01:15')\n    >>> ts + BQuarterBegin(startingMonth=2)\n    Timestamp('2020-08-03 05:01:15')\n    >>> ts + BQuarterBegin(-1)\n    Timestamp('2020-03-02 05:01:15')\n    "
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    _day_opt: str
    _default_starting_month: int
    @classmethod
    def _from_name(cls) -> typing.Any:
        ...
    
    _from_name_starting_month: int
    _output_name: str
    _prefix: str
    def __getattr__(self, name) -> typing.Any:
        ...
    

class BQuarterEnd(QuarterOffset):
    "\n    DateOffset increments between the last business day of each Quarter.\n\n    startingMonth = 1 corresponds to dates like 1/31/2007, 4/30/2007, ...\n    startingMonth = 2 corresponds to dates like 2/28/2007, 5/31/2007, ...\n    startingMonth = 3 corresponds to dates like 3/30/2007, 6/29/2007, ...\n\n    Examples\n    --------\n    >>> from pandas.tseries.offset import BQuarterEnd\n    >>> ts = pd.Timestamp('2020-05-24 05:01:15')\n    >>> ts + BQuarterEnd()\n    Timestamp('2020-06-30 05:01:15')\n    >>> ts + BQuarterEnd(2)\n    Timestamp('2020-09-30 05:01:15')\n    >>> ts + BQuarterEnd(1, startingMonth=2)\n    Timestamp('2020-05-29 05:01:15')\n    >>> ts + BQuarterEnd(startingMonth=2)\n    Timestamp('2020-05-29 05:01:15')\n    "
    def __init__(self, *args, **kwargs) -> None:
        "\n    DateOffset increments between the last business day of each Quarter.\n\n    startingMonth = 1 corresponds to dates like 1/31/2007, 4/30/2007, ...\n    startingMonth = 2 corresponds to dates like 2/28/2007, 5/31/2007, ...\n    startingMonth = 3 corresponds to dates like 3/30/2007, 6/29/2007, ...\n\n    Examples\n    --------\n    >>> from pandas.tseries.offset import BQuarterEnd\n    >>> ts = pd.Timestamp('2020-05-24 05:01:15')\n    >>> ts + BQuarterEnd()\n    Timestamp('2020-06-30 05:01:15')\n    >>> ts + BQuarterEnd(2)\n    Timestamp('2020-09-30 05:01:15')\n    >>> ts + BQuarterEnd(1, startingMonth=2)\n    Timestamp('2020-05-29 05:01:15')\n    >>> ts + BQuarterEnd(startingMonth=2)\n    Timestamp('2020-05-29 05:01:15')\n    "
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    _day_opt: str
    _default_starting_month: int
    @classmethod
    def _from_name(cls) -> typing.Any:
        ...
    
    _from_name_starting_month: int
    _output_name: str
    _prefix: str
    def __getattr__(self, name) -> typing.Any:
        ...
    

class BYearBegin(YearOffset):
    "\n    DateOffset increments between the first business day of the year.\n\n    Examples\n    --------\n    >>> from pandas.tseries.offset import BYearBegin\n    >>> ts = pd.Timestamp('2020-05-24 05:01:15')\n    >>> ts + BYearBegin()\n    Timestamp('2021-01-01 05:01:15')\n    >>> ts - BYearBegin()\n    Timestamp('2020-01-01 05:01:15')\n    >>> ts + BYearBegin(-1)\n    Timestamp('2020-01-01 05:01:15')\n    >>> ts + BYearBegin(2)\n    Timestamp('2022-01-03 05:01:15')\n    "
    def __init__(self, *args, **kwargs) -> None:
        "\n    DateOffset increments between the first business day of the year.\n\n    Examples\n    --------\n    >>> from pandas.tseries.offset import BYearBegin\n    >>> ts = pd.Timestamp('2020-05-24 05:01:15')\n    >>> ts + BYearBegin()\n    Timestamp('2021-01-01 05:01:15')\n    >>> ts - BYearBegin()\n    Timestamp('2020-01-01 05:01:15')\n    >>> ts + BYearBegin(-1)\n    Timestamp('2020-01-01 05:01:15')\n    >>> ts + BYearBegin(2)\n    Timestamp('2022-01-03 05:01:15')\n    "
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    _day_opt: str
    _default_month: int
    @classmethod
    def _from_name(cls) -> typing.Any:
        ...
    
    _outputName: str
    _prefix: str
    def __getattr__(self, name) -> typing.Any:
        ...
    

class BYearEnd(YearOffset):
    "\n    DateOffset increments between the last business day of the year.\n\n    Examples\n    --------\n    >>> from pandas.tseries.offset import BYearEnd\n    >>> ts = pd.Timestamp('2020-05-24 05:01:15')\n    >>> ts - BYearEnd()\n    Timestamp('2019-12-31 05:01:15')\n    >>> ts + BYearEnd()\n    Timestamp('2020-12-31 05:01:15')\n    >>> ts + BYearEnd(3)\n    Timestamp('2022-12-30 05:01:15')\n    >>> ts + BYearEnd(-3)\n    Timestamp('2017-12-29 05:01:15')\n    >>> ts + BYearEnd(month=11)\n    Timestamp('2020-11-30 05:01:15')\n    "
    def __init__(self, *args, **kwargs) -> None:
        "\n    DateOffset increments between the last business day of the year.\n\n    Examples\n    --------\n    >>> from pandas.tseries.offset import BYearEnd\n    >>> ts = pd.Timestamp('2020-05-24 05:01:15')\n    >>> ts - BYearEnd()\n    Timestamp('2019-12-31 05:01:15')\n    >>> ts + BYearEnd()\n    Timestamp('2020-12-31 05:01:15')\n    >>> ts + BYearEnd(3)\n    Timestamp('2022-12-30 05:01:15')\n    >>> ts + BYearEnd(-3)\n    Timestamp('2017-12-29 05:01:15')\n    >>> ts + BYearEnd(month=11)\n    Timestamp('2020-11-30 05:01:15')\n    "
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    _day_opt: str
    _default_month: int
    @classmethod
    def _from_name(cls) -> typing.Any:
        ...
    
    _outputName: str
    _prefix: str
    def __getattr__(self, name) -> typing.Any:
        ...
    

class BaseOffset(_mod_builtins.object):
    '\n    Base class for DateOffset methods that are not overridden by subclasses.\n    '
    def __add__(self, value) -> BaseOffset:
        'Return self+value.'
        ...
    
    def __call__(self, *args, **kwargs) -> typing.Any:
        'Call self as a function.'
        ...
    
    def __eq__(self, value) -> bool:
        'Return self==value.'
        ...
    
    def __ge__(self, value) -> bool:
        'Return self>=value.'
        ...
    
    def __getstate__(self) -> typing.Any:
        '\n        Return a pickleable state\n        '
        ...
    
    def __gt__(self, value) -> bool:
        'Return self>value.'
        ...
    
    def __hash__(self) -> int:
        'Return hash(self).'
        ...
    
    def __init__(self, *args, **kwargs) -> None:
        '\n    Base class for DateOffset methods that are not overridden by subclasses.\n    '
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
    
    def __mul__(self, value) -> BaseOffset:
        'Return self*value.'
        ...
    
    def __ne__(self, value) -> bool:
        'Return self!=value.'
        ...
    
    def __neg__(self) -> BaseOffset:
        '-self'
        ...
    
    def __radd__(self, value) -> BaseOffset:
        'Return value+self.'
        ...
    
    def __reduce_cython__(self) -> typing.Any:
        ...
    
    def __repr__(self) -> str:
        'Return repr(self).'
        ...
    
    def __rmul__(self, value) -> BaseOffset:
        'Return value*self.'
        ...
    
    def __rsub__(self, value) -> BaseOffset:
        'Return value-self.'
        ...
    
    def __setstate__(self, state: typing.Any) -> None:
        '\n        Reconstruct an instance from a pickled state\n        '
        ...
    
    def __setstate_cython__(self) -> typing.Any:
        ...
    
    def __sub__(self, value) -> BaseOffset:
        'Return self-value.'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    _adjust_dst: bool
    def _apply_array(self, other) -> numpy.ndarray:
        ...
    
    _attributes: tuple
    @property
    def _cache(self) -> typing.Any:
        ...
    
    _day_opt: typing.Any
    _deprecations: frozenset
    def _get_offset_day(self) -> typing.Any:
        ...
    
    def _offset_str(self) -> typing.Any:
        ...
    
    _params: _mod_pandas__libs_properties.CachedProperty
    @property
    def _prefix(self) -> typing.Any:
        ...
    
    def _repr_attrs(self) -> typing.Any:
        ...
    
    _use_relativedelta: bool
    @classmethod
    def _validate_n(cls) -> typing.Any:
        '\n        Require that `n` be an integer.\n\n        Parameters\n        ----------\n        n : int\n\n        Returns\n        -------\n        nint : int\n\n        Raises\n        ------\n        TypeError if `int(n)` raises\n        ValueError if n != int(n)\n        '
        ...
    
    def apply_index(self, other) -> typing.Any:
        ...
    
    @property
    def base(self) -> typing.Any:
        '\n        Returns a copy of the calling offset object with n=1 and all other\n        attributes equal.\n        '
        ...
    
    def copy(self) -> typing.Any:
        ...
    
    freqstr: _mod_pandas__libs_properties.CachedProperty
    def isAnchored(self) -> typing.Any:
        ...
    
    def is_anchored(self) -> typing.Any:
        ...
    
    def is_on_offset(self) -> typing.Any:
        ...
    
    @property
    def kwds(self) -> typing.Any:
        ...
    
    @property
    def n(self) -> typing.Any:
        ...
    
    @property
    def name(self) -> typing.Any:
        ...
    
    @property
    def nanos(self) -> typing.Any:
        ...
    
    @property
    def normalize(self) -> typing.Any:
        ...
    
    def onOffset(self) -> typing.Any:
        ...
    
    def rollback(self) -> typing.Any:
        '\n        Roll provided date backward to next offset only if not on offset.\n\n        Returns\n        -------\n        TimeStamp\n            Rolled timestamp if not on offset, otherwise unchanged timestamp.\n        '
        ...
    
    def rollforward(self) -> typing.Any:
        '\n        Roll provided date forward to next offset only if not on offset.\n\n        Returns\n        -------\n        TimeStamp\n            Rolled timestamp if not on offset, otherwise unchanged timestamp.\n        '
        ...
    
    @property
    def rule_code(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class BusinessDay(BusinessMixin):
    '\n    DateOffset subclass representing possibly n business days.\n    '
    def __init__(self, *args, **kwargs) -> None:
        '\n    DateOffset subclass representing possibly n business days.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    def __setstate__(self, state: typing.Any) -> None:
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def _apply_array(self, other) -> numpy.ndarray:
        ...
    
    _attributes: tuple
    @classmethod
    def _from_name(cls) -> typing.Any:
        ...
    
    def _offset_str(self) -> typing.Any:
        ...
    
    _period_dtype_code: int
    _prefix: str
    def apply(self, other) -> typing.Any:
        ...
    
    def apply_index(self, other) -> typing.Any:
        ...
    
    def is_on_offset(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class BusinessHour(BusinessMixin):
    '\n    DateOffset subclass representing possibly n business hours.\n\n    Parameters\n    ----------\n    n : int, default 1\n        The number of months represented.\n    normalize : bool, default False\n        Normalize start/end dates to midnight before generating date range.\n    weekmask : str, Default \'Mon Tue Wed Thu Fri\'\n        Weekmask of valid business days, passed to ``numpy.busdaycalendar``.\n    start : str, default "09:00"\n        Start time of your custom business hour in 24h format.\n    end : str, default: "17:00"\n        End time of your custom business hour in 24h format.\n    '
    def __init__(self, *args, **kwargs) -> None:
        '\n    DateOffset subclass representing possibly n business hours.\n\n    Parameters\n    ----------\n    n : int, default 1\n        The number of months represented.\n    normalize : bool, default False\n        Normalize start/end dates to midnight before generating date range.\n    weekmask : str, Default \'Mon Tue Wed Thu Fri\'\n        Weekmask of valid business days, passed to ``numpy.busdaycalendar``.\n    start : str, default "09:00"\n        Start time of your custom business hour in 24h format.\n    end : str, default: "17:00"\n        End time of your custom business hour in 24h format.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    def __setstate__(self, state: typing.Any) -> None:
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    _adjust_dst: bool
    _anchor: int
    _attributes: tuple
    @classmethod
    def _from_name(cls) -> typing.Any:
        ...
    
    def _get_business_hours_by_sec(self) -> typing.Any:
        '\n        Return business hours in a day by seconds.\n        '
        ...
    
    def _get_closing_time(self) -> typing.Any:
        '\n        Get the closing time of a business hour interval by its opening time.\n\n        Parameters\n        ----------\n        dt : datetime\n            Opening time of a business hour interval.\n\n        Returns\n        -------\n        result : datetime\n            Corresponding closing time.\n        '
        ...
    
    def _is_on_offset(self) -> typing.Any:
        '\n        Slight speedups using calculated values.\n        '
        ...
    
    def _next_opening_time(self) -> typing.Any:
        '\n        If self.n and sign have the same sign, return the earliest opening time\n        later than or equal to current time.\n        Otherwise the latest opening time earlier than or equal to current\n        time.\n\n        Opening time always locates on BusinessDay.\n        However, closing time may not if business hour extends over midnight.\n\n        Parameters\n        ----------\n        other : datetime\n            Current time.\n        sign : int, default 1.\n            Either 1 or -1. Going forward in time if it has the same sign as\n            self.n. Going backward in time otherwise.\n\n        Returns\n        -------\n        result : datetime\n            Next opening time.\n        '
        ...
    
    _prefix: str
    def _prev_opening_time(self) -> typing.Any:
        '\n        If n is positive, return the latest opening time earlier than or equal\n        to current time.\n        Otherwise the earliest opening time later than or equal to current\n        time.\n\n        Parameters\n        ----------\n        other : datetime\n            Current time.\n\n        Returns\n        -------\n        result : datetime\n            Previous opening time.\n        '
        ...
    
    def _repr_attrs(self) -> typing.Any:
        ...
    
    def apply(self, other) -> typing.Any:
        ...
    
    @property
    def end(self) -> typing.Any:
        ...
    
    def is_on_offset(self) -> typing.Any:
        ...
    
    next_bday: _mod_pandas__libs_properties.CachedProperty
    def rollback(self, other) -> typing.Any:
        '\n        Roll provided date backward to next offset only if not on offset.\n        '
        ...
    
    def rollforward(self, other) -> typing.Any:
        '\n        Roll provided date forward to next offset only if not on offset.\n        '
        ...
    
    @property
    def start(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class BusinessMixin(SingleConstructorOffset):
    '\n    Mixin to business types to provide related functions.\n    '
    def __init__(self, *args, **kwargs) -> None:
        '\n    Mixin to business types to provide related functions.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    def __setstate__(self, state: typing.Any) -> None:
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @classmethod
    def _from_name(cls) -> typing.Any:
        ...
    
    def _init_custom(self) -> typing.Any:
        '\n        Additional __init__ for Custom subclasses.\n        '
        ...
    
    @property
    def _offset(self) -> typing.Any:
        ...
    
    def _repr_attrs(self) -> typing.Any:
        ...
    
    @property
    def calendar(self) -> typing.Any:
        ...
    
    @property
    def holidays(self) -> typing.Any:
        ...
    
    @property
    def offset(self) -> typing.Any:
        '\n        Alias for self._offset.\n        '
        ...
    
    @property
    def weekmask(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class BusinessMonthBegin(MonthOffset):
    "\n    DateOffset of one month at the first business day.\n\n    Examples\n    --------\n    >>> from pandas.tseries.offset import BMonthBegin\n    >>> ts=pd.Timestamp('2020-05-24 05:01:15')\n    >>> ts + BMonthBegin()\n    Timestamp('2020-06-01 05:01:15')\n    >>> ts + BMonthBegin(2)\n    Timestamp('2020-07-01 05:01:15')\n    >>> ts + BMonthBegin(-3)\n    Timestamp('2020-03-02 05:01:15')\n    "
    def __init__(self, *args, **kwargs) -> None:
        "\n    DateOffset of one month at the first business day.\n\n    Examples\n    --------\n    >>> from pandas.tseries.offset import BMonthBegin\n    >>> ts=pd.Timestamp('2020-05-24 05:01:15')\n    >>> ts + BMonthBegin()\n    Timestamp('2020-06-01 05:01:15')\n    >>> ts + BMonthBegin(2)\n    Timestamp('2020-07-01 05:01:15')\n    >>> ts + BMonthBegin(-3)\n    Timestamp('2020-03-02 05:01:15')\n    "
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    _day_opt: str
    @classmethod
    def _from_name(cls) -> typing.Any:
        ...
    
    _prefix: str
    def __getattr__(self, name) -> typing.Any:
        ...
    

class BusinessMonthEnd(MonthOffset):
    "\n    DateOffset increments between the last business day of the month\n\n    Examples\n    --------\n    >>> from pandas.tseries.offset import BMonthEnd\n    >>> ts = pd.Timestamp('2020-05-24 05:01:15')\n    >>> ts + BMonthEnd()\n    Timestamp('2020-05-29 05:01:15')\n    >>> ts + BMonthEnd(2)\n    Timestamp('2020-06-30 05:01:15')\n    >>> ts + BMonthEnd(-2)\n    Timestamp('2020-03-31 05:01:15')\n    "
    def __init__(self, *args, **kwargs) -> None:
        "\n    DateOffset increments between the last business day of the month\n\n    Examples\n    --------\n    >>> from pandas.tseries.offset import BMonthEnd\n    >>> ts = pd.Timestamp('2020-05-24 05:01:15')\n    >>> ts + BMonthEnd()\n    Timestamp('2020-05-29 05:01:15')\n    >>> ts + BMonthEnd(2)\n    Timestamp('2020-06-30 05:01:15')\n    >>> ts + BMonthEnd(-2)\n    Timestamp('2020-03-31 05:01:15')\n    "
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    _day_opt: str
    @classmethod
    def _from_name(cls) -> typing.Any:
        ...
    
    _prefix: str
    def __getattr__(self, name) -> typing.Any:
        ...
    

CBMonthBegin: CustomBusinessMonthBegin
CBMonthEnd: CustomBusinessMonthEnd
CDay: CustomBusinessDay
class CustomBusinessDay(BusinessDay):
    "\n    DateOffset subclass representing custom business days excluding holidays.\n\n    Parameters\n    ----------\n    n : int, default 1\n    normalize : bool, default False\n        Normalize start/end dates to midnight before generating date range.\n    weekmask : str, Default 'Mon Tue Wed Thu Fri'\n        Weekmask of valid business days, passed to ``numpy.busdaycalendar``.\n    holidays : list\n        List/array of dates to exclude from the set of valid business days,\n        passed to ``numpy.busdaycalendar``.\n    calendar : pd.HolidayCalendar or np.busdaycalendar\n    offset : timedelta, default timedelta(0)\n    "
    def __init__(self, *args, **kwargs) -> None:
        "\n    DateOffset subclass representing custom business days excluding holidays.\n\n    Parameters\n    ----------\n    n : int, default 1\n    normalize : bool, default False\n        Normalize start/end dates to midnight before generating date range.\n    weekmask : str, Default 'Mon Tue Wed Thu Fri'\n        Weekmask of valid business days, passed to ``numpy.busdaycalendar``.\n    holidays : list\n        List/array of dates to exclude from the set of valid business days,\n        passed to ``numpy.busdaycalendar``.\n    calendar : pd.HolidayCalendar or np.busdaycalendar\n    offset : timedelta, default timedelta(0)\n    "
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    def __setstate__(self, state: typing.Any) -> None:
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def _apply_array(self) -> typing.Any:
        ...
    
    _attributes: tuple
    @classmethod
    def _from_name(cls) -> typing.Any:
        ...
    
    _prefix: str
    def apply(self, other) -> typing.Any:
        ...
    
    def apply_index(self) -> typing.Any:
        ...
    
    def is_on_offset(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class CustomBusinessHour(BusinessHour):
    '\n    DateOffset subclass representing possibly n custom business days.\n\n    Parameters\n    ----------\n    n : int, default 1\n        The number of months represented.\n    normalize : bool, default False\n        Normalize start/end dates to midnight before generating date range.\n    weekmask : str, Default \'Mon Tue Wed Thu Fri\'\n        Weekmask of valid business days, passed to ``numpy.busdaycalendar``.\n    start : str, default "09:00"\n        Start time of your custom business hour in 24h format.\n    end : str, default: "17:00"\n        End time of your custom business hour in 24h format.\n    '
    def __init__(self, *args, **kwargs) -> None:
        '\n    DateOffset subclass representing possibly n custom business days.\n\n    Parameters\n    ----------\n    n : int, default 1\n        The number of months represented.\n    normalize : bool, default False\n        Normalize start/end dates to midnight before generating date range.\n    weekmask : str, Default \'Mon Tue Wed Thu Fri\'\n        Weekmask of valid business days, passed to ``numpy.busdaycalendar``.\n    start : str, default "09:00"\n        Start time of your custom business hour in 24h format.\n    end : str, default: "17:00"\n        End time of your custom business hour in 24h format.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    _attributes: tuple
    @classmethod
    def _from_name(cls) -> typing.Any:
        ...
    
    _prefix: str
    def __getattr__(self, name) -> typing.Any:
        ...
    

class CustomBusinessMonthBegin(_CustomBusinessMonth):
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @classmethod
    def _from_name(cls) -> typing.Any:
        ...
    
    _prefix: str
    def __getattr__(self, name) -> typing.Any:
        ...
    

class CustomBusinessMonthEnd(_CustomBusinessMonth):
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @classmethod
    def _from_name(cls) -> typing.Any:
        ...
    
    _prefix: str
    def __getattr__(self, name) -> typing.Any:
        ...
    

class DateOffset(RelativeDeltaOffset):
    "\n    Standard kind of date increment used for a date range.\n\n    Works exactly like relativedelta in terms of the keyword args you\n    pass in, use of the keyword n is discouraged-- you would be better\n    off specifying n in the keywords you use, but regardless it is\n    there for you. n is needed for DateOffset subclasses.\n\n    DateOffset work as follows.  Each offset specify a set of dates\n    that conform to the DateOffset.  For example, Bday defines this\n    set to be the set of dates that are weekdays (M-F).  To test if a\n    date is in the set of a DateOffset dateOffset we can use the\n    is_on_offset method: dateOffset.is_on_offset(date).\n\n    If a date is not on a valid date, the rollback and rollforward\n    methods can be used to roll the date to the nearest valid date\n    before/after the date.\n\n    DateOffsets can be created to move dates forward a given number of\n    valid dates.  For example, Bday(2) can be added to a date to move\n    it two business days forward.  If the date does not start on a\n    valid date, first it is moved to a valid date.  Thus pseudo code\n    is:\n\n    def __add__(date):\n      date = rollback(date) # does nothing if date is valid\n      return date + <n number of periods>\n\n    When a date offset is created for a negative number of periods,\n    the date is first rolled forward.  The pseudo code is:\n\n    def __add__(date):\n      date = rollforward(date) # does nothing is date is valid\n      return date + <n number of periods>\n\n    Zero presents a problem.  Should it roll forward or back?  We\n    arbitrarily have it rollforward:\n\n    date + BDay(0) == BDay.rollforward(date)\n\n    Since 0 is a bit weird, we suggest avoiding its use.\n\n    Parameters\n    ----------\n    n : int, default 1\n        The number of time periods the offset represents.\n    normalize : bool, default False\n        Whether to round the result of a DateOffset addition down to the\n        previous midnight.\n    **kwds\n        Temporal parameter that add to or replace the offset value.\n\n        Parameters that **add** to the offset (like Timedelta):\n\n        - years\n        - months\n        - weeks\n        - days\n        - hours\n        - minutes\n        - seconds\n        - microseconds\n        - nanoseconds\n\n        Parameters that **replace** the offset value:\n\n        - year\n        - month\n        - day\n        - weekday\n        - hour\n        - minute\n        - second\n        - microsecond\n        - nanosecond.\n\n    See Also\n    --------\n    dateutil.relativedelta.relativedelta : The relativedelta type is designed\n        to be applied to an existing datetime an can replace specific components of\n        that datetime, or represents an interval of time.\n\n    Examples\n    --------\n    >>> from pandas.tseries.offsets import DateOffset\n    >>> ts = pd.Timestamp('2017-01-01 09:10:11')\n    >>> ts + DateOffset(months=3)\n    Timestamp('2017-04-01 09:10:11')\n\n    >>> ts = pd.Timestamp('2017-01-01 09:10:11')\n    >>> ts + DateOffset(months=2)\n    Timestamp('2017-03-01 09:10:11')\n    "
    __class__: OffsetMeta
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, *args, **kwargs) -> None:
        "\n    Standard kind of date increment used for a date range.\n\n    Works exactly like relativedelta in terms of the keyword args you\n    pass in, use of the keyword n is discouraged-- you would be better\n    off specifying n in the keywords you use, but regardless it is\n    there for you. n is needed for DateOffset subclasses.\n\n    DateOffset work as follows.  Each offset specify a set of dates\n    that conform to the DateOffset.  For example, Bday defines this\n    set to be the set of dates that are weekdays (M-F).  To test if a\n    date is in the set of a DateOffset dateOffset we can use the\n    is_on_offset method: dateOffset.is_on_offset(date).\n\n    If a date is not on a valid date, the rollback and rollforward\n    methods can be used to roll the date to the nearest valid date\n    before/after the date.\n\n    DateOffsets can be created to move dates forward a given number of\n    valid dates.  For example, Bday(2) can be added to a date to move\n    it two business days forward.  If the date does not start on a\n    valid date, first it is moved to a valid date.  Thus pseudo code\n    is:\n\n    def __add__(date):\n      date = rollback(date) # does nothing if date is valid\n      return date + <n number of periods>\n\n    When a date offset is created for a negative number of periods,\n    the date is first rolled forward.  The pseudo code is:\n\n    def __add__(date):\n      date = rollforward(date) # does nothing is date is valid\n      return date + <n number of periods>\n\n    Zero presents a problem.  Should it roll forward or back?  We\n    arbitrarily have it rollforward:\n\n    date + BDay(0) == BDay.rollforward(date)\n\n    Since 0 is a bit weird, we suggest avoiding its use.\n\n    Parameters\n    ----------\n    n : int, default 1\n        The number of time periods the offset represents.\n    normalize : bool, default False\n        Whether to round the result of a DateOffset addition down to the\n        previous midnight.\n    **kwds\n        Temporal parameter that add to or replace the offset value.\n\n        Parameters that **add** to the offset (like Timedelta):\n\n        - years\n        - months\n        - weeks\n        - days\n        - hours\n        - minutes\n        - seconds\n        - microseconds\n        - nanoseconds\n\n        Parameters that **replace** the offset value:\n\n        - year\n        - month\n        - day\n        - weekday\n        - hour\n        - minute\n        - second\n        - microsecond\n        - nanosecond.\n\n    See Also\n    --------\n    dateutil.relativedelta.relativedelta : The relativedelta type is designed\n        to be applied to an existing datetime an can replace specific components of\n        that datetime, or represents an interval of time.\n\n    Examples\n    --------\n    >>> from pandas.tseries.offsets import DateOffset\n    >>> ts = pd.Timestamp('2017-01-01 09:10:11')\n    >>> ts + DateOffset(months=3)\n    Timestamp('2017-04-01 09:10:11')\n\n    >>> ts = pd.Timestamp('2017-01-01 09:10:11')\n    >>> ts + DateOffset(months=2)\n    Timestamp('2017-03-01 09:10:11')\n    "
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __setattr__(self, name, value) -> None:
        ...
    
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
    

class Day(Tick):
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @classmethod
    def _from_name(cls) -> typing.Any:
        ...
    
    _nanos_inc: int
    _period_dtype_code: int
    _prefix: str
    def __getattr__(self, name) -> typing.Any:
        ...
    

class Easter(SingleConstructorOffset):
    '\n    DateOffset for the Easter holiday using logic defined in dateutil.\n\n    Right now uses the revised method which is valid in years 1583-4099.\n    '
    def __init__(self, *args, **kwargs) -> None:
        '\n    DateOffset for the Easter holiday using logic defined in dateutil.\n\n    Right now uses the revised method which is valid in years 1583-4099.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    def __setstate__(self, state: typing.Any) -> None:
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @classmethod
    def _from_name(cls) -> typing.Any:
        ...
    
    def apply(self, other) -> typing.Any:
        ...
    
    def is_on_offset(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class FY5253(FY5253Mixin):
    '\n    Describes 52-53 week fiscal year. This is also known as a 4-4-5 calendar.\n\n    It is used by companies that desire that their\n    fiscal year always end on the same day of the week.\n\n    It is a method of managing accounting periods.\n    It is a common calendar structure for some industries,\n    such as retail, manufacturing and parking industry.\n\n    For more information see:\n    https://en.wikipedia.org/wiki/4-4-5_calendar\n\n    The year may either:\n\n    - end on the last X day of the Y month.\n    - end on the last X day closest to the last day of the Y month.\n\n    X is a specific day of the week.\n    Y is a certain month of the year\n\n    Parameters\n    ----------\n    n : int\n    weekday : int {0, 1, ..., 6}, default 0\n        A specific integer for the day of the week.\n\n        - 0 is Monday\n        - 1 is Tuesday\n        - 2 is Wednesday\n        - 3 is Thursday\n        - 4 is Friday\n        - 5 is Saturday\n        - 6 is Sunday.\n\n    startingMonth : int {1, 2, ... 12}, default 1\n        The month in which the fiscal year ends.\n\n    variation : str, default "nearest"\n        Method of employing 4-4-5 calendar.\n\n        There are two options:\n\n        - "nearest" means year end is **weekday** closest to last day of month in year.\n        - "last" means year end is final **weekday** of the final month in fiscal year.\n    '
    def __init__(self, *args, **kwargs) -> None:
        '\n    Describes 52-53 week fiscal year. This is also known as a 4-4-5 calendar.\n\n    It is used by companies that desire that their\n    fiscal year always end on the same day of the week.\n\n    It is a method of managing accounting periods.\n    It is a common calendar structure for some industries,\n    such as retail, manufacturing and parking industry.\n\n    For more information see:\n    https://en.wikipedia.org/wiki/4-4-5_calendar\n\n    The year may either:\n\n    - end on the last X day of the Y month.\n    - end on the last X day closest to the last day of the Y month.\n\n    X is a specific day of the week.\n    Y is a certain month of the year\n\n    Parameters\n    ----------\n    n : int\n    weekday : int {0, 1, ..., 6}, default 0\n        A specific integer for the day of the week.\n\n        - 0 is Monday\n        - 1 is Tuesday\n        - 2 is Wednesday\n        - 3 is Thursday\n        - 4 is Friday\n        - 5 is Saturday\n        - 6 is Sunday.\n\n    startingMonth : int {1, 2, ... 12}, default 1\n        The month in which the fiscal year ends.\n\n    variation : str, default "nearest"\n        Method of employing 4-4-5 calendar.\n\n        There are two options:\n\n        - "nearest" means year end is **weekday** closest to last day of month in year.\n        - "last" means year end is final **weekday** of the final month in fiscal year.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    _attributes: tuple
    @classmethod
    def _from_name(cls) -> typing.Any:
        ...
    
    @classmethod
    def _parse_suffix(cls) -> typing.Any:
        ...
    
    _prefix: str
    def apply(self, other) -> typing.Any:
        ...
    
    def get_year_end(self) -> typing.Any:
        ...
    
    def is_on_offset(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class FY5253Mixin(SingleConstructorOffset):
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    def __setstate__(self, state: typing.Any) -> None:
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @classmethod
    def _from_name(cls) -> typing.Any:
        ...
    
    def _get_suffix_prefix(self) -> typing.Any:
        ...
    
    def get_rule_code_suffix(self) -> typing.Any:
        ...
    
    def is_anchored(self) -> typing.Any:
        ...
    
    @property
    def rule_code(self) -> typing.Any:
        ...
    
    @property
    def startingMonth(self) -> typing.Any:
        ...
    
    @property
    def variation(self) -> typing.Any:
        ...
    
    @property
    def weekday(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class FY5253Quarter(FY5253Mixin):
    '\n    DateOffset increments between business quarter dates\n    for 52-53 week fiscal year (also known as a 4-4-5 calendar).\n\n    It is used by companies that desire that their\n    fiscal year always end on the same day of the week.\n\n    It is a method of managing accounting periods.\n    It is a common calendar structure for some industries,\n    such as retail, manufacturing and parking industry.\n\n    For more information see:\n    https://en.wikipedia.org/wiki/4-4-5_calendar\n\n    The year may either:\n\n    - end on the last X day of the Y month.\n    - end on the last X day closest to the last day of the Y month.\n\n    X is a specific day of the week.\n    Y is a certain month of the year\n\n    startingMonth = 1 corresponds to dates like 1/31/2007, 4/30/2007, ...\n    startingMonth = 2 corresponds to dates like 2/28/2007, 5/31/2007, ...\n    startingMonth = 3 corresponds to dates like 3/30/2007, 6/29/2007, ...\n\n    Parameters\n    ----------\n    n : int\n    weekday : int {0, 1, ..., 6}, default 0\n        A specific integer for the day of the week.\n\n        - 0 is Monday\n        - 1 is Tuesday\n        - 2 is Wednesday\n        - 3 is Thursday\n        - 4 is Friday\n        - 5 is Saturday\n        - 6 is Sunday.\n\n    startingMonth : int {1, 2, ..., 12}, default 1\n        The month in which fiscal years end.\n\n    qtr_with_extra_week : int {1, 2, 3, 4}, default 1\n        The quarter number that has the leap or 14 week when needed.\n\n    variation : str, default "nearest"\n        Method of employing 4-4-5 calendar.\n\n        There are two options:\n\n        - "nearest" means year end is **weekday** closest to last day of month in year.\n        - "last" means year end is final **weekday** of the final month in fiscal year.\n    '
    def __init__(self, *args, **kwargs) -> None:
        '\n    DateOffset increments between business quarter dates\n    for 52-53 week fiscal year (also known as a 4-4-5 calendar).\n\n    It is used by companies that desire that their\n    fiscal year always end on the same day of the week.\n\n    It is a method of managing accounting periods.\n    It is a common calendar structure for some industries,\n    such as retail, manufacturing and parking industry.\n\n    For more information see:\n    https://en.wikipedia.org/wiki/4-4-5_calendar\n\n    The year may either:\n\n    - end on the last X day of the Y month.\n    - end on the last X day closest to the last day of the Y month.\n\n    X is a specific day of the week.\n    Y is a certain month of the year\n\n    startingMonth = 1 corresponds to dates like 1/31/2007, 4/30/2007, ...\n    startingMonth = 2 corresponds to dates like 2/28/2007, 5/31/2007, ...\n    startingMonth = 3 corresponds to dates like 3/30/2007, 6/29/2007, ...\n\n    Parameters\n    ----------\n    n : int\n    weekday : int {0, 1, ..., 6}, default 0\n        A specific integer for the day of the week.\n\n        - 0 is Monday\n        - 1 is Tuesday\n        - 2 is Wednesday\n        - 3 is Thursday\n        - 4 is Friday\n        - 5 is Saturday\n        - 6 is Sunday.\n\n    startingMonth : int {1, 2, ..., 12}, default 1\n        The month in which fiscal years end.\n\n    qtr_with_extra_week : int {1, 2, 3, 4}, default 1\n        The quarter number that has the leap or 14 week when needed.\n\n    variation : str, default "nearest"\n        Method of employing 4-4-5 calendar.\n\n        There are two options:\n\n        - "nearest" means year end is **weekday** closest to last day of month in year.\n        - "last" means year end is final **weekday** of the final month in fiscal year.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    def __setstate__(self, state: typing.Any) -> None:
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    _attributes: tuple
    @classmethod
    def _from_name(cls) -> typing.Any:
        ...
    
    _offset: _mod_pandas__libs_properties.CachedProperty
    _prefix: str
    def _rollback_to_year(self) -> typing.Any:
        '\n        Roll `other` back to the most recent date that was on a fiscal year\n        end.\n\n        Return the date of that year-end, the number of full quarters\n        elapsed between that year-end and other, and the remaining Timedelta\n        since the most recent quarter-end.\n\n        Parameters\n        ----------\n        other : datetime or Timestamp\n\n        Returns\n        -------\n        tuple of\n        prev_year_end : Timestamp giving most recent fiscal year end\n        num_qtrs : int\n        tdelta : Timedelta\n        '
        ...
    
    def apply(self, other) -> typing.Any:
        ...
    
    def get_weeks(self) -> typing.Any:
        ...
    
    def is_on_offset(self) -> typing.Any:
        ...
    
    @property
    def qtr_with_extra_week(self) -> typing.Any:
        ...
    
    @property
    def rule_code(self) -> typing.Any:
        ...
    
    def year_has_extra_week(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class Hour(Tick):
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @classmethod
    def _from_name(cls) -> typing.Any:
        ...
    
    _nanos_inc: int
    _period_dtype_code: int
    _prefix: str
    def __getattr__(self, name) -> typing.Any:
        ...
    

INVALID_FREQ_ERR_MSG: str
class LastWeekOfMonth(WeekOfMonthMixin):
    '\n    Describes monthly dates in last week of month like "the last Tuesday of\n    each month".\n\n    Parameters\n    ----------\n    n : int, default 1\n    weekday : int {0, 1, ..., 6}, default 0\n        A specific integer for the day of the week.\n\n        - 0 is Monday\n        - 1 is Tuesday\n        - 2 is Wednesday\n        - 3 is Thursday\n        - 4 is Friday\n        - 5 is Saturday\n        - 6 is Sunday.\n    '
    def __init__(self, *args, **kwargs) -> None:
        '\n    Describes monthly dates in last week of month like "the last Tuesday of\n    each month".\n\n    Parameters\n    ----------\n    n : int, default 1\n    weekday : int {0, 1, ..., 6}, default 0\n        A specific integer for the day of the week.\n\n        - 0 is Monday\n        - 1 is Tuesday\n        - 2 is Wednesday\n        - 3 is Thursday\n        - 4 is Friday\n        - 5 is Saturday\n        - 6 is Sunday.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    def __setstate__(self, state: typing.Any) -> None:
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    _attributes: tuple
    @classmethod
    def _from_name(cls) -> typing.Any:
        ...
    
    def _get_offset_day(self) -> typing.Any:
        '\n        Find the day in the same month as other that has the same\n        weekday as self.weekday and is the last such day in the month.\n\n        Parameters\n        ----------\n        other: datetime\n\n        Returns\n        -------\n        day: int\n        '
        ...
    
    _prefix: str
    def __getattr__(self, name) -> typing.Any:
        ...
    

MONTH_ALIASES: dict
MONTH_TO_CAL_NUM: dict
class Micro(Tick):
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @classmethod
    def _from_name(cls) -> typing.Any:
        ...
    
    _nanos_inc: int
    _period_dtype_code: int
    _prefix: str
    def __getattr__(self, name) -> typing.Any:
        ...
    

class Milli(Tick):
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @classmethod
    def _from_name(cls) -> typing.Any:
        ...
    
    _nanos_inc: int
    _period_dtype_code: int
    _prefix: str
    def __getattr__(self, name) -> typing.Any:
        ...
    

class Minute(Tick):
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @classmethod
    def _from_name(cls) -> typing.Any:
        ...
    
    _nanos_inc: int
    _period_dtype_code: int
    _prefix: str
    def __getattr__(self, name) -> typing.Any:
        ...
    

class MonthBegin(MonthOffset):
    '\n    DateOffset of one month at beginning.\n    '
    def __init__(self, *args, **kwargs) -> None:
        '\n    DateOffset of one month at beginning.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    _day_opt: str
    @classmethod
    def _from_name(cls) -> typing.Any:
        ...
    
    _prefix: str
    def __getattr__(self, name) -> typing.Any:
        ...
    

class MonthEnd(MonthOffset):
    '\n    DateOffset of one month end.\n    '
    def __init__(self, *args, **kwargs) -> None:
        '\n    DateOffset of one month end.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    _day_opt: str
    @classmethod
    def _from_name(cls) -> typing.Any:
        ...
    
    _period_dtype_code: int
    _prefix: str
    def __getattr__(self, name) -> typing.Any:
        ...
    

class MonthOffset(SingleConstructorOffset):
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    def __setstate__(self, state: typing.Any) -> None:
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def _apply_array(self, other) -> numpy.ndarray:
        ...
    
    @classmethod
    def _from_name(cls) -> typing.Any:
        ...
    
    def apply(self, other) -> typing.Any:
        ...
    
    def apply_index(self, other) -> typing.Any:
        ...
    
    def is_on_offset(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class Nano(Tick):
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @classmethod
    def _from_name(cls) -> typing.Any:
        ...
    
    _nanos_inc: int
    _period_dtype_code: int
    _prefix: str
    def __getattr__(self, name) -> typing.Any:
        ...
    

class OffsetMeta(_mod_builtins.type):
    '\n    Metaclass that allows us to pretend that all BaseOffset subclasses\n    inherit from DateOffset (which is needed for backward-compatibility).\n    '
    __base__ = _mod_builtins.type
    __bases__: typing.Tuple[type, ...]
    __basicsize__: int
    __dict__: typing.Dict[str, typing.Any]
    __dictoffset__: int
    __flags__: int
    def __init__(self, *args, **kwargs) -> None:
        '\n    Metaclass that allows us to pretend that all BaseOffset subclasses\n    inherit from DateOffset (which is needed for backward-compatibility).\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __instancecheck__(self, cls, obj) -> bool:
        ...
    
    __module__: str
    __mro__: typing.Tuple[type, ...]
    __name__: str
    @classmethod
    def __prepare__(cls, name: str, bases: typing.Tuple[type, ...], **kwds: typing.Any) -> typing.Dict[typing.Any, typing.Any]:
        '__prepare__() -> dict\nused to create the namespace for the class statement'
        ...
    
    __qualname__: str
    def __subclasscheck__(self, cls, obj) -> bool:
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    __weakrefoffset__: int
    def __getattr__(self, name) -> typing.Any:
        ...
    

class QuarterBegin(QuarterOffset):
    '\n    DateOffset increments between Quarter start dates.\n\n    startingMonth = 1 corresponds to dates like 1/01/2007, 4/01/2007, ...\n    startingMonth = 2 corresponds to dates like 2/01/2007, 5/01/2007, ...\n    startingMonth = 3 corresponds to dates like 3/01/2007, 6/01/2007, ...\n    '
    def __init__(self, *args, **kwargs) -> None:
        '\n    DateOffset increments between Quarter start dates.\n\n    startingMonth = 1 corresponds to dates like 1/01/2007, 4/01/2007, ...\n    startingMonth = 2 corresponds to dates like 2/01/2007, 5/01/2007, ...\n    startingMonth = 3 corresponds to dates like 3/01/2007, 6/01/2007, ...\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    _day_opt: str
    _default_starting_month: int
    @classmethod
    def _from_name(cls) -> typing.Any:
        ...
    
    _from_name_starting_month: int
    _prefix: str
    def __getattr__(self, name) -> typing.Any:
        ...
    

class QuarterEnd(QuarterOffset):
    '\n    DateOffset increments between Quarter end dates.\n\n    startingMonth = 1 corresponds to dates like 1/31/2007, 4/30/2007, ...\n    startingMonth = 2 corresponds to dates like 2/28/2007, 5/31/2007, ...\n    startingMonth = 3 corresponds to dates like 3/31/2007, 6/30/2007, ...\n    '
    def __init__(self, *args, **kwargs) -> None:
        '\n    DateOffset increments between Quarter end dates.\n\n    startingMonth = 1 corresponds to dates like 1/31/2007, 4/30/2007, ...\n    startingMonth = 2 corresponds to dates like 2/28/2007, 5/31/2007, ...\n    startingMonth = 3 corresponds to dates like 3/31/2007, 6/30/2007, ...\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    _day_opt: str
    _default_starting_month: int
    @classmethod
    def _from_name(cls) -> typing.Any:
        ...
    
    @property
    def _period_dtype_code(self) -> typing.Any:
        ...
    
    _prefix: str
    def __getattr__(self, name) -> typing.Any:
        ...
    

class QuarterOffset(SingleConstructorOffset):
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    def __setstate__(self, state: typing.Any) -> None:
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def _apply_array(self, other) -> numpy.ndarray:
        ...
    
    _attributes: tuple
    @classmethod
    def _from_name(cls) -> typing.Any:
        ...
    
    def apply(self, other) -> typing.Any:
        ...
    
    def apply_index(self, other) -> typing.Any:
        ...
    
    def is_anchored(self) -> typing.Any:
        ...
    
    def is_on_offset(self) -> typing.Any:
        ...
    
    @property
    def rule_code(self) -> typing.Any:
        ...
    
    @property
    def startingMonth(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class RelativeDeltaOffset(BaseOffset):
    '\n    DateOffset subclass backed by a dateutil relativedelta object.\n    '
    def __getstate__(self) -> typing.Any:
        '\n        Return a pickleable state\n        '
        ...
    
    def __init__(self, *args, **kwargs) -> None:
        '\n    DateOffset subclass backed by a dateutil relativedelta object.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __reduce_cython__(self) -> typing.Any:
        ...
    
    def __setstate__(self, state: typing.Any) -> None:
        '\n        Reconstruct an instance from a pickled state\n        '
        ...
    
    def __setstate_cython__(self) -> typing.Any:
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    _adjust_dst: bool
    def _apply_array(self, other) -> numpy.ndarray:
        ...
    
    _attributes: tuple
    def apply(self, other) -> typing.Any:
        ...
    
    def apply_index(self, other) -> typing.Any:
        ...
    
    def is_on_offset(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class Second(Tick):
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @classmethod
    def _from_name(cls) -> typing.Any:
        ...
    
    _nanos_inc: int
    _period_dtype_code: int
    _prefix: str
    def __getattr__(self, name) -> typing.Any:
        ...
    

class SemiMonthBegin(SemiMonthOffset):
    "\n    Two DateOffset's per month repeating on the first\n    day of the month and day_of_month.\n\n    Parameters\n    ----------\n    n : int\n    normalize : bool, default False\n    day_of_month : int, {2, 3,...,27}, default 15\n    "
    def __init__(self, *args, **kwargs) -> None:
        "\n    Two DateOffset's per month repeating on the first\n    day of the month and day_of_month.\n\n    Parameters\n    ----------\n    n : int\n    normalize : bool, default False\n    day_of_month : int, {2, 3,...,27}, default 15\n    "
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @classmethod
    def _from_name(cls) -> typing.Any:
        ...
    
    _prefix: str
    def is_on_offset(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class SemiMonthEnd(SemiMonthOffset):
    "\n    Two DateOffset's per month repeating on the last\n    day of the month and day_of_month.\n\n    Parameters\n    ----------\n    n : int\n    normalize : bool, default False\n    day_of_month : int, {1, 3,...,27}, default 15\n    "
    def __init__(self, *args, **kwargs) -> None:
        "\n    Two DateOffset's per month repeating on the last\n    day of the month and day_of_month.\n\n    Parameters\n    ----------\n    n : int\n    normalize : bool, default False\n    day_of_month : int, {1, 3,...,27}, default 15\n    "
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @classmethod
    def _from_name(cls) -> typing.Any:
        ...
    
    _min_day_of_month: int
    _prefix: str
    def is_on_offset(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class SemiMonthOffset(SingleConstructorOffset):
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    def __setstate__(self, state: typing.Any) -> None:
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def _apply_array(self, other) -> numpy.ndarray:
        ...
    
    _attributes: tuple
    _default_day_of_month: int
    @classmethod
    def _from_name(cls) -> typing.Any:
        ...
    
    _min_day_of_month: int
    def apply(self, other) -> typing.Any:
        ...
    
    def apply_index(self, other) -> typing.Any:
        ...
    
    @property
    def day_of_month(self) -> typing.Any:
        ...
    
    @property
    def rule_code(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class SingleConstructorOffset(BaseOffset):
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __reduce__(self) -> typing.Union[str, typing.Tuple[typing.Any, ...]]:
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @classmethod
    def _from_name(cls) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class Tick(SingleConstructorOffset):
    def __add__(self, value) -> Tick:
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
    
    def __mul__(self, value) -> Tick:
        'Return self*value.'
        ...
    
    def __ne__(self, value) -> bool:
        'Return self!=value.'
        ...
    
    __pyx_vtable__: PyCapsule
    def __radd__(self, value) -> Tick:
        'Return value+self.'
        ...
    
    def __rmul__(self, value) -> Tick:
        'Return value*self.'
        ...
    
    def __rtruediv__(self, value) -> Tick:
        'Return value/self.'
        ...
    
    def __setstate__(self, state: typing.Any) -> None:
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __truediv__(self, value) -> float:
        'Return self/value.'
        ...
    
    _adjust_dst: bool
    _attributes: tuple
    @classmethod
    def _from_name(cls) -> typing.Any:
        ...
    
    def _next_higher_resolution(self) -> typing.Any:
        ...
    
    _prefix: str
    def _repr_attrs(self) -> typing.Any:
        ...
    
    def apply(self) -> typing.Any:
        ...
    
    @property
    def delta(self) -> typing.Any:
        ...
    
    def is_anchored(self) -> typing.Any:
        ...
    
    def is_on_offset(self) -> typing.Any:
        ...
    
    @property
    def nanos(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

Timedelta = _mod_pandas__libs_tslibs_timedeltas.Timedelta
Timestamp = _mod_pandas__libs_tslibs_timestamps.Timestamp
class Week(SingleConstructorOffset):
    '\n    Weekly offset.\n\n    Parameters\n    ----------\n    weekday : int or None, default None\n        Always generate specific day of week. 0 for Monday.\n    '
    def __init__(self, *args, **kwargs) -> None:
        '\n    Weekly offset.\n\n    Parameters\n    ----------\n    weekday : int or None, default None\n        Always generate specific day of week. 0 for Monday.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    def __setstate__(self, state: typing.Any) -> None:
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def _apply_array(self, other) -> numpy.ndarray:
        ...
    
    _attributes: tuple
    @classmethod
    def _from_name(cls) -> typing.Any:
        ...
    
    _inc: _mod_datetime.timedelta
    @property
    def _period_dtype_code(self) -> typing.Any:
        ...
    
    _prefix: str
    def apply(self, other) -> typing.Any:
        ...
    
    def apply_index(self, other) -> typing.Any:
        ...
    
    def is_anchored(self) -> typing.Any:
        ...
    
    def is_on_offset(self) -> typing.Any:
        ...
    
    @property
    def rule_code(self) -> typing.Any:
        ...
    
    @property
    def weekday(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class WeekOfMonth(WeekOfMonthMixin):
    '\n    Describes monthly dates like "the Tuesday of the 2nd week of each month".\n\n    Parameters\n    ----------\n    n : int\n    week : int {0, 1, 2, 3, ...}, default 0\n        A specific integer for the week of the month.\n        e.g. 0 is 1st week of month, 1 is the 2nd week, etc.\n    weekday : int {0, 1, ..., 6}, default 0\n        A specific integer for the day of the week.\n\n        - 0 is Monday\n        - 1 is Tuesday\n        - 2 is Wednesday\n        - 3 is Thursday\n        - 4 is Friday\n        - 5 is Saturday\n        - 6 is Sunday.\n    '
    def __init__(self, *args, **kwargs) -> None:
        '\n    Describes monthly dates like "the Tuesday of the 2nd week of each month".\n\n    Parameters\n    ----------\n    n : int\n    week : int {0, 1, 2, 3, ...}, default 0\n        A specific integer for the week of the month.\n        e.g. 0 is 1st week of month, 1 is the 2nd week, etc.\n    weekday : int {0, 1, ..., 6}, default 0\n        A specific integer for the day of the week.\n\n        - 0 is Monday\n        - 1 is Tuesday\n        - 2 is Wednesday\n        - 3 is Thursday\n        - 4 is Friday\n        - 5 is Saturday\n        - 6 is Sunday.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    def __setstate__(self, state: typing.Any) -> None:
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    _attributes: tuple
    @classmethod
    def _from_name(cls) -> typing.Any:
        ...
    
    def _get_offset_day(self) -> typing.Any:
        "\n        Find the day in the same month as other that has the same\n        weekday as self.weekday and is the self.week'th such day in the month.\n\n        Parameters\n        ----------\n        other : datetime\n\n        Returns\n        -------\n        day : int\n        "
        ...
    
    _prefix: str
    def __getattr__(self, name) -> typing.Any:
        ...
    

class WeekOfMonthMixin(SingleConstructorOffset):
    '\n    Mixin for methods common to WeekOfMonth and LastWeekOfMonth.\n    '
    def __init__(self, *args, **kwargs) -> None:
        '\n    Mixin for methods common to WeekOfMonth and LastWeekOfMonth.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @classmethod
    def _from_name(cls) -> typing.Any:
        ...
    
    def apply(self, other) -> typing.Any:
        ...
    
    def is_on_offset(self) -> typing.Any:
        ...
    
    @property
    def rule_code(self) -> typing.Any:
        ...
    
    @property
    def week(self) -> typing.Any:
        ...
    
    @property
    def weekday(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class YearBegin(YearOffset):
    '\n    DateOffset increments between calendar year begin dates.\n    '
    def __init__(self, *args, **kwargs) -> None:
        '\n    DateOffset increments between calendar year begin dates.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    _day_opt: str
    _default_month: int
    @classmethod
    def _from_name(cls) -> typing.Any:
        ...
    
    _prefix: str
    def __getattr__(self, name) -> typing.Any:
        ...
    

class YearEnd(YearOffset):
    '\n    DateOffset increments between calendar year ends.\n    '
    def __init__(self, *args, **kwargs) -> None:
        '\n    DateOffset increments between calendar year ends.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    _day_opt: str
    _default_month: int
    @classmethod
    def _from_name(cls) -> typing.Any:
        ...
    
    @property
    def _period_dtype_code(self) -> typing.Any:
        ...
    
    _prefix: str
    def __getattr__(self, name) -> typing.Any:
        ...
    

class YearOffset(SingleConstructorOffset):
    '\n    DateOffset that just needs a month.\n    '
    def __init__(self, *args, **kwargs) -> None:
        '\n    DateOffset that just needs a month.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    def __setstate__(self, state: typing.Any) -> None:
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def _apply_array(self, other) -> numpy.ndarray:
        ...
    
    _attributes: tuple
    @classmethod
    def _from_name(cls) -> typing.Any:
        ...
    
    def _get_offset_day(self) -> typing.Any:
        ...
    
    def apply(self, other) -> typing.Any:
        ...
    
    def apply_index(self, other) -> typing.Any:
        ...
    
    def is_on_offset(self) -> typing.Any:
        ...
    
    @property
    def month(self) -> typing.Any:
        ...
    
    @property
    def rule_code(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class _CustomBusinessMonth(BusinessMixin):
    "\n    DateOffset subclass representing custom business month(s).\n\n    Increments between beginning/end of month dates.\n\n    Parameters\n    ----------\n    n : int, default 1\n        The number of months represented.\n    normalize : bool, default False\n        Normalize start/end dates to midnight before generating date range.\n    weekmask : str, Default 'Mon Tue Wed Thu Fri'\n        Weekmask of valid business days, passed to ``numpy.busdaycalendar``.\n    holidays : list\n        List/array of dates to exclude from the set of valid business days,\n        passed to ``numpy.busdaycalendar``.\n    calendar : pd.HolidayCalendar or np.busdaycalendar\n        Calendar to integrate.\n    offset : timedelta, default timedelta(0)\n        Time offset to apply.\n    "
    def __init__(self, *args, **kwargs) -> None:
        "\n    DateOffset subclass representing custom business month(s).\n\n    Increments between beginning/end of month dates.\n\n    Parameters\n    ----------\n    n : int, default 1\n        The number of months represented.\n    normalize : bool, default False\n        Normalize start/end dates to midnight before generating date range.\n    weekmask : str, Default 'Mon Tue Wed Thu Fri'\n        Weekmask of valid business days, passed to ``numpy.busdaycalendar``.\n    holidays : list\n        List/array of dates to exclude from the set of valid business days,\n        passed to ``numpy.busdaycalendar``.\n    calendar : pd.HolidayCalendar or np.busdaycalendar\n        Calendar to integrate.\n    offset : timedelta, default timedelta(0)\n        Time offset to apply.\n    "
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    _attributes: tuple
    @classmethod
    def _from_name(cls) -> typing.Any:
        ...
    
    def apply(self, other) -> typing.Any:
        ...
    
    cbday_roll: _mod_pandas__libs_properties.CachedProperty
    m_offset: _mod_pandas__libs_properties.CachedProperty
    month_roll: _mod_pandas__libs_properties.CachedProperty
    def __getattr__(self, name) -> typing.Any:
        ...
    

__doc__: typing.Any
__file__: str
__name__: str
__package__: str
__pyx_capi__: dict
def __pyx_unpickle_BaseOffset() -> typing.Any:
    ...

def __pyx_unpickle_Enum() -> typing.Any:
    ...

def __pyx_unpickle_RelativeDeltaOffset() -> typing.Any:
    ...

__test__: dict
_dont_uppercase: set
def _get_offset() -> typing.Any:
    "\n    Return DateOffset object associated with rule name.\n\n    Examples\n    --------\n    _get_offset('EOM') --> BMonthEnd(1)\n    "
    ...

_lite_rule_alias: dict
_offset_map: dict
_relativedelta_kwds: set
def apply_array_wraps() -> typing.Any:
    ...

def apply_index_wraps() -> typing.Any:
    ...

def apply_wrapper_core() -> typing.Any:
    ...

def apply_wraps() -> typing.Any:
    ...

cache_readonly = _mod_pandas__libs_properties.CachedProperty
def delta_to_tick() -> typing.Any:
    ...

def easter(year, method) -> typing.Any:
    '\n    This method was ported from the work done by GM Arts,\n    on top of the algorithm by Claus Tondering, which was\n    based in part on the algorithm of Ouding (1940), as\n    quoted in "Explanatory Supplement to the Astronomical\n    Almanac", P.  Kenneth Seidelmann, editor.\n\n    This algorithm implements three different easter\n    calculation methods:\n\n    1 - Original calculation in Julian calendar, valid in\n        dates after 326 AD\n    2 - Original method, with date converted to Gregorian\n        calendar, valid in years 1583 to 4099\n    3 - Revised method, in Gregorian calendar, valid in\n        years 1583 to 4099 as well\n\n    These methods are represented by the constants:\n\n    * ``EASTER_JULIAN   = 1``\n    * ``EASTER_ORTHODOX = 2``\n    * ``EASTER_WESTERN  = 3``\n\n    The default method is method 3.\n\n    More about the algorithm may be found at:\n\n    `GM Arts: Easter Algorithms <http://www.gmarts.org/index.php?go=415>`_\n\n    and\n\n    `The Calendar FAQ: Easter <https://www.tondering.dk/claus/cal/easter.php>`_\n\n    '
    ...

int_to_weekday: dict
opattern: _mod_re.Pattern
prefix_mapping: dict
relativedelta = _mod_dateutil_relativedelta.relativedelta
def roll_convention() -> typing.Any:
    '\n    Possibly increment or decrement the number of periods to shift\n    based on rollforward/rollbackward conventions.\n\n    Parameters\n    ----------\n    other : int, generally the day component of a datetime\n    n : number of periods to increment, before adjusting for rolling\n    compare : int, generally the day component of a datetime, in the same\n              month as the datetime form which `other` was taken.\n\n    Returns\n    -------\n    n : int number of periods to increment\n    '
    ...

def roll_qtrday() -> typing.Any:
    "\n    Possibly increment or decrement the number of periods to shift\n    based on rollforward/rollbackward conventions.\n\n    Parameters\n    ----------\n    other : datetime or Timestamp\n    n : number of periods to increment, before adjusting for rolling\n    month : int reference month giving the first month of the year\n    day_opt : {'start', 'end', 'business_start', 'business_end'}\n        The convention to use in finding the day in a given month against\n        which to compare for rollforward/rollbackward decisions.\n    modby : int 3 for quarters, 12 for years\n\n    Returns\n    -------\n    n : int number of periods to increment\n\n    See Also\n    --------\n    get_day_of_month : Find the day in a month provided an offset.\n    "
    ...

def shift_day() -> typing.Any:
    "\n    Increment the datetime `other` by the given number of days, retaining\n    the time-portion of the datetime.  For tz-naive datetimes this is\n    equivalent to adding a timedelta.  For tz-aware datetimes it is similar to\n    dateutil's relativedelta.__add__, but handles pytz tzinfo objects.\n\n    Parameters\n    ----------\n    other : datetime or Timestamp\n    days : int\n\n    Returns\n    -------\n    shifted: datetime or Timestamp\n    "
    ...

def shift_month() -> typing.Any:
    "\n    Given a datetime (or Timestamp) `stamp`, an integer `months` and an\n    option `day_opt`, return a new datetimelike that many months later,\n    with day determined by `day_opt` using relativedelta semantics.\n\n    Scalar analogue of shift_months\n\n    Parameters\n    ----------\n    stamp : datetime or Timestamp\n    months : int\n    day_opt : None, 'start', 'end', 'business_start', 'business_end', or int\n        None: returned datetimelike has the same day as the input, or the\n              last day of the month if the new month is too short\n        'start': returned datetimelike has day=1\n        'end': returned datetimelike has day on the last day of the month\n        'business_start': returned datetimelike has day on the first\n            business day of the month\n        'business_end': returned datetimelike has day on the last\n            business day of the month\n        int: returned datetimelike has day equal to day_opt\n\n    Returns\n    -------\n    shifted : datetime or Timestamp (same as input `stamp`)\n    "
    ...

def shift_months() -> typing.Any:
    "\n    Given an int64-based datetime index, shift all elements\n    specified number of months using DateOffset semantics\n\n    day_opt: {None, 'start', 'end', 'business_start', 'business_end'}\n       * None: day of month\n       * 'start' 1st day of month\n       * 'end' last day of month\n    "
    ...

def to_offset() -> typing.Any:
    '\n    Return DateOffset object from string or tuple representation\n    or datetime.timedelta object.\n\n    Parameters\n    ----------\n    freq : str, tuple, datetime.timedelta, DateOffset or None\n\n    Returns\n    -------\n    DateOffset or None\n\n    Raises\n    ------\n    ValueError\n        If freq is an invalid frequency\n\n    See Also\n    --------\n    DateOffset : Standard kind of date increment used for a date range.\n\n    Examples\n    --------\n    >>> to_offset("5min")\n    <5 * Minutes>\n\n    >>> to_offset("1D1H")\n    <25 * Hours>\n\n    >>> to_offset("2W")\n    <2 * Weeks: weekday=6>\n\n    >>> to_offset("2B")\n    <2 * BusinessDays>\n\n    >>> to_offset(pd.Timedelta(days=1))\n    <Day>\n\n    >>> to_offset(Hour())\n    <Hour>\n    '
    ...

weekday_to_int: dict
def __getattr__(name) -> typing.Any:
    ...

