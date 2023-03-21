# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: scipy, version: 1.6.2
# Module: scipy.io._test_fortran, version: $Revision: $
import typing
import builtins as _mod_builtins

__doc__: str
__file__: str
__name__: str
__package__: str
__version__: bytes
def read_unformatted_double(m, n, k, filename) -> typing.Any:
    "a = read_unformatted_double(m,n,k,filename)\n\nWrapper for ``read_unformatted_double``.\n\nParameters\n----------\nm : input int\nn : input int\nk : input int\nfilename : input string(len=4096)\n\nReturns\n-------\na : rank-3 array('d') with bounds (m,n,k)\n"
    ...

def read_unformatted_int(m, n, k, filename) -> typing.Any:
    "a = read_unformatted_int(m,n,k,filename)\n\nWrapper for ``read_unformatted_int``.\n\nParameters\n----------\nm : input int\nn : input int\nk : input int\nfilename : input string(len=4096)\n\nReturns\n-------\na : rank-3 array('i') with bounds (m,n,k)\n"
    ...

def read_unformatted_mixed(m, n, k, filename) -> typing.Any:
    "a,b = read_unformatted_mixed(m,n,k,filename)\n\nWrapper for ``read_unformatted_mixed``.\n\nParameters\n----------\nm : input int\nn : input int\nk : input int\nfilename : input string(len=4096)\n\nReturns\n-------\na : rank-2 array('d') with bounds (m,n)\nb : rank-1 array('i') with bounds (k)\n"
    ...

def __getattr__(name) -> typing.Any:
    ...

