# Python: 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)]
# Library: pandas, version: 1.2.4
# Module: pandas._libs.ops, version: unspecified
import typing
import builtins as _mod_builtins

__doc__: typing.Any
__file__: str
__name__: str
__package__: str
def __pyx_unpickle_Enum() -> typing.Any:
    ...

__test__: dict
def maybe_convert_bool() -> typing.Any:
    ...

def scalar_binop() -> typing.Any:
    '\n    Apply the given binary operator `op` between each element of the array\n    `values` and the scalar `val`.\n\n    Parameters\n    ----------\n    values : ndarray[object]\n    val : object\n    op : binary operator\n\n    Returns\n    -------\n    result : ndarray[object]\n    '
    ...

def scalar_compare() -> typing.Any:
    '\n    Compare each element of `values` array with the scalar `val`, with\n    the comparison operation described by `op`.\n\n    Parameters\n    ----------\n    values : ndarray[object]\n    val : object\n    op : {operator.eq, operator.ne,\n          operator.le, operator.lt,\n          operator.ge, operator.gt}\n\n    Returns\n    -------\n    result : ndarray[bool]\n    '
    ...

def vec_binop() -> typing.Any:
    '\n    Apply the given binary operator `op` pointwise to the elements of\n    arrays `left` and `right`.\n\n    Parameters\n    ----------\n    left : ndarray[object]\n    right : ndarray[object]\n    op : binary operator\n\n    Returns\n    -------\n    result : ndarray[object]\n    '
    ...

def vec_compare() -> typing.Any:
    '\n    Compare the elements of `left` with the elements of `right` pointwise,\n    with the comparison operation described by `op`.\n\n    Parameters\n    ----------\n    left : ndarray[object]\n    right : ndarray[object]\n    op : {operator.eq, operator.ne,\n          operator.le, operator.lt,\n          operator.ge, operator.gt}\n\n    Returns\n    -------\n    result : ndarray[bool]\n    '
    ...

def __getattr__(name) -> typing.Any:
    ...

