# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: scipy, version: 1.6.2
# Module: scipy.optimize._slsqp, version: $Revision: $
import typing
import builtins as _mod_builtins

__doc__: str
__file__: str
__name__: str
__package__: str
__version__: bytes
def slsqp(m, meq, x, xl, xu, f, c, g, a, acc, iter, mode, w, jw, alpha, f0, gs, h1, h2, h3, h4, t, t0, tol, iexact, incons, ireset, itermx, line, n1, n2, n3, la=..., n=..., l_w=..., l_jw=...) -> typing.Any:
    "slsqp(m,meq,x,xl,xu,f,c,g,a,acc,iter,mode,w,jw,alpha,f0,gs,h1,h2,h3,h4,t,t0,tol,iexact,incons,ireset,itermx,line,n1,n2,n3,[la,n,l_w,l_jw])\n\nWrapper for ``slsqp``.\n\nParameters\n----------\nm : input int\nmeq : input int\nx : in/output rank-1 array('d') with bounds (n)\nxl : input rank-1 array('d') with bounds (n)\nxu : input rank-1 array('d') with bounds (n)\nf : input float\nc : input rank-1 array('d') with bounds (la)\ng : input rank-1 array('d') with bounds (n + 1)\na : input rank-2 array('d') with bounds (la,n + 1)\nacc : in/output rank-0 array(float,'d')\niter : in/output rank-0 array(int,'i')\nmode : in/output rank-0 array(int,'i')\nw : input rank-1 array('d') with bounds (l_w)\njw : input rank-1 array('i') with bounds (l_jw)\nalpha : in/output rank-0 array(float,'d')\nf0 : in/output rank-0 array(float,'d')\ngs : in/output rank-0 array(float,'d')\nh1 : in/output rank-0 array(float,'d')\nh2 : in/output rank-0 array(float,'d')\nh3 : in/output rank-0 array(float,'d')\nh4 : in/output rank-0 array(float,'d')\nt : in/output rank-0 array(float,'d')\nt0 : in/output rank-0 array(float,'d')\ntol : in/output rank-0 array(float,'d')\niexact : in/output rank-0 array(int,'i')\nincons : in/output rank-0 array(int,'i')\nireset : in/output rank-0 array(int,'i')\nitermx : in/output rank-0 array(int,'i')\nline : in/output rank-0 array(int,'i')\nn1 : in/output rank-0 array(int,'i')\nn2 : in/output rank-0 array(int,'i')\nn3 : in/output rank-0 array(int,'i')\n\nOther Parameters\n----------------\nla : input int, optional\n    Default: len(c)\nn : input int, optional\n    Default: len(x)\nl_w : input int, optional\n    Default: len(w)\nl_jw : input int, optional\n    Default: len(jw)\n"
    ...

def __getattr__(name) -> typing.Any:
    ...

