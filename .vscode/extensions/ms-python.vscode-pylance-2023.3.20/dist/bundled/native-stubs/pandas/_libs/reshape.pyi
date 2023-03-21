# Python: 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)]
# Library: pandas, version: 1.2.4
# Module: pandas._libs.reshape, version: unspecified
import typing
import builtins as _mod_builtins

__doc__: typing.Any
__file__: str
__name__: str
__package__: str
def __pyx_unpickle_Enum() -> typing.Any:
    ...

__test__: dict
def explode() -> typing.Any:
    '\n    transform array list-likes to long form\n    preserve non-list entries\n\n    Parameters\n    ----------\n    values : object ndarray\n\n    Returns\n    -------\n    tuple(values, counts)\n    '
    ...

def unstack(values, mask, stride, length, width, new_values, new_mask) -> typing.Any:
    '\n    Transform long values to wide new_values.\n\n    Parameters\n    ----------\n    values : typed ndarray\n    mask : boolean ndarray\n    stride : int\n    length : int\n    width : int\n    new_values : typed ndarray\n        result array\n    new_mask : boolean ndarray\n        result mask\n    '
    ...

def __getattr__(name) -> typing.Any:
    ...

