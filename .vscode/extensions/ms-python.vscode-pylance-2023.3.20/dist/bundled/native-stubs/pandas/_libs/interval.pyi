# Python: 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)]
# Library: pandas, version: 1.2.4
# Module: pandas._libs.interval, version: unspecified
import typing
import builtins as _mod_builtins

class Float64ClosedBothIntervalNode(_mod_builtins.object):
    'Non-terminal node for an IntervalTree\n\n    Categorizes intervals by those that fall to the left, those that fall to\n    the right, and those that overlap with the pivot.\n    '
    def __init__(self, *args, **kwargs) -> None:
        'Non-terminal node for an IntervalTree\n\n    Categorizes intervals by those that fall to the left, those that fall to\n    the right, and those that overlap with the pivot.\n    '
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
    
    def __setstate__(self, state: typing.Any) -> None:
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @property
    def center_left_indices(self) -> typing.Any:
        ...
    
    @property
    def center_left_values(self) -> typing.Any:
        ...
    
    @property
    def center_right_indices(self) -> typing.Any:
        ...
    
    @property
    def center_right_values(self) -> typing.Any:
        ...
    
    def counts(self) -> typing.Any:
        '\n        Inspect counts on this node\n        useful for debugging purposes\n        '
        ...
    
    @property
    def indices(self) -> typing.Any:
        ...
    
    @property
    def is_leaf_node(self) -> typing.Any:
        ...
    
    @property
    def leaf_size(self) -> typing.Any:
        ...
    
    @property
    def left(self) -> typing.Any:
        ...
    
    @property
    def left_node(self) -> typing.Any:
        ...
    
    @property
    def max_right(self) -> typing.Any:
        ...
    
    @property
    def min_left(self) -> typing.Any:
        ...
    
    @property
    def n_center(self) -> typing.Any:
        ...
    
    @property
    def n_elements(self) -> typing.Any:
        ...
    
    @property
    def pivot(self) -> typing.Any:
        ...
    
    def query(self, result, point) -> typing.Any:
        'Recursively query this node and its sub-nodes for intervals that\n        overlap with the query point.\n        '
        ...
    
    @property
    def right(self) -> typing.Any:
        ...
    
    @property
    def right_node(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class Float64ClosedLeftIntervalNode(_mod_builtins.object):
    'Non-terminal node for an IntervalTree\n\n    Categorizes intervals by those that fall to the left, those that fall to\n    the right, and those that overlap with the pivot.\n    '
    def __init__(self, *args, **kwargs) -> None:
        'Non-terminal node for an IntervalTree\n\n    Categorizes intervals by those that fall to the left, those that fall to\n    the right, and those that overlap with the pivot.\n    '
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
    
    def __setstate__(self, state: typing.Any) -> None:
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @property
    def center_left_indices(self) -> typing.Any:
        ...
    
    @property
    def center_left_values(self) -> typing.Any:
        ...
    
    @property
    def center_right_indices(self) -> typing.Any:
        ...
    
    @property
    def center_right_values(self) -> typing.Any:
        ...
    
    def counts(self) -> typing.Any:
        '\n        Inspect counts on this node\n        useful for debugging purposes\n        '
        ...
    
    @property
    def indices(self) -> typing.Any:
        ...
    
    @property
    def is_leaf_node(self) -> typing.Any:
        ...
    
    @property
    def leaf_size(self) -> typing.Any:
        ...
    
    @property
    def left(self) -> typing.Any:
        ...
    
    @property
    def left_node(self) -> typing.Any:
        ...
    
    @property
    def max_right(self) -> typing.Any:
        ...
    
    @property
    def min_left(self) -> typing.Any:
        ...
    
    @property
    def n_center(self) -> typing.Any:
        ...
    
    @property
    def n_elements(self) -> typing.Any:
        ...
    
    @property
    def pivot(self) -> typing.Any:
        ...
    
    def query(self, result, point) -> typing.Any:
        'Recursively query this node and its sub-nodes for intervals that\n        overlap with the query point.\n        '
        ...
    
    @property
    def right(self) -> typing.Any:
        ...
    
    @property
    def right_node(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class Float64ClosedNeitherIntervalNode(_mod_builtins.object):
    'Non-terminal node for an IntervalTree\n\n    Categorizes intervals by those that fall to the left, those that fall to\n    the right, and those that overlap with the pivot.\n    '
    def __init__(self, *args, **kwargs) -> None:
        'Non-terminal node for an IntervalTree\n\n    Categorizes intervals by those that fall to the left, those that fall to\n    the right, and those that overlap with the pivot.\n    '
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
    
    def __setstate__(self, state: typing.Any) -> None:
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @property
    def center_left_indices(self) -> typing.Any:
        ...
    
    @property
    def center_left_values(self) -> typing.Any:
        ...
    
    @property
    def center_right_indices(self) -> typing.Any:
        ...
    
    @property
    def center_right_values(self) -> typing.Any:
        ...
    
    def counts(self) -> typing.Any:
        '\n        Inspect counts on this node\n        useful for debugging purposes\n        '
        ...
    
    @property
    def indices(self) -> typing.Any:
        ...
    
    @property
    def is_leaf_node(self) -> typing.Any:
        ...
    
    @property
    def leaf_size(self) -> typing.Any:
        ...
    
    @property
    def left(self) -> typing.Any:
        ...
    
    @property
    def left_node(self) -> typing.Any:
        ...
    
    @property
    def max_right(self) -> typing.Any:
        ...
    
    @property
    def min_left(self) -> typing.Any:
        ...
    
    @property
    def n_center(self) -> typing.Any:
        ...
    
    @property
    def n_elements(self) -> typing.Any:
        ...
    
    @property
    def pivot(self) -> typing.Any:
        ...
    
    def query(self, result, point) -> typing.Any:
        'Recursively query this node and its sub-nodes for intervals that\n        overlap with the query point.\n        '
        ...
    
    @property
    def right(self) -> typing.Any:
        ...
    
    @property
    def right_node(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class Float64ClosedRightIntervalNode(_mod_builtins.object):
    'Non-terminal node for an IntervalTree\n\n    Categorizes intervals by those that fall to the left, those that fall to\n    the right, and those that overlap with the pivot.\n    '
    def __init__(self, *args, **kwargs) -> None:
        'Non-terminal node for an IntervalTree\n\n    Categorizes intervals by those that fall to the left, those that fall to\n    the right, and those that overlap with the pivot.\n    '
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
    
    def __setstate__(self, state: typing.Any) -> None:
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @property
    def center_left_indices(self) -> typing.Any:
        ...
    
    @property
    def center_left_values(self) -> typing.Any:
        ...
    
    @property
    def center_right_indices(self) -> typing.Any:
        ...
    
    @property
    def center_right_values(self) -> typing.Any:
        ...
    
    def counts(self) -> typing.Any:
        '\n        Inspect counts on this node\n        useful for debugging purposes\n        '
        ...
    
    @property
    def indices(self) -> typing.Any:
        ...
    
    @property
    def is_leaf_node(self) -> typing.Any:
        ...
    
    @property
    def leaf_size(self) -> typing.Any:
        ...
    
    @property
    def left(self) -> typing.Any:
        ...
    
    @property
    def left_node(self) -> typing.Any:
        ...
    
    @property
    def max_right(self) -> typing.Any:
        ...
    
    @property
    def min_left(self) -> typing.Any:
        ...
    
    @property
    def n_center(self) -> typing.Any:
        ...
    
    @property
    def n_elements(self) -> typing.Any:
        ...
    
    @property
    def pivot(self) -> typing.Any:
        ...
    
    def query(self, result, point) -> typing.Any:
        'Recursively query this node and its sub-nodes for intervals that\n        overlap with the query point.\n        '
        ...
    
    @property
    def right(self) -> typing.Any:
        ...
    
    @property
    def right_node(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class Int64ClosedBothIntervalNode(_mod_builtins.object):
    'Non-terminal node for an IntervalTree\n\n    Categorizes intervals by those that fall to the left, those that fall to\n    the right, and those that overlap with the pivot.\n    '
    def __init__(self, *args, **kwargs) -> None:
        'Non-terminal node for an IntervalTree\n\n    Categorizes intervals by those that fall to the left, those that fall to\n    the right, and those that overlap with the pivot.\n    '
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
    
    def __setstate__(self, state: typing.Any) -> None:
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @property
    def center_left_indices(self) -> typing.Any:
        ...
    
    @property
    def center_left_values(self) -> typing.Any:
        ...
    
    @property
    def center_right_indices(self) -> typing.Any:
        ...
    
    @property
    def center_right_values(self) -> typing.Any:
        ...
    
    def counts(self) -> typing.Any:
        '\n        Inspect counts on this node\n        useful for debugging purposes\n        '
        ...
    
    @property
    def indices(self) -> typing.Any:
        ...
    
    @property
    def is_leaf_node(self) -> typing.Any:
        ...
    
    @property
    def leaf_size(self) -> typing.Any:
        ...
    
    @property
    def left(self) -> typing.Any:
        ...
    
    @property
    def left_node(self) -> typing.Any:
        ...
    
    @property
    def max_right(self) -> typing.Any:
        ...
    
    @property
    def min_left(self) -> typing.Any:
        ...
    
    @property
    def n_center(self) -> typing.Any:
        ...
    
    @property
    def n_elements(self) -> typing.Any:
        ...
    
    @property
    def pivot(self) -> typing.Any:
        ...
    
    def query(self, result, point) -> typing.Any:
        'Recursively query this node and its sub-nodes for intervals that\n        overlap with the query point.\n        '
        ...
    
    @property
    def right(self) -> typing.Any:
        ...
    
    @property
    def right_node(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class Int64ClosedLeftIntervalNode(_mod_builtins.object):
    'Non-terminal node for an IntervalTree\n\n    Categorizes intervals by those that fall to the left, those that fall to\n    the right, and those that overlap with the pivot.\n    '
    def __init__(self, *args, **kwargs) -> None:
        'Non-terminal node for an IntervalTree\n\n    Categorizes intervals by those that fall to the left, those that fall to\n    the right, and those that overlap with the pivot.\n    '
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
    
    def __setstate__(self, state: typing.Any) -> None:
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @property
    def center_left_indices(self) -> typing.Any:
        ...
    
    @property
    def center_left_values(self) -> typing.Any:
        ...
    
    @property
    def center_right_indices(self) -> typing.Any:
        ...
    
    @property
    def center_right_values(self) -> typing.Any:
        ...
    
    def counts(self) -> typing.Any:
        '\n        Inspect counts on this node\n        useful for debugging purposes\n        '
        ...
    
    @property
    def indices(self) -> typing.Any:
        ...
    
    @property
    def is_leaf_node(self) -> typing.Any:
        ...
    
    @property
    def leaf_size(self) -> typing.Any:
        ...
    
    @property
    def left(self) -> typing.Any:
        ...
    
    @property
    def left_node(self) -> typing.Any:
        ...
    
    @property
    def max_right(self) -> typing.Any:
        ...
    
    @property
    def min_left(self) -> typing.Any:
        ...
    
    @property
    def n_center(self) -> typing.Any:
        ...
    
    @property
    def n_elements(self) -> typing.Any:
        ...
    
    @property
    def pivot(self) -> typing.Any:
        ...
    
    def query(self, result, point) -> typing.Any:
        'Recursively query this node and its sub-nodes for intervals that\n        overlap with the query point.\n        '
        ...
    
    @property
    def right(self) -> typing.Any:
        ...
    
    @property
    def right_node(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class Int64ClosedNeitherIntervalNode(_mod_builtins.object):
    'Non-terminal node for an IntervalTree\n\n    Categorizes intervals by those that fall to the left, those that fall to\n    the right, and those that overlap with the pivot.\n    '
    def __init__(self, *args, **kwargs) -> None:
        'Non-terminal node for an IntervalTree\n\n    Categorizes intervals by those that fall to the left, those that fall to\n    the right, and those that overlap with the pivot.\n    '
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
    
    def __setstate__(self, state: typing.Any) -> None:
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @property
    def center_left_indices(self) -> typing.Any:
        ...
    
    @property
    def center_left_values(self) -> typing.Any:
        ...
    
    @property
    def center_right_indices(self) -> typing.Any:
        ...
    
    @property
    def center_right_values(self) -> typing.Any:
        ...
    
    def counts(self) -> typing.Any:
        '\n        Inspect counts on this node\n        useful for debugging purposes\n        '
        ...
    
    @property
    def indices(self) -> typing.Any:
        ...
    
    @property
    def is_leaf_node(self) -> typing.Any:
        ...
    
    @property
    def leaf_size(self) -> typing.Any:
        ...
    
    @property
    def left(self) -> typing.Any:
        ...
    
    @property
    def left_node(self) -> typing.Any:
        ...
    
    @property
    def max_right(self) -> typing.Any:
        ...
    
    @property
    def min_left(self) -> typing.Any:
        ...
    
    @property
    def n_center(self) -> typing.Any:
        ...
    
    @property
    def n_elements(self) -> typing.Any:
        ...
    
    @property
    def pivot(self) -> typing.Any:
        ...
    
    def query(self, result, point) -> typing.Any:
        'Recursively query this node and its sub-nodes for intervals that\n        overlap with the query point.\n        '
        ...
    
    @property
    def right(self) -> typing.Any:
        ...
    
    @property
    def right_node(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class Int64ClosedRightIntervalNode(_mod_builtins.object):
    'Non-terminal node for an IntervalTree\n\n    Categorizes intervals by those that fall to the left, those that fall to\n    the right, and those that overlap with the pivot.\n    '
    def __init__(self, *args, **kwargs) -> None:
        'Non-terminal node for an IntervalTree\n\n    Categorizes intervals by those that fall to the left, those that fall to\n    the right, and those that overlap with the pivot.\n    '
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
    
    def __setstate__(self, state: typing.Any) -> None:
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @property
    def center_left_indices(self) -> typing.Any:
        ...
    
    @property
    def center_left_values(self) -> typing.Any:
        ...
    
    @property
    def center_right_indices(self) -> typing.Any:
        ...
    
    @property
    def center_right_values(self) -> typing.Any:
        ...
    
    def counts(self) -> typing.Any:
        '\n        Inspect counts on this node\n        useful for debugging purposes\n        '
        ...
    
    @property
    def indices(self) -> typing.Any:
        ...
    
    @property
    def is_leaf_node(self) -> typing.Any:
        ...
    
    @property
    def leaf_size(self) -> typing.Any:
        ...
    
    @property
    def left(self) -> typing.Any:
        ...
    
    @property
    def left_node(self) -> typing.Any:
        ...
    
    @property
    def max_right(self) -> typing.Any:
        ...
    
    @property
    def min_left(self) -> typing.Any:
        ...
    
    @property
    def n_center(self) -> typing.Any:
        ...
    
    @property
    def n_elements(self) -> typing.Any:
        ...
    
    @property
    def pivot(self) -> typing.Any:
        ...
    
    def query(self, result, point) -> typing.Any:
        'Recursively query this node and its sub-nodes for intervals that\n        overlap with the query point.\n        '
        ...
    
    @property
    def right(self) -> typing.Any:
        ...
    
    @property
    def right_node(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class Interval(IntervalMixin):
    "\n    Immutable object implementing an Interval, a bounded slice-like interval.\n\n    Parameters\n    ----------\n    left : orderable scalar\n        Left bound for the interval.\n    right : orderable scalar\n        Right bound for the interval.\n    closed : {'right', 'left', 'both', 'neither'}, default 'right'\n        Whether the interval is closed on the left-side, right-side, both or\n        neither. See the Notes for more detailed explanation.\n\n    See Also\n    --------\n    IntervalIndex : An Index of Interval objects that are all closed on the\n        same side.\n    cut : Convert continuous data into discrete bins (Categorical\n        of Interval objects).\n    qcut : Convert continuous data into bins (Categorical of Interval objects)\n        based on quantiles.\n    Period : Represents a period of time.\n\n    Notes\n    -----\n    The parameters `left` and `right` must be from the same type, you must be\n    able to compare them and they must satisfy ``left <= right``.\n\n    A closed interval (in mathematics denoted by square brackets) contains\n    its endpoints, i.e. the closed interval ``[0, 5]`` is characterized by the\n    conditions ``0 <= x <= 5``. This is what ``closed='both'`` stands for.\n    An open interval (in mathematics denoted by parentheses) does not contain\n    its endpoints, i.e. the open interval ``(0, 5)`` is characterized by the\n    conditions ``0 < x < 5``. This is what ``closed='neither'`` stands for.\n    Intervals can also be half-open or half-closed, i.e. ``[0, 5)`` is\n    described by ``0 <= x < 5`` (``closed='left'``) and ``(0, 5]`` is\n    described by ``0 < x <= 5`` (``closed='right'``).\n\n    Examples\n    --------\n    It is possible to build Intervals of different types, like numeric ones:\n\n    >>> iv = pd.Interval(left=0, right=5)\n    >>> iv\n    Interval(0, 5, closed='right')\n\n    You can check if an element belongs to it\n\n    >>> 2.5 in iv\n    True\n\n    You can test the bounds (``closed='right'``, so ``0 < x <= 5``):\n\n    >>> 0 in iv\n    False\n    >>> 5 in iv\n    True\n    >>> 0.0001 in iv\n    True\n\n    Calculate its length\n\n    >>> iv.length\n    5\n\n    You can operate with `+` and `*` over an Interval and the operation\n    is applied to each of its bounds, so the result depends on the type\n    of the bound elements\n\n    >>> shifted_iv = iv + 3\n    >>> shifted_iv\n    Interval(3, 8, closed='right')\n    >>> extended_iv = iv * 10.0\n    >>> extended_iv\n    Interval(0.0, 50.0, closed='right')\n\n    To create a time interval you can use Timestamps as the bounds\n\n    >>> year_2017 = pd.Interval(pd.Timestamp('2017-01-01 00:00:00'),\n    ...                         pd.Timestamp('2018-01-01 00:00:00'),\n    ...                         closed='left')\n    >>> pd.Timestamp('2017-01-01 00:00') in year_2017\n    True\n    >>> year_2017.length\n    Timedelta('365 days 00:00:00')\n    "
    def __add__(self, value) -> Interval:
        'Return self+value.'
        ...
    
    __array_priority__: int
    def __contains__(self, key) -> bool:
        'Return key in self.'
        ...
    
    def __eq__(self, value) -> bool:
        'Return self==value.'
        ...
    
    def __floordiv__(self, value) -> int:
        'Return self//value.'
        ...
    
    def __ge__(self, value) -> bool:
        'Return self>=value.'
        ...
    
    def __gt__(self, value) -> bool:
        'Return self>value.'
        ...
    
    def __hash__(self) -> int:
        'Return hash(self).'
        ...
    
    def __init__(self, *args, **kwargs) -> None:
        "\n    Immutable object implementing an Interval, a bounded slice-like interval.\n\n    Parameters\n    ----------\n    left : orderable scalar\n        Left bound for the interval.\n    right : orderable scalar\n        Right bound for the interval.\n    closed : {'right', 'left', 'both', 'neither'}, default 'right'\n        Whether the interval is closed on the left-side, right-side, both or\n        neither. See the Notes for more detailed explanation.\n\n    See Also\n    --------\n    IntervalIndex : An Index of Interval objects that are all closed on the\n        same side.\n    cut : Convert continuous data into discrete bins (Categorical\n        of Interval objects).\n    qcut : Convert continuous data into bins (Categorical of Interval objects)\n        based on quantiles.\n    Period : Represents a period of time.\n\n    Notes\n    -----\n    The parameters `left` and `right` must be from the same type, you must be\n    able to compare them and they must satisfy ``left <= right``.\n\n    A closed interval (in mathematics denoted by square brackets) contains\n    its endpoints, i.e. the closed interval ``[0, 5]`` is characterized by the\n    conditions ``0 <= x <= 5``. This is what ``closed='both'`` stands for.\n    An open interval (in mathematics denoted by parentheses) does not contain\n    its endpoints, i.e. the open interval ``(0, 5)`` is characterized by the\n    conditions ``0 < x < 5``. This is what ``closed='neither'`` stands for.\n    Intervals can also be half-open or half-closed, i.e. ``[0, 5)`` is\n    described by ``0 <= x < 5`` (``closed='left'``) and ``(0, 5]`` is\n    described by ``0 < x <= 5`` (``closed='right'``).\n\n    Examples\n    --------\n    It is possible to build Intervals of different types, like numeric ones:\n\n    >>> iv = pd.Interval(left=0, right=5)\n    >>> iv\n    Interval(0, 5, closed='right')\n\n    You can check if an element belongs to it\n\n    >>> 2.5 in iv\n    True\n\n    You can test the bounds (``closed='right'``, so ``0 < x <= 5``):\n\n    >>> 0 in iv\n    False\n    >>> 5 in iv\n    True\n    >>> 0.0001 in iv\n    True\n\n    Calculate its length\n\n    >>> iv.length\n    5\n\n    You can operate with `+` and `*` over an Interval and the operation\n    is applied to each of its bounds, so the result depends on the type\n    of the bound elements\n\n    >>> shifted_iv = iv + 3\n    >>> shifted_iv\n    Interval(3, 8, closed='right')\n    >>> extended_iv = iv * 10.0\n    >>> extended_iv\n    Interval(0.0, 50.0, closed='right')\n\n    To create a time interval you can use Timestamps as the bounds\n\n    >>> year_2017 = pd.Interval(pd.Timestamp('2017-01-01 00:00:00'),\n    ...                         pd.Timestamp('2018-01-01 00:00:00'),\n    ...                         closed='left')\n    >>> pd.Timestamp('2017-01-01 00:00') in year_2017\n    True\n    >>> year_2017.length\n    Timedelta('365 days 00:00:00')\n    "
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
    
    def __mul__(self, value) -> Interval:
        'Return self*value.'
        ...
    
    def __ne__(self, value) -> bool:
        'Return self!=value.'
        ...
    
    def __radd__(self, value) -> Interval:
        'Return value+self.'
        ...
    
    def __reduce__(self) -> typing.Union[str, typing.Tuple[typing.Any, ...]]:
        ...
    
    def __repr__(self) -> str:
        'Return repr(self).'
        ...
    
    def __rfloordiv__(self, value) -> Interval:
        'Return value//self.'
        ...
    
    def __rmul__(self, value) -> Interval:
        'Return value*self.'
        ...
    
    def __rsub__(self, value) -> Interval:
        'Return value-self.'
        ...
    
    def __rtruediv__(self, value) -> Interval:
        'Return value/self.'
        ...
    
    def __str__(self) -> str:
        'Return str(self).'
        ...
    
    def __sub__(self, value) -> Interval:
        'Return self-value.'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __truediv__(self, value) -> float:
        'Return self/value.'
        ...
    
    def _repr_base(self) -> typing.Any:
        ...
    
    _typ: str
    def _validate_endpoint(self) -> typing.Any:
        ...
    
    @property
    def closed(self) -> typing.Any:
        '\n    Whether the interval is closed on the left-side, right-side, both or\n    neither.\n    '
        ...
    
    @property
    def left(self) -> typing.Any:
        '\n    Left bound for the interval.\n    '
        ...
    
    def overlaps(self) -> typing.Any:
        "\n        Check whether two Interval objects overlap.\n\n        Two intervals overlap if they share a common point, including closed\n        endpoints. Intervals that only have an open endpoint in common do not\n        overlap.\n\n        .. versionadded:: 0.24.0\n\n        Parameters\n        ----------\n        other : Interval\n            Interval to check against for an overlap.\n\n        Returns\n        -------\n        bool\n            True if the two intervals overlap.\n\n        See Also\n        --------\n        IntervalArray.overlaps : The corresponding method for IntervalArray.\n        IntervalIndex.overlaps : The corresponding method for IntervalIndex.\n\n        Examples\n        --------\n        >>> i1 = pd.Interval(0, 2)\n        >>> i2 = pd.Interval(1, 3)\n        >>> i1.overlaps(i2)\n        True\n        >>> i3 = pd.Interval(4, 5)\n        >>> i1.overlaps(i3)\n        False\n\n        Intervals that share closed endpoints overlap:\n\n        >>> i4 = pd.Interval(0, 1, closed='both')\n        >>> i5 = pd.Interval(1, 2, closed='both')\n        >>> i4.overlaps(i5)\n        True\n\n        Intervals that only have an open endpoint in common do not overlap:\n\n        >>> i6 = pd.Interval(1, 2, closed='neither')\n        >>> i4.overlaps(i6)\n        False\n        "
        ...
    
    @property
    def right(self) -> typing.Any:
        '\n    Right bound for the interval.\n    '
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class IntervalMixin(_mod_builtins.object):
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
    
    def _check_closed_matches(self) -> typing.Any:
        "\n        Check if the closed attribute of `other` matches.\n\n        Note that 'left' and 'right' are considered different from 'both'.\n\n        Parameters\n        ----------\n        other : Interval, IntervalIndex, IntervalArray\n        name : str\n            Name to use for 'other' in the error message.\n\n        Raises\n        ------\n        ValueError\n            When `other` is not closed exactly the same as self.\n        "
        ...
    
    @property
    def closed_left(self) -> typing.Any:
        '\n        Check if the interval is closed on the left side.\n\n        For the meaning of `closed` and `open` see :class:`~pandas.Interval`.\n\n        Returns\n        -------\n        bool\n            True if the Interval is closed on the left-side.\n        '
        ...
    
    @property
    def closed_right(self) -> typing.Any:
        '\n        Check if the interval is closed on the right side.\n\n        For the meaning of `closed` and `open` see :class:`~pandas.Interval`.\n\n        Returns\n        -------\n        bool\n            True if the Interval is closed on the left-side.\n        '
        ...
    
    @property
    def is_empty(self) -> typing.Any:
        "\n        Indicates if an interval is empty, meaning it contains no points.\n\n        .. versionadded:: 0.25.0\n\n        Returns\n        -------\n        bool or ndarray\n            A boolean indicating if a scalar :class:`Interval` is empty, or a\n            boolean ``ndarray`` positionally indicating if an ``Interval`` in\n            an :class:`~arrays.IntervalArray` or :class:`IntervalIndex` is\n            empty.\n\n        Examples\n        --------\n        An :class:`Interval` that contains points is not empty:\n\n        >>> pd.Interval(0, 1, closed='right').is_empty\n        False\n\n        An ``Interval`` that does not contain any points is empty:\n\n        >>> pd.Interval(0, 0, closed='right').is_empty\n        True\n        >>> pd.Interval(0, 0, closed='left').is_empty\n        True\n        >>> pd.Interval(0, 0, closed='neither').is_empty\n        True\n\n        An ``Interval`` that contains a single point is not empty:\n\n        >>> pd.Interval(0, 0, closed='both').is_empty\n        False\n\n        An :class:`~arrays.IntervalArray` or :class:`IntervalIndex` returns a\n        boolean ``ndarray`` positionally indicating if an ``Interval`` is\n        empty:\n\n        >>> ivs = [pd.Interval(0, 0, closed='neither'),\n        ...        pd.Interval(1, 2, closed='neither')]\n        >>> pd.arrays.IntervalArray(ivs).is_empty\n        array([ True, False])\n\n        Missing values are not considered empty:\n\n        >>> ivs = [pd.Interval(0, 0, closed='neither'), np.nan]\n        >>> pd.IntervalIndex(ivs).is_empty\n        array([ True, False])\n        "
        ...
    
    @property
    def length(self) -> typing.Any:
        '\n        Return the length of the Interval.\n        '
        ...
    
    @property
    def mid(self) -> typing.Any:
        '\n        Return the midpoint of the Interval.\n        '
        ...
    
    @property
    def open_left(self) -> typing.Any:
        '\n        Check if the interval is open on the left side.\n\n        For the meaning of `closed` and `open` see :class:`~pandas.Interval`.\n\n        Returns\n        -------\n        bool\n            True if the Interval is closed on the left-side.\n        '
        ...
    
    @property
    def open_right(self) -> typing.Any:
        '\n        Check if the interval is open on the right side.\n\n        For the meaning of `closed` and `open` see :class:`~pandas.Interval`.\n\n        Returns\n        -------\n        bool\n            True if the Interval is closed on the left-side.\n        '
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class IntervalTree(IntervalMixin):
    'A centered interval tree\n\n    Based off the algorithm described on Wikipedia:\n    https://en.wikipedia.org/wiki/Interval_tree\n\n    we are emulating the IndexEngine interface\n    '
    def __init__(self) -> None:
        "\n        Parameters\n        ----------\n        left, right : np.ndarray[ndim=1]\n            Left and right bounds for each interval. Assumed to contain no\n            NaNs.\n        closed : {'left', 'right', 'both', 'neither'}, optional\n            Whether the intervals are closed on the left-side, right-side, both\n            or neither. Defaults to 'right'.\n        leaf_size : int, optional\n            Parameter that controls when the tree switches from creating nodes\n            to brute-force search. Tune this parameter to optimize query\n            performance.\n        "
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __pyx_fuse_0get_indexer(self) -> typing.Any:
        'Return the positions corresponding to unique intervals that overlap\n        with the given array of scalar targets.\n        '
        ...
    
    def __pyx_fuse_0get_indexer_non_unique(self) -> typing.Any:
        'Return the positions corresponding to intervals that overlap with\n        the given array of scalar targets. Non-unique positions are repeated.\n        '
        ...
    
    def __pyx_fuse_1get_indexer(self) -> typing.Any:
        'Return the positions corresponding to unique intervals that overlap\n        with the given array of scalar targets.\n        '
        ...
    
    def __pyx_fuse_1get_indexer_non_unique(self) -> typing.Any:
        'Return the positions corresponding to intervals that overlap with\n        the given array of scalar targets. Non-unique positions are repeated.\n        '
        ...
    
    def __pyx_fuse_2get_indexer(self) -> typing.Any:
        'Return the positions corresponding to unique intervals that overlap\n        with the given array of scalar targets.\n        '
        ...
    
    def __pyx_fuse_2get_indexer_non_unique(self) -> typing.Any:
        'Return the positions corresponding to intervals that overlap with\n        the given array of scalar targets. Non-unique positions are repeated.\n        '
        ...
    
    def __reduce__(self) -> typing.Union[str, typing.Tuple[typing.Any, ...]]:
        ...
    
    def __repr__(self) -> str:
        'Return repr(self).'
        ...
    
    def __setstate__(self, state: typing.Any) -> None:
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @property
    def _is_overlapping(self) -> typing.Any:
        ...
    
    @property
    def _left_sorter(self) -> typing.Any:
        ...
    
    @property
    def _right_sorter(self) -> typing.Any:
        ...
    
    def clear_mapping(self) -> typing.Any:
        ...
    
    @property
    def closed(self) -> typing.Any:
        ...
    
    @property
    def dtype(self) -> typing.Any:
        ...
    
    def get_indexer(self, target) -> typing.Any:
        'Return the positions corresponding to unique intervals that overlap\n        with the given array of scalar targets.\n        '
        ...
    
    def get_indexer_non_unique(self, target) -> typing.Any:
        'Return the positions corresponding to intervals that overlap with\n        the given array of scalar targets. Non-unique positions are repeated.\n        '
        ...
    
    @property
    def is_monotonic_increasing(self) -> typing.Any:
        '\n        Return True if the IntervalTree is monotonic increasing (only equal or\n        increasing values), else False\n        '
        ...
    
    @property
    def is_overlapping(self) -> typing.Any:
        '\n        Determine if the IntervalTree contains overlapping intervals.\n        Cached as self._is_overlapping.\n        '
        ...
    
    @property
    def left(self) -> typing.Any:
        ...
    
    @property
    def left_sorter(self) -> typing.Any:
        'How to sort the left labels; this is used for binary search\n        '
        ...
    
    @property
    def right(self) -> typing.Any:
        ...
    
    @property
    def right_sorter(self) -> typing.Any:
        'How to sort the right labels\n        '
        ...
    
    @property
    def root(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

NODE_CLASSES: dict
class Uint64ClosedBothIntervalNode(_mod_builtins.object):
    'Non-terminal node for an IntervalTree\n\n    Categorizes intervals by those that fall to the left, those that fall to\n    the right, and those that overlap with the pivot.\n    '
    def __init__(self, *args, **kwargs) -> None:
        'Non-terminal node for an IntervalTree\n\n    Categorizes intervals by those that fall to the left, those that fall to\n    the right, and those that overlap with the pivot.\n    '
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
    
    def __setstate__(self, state: typing.Any) -> None:
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @property
    def center_left_indices(self) -> typing.Any:
        ...
    
    @property
    def center_left_values(self) -> typing.Any:
        ...
    
    @property
    def center_right_indices(self) -> typing.Any:
        ...
    
    @property
    def center_right_values(self) -> typing.Any:
        ...
    
    def counts(self) -> typing.Any:
        '\n        Inspect counts on this node\n        useful for debugging purposes\n        '
        ...
    
    @property
    def indices(self) -> typing.Any:
        ...
    
    @property
    def is_leaf_node(self) -> typing.Any:
        ...
    
    @property
    def leaf_size(self) -> typing.Any:
        ...
    
    @property
    def left(self) -> typing.Any:
        ...
    
    @property
    def left_node(self) -> typing.Any:
        ...
    
    @property
    def max_right(self) -> typing.Any:
        ...
    
    @property
    def min_left(self) -> typing.Any:
        ...
    
    @property
    def n_center(self) -> typing.Any:
        ...
    
    @property
    def n_elements(self) -> typing.Any:
        ...
    
    @property
    def pivot(self) -> typing.Any:
        ...
    
    def query(self, result, point) -> typing.Any:
        'Recursively query this node and its sub-nodes for intervals that\n        overlap with the query point.\n        '
        ...
    
    @property
    def right(self) -> typing.Any:
        ...
    
    @property
    def right_node(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class Uint64ClosedLeftIntervalNode(_mod_builtins.object):
    'Non-terminal node for an IntervalTree\n\n    Categorizes intervals by those that fall to the left, those that fall to\n    the right, and those that overlap with the pivot.\n    '
    def __init__(self, *args, **kwargs) -> None:
        'Non-terminal node for an IntervalTree\n\n    Categorizes intervals by those that fall to the left, those that fall to\n    the right, and those that overlap with the pivot.\n    '
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
    
    def __setstate__(self, state: typing.Any) -> None:
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @property
    def center_left_indices(self) -> typing.Any:
        ...
    
    @property
    def center_left_values(self) -> typing.Any:
        ...
    
    @property
    def center_right_indices(self) -> typing.Any:
        ...
    
    @property
    def center_right_values(self) -> typing.Any:
        ...
    
    def counts(self) -> typing.Any:
        '\n        Inspect counts on this node\n        useful for debugging purposes\n        '
        ...
    
    @property
    def indices(self) -> typing.Any:
        ...
    
    @property
    def is_leaf_node(self) -> typing.Any:
        ...
    
    @property
    def leaf_size(self) -> typing.Any:
        ...
    
    @property
    def left(self) -> typing.Any:
        ...
    
    @property
    def left_node(self) -> typing.Any:
        ...
    
    @property
    def max_right(self) -> typing.Any:
        ...
    
    @property
    def min_left(self) -> typing.Any:
        ...
    
    @property
    def n_center(self) -> typing.Any:
        ...
    
    @property
    def n_elements(self) -> typing.Any:
        ...
    
    @property
    def pivot(self) -> typing.Any:
        ...
    
    def query(self, result, point) -> typing.Any:
        'Recursively query this node and its sub-nodes for intervals that\n        overlap with the query point.\n        '
        ...
    
    @property
    def right(self) -> typing.Any:
        ...
    
    @property
    def right_node(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class Uint64ClosedNeitherIntervalNode(_mod_builtins.object):
    'Non-terminal node for an IntervalTree\n\n    Categorizes intervals by those that fall to the left, those that fall to\n    the right, and those that overlap with the pivot.\n    '
    def __init__(self, *args, **kwargs) -> None:
        'Non-terminal node for an IntervalTree\n\n    Categorizes intervals by those that fall to the left, those that fall to\n    the right, and those that overlap with the pivot.\n    '
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
    
    def __setstate__(self, state: typing.Any) -> None:
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @property
    def center_left_indices(self) -> typing.Any:
        ...
    
    @property
    def center_left_values(self) -> typing.Any:
        ...
    
    @property
    def center_right_indices(self) -> typing.Any:
        ...
    
    @property
    def center_right_values(self) -> typing.Any:
        ...
    
    def counts(self) -> typing.Any:
        '\n        Inspect counts on this node\n        useful for debugging purposes\n        '
        ...
    
    @property
    def indices(self) -> typing.Any:
        ...
    
    @property
    def is_leaf_node(self) -> typing.Any:
        ...
    
    @property
    def leaf_size(self) -> typing.Any:
        ...
    
    @property
    def left(self) -> typing.Any:
        ...
    
    @property
    def left_node(self) -> typing.Any:
        ...
    
    @property
    def max_right(self) -> typing.Any:
        ...
    
    @property
    def min_left(self) -> typing.Any:
        ...
    
    @property
    def n_center(self) -> typing.Any:
        ...
    
    @property
    def n_elements(self) -> typing.Any:
        ...
    
    @property
    def pivot(self) -> typing.Any:
        ...
    
    def query(self, result, point) -> typing.Any:
        'Recursively query this node and its sub-nodes for intervals that\n        overlap with the query point.\n        '
        ...
    
    @property
    def right(self) -> typing.Any:
        ...
    
    @property
    def right_node(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class Uint64ClosedRightIntervalNode(_mod_builtins.object):
    'Non-terminal node for an IntervalTree\n\n    Categorizes intervals by those that fall to the left, those that fall to\n    the right, and those that overlap with the pivot.\n    '
    def __init__(self, *args, **kwargs) -> None:
        'Non-terminal node for an IntervalTree\n\n    Categorizes intervals by those that fall to the left, those that fall to\n    the right, and those that overlap with the pivot.\n    '
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
    
    def __setstate__(self, state: typing.Any) -> None:
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @property
    def center_left_indices(self) -> typing.Any:
        ...
    
    @property
    def center_left_values(self) -> typing.Any:
        ...
    
    @property
    def center_right_indices(self) -> typing.Any:
        ...
    
    @property
    def center_right_values(self) -> typing.Any:
        ...
    
    def counts(self) -> typing.Any:
        '\n        Inspect counts on this node\n        useful for debugging purposes\n        '
        ...
    
    @property
    def indices(self) -> typing.Any:
        ...
    
    @property
    def is_leaf_node(self) -> typing.Any:
        ...
    
    @property
    def leaf_size(self) -> typing.Any:
        ...
    
    @property
    def left(self) -> typing.Any:
        ...
    
    @property
    def left_node(self) -> typing.Any:
        ...
    
    @property
    def max_right(self) -> typing.Any:
        ...
    
    @property
    def min_left(self) -> typing.Any:
        ...
    
    @property
    def n_center(self) -> typing.Any:
        ...
    
    @property
    def n_elements(self) -> typing.Any:
        ...
    
    @property
    def pivot(self) -> typing.Any:
        ...
    
    def query(self, result, point) -> typing.Any:
        'Recursively query this node and its sub-nodes for intervals that\n        overlap with the query point.\n        '
        ...
    
    @property
    def right(self) -> typing.Any:
        ...
    
    @property
    def right_node(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

VALID_CLOSED: frozenset
__doc__: typing.Any
__file__: str
__name__: str
__package__: str
def __pyx_unpickle_Enum() -> typing.Any:
    ...

def __pyx_unpickle_Float64ClosedBothIntervalNode() -> typing.Any:
    ...

def __pyx_unpickle_Float64ClosedLeftIntervalNode() -> typing.Any:
    ...

def __pyx_unpickle_Float64ClosedNeitherIntervalNode() -> typing.Any:
    ...

def __pyx_unpickle_Float64ClosedRightIntervalNode() -> typing.Any:
    ...

def __pyx_unpickle_Int64ClosedBothIntervalNode() -> typing.Any:
    ...

def __pyx_unpickle_Int64ClosedLeftIntervalNode() -> typing.Any:
    ...

def __pyx_unpickle_Int64ClosedNeitherIntervalNode() -> typing.Any:
    ...

def __pyx_unpickle_Int64ClosedRightIntervalNode() -> typing.Any:
    ...

def __pyx_unpickle_IntervalMixin() -> typing.Any:
    ...

def __pyx_unpickle_IntervalTree() -> typing.Any:
    ...

def __pyx_unpickle_Uint64ClosedBothIntervalNode() -> typing.Any:
    ...

def __pyx_unpickle_Uint64ClosedLeftIntervalNode() -> typing.Any:
    ...

def __pyx_unpickle_Uint64ClosedNeitherIntervalNode() -> typing.Any:
    ...

def __pyx_unpickle_Uint64ClosedRightIntervalNode() -> typing.Any:
    ...

__test__: dict
def intervals_to_interval_bounds() -> typing.Any:
    '\n    Parameters\n    ----------\n    intervals : ndarray\n        Object array of Intervals / nulls.\n\n    validate_closed: bool, default True\n        Boolean indicating if all intervals must be closed on the same side.\n        Mismatching closed will raise if True, else return None for closed.\n\n    Returns\n    -------\n    tuple of tuples\n        left : (ndarray, object, array)\n        right : (ndarray, object, array)\n        closed: str\n    '
    ...

def is_monotonic(arr, timelike) -> typing.Any:
    '\n    Returns\n    -------\n    tuple\n        is_monotonic_inc : bool\n        is_monotonic_dec : bool\n        is_unique : bool\n    '
    ...

def le(a, b) -> typing.Any:
    'Same as a <= b.'
    ...

def lt(a, b) -> typing.Any:
    'Same as a < b.'
    ...

def __getattr__(name) -> typing.Any:
    ...

