# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: scipy, version: 1.6.2
# Module: scipy.integrate._dop, version: $Revision: $
import typing
import builtins as _mod_builtins

__doc__: str
__file__: str
__name__: str
__package__: str
__version__: bytes
def dop853(fcn, x, y, xend, rtol, atol, solout, iout, work, iwork, fcn_extra_args=..., overwrite_y=..., solout_extra_args=...) -> typing.Any:
    "x,y,iwork,idid = dop853(fcn,x,y,xend,rtol,atol,solout,iout,work,iwork,[fcn_extra_args,overwrite_y,solout_extra_args])\n\nWrapper for ``dop853``.\n\nParameters\n----------\nfcn : call-back function\nx : input float\ny : input rank-1 array('d') with bounds (n)\nxend : input float\nrtol : input rank-1 array('d') with bounds (*)\natol : input rank-1 array('d') with bounds (*)\nsolout : call-back function\niout : input int\nwork : input rank-1 array('d') with bounds (*)\niwork : input rank-1 array('i') with bounds (*)\n\nOther Parameters\n----------------\nfcn_extra_args : input tuple, optional\n    Default: ()\noverwrite_y : input int, optional\n    Default: 0\nsolout_extra_args : input tuple, optional\n    Default: ()\n\nReturns\n-------\nx : float\ny : rank-1 array('d') with bounds (n)\niwork : rank-1 array('i') with bounds (*)\nidid : int\n\nNotes\n-----\nCall-back functions::\n\n  def fcn(x,y): return f\n  Required arguments:\n    x : input float\n    y : input rank-1 array('d') with bounds (n)\n  Return objects:\n    f : rank-1 array('d') with bounds (n)\n  def solout(nr,xold,x,y,con,icomp,[nd]): return irtn\n  Required arguments:\n    nr : input int\n    xold : input float\n    x : input float\n    y : input rank-1 array('d') with bounds (n)\n    con : input rank-1 array('d') with bounds (5 * nd)\n    icomp : input rank-1 array('i') with bounds (nd)\n  Optional arguments:\n    nd : input int, optional\n    Default: (len(con))/(5)\n  Return objects:\n    irtn : int\n"
    ...

def dopri5(fcn, x, y, xend, rtol, atol, solout, iout, work, iwork, fcn_extra_args=..., overwrite_y=..., solout_extra_args=...) -> typing.Any:
    "x,y,iwork,idid = dopri5(fcn,x,y,xend,rtol,atol,solout,iout,work,iwork,[fcn_extra_args,overwrite_y,solout_extra_args])\n\nWrapper for ``dopri5``.\n\nParameters\n----------\nfcn : call-back function\nx : input float\ny : input rank-1 array('d') with bounds (n)\nxend : input float\nrtol : input rank-1 array('d') with bounds (*)\natol : input rank-1 array('d') with bounds (*)\nsolout : call-back function\niout : input int\nwork : input rank-1 array('d') with bounds (*)\niwork : input rank-1 array('i') with bounds (*)\n\nOther Parameters\n----------------\nfcn_extra_args : input tuple, optional\n    Default: ()\noverwrite_y : input int, optional\n    Default: 0\nsolout_extra_args : input tuple, optional\n    Default: ()\n\nReturns\n-------\nx : float\ny : rank-1 array('d') with bounds (n)\niwork : rank-1 array('i') with bounds (*)\nidid : int\n\nNotes\n-----\nCall-back functions::\n\n  def fcn(x,y): return f\n  Required arguments:\n    x : input float\n    y : input rank-1 array('d') with bounds (n)\n  Return objects:\n    f : rank-1 array('d') with bounds (n)\n  def solout(nr,xold,x,y,con,icomp,[nd]): return irtn\n  Required arguments:\n    nr : input int\n    xold : input float\n    x : input float\n    y : input rank-1 array('d') with bounds (n)\n    con : input rank-1 array('d') with bounds (5 * nd)\n    icomp : input rank-1 array('i') with bounds (nd)\n  Optional arguments:\n    nd : input int, optional\n    Default: (len(con))/(5)\n  Return objects:\n    irtn : int\n"
    ...

def types() -> typing.Any:
    "'i'-scalar\n"
    ...

def __getattr__(name) -> typing.Any:
    ...

