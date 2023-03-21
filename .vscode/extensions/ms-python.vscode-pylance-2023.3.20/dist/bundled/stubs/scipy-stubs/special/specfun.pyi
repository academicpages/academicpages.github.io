# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: scipy, version: 1.6.2
# Module: scipy.special.specfun, version: $Revision: $
import typing
import builtins as _mod_builtins

__doc__: str
__file__: str
__name__: str
__package__: str
__version__: bytes
def airyzo(nt, kf=...) -> typing.Any:
    "xa,xb,xc,xd = airyzo(nt,[kf])\n\nWrapper for ``airyzo``.\n\nParameters\n----------\nnt : input int\n\nOther Parameters\n----------------\nkf : input int, optional\n    Default: 1\n\nReturns\n-------\nxa : rank-1 array('d') with bounds (nt)\nxb : rank-1 array('d') with bounds (nt)\nxc : rank-1 array('d') with bounds (nt)\nxd : rank-1 array('d') with bounds (nt)\n"
    ...

def bernob(n) -> typing.Any:
    "bn = bernob(n)\n\nWrapper for ``bernob``.\n\nParameters\n----------\nn : input int\n\nReturns\n-------\nbn : rank-1 array('d') with bounds (n + 1)\n"
    ...

def cerzo(nt) -> typing.Any:
    "zo = cerzo(nt)\n\nWrapper for ``cerzo``.\n\nParameters\n----------\nnt : input int\n\nReturns\n-------\nzo : rank-1 array('D') with bounds (nt)\n"
    ...

def clpmn(m, n, x, y, ntype) -> typing.Any:
    "cpm,cpd = clpmn(m,n,x,y,ntype)\n\nWrapper for ``clpmn``.\n\nParameters\n----------\nm : input int\nn : input int\nx : input float\ny : input float\nntype : input int\n\nReturns\n-------\ncpm : rank-2 array('D') with bounds (m + 1,n + 1)\ncpd : rank-2 array('D') with bounds (m + 1,n + 1)\n"
    ...

def clpn(n, z) -> typing.Any:
    "cpn,cpd = clpn(n,z)\n\nWrapper for ``clpn``.\n\nParameters\n----------\nn : input int\nz : input complex\n\nReturns\n-------\ncpn : rank-1 array('D') with bounds (n + 1)\ncpd : rank-1 array('D') with bounds (n + 1)\n"
    ...

def clqmn(m, n, z) -> typing.Any:
    "cqm,cqd = clqmn(m,n,z)\n\nWrapper for ``clqmn``.\n\nParameters\n----------\nm : input int\nn : input int\nz : input complex\n\nReturns\n-------\ncqm : rank-2 array('D') with bounds (mm + 1,n + 1)\ncqd : rank-2 array('D') with bounds (mm + 1,n + 1)\n"
    ...

def clqn(n, z) -> typing.Any:
    "cqn,cqd = clqn(n,z)\n\nWrapper for ``clqn``.\n\nParameters\n----------\nn : input int\nz : input complex\n\nReturns\n-------\ncqn : rank-1 array('D') with bounds (n + 1)\ncqd : rank-1 array('D') with bounds (n + 1)\n"
    ...

def cpbdn(n, z) -> typing.Any:
    "cpb,cpd = cpbdn(n,z)\n\nWrapper for ``cpbdn``.\n\nParameters\n----------\nn : input int\nz : input complex\n\nReturns\n-------\ncpb : rank-1 array('D') with bounds (abs(n)+2)\ncpd : rank-1 array('D') with bounds (abs(n)+2)\n"
    ...

def cyzo(nt, kf, kc) -> typing.Any:
    "zo,zv = cyzo(nt,kf,kc)\n\nWrapper for ``cyzo``.\n\nParameters\n----------\nnt : input int\nkf : input int\nkc : input int\n\nReturns\n-------\nzo : rank-1 array('D') with bounds (nt)\nzv : rank-1 array('D') with bounds (nt)\n"
    ...

def eulerb(n) -> typing.Any:
    "en = eulerb(n)\n\nWrapper for ``eulerb``.\n\nParameters\n----------\nn : input int\n\nReturns\n-------\nen : rank-1 array('d') with bounds (n + 1)\n"
    ...

def fcoef(kd, m, q, a) -> typing.Any:
    "fc = fcoef(kd,m,q,a)\n\nWrapper for ``fcoef``.\n\nParameters\n----------\nkd : input int\nm : input int\nq : input float\na : input float\n\nReturns\n-------\nfc : rank-1 array('d') with bounds (251)\n"
    ...

def fcszo(kf, nt) -> typing.Any:
    "zo = fcszo(kf,nt)\n\nWrapper for ``fcszo``.\n\nParameters\n----------\nkf : input int\nnt : input int\n\nReturns\n-------\nzo : rank-1 array('D') with bounds (nt)\n"
    ...

