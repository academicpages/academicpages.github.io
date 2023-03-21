# Python: 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)]
# Library: pandas, version: 1.2.4
# Module: pandas._libs.missing, version: unspecified
import typing
import builtins as _mod_builtins

class C_NAType(_mod_builtins.object):
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
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

IS64: bool
NA: NAType
class NAType(C_NAType):
    '\n    NA ("not available") missing value indicator.\n\n    .. warning::\n\n       Experimental: the behaviour of NA can still change without warning.\n\n    .. versionadded:: 1.0.0\n\n    The NA singleton is a missing value indicator defined by pandas. It is\n    used in certain new extension dtypes (currently the "string" dtype).\n    '
    _HANDLED_TYPES: tuple
    def __abs__(self) -> NAType:
        ...
    
    def __add__(self, other) -> NAType:
        ...
    
    def __and__(self, other) -> NAType:
        ...
    
    __array_priority__: int
    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs) -> typing.Any:
        ...
    
    def __bool__(self) -> bool:
        ...
    
    __dict__: typing.Dict[str, typing.Any]
    def __divmod__(self, other) -> typing.Tuple[NAType, NAType]:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __floordiv__(self, other) -> int:
        ...
    
    def __format__(self, format_spec) -> 'unicode':
        ...
    
    def __ge__(self, other) -> bool:
        ...
    
    def __gt__(self, other) -> bool:
        ...
    
    def __hash__(self) -> int:
        ...
    
    def __init__(self) -> None:
        '\n    NA ("not available") missing value indicator.\n\n    .. warning::\n\n       Experimental: the behaviour of NA can still change without warning.\n\n    .. versionadded:: 1.0.0\n\n    The NA singleton is a missing value indicator defined by pandas. It is\n    used in certain new extension dtypes (currently the "string" dtype).\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __invert__(self) -> NAType:
        ...
    
    def __le__(self, other) -> bool:
        ...
    
    def __lt__(self, other) -> bool:
        ...
    
    def __matmul__(self, other) -> typing.Any:
        ...
    
    def __mod__(self, other) -> NAType:
        ...
    
    def __mul__(self, other) -> NAType:
        ...
    
    def __ne__(self, other) -> bool:
        ...
    
    def __neg__(self) -> NAType:
        ...
    
    def __or__(self, other) -> NAType:
        ...
    
    def __pos__(self) -> NAType:
        ...
    
    def __pow__(self, other) -> NAType:
        ...
    
    def __radd__(self, other) -> NAType:
        ...
    
    def __rand__(self, other) -> NAType:
        ...
    
    def __rdivmod__(self, other) -> typing.Tuple[NAType, NAType]:
        ...
    
    def __reduce__(self) -> typing.Union[str, typing.Tuple[typing.Any, ...]]:
        ...
    
    def __repr__(self) -> 'unicode':
        ...
    
    def __rfloordiv__(self, other) -> NAType:
        ...
    
    def __rmatmul__(self, other) -> typing.Any:
        ...
    
    def __rmod__(self, other) -> NAType:
        ...
    
    def __rmul__(self, other) -> NAType:
        ...
    
    def __ror__(self, other) -> NAType:
        ...
    
    def __rpow__(self, other) -> NAType:
        ...
    
    def __rsub__(self, other) -> NAType:
        ...
    
    def __rtruediv__(self, other) -> NAType:
        ...
    
    def __rxor__(self, other) -> NAType:
        ...
    
    def __sub__(self, other) -> NAType:
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
    
    def __xor__(self, other) -> NAType:
        ...
    
    _instance: NAType
    def __getattr__(self, name) -> typing.Any:
        ...
    

__doc__: typing.Any
__file__: str
__name__: str
__package__: str
__pyx_capi__: dict
def __pyx_unpickle_C_NAType() -> typing.Any:
    ...

__test__: dict
def _create_binary_propagating_op() -> typing.Any:
    ...

def _create_unary_propagating_op() -> typing.Any:
    ...

