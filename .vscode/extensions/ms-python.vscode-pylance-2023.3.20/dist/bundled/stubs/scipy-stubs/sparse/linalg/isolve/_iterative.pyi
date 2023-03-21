# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: scipy, version: 1.6.2
# Module: scipy.sparse.linalg.isolve._iterative, version: $Revision: $
import typing
import builtins as _mod_builtins

__doc__: str
__file__: str
__name__: str
__package__: str
__version__: bytes
def cbicgrevcom(b, x, work, iter, resid, info, ndx1, ndx2, ijob) -> typing.Any:
    "x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = cbicgrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)\n\nWrapper for ``cbicgrevcom``.\n\nParameters\n----------\nb : input rank-1 array('F') with bounds (n)\nx : input rank-1 array('F') with bounds (n)\nwork : in/output rank-1 array('F') with bounds (6 * ldw)\niter : input int\nresid : input float\ninfo : input int\nndx1 : input int\nndx2 : input int\nijob : input int\n\nReturns\n-------\nx : rank-1 array('F') with bounds (n)\niter : int\nresid : float\ninfo : int\nndx1 : int\nndx2 : int\nsclr1 : complex\nsclr2 : complex\nijob : int\n"
    ...

def cbicgstabrevcom(b, x, work, iter, resid, info, ndx1, ndx2, ijob) -> typing.Any:
    "x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = cbicgstabrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)\n\nWrapper for ``cbicgstabrevcom``.\n\nParameters\n----------\nb : input rank-1 array('F') with bounds (n)\nx : input rank-1 array('F') with bounds (n)\nwork : in/output rank-1 array('F') with bounds (7 * ldw)\niter : input int\nresid : input float\ninfo : input int\nndx1 : input int\nndx2 : input int\nijob : input int\n\nReturns\n-------\nx : rank-1 array('F') with bounds (n)\niter : int\nresid : float\ninfo : int\nndx1 : int\nndx2 : int\nsclr1 : complex\nsclr2 : complex\nijob : int\n"
    ...

def ccgrevcom(b, x, work, iter, resid, info, ndx1, ndx2, ijob) -> typing.Any:
    "x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = ccgrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)\n\nWrapper for ``ccgrevcom``.\n\nParameters\n----------\nb : input rank-1 array('F') with bounds (n)\nx : input rank-1 array('F') with bounds (n)\nwork : in/output rank-1 array('F') with bounds (4 * ldw)\niter : input int\nresid : input float\ninfo : input int\nndx1 : input int\nndx2 : input int\nijob : input int\n\nReturns\n-------\nx : rank-1 array('F') with bounds (n)\niter : int\nresid : float\ninfo : int\nndx1 : int\nndx2 : int\nsclr1 : complex\nsclr2 : complex\nijob : int\n"
    ...

def ccgsrevcom(b, x, work, iter, resid, info, ndx1, ndx2, ijob) -> typing.Any:
    "x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = ccgsrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)\n\nWrapper for ``ccgsrevcom``.\n\nParameters\n----------\nb : input rank-1 array('F') with bounds (n)\nx : input rank-1 array('F') with bounds (n)\nwork : in/output rank-1 array('F') with bounds (7 * ldw)\niter : input int\nresid : input float\ninfo : input int\nndx1 : input int\nndx2 : input int\nijob : input int\n\nReturns\n-------\nx : rank-1 array('F') with bounds (n)\niter : int\nresid : float\ninfo : int\nndx1 : int\nndx2 : int\nsclr1 : complex\nsclr2 : complex\nijob : int\n"
    ...

