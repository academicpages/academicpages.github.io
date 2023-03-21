# Python: 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)]
# Library: pandas, version: 1.2.4
# Module: pandas._libs.index, version: unspecified
import typing
import builtins as _mod_builtins

class BaseMultiIndexCodesEngine(_mod_builtins.object):
    '\n    Base class for MultiIndexUIntEngine and MultiIndexPyIntEngine, which\n    represent each label in a MultiIndex as an integer, by juxtaposing the bits\n    encoding each level, with appropriate offsets.\n\n    For instance: if 3 levels have respectively 3, 6 and 1 possible values,\n    then their labels can be represented using respectively 2, 3 and 1 bits,\n    as follows:\n     _ _ _ _____ _ __ __ __\n    |0|0|0| ... |0| 0|a1|a0| -> offset 0 (first level)\n     — — — ————— — —— —— ——\n    |0|0|0| ... |0|b2|b1|b0| -> offset 2 (bits required for first level)\n     — — — ————— — —— —— ——\n    |0|0|0| ... |0| 0| 0|c0| -> offset 5 (bits required for first two levels)\n     ‾ ‾ ‾ ‾‾‾‾‾ ‾ ‾‾ ‾‾ ‾‾\n    and the resulting unsigned integer representation will be:\n     _ _ _ _____ _ __ __ __ __ __ __\n    |0|0|0| ... |0|c0|b2|b1|b0|a1|a0|\n     ‾ ‾ ‾ ‾‾‾‾‾ ‾ ‾‾ ‾‾ ‾‾ ‾‾ ‾‾ ‾‾\n\n    Offsets are calculated at initialization, labels are transformed by method\n    _codes_to_ints.\n\n    Keys are located by first locating each component against the respective\n    level, then locating (the integer representation of) codes.\n    '
    def __contains__(self, key) -> bool:
        'Return key in self.'
        ...
    
    def __init__(self) -> None:
        '\n        Parameters\n        ----------\n        levels : list-like of numpy arrays\n            Levels of the MultiIndex.\n        labels : list-like of numpy arrays of integer dtype\n            Labels of the MultiIndex.\n        offsets : numpy array of uint64 dtype\n            Pre-calculated offsets, one for each level of the index.\n        '
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
    
    def _codes_to_ints(self) -> typing.Any:
        ...
    
    def _extract_level_codes(self) -> typing.Any:
        '\n        Map the requested list of (tuple) keys to their integer representations\n        for searching in the underlying integer index.\n\n        Parameters\n        ----------\n        target : list-like of keys\n            Each key is a tuple, with a label for each level of the index.\n\n        Returns\n        ------\n        int_keys : 1-dimensional array of dtype uint64 or object\n            Integers representing one combination each\n        '
        ...
    
    def get_indexer(self) -> typing.Any:
        '\n        Returns an array giving the positions of each value of `target` in\n        `values`, where -1 represents a value in `target` which does not\n        appear in `values`\n\n        If `method` is "backfill" then the position for a value in `target`\n        which does not appear in `values` is that of the next greater value\n        in `values` (if one exists), and -1 if there is no such value.\n\n        Similarly, if the method is "pad" then the position for a value in\n        `target` which does not appear in `values` is that of the next smaller\n        value in `values` (if one exists), and -1 if there is no such value.\n\n        Parameters\n        ----------\n        target: list-like of tuples\n            need not be sorted, but all must have the same length, which must be\n            the same as the length of all tuples in `values`\n        values : list-like of tuples\n            must be sorted and all have the same length.  Should be the set of\n            the MultiIndex\'s values.  Needed only if `method` is not None\n        method: string\n            "backfill" or "pad"\n        limit: int, optional\n            if provided, limit the number of fills to this value\n\n        Returns\n        -------\n        np.ndarray[int64_t, ndim=1] of the indexer of `target` into `values`,\n        filled with the `method` (and optionally `limit`) specified\n        '
        ...
    
    def get_indexer_no_fill(self) -> typing.Any:
        '\n        Returns an array giving the positions of each value of `target` in\n        `self.values`, where -1 represents a value in `target` which does not\n        appear in `self.values`\n\n        Parameters\n        ----------\n        target : list-like of keys\n            Each key is a tuple, with a label for each level of the index\n\n        Returns\n        -------\n        np.ndarray[int64_t, ndim=1] of the indexer of `target` into\n        `self.values`\n        '
        ...
    
    def get_indexer_non_unique(self) -> typing.Any:
        ...
    
    def get_loc(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class DatetimeEngine(Int64Engine):
    def __contains__(self, key) -> bool:
        'Return key in self.'
        ...
    
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
    
    def get_backfill_indexer(self) -> typing.Any:
        ...
    
    def get_indexer(self) -> typing.Any:
        ...
    
    def get_indexer_non_unique(self) -> typing.Any:
        ...
    
    def get_loc(self) -> typing.Any:
        ...
    
    def get_pad_indexer(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class Float32Engine(IndexEngine):
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
    

class Float64Engine(IndexEngine):
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
    

class IndexEngine(_mod_builtins.object):
    def __contains__(self, key) -> bool:
        'Return key in self.'
        ...
    
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
    
    def __sizeof__(self) -> int:
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def clear_mapping(self) -> typing.Any:
        ...
    
    def get_backfill_indexer(self) -> typing.Any:
        ...
    
    def get_indexer(self) -> typing.Any:
        ...
    
    def get_indexer_non_unique(self) -> typing.Any:
        '\n        Return an indexer suitable for taking from a non unique index\n        return the labels in the same order as the target\n        and a missing indexer into the targets (which correspond\n        to the -1 indices in the results\n        '
        ...
    
    def get_loc(self) -> typing.Any:
        ...
    
    def get_pad_indexer(self) -> typing.Any:
        ...
    
    @property
    def is_mapping_populated(self) -> typing.Any:
        ...
    
    @property
    def is_monotonic_decreasing(self) -> typing.Any:
        ...
    
    @property
    def is_monotonic_increasing(self) -> typing.Any:
        ...
    
    @property
    def is_unique(self) -> typing.Any:
        ...
    
    @property
    def mapping(self) -> typing.Any:
        ...
    
    @property
    def over_size_threshold(self) -> typing.Any:
        ...
    
    def sizeof(self) -> typing.Any:
        ' return the sizeof our mapping '
        ...
    
    @property
    def vgetter(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class Int16Engine(IndexEngine):
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
    

class Int32Engine(IndexEngine):
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
    

class Int64Engine(IndexEngine):
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
    

class Int8Engine(IndexEngine):
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
    

class ObjectEngine(IndexEngine):
    '\n    Index Engine for use with object-dtype Index, namely the base class Index.\n    '
    def __init__(self, *args, **kwargs) -> None:
        '\n    Index Engine for use with object-dtype Index, namely the base class Index.\n    '
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
    

class PeriodEngine(Int64Engine):
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
    
    def get_loc(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class TimedeltaEngine(DatetimeEngine):
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
    

class UInt16Engine(IndexEngine):
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
    

class UInt32Engine(IndexEngine):
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
    

class UInt64Engine(IndexEngine):
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
    

class UInt8Engine(IndexEngine):
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
    

_SIZE_CUTOFF: int
__doc__: typing.Any
__file__: str
__name__: str
__package__: str
def __pyx_unpickle_BaseMultiIndexCodesEngine() -> typing.Any:
    ...

def __pyx_unpickle_DatetimeEngine() -> typing.Any:
    ...

def __pyx_unpickle_Enum() -> typing.Any:
    ...

def __pyx_unpickle_Float32Engine() -> typing.Any:
    ...

def __pyx_unpickle_Float64Engine() -> typing.Any:
    ...

def __pyx_unpickle_IndexEngine() -> typing.Any:
    ...

def __pyx_unpickle_Int16Engine() -> typing.Any:
    ...

def __pyx_unpickle_Int32Engine() -> typing.Any:
    ...

def __pyx_unpickle_Int64Engine() -> typing.Any:
    ...

def __pyx_unpickle_Int8Engine() -> typing.Any:
    ...

def __pyx_unpickle_ObjectEngine() -> typing.Any:
    ...

def __pyx_unpickle_PeriodEngine() -> typing.Any:
    ...

def __pyx_unpickle_TimedeltaEngine() -> typing.Any:
    ...

def __pyx_unpickle_UInt16Engine() -> typing.Any:
    ...

def __pyx_unpickle_UInt32Engine() -> typing.Any:
    ...

def __pyx_unpickle_UInt64Engine() -> typing.Any:
    ...

def __pyx_unpickle_UInt8Engine() -> typing.Any:
    ...

__test__: dict
def checknull() -> typing.Any:
    '\n    Return boolean describing of the input is NA-like, defined here as any\n    of:\n     - None\n     - nan\n     - NaT\n     - np.datetime64 representation of NaT\n     - np.timedelta64 representation of NaT\n     - NA\n\n    Parameters\n    ----------\n    val : object\n\n    Returns\n    -------\n    bool\n\n    Notes\n    -----\n    The difference between `checknull` and `checknull_old` is that `checknull`\n    does *not* consider INF or NEGINF to be NA.\n    '
    ...

def __getattr__(name) -> typing.Any:
    ...