def checknull() -> typing.Any:
    '\n    Return boolean describing of the input is NA-like, defined here as any\n    of:\n     - None\n     - nan\n     - NaT\n     - np.datetime64 representation of NaT\n     - np.timedelta64 representation of NaT\n     - NA\n\n    Parameters\n    ----------\n    val : object\n\n    Returns\n    -------\n    bool\n\n    Notes\n    -----\n    The difference between `checknull` and `checknull_old` is that `checknull`\n    does *not* consider INF or NEGINF to be NA.\n    '
    ...

def checknull_old() -> typing.Any:
    '\n    Return boolean describing of the input is NA-like, defined here as any\n    of:\n     - None\n     - nan\n     - INF\n     - NEGINF\n     - NaT\n     - np.datetime64 representation of NaT\n     - np.timedelta64 representation of NaT\n\n    Parameters\n    ----------\n    val : object\n\n    Returns\n    -------\n    result : bool\n\n    Notes\n    -----\n    The difference between `checknull` and `checknull_old` is that `checknull`\n    does *not* consider INF or NEGINF to be NA.\n    '
    ...

def isnaobj() -> typing.Any:
    '\n    Return boolean mask denoting which elements of a 1-D array are na-like,\n    according to the criteria defined in `checknull`:\n     - None\n     - nan\n     - NaT\n     - np.datetime64 representation of NaT\n     - np.timedelta64 representation of NaT\n\n    Parameters\n    ----------\n    arr : ndarray\n\n    Returns\n    -------\n    result : ndarray (dtype=np.bool_)\n    '
    ...

def isnaobj2d() -> typing.Any:
    '\n    Return boolean mask denoting which elements of a 2-D array are na-like,\n    according to the criteria defined in `checknull`:\n     - None\n     - nan\n     - NaT\n     - np.datetime64 representation of NaT\n     - np.timedelta64 representation of NaT\n\n    Parameters\n    ----------\n    arr : ndarray\n\n    Returns\n    -------\n    result : ndarray (dtype=np.bool_)\n\n    Notes\n    -----\n    The difference between `isnaobj2d` and `isnaobj2d_old` is that `isnaobj2d`\n    does *not* consider INF or NEGINF to be NA.\n    '
    ...

def isnaobj2d_old() -> typing.Any:
    '\n    Return boolean mask denoting which elements of a 2-D array are na-like,\n    according to the criteria defined in `checknull_old`:\n     - None\n     - nan\n     - INF\n     - NEGINF\n     - NaT\n     - np.datetime64 representation of NaT\n     - np.timedelta64 representation of NaT\n\n    Parameters\n    ----------\n    arr : ndarray\n\n    Returns\n    -------\n    ndarray (dtype=np.bool_)\n\n    Notes\n    -----\n    The difference between `isnaobj2d` and `isnaobj2d_old` is that `isnaobj2d`\n    does *not* consider INF or NEGINF to be NA.\n    '
    ...

def isnaobj_old() -> typing.Any:
    '\n    Return boolean mask denoting which elements of a 1-D array are na-like,\n    defined as being any of:\n     - None\n     - nan\n     - INF\n     - NEGINF\n     - NaT\n     - NA\n\n    Parameters\n    ----------\n    arr : ndarray\n\n    Returns\n    -------\n    result : ndarray (dtype=np.bool_)\n    '
    ...

def isneginf_scalar() -> typing.Any:
    ...

def isposinf_scalar() -> typing.Any:
    ...

def maybe_dispatch_ufunc_to_dunder_op() -> typing.Any:
    "\n    Dispatch a ufunc to the equivalent dunder method.\n\n    Parameters\n    ----------\n    self : ArrayLike\n        The array whose dunder method we dispatch to\n    ufunc : Callable\n        A NumPy ufunc\n    method : {'reduce', 'accumulate', 'reduceat', 'outer', 'at', '__call__'}\n    inputs : ArrayLike\n        The input arrays.\n    kwargs : Any\n        The additional keyword arguments, e.g. ``out``.\n\n    Returns\n    -------\n    result : Any\n        The result of applying the ufunc\n    "
    ...

def __getattr__(name) -> typing.Any:
    ...

