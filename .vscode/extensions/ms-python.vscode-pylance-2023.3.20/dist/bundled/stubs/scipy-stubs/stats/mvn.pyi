# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: scipy, version: 1.6.2
# Module: scipy.stats.mvn, version: $Revision: $
import typing
import builtins as _mod_builtins

__doc__: str
__file__: str
__name__: str
__package__: str
__version__: bytes
def dkblck() -> typing.Any:
    "'i'-scalar\n"
    ...

def mvndst(lower, upper, infin, correl, maxpts=..., abseps=..., releps=...) -> typing.Any:
    "error,value,inform = mvndst(lower,upper,infin,correl,[maxpts,abseps,releps])\n\nWrapper for ``mvndst``.\n\nParameters\n----------\nlower : input rank-1 array('d') with bounds (n)\nupper : input rank-1 array('d') with bounds (n)\ninfin : input rank-1 array('i') with bounds (n)\ncorrel : input rank-1 array('d') with bounds (n*(n-1)/2)\n\nOther Parameters\n----------------\nmaxpts : input int, optional\n    Default: 2000\nabseps : input float, optional\n    Default: 1e-06\nreleps : input float, optional\n    Default: 1e-06\n\nReturns\n-------\nerror : float\nvalue : float\ninform : int\n"
    ...

def mvnun(lower, upper, means, covar, maxpts=..., abseps=..., releps=...) -> typing.Any:
    "value,inform = mvnun(lower,upper,means,covar,[maxpts,abseps,releps])\n\nWrapper for ``mvnun``.\n\nParameters\n----------\nlower : input rank-1 array('d') with bounds (d)\nupper : input rank-1 array('d') with bounds (d)\nmeans : input rank-2 array('d') with bounds (d,n)\ncovar : input rank-2 array('d') with bounds (d,d)\n\nOther Parameters\n----------------\nmaxpts : input int, optional\n    Default: d*1000\nabseps : input float, optional\n    Default: 1e-06\nreleps : input float, optional\n    Default: 1e-06\n\nReturns\n-------\nvalue : float\ninform : int\n"
    ...

def mvnun_weighted(lower, upper, means, weights, covar, maxpts=..., abseps=..., releps=...) -> typing.Any:
    "value,inform = mvnun_weighted(lower,upper,means,weights,covar,[maxpts,abseps,releps])\n\nWrapper for ``mvnun_weighted``.\n\nParameters\n----------\nlower : input rank-1 array('d') with bounds (d)\nupper : input rank-1 array('d') with bounds (d)\nmeans : input rank-2 array('d') with bounds (d,n)\nweights : input rank-1 array('d') with bounds (n)\ncovar : input rank-2 array('d') with bounds (d,d)\n\nOther Parameters\n----------------\nmaxpts : input int, optional\n    Default: d*1000\nabseps : input float, optional\n    Default: 1e-06\nreleps : input float, optional\n    Default: 1e-06\n\nReturns\n-------\nvalue : float\ninform : int\n"
    ...

def __getattr__(name) -> typing.Any:
    ...

