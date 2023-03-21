# Python: 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)]
# Library: pandas, version: 1.2.4
# Module: pandas._libs.tslibs.timedeltas, version: unspecified
import typing
import builtins as _mod_builtins
import datetime as _mod_datetime
import importlib._bootstrap as _mod_importlib__bootstrap

Components = _mod_importlib__bootstrap.Components
class Timedelta(_Timedelta):
    "\n    Represents a duration, the difference between two dates or times.\n\n    Timedelta is the pandas equivalent of python's ``datetime.timedelta``\n    and is interchangeable with it in most cases.\n\n    Parameters\n    ----------\n    value : Timedelta, timedelta, np.timedelta64, str, or int\n    unit : str, default 'ns'\n        Denote the unit of the input, if input is an integer.\n\n        Possible values:\n\n        * 'W', 'D', 'T', 'S', 'L', 'U', or 'N'\n        * 'days' or 'day'\n        * 'hours', 'hour', 'hr', or 'h'\n        * 'minutes', 'minute', 'min', or 'm'\n        * 'seconds', 'second', or 'sec'\n        * 'milliseconds', 'millisecond', 'millis', or 'milli'\n        * 'microseconds', 'microsecond', 'micros', or 'micro'\n        * 'nanoseconds', 'nanosecond', 'nanos', 'nano', or 'ns'.\n\n    **kwargs\n        Available kwargs: {days, seconds, microseconds,\n        milliseconds, minutes, hours, weeks}.\n        Values for construction in compat with datetime.timedelta.\n        Numpy ints and floats will be coerced to python ints and floats.\n\n    Notes\n    -----\n    The ``.value`` attribute is always in ns.\n\n    If the precision is higher than nanoseconds, the precision of the duration is\n    truncated to nanoseconds.\n    "
    def __abs__(self) -> Timedelta:
        ...
    
    def __add__(self, other) -> Timedelta:
        ...
    
    __dict__: typing.Dict[str, typing.Any]
    def __divmod__(self, other) -> typing.Tuple[Timedelta, Timedelta]:
        ...
    
    def __floordiv__(self, other) -> int:
        ...
    
    def __init__(self, *args, **kwargs) -> None:
        "\n    Represents a duration, the difference between two dates or times.\n\n    Timedelta is the pandas equivalent of python's ``datetime.timedelta``\n    and is interchangeable with it in most cases.\n\n    Parameters\n    ----------\n    value : Timedelta, timedelta, np.timedelta64, str, or int\n    unit : str, default 'ns'\n        Denote the unit of the input, if input is an integer.\n\n        Possible values:\n\n        * 'W', 'D', 'T', 'S', 'L', 'U', or 'N'\n        * 'days' or 'day'\n        * 'hours', 'hour', 'hr', or 'h'\n        * 'minutes', 'minute', 'min', or 'm'\n        * 'seconds', 'second', or 'sec'\n        * 'milliseconds', 'millisecond', 'millis', or 'milli'\n        * 'microseconds', 'microsecond', 'micros', or 'micro'\n        * 'nanoseconds', 'nanosecond', 'nanos', 'nano', or 'ns'.\n\n    **kwargs\n        Available kwargs: {days, seconds, microseconds,\n        milliseconds, minutes, hours, weeks}.\n        Values for construction in compat with datetime.timedelta.\n        Numpy ints and floats will be coerced to python ints and floats.\n\n    Notes\n    -----\n    The ``.value`` attribute is always in ns.\n\n    If the precision is higher than nanoseconds, the precision of the duration is\n    truncated to nanoseconds.\n    "
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __inv__(self) -> typing.Any:
        ...
    
    def __mod__(self, other) -> Timedelta:
        ...
    
    def __mul__(self, other) -> Timedelta:
        ...
    
    def __neg__(self) -> Timedelta:
        ...
    
    def __pos__(self) -> Timedelta:
        ...
    
    def __radd__(self, other) -> Timedelta:
        ...
    
    def __rdivmod__(self, other) -> typing.Tuple[Timedelta, Timedelta]:
        ...
    
    def __reduce__(self) -> typing.Union[str, typing.Tuple[typing.Any, ...]]:
        ...
    
    def __rfloordiv__(self, other) -> Timedelta:
        ...
    
    def __rmod__(self, other) -> Timedelta:
        ...
    
    def __rmul__(self, other) -> Timedelta:
        ...
    
    def __rsub__(self, other) -> Timedelta:
        ...
    
    def __rtruediv__(self, other) -> Timedelta:
        ...
    
    def __setstate__(self, state) -> None:
        ...
    
    def __sub__(self, other) -> Timedelta:
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __truediv__(self, other) -> float:
        ...
    
    @property
    def __weakref__(self) -> typing.Any:
        'list of weak references to the object (if defined)'
        ...
    
    def _round(self, freq, rounder) -> typing.Any:
        ...
    
    def ceil(self, freq) -> typing.Any:
        '\n        Return a new Timedelta ceiled to this resolution.\n\n        Parameters\n        ----------\n        freq : str\n            Frequency string indicating the ceiling resolution.\n        '
        ...
    
    def floor(self, freq) -> typing.Any:
        '\n        Return a new Timedelta floored to this resolution.\n\n        Parameters\n        ----------\n        freq : str\n            Frequency string indicating the flooring resolution.\n        '
        ...
    
    max: Timedelta
    min: Timedelta
    resolution: Timedelta
    def round(self, freq) -> typing.Any:
        '\n        Round the Timedelta to the specified resolution.\n\n        Parameters\n        ----------\n        freq : str\n            Frequency string indicating the rounding resolution.\n\n        Returns\n        -------\n        a new Timedelta rounded to the given resolution of `freq`\n\n        Raises\n        ------\n        ValueError if the freq cannot be converted\n        '
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class _Timedelta(_mod_datetime.timedelta):
    __array_priority__: int
    def __bool__(self) -> bool:
        'self != 0'
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
    def __reduce_cython__(self) -> typing.Any:
        ...
    
    def __repr__(self) -> str:
        'Return repr(self).'
        ...
    
    def __setstate_cython__(self) -> typing.Any:
        ...
    
    def __str__(self) -> str:
        'Return str(self).'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @property
    def _d(self) -> typing.Any:
        ...
    
    def _ensure_components(self) -> typing.Any:
        '\n        compute the components\n        '
        ...
    
    @property
    def _h(self) -> typing.Any:
        ...
    
    def _has_ns(self) -> typing.Any:
        ...
    
    @property
    def _m(self) -> typing.Any:
        ...
    
    @property
    def _ms(self) -> typing.Any:
        ...
    
    @property
    def _ns(self) -> typing.Any:
        ...
    
    def _repr_base(self) -> typing.Any:
        '\n\n        Parameters\n        ----------\n        format : None|all|sub_day|long\n\n        Returns\n        -------\n        converted : string of a Timedelta\n\n        '
        ...
    
    @property
    def _s(self) -> typing.Any:
        ...
    
    @property
    def _us(self) -> typing.Any:
        ...
    
    @property
    def asm8(self) -> typing.Any:
        "\n        Return a numpy timedelta64 array scalar view.\n\n        Provides access to the array scalar view (i.e. a combination of the\n        value and the units) associated with the numpy.timedelta64().view(),\n        including a 64-bit integer representation of the timedelta in\n        nanoseconds (Python int compatible).\n\n        Returns\n        -------\n        numpy timedelta64 array scalar view\n            Array scalar view of the timedelta in nanoseconds.\n\n        Examples\n        --------\n        >>> td = pd.Timedelta('1 days 2 min 3 us 42 ns')\n        >>> td.asm8\n        numpy.timedelta64(86520000003042,'ns')\n\n        >>> td = pd.Timedelta('2 min 3 s')\n        >>> td.asm8\n        numpy.timedelta64(123000000000,'ns')\n\n        >>> td = pd.Timedelta('3 ms 5 us')\n        >>> td.asm8\n        numpy.timedelta64(3005000,'ns')\n\n        >>> td = pd.Timedelta(42, unit='ns')\n        >>> td.asm8\n        numpy.timedelta64(42,'ns')\n        "
        ...
    
    @property
    def components(self) -> typing.Any:
        '\n        Return a components namedtuple-like.\n        '
        ...
    
    @property
    def delta(self) -> typing.Any:
        "\n        Return the timedelta in nanoseconds (ns), for internal compatibility.\n\n        Returns\n        -------\n        int\n            Timedelta in nanoseconds.\n\n        Examples\n        --------\n        >>> td = pd.Timedelta('1 days 42 ns')\n        >>> td.delta\n        86400000000042\n\n        >>> td = pd.Timedelta('3 s')\n        >>> td.delta\n        3000000000\n\n        >>> td = pd.Timedelta('3 ms 5 us')\n        >>> td.delta\n        3005000\n\n        >>> td = pd.Timedelta(42, unit='ns')\n        >>> td.delta\n        42\n        "
        ...
    
    @property
    def freq(self) -> typing.Any:
        ...
    
    @property
    def is_populated(self) -> typing.Any:
        ...
    
    def isoformat(self) -> typing.Any:
        "\n        Format Timedelta as ISO 8601 Duration like\n        ``P[n]Y[n]M[n]DT[n]H[n]M[n]S``, where the ``[n]`` s are replaced by the\n        values. See https://en.wikipedia.org/wiki/ISO_8601#Durations.\n\n        Returns\n        -------\n        str\n\n        See Also\n        --------\n        Timestamp.isoformat : Function is used to convert the given\n            Timestamp object into the ISO format.\n\n        Notes\n        -----\n        The longest component is days, whose value may be larger than\n        365.\n        Every component is always included, even if its value is 0.\n        Pandas uses nanosecond precision, so up to 9 decimal places may\n        be included in the seconds component.\n        Trailing 0's are removed from the seconds component after the decimal.\n        We do not 0 pad components, so it's `...T5H...`, not `...T05H...`\n\n        Examples\n        --------\n        >>> td = pd.Timedelta(days=6, minutes=50, seconds=3,\n        ...                   milliseconds=10, microseconds=10, nanoseconds=12)\n\n        >>> td.isoformat()\n        'P6DT0H50M3.010010012S'\n        >>> pd.Timedelta(hours=1, seconds=10).isoformat()\n        'P0DT0H0M10S'\n        >>> pd.Timedelta(hours=1, seconds=10).isoformat()\n        'P0DT0H0M10S'\n        >>> pd.Timedelta(days=500.5).isoformat()\n        'P500DT12H0MS'\n        "
        ...
    
    @property
    def nanoseconds(self) -> typing.Any:
        "\n        Return the number of nanoseconds (n), where 0 <= n < 1 microsecond.\n\n        Returns\n        -------\n        int\n            Number of nanoseconds.\n\n        See Also\n        --------\n        Timedelta.components : Return all attributes with assigned values\n            (i.e. days, hours, minutes, seconds, milliseconds, microseconds,\n            nanoseconds).\n\n        Examples\n        --------\n        **Using string input**\n\n        >>> td = pd.Timedelta('1 days 2 min 3 us 42 ns')\n\n        >>> td.nanoseconds\n        42\n\n        **Using integer input**\n\n        >>> td = pd.Timedelta(42, unit='ns')\n        >>> td.nanoseconds\n        42\n        "
        ...
    
    @property
    def resolution_string(self) -> typing.Any:
        "\n        Return a string representing the lowest timedelta resolution.\n\n        Each timedelta has a defined resolution that represents the lowest OR\n        most granular level of precision. Each level of resolution is\n        represented by a short string as defined below:\n\n        Resolution:     Return value\n\n        * Days:         'D'\n        * Hours:        'H'\n        * Minutes:      'T'\n        * Seconds:      'S'\n        * Milliseconds: 'L'\n        * Microseconds: 'U'\n        * Nanoseconds:  'N'\n\n        Returns\n        -------\n        str\n            Timedelta resolution.\n\n        Examples\n        --------\n        >>> td = pd.Timedelta('1 days 2 min 3 us 42 ns')\n        >>> td.resolution_string\n        'N'\n\n        >>> td = pd.Timedelta('1 days 2 min 3 us')\n        >>> td.resolution_string\n        'U'\n\n        >>> td = pd.Timedelta('2 min 3 s')\n        >>> td.resolution_string\n        'S'\n\n        >>> td = pd.Timedelta(36, unit='us')\n        >>> td.resolution_string\n        'U'\n        "
        ...
    
    def to_numpy(self) -> typing.Any:
        '\n        Convert the Timedelta to a NumPy timedelta64.\n\n        .. versionadded:: 0.25.0\n\n        This is an alias method for `Timedelta.to_timedelta64()`. The dtype and\n        copy parameters are available here only for compatibility. Their values\n        will not affect the return value.\n\n        Returns\n        -------\n        numpy.timedelta64\n\n        See Also\n        --------\n        Series.to_numpy : Similar method for Series.\n        '
        ...
    
    def to_pytimedelta(self) -> typing.Any:
        '\n        Convert a pandas Timedelta object into a python timedelta object.\n\n        Timedelta objects are internally saved as numpy datetime64[ns] dtype.\n        Use to_pytimedelta() to convert to object dtype.\n\n        Returns\n        -------\n        datetime.timedelta or numpy.array of datetime.timedelta\n\n        See Also\n        --------\n        to_timedelta : Convert argument to Timedelta type.\n\n        Notes\n        -----\n        Any nanosecond resolution will be lost.\n        '
        ...
    
    def to_timedelta64(self) -> typing.Any:
        "\n        Return a numpy.timedelta64 object with 'ns' precision.\n        "
        ...
    
    @property
    def value(self) -> typing.Any:
        ...
    
    def view(self) -> typing.Any:
        '\n        Array view compatibility.\n        '
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

def __pyx_unpickle__Timedelta() -> typing.Any:
    ...

__test__: dict
def _binary_op_method_timedeltalike() -> typing.Any:
    ...

_no_input: object
def _op_unary_method() -> typing.Any:
    ...

def array_to_timedelta64() -> typing.Any:
    "\n    Convert an ndarray to an array of timedeltas. If errors == 'coerce',\n    coerce non-convertible objects to NaT. Otherwise, raise.\n    "
    ...

def delta_to_nanoseconds() -> typing.Any:
    ...

def ints_to_pytimedelta() -> typing.Any:
    '\n    convert an i8 repr to an ndarray of timedelta or Timedelta (if box ==\n    True)\n\n    Parameters\n    ----------\n    arr : ndarray[int64_t]\n    box : bool, default False\n\n    Returns\n    -------\n    result : ndarray[object]\n        array of Timedelta or timedeltas objects\n    '
    ...

def parse_timedelta_unit() -> typing.Any:
    '\n    Parameters\n    ----------\n    unit : str or None\n\n    Returns\n    -------\n    str\n        Canonical unit string.\n\n    Raises\n    ------\n    ValueError : on non-parseable input\n    '
    ...

def __getattr__(name) -> typing.Any:
    ...

