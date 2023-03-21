# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: scipy, version: 1.6.2
# Module: scipy.linalg._flinalg, version: $Revision: $
import typing
import builtins as _mod_builtins

__doc__: str
__file__: str
__name__: str
__package__: str
__version__: bytes
def cdet_c(a, overwrite_a=...) -> typing.Any:
    "det,info = cdet_c(a,[overwrite_a])\n\nWrapper for ``cdet_c``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\ndet : complex\ninfo : int\n"
    ...

def cdet_r(a, overwrite_a=...) -> typing.Any:
    "det,info = cdet_r(a,[overwrite_a])\n\nWrapper for ``cdet_r``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\ndet : complex\ninfo : int\n"
    ...

def clu_c(a, permute_l=..., overwrite_a=...) -> typing.Any:
    "p,l,u,info = clu_c(a,[permute_l,overwrite_a])\n\nWrapper for ``clu_c``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\npermute_l : input int, optional\n    Default: 0\n\nReturns\n-------\np : rank-2 array('f') with bounds (m1,m1)\nl : rank-2 array('F') with bounds (m,k)\nu : rank-2 array('F') with bounds (k,n)\ninfo : int\n"
    ...

def ddet_c(a, overwrite_a=...) -> typing.Any:
    "det,info = ddet_c(a,[overwrite_a])\n\nWrapper for ``ddet_c``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\ndet : float\ninfo : int\n"
    ...

def ddet_r(a, overwrite_a=...) -> typing.Any:
    "det,info = ddet_r(a,[overwrite_a])\n\nWrapper for ``ddet_r``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\ndet : float\ninfo : int\n"
    ...

def dlu_c(a, permute_l=..., overwrite_a=...) -> typing.Any:
    "p,l,u,info = dlu_c(a,[permute_l,overwrite_a])\n\nWrapper for ``dlu_c``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\npermute_l : input int, optional\n    Default: 0\n\nReturns\n-------\np : rank-2 array('d') with bounds (m1,m1)\nl : rank-2 array('d') with bounds (m,k)\nu : rank-2 array('d') with bounds (k,n)\ninfo : int\n"
    ...

def sdet_c(a, overwrite_a=...) -> typing.Any:
    "det,info = sdet_c(a,[overwrite_a])\n\nWrapper for ``sdet_c``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\ndet : float\ninfo : int\n"
    ...

def sdet_r(a, overwrite_a=...) -> typing.Any:
    "det,info = sdet_r(a,[overwrite_a])\n\nWrapper for ``sdet_r``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\ndet : float\ninfo : int\n"
    ...

def slu_c(a, permute_l=..., overwrite_a=...) -> typing.Any:
    "p,l,u,info = slu_c(a,[permute_l,overwrite_a])\n\nWrapper for ``slu_c``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\npermute_l : input int, optional\n    Default: 0\n\nReturns\n-------\np : rank-2 array('f') with bounds (m1,m1)\nl : rank-2 array('f') with bounds (m,k)\nu : rank-2 array('f') with bounds (k,n)\ninfo : int\n"
    ...

def zdet_c(a, overwrite_a=...) -> typing.Any:
    "det,info = zdet_c(a,[overwrite_a])\n\nWrapper for ``zdet_c``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\ndet : complex\ninfo : int\n"
    ...

def zdet_r(a, overwrite_a=...) -> typing.Any:
    "det,info = zdet_r(a,[overwrite_a])\n\nWrapper for ``zdet_r``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\ndet : complex\ninfo : int\n"
    ...

def zlu_c(a, permute_l=..., overwrite_a=...) -> typing.Any:
    "p,l,u,info = zlu_c(a,[permute_l,overwrite_a])\n\nWrapper for ``zlu_c``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\npermute_l : input int, optional\n    Default: 0\n\nReturns\n-------\np : rank-2 array('d') with bounds (m1,m1)\nl : rank-2 array('D') with bounds (m,k)\nu : rank-2 array('D') with bounds (k,n)\ninfo : int\n"
    ...

def __getattr__(name) -> typing.Any:
    ...

