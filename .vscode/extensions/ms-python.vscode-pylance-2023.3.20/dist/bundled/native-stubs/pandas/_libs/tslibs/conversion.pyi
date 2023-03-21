# Python: 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)]
# Library: pandas, version: 1.2.4
# Module: pandas._libs.tslibs.conversion, version: unspecified
import typing
import builtins as _mod_builtins
import numpy as _mod_numpy
import pandas._libs.tslibs.np_datetime as _mod_pandas__libs_tslibs_np_datetime

DT64NS_DTYPE: _mod_numpy.dtype[datetime64]
OutOfBoundsDatetime = _mod_pandas__libs_tslibs_np_datetime.OutOfBoundsDatetime
class OutOfBoundsTimedelta(_mod_builtins.ValueError):
    '\n    Raised when encountering a timedelta value that cannot be represented\n    as a timedelta64[ns].\n    '
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, *args, **kwargs) -> None:
        '\n    Raised when encountering a timedelta value that cannot be represented\n    as a timedelta64[ns].\n    '
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
    

TD64NS_DTYPE: _mod_numpy.dtype[timedelta64]
class _TSObject(_mod_builtins.object):
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __reduce__(self) -> typing.Union[str, typing.Tuple[typing.Any, ...]]:
        ...
    
    def __setstate__(self, state: typing.Any) -> None:
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @property
    def value(self) -> typing.Any:
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

__test__: dict
def datetime_to_datetime64() -> typing.Any:
    '\n    Convert ndarray of datetime-like objects to int64 array representing\n    nanosecond timestamps.\n\n    Parameters\n    ----------\n    values : ndarray[object]\n\n    Returns\n    -------\n    result : ndarray[int64_t]\n    inferred_tz : tzinfo or None\n    '
    ...

def ensure_datetime64ns() -> typing.Any:
    "\n    Ensure a np.datetime64 array has dtype specifically 'datetime64[ns]'\n\n    Parameters\n    ----------\n    arr : ndarray\n    copy : bool, default True\n\n    Returns\n    -------\n    ndarray with dtype datetime64[ns]\n    "
    ...

def ensure_timedelta64ns() -> typing.Any:
    "\n    Ensure a np.timedelta64 array has dtype specifically 'timedelta64[ns]'\n\n    Parameters\n    ----------\n    arr : ndarray\n    copy : boolean, default True\n\n    Returns\n    -------\n    ndarray[timedelta64[ns]]\n    "
    ...

def localize_pydatetime() -> typing.Any:
    '\n    Take a datetime/Timestamp in UTC and localizes to timezone tz.\n\n    Parameters\n    ----------\n    dt : datetime or Timestamp\n    tz : tzinfo, "UTC", or None\n\n    Returns\n    -------\n    localized : datetime or Timestamp\n    '
    ...

def parse_datetime_string() -> typing.Any:
    '\n    Parse datetime string, only returns datetime.\n    Also cares special handling matching time patterns.\n\n    Returns\n    -------\n    datetime\n    '
    ...

def precision_from_unit() -> typing.Any:
    '\n    Return a casting of the unit represented to nanoseconds + the precision\n    to round the fractional part.\n\n    Notes\n    -----\n    The caller is responsible for ensuring that the default value of "ns"\n    takes the place of None.\n    '
    ...

def __getattr__(name) -> typing.Any:
    ...

