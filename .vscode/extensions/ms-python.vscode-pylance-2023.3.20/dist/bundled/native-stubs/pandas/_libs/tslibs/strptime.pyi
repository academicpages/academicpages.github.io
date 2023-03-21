# Python: 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)]
# Library: pandas, version: 1.2.4
# Module: pandas._libs.tslibs.strptime, version: unspecified
import typing
import _thread as _mod__thread
import builtins as _mod_builtins

class LocaleTime(_mod_builtins.object):
    '\n    Stores and handles locale-specific information related to time.\n\n    ATTRIBUTES:\n        f_weekday -- full weekday names (7-item list)\n        a_weekday -- abbreviated weekday names (7-item list)\n        f_month -- full month names (13-item list; dummy value in [0], which\n                    is added by code)\n        a_month -- abbreviated month names (13-item list, dummy value in\n                    [0], which is added by code)\n        am_pm -- AM/PM representation (2-item list)\n        LC_date_time -- format string for date/time representation (string)\n        LC_date -- format string for date representation (string)\n        LC_time -- format string for time representation (string)\n        timezone -- daylight- and non-daylight-savings timezone representation\n                    (2-item list of sets)\n        lang -- Language used by instance (2-item tuple)\n    '
    def _LocaleTime__calc_am_pm(self) -> typing.Any:
        ...
    
    def _LocaleTime__calc_date_time(self) -> typing.Any:
        ...
    
    def _LocaleTime__calc_month(self) -> typing.Any:
        ...
    
    def _LocaleTime__calc_timezone(self) -> typing.Any:
        ...
    
    def _LocaleTime__calc_weekday(self) -> typing.Any:
        ...
    
    def _LocaleTime__pad(self, seq, front) -> typing.Any:
        ...
    
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self) -> None:
        '\n        Set all attributes.\n\n        Order of methods called matters for dependency reasons.\n\n        The locale language is set at the offset and then checked again before\n        exiting.  This is to make sure that the attributes were not set with a\n        mix of information from more than one locale.  This would most likely\n        happen when using threads where one thread calls a locale-dependent\n        function while another thread changes the locale while the function in\n        the other thread is still running.  Proper coding would call for\n        locks to prevent changing the locale while locale-dependent code is\n        running.  The check here is done in case someone does not think about\n        doing this.\n\n        Only other possible issue is if someone changed the timezone and did\n        not call tz.tzset .  That is an issue for the programmer, though,\n        since changing the timezone is worthless without that call.\n        '
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
    

class TimeRE(_mod_builtins.dict):
    '\n    Handle conversion from format directives to regexes.\n\n    Creates regexes for pattern matching a string of text containing\n    time information\n    '
    def _TimeRE__seqToRE(self, to_convert, directive) -> typing.Any:
        "\n        Convert a list to a regex string for matching a directive.\n\n        Want possible matching values to be from longest to shortest.  This\n        prevents the possibility of a match occurring for a value that also\n        a substring of a larger value that should have matched (e.g., 'abc'\n        matching when 'abcdef' should have been the match).\n        "
        ...
    
    @classmethod
    def __class_getitem__(cls) -> typing.Any:
        'See PEP 585'
        ...
    
    __dict__: typing.Dict[str, typing.Any]
    def __getitem__(self, key) -> typing.Any:
        ...
    
    def __init__(self, locale_time) -> None:
        '\n        Create keys/values.\n\n        Order of execution is important for dependency reasons.\n        '
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
    
    def compile(self, format) -> typing.Any:
        'Return a compiled re object for the format string.'
        ...
    
    @classmethod
    def fromkeys(cls, type, iterable, value) -> typing.Any:
        'Create a new dictionary with keys from iterable and values set to value.'
        ...
    
    def pattern(self, format) -> typing.Any:
        '\n        Return regex pattern for the format string.\n\n        Need to make sure that any characters that might be interpreted as\n        regex syntax are escaped.\n        '
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

_CACHE_MAX_SIZE: int
_TimeRE_cache: TimeRE
__doc__: str
__file__: str
__name__: str
__package__: str
def __pyx_unpickle_Enum() -> typing.Any:
    ...

__test__: dict
_cache_lock: _mod__thread.lock
def _getlang() -> typing.Any:
    'Figure out what language is being used for the locale'
    ...

_regex_cache: dict
def _thread_allocate_lock() -> typing.Any:
    'allocate_lock() -> lock object\n(allocate() is an obsolete synonym)\n\nCreate a new lock object. See help(type(threading.Lock())) for\ninformation about locks.'
    ...

def array_strptime() -> typing.Any:
    "\n    Calculates the datetime structs represented by the passed array of strings\n\n    Parameters\n    ----------\n    values : ndarray of string-like objects\n    fmt : string-like regex\n    exact : matches must be exact if True, search if False\n    errors : string specifying error handling, {'raise', 'ignore', 'coerce'}\n    "
    ...

def __getattr__(name) -> typing.Any:
    ...

