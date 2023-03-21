# Python: 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)]
# Library: pandas, version: 1.2.4
# Module: pandas._libs.reduction, version: unspecified
import typing
import builtins as _mod_builtins

class BlockSlider(_mod_builtins.object):
    '\n    Only capable of sliding on axis=0\n    '
    def __init__(self, *args, **kwargs) -> None:
        '\n    Only capable of sliding on axis=0\n    '
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
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class InvalidApply(_mod_builtins.Exception):
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
    

class SeriesBinGrouper(_BaseGrouper):
    '\n    Performs grouping operation according to bin edges, rather than labels\n    '
    def __init__(self, *args, **kwargs) -> None:
        '\n    Performs grouping operation according to bin edges, rather than labels\n    '
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
    
    @property
    def arr(self) -> typing.Any:
        ...
    
    @property
    def bins(self) -> typing.Any:
        ...
    
    @property
    def dummy_arr(self) -> typing.Any:
        ...
    
    @property
    def dummy_index(self) -> typing.Any:
        ...
    
    @property
    def f(self) -> typing.Any:
        ...
    
    def get_result(self) -> typing.Any:
        ...
    
    @property
    def index(self) -> typing.Any:
        ...
    
    @property
    def ityp(self) -> typing.Any:
        ...
    
    @property
    def name(self) -> typing.Any:
        ...
    
    @property
    def typ(self) -> typing.Any:
        ...
    
    @property
    def values(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class SeriesGrouper(_BaseGrouper):
    '\n    Performs generic grouping operation while avoiding ndarray construction\n    overhead\n    '
    def __init__(self, *args, **kwargs) -> None:
        '\n    Performs generic grouping operation while avoiding ndarray construction\n    overhead\n    '
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
    
    @property
    def arr(self) -> typing.Any:
        ...
    
    @property
    def dummy_arr(self) -> typing.Any:
        ...
    
    @property
    def dummy_index(self) -> typing.Any:
        ...
    
    @property
    def f(self) -> typing.Any:
        ...
    
    def get_result(self) -> typing.Any:
        ...
    
    @property
    def index(self) -> typing.Any:
        ...
    
    @property
    def ityp(self) -> typing.Any:
        ...
    
    @property
    def labels(self) -> typing.Any:
        ...
    
    @property
    def name(self) -> typing.Any:
        ...
    
    @property
    def typ(self) -> typing.Any:
        ...
    
    @property
    def values(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class Slider(_mod_builtins.object):
    '\n    Only handles contiguous data for now\n    '
    def __init__(self, *args, **kwargs) -> None:
        '\n    Only handles contiguous data for now\n    '
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
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class _BaseGrouper(_mod_builtins.object):
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
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

__doc__: typing.Any
__file__: str
__name__: str
__package__: str
def __pyx_unpickle_Enum() -> typing.Any:
    ...

def __pyx_unpickle_SeriesBinGrouper() -> typing.Any:
    ...

def __pyx_unpickle_SeriesGrouper() -> typing.Any:
    ...

def __pyx_unpickle_Slider() -> typing.Any:
    ...

def __pyx_unpickle__BaseGrouper() -> typing.Any:
    ...

__test__: dict
def apply_frame_axis0() -> typing.Any:
    ...

def check_result_array() -> typing.Any:
    ...

def copy(x) -> typing.Any:
    "Shallow copy operation on arbitrary Python objects.\n\n    See the module's __doc__ string for more info.\n    "
    ...

def extract_result() -> typing.Any:
    ' extract the result object, it might be a 0-dim ndarray\n        or a len-1 0-dim, or a scalar '
    ...

def is_scalar() -> typing.Any:
    '\n    Return True if given object is scalar.\n\n    Parameters\n    ----------\n    val : object\n        This includes:\n\n        - numpy array scalar (e.g. np.int64)\n        - Python builtin numerics\n        - Python builtin byte arrays and strings\n        - None\n        - datetime.datetime\n        - datetime.timedelta\n        - Period\n        - decimal.Decimal\n        - Interval\n        - DateOffset\n        - Fraction\n        - Number.\n\n    Returns\n    -------\n    bool\n        Return True if given object is scalar.\n\n    Examples\n    --------\n    >>> dt = datetime.datetime(2018, 10, 3)\n    >>> pd.api.types.is_scalar(dt)\n    True\n\n    >>> pd.api.types.is_scalar([2, 3])\n    False\n\n    >>> pd.api.types.is_scalar({0: 1, 2: 3})\n    False\n\n    >>> pd.api.types.is_scalar((0, 2))\n    False\n\n    pandas supports PEP 3141 numbers:\n\n    >>> from fractions import Fraction\n    >>> pd.api.types.is_scalar(Fraction(3, 5))\n    True\n    '
    ...

def maybe_convert_objects() -> typing.Any:
    '\n    Type inference function-- convert object array to proper dtype\n\n    Parameters\n    ----------\n    values : ndarray\n        Array of object elements to convert.\n    try_float : bool, default False\n        If an array-like object contains only float or NaN values is\n        encountered, whether to convert and return an array of float dtype.\n    safe : bool, default False\n        Whether to upcast numeric type (e.g. int cast to float). If set to\n        True, no upcasting will be performed.\n    convert_datetime : bool, default False\n        If an array-like object contains only datetime values or NaT is\n        encountered, whether to convert and return an array of M8[ns] dtype.\n    convert_timedelta : bool, default False\n        If an array-like object contains only timedelta values or NaT is\n        encountered, whether to convert and return an array of m8[ns] dtype.\n    convert_to_nullable_integer : bool, default False\n        If an array-like object contains only integer values (and NaN) is\n        encountered, whether to convert and return an IntegerArray.\n\n    Returns\n    -------\n    Array of converted object values to more specific dtypes if applicable.\n    '
    ...

def __getattr__(name) -> typing.Any:
    ...

