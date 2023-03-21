# Python: 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)]
# Library: pandas, version: 1.2.4
# Module: pandas._libs.properties, version: unspecified
import typing
import builtins as _mod_builtins

class AxisProperty(_mod_builtins.object):
    def __delete__(self, instance) -> typing.Any:
        'Delete an attribute of instance.'
        ...
    
    def __get__(self, instance, owner) -> AxisProperty:
        'Return an attribute of instance, which is of type owner.'
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __reduce__(self) -> typing.Union[str, typing.Tuple[typing.Any, ...]]:
        ...
    
    def __set__(self, instance, value) -> None:
        'Set an attribute of instance to value.'
        ...
    
    def __setstate__(self, state: typing.Any) -> None:
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @property
    def axis(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class CachedProperty(_mod_builtins.object):
    def __delete__(self, instance) -> typing.Any:
        'Delete an attribute of instance.'
        ...
    
    def __get__(self, instance, owner) -> CachedProperty:
        'Return an attribute of instance, which is of type owner.'
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __reduce__(self) -> typing.Union[str, typing.Tuple[typing.Any, ...]]:
        ...
    
    def __set__(self, instance, value) -> None:
        'Set an attribute of instance to value.'
        ...
    
    def __setstate__(self, state: typing.Any) -> None:
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @property
    def func(self) -> typing.Any:
        ...
    
    @property
    def name(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

__doc__: typing.Any
__file__: str
__name__: str
__package__: str
def __pyx_unpickle_AxisProperty() -> typing.Any:
    ...

def __pyx_unpickle_CachedProperty() -> typing.Any:
    ...

__test__: dict
cache_readonly: CachedProperty
def __getattr__(name) -> typing.Any:
    ...

