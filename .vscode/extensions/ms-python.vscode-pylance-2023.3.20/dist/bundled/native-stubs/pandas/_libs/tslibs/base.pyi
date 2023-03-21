# Python: 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)]
# Library: pandas, version: 1.2.4
# Module: pandas._libs.tslibs.base, version: unspecified
import typing
import builtins as _mod_builtins
import datetime as _mod_datetime

class ABCTimestamp(_mod_datetime.datetime):
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __reduce_cython__(self) -> typing.Any:
        ...
    
    def __setstate_cython__(self) -> typing.Any:
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @classmethod
    def combine(cls) -> typing.Any:
        'date, time -> datetime with same date and time fields'
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
    
    @classmethod
    def now(cls, type, tz) -> typing.Any:
        'Returns new datetime object representing current time local to tz.\n\n  tz\n    Timezone object.\n\nIf no tz is specified, uses local timezone.'
        ...
    
    @classmethod
    def strptime(cls) -> typing.Any:
        'string, format -> new datetime parsed from a string (like time.strptime()).'
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
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

__doc__: str
__file__: str
__name__: str
__package__: str
def __pyx_unpickle_ABCTimestamp() -> typing.Any:
    ...

__test__: dict
def __getattr__(name) -> typing.Any:
    ...

