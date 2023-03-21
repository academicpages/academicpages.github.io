# Python: 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)]
# Library: pandas, version: 1.2.4
# Module: pandas._libs.algos, version: unspecified
import typing
import builtins as _mod_builtins

class Infinity(_mod_builtins.object):
    '\n    Provide a positive Infinity comparison method for ranking.\n    '
    __dict__: typing.Dict[str, typing.Any]
    def __eq__(self) -> bool:
        ...
    
    def __ge__(self) -> bool:
        ...
    
    def __gt__(self) -> bool:
        ...
    
    __hash__: typing.Any
    def __init__(self, *args, **kwargs) -> None:
        '\n    Provide a positive Infinity comparison method for ranking.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __le__(self) -> bool:
        ...
    
    def __lt__(self) -> bool:
        ...
    
    __module__: str
    def __ne__(self) -> bool:
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
    

class NegInfinity(_mod_builtins.object):
    '\n    Provide a negative Infinity comparison method for ranking.\n    '
    __dict__: typing.Dict[str, typing.Any]
    def __eq__(self) -> bool:
        ...
    
    def __ge__(self) -> bool:
        ...
    
    def __gt__(self) -> bool:
        ...
    
    __hash__: typing.Any
    def __init__(self, *args, **kwargs) -> None:
        '\n    Provide a negative Infinity comparison method for ranking.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __le__(self) -> bool:
        ...
    
    def __lt__(self) -> bool:
        ...
    
    __module__: str
    def __ne__(self) -> bool:
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
    

__doc__: typing.Any
__file__: str
__name__: str
__package__: str
def __pyx_unpickle_Enum() -> typing.Any:
    ...

__test__: dict
def backfill() -> typing.Any:
    ...

def backfill_2d_inplace() -> typing.Any:
    ...

def backfill_inplace() -> typing.Any:
    ...

def diff_2d() -> typing.Any:
    ...

def ensure_float32() -> typing.Any:
    ...

def ensure_float64() -> typing.Any:
    ...

def ensure_int16() -> typing.Any:
    ...

def ensure_int32() -> typing.Any:
    ...

def ensure_int64() -> typing.Any:
    ...

def ensure_int8() -> typing.Any:
    ...

def ensure_object() -> typing.Any:
    ...

def ensure_platform_int() -> typing.Any:
    ...

def ensure_uint16() -> typing.Any:
    ...

def ensure_uint32() -> typing.Any:
    ...

def ensure_uint64() -> typing.Any:
    ...

def ensure_uint8() -> typing.Any:
    ...

def groupsort_indexer() -> typing.Any:
    '\n    Compute a 1-d indexer.\n\n    The indexer is an ordering of the passed index,\n    ordered by the groups.\n\n    Parameters\n    ----------\n    index: int64 ndarray\n        Mappings from group -> position.\n    ngroups: int64\n        Number of groups.\n\n    Returns\n    -------\n    tuple\n        1-d indexer ordered by groups, group counts.\n\n    Notes\n    -----\n    This is a reverse of the label factorization process.\n    '
    ...

def is_lexsorted() -> typing.Any:
    ...

def is_monotonic(arr, timelike) -> typing.Any:
    '\n    Returns\n    -------\n    tuple\n        is_monotonic_inc : bool\n        is_monotonic_dec : bool\n        is_unique : bool\n    '
    ...

def kth_smallest(a, k) -> typing.Any:
    ...

def nancorr() -> typing.Any:
    ...

def nancorr_spearman() -> typing.Any:
    ...

def pad() -> typing.Any:
    ...

def pad_2d_inplace() -> typing.Any:
    ...

def pad_inplace() -> typing.Any:
    ...

def rank_1d() -> typing.Any:
    '\n    Fast NaN-friendly version of ``scipy.stats.rankdata``.\n    '
    ...

def rank_2d() -> typing.Any:
    '\n    Fast NaN-friendly version of ``scipy.stats.rankdata``.\n    '
    ...

def take_1d_bool_bool() -> typing.Any:
    ...

def take_1d_bool_object() -> typing.Any:
    ...

def take_1d_float32_float32() -> typing.Any:
    ...

def take_1d_float32_float64() -> typing.Any:
    ...

def take_1d_float64_float64() -> typing.Any:
    ...

def take_1d_int16_float64() -> typing.Any:
    ...

def take_1d_int16_int16() -> typing.Any:
    ...

def take_1d_int16_int32() -> typing.Any:
    ...

def take_1d_int16_int64() -> typing.Any:
    ...

def take_1d_int32_float64() -> typing.Any:
    ...

def take_1d_int32_int32() -> typing.Any:
    ...

def take_1d_int32_int64() -> typing.Any:
    ...

def take_1d_int64_float64() -> typing.Any:
    ...

def take_1d_int64_int64() -> typing.Any:
    ...

def take_1d_int8_float64() -> typing.Any:
    ...

def take_1d_int8_int32() -> typing.Any:
    ...

