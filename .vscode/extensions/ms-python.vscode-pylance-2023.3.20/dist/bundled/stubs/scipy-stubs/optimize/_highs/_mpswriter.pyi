# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: scipy, version: 1.6.2
# Module: scipy.optimize._highs._mpswriter, version: unspecified
import typing
import builtins as _mod_builtins
import scipy.sparse.csc as _mod_scipy_sparse_csc

__doc__: typing.Any
__file__: str
__name__: str
__package__: str
def __pyx_unpickle_Enum() -> typing.Any:
    ...

__test__: dict
csc_matrix = _mod_scipy_sparse_csc.csc_matrix
def mpswriter() -> typing.Any:
    'MPS writer: create MPS file from matrices.\n\n    Parameters\n    ----------\n    filename : bytes (string)\n        Name of MPS file to write out to.  Will be overwritten.\n    c : 1-D array (numcol,)\n        Objective coefficient values (assumes minimization).\n    A : 2-D array (numrow, numcol), scipy.sparse.csc_matrix\n        Sparse inequality constraint matrix.\n    lhs : 1-D array (numrow,)\n        Left hand side inequality values.\n    rhs : 1-D array (numrow,)\n        Right hand side inequality values.\n    lb : 1-D array (numcol,)\n        Lower bounds of solution variables.\n    ub : 1-D array (numcol,)\n        Upper bounds of solution variables.\n    integer_valued : 1-D array (numint,)\n        Indices of integer valued solution variables.\n    use_free_format : bool, optional\n        Use MPS free format.  Default is False.\n\n    Notes\n    -----\n    Wrapper over HiGHS `writeMPS` function.\n    '
    ...

def __getattr__(name) -> typing.Any:
    ...

