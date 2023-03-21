# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: scipy, version: 1.6.2
# Module: scipy.optimize.minpack2, version: $Revision: $
import typing
import builtins as _mod_builtins

__doc__: str
__file__: str
__name__: str
__package__: str
__version__: bytes
def dcsrch(stp, f, g, ftol, gtol, xtol, task, stpmin, stpmax, isave, dsave) -> typing.Any:
    "stp,f,g,task = dcsrch(stp,f,g,ftol,gtol,xtol,task,stpmin,stpmax,isave,dsave)\n\nWrapper for ``dcsrch``.\n\nParameters\n----------\nstp : input float\nf : input float\ng : input float\nftol : input float\ngtol : input float\nxtol : input float\ntask : input string(len=60)\nstpmin : input float\nstpmax : input float\nisave : in/output rank-1 array('i') with bounds (2)\ndsave : in/output rank-1 array('d') with bounds (13)\n\nReturns\n-------\nstp : float\nf : float\ng : float\ntask : string(len=60)\n"
    ...

def dcstep(stx, fx, dx, sty, fy, dy, stp, fp, dp, brackt, stpmin, stpmax) -> typing.Any:
    'stx,fx,dx,sty,fy,dy,stp,brackt = dcstep(stx,fx,dx,sty,fy,dy,stp,fp,dp,brackt,stpmin,stpmax)\n\nWrapper for ``dcstep``.\n\nParameters\n----------\nstx : input float\nfx : input float\ndx : input float\nsty : input float\nfy : input float\ndy : input float\nstp : input float\nfp : input float\ndp : input float\nbrackt : input int\nstpmin : input float\nstpmax : input float\n\nReturns\n-------\nstx : float\nfx : float\ndx : float\nsty : float\nfy : float\ndy : float\nstp : float\nbrackt : int\n'
    ...

def __getattr__(name) -> typing.Any:
    ...