def cgmresrevcom(b, x, restrt, work, work2, iter, resid, info, ndx1, ndx2, ijob, tol) -> typing.Any:
    "x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = cgmresrevcom(b,x,restrt,work,work2,iter,resid,info,ndx1,ndx2,ijob,tol)\n\nWrapper for ``cgmresrevcom``.\n\nParameters\n----------\nb : input rank-1 array('F') with bounds (n)\nx : input rank-1 array('F') with bounds (n)\nrestrt : input int\nwork : in/output rank-1 array('F') with bounds (ldw*(6+restrt))\nwork2 : in/output rank-1 array('F') with bounds (ldw2*(2*restrt+2))\niter : input int\nresid : input float\ninfo : input int\nndx1 : input int\nndx2 : input int\nijob : input int\ntol : input float\n\nReturns\n-------\nx : rank-1 array('F') with bounds (n)\niter : int\nresid : float\ninfo : int\nndx1 : int\nndx2 : int\nsclr1 : complex\nsclr2 : complex\nijob : int\n"
    ...

def cqmrrevcom(b, x, work, iter, resid, info, ndx1, ndx2, ijob) -> typing.Any:
    "x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = cqmrrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)\n\nWrapper for ``cqmrrevcom``.\n\nParameters\n----------\nb : input rank-1 array('F') with bounds (n)\nx : input rank-1 array('F') with bounds (n)\nwork : in/output rank-1 array('F') with bounds (11 * ldw)\niter : input int\nresid : input float\ninfo : input int\nndx1 : input int\nndx2 : input int\nijob : input int\n\nReturns\n-------\nx : rank-1 array('F') with bounds (n)\niter : int\nresid : float\ninfo : int\nndx1 : int\nndx2 : int\nsclr1 : complex\nsclr2 : complex\nijob : int\n"
    ...

def dbicgrevcom(b, x, work, iter, resid, info, ndx1, ndx2, ijob) -> typing.Any:
    "x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = dbicgrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)\n\nWrapper for ``dbicgrevcom``.\n\nParameters\n----------\nb : input rank-1 array('d') with bounds (n)\nx : input rank-1 array('d') with bounds (n)\nwork : in/output rank-1 array('d') with bounds (6 * ldw)\niter : input int\nresid : input float\ninfo : input int\nndx1 : input int\nndx2 : input int\nijob : input int\n\nReturns\n-------\nx : rank-1 array('d') with bounds (n)\niter : int\nresid : float\ninfo : int\nndx1 : int\nndx2 : int\nsclr1 : float\nsclr2 : float\nijob : int\n"
    ...

def dbicgstabrevcom(b, x, work, iter, resid, info, ndx1, ndx2, ijob) -> typing.Any:
    "x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = dbicgstabrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)\n\nWrapper for ``dbicgstabrevcom``.\n\nParameters\n----------\nb : input rank-1 array('d') with bounds (n)\nx : input rank-1 array('d') with bounds (n)\nwork : in/output rank-1 array('d') with bounds (7 * ldw)\niter : input int\nresid : input float\ninfo : input int\nndx1 : input int\nndx2 : input int\nijob : input int\n\nReturns\n-------\nx : rank-1 array('d') with bounds (n)\niter : int\nresid : float\ninfo : int\nndx1 : int\nndx2 : int\nsclr1 : float\nsclr2 : float\nijob : int\n"
    ...

def dcgrevcom(b, x, work, iter, resid, info, ndx1, ndx2, ijob) -> typing.Any:
    "x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = dcgrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)\n\nWrapper for ``dcgrevcom``.\n\nParameters\n----------\nb : input rank-1 array('d') with bounds (n)\nx : input rank-1 array('d') with bounds (n)\nwork : in/output rank-1 array('d') with bounds (4 * ldw)\niter : input int\nresid : input float\ninfo : input int\nndx1 : input int\nndx2 : input int\nijob : input int\n\nReturns\n-------\nx : rank-1 array('d') with bounds (n)\niter : int\nresid : float\ninfo : int\nndx1 : int\nndx2 : int\nsclr1 : float\nsclr2 : float\nijob : int\n"
    ...

