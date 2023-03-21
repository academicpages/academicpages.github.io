# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: scipy, version: 1.6.2
# Module: scipy.optimize.__nnls, version: $Revision: $
import typing
import builtins as _mod_builtins

__doc__: str
__file__: str
__name__: str
__package__: str
__version__: bytes
def nnls(a, m, n, b, w, zz, index_bn, maxiter, mda=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "x,rnorm,mode = nnls(a,m,n,b,w,zz,index_bn,maxiter,[mda,overwrite_a,overwrite_b])\n\nWrapper for ``nnls``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (mda,*)\nm : input int\nn : input int\nb : input rank-1 array('d') with bounds (*)\nw : input rank-1 array('d') with bounds (*)\nzz : input rank-1 array('d') with bounds (*)\nindex_bn : input rank-1 array('i') with bounds (*)\nmaxiter : input int\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nmda : input int, optional\n    Default: shape(a,0)\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-1 array('d') with bounds (n)\nrnorm : float\nmode : int\n"
    ...

def __getattr__(name) -> typing.Any:
    ...

