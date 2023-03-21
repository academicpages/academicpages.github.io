# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: scipy, version: 1.6.2
# Module: scipy.integrate._test_odeint_banded, version: $Revision: $
import typing
import builtins as _mod_builtins

__doc__: str
__file__: str
__name__: str
__package__: str
__version__: bytes
def banded5x5(t, y, f, n=...) -> typing.Any:
    "banded5x5(t,y,f,[n])\n\nWrapper for ``banded5x5``.\n\nParameters\n----------\nt : input float\ny : input rank-1 array('d') with bounds (n)\nf : input rank-1 array('d') with bounds (n)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: len(y)\n"
    ...

def banded5x5_bjac(t, y, ml, mu, bjac, n=..., nrowpd=...) -> typing.Any:
    "banded5x5_bjac(t,y,ml,mu,bjac,[n,nrowpd])\n\nWrapper for ``banded5x5_bjac``.\n\nParameters\n----------\nt : input float\ny : input rank-1 array('d') with bounds (5)\nml : input int\nmu : input int\nbjac : input rank-2 array('d') with bounds (nrowpd,n)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: shape(bjac,1)\nnrowpd : input int, optional\n    Default: shape(bjac,0)\n"
    ...

def banded5x5_jac(t, y, ml, mu, jac, n=..., nrowpd=...) -> typing.Any:
    "banded5x5_jac(t,y,ml,mu,jac,[n,nrowpd])\n\nWrapper for ``banded5x5_jac``.\n\nParameters\n----------\nt : input float\ny : input rank-1 array('d') with bounds (n)\nml : input int\nmu : input int\njac : input rank-2 array('d') with bounds (nrowpd,n)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: len(y)\nnrowpd : input int, optional\n    Default: shape(jac,0)\n"
    ...

def banded5x5_solve(y, nsteps, dt, jt) -> typing.Any:
    "nst,nfe,nje = banded5x5_solve(y,nsteps,dt,jt)\n\nWrapper for ``banded5x5_solve``.\n\nParameters\n----------\ny : in/output rank-1 array('d') with bounds (5)\nnsteps : input int\ndt : input float\njt : input int\n\nReturns\n-------\nnst : int\nnfe : int\nnje : int\n"
    ...

def getbands() -> typing.Any:
    "jac = getbands()\n\nWrapper for ``getbands``.\n\nReturns\n-------\njac : rank-2 array('d') with bounds (4,5)\n"
    ...

def jac() -> typing.Any:
    "'d'-array(4,5)\n"
    ...

def __getattr__(name) -> typing.Any:
    ...

