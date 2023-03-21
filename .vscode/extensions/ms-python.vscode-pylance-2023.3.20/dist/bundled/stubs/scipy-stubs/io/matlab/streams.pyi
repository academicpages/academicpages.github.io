# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: scipy, version: 1.6.2
# Module: scipy.io.matlab.streams, version: unspecified
import typing
import builtins as _mod_builtins

BLOCK_SIZE: int
class GenericStream(_mod_builtins.object):
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
    
    def all_data_read(self) -> typing.Any:
        ...
    
    def read(self) -> typing.Any:
        ...
    
    def seek(self) -> typing.Any:
        ...
    
    def tell(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class ZlibInputStream(GenericStream):
    '\n    File-like object uncompressing bytes from a zlib compressed stream.\n\n    Parameters\n    ----------\n    stream : file-like\n        Stream to read compressed data from.\n    max_length : int\n        Maximum number of bytes to read from the stream.\n\n    Notes\n    -----\n    Some matlab files contain zlib streams without valid Z_STREAM_END\n    termination.  To get round this, we use the decompressobj object, that\n    allows you to decode an incomplete stream.  See discussion at\n    https://bugs.python.org/issue8672\n\n    '
    def __init__(self, *args, **kwargs) -> None:
        '\n    File-like object uncompressing bytes from a zlib compressed stream.\n\n    Parameters\n    ----------\n    stream : file-like\n        Stream to read compressed data from.\n    max_length : int\n        Maximum number of bytes to read from the stream.\n\n    Notes\n    -----\n    Some matlab files contain zlib streams without valid Z_STREAM_END\n    termination.  To get round this, we use the decompressobj object, that\n    allows you to decode an incomplete stream.  See discussion at\n    https://bugs.python.org/issue8672\n\n    '
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
    
    def all_data_read(self) -> typing.Any:
        ...
    
    def read(self) -> typing.Any:
        ...
    
    def seek(self) -> typing.Any:
        ...
    
    def tell(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

__doc__: typing.Any
__file__: str
__name__: str
__package__: str
__pyx_capi__: dict
def __pyx_unpickle_GenericStream() -> typing.Any:
    ...

def __pyx_unpickle_ZlibInputStream() -> typing.Any:
    ...

__test__: dict
def _read_into() -> typing.Any:
    ...

def _read_string() -> typing.Any:
    ...

def make_stream() -> typing.Any:
    ' Make stream of correct type for file-like `fobj`\n    '
    ...

def __getattr__(name) -> typing.Any:
    ...