def take_1d_int8_int64() -> typing.Any:
    ...

def take_1d_int8_int8() -> typing.Any:
    ...

def take_1d_object_object() -> typing.Any:
    ...

def take_2d_axis0_bool_bool() -> typing.Any:
    ...

def take_2d_axis0_bool_object() -> typing.Any:
    ...

def take_2d_axis0_float32_float32() -> typing.Any:
    ...

def take_2d_axis0_float32_float64() -> typing.Any:
    ...

def take_2d_axis0_float64_float64() -> typing.Any:
    ...

def take_2d_axis0_int16_float64() -> typing.Any:
    ...

def take_2d_axis0_int16_int16() -> typing.Any:
    ...

def take_2d_axis0_int16_int32() -> typing.Any:
    ...

def take_2d_axis0_int16_int64() -> typing.Any:
    ...

def take_2d_axis0_int32_float64() -> typing.Any:
    ...

def take_2d_axis0_int32_int32() -> typing.Any:
    ...

def take_2d_axis0_int32_int64() -> typing.Any:
    ...

def take_2d_axis0_int64_float64() -> typing.Any:
    ...

def take_2d_axis0_int64_int64() -> typing.Any:
    ...

def take_2d_axis0_int8_float64() -> typing.Any:
    ...

def take_2d_axis0_int8_int32() -> typing.Any:
    ...

def take_2d_axis0_int8_int64() -> typing.Any:
    ...

def take_2d_axis0_int8_int8() -> typing.Any:
    ...

def take_2d_axis0_object_object() -> typing.Any:
    ...

def take_2d_axis1_bool_bool() -> typing.Any:
    ...

def take_2d_axis1_bool_object() -> typing.Any:
    ...

def take_2d_axis1_float32_float32() -> typing.Any:
    ...

def take_2d_axis1_float32_float64() -> typing.Any:
    ...

def take_2d_axis1_float64_float64() -> typing.Any:
    ...

def take_2d_axis1_int16_float64() -> typing.Any:
    ...

def take_2d_axis1_int16_int16() -> typing.Any:
    ...

def take_2d_axis1_int16_int32() -> typing.Any:
    ...

def take_2d_axis1_int16_int64() -> typing.Any:
    ...

def take_2d_axis1_int32_float64() -> typing.Any:
    ...

def take_2d_axis1_int32_int32() -> typing.Any:
    ...

def take_2d_axis1_int32_int64() -> typing.Any:
    ...

def take_2d_axis1_int64_float64() -> typing.Any:
    ...

def take_2d_axis1_int64_int64() -> typing.Any:
    ...

def take_2d_axis1_int8_float64() -> typing.Any:
    ...

def take_2d_axis1_int8_int32() -> typing.Any:
    ...

def take_2d_axis1_int8_int64() -> typing.Any:
    ...

def take_2d_axis1_int8_int8() -> typing.Any:
    ...

def take_2d_axis1_object_object() -> typing.Any:
    ...

def take_2d_multi_bool_bool() -> typing.Any:
    ...

def take_2d_multi_bool_object() -> typing.Any:
    ...

def take_2d_multi_float32_float32() -> typing.Any:
    ...

def take_2d_multi_float32_float64() -> typing.Any:
    ...

def take_2d_multi_float64_float64() -> typing.Any:
    ...

def take_2d_multi_int16_float64() -> typing.Any:
    ...

def take_2d_multi_int16_int16() -> typing.Any:
    ...

def take_2d_multi_int16_int32() -> typing.Any:
    ...

def take_2d_multi_int16_int64() -> typing.Any:
    ...

def take_2d_multi_int32_float64() -> typing.Any:
    ...

def take_2d_multi_int32_int32() -> typing.Any:
    ...

def take_2d_multi_int32_int64() -> typing.Any:
    ...

def take_2d_multi_int64_float64() -> typing.Any:
    ...

def take_2d_multi_int64_int64() -> typing.Any:
    ...

def take_2d_multi_int8_float64() -> typing.Any:
    ...

def take_2d_multi_int8_int32() -> typing.Any:
    ...

def take_2d_multi_int8_int64() -> typing.Any:
    ...

def take_2d_multi_int8_int8() -> typing.Any:
    ...

def take_2d_multi_object_object() -> typing.Any:
    ...

tiebreakers: dict
def unique_deltas() -> typing.Any:
    '\n    Efficiently find the unique first-differences of the given array.\n\n    Parameters\n    ----------\n    arr : ndarray[in64_t]\n\n    Returns\n    -------\n    ndarray[int64_t]\n        An ordered ndarray[int64_t]\n    '
    ...

def validate_limit() -> typing.Any:
    '\n    Check that the `limit` argument is a positive integer.\n\n    Parameters\n    ----------\n    nobs : int\n    limit : object\n\n    Returns\n    -------\n    int\n        The limit.\n    '
    ...

def __getattr__(name) -> typing.Any:
    ...

