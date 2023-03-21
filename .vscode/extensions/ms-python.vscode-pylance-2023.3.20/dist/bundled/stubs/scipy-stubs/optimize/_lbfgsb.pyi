# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: scipy, version: 1.6.2
# Module: scipy.optimize._lbfgsb, version: $Revision: $
import typing
import builtins as _mod_builtins

__doc__: str
__file__: str
__name__: str
__package__: str
__version__: bytes
def setulb(m, x, l, u, nbd, f, g, factr, pgtol, wa, iwa, task, iprint, csave, lsave, isave, dsave, maxls, n=...) -> typing.Any:
    "setulb(m,x,l,u,nbd,f,g,factr,pgtol,wa,iwa,task,iprint,csave,lsave,isave,dsave,maxls,[n])\n\nWrapper for ``setulb``.\n\nParameters\n----------\nm : input int\nx : in/output rank-1 array('d') with bounds (n)\nl : input rank-1 array('d') with bounds (n)\nu : input rank-1 array('d') with bounds (n)\nnbd : input rank-1 array('i') with bounds (n)\nf : in/output rank-0 array(float,'d')\ng : in/output rank-1 array('d') with bounds (n)\nfactr : input float\npgtol : input float\nwa : in/output rank-1 array('d') with bounds (2*m*n+5*n+11*m*m+8*m)\niwa : in/output rank-1 array('i') with bounds (3 * n)\ntask : in/output rank-0 array(string(len=60),'c')\niprint : input int\ncsave : in/output rank-0 array(string(len=60),'c')\nlsave : in/output rank-1 array('i') with bounds (4)\nisave : in/output rank-1 array('i') with bounds (44)\ndsave : in/output rank-1 array('d') with bounds (29)\nmaxls : input int\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: len(x)\n"
    ...

def types() -> typing.Any:
    "'i'-scalar\n"
    ...

def __getattr__(name) -> typing.Any:
    ...

