# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: scipy, version: 1.6.2
# Module: scipy._lib.messagestream, version: unspecified
import typing
import builtins as _mod_builtins

class MessageStream(_mod_builtins.object):
    '\n    Capture messages emitted to FILE* streams. Do this by directing them\n    to a temporary file, residing in memory (if possible) or on disk.\n    '
    def __del__(self) -> None:
        ...
    
    def __init__(self, *args, **kwargs) -> None:
        '\n    Capture messages emitted to FILE* streams. Do this by directing them\n    to a temporary file, residing in memory (if possible) or on disk.\n    '
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
    
    def clear(self) -> typing.Any:
        ...
    
    def close(self) -> typing.Any:
        ...
    
    def get(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

__doc__: typing.Any
__file__: str
__name__: str
__package__: str
__test__: dict
def __getattr__(name) -> typing.Any:
    ...