def dcgsrevcom(b, x, work, iter, resid, info, ndx1, ndx2, ijob) -> typing.Any:
    "x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = dcgsrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)\n\nWrapper for ``dcgsrevcom``.\n\nParameters\n----------\nb : input rank-1 array('d') with bounds (n)\nx : input rank-1 array('d') with bounds (n)\nwork : in/output rank-1 array('d') with bounds (7 * ldw)\niter : input int\nresid : input float\ninfo : input int\nndx1 : input int\nndx2 : input int\nijob : input int\n\nReturns\n-------\nx : rank-1 array('d') with bounds (n)\niter : int\nresid : float\ninfo : int\nndx1 : int\nndx2 : int\nsclr1 : float\nsclr2 : float\nijob : int\n"
    ...

def dgmresrevcom(b, x, restrt, work, work2, iter, resid, info, ndx1, ndx2, ijob, tol) -> typing.Any:
    "x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = dgmresrevcom(b,x,restrt,work,work2,iter,resid,info,ndx1,ndx2,ijob,tol)\n\nWrapper for ``dgmresrevcom``.\n\nParameters\n----------\nb : input rank-1 array('d') with bounds (n)\nx : input rank-1 array('d') with bounds (n)\nrestrt : input int\nwork : in/output rank-1 array('d') with bounds (ldw*(6+restrt))\nwork2 : in/output rank-1 array('d') with bounds (ldw2*(2*restrt+2))\niter : input int\nresid : input float\ninfo : input int\nndx1 : input int\nndx2 : input int\nijob : input int\ntol : input float\n\nReturns\n-------\nx : rank-1 array('d') with bounds (n)\niter : int\nresid : float\ninfo : int\nndx1 : int\nndx2 : int\nsclr1 : float\nsclr2 : float\nijob : int\n"
    ...

def dqmrrevcom(b, x, work, iter, resid, info, ndx1, ndx2, ijob) -> typing.Any:
    "x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = dqmrrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)\n\nWrapper for ``dqmrrevcom``.\n\nParameters\n----------\nb : input rank-1 array('d') with bounds (n)\nx : input rank-1 array('d') with bounds (n)\nwork : in/output rank-1 array('d') with bounds (11 * ldw)\niter : input int\nresid : input float\ninfo : input int\nndx1 : input int\nndx2 : input int\nijob : input int\n\nReturns\n-------\nx : rank-1 array('d') with bounds (n)\niter : int\nresid : float\ninfo : int\nndx1 : int\nndx2 : int\nsclr1 : float\nsclr2 : float\nijob : int\n"
    ...

def sbicgrevcom(b, x, work, iter, resid, info, ndx1, ndx2, ijob) -> typing.Any:
    "x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = sbicgrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)\n\nWrapper for ``sbicgrevcom``.\n\nParameters\n----------\nb : input rank-1 array('f') with bounds (n)\nx : input rank-1 array('f') with bounds (n)\nwork : in/output rank-1 array('f') with bounds (6 * ldw)\niter : input int\nresid : input float\ninfo : input int\nndx1 : input int\nndx2 : input int\nijob : input int\n\nReturns\n-------\nx : rank-1 array('f') with bounds (n)\niter : int\nresid : float\ninfo : int\nndx1 : int\nndx2 : int\nsclr1 : float\nsclr2 : float\nijob : int\n"
    ...

def sbicgstabrevcom(b, x, work, iter, resid, info, ndx1, ndx2, ijob) -> typing.Any:
    "x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = sbicgstabrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)\n\nWrapper for ``sbicgstabrevcom``.\n\nParameters\n----------\nb : input rank-1 array('f') with bounds (n)\nx : input rank-1 array('f') with bounds (n)\nwork : in/output rank-1 array('f') with bounds (7 * ldw)\niter : input int\nresid : input float\ninfo : input int\nndx1 : input int\nndx2 : input int\nijob : input int\n\nReturns\n-------\nx : rank-1 array('f') with bounds (n)\niter : int\nresid : float\ninfo : int\nndx1 : int\nndx2 : int\nsclr1 : float\nsclr2 : float\nijob : int\n"
    ...

