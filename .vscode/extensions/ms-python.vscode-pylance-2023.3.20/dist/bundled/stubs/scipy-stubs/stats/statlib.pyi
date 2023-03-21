# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: scipy, version: 1.6.2
# Module: scipy.stats.statlib, version: $Revision: $
import typing
import builtins as _mod_builtins

__doc__: str
__file__: str
__name__: str
__package__: str
__version__: bytes
def gscale(test, other) -> typing.Any:
    "astart,a1,ifault = gscale(test,other)\n\nWrapper for ``gscale``.\n\nParameters\n----------\ntest : input int\nother : input int\n\nReturns\n-------\nastart : float\na1 : rank-1 array('f') with bounds (l1)\nifault : int\n"
    ...

def prho(n, is_) -> typing.Any:
    'ifault = prho(n,is)\n\nWrapper for ``prho``.\n\nParameters\n----------\nn : input int\nis : input int\n\nReturns\n-------\nprho : float\nifault : int\n'
    ...

def swilk(x, a, init=..., n1=...) -> typing.Any:
    "a,w,pw,ifault = swilk(x,a,[init,n1])\n\nWrapper for ``swilk``.\n\nParameters\n----------\nx : input rank-1 array('f') with bounds (n)\na : input rank-1 array('f') with bounds (n2)\n\nOther Parameters\n----------------\ninit : input int, optional\n    Default: 0\nn1 : input int, optional\n    Default: n\n\nReturns\n-------\na : rank-1 array('f') with bounds (n2)\nw : float\npw : float\nifault : int\n"
    ...

def __getattr__(name) -> typing.Any:
    ...

