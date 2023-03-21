# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: scipy, version: 1.6.2
# Module: scipy.interpolate._fitpack, version:  1.7 
import typing
import builtins as _mod_builtins

__doc__: typing.Any
__file__: str
__name__: str
__package__: str
__version__: str
def _bispev(tx, ty, c, kx, ky, x, y, nux, nuy) -> typing.Any:
    ' [z,ier] = _bispev(tx,ty,c,kx,ky,x,y,nux,nuy)'
    ...

def _bspldismat(order, xk) -> typing.Any:
    'B = _bspldismat(order,xk)\nConstruct the kth derivative discontinuity jump constraint matrix \nfor spline fitting of order k given sample positions in xk.\n\nIf xk is an integer (N+1), then the result is equivalent to\nxk=arange(N+1)+x0 for any value of x0.   This produces the\ninteger-spaced matrix a bit faster.  If xk is a 2-tuple (N+1,dx)\nthen it produces the result as if the sample distance were dx'
    ...

def _bspleval(xx, xk, coef, k, deriv) -> typing.Any:
    'y = _bspleval(xx,xk,coef,k,{deriv (0)})\n\nThe spline is defined by the approximation interval xk[0] to xk[-1],\nthe length of xk (N+1), the order of the spline, k, and \nthe number of coeficients N+k.  The coefficients range from xk_{-K}\nto xk_{N-1} inclusive and are all the coefficients needed to define\nan arbitrary spline of order k, on the given approximation interval\n\nExtra knot points are internally added using knot-point symmetry \naround xk[0] and xk[-1]'
    ...

def _bsplmat(order, xk) -> typing.Any:
    'B = _bsplmat(order,xk)\nConstruct the constraint matrix for spline fitting of order k\ngiven sample positions in xk.\n\nIf xk is an integer (N+1), then the result is equivalent to\nxk=arange(N+1)+x0 for any value of x0.   This produces the\ninteger-spaced, or cardinal spline matrix a bit faster.'
    ...

def _curfit(x, y, w, xb, xe, k, iopt, s, t, nest, wrk, iwrk, per) -> typing.Any:
    ' [t,c,o] = _curfit(x,y,w,xb,xe,k,iopt,s,t,nest,wrk,iwrk,per)'
    ...

def _insert(iopt, t, c, k, x, m) -> typing.Any:
    ' [tt,cc,ier] = _insert(iopt,t,c,k,x,m)'
    ...

def _parcur(x, w, u, ub, ue, k, iopt, ipar, s, t, nest, wrk, iwrk, per) -> typing.Any:
    ' [t,c,o] = _parcur(x,w,u,ub,ue,k,iopt,ipar,s,t,nest,wrk,iwrk,per)'
    ...

def _spalde(t, c, k, x) -> typing.Any:
    ' [d,ier] = _spalde(t,c,k,x)'
    ...

def _spl_(x, nu, t, c, k, e) -> typing.Any:
    ' [y,ier] = _spl_(x,nu,t,c,k,e)'
    ...

def _splint(t, c, k, a, b) -> typing.Any:
    ' [aint,wrk] = _splint(t,c,k,a,b)'
    ...

def _sproot(t, c, k, mest) -> typing.Any:
    ' [z,ier] = _sproot(t,c,k,mest)'
    ...

def _surfit(x, y, z, w, xb, xe, yb, ye, kx, ky, iopt, s, eps, tx, ty, nxest, nyest, wrk, lwrk1, lwrk2) -> typing.Any:
    ' [tx,ty,c,o] = _surfit(x, y, z, w, xb, xe, yb, ye, kx,ky,iopt,s,eps,tx,ty,nxest,nyest,wrk,lwrk1,lwrk2)'
    ...

def __getattr__(name) -> typing.Any:
    ...

