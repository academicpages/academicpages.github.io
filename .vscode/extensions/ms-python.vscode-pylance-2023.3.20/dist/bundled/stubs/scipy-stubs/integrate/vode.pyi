# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: scipy, version: 1.6.2
# Module: scipy.integrate.vode, version: $Revision: $
import typing
import builtins as _mod_builtins

__doc__: str
__file__: str
__name__: str
__package__: str
__version__: bytes
def dvode(f, jac, y, t, tout, rtol, atol, itask, istate, rwork, iwork, mf, f_extra_args=..., jac_extra_args=..., overwrite_y=...) -> typing.Any:
    "y,t,istate = dvode(f,jac,y,t,tout,rtol,atol,itask,istate,rwork,iwork,mf,[f_extra_args,jac_extra_args,overwrite_y])\n\nWrapper for ``dvode``.\n\nParameters\n----------\nf : call-back function\njac : call-back function\ny : input rank-1 array('d') with bounds (neq)\nt : input float\ntout : input float\nrtol : input rank-1 array('d') with bounds (*)\natol : input rank-1 array('d') with bounds (*)\nitask : input int\nistate : input int\nrwork : input rank-1 array('d') with bounds (lrw)\niwork : input rank-1 array('i') with bounds (liw)\nmf : input int\n\nOther Parameters\n----------------\nf_extra_args : input tuple, optional\n    Default: ()\njac_extra_args : input tuple, optional\n    Default: ()\noverwrite_y : input int, optional\n    Default: 0\n\nReturns\n-------\ny : rank-1 array('d') with bounds (neq)\nt : float\nistate : int\n\nNotes\n-----\nCall-back functions::\n\n  def f(t,y): return ydot\n  Required arguments:\n    t : input float\n    y : input rank-1 array('d') with bounds (n)\n  Return objects:\n    ydot : rank-1 array('d') with bounds (n)\n  def jac(t,y): return jac\n  Required arguments:\n    t : input float\n    y : input rank-1 array('d') with bounds (n)\n  Return objects:\n    jac : rank-2 array('d') with bounds (nrowpd,n)\n"
    ...

def types() -> typing.Any:
    "'i'-scalar\n"
    ...

def zvode(f, jac, y, t, tout, rtol, atol, itask, istate, zwork, rwork, iwork, mf, f_extra_args=..., jac_extra_args=..., overwrite_y=...) -> typing.Any:
    "y,t,istate = zvode(f,jac,y,t,tout,rtol,atol,itask,istate,zwork,rwork,iwork,mf,[f_extra_args,jac_extra_args,overwrite_y])\n\nWrapper for ``zvode``.\n\nParameters\n----------\nf : call-back function\njac : call-back function\ny : input rank-1 array('D') with bounds (neq)\nt : input float\ntout : input float\nrtol : input rank-1 array('d') with bounds (*)\natol : input rank-1 array('d') with bounds (*)\nitask : input int\nistate : input int\nzwork : input rank-1 array('D') with bounds (lzw)\nrwork : input rank-1 array('d') with bounds (lrw)\niwork : input rank-1 array('i') with bounds (liw)\nmf : input int\n\nOther Parameters\n----------------\nf_extra_args : input tuple, optional\n    Default: ()\njac_extra_args : input tuple, optional\n    Default: ()\noverwrite_y : input int, optional\n    Default: 0\n\nReturns\n-------\ny : rank-1 array('D') with bounds (neq)\nt : float\nistate : int\n\nNotes\n-----\nCall-back functions::\n\n  def f(t,y): return ydot\n  Required arguments:\n    t : input float\n    y : input rank-1 array('D') with bounds (n)\n  Return objects:\n    ydot : rank-1 array('D') with bounds (n)\n  def jac(t,y): return jac\n  Required arguments:\n    t : input float\n    y : input rank-1 array('D') with bounds (n)\n  Return objects:\n    jac : rank-2 array('D') with bounds (nrowpd,n)\n"
    ...

def __getattr__(name) -> typing.Any:
    ...

