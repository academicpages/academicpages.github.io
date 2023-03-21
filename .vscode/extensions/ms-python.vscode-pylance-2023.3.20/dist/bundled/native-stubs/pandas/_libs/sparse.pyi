# Python: 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)]
# Library: pandas, version: 1.2.4
# Module: pandas._libs.sparse, version: unspecified
import typing
import builtins as _mod_builtins

class BlockIndex(SparseIndex):
    '\n    Object for holding block-based sparse indexing information\n\n    Parameters\n    ----------\n    '
    def __init__(self, *args, **kwargs) -> None:
        '\n    Object for holding block-based sparse indexing information\n\n    Parameters\n    ----------\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    def __reduce__(self) -> typing.Union[str, typing.Tuple[typing.Any, ...]]:
        ...
    
    def __repr__(self) -> str:
        'Return repr(self).'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @property
    def blengths(self) -> typing.Any:
        ...
    
    @property
    def blocs(self) -> typing.Any:
        ...
    
    def check_integrity(self) -> typing.Any:
        '\n        Check:\n        - Locations are in ascending order\n        - No overlapping blocks\n        - Blocks to not start after end of index, nor extend beyond end\n        '
        ...
    
    def equals(self) -> typing.Any:
        ...
    
    def intersect(self) -> typing.Any:
        '\n        Intersect two BlockIndex objects\n\n        Returns\n        -------\n        BlockIndex\n        '
        ...
    
    @property
    def length(self) -> typing.Any:
        ...
    
    def lookup(self) -> typing.Any:
        '\n        Return the internal location if value exists on given index.\n        Return -1 otherwise.\n        '
        ...
    
    def lookup_array(self) -> typing.Any:
        '\n        Vectorized lookup, returns ndarray[int32_t]\n        '
        ...
    
    def make_union(self) -> typing.Any:
        '\n        Combine together two BlockIndex objects, accepting indices if contained\n        in one or the other\n\n        Parameters\n        ----------\n        other : SparseIndex\n\n        Notes\n        -----\n        union is a protected keyword in Cython, hence make_union\n\n        Returns\n        -------\n        BlockIndex\n        '
        ...
    
    @property
    def nblocks(self) -> typing.Any:
        ...
    
    @property
    def nbytes(self) -> typing.Any:
        ...
    
    @property
    def ngaps(self) -> typing.Any:
        ...
    
    @property
    def npoints(self) -> typing.Any:
        ...
    
    def put(self) -> typing.Any:
        ...
    
    def reindex(self) -> typing.Any:
        ...
    
    def take(self) -> typing.Any:
        ...
    
    def to_block_index(self) -> typing.Any:
        ...
    
    def to_int_index(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class BlockMerge(_mod_builtins.object):
    '\n    Object-oriented approach makes sharing state between recursive functions a\n    lot easier and reduces code duplication\n    '
    def __init__(self, *args, **kwargs) -> None:
        '\n    Object-oriented approach makes sharing state between recursive functions a\n    lot easier and reduces code duplication\n    '
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
    

class BlockUnion(BlockMerge):
    '\n    Object-oriented approach makes sharing state between recursive functions a\n    lot easier and reduces code duplication\n    '
    def __init__(self, *args, **kwargs) -> None:
        '\n    Object-oriented approach makes sharing state between recursive functions a\n    lot easier and reduces code duplication\n    '
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
    

class IntIndex(SparseIndex):
    '\n    Object for holding exact integer sparse indexing information\n\n    Parameters\n    ----------\n    length : integer\n    indices : array-like\n        Contains integers corresponding to the indices.\n    check_integrity : bool, default=True\n        Check integrity of the input.\n    '
    def __init__(self, *args, **kwargs) -> None:
        '\n    Object for holding exact integer sparse indexing information\n\n    Parameters\n    ----------\n    length : integer\n    indices : array-like\n        Contains integers corresponding to the indices.\n    check_integrity : bool, default=True\n        Check integrity of the input.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    def __reduce__(self) -> typing.Union[str, typing.Tuple[typing.Any, ...]]:
        ...
    
    def __repr__(self) -> str:
        'Return repr(self).'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def check_integrity(self) -> typing.Any:
        '\n        Checks the following:\n\n        - Indices are strictly ascending\n        - Number of indices is at most self.length\n        - Indices are at least 0 and at most the total length less one\n\n        A ValueError is raised if any of these conditions is violated.\n        '
        ...
    
    def equals(self) -> typing.Any:
        ...
    
    @property
    def indices(self) -> typing.Any:
        ...
    
    def intersect(self) -> typing.Any:
        ...
    
    @property
    def length(self) -> typing.Any:
        ...
    
    def lookup(self) -> typing.Any:
        '\n        Return the internal location if value exists on given index.\n        Return -1 otherwise.\n        '
        ...
    
    def lookup_array(self) -> typing.Any:
        '\n        Vectorized lookup, returns ndarray[int32_t]\n        '
        ...
    
    def make_union(self) -> typing.Any:
        ...
    
    @property
    def nbytes(self) -> typing.Any:
        ...
    
    @property
    def ngaps(self) -> typing.Any:
        ...
    
    @property
    def npoints(self) -> typing.Any:
        ...
    
    def put(self) -> typing.Any:
        ...
    
    def reindex(self) -> typing.Any:
        ...
    
    def take(self) -> typing.Any:
        ...
    
    def to_block_index(self) -> typing.Any:
        ...
    
    def to_int_index(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class SparseIndex(_mod_builtins.object):
    '\n    Abstract superclass for sparse index types.\n    '
    def __init__(self, *args, **kwargs) -> None:
        '\n    Abstract superclass for sparse index types.\n    '
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
    

__doc__: typing.Any
__file__: str
__name__: str
__package__: str
def __pyx_unpickle_BlockMerge() -> typing.Any:
    ...

def __pyx_unpickle_BlockUnion() -> typing.Any:
    ...

def __pyx_unpickle_Enum() -> typing.Any:
    ...

def __pyx_unpickle_SparseIndex() -> typing.Any:
    ...

__test__: dict
def get_blocks() -> typing.Any:
    ...

def make_mask_object_ndarray() -> typing.Any:
    ...

def sparse_add_float64() -> typing.Any:
    ...

def sparse_add_int64() -> typing.Any:
    ...

def sparse_and_int64() -> typing.Any:
    ...

def sparse_and_uint8() -> typing.Any:
    ...

def sparse_div_float64() -> typing.Any:
    ...

def sparse_div_int64() -> typing.Any:
    ...

def sparse_eq_float64() -> typing.Any:
    ...

def sparse_eq_int64() -> typing.Any:
    ...

def sparse_fill_add_float64() -> typing.Any:
    ...

def sparse_fill_add_int64() -> typing.Any:
    ...

def sparse_fill_and_int64() -> typing.Any:
    ...

def sparse_fill_and_uint8() -> typing.Any:
    ...

def sparse_fill_div_float64() -> typing.Any:
    ...

def sparse_fill_div_int64() -> typing.Any:
    ...

def sparse_fill_eq_float64() -> typing.Any:
    ...

def sparse_fill_eq_int64() -> typing.Any:
    ...

def sparse_fill_floordiv_float64() -> typing.Any:
    ...

def sparse_fill_floordiv_int64() -> typing.Any:
    ...

def sparse_fill_ge_float64() -> typing.Any:
    ...

def sparse_fill_ge_int64() -> typing.Any:
    ...

def sparse_fill_gt_float64() -> typing.Any:
    ...

def sparse_fill_gt_int64() -> typing.Any:
    ...

def sparse_fill_le_float64() -> typing.Any:
    ...

def sparse_fill_le_int64() -> typing.Any:
    ...

def sparse_fill_lt_float64() -> typing.Any:
    ...

def sparse_fill_lt_int64() -> typing.Any:
    ...

def sparse_fill_mod_float64() -> typing.Any:
    ...

def sparse_fill_mod_int64() -> typing.Any:
    ...

def sparse_fill_mul_float64() -> typing.Any:
    ...

def sparse_fill_mul_int64() -> typing.Any:
    ...

def sparse_fill_ne_float64() -> typing.Any:
    ...

def sparse_fill_ne_int64() -> typing.Any:
    ...

def sparse_fill_or_int64() -> typing.Any:
    ...

def sparse_fill_or_uint8() -> typing.Any:
    ...

def sparse_fill_pow_float64() -> typing.Any:
    ...

def sparse_fill_pow_int64() -> typing.Any:
    ...

def sparse_fill_sub_float64() -> typing.Any:
    ...

def sparse_fill_sub_int64() -> typing.Any:
    ...

def sparse_fill_truediv_float64() -> typing.Any:
    ...

def sparse_fill_truediv_int64() -> typing.Any:
    ...

def sparse_fill_xor_int64() -> typing.Any:
    ...

def sparse_fill_xor_uint8() -> typing.Any:
    ...

def sparse_floordiv_float64() -> typing.Any:
    ...

def sparse_floordiv_int64() -> typing.Any:
    ...

def sparse_ge_float64() -> typing.Any:
    ...

def sparse_ge_int64() -> typing.Any:
    ...

def sparse_gt_float64() -> typing.Any:
    ...

def sparse_gt_int64() -> typing.Any:
    ...

def sparse_le_float64() -> typing.Any:
    ...

def sparse_le_int64() -> typing.Any:
    ...

def sparse_lt_float64() -> typing.Any:
    ...

def sparse_lt_int64() -> typing.Any:
    ...

def sparse_mod_float64() -> typing.Any:
    ...

def sparse_mod_int64() -> typing.Any:
    ...

def sparse_mul_float64() -> typing.Any:
    ...

def sparse_mul_int64() -> typing.Any:
    ...

def sparse_ne_float64() -> typing.Any:
    ...

def sparse_ne_int64() -> typing.Any:
    ...

def sparse_or_int64() -> typing.Any:
    ...

def sparse_or_uint8() -> typing.Any:
    ...

def sparse_pow_float64() -> typing.Any:
    ...

def sparse_pow_int64() -> typing.Any:
    ...

def sparse_sub_float64() -> typing.Any:
    ...

def sparse_sub_int64() -> typing.Any:
    ...

def sparse_truediv_float64() -> typing.Any:
    ...

def sparse_truediv_int64() -> typing.Any:
    ...

def sparse_xor_int64() -> typing.Any:
    ...

def sparse_xor_uint8() -> typing.Any:
    ...

def __getattr__(name) -> typing.Any:
    ...

