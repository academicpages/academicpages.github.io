# Python: 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)]
# Library: pandas, version: 1.2.4
# Module: pandas._libs.internals, version: unspecified
import typing
import builtins as _mod_builtins
import collections as _mod_collections

class BlockPlacement(_mod_builtins.object):
    def __getitem__(self, key) -> typing.Any:
        'Return self[key].'
        ...
    
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __iter__(self) -> BlockPlacement:
        'Implement iter(self).'
        ...
    
    def __len__(self) -> int:
        'Return len(self).'
        ...
    
    __pyx_vtable__: PyCapsule
    def __reduce__(self) -> typing.Union[str, typing.Tuple[typing.Any, ...]]:
        ...
    
    def __repr__(self) -> str:
        'Return repr(self).'
        ...
    
    def __setstate__(self, state: typing.Any) -> None:
        ...
    
    def __str__(self) -> str:
        'Return str(self).'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def add(self) -> typing.Any:
        ...
    
    def append(self) -> typing.Any:
        ...
    
    @property
    def as_array(self) -> typing.Any:
        ...
    
    @property
    def as_slice(self) -> typing.Any:
        ...
    
    def delete(self) -> typing.Any:
        ...
    
    @property
    def indexer(self) -> typing.Any:
        ...
    
    @property
    def is_slice_like(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

__doc__: typing.Any
__file__: str
__name__: str
__package__: str
def __pyx_unpickle_BlockPlacement() -> typing.Any:
    ...

def __pyx_unpickle_Enum() -> typing.Any:
    ...

__test__: dict
defaultdict = _mod_collections.defaultdict
def ensure_int64() -> typing.Any:
    ...

def get_blkno_indexers() -> typing.Any:
    '\n    Enumerate contiguous runs of integers in ndarray.\n\n    Iterate over elements of `blknos` yielding ``(blkno, slice(start, stop))``\n    pairs for each contiguous run found.\n\n    If `group` is True and there is more than one run for a certain blkno,\n    ``(blkno, array)`` with an array containing positions of all elements equal\n    to blkno.\n\n    Returns\n    -------\n    iter : iterator of (int, slice or array)\n    '
    ...

def get_blkno_placements() -> typing.Any:
    '\n    Parameters\n    ----------\n    blknos : array of int64\n    group : bool, default True\n\n    Returns\n    -------\n    iterator\n        yield (BlockPlacement, blkno)\n    '
    ...

def slice_len() -> typing.Any:
    '\n    Get length of a bounded slice.\n\n    The slice must not have any "open" bounds that would create dependency on\n    container size, i.e.:\n    - if ``s.step is None or s.step > 0``, ``s.stop`` is not ``None``\n    - if ``s.step < 0``, ``s.start`` is not ``None``\n\n    Otherwise, the result is unreliable.\n    '
    ...

def __getattr__(name) -> typing.Any:
    ...