def scgrevcom(b, x, work, iter, resid, info, ndx1, ndx2, ijob) -> typing.Any:
    "x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = scgrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)\n\nWrapper for ``scgrevcom``.\n\nParameters\n----------\nb : input rank-1 array('f') with bounds (n)\nx : input rank-1 array('f') with bounds (n)\nwork : in/output rank-1 array('f') with bounds (4 * ldw)\niter : input int\nresid : input float\ninfo : input int\nndx1 : input int\nndx2 : input int\nijob : input int\n\nReturns\n-------\nx : rank-1 array('f') with bounds (n)\niter : int\nresid : float\ninfo : int\nndx1 : int\nndx2 : int\nsclr1 : float\nsclr2 : float\nijob : int\n"
    ...

def scgsrevcom(b, x, work, iter, resid, info, ndx1, ndx2, ijob) -> typing.Any:
    "x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = scgsrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)\n\nWrapper for ``scgsrevcom``.\n\nParameters\n----------\nb : input rank-1 array('f') with bounds (n)\nx : input rank-1 array('f') with bounds (n)\nwork : in/output rank-1 array('f') with bounds (7 * ldw)\niter : input int\nresid : input float\ninfo : input int\nndx1 : input int\nndx2 : input int\nijob : input int\n\nReturns\n-------\nx : rank-1 array('f') with bounds (n)\niter : int\nresid : float\ninfo : int\nndx1 : int\nndx2 : int\nsclr1 : float\nsclr2 : float\nijob : int\n"
    ...

def sgmresrevcom(b, x, restrt, work, work2, iter, resid, info, ndx1, ndx2, ijob, tol) -> typing.Any:
    "x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = sgmresrevcom(b,x,restrt,work,work2,iter,resid,info,ndx1,ndx2,ijob,tol)\n\nWrapper for ``sgmresrevcom``.\n\nParameters\n----------\nb : input rank-1 array('f') with bounds (n)\nx : input rank-1 array('f') with bounds (n)\nrestrt : input int\nwork : in/output rank-1 array('f') with bounds (ldw*(6+restrt))\nwork2 : in/output rank-1 array('f') with bounds (ldw2*(2*restrt+2))\niter : input int\nresid : input float\ninfo : input int\nndx1 : input int\nndx2 : input int\nijob : input int\ntol : input float\n\nReturns\n-------\nx : rank-1 array('f') with bounds (n)\niter : int\nresid : float\ninfo : int\nndx1 : int\nndx2 : int\nsclr1 : float\nsclr2 : float\nijob : int\n"
    ...

def sqmrrevcom(b, x, work, iter, resid, info, ndx1, ndx2, ijob) -> typing.Any:
    "x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = sqmrrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)\n\nWrapper for ``sqmrrevcom``.\n\nParameters\n----------\nb : input rank-1 array('f') with bounds (n)\nx : input rank-1 array('f') with bounds (n)\nwork : in/output rank-1 array('f') with bounds (11 * ldw)\niter : input int\nresid : input float\ninfo : input int\nndx1 : input int\nndx2 : input int\nijob : input int\n\nReturns\n-------\nx : rank-1 array('f') with bounds (n)\niter : int\nresid : float\ninfo : int\nndx1 : int\nndx2 : int\nsclr1 : float\nsclr2 : float\nijob : int\n"
    ...

def zbicgrevcom(b, x, work, iter, resid, info, ndx1, ndx2, ijob) -> typing.Any:
    "x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = zbicgrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)\n\nWrapper for ``zbicgrevcom``.\n\nParameters\n----------\nb : input rank-1 array('D') with bounds (n)\nx : input rank-1 array('D') with bounds (n)\nwork : in/output rank-1 array('D') with bounds (6 * ldw)\niter : input int\nresid : input float\ninfo : input int\nndx1 : input int\nndx2 : input int\nijob : input int\n\nReturns\n-------\nx : rank-1 array('D') with bounds (n)\niter : int\nresid : float\ninfo : int\nndx1 : int\nndx2 : int\nsclr1 : complex\nsclr2 : complex\nijob : int\n"
    ...

