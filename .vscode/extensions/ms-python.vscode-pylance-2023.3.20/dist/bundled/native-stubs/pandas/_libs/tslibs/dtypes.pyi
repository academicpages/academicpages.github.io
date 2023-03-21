# Python: 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)]
# Library: pandas, version: 1.2.4
# Module: pandas._libs.tslibs.dtypes, version: unspecified
import typing
import builtins as _mod_builtins
import enum as _mod_enum

Enum = _mod_enum.Enum
class FreqGroup(_mod_builtins.object):
    FR_ANN: int
    FR_BUS: int
    FR_DAY: int
    FR_HR: int
    FR_MIN: int
    FR_MS: int
    FR_MTH: int
    FR_NS: int
    FR_QTR: int
    FR_SEC: int
    FR_UND: int
    FR_US: int
    FR_WK: int
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
    
    def get_freq_group(self, code) -> 'int':
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class PeriodDtypeBase(_mod_builtins.object):
    '\n    Similar to an actual dtype, this contains all of the information\n    describing a PeriodDtype in an integer code.\n    '
    def __eq__(self, value) -> bool:
        'Return self==value.'
        ...
    
    def __ge__(self, value) -> bool:
        'Return self>=value.'
        ...
    
    def __gt__(self, value) -> bool:
        'Return self>value.'
        ...
    
    __hash__: typing.Any
    def __init__(self, *args, **kwargs) -> None:
        '\n    Similar to an actual dtype, this contains all of the information\n    describing a PeriodDtype in an integer code.\n    '
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
    
    def __reduce__(self) -> typing.Union[str, typing.Tuple[typing.Any, ...]]:
        ...
    
    def __setstate__(self, state: typing.Any) -> None:
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @property
    def _dtype_code(self) -> typing.Any:
        ...
    
    @property
    def date_offset(self) -> typing.Any:
        '\n        Corresponding DateOffset object.\n\n        This mapping is mainly for backward-compatibility.\n        '
        ...
    
    @property
    def freq_group(self) -> typing.Any:
        ...
    
    @classmethod
    def from_date_offset(cls) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class Resolution(_mod_enum.Enum):
    'An enumeration.'
    RESO_DAY: Resolution
    RESO_HR: Resolution
    RESO_MIN: Resolution
    RESO_MS: Resolution
    RESO_MTH: Resolution
    RESO_NS: Resolution
    RESO_QTR: Resolution
    RESO_SEC: Resolution
    RESO_US: Resolution
    RESO_YR: Resolution
    __members__: mappingproxy
    __module__: str
    def __getattr__(self, name) -> typing.Any:
        ...
    

__doc__: typing.Any
__file__: str
__name__: str
__package__: str
__pyx_capi__: dict
__test__: dict
_attrname_to_abbrevs: dict
_period_code_map: dict
_reverse_period_code_map: dict
def __getattr__(name) -> typing.Any:
    ...

