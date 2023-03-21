# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: scipy, version: 1.6.2
# Module: scipy.optimize._cobyla, version: $Revision: $
import typing
import builtins as _mod_builtins

__doc__: str
__file__: str
__name__: str
__package__: str
__version__: bytes
def minimize(calcfc, m, x, rhobeg, rhoend, dinfo, iprint=..., maxfun=..., calcfc_extra_args=...) -> typing.Any:
    "x,dinfo = minimize(calcfc,m,x,rhobeg,rhoend,dinfo,[iprint,maxfun,calcfc_extra_args])\n\nWrapper for ``minimize``.\n\nParameters\n----------\ncalcfc : call-back function\nm : input int\nx : input rank-1 array('d') with bounds (n)\nrhobeg : input float\nrhoend : input float\ndinfo : input rank-1 array('d') with bounds (4)\n\nOther Parameters\n----------------\ncalcfc_extra_args : input tuple, optional\n    Default: ()\niprint : input int, optional\n    Default: 1\nmaxfun : input int, optional\n    Default: 100\n\nReturns\n-------\nx : rank-1 array('d') with bounds (n)\ndinfo : rank-1 array('d') with bounds (4)\n\nNotes\n-----\nCall-back functions::\n\n  def calcfc(x,con): return f\n  Required arguments:\n    x : input rank-1 array('d') with bounds (n)\n    con : input rank-1 array('d') with bounds (m)\n  Return objects:\n    f : float\n"
    ...

def __getattr__(name) -> typing.Any:
    ...

