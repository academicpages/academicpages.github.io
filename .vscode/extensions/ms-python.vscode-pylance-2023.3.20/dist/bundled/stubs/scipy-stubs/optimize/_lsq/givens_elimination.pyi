# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: scipy, version: 1.6.2
# Module: scipy.optimize._lsq.givens_elimination, version: unspecified
import typing
import builtins as _mod_builtins

__doc__: typing.Any
__file__: str
__name__: str
__package__: str
def __pyx_unpickle_Enum() -> typing.Any:
    ...

__test__: dict
def givens_elimination() -> typing.Any:
    'Zero out a diagonal block of a matrix by series of Givens rotations.\n\n    The matrix has the structure::\n\n        [ S ]\n        [ D ]\n\n    Where S is an upper triangular matrix with shape (n, n) and D is a\n    diagonal matrix with shape (n, n) with elements from `diag`. This function\n    applies Givens rotations to it such that the resulting matrix has zeros\n    in place of D.\n\n    Array `S` will be modified in-place.\n\n    Array `v` of shape (n,) is the part of the full vector with shape (2*n,)::\n\n        [ v ]\n        [ 0 ]\n\n    to which Givens rotations are applied. This array is modified in place,\n    such that on exit it contains the first n components of the above\n    mentioned vector after rotations were applied.\n    '
    ...

def __getattr__(name) -> typing.Any:
    ...

