# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: scipy, version: 1.6.2
# Module: scipy.sparse.linalg.dsolve._superlu, version: unspecified
import typing
import builtins as _mod_builtins

SuperLU = _mod_builtins.SuperLU
__doc__: typing.Any
__file__: str
__name__: str
__package__: str
def gssv() -> typing.Any:
    'Direct inversion of sparse matrix.\n\nX = gssv(A,B) solves A*X = B for X.'
    ...

def gstrf() -> typing.Any:
    "gstrf(A, ...)\n\nperforms a factorization of the sparse matrix A=*(N,nnz,nzvals,rowind,colptr) and \nreturns a factored_lu object.\n\narguments\n---------\n\nMatrix to be factorized is represented as N,nnz,nzvals,rowind,colptr\n  as separate arguments.  This is compressed sparse column representation.\n\nN         number of rows and columns \nnnz       number of non-zero elements\nnzvals    non-zero values \nrowind    row-index for this column (same size as nzvals)\ncolptr    index into rowind for first non-zero value in this column\n          size is (N+1).  Last value should be nnz. \n\nadditional keyword arguments:\n-----------------------------\noptions             specifies additional options for SuperLU\n                    (same keys and values as in superlu_options_t C structure,\n                    and additionally 'Relax' and 'PanelSize')\n\nilu                 whether to perform an incomplete LU decomposition\n                    (default: false)\n"
    ...

def __getattr__(name) -> typing.Any:
    ...