def jdzo(nt) -> typing.Any:
    "n,m,pcode,zo = jdzo(nt)\n\nWrapper for ``jdzo``.\n\nParameters\n----------\nnt : input int\n\nReturns\n-------\nn : rank-1 array('i') with bounds (1400)\nm : rank-1 array('i') with bounds (1400)\npcode : rank-1 array('i') with bounds (1400)\nzo : rank-1 array('d') with bounds (1401)\n"
    ...

def jyzo(n, nt) -> typing.Any:
    "rj0,rj1,ry0,ry1 = jyzo(n,nt)\n\nWrapper for ``jyzo``.\n\nParameters\n----------\nn : input int\nnt : input int\n\nReturns\n-------\nrj0 : rank-1 array('d') with bounds (nt)\nrj1 : rank-1 array('d') with bounds (nt)\nry0 : rank-1 array('d') with bounds (nt)\nry1 : rank-1 array('d') with bounds (nt)\n"
    ...

def klvnzo(nt, kd) -> typing.Any:
    "zo = klvnzo(nt,kd)\n\nWrapper for ``klvnzo``.\n\nParameters\n----------\nnt : input int\nkd : input int\n\nReturns\n-------\nzo : rank-1 array('d') with bounds (nt)\n"
    ...

def lamn(n, x) -> typing.Any:
    "nm,bl,dl = lamn(n,x)\n\nWrapper for ``lamn``.\n\nParameters\n----------\nn : input int\nx : input float\n\nReturns\n-------\nnm : int\nbl : rank-1 array('d') with bounds (n + 1)\ndl : rank-1 array('d') with bounds (n + 1)\n"
    ...

def lamv(v, x) -> typing.Any:
    "vm,vl,dl = lamv(v,x)\n\nWrapper for ``lamv``.\n\nParameters\n----------\nv : input float\nx : input float\n\nReturns\n-------\nvm : float\nvl : rank-1 array('d') with bounds ((int)v+1)\ndl : rank-1 array('d') with bounds ((int)v+1)\n"
    ...

def lpmn(m, n, x) -> typing.Any:
    "pm,pd = lpmn(m,n,x)\n\nWrapper for ``lpmn``.\n\nParameters\n----------\nm : input int\nn : input int\nx : input float\n\nReturns\n-------\npm : rank-2 array('d') with bounds (m + 1,n + 1)\npd : rank-2 array('d') with bounds (m + 1,n + 1)\n"
    ...

def lpn(n, x) -> typing.Any:
    "pn,pd = lpn(n,x)\n\nWrapper for ``lpn``.\n\nParameters\n----------\nn : input int\nx : input float\n\nReturns\n-------\npn : rank-1 array('d') with bounds (n + 1)\npd : rank-1 array('d') with bounds (n + 1)\n"
    ...

def lqmn(m, n, x) -> typing.Any:
    "qm,qd = lqmn(m,n,x)\n\nWrapper for ``lqmn``.\n\nParameters\n----------\nm : input int\nn : input int\nx : input float\n\nReturns\n-------\nqm : rank-2 array('d') with bounds (mm + 1,n + 1)\nqd : rank-2 array('d') with bounds (mm + 1,n + 1)\n"
    ...

def lqnb(n, x) -> typing.Any:
    "qn,qd = lqnb(n,x)\n\nWrapper for ``lqnb``.\n\nParameters\n----------\nn : input int\nx : input float\n\nReturns\n-------\nqn : rank-1 array('d') with bounds (n + 1)\nqd : rank-1 array('d') with bounds (n + 1)\n"
    ...

def pbdv(v, x) -> typing.Any:
    "dv,dp,pdf,pdd = pbdv(v,x)\n\nWrapper for ``pbdv``.\n\nParameters\n----------\nv : input float\nx : input float\n\nReturns\n-------\ndv : rank-1 array('d') with bounds (abs((int)v)+2)\ndp : rank-1 array('d') with bounds (abs((int)v)+2)\npdf : float\npdd : float\n"
    ...

def rctj(n, x) -> typing.Any:
    "nm,rj,dj = rctj(n,x)\n\nWrapper for ``rctj``.\n\nParameters\n----------\nn : input int\nx : input float\n\nReturns\n-------\nnm : int\nrj : rank-1 array('d') with bounds (n + 1)\ndj : rank-1 array('d') with bounds (n + 1)\n"
    ...

def rcty(n, x) -> typing.Any:
    "nm,ry,dy = rcty(n,x)\n\nWrapper for ``rcty``.\n\nParameters\n----------\nn : input int\nx : input float\n\nReturns\n-------\nnm : int\nry : rank-1 array('d') with bounds (n + 1)\ndy : rank-1 array('d') with bounds (n + 1)\n"
    ...

def segv(m, n, c, kd) -> typing.Any:
    "cv,eg = segv(m,n,c,kd)\n\nWrapper for ``segv``.\n\nParameters\n----------\nm : input int\nn : input int\nc : input float\nkd : input int\n\nReturns\n-------\ncv : float\neg : rank-1 array('d') with bounds (n-m+2)\n"
    ...

def __getattr__(name) -> typing.Any:
    ...