def zbicgstabrevcom(b, x, work, iter, resid, info, ndx1, ndx2, ijob) -> typing.Any:
    "x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = zbicgstabrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)\n\nWrapper for ``zbicgstabrevcom``.\n\nParameters\n----------\nb : input rank-1 array('D') with bounds (n)\nx : input rank-1 array('D') with bounds (n)\nwork : in/output rank-1 array('D') with bounds (7 * ldw)\niter : input int\nresid : input float\ninfo : input int\nndx1 : input int\nndx2 : input int\nijob : input int\n\nReturns\n-------\nx : rank-1 array('D') with bounds (n)\niter : int\nresid : float\ninfo : int\nndx1 : int\nndx2 : int\nsclr1 : complex\nsclr2 : complex\nijob : int\n"
    ...

def zcgrevcom(b, x, work, iter, resid, info, ndx1, ndx2, ijob) -> typing.Any:
    "x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = zcgrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)\n\nWrapper for ``zcgrevcom``.\n\nParameters\n----------\nb : input rank-1 array('D') with bounds (n)\nx : input rank-1 array('D') with bounds (n)\nwork : in/output rank-1 array('D') with bounds (4 * ldw)\niter : input int\nresid : input float\ninfo : input int\nndx1 : input int\nndx2 : input int\nijob : input int\n\nReturns\n-------\nx : rank-1 array('D') with bounds (n)\niter : int\nresid : float\ninfo : int\nndx1 : int\nndx2 : int\nsclr1 : complex\nsclr2 : complex\nijob : int\n"
    ...

def zcgsrevcom(b, x, work, iter, resid, info, ndx1, ndx2, ijob) -> typing.Any:
    "x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = zcgsrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)\n\nWrapper for ``zcgsrevcom``.\n\nParameters\n----------\nb : input rank-1 array('D') with bounds (n)\nx : input rank-1 array('D') with bounds (n)\nwork : in/output rank-1 array('D') with bounds (7 * ldw)\niter : input int\nresid : input float\ninfo : input int\nndx1 : input int\nndx2 : input int\nijob : input int\n\nReturns\n-------\nx : rank-1 array('D') with bounds (n)\niter : int\nresid : float\ninfo : int\nndx1 : int\nndx2 : int\nsclr1 : complex\nsclr2 : complex\nijob : int\n"
    ...

def zgmresrevcom(b, x, restrt, work, work2, iter, resid, info, ndx1, ndx2, ijob, tol) -> typing.Any:
    "x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = zgmresrevcom(b,x,restrt,work,work2,iter,resid,info,ndx1,ndx2,ijob,tol)\n\nWrapper for ``zgmresrevcom``.\n\nParameters\n----------\nb : input rank-1 array('D') with bounds (n)\nx : input rank-1 array('D') with bounds (n)\nrestrt : input int\nwork : in/output rank-1 array('D') with bounds (ldw*(6+restrt))\nwork2 : in/output rank-1 array('D') with bounds (ldw2*(2*restrt+2))\niter : input int\nresid : input float\ninfo : input int\nndx1 : input int\nndx2 : input int\nijob : input int\ntol : input float\n\nReturns\n-------\nx : rank-1 array('D') with bounds (n)\niter : int\nresid : float\ninfo : int\nndx1 : int\nndx2 : int\nsclr1 : complex\nsclr2 : complex\nijob : int\n"
    ...

def zqmrrevcom(b, x, work, iter, resid, info, ndx1, ndx2, ijob) -> typing.Any:
    "x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = zqmrrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)\n\nWrapper for ``zqmrrevcom``.\n\nParameters\n----------\nb : input rank-1 array('D') with bounds (n)\nx : input rank-1 array('D') with bounds (n)\nwork : in/output rank-1 array('D') with bounds (11 * ldw)\niter : input int\nresid : input float\ninfo : input int\nndx1 : input int\nndx2 : input int\nijob : input int\n\nReturns\n-------\nx : rank-1 array('D') with bounds (n)\niter : int\nresid : float\ninfo : int\nndx1 : int\nndx2 : int\nsclr1 : complex\nsclr2 : complex\nijob : int\n"
    ...

def __getattr__(name) -> typing.Any:
    ...

