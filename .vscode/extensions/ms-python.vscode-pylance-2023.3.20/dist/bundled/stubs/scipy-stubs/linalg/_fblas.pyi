# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: scipy, version: 1.6.2
# Module: scipy.linalg._fblas, version: $Revision: $
import typing
import builtins as _mod_builtins

__doc__: str
__file__: str
__name__: str
__package__: str
__version__: bytes
def caxpy(x, y, n=..., a=..., offx=..., incx=..., offy=..., incy=...) -> typing.Any:
    "z = caxpy(x,y,[n,a,offx,incx,offy,incy])\n\nWrapper for ``caxpy``.\n\nParameters\n----------\nx : input rank-1 array('F') with bounds (*)\ny : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\na : input complex, optional\n    Default: (1.0, 0.0)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\n\nReturns\n-------\nz : rank-1 array('F') with bounds (*) and y storage\n"
    ...

def ccopy(x, y, n=..., offx=..., incx=..., offy=..., incy=...) -> typing.Any:
    "y = ccopy(x,y,[n,offx,incx,offy,incy])\n\nWrapper for ``ccopy``.\n\nParameters\n----------\nx : input rank-1 array('F') with bounds (*)\ny : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\n\nReturns\n-------\ny : rank-1 array('F') with bounds (*)\n"
    ...

def cdotc(x, y, n=..., offx=..., incx=..., offy=..., incy=...) -> typing.Any:
    "xy = cdotc(x,y,[n,offx,incx,offy,incy])\n\nWrapper for ``cdotc``.\n\nParameters\n----------\nx : input rank-1 array('F') with bounds (*)\ny : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\n\nReturns\n-------\nxy : complex\n"
    ...

def cdotu(x, y, n=..., offx=..., incx=..., offy=..., incy=...) -> typing.Any:
    "xy = cdotu(x,y,[n,offx,incx,offy,incy])\n\nWrapper for ``cdotu``.\n\nParameters\n----------\nx : input rank-1 array('F') with bounds (*)\ny : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\n\nReturns\n-------\nxy : complex\n"
    ...

def cgbmv(m, n, kl, ku, alpha, a, x, incx=..., offx=..., beta=..., y=..., incy=..., offy=..., trans=..., overwrite_y=...) -> typing.Any:
    "yout = cgbmv(m,n,kl,ku,alpha,a,x,[incx,offx,beta,y,incy,offy,trans,overwrite_y])\n\nWrapper for ``cgbmv``.\n\nParameters\n----------\nm : input int\nn : input int\nkl : input int\nku : input int\nalpha : input complex\na : input rank-2 array('F') with bounds (lda,n)\nx : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nbeta : input complex, optional\n    Default: (0.0, 0.0)\ny : input rank-1 array('F') with bounds (ly)\noverwrite_y : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\n\nReturns\n-------\nyout : rank-1 array('F') with bounds (ly) and y storage\n"
    ...

def cgemm(alpha, a, b, beta=..., c=..., trans_a=..., trans_b=..., overwrite_c=...) -> typing.Any:
    "c = cgemm(alpha,a,b,[beta,c,trans_a,trans_b,overwrite_c])\n\nWrapper for ``cgemm``.\n\nParameters\n----------\nalpha : input complex\na : input rank-2 array('F') with bounds (lda,ka)\nb : input rank-2 array('F') with bounds (ldb,kb)\n\nOther Parameters\n----------------\nbeta : input complex, optional\n    Default: (0.0, 0.0)\nc : input rank-2 array('F') with bounds (m,n)\noverwrite_c : input int, optional\n    Default: 0\ntrans_a : input int, optional\n    Default: 0\ntrans_b : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('F') with bounds (m,n)\n"
    ...

def cgemv(alpha, a, x, beta=..., y=..., offx=..., incx=..., offy=..., incy=..., trans=..., overwrite_y=...) -> typing.Any:
    "y = cgemv(alpha,a,x,[beta,y,offx,incx,offy,incy,trans,overwrite_y])\n\nWrapper for ``cgemv``.\n\nParameters\n----------\nalpha : input complex\na : input rank-2 array('F') with bounds (m,n)\nx : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\nbeta : input complex, optional\n    Default: (0.0, 0.0)\ny : input rank-1 array('F') with bounds (ly)\noverwrite_y : input int, optional\n    Default: 0\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\ntrans : input int, optional\n    Default: 0\n\nReturns\n-------\ny : rank-1 array('F') with bounds (ly)\n"
    ...

def cgerc(alpha, x, y, incx=..., incy=..., a=..., overwrite_x=..., overwrite_y=..., overwrite_a=...) -> typing.Any:
    "a = cgerc(alpha,x,y,[incx,incy,a,overwrite_x,overwrite_y,overwrite_a])\n\nWrapper for ``cgerc``.\n\nParameters\n----------\nalpha : input complex\nx : input rank-1 array('F') with bounds (m)\ny : input rank-1 array('F') with bounds (n)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 1\nincx : input int, optional\n    Default: 1\noverwrite_y : input int, optional\n    Default: 1\nincy : input int, optional\n    Default: 1\na : input rank-2 array('F') with bounds (m,n), optional\n    Default: (0.0,0.0)\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\na : rank-2 array('F') with bounds (m,n)\n"
    ...

def cgeru(alpha, x, y, incx=..., incy=..., a=..., overwrite_x=..., overwrite_y=..., overwrite_a=...) -> typing.Any:
    "a = cgeru(alpha,x,y,[incx,incy,a,overwrite_x,overwrite_y,overwrite_a])\n\nWrapper for ``cgeru``.\n\nParameters\n----------\nalpha : input complex\nx : input rank-1 array('F') with bounds (m)\ny : input rank-1 array('F') with bounds (n)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 1\nincx : input int, optional\n    Default: 1\noverwrite_y : input int, optional\n    Default: 1\nincy : input int, optional\n    Default: 1\na : input rank-2 array('F') with bounds (m,n), optional\n    Default: (0.0,0.0)\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\na : rank-2 array('F') with bounds (m,n)\n"
    ...

def chbmv(k, alpha, a, x, incx=..., offx=..., beta=..., y=..., incy=..., offy=..., lower=..., overwrite_y=...) -> typing.Any:
    "yout = chbmv(k,alpha,a,x,[incx,offx,beta,y,incy,offy,lower,overwrite_y])\n\nWrapper for ``chbmv``.\n\nParameters\n----------\nk : input int\nalpha : input complex\na : input rank-2 array('F') with bounds (lda,n)\nx : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nbeta : input complex, optional\n    Default: (0.0, 0.0)\ny : input rank-1 array('F') with bounds (ly)\noverwrite_y : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nyout : rank-1 array('F') with bounds (ly) and y storage\n"
    ...

def chemm(alpha, a, b, beta=..., c=..., side=..., lower=..., overwrite_c=...) -> typing.Any:
    "c = chemm(alpha,a,b,[beta,c,side,lower,overwrite_c])\n\nWrapper for ``chemm``.\n\nParameters\n----------\nalpha : input complex\na : input rank-2 array('F') with bounds (lda,ka)\nb : input rank-2 array('F') with bounds (ldb,kb)\n\nOther Parameters\n----------------\nbeta : input complex, optional\n    Default: (0.0, 0.0)\nc : input rank-2 array('F') with bounds (m,n)\noverwrite_c : input int, optional\n    Default: 0\nside : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('F') with bounds (m,n)\n"
    ...

def chemv(alpha, a, x, beta=..., y=..., offx=..., incx=..., offy=..., incy=..., lower=..., overwrite_y=...) -> typing.Any:
    "y = chemv(alpha,a,x,[beta,y,offx,incx,offy,incy,lower,overwrite_y])\n\nWrapper for ``chemv``.\n\nParameters\n----------\nalpha : input complex\na : input rank-2 array('F') with bounds (n,n)\nx : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\nbeta : input complex, optional\n    Default: (0.0, 0.0)\ny : input rank-1 array('F') with bounds (ly)\noverwrite_y : input int, optional\n    Default: 0\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\ny : rank-1 array('F') with bounds (ly)\n"
    ...

def cher(alpha, x, lower=..., incx=..., offx=..., n=..., a=..., overwrite_a=...) -> typing.Any:
    "a = cher(alpha,x,[lower,incx,offx,n,a,overwrite_a])\n\nWrapper for ``cher``.\n\nParameters\n----------\nalpha : input complex\nx : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nn : input int, optional\n    Default: (len(x)-1-offx)/abs(incx)+1\na : input rank-2 array('F') with bounds (n,n)\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\na : rank-2 array('F') with bounds (n,n)\n"
    ...

def cher2(alpha, x, y, lower=..., incx=..., offx=..., incy=..., offy=..., n=..., a=..., overwrite_a=...) -> typing.Any:
    "a = cher2(alpha,x,y,[lower,incx,offx,incy,offy,n,a,overwrite_a])\n\nWrapper for ``cher2``.\n\nParameters\n----------\nalpha : input complex\nx : input rank-1 array('F') with bounds (*)\ny : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nn : input int, optional\n    Default: ((len(x)-1-offx)/abs(incx)+1 <=(len(y)-1-offy)/abs(incy)+1 ?(len(x)-1-offx)/abs(incx)+1 :(len(y)-1-offy)/abs(incy)+1)\na : input rank-2 array('F') with bounds (n,n)\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\na : rank-2 array('F') with bounds (n,n)\n"
    ...

def cher2k(alpha, a, b, beta=..., c=..., trans=..., lower=..., overwrite_c=...) -> typing.Any:
    "c = cher2k(alpha,a,b,[beta,c,trans,lower,overwrite_c])\n\nWrapper for ``cher2k``.\n\nParameters\n----------\nalpha : input complex\na : input rank-2 array('F') with bounds (lda,ka)\nb : input rank-2 array('F') with bounds (ldb,kb)\n\nOther Parameters\n----------------\nbeta : input complex, optional\n    Default: (0.0, 0.0)\nc : input rank-2 array('F') with bounds (n,n)\noverwrite_c : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('F') with bounds (n,n)\n"
    ...

def cherk(alpha, a, beta=..., c=..., trans=..., lower=..., overwrite_c=...) -> typing.Any:
    "c = cherk(alpha,a,[beta,c,trans,lower,overwrite_c])\n\nWrapper for ``cherk``.\n\nParameters\n----------\nalpha : input complex\na : input rank-2 array('F') with bounds (lda,ka)\n\nOther Parameters\n----------------\nbeta : input complex, optional\n    Default: (0.0, 0.0)\nc : input rank-2 array('F') with bounds (n,n)\noverwrite_c : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('F') with bounds (n,n)\n"
    ...

def chpmv(n, alpha, ap, x, incx=..., offx=..., beta=..., y=..., incy=..., offy=..., lower=..., overwrite_y=...) -> typing.Any:
    "yout = chpmv(n,alpha,ap,x,[incx,offx,beta,y,incy,offy,lower,overwrite_y])\n\nWrapper for ``chpmv``.\n\nParameters\n----------\nn : input int\nalpha : input complex\nap : input rank-1 array('F') with bounds (*)\nx : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nbeta : input complex, optional\n    Default: (0.0, 0.0)\ny : input rank-1 array('F') with bounds (ly)\noverwrite_y : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nyout : rank-1 array('F') with bounds (ly) and y storage\n"
    ...

def chpr(n, alpha, x, ap, incx=..., offx=..., lower=..., overwrite_ap=...) -> typing.Any:
    "apu = chpr(n,alpha,x,ap,[incx,offx,lower,overwrite_ap])\n\nWrapper for ``chpr``.\n\nParameters\n----------\nn : input int\nalpha : input float\nx : input rank-1 array('F') with bounds (*)\nap : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\noverwrite_ap : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\napu : rank-1 array('F') with bounds (*) and ap storage\n"
    ...

def chpr2(n, alpha, x, y, ap, incx=..., offx=..., incy=..., offy=..., lower=..., overwrite_ap=...) -> typing.Any:
    "apu = chpr2(n,alpha,x,y,ap,[incx,offx,incy,offy,lower,overwrite_ap])\n\nWrapper for ``chpr2``.\n\nParameters\n----------\nn : input int\nalpha : input complex\nx : input rank-1 array('F') with bounds (*)\ny : input rank-1 array('F') with bounds (*)\nap : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\noverwrite_ap : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\napu : rank-1 array('F') with bounds (*) and ap storage\n"
    ...

def crotg(a, b) -> typing.Any:
    'c,s = crotg(a,b)\n\nWrapper for ``crotg``.\n\nParameters\n----------\na : input complex\nb : input complex\n\nReturns\n-------\nc : complex\ns : complex\n'
    ...

def cscal(a, x, n=..., offx=..., incx=...) -> typing.Any:
    "x = cscal(a,x,[n,offx,incx])\n\nWrapper for ``cscal``.\n\nParameters\n----------\na : input complex\nx : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\n\nReturns\n-------\nx : rank-1 array('F') with bounds (*)\n"
    ...

def cspmv(n, alpha, ap, x, incx=..., offx=..., beta=..., y=..., incy=..., offy=..., lower=..., overwrite_y=...) -> typing.Any:
    "yout = cspmv(n,alpha,ap,x,[incx,offx,beta,y,incy,offy,lower,overwrite_y])\n\nWrapper for ``cspmv``.\n\nParameters\n----------\nn : input int\nalpha : input complex\nap : input rank-1 array('F') with bounds (*)\nx : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nbeta : input complex, optional\n    Default: (0.0, 0.0)\ny : input rank-1 array('F') with bounds (ly)\noverwrite_y : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nyout : rank-1 array('F') with bounds (ly) and y storage\n"
    ...

def cspr(n, alpha, x, ap, incx=..., offx=..., lower=..., overwrite_ap=...) -> typing.Any:
    "apu = cspr(n,alpha,x,ap,[incx,offx,lower,overwrite_ap])\n\nWrapper for ``cspr``.\n\nParameters\n----------\nn : input int\nalpha : input complex\nx : input rank-1 array('F') with bounds (*)\nap : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\noverwrite_ap : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\napu : rank-1 array('F') with bounds (*) and ap storage\n"
    ...

def csrot(x, y, c, s, n=..., offx=..., incx=..., offy=..., incy=..., overwrite_x=..., overwrite_y=...) -> typing.Any:
    "x,y = csrot(x,y,c,s,[n,offx,incx,offy,incy,overwrite_x,overwrite_y])\n\nWrapper for ``csrot``.\n\nParameters\n----------\nx : input rank-1 array('F') with bounds (*)\ny : input rank-1 array('F') with bounds (*)\nc : input float\ns : input float\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-1-offx)/abs(incx)+1\noverwrite_x : input int, optional\n    Default: 0\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noverwrite_y : input int, optional\n    Default: 0\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\n\nReturns\n-------\nx : rank-1 array('F') with bounds (*)\ny : rank-1 array('F') with bounds (*)\n"
    ...

def csscal(a, x, n=..., offx=..., incx=..., overwrite_x=...) -> typing.Any:
    "x = csscal(a,x,[n,offx,incx,overwrite_x])\n\nWrapper for ``csscal``.\n\nParameters\n----------\na : input float\nx : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noverwrite_x : input int, optional\n    Default: 0\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\n\nReturns\n-------\nx : rank-1 array('F') with bounds (*)\n"
    ...

def cswap(x, y, n=..., offx=..., incx=..., offy=..., incy=...) -> typing.Any:
    "x,y = cswap(x,y,[n,offx,incx,offy,incy])\n\nWrapper for ``cswap``.\n\nParameters\n----------\nx : input rank-1 array('F') with bounds (*)\ny : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\n\nReturns\n-------\nx : rank-1 array('F') with bounds (*)\ny : rank-1 array('F') with bounds (*)\n"
    ...

def csymm(alpha, a, b, beta=..., c=..., side=..., lower=..., overwrite_c=...) -> typing.Any:
    "c = csymm(alpha,a,b,[beta,c,side,lower,overwrite_c])\n\nWrapper for ``csymm``.\n\nParameters\n----------\nalpha : input complex\na : input rank-2 array('F') with bounds (lda,ka)\nb : input rank-2 array('F') with bounds (ldb,kb)\n\nOther Parameters\n----------------\nbeta : input complex, optional\n    Default: (0.0, 0.0)\nc : input rank-2 array('F') with bounds (m,n)\noverwrite_c : input int, optional\n    Default: 0\nside : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('F') with bounds (m,n)\n"
    ...

def csyr(alpha, x, lower=..., incx=..., offx=..., n=..., a=..., overwrite_a=...) -> typing.Any:
    "a = csyr(alpha,x,[lower,incx,offx,n,a,overwrite_a])\n\nWrapper for ``csyr``.\n\nParameters\n----------\nalpha : input complex\nx : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nn : input int, optional\n    Default: (len(x)-1-offx)/abs(incx)+1\na : input rank-2 array('F') with bounds (n,n)\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\na : rank-2 array('F') with bounds (n,n)\n"
    ...

def csyr2k(alpha, a, b, beta=..., c=..., trans=..., lower=..., overwrite_c=...) -> typing.Any:
    "c = csyr2k(alpha,a,b,[beta,c,trans,lower,overwrite_c])\n\nWrapper for ``csyr2k``.\n\nParameters\n----------\nalpha : input complex\na : input rank-2 array('F') with bounds (lda,ka)\nb : input rank-2 array('F') with bounds (ldb,kb)\n\nOther Parameters\n----------------\nbeta : input complex, optional\n    Default: (0.0, 0.0)\nc : input rank-2 array('F') with bounds (n,n)\noverwrite_c : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('F') with bounds (n,n)\n"
    ...

def csyrk(alpha, a, beta=..., c=..., trans=..., lower=..., overwrite_c=...) -> typing.Any:
    "c = csyrk(alpha,a,[beta,c,trans,lower,overwrite_c])\n\nWrapper for ``csyrk``.\n\nParameters\n----------\nalpha : input complex\na : input rank-2 array('F') with bounds (lda,ka)\n\nOther Parameters\n----------------\nbeta : input complex, optional\n    Default: (0.0, 0.0)\nc : input rank-2 array('F') with bounds (n,n)\noverwrite_c : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('F') with bounds (n,n)\n"
    ...

def ctbmv(k, a, x, incx=..., offx=..., lower=..., trans=..., diag=..., overwrite_x=...) -> typing.Any:
    "xout = ctbmv(k,a,x,[incx,offx,lower,trans,diag,overwrite_x])\n\nWrapper for ``ctbmv``.\n\nParameters\n----------\nk : input int\na : input rank-2 array('F') with bounds (lda,n)\nx : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nxout : rank-1 array('F') with bounds (*) and x storage\n"
    ...

def ctbsv(k, a, x, incx=..., offx=..., lower=..., trans=..., diag=..., overwrite_x=...) -> typing.Any:
    "xout = ctbsv(k,a,x,[incx,offx,lower,trans,diag,overwrite_x])\n\nWrapper for ``ctbsv``.\n\nParameters\n----------\nk : input int\na : input rank-2 array('F') with bounds (lda,n)\nx : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nxout : rank-1 array('F') with bounds (*) and x storage\n"
    ...

def ctpmv(n, ap, x, incx=..., offx=..., lower=..., trans=..., diag=..., overwrite_x=...) -> typing.Any:
    "xout = ctpmv(n,ap,x,[incx,offx,lower,trans,diag,overwrite_x])\n\nWrapper for ``ctpmv``.\n\nParameters\n----------\nn : input int\nap : input rank-1 array('F') with bounds (*)\nx : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nxout : rank-1 array('F') with bounds (*) and x storage\n"
    ...

def ctpsv(n, ap, x, incx=..., offx=..., lower=..., trans=..., diag=..., overwrite_x=...) -> typing.Any:
    "xout = ctpsv(n,ap,x,[incx,offx,lower,trans,diag,overwrite_x])\n\nWrapper for ``ctpsv``.\n\nParameters\n----------\nn : input int\nap : input rank-1 array('F') with bounds (*)\nx : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nxout : rank-1 array('F') with bounds (*) and x storage\n"
    ...

def ctrmm(alpha, a, b, side=..., lower=..., trans_a=..., diag=..., overwrite_b=...) -> typing.Any:
    "b = ctrmm(alpha,a,b,[side,lower,trans_a,diag,overwrite_b])\n\nWrapper for ``ctrmm``.\n\nParameters\n----------\nalpha : input complex\na : input rank-2 array('F') with bounds (lda,k)\nb : input rank-2 array('F') with bounds (ldb,n)\n\nOther Parameters\n----------------\noverwrite_b : input int, optional\n    Default: 0\nside : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\ntrans_a : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nb : rank-2 array('F') with bounds (ldb,n)\n"
    ...

def ctrmv(a, x, offx=..., incx=..., lower=..., trans=..., diag=..., overwrite_x=...) -> typing.Any:
    "x = ctrmv(a,x,[offx,incx,lower,trans,diag,overwrite_x])\n\nWrapper for ``ctrmv``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (n,n)\nx : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\nlower : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-1 array('F') with bounds (*)\n"
    ...

def ctrsm(alpha, a, b, side=..., lower=..., trans_a=..., diag=..., overwrite_b=...) -> typing.Any:
    "x = ctrsm(alpha,a,b,[side,lower,trans_a,diag,overwrite_b])\n\nWrapper for ``ctrsm``.\n\nParameters\n----------\nalpha : input complex\na : input rank-2 array('F') with bounds (lda,*)\nb : input rank-2 array('F') with bounds (ldb,n)\n\nOther Parameters\n----------------\noverwrite_b : input int, optional\n    Default: 0\nside : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\ntrans_a : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('F') with bounds (ldb,n) and b storage\n"
    ...

def ctrsv(a, x, incx=..., offx=..., lower=..., trans=..., diag=..., overwrite_x=...) -> typing.Any:
    "xout = ctrsv(a,x,[incx,offx,lower,trans,diag,overwrite_x])\n\nWrapper for ``ctrsv``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (n,n)\nx : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nxout : rank-1 array('F') with bounds (*) and x storage\n"
    ...

def dasum(x, n=..., offx=..., incx=...) -> typing.Any:
    "s = dasum(x,[n,offx,incx])\n\nWrapper for ``dasum``.\n\nParameters\n----------\nx : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\n\nReturns\n-------\ns : float\n"
    ...

def daxpy(x, y, n=..., a=..., offx=..., incx=..., offy=..., incy=...) -> typing.Any:
    "z = daxpy(x,y,[n,a,offx,incx,offy,incy])\n\nWrapper for ``daxpy``.\n\nParameters\n----------\nx : input rank-1 array('d') with bounds (*)\ny : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\na : input float, optional\n    Default: 1.0\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\n\nReturns\n-------\nz : rank-1 array('d') with bounds (*) and y storage\n"
    ...

def dcopy(x, y, n=..., offx=..., incx=..., offy=..., incy=...) -> typing.Any:
    "y = dcopy(x,y,[n,offx,incx,offy,incy])\n\nWrapper for ``dcopy``.\n\nParameters\n----------\nx : input rank-1 array('d') with bounds (*)\ny : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\n\nReturns\n-------\ny : rank-1 array('d') with bounds (*)\n"
    ...

def ddot(x, y, n=..., offx=..., incx=..., offy=..., incy=...) -> typing.Any:
    "xy = ddot(x,y,[n,offx,incx,offy,incy])\n\nWrapper for ``ddot``.\n\nParameters\n----------\nx : input rank-1 array('d') with bounds (*)\ny : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\n\nReturns\n-------\nxy : float\n"
    ...

def dgbmv(m, n, kl, ku, alpha, a, x, incx=..., offx=..., beta=..., y=..., incy=..., offy=..., trans=..., overwrite_y=...) -> typing.Any:
    "yout = dgbmv(m,n,kl,ku,alpha,a,x,[incx,offx,beta,y,incy,offy,trans,overwrite_y])\n\nWrapper for ``dgbmv``.\n\nParameters\n----------\nm : input int\nn : input int\nkl : input int\nku : input int\nalpha : input float\na : input rank-2 array('d') with bounds (lda,n)\nx : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nbeta : input float, optional\n    Default: 0.0\ny : input rank-1 array('d') with bounds (ly)\noverwrite_y : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\n\nReturns\n-------\nyout : rank-1 array('d') with bounds (ly) and y storage\n"
    ...

def dgemm(alpha, a, b, beta=..., c=..., trans_a=..., trans_b=..., overwrite_c=...) -> typing.Any:
    "c = dgemm(alpha,a,b,[beta,c,trans_a,trans_b,overwrite_c])\n\nWrapper for ``dgemm``.\n\nParameters\n----------\nalpha : input float\na : input rank-2 array('d') with bounds (lda,ka)\nb : input rank-2 array('d') with bounds (ldb,kb)\n\nOther Parameters\n----------------\nbeta : input float, optional\n    Default: 0.0\nc : input rank-2 array('d') with bounds (m,n)\noverwrite_c : input int, optional\n    Default: 0\ntrans_a : input int, optional\n    Default: 0\ntrans_b : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('d') with bounds (m,n)\n"
    ...

def dgemv(alpha, a, x, beta=..., y=..., offx=..., incx=..., offy=..., incy=..., trans=..., overwrite_y=...) -> typing.Any:
    "y = dgemv(alpha,a,x,[beta,y,offx,incx,offy,incy,trans,overwrite_y])\n\nWrapper for ``dgemv``.\n\nParameters\n----------\nalpha : input float\na : input rank-2 array('d') with bounds (m,n)\nx : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\nbeta : input float, optional\n    Default: 0.0\ny : input rank-1 array('d') with bounds (ly)\noverwrite_y : input int, optional\n    Default: 0\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\ntrans : input int, optional\n    Default: 0\n\nReturns\n-------\ny : rank-1 array('d') with bounds (ly)\n"
    ...

def dger(alpha, x, y, incx=..., incy=..., a=..., overwrite_x=..., overwrite_y=..., overwrite_a=...) -> typing.Any:
    "a = dger(alpha,x,y,[incx,incy,a,overwrite_x,overwrite_y,overwrite_a])\n\nWrapper for ``dger``.\n\nParameters\n----------\nalpha : input float\nx : input rank-1 array('d') with bounds (m)\ny : input rank-1 array('d') with bounds (n)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 1\nincx : input int, optional\n    Default: 1\noverwrite_y : input int, optional\n    Default: 1\nincy : input int, optional\n    Default: 1\na : input rank-2 array('d') with bounds (m,n), optional\n    Default: 0.0\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\na : rank-2 array('d') with bounds (m,n)\n"
    ...

def dnrm2(x, n=..., offx=..., incx=...) -> typing.Any:
    "n2 = dnrm2(x,[n,offx,incx])\n\nWrapper for ``dnrm2``.\n\nParameters\n----------\nx : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\n\nReturns\n-------\nn2 : float\n"
    ...

def drot(x, y, c, s, n=..., offx=..., incx=..., offy=..., incy=..., overwrite_x=..., overwrite_y=...) -> typing.Any:
    "x,y = drot(x,y,c,s,[n,offx,incx,offy,incy,overwrite_x,overwrite_y])\n\nWrapper for ``drot``.\n\nParameters\n----------\nx : input rank-1 array('d') with bounds (*)\ny : input rank-1 array('d') with bounds (*)\nc : input float\ns : input float\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-1-offx)/abs(incx)+1\noverwrite_x : input int, optional\n    Default: 0\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noverwrite_y : input int, optional\n    Default: 0\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\n\nReturns\n-------\nx : rank-1 array('d') with bounds (*)\ny : rank-1 array('d') with bounds (*)\n"
    ...

def drotg(a, b) -> typing.Any:
    'c,s = drotg(a,b)\n\nWrapper for ``drotg``.\n\nParameters\n----------\na : input float\nb : input float\n\nReturns\n-------\nc : float\ns : float\n'
    ...

def drotm(x, y, param, n=..., offx=..., incx=..., offy=..., incy=..., overwrite_x=..., overwrite_y=...) -> typing.Any:
    "x,y = drotm(x,y,param,[n,offx,incx,offy,incy,overwrite_x,overwrite_y])\n\nWrapper for ``drotm``.\n\nParameters\n----------\nx : input rank-1 array('d') with bounds (*)\ny : input rank-1 array('d') with bounds (*)\nparam : input rank-1 array('d') with bounds (5)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noverwrite_x : input int, optional\n    Default: 0\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noverwrite_y : input int, optional\n    Default: 0\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\n\nReturns\n-------\nx : rank-1 array('d') with bounds (*)\ny : rank-1 array('d') with bounds (*)\n"
    ...

def drotmg(d1, d2, x1, y1) -> typing.Any:
    "param = drotmg(d1,d2,x1,y1)\n\nWrapper for ``drotmg``.\n\nParameters\n----------\nd1 : input float\nd2 : input float\nx1 : input float\ny1 : input float\n\nReturns\n-------\nparam : rank-1 array('d') with bounds (5)\n"
    ...

def dsbmv(k, alpha, a, x, incx=..., offx=..., beta=..., y=..., incy=..., offy=..., lower=..., overwrite_y=...) -> typing.Any:
    "yout = dsbmv(k,alpha,a,x,[incx,offx,beta,y,incy,offy,lower,overwrite_y])\n\nWrapper for ``dsbmv``.\n\nParameters\n----------\nk : input int\nalpha : input float\na : input rank-2 array('d') with bounds (lda,n)\nx : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nbeta : input float, optional\n    Default: 0.0\ny : input rank-1 array('d') with bounds (ly)\noverwrite_y : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nyout : rank-1 array('d') with bounds (ly) and y storage\n"
    ...

def dscal(a, x, n=..., offx=..., incx=...) -> typing.Any:
    "x = dscal(a,x,[n,offx,incx])\n\nWrapper for ``dscal``.\n\nParameters\n----------\na : input float\nx : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\n\nReturns\n-------\nx : rank-1 array('d') with bounds (*)\n"
    ...

def dspmv(n, alpha, ap, x, incx=..., offx=..., beta=..., y=..., incy=..., offy=..., lower=..., overwrite_y=...) -> typing.Any:
    "yout = dspmv(n,alpha,ap,x,[incx,offx,beta,y,incy,offy,lower,overwrite_y])\n\nWrapper for ``dspmv``.\n\nParameters\n----------\nn : input int\nalpha : input float\nap : input rank-1 array('d') with bounds (*)\nx : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nbeta : input float, optional\n    Default: 0.0\ny : input rank-1 array('d') with bounds (ly)\noverwrite_y : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nyout : rank-1 array('d') with bounds (ly) and y storage\n"
    ...

def dspr(n, alpha, x, ap, incx=..., offx=..., lower=..., overwrite_ap=...) -> typing.Any:
    "apu = dspr(n,alpha,x,ap,[incx,offx,lower,overwrite_ap])\n\nWrapper for ``dspr``.\n\nParameters\n----------\nn : input int\nalpha : input float\nx : input rank-1 array('d') with bounds (*)\nap : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\noverwrite_ap : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\napu : rank-1 array('d') with bounds (*) and ap storage\n"
    ...

def dspr2(n, alpha, x, y, ap, incx=..., offx=..., incy=..., offy=..., lower=..., overwrite_ap=...) -> typing.Any:
    "apu = dspr2(n,alpha,x,y,ap,[incx,offx,incy,offy,lower,overwrite_ap])\n\nWrapper for ``dspr2``.\n\nParameters\n----------\nn : input int\nalpha : input float\nx : input rank-1 array('d') with bounds (*)\ny : input rank-1 array('d') with bounds (*)\nap : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\noverwrite_ap : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\napu : rank-1 array('d') with bounds (*) and ap storage\n"
    ...

def dswap(x, y, n=..., offx=..., incx=..., offy=..., incy=...) -> typing.Any:
    "x,y = dswap(x,y,[n,offx,incx,offy,incy])\n\nWrapper for ``dswap``.\n\nParameters\n----------\nx : input rank-1 array('d') with bounds (*)\ny : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\n\nReturns\n-------\nx : rank-1 array('d') with bounds (*)\ny : rank-1 array('d') with bounds (*)\n"
    ...

def dsymm(alpha, a, b, beta=..., c=..., side=..., lower=..., overwrite_c=...) -> typing.Any:
    "c = dsymm(alpha,a,b,[beta,c,side,lower,overwrite_c])\n\nWrapper for ``dsymm``.\n\nParameters\n----------\nalpha : input float\na : input rank-2 array('d') with bounds (lda,ka)\nb : input rank-2 array('d') with bounds (ldb,kb)\n\nOther Parameters\n----------------\nbeta : input float, optional\n    Default: 0.0\nc : input rank-2 array('d') with bounds (m,n)\noverwrite_c : input int, optional\n    Default: 0\nside : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('d') with bounds (m,n)\n"
    ...

def dsymv(alpha, a, x, beta=..., y=..., offx=..., incx=..., offy=..., incy=..., lower=..., overwrite_y=...) -> typing.Any:
    "y = dsymv(alpha,a,x,[beta,y,offx,incx,offy,incy,lower,overwrite_y])\n\nWrapper for ``dsymv``.\n\nParameters\n----------\nalpha : input float\na : input rank-2 array('d') with bounds (n,n)\nx : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\nbeta : input float, optional\n    Default: 0.0\ny : input rank-1 array('d') with bounds (ly)\noverwrite_y : input int, optional\n    Default: 0\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\ny : rank-1 array('d') with bounds (ly)\n"
    ...

def dsyr(alpha, x, lower=..., incx=..., offx=..., n=..., a=..., overwrite_a=...) -> typing.Any:
    "a = dsyr(alpha,x,[lower,incx,offx,n,a,overwrite_a])\n\nWrapper for ``dsyr``.\n\nParameters\n----------\nalpha : input float\nx : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nn : input int, optional\n    Default: (len(x)-1-offx)/abs(incx)+1\na : input rank-2 array('d') with bounds (n,n)\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\na : rank-2 array('d') with bounds (n,n)\n"
    ...

def dsyr2(alpha, x, y, lower=..., incx=..., offx=..., incy=..., offy=..., n=..., a=..., overwrite_a=...) -> typing.Any:
    "a = dsyr2(alpha,x,y,[lower,incx,offx,incy,offy,n,a,overwrite_a])\n\nWrapper for ``dsyr2``.\n\nParameters\n----------\nalpha : input float\nx : input rank-1 array('d') with bounds (*)\ny : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nn : input int, optional\n    Default: ((len(x)-1-offx)/abs(incx)+1 <=(len(y)-1-offy)/abs(incy)+1 ?(len(x)-1-offx)/abs(incx)+1 :(len(y)-1-offy)/abs(incy)+1)\na : input rank-2 array('d') with bounds (n,n)\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\na : rank-2 array('d') with bounds (n,n)\n"
    ...

def dsyr2k(alpha, a, b, beta=..., c=..., trans=..., lower=..., overwrite_c=...) -> typing.Any:
    "c = dsyr2k(alpha,a,b,[beta,c,trans,lower,overwrite_c])\n\nWrapper for ``dsyr2k``.\n\nParameters\n----------\nalpha : input float\na : input rank-2 array('d') with bounds (lda,ka)\nb : input rank-2 array('d') with bounds (ldb,kb)\n\nOther Parameters\n----------------\nbeta : input float, optional\n    Default: 0.0\nc : input rank-2 array('d') with bounds (n,n)\noverwrite_c : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('d') with bounds (n,n)\n"
    ...

def dsyrk(alpha, a, beta=..., c=..., trans=..., lower=..., overwrite_c=...) -> typing.Any:
    "c = dsyrk(alpha,a,[beta,c,trans,lower,overwrite_c])\n\nWrapper for ``dsyrk``.\n\nParameters\n----------\nalpha : input float\na : input rank-2 array('d') with bounds (lda,ka)\n\nOther Parameters\n----------------\nbeta : input float, optional\n    Default: 0.0\nc : input rank-2 array('d') with bounds (n,n)\noverwrite_c : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('d') with bounds (n,n)\n"
    ...

def dtbmv(k, a, x, incx=..., offx=..., lower=..., trans=..., diag=..., overwrite_x=...) -> typing.Any:
    "xout = dtbmv(k,a,x,[incx,offx,lower,trans,diag,overwrite_x])\n\nWrapper for ``dtbmv``.\n\nParameters\n----------\nk : input int\na : input rank-2 array('d') with bounds (lda,n)\nx : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nxout : rank-1 array('d') with bounds (*) and x storage\n"
    ...

def dtbsv(k, a, x, incx=..., offx=..., lower=..., trans=..., diag=..., overwrite_x=...) -> typing.Any:
    "xout = dtbsv(k,a,x,[incx,offx,lower,trans,diag,overwrite_x])\n\nWrapper for ``dtbsv``.\n\nParameters\n----------\nk : input int\na : input rank-2 array('d') with bounds (lda,n)\nx : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nxout : rank-1 array('d') with bounds (*) and x storage\n"
    ...

def dtpmv(n, ap, x, incx=..., offx=..., lower=..., trans=..., diag=..., overwrite_x=...) -> typing.Any:
    "xout = dtpmv(n,ap,x,[incx,offx,lower,trans,diag,overwrite_x])\n\nWrapper for ``dtpmv``.\n\nParameters\n----------\nn : input int\nap : input rank-1 array('d') with bounds (*)\nx : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nxout : rank-1 array('d') with bounds (*) and x storage\n"
    ...

def dtpsv(n, ap, x, incx=..., offx=..., lower=..., trans=..., diag=..., overwrite_x=...) -> typing.Any:
    "xout = dtpsv(n,ap,x,[incx,offx,lower,trans,diag,overwrite_x])\n\nWrapper for ``dtpsv``.\n\nParameters\n----------\nn : input int\nap : input rank-1 array('d') with bounds (*)\nx : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nxout : rank-1 array('d') with bounds (*) and x storage\n"
    ...

def dtrmm(alpha, a, b, side=..., lower=..., trans_a=..., diag=..., overwrite_b=...) -> typing.Any:
    "b = dtrmm(alpha,a,b,[side,lower,trans_a,diag,overwrite_b])\n\nWrapper for ``dtrmm``.\n\nParameters\n----------\nalpha : input float\na : input rank-2 array('d') with bounds (lda,k)\nb : input rank-2 array('d') with bounds (ldb,n)\n\nOther Parameters\n----------------\noverwrite_b : input int, optional\n    Default: 0\nside : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\ntrans_a : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nb : rank-2 array('d') with bounds (ldb,n)\n"
    ...

def dtrmv(a, x, offx=..., incx=..., lower=..., trans=..., diag=..., overwrite_x=...) -> typing.Any:
    "x = dtrmv(a,x,[offx,incx,lower,trans,diag,overwrite_x])\n\nWrapper for ``dtrmv``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (n,n)\nx : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\nlower : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-1 array('d') with bounds (*)\n"
    ...

def dtrsm(alpha, a, b, side=..., lower=..., trans_a=..., diag=..., overwrite_b=...) -> typing.Any:
    "x = dtrsm(alpha,a,b,[side,lower,trans_a,diag,overwrite_b])\n\nWrapper for ``dtrsm``.\n\nParameters\n----------\nalpha : input float\na : input rank-2 array('d') with bounds (lda,*)\nb : input rank-2 array('d') with bounds (ldb,n)\n\nOther Parameters\n----------------\noverwrite_b : input int, optional\n    Default: 0\nside : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\ntrans_a : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('d') with bounds (ldb,n) and b storage\n"
    ...

def dtrsv(a, x, incx=..., offx=..., lower=..., trans=..., diag=..., overwrite_x=...) -> typing.Any:
    "xout = dtrsv(a,x,[incx,offx,lower,trans,diag,overwrite_x])\n\nWrapper for ``dtrsv``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (n,n)\nx : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nxout : rank-1 array('d') with bounds (*) and x storage\n"
    ...

def dzasum(x, n=..., offx=..., incx=...) -> typing.Any:
    "s = dzasum(x,[n,offx,incx])\n\nWrapper for ``dzasum``.\n\nParameters\n----------\nx : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\n\nReturns\n-------\ns : float\n"
    ...

def dznrm2(x, n=..., offx=..., incx=...) -> typing.Any:
    "n2 = dznrm2(x,[n,offx,incx])\n\nWrapper for ``dznrm2``.\n\nParameters\n----------\nx : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\n\nReturns\n-------\nn2 : float\n"
    ...

def icamax(x, n=..., offx=..., incx=...) -> typing.Any:
    "k = icamax(x,[n,offx,incx])\n\nWrapper for ``icamax``.\n\nParameters\n----------\nx : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\n\nReturns\n-------\nk : int\n"
    ...

def idamax(x, n=..., offx=..., incx=...) -> typing.Any:
    "k = idamax(x,[n,offx,incx])\n\nWrapper for ``idamax``.\n\nParameters\n----------\nx : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\n\nReturns\n-------\nk : int\n"
    ...

def isamax(x, n=..., offx=..., incx=...) -> typing.Any:
    "k = isamax(x,[n,offx,incx])\n\nWrapper for ``isamax``.\n\nParameters\n----------\nx : input rank-1 array('f') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\n\nReturns\n-------\nk : int\n"
    ...

def izamax(x, n=..., offx=..., incx=...) -> typing.Any:
    "k = izamax(x,[n,offx,incx])\n\nWrapper for ``izamax``.\n\nParameters\n----------\nx : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\n\nReturns\n-------\nk : int\n"
    ...

def sasum(x, n=..., offx=..., incx=...) -> typing.Any:
    "s = sasum(x,[n,offx,incx])\n\nWrapper for ``sasum``.\n\nParameters\n----------\nx : input rank-1 array('f') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\n\nReturns\n-------\ns : float\n"
    ...

def saxpy(x, y, n=..., a=..., offx=..., incx=..., offy=..., incy=...) -> typing.Any:
    "z = saxpy(x,y,[n,a,offx,incx,offy,incy])\n\nWrapper for ``saxpy``.\n\nParameters\n----------\nx : input rank-1 array('f') with bounds (*)\ny : input rank-1 array('f') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\na : input float, optional\n    Default: 1.0\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\n\nReturns\n-------\nz : rank-1 array('f') with bounds (*) and y storage\n"
    ...

def scasum(x, n=..., offx=..., incx=...) -> typing.Any:
    "s = scasum(x,[n,offx,incx])\n\nWrapper for ``scasum``.\n\nParameters\n----------\nx : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\n\nReturns\n-------\ns : float\n"
    ...

def scnrm2(x, n=..., offx=..., incx=...) -> typing.Any:
    "n2 = scnrm2(x,[n,offx,incx])\n\nWrapper for ``scnrm2``.\n\nParameters\n----------\nx : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\n\nReturns\n-------\nn2 : float\n"
    ...

def scopy(x, y, n=..., offx=..., incx=..., offy=..., incy=...) -> typing.Any:
    "y = scopy(x,y,[n,offx,incx,offy,incy])\n\nWrapper for ``scopy``.\n\nParameters\n----------\nx : input rank-1 array('f') with bounds (*)\ny : input rank-1 array('f') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\n\nReturns\n-------\ny : rank-1 array('f') with bounds (*)\n"
    ...

def sdot(x, y, n=..., offx=..., incx=..., offy=..., incy=...) -> typing.Any:
    "xy = sdot(x,y,[n,offx,incx,offy,incy])\n\nWrapper for ``sdot``.\n\nParameters\n----------\nx : input rank-1 array('f') with bounds (*)\ny : input rank-1 array('f') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\n\nReturns\n-------\nxy : float\n"
    ...

def sgbmv(m, n, kl, ku, alpha, a, x, incx=..., offx=..., beta=..., y=..., incy=..., offy=..., trans=..., overwrite_y=...) -> typing.Any:
    "yout = sgbmv(m,n,kl,ku,alpha,a,x,[incx,offx,beta,y,incy,offy,trans,overwrite_y])\n\nWrapper for ``sgbmv``.\n\nParameters\n----------\nm : input int\nn : input int\nkl : input int\nku : input int\nalpha : input float\na : input rank-2 array('f') with bounds (lda,n)\nx : input rank-1 array('f') with bounds (*)\n\nOther Parameters\n----------------\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nbeta : input float, optional\n    Default: 0.0\ny : input rank-1 array('f') with bounds (ly)\noverwrite_y : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\n\nReturns\n-------\nyout : rank-1 array('f') with bounds (ly) and y storage\n"
    ...

def sgemm(alpha, a, b, beta=..., c=..., trans_a=..., trans_b=..., overwrite_c=...) -> typing.Any:
    "c = sgemm(alpha,a,b,[beta,c,trans_a,trans_b,overwrite_c])\n\nWrapper for ``sgemm``.\n\nParameters\n----------\nalpha : input float\na : input rank-2 array('f') with bounds (lda,ka)\nb : input rank-2 array('f') with bounds (ldb,kb)\n\nOther Parameters\n----------------\nbeta : input float, optional\n    Default: 0.0\nc : input rank-2 array('f') with bounds (m,n)\noverwrite_c : input int, optional\n    Default: 0\ntrans_a : input int, optional\n    Default: 0\ntrans_b : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('f') with bounds (m,n)\n"
    ...

def sgemv(alpha, a, x, beta=..., y=..., offx=..., incx=..., offy=..., incy=..., trans=..., overwrite_y=...) -> typing.Any:
    "y = sgemv(alpha,a,x,[beta,y,offx,incx,offy,incy,trans,overwrite_y])\n\nWrapper for ``sgemv``.\n\nParameters\n----------\nalpha : input float\na : input rank-2 array('f') with bounds (m,n)\nx : input rank-1 array('f') with bounds (*)\n\nOther Parameters\n----------------\nbeta : input float, optional\n    Default: 0.0\ny : input rank-1 array('f') with bounds (ly)\noverwrite_y : input int, optional\n    Default: 0\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\ntrans : input int, optional\n    Default: 0\n\nReturns\n-------\ny : rank-1 array('f') with bounds (ly)\n"
    ...

def sger(alpha, x, y, incx=..., incy=..., a=..., overwrite_x=..., overwrite_y=..., overwrite_a=...) -> typing.Any:
    "a = sger(alpha,x,y,[incx,incy,a,overwrite_x,overwrite_y,overwrite_a])\n\nWrapper for ``sger``.\n\nParameters\n----------\nalpha : input float\nx : input rank-1 array('f') with bounds (m)\ny : input rank-1 array('f') with bounds (n)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 1\nincx : input int, optional\n    Default: 1\noverwrite_y : input int, optional\n    Default: 1\nincy : input int, optional\n    Default: 1\na : input rank-2 array('f') with bounds (m,n), optional\n    Default: 0.0\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\na : rank-2 array('f') with bounds (m,n)\n"
    ...

def snrm2(x, n=..., offx=..., incx=...) -> typing.Any:
    "n2 = snrm2(x,[n,offx,incx])\n\nWrapper for ``snrm2``.\n\nParameters\n----------\nx : input rank-1 array('f') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\n\nReturns\n-------\nn2 : float\n"
    ...

def srot(x, y, c, s, n=..., offx=..., incx=..., offy=..., incy=..., overwrite_x=..., overwrite_y=...) -> typing.Any:
    "x,y = srot(x,y,c,s,[n,offx,incx,offy,incy,overwrite_x,overwrite_y])\n\nWrapper for ``srot``.\n\nParameters\n----------\nx : input rank-1 array('f') with bounds (*)\ny : input rank-1 array('f') with bounds (*)\nc : input float\ns : input float\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-1-offx)/abs(incx)+1\noverwrite_x : input int, optional\n    Default: 0\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noverwrite_y : input int, optional\n    Default: 0\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\n\nReturns\n-------\nx : rank-1 array('f') with bounds (*)\ny : rank-1 array('f') with bounds (*)\n"
    ...

def srotg(a, b) -> typing.Any:
    'c,s = srotg(a,b)\n\nWrapper for ``srotg``.\n\nParameters\n----------\na : input float\nb : input float\n\nReturns\n-------\nc : float\ns : float\n'
    ...

def srotm(x, y, param, n=..., offx=..., incx=..., offy=..., incy=..., overwrite_x=..., overwrite_y=...) -> typing.Any:
    "x,y = srotm(x,y,param,[n,offx,incx,offy,incy,overwrite_x,overwrite_y])\n\nWrapper for ``srotm``.\n\nParameters\n----------\nx : input rank-1 array('f') with bounds (*)\ny : input rank-1 array('f') with bounds (*)\nparam : input rank-1 array('f') with bounds (5)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noverwrite_x : input int, optional\n    Default: 0\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noverwrite_y : input int, optional\n    Default: 0\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\n\nReturns\n-------\nx : rank-1 array('f') with bounds (*)\ny : rank-1 array('f') with bounds (*)\n"
    ...

def srotmg(d1, d2, x1, y1) -> typing.Any:
    "param = srotmg(d1,d2,x1,y1)\n\nWrapper for ``srotmg``.\n\nParameters\n----------\nd1 : input float\nd2 : input float\nx1 : input float\ny1 : input float\n\nReturns\n-------\nparam : rank-1 array('f') with bounds (5)\n"
    ...

def ssbmv(k, alpha, a, x, incx=..., offx=..., beta=..., y=..., incy=..., offy=..., lower=..., overwrite_y=...) -> typing.Any:
    "yout = ssbmv(k,alpha,a,x,[incx,offx,beta,y,incy,offy,lower,overwrite_y])\n\nWrapper for ``ssbmv``.\n\nParameters\n----------\nk : input int\nalpha : input float\na : input rank-2 array('f') with bounds (lda,n)\nx : input rank-1 array('f') with bounds (*)\n\nOther Parameters\n----------------\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nbeta : input float, optional\n    Default: 0.0\ny : input rank-1 array('f') with bounds (ly)\noverwrite_y : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nyout : rank-1 array('f') with bounds (ly) and y storage\n"
    ...

def sscal(a, x, n=..., offx=..., incx=...) -> typing.Any:
    "x = sscal(a,x,[n,offx,incx])\n\nWrapper for ``sscal``.\n\nParameters\n----------\na : input float\nx : input rank-1 array('f') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\n\nReturns\n-------\nx : rank-1 array('f') with bounds (*)\n"
    ...

def sspmv(n, alpha, ap, x, incx=..., offx=..., beta=..., y=..., incy=..., offy=..., lower=..., overwrite_y=...) -> typing.Any:
    "yout = sspmv(n,alpha,ap,x,[incx,offx,beta,y,incy,offy,lower,overwrite_y])\n\nWrapper for ``sspmv``.\n\nParameters\n----------\nn : input int\nalpha : input float\nap : input rank-1 array('f') with bounds (*)\nx : input rank-1 array('f') with bounds (*)\n\nOther Parameters\n----------------\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nbeta : input float, optional\n    Default: 0.0\ny : input rank-1 array('f') with bounds (ly)\noverwrite_y : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nyout : rank-1 array('f') with bounds (ly) and y storage\n"
    ...

def sspr(n, alpha, x, ap, incx=..., offx=..., lower=..., overwrite_ap=...) -> typing.Any:
    "apu = sspr(n,alpha,x,ap,[incx,offx,lower,overwrite_ap])\n\nWrapper for ``sspr``.\n\nParameters\n----------\nn : input int\nalpha : input float\nx : input rank-1 array('f') with bounds (*)\nap : input rank-1 array('f') with bounds (*)\n\nOther Parameters\n----------------\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\noverwrite_ap : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\napu : rank-1 array('f') with bounds (*) and ap storage\n"
    ...

def sspr2(n, alpha, x, y, ap, incx=..., offx=..., incy=..., offy=..., lower=..., overwrite_ap=...) -> typing.Any:
    "apu = sspr2(n,alpha,x,y,ap,[incx,offx,incy,offy,lower,overwrite_ap])\n\nWrapper for ``sspr2``.\n\nParameters\n----------\nn : input int\nalpha : input float\nx : input rank-1 array('f') with bounds (*)\ny : input rank-1 array('f') with bounds (*)\nap : input rank-1 array('f') with bounds (*)\n\nOther Parameters\n----------------\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\noverwrite_ap : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\napu : rank-1 array('f') with bounds (*) and ap storage\n"
    ...

def sswap(x, y, n=..., offx=..., incx=..., offy=..., incy=...) -> typing.Any:
    "x,y = sswap(x,y,[n,offx,incx,offy,incy])\n\nWrapper for ``sswap``.\n\nParameters\n----------\nx : input rank-1 array('f') with bounds (*)\ny : input rank-1 array('f') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\n\nReturns\n-------\nx : rank-1 array('f') with bounds (*)\ny : rank-1 array('f') with bounds (*)\n"
    ...

def ssymm(alpha, a, b, beta=..., c=..., side=..., lower=..., overwrite_c=...) -> typing.Any:
    "c = ssymm(alpha,a,b,[beta,c,side,lower,overwrite_c])\n\nWrapper for ``ssymm``.\n\nParameters\n----------\nalpha : input float\na : input rank-2 array('f') with bounds (lda,ka)\nb : input rank-2 array('f') with bounds (ldb,kb)\n\nOther Parameters\n----------------\nbeta : input float, optional\n    Default: 0.0\nc : input rank-2 array('f') with bounds (m,n)\noverwrite_c : input int, optional\n    Default: 0\nside : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('f') with bounds (m,n)\n"
    ...

def ssymv(alpha, a, x, beta=..., y=..., offx=..., incx=..., offy=..., incy=..., lower=..., overwrite_y=...) -> typing.Any:
    "y = ssymv(alpha,a,x,[beta,y,offx,incx,offy,incy,lower,overwrite_y])\n\nWrapper for ``ssymv``.\n\nParameters\n----------\nalpha : input float\na : input rank-2 array('f') with bounds (n,n)\nx : input rank-1 array('f') with bounds (*)\n\nOther Parameters\n----------------\nbeta : input float, optional\n    Default: 0.0\ny : input rank-1 array('f') with bounds (ly)\noverwrite_y : input int, optional\n    Default: 0\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\ny : rank-1 array('f') with bounds (ly)\n"
    ...

def ssyr(alpha, x, lower=..., incx=..., offx=..., n=..., a=..., overwrite_a=...) -> typing.Any:
    "a = ssyr(alpha,x,[lower,incx,offx,n,a,overwrite_a])\n\nWrapper for ``ssyr``.\n\nParameters\n----------\nalpha : input float\nx : input rank-1 array('f') with bounds (*)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nn : input int, optional\n    Default: (len(x)-1-offx)/abs(incx)+1\na : input rank-2 array('f') with bounds (n,n)\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\na : rank-2 array('f') with bounds (n,n)\n"
    ...

def ssyr2(alpha, x, y, lower=..., incx=..., offx=..., incy=..., offy=..., n=..., a=..., overwrite_a=...) -> typing.Any:
    "a = ssyr2(alpha,x,y,[lower,incx,offx,incy,offy,n,a,overwrite_a])\n\nWrapper for ``ssyr2``.\n\nParameters\n----------\nalpha : input float\nx : input rank-1 array('f') with bounds (*)\ny : input rank-1 array('f') with bounds (*)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nn : input int, optional\n    Default: ((len(x)-1-offx)/abs(incx)+1 <=(len(y)-1-offy)/abs(incy)+1 ?(len(x)-1-offx)/abs(incx)+1 :(len(y)-1-offy)/abs(incy)+1)\na : input rank-2 array('f') with bounds (n,n)\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\na : rank-2 array('f') with bounds (n,n)\n"
    ...

def ssyr2k(alpha, a, b, beta=..., c=..., trans=..., lower=..., overwrite_c=...) -> typing.Any:
    "c = ssyr2k(alpha,a,b,[beta,c,trans,lower,overwrite_c])\n\nWrapper for ``ssyr2k``.\n\nParameters\n----------\nalpha : input float\na : input rank-2 array('f') with bounds (lda,ka)\nb : input rank-2 array('f') with bounds (ldb,kb)\n\nOther Parameters\n----------------\nbeta : input float, optional\n    Default: 0.0\nc : input rank-2 array('f') with bounds (n,n)\noverwrite_c : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('f') with bounds (n,n)\n"
    ...

def ssyrk(alpha, a, beta=..., c=..., trans=..., lower=..., overwrite_c=...) -> typing.Any:
    "c = ssyrk(alpha,a,[beta,c,trans,lower,overwrite_c])\n\nWrapper for ``ssyrk``.\n\nParameters\n----------\nalpha : input float\na : input rank-2 array('f') with bounds (lda,ka)\n\nOther Parameters\n----------------\nbeta : input float, optional\n    Default: 0.0\nc : input rank-2 array('f') with bounds (n,n)\noverwrite_c : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('f') with bounds (n,n)\n"
    ...

def stbmv(k, a, x, incx=..., offx=..., lower=..., trans=..., diag=..., overwrite_x=...) -> typing.Any:
    "xout = stbmv(k,a,x,[incx,offx,lower,trans,diag,overwrite_x])\n\nWrapper for ``stbmv``.\n\nParameters\n----------\nk : input int\na : input rank-2 array('f') with bounds (lda,n)\nx : input rank-1 array('f') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nxout : rank-1 array('f') with bounds (*) and x storage\n"
    ...

def stbsv(k, a, x, incx=..., offx=..., lower=..., trans=..., diag=..., overwrite_x=...) -> typing.Any:
    "xout = stbsv(k,a,x,[incx,offx,lower,trans,diag,overwrite_x])\n\nWrapper for ``stbsv``.\n\nParameters\n----------\nk : input int\na : input rank-2 array('f') with bounds (lda,n)\nx : input rank-1 array('f') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nxout : rank-1 array('f') with bounds (*) and x storage\n"
    ...

def stpmv(n, ap, x, incx=..., offx=..., lower=..., trans=..., diag=..., overwrite_x=...) -> typing.Any:
    "xout = stpmv(n,ap,x,[incx,offx,lower,trans,diag,overwrite_x])\n\nWrapper for ``stpmv``.\n\nParameters\n----------\nn : input int\nap : input rank-1 array('f') with bounds (*)\nx : input rank-1 array('f') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nxout : rank-1 array('f') with bounds (*) and x storage\n"
    ...

def stpsv(n, ap, x, incx=..., offx=..., lower=..., trans=..., diag=..., overwrite_x=...) -> typing.Any:
    "xout = stpsv(n,ap,x,[incx,offx,lower,trans,diag,overwrite_x])\n\nWrapper for ``stpsv``.\n\nParameters\n----------\nn : input int\nap : input rank-1 array('f') with bounds (*)\nx : input rank-1 array('f') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nxout : rank-1 array('f') with bounds (*) and x storage\n"
    ...

def strmm(alpha, a, b, side=..., lower=..., trans_a=..., diag=..., overwrite_b=...) -> typing.Any:
    "b = strmm(alpha,a,b,[side,lower,trans_a,diag,overwrite_b])\n\nWrapper for ``strmm``.\n\nParameters\n----------\nalpha : input float\na : input rank-2 array('f') with bounds (lda,k)\nb : input rank-2 array('f') with bounds (ldb,n)\n\nOther Parameters\n----------------\noverwrite_b : input int, optional\n    Default: 0\nside : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\ntrans_a : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nb : rank-2 array('f') with bounds (ldb,n)\n"
    ...

def strmv(a, x, offx=..., incx=..., lower=..., trans=..., diag=..., overwrite_x=...) -> typing.Any:
    "x = strmv(a,x,[offx,incx,lower,trans,diag,overwrite_x])\n\nWrapper for ``strmv``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (n,n)\nx : input rank-1 array('f') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\nlower : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-1 array('f') with bounds (*)\n"
    ...

def strsm(alpha, a, b, side=..., lower=..., trans_a=..., diag=..., overwrite_b=...) -> typing.Any:
    "x = strsm(alpha,a,b,[side,lower,trans_a,diag,overwrite_b])\n\nWrapper for ``strsm``.\n\nParameters\n----------\nalpha : input float\na : input rank-2 array('f') with bounds (lda,*)\nb : input rank-2 array('f') with bounds (ldb,n)\n\nOther Parameters\n----------------\noverwrite_b : input int, optional\n    Default: 0\nside : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\ntrans_a : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('f') with bounds (ldb,n) and b storage\n"
    ...

def strsv(a, x, incx=..., offx=..., lower=..., trans=..., diag=..., overwrite_x=...) -> typing.Any:
    "xout = strsv(a,x,[incx,offx,lower,trans,diag,overwrite_x])\n\nWrapper for ``strsv``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (n,n)\nx : input rank-1 array('f') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nxout : rank-1 array('f') with bounds (*) and x storage\n"
    ...

def zaxpy(x, y, n=..., a=..., offx=..., incx=..., offy=..., incy=...) -> typing.Any:
    "z = zaxpy(x,y,[n,a,offx,incx,offy,incy])\n\nWrapper for ``zaxpy``.\n\nParameters\n----------\nx : input rank-1 array('D') with bounds (*)\ny : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\na : input complex, optional\n    Default: (1.0, 0.0)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\n\nReturns\n-------\nz : rank-1 array('D') with bounds (*) and y storage\n"
    ...

def zcopy(x, y, n=..., offx=..., incx=..., offy=..., incy=...) -> typing.Any:
    "y = zcopy(x,y,[n,offx,incx,offy,incy])\n\nWrapper for ``zcopy``.\n\nParameters\n----------\nx : input rank-1 array('D') with bounds (*)\ny : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\n\nReturns\n-------\ny : rank-1 array('D') with bounds (*)\n"
    ...

def zdotc(x, y, n=..., offx=..., incx=..., offy=..., incy=...) -> typing.Any:
    "xy = zdotc(x,y,[n,offx,incx,offy,incy])\n\nWrapper for ``zdotc``.\n\nParameters\n----------\nx : input rank-1 array('D') with bounds (*)\ny : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\n\nReturns\n-------\nxy : complex\n"
    ...

def zdotu(x, y, n=..., offx=..., incx=..., offy=..., incy=...) -> typing.Any:
    "xy = zdotu(x,y,[n,offx,incx,offy,incy])\n\nWrapper for ``zdotu``.\n\nParameters\n----------\nx : input rank-1 array('D') with bounds (*)\ny : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\n\nReturns\n-------\nxy : complex\n"
    ...

def zdrot(x, y, c, s, n=..., offx=..., incx=..., offy=..., incy=..., overwrite_x=..., overwrite_y=...) -> typing.Any:
    "x,y = zdrot(x,y,c,s,[n,offx,incx,offy,incy,overwrite_x,overwrite_y])\n\nWrapper for ``zdrot``.\n\nParameters\n----------\nx : input rank-1 array('D') with bounds (*)\ny : input rank-1 array('D') with bounds (*)\nc : input float\ns : input float\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-1-offx)/abs(incx)+1\noverwrite_x : input int, optional\n    Default: 0\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noverwrite_y : input int, optional\n    Default: 0\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\n\nReturns\n-------\nx : rank-1 array('D') with bounds (*)\ny : rank-1 array('D') with bounds (*)\n"
    ...

def zdscal(a, x, n=..., offx=..., incx=..., overwrite_x=...) -> typing.Any:
    "x = zdscal(a,x,[n,offx,incx,overwrite_x])\n\nWrapper for ``zdscal``.\n\nParameters\n----------\na : input float\nx : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noverwrite_x : input int, optional\n    Default: 0\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\n\nReturns\n-------\nx : rank-1 array('D') with bounds (*)\n"
    ...

def zgbmv(m, n, kl, ku, alpha, a, x, incx=..., offx=..., beta=..., y=..., incy=..., offy=..., trans=..., overwrite_y=...) -> typing.Any:
    "yout = zgbmv(m,n,kl,ku,alpha,a,x,[incx,offx,beta,y,incy,offy,trans,overwrite_y])\n\nWrapper for ``zgbmv``.\n\nParameters\n----------\nm : input int\nn : input int\nkl : input int\nku : input int\nalpha : input complex\na : input rank-2 array('D') with bounds (lda,n)\nx : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nbeta : input complex, optional\n    Default: (0.0, 0.0)\ny : input rank-1 array('D') with bounds (ly)\noverwrite_y : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\n\nReturns\n-------\nyout : rank-1 array('D') with bounds (ly) and y storage\n"
    ...

def zgemm(alpha, a, b, beta=..., c=..., trans_a=..., trans_b=..., overwrite_c=...) -> typing.Any:
    "c = zgemm(alpha,a,b,[beta,c,trans_a,trans_b,overwrite_c])\n\nWrapper for ``zgemm``.\n\nParameters\n----------\nalpha : input complex\na : input rank-2 array('D') with bounds (lda,ka)\nb : input rank-2 array('D') with bounds (ldb,kb)\n\nOther Parameters\n----------------\nbeta : input complex, optional\n    Default: (0.0, 0.0)\nc : input rank-2 array('D') with bounds (m,n)\noverwrite_c : input int, optional\n    Default: 0\ntrans_a : input int, optional\n    Default: 0\ntrans_b : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('D') with bounds (m,n)\n"
    ...

def zgemv(alpha, a, x, beta=..., y=..., offx=..., incx=..., offy=..., incy=..., trans=..., overwrite_y=...) -> typing.Any:
    "y = zgemv(alpha,a,x,[beta,y,offx,incx,offy,incy,trans,overwrite_y])\n\nWrapper for ``zgemv``.\n\nParameters\n----------\nalpha : input complex\na : input rank-2 array('D') with bounds (m,n)\nx : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\nbeta : input complex, optional\n    Default: (0.0, 0.0)\ny : input rank-1 array('D') with bounds (ly)\noverwrite_y : input int, optional\n    Default: 0\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\ntrans : input int, optional\n    Default: 0\n\nReturns\n-------\ny : rank-1 array('D') with bounds (ly)\n"
    ...

def zgerc(alpha, x, y, incx=..., incy=..., a=..., overwrite_x=..., overwrite_y=..., overwrite_a=...) -> typing.Any:
    "a = zgerc(alpha,x,y,[incx,incy,a,overwrite_x,overwrite_y,overwrite_a])\n\nWrapper for ``zgerc``.\n\nParameters\n----------\nalpha : input complex\nx : input rank-1 array('D') with bounds (m)\ny : input rank-1 array('D') with bounds (n)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 1\nincx : input int, optional\n    Default: 1\noverwrite_y : input int, optional\n    Default: 1\nincy : input int, optional\n    Default: 1\na : input rank-2 array('D') with bounds (m,n), optional\n    Default: (0.0,0.0)\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\na : rank-2 array('D') with bounds (m,n)\n"
    ...

def zgeru(alpha, x, y, incx=..., incy=..., a=..., overwrite_x=..., overwrite_y=..., overwrite_a=...) -> typing.Any:
    "a = zgeru(alpha,x,y,[incx,incy,a,overwrite_x,overwrite_y,overwrite_a])\n\nWrapper for ``zgeru``.\n\nParameters\n----------\nalpha : input complex\nx : input rank-1 array('D') with bounds (m)\ny : input rank-1 array('D') with bounds (n)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 1\nincx : input int, optional\n    Default: 1\noverwrite_y : input int, optional\n    Default: 1\nincy : input int, optional\n    Default: 1\na : input rank-2 array('D') with bounds (m,n), optional\n    Default: (0.0,0.0)\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\na : rank-2 array('D') with bounds (m,n)\n"
    ...

def zhbmv(k, alpha, a, x, incx=..., offx=..., beta=..., y=..., incy=..., offy=..., lower=..., overwrite_y=...) -> typing.Any:
    "yout = zhbmv(k,alpha,a,x,[incx,offx,beta,y,incy,offy,lower,overwrite_y])\n\nWrapper for ``zhbmv``.\n\nParameters\n----------\nk : input int\nalpha : input complex\na : input rank-2 array('D') with bounds (lda,n)\nx : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nbeta : input complex, optional\n    Default: (0.0, 0.0)\ny : input rank-1 array('D') with bounds (ly)\noverwrite_y : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nyout : rank-1 array('D') with bounds (ly) and y storage\n"
    ...

def zhemm(alpha, a, b, beta=..., c=..., side=..., lower=..., overwrite_c=...) -> typing.Any:
    "c = zhemm(alpha,a,b,[beta,c,side,lower,overwrite_c])\n\nWrapper for ``zhemm``.\n\nParameters\n----------\nalpha : input complex\na : input rank-2 array('D') with bounds (lda,ka)\nb : input rank-2 array('D') with bounds (ldb,kb)\n\nOther Parameters\n----------------\nbeta : input complex, optional\n    Default: (0.0, 0.0)\nc : input rank-2 array('D') with bounds (m,n)\noverwrite_c : input int, optional\n    Default: 0\nside : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('D') with bounds (m,n)\n"
    ...

def zhemv(alpha, a, x, beta=..., y=..., offx=..., incx=..., offy=..., incy=..., lower=..., overwrite_y=...) -> typing.Any:
    "y = zhemv(alpha,a,x,[beta,y,offx,incx,offy,incy,lower,overwrite_y])\n\nWrapper for ``zhemv``.\n\nParameters\n----------\nalpha : input complex\na : input rank-2 array('D') with bounds (n,n)\nx : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\nbeta : input complex, optional\n    Default: (0.0, 0.0)\ny : input rank-1 array('D') with bounds (ly)\noverwrite_y : input int, optional\n    Default: 0\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\ny : rank-1 array('D') with bounds (ly)\n"
    ...

def zher(alpha, x, lower=..., incx=..., offx=..., n=..., a=..., overwrite_a=...) -> typing.Any:
    "a = zher(alpha,x,[lower,incx,offx,n,a,overwrite_a])\n\nWrapper for ``zher``.\n\nParameters\n----------\nalpha : input complex\nx : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nn : input int, optional\n    Default: (len(x)-1-offx)/abs(incx)+1\na : input rank-2 array('D') with bounds (n,n)\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\na : rank-2 array('D') with bounds (n,n)\n"
    ...

def zher2(alpha, x, y, lower=..., incx=..., offx=..., incy=..., offy=..., n=..., a=..., overwrite_a=...) -> typing.Any:
    "a = zher2(alpha,x,y,[lower,incx,offx,incy,offy,n,a,overwrite_a])\n\nWrapper for ``zher2``.\n\nParameters\n----------\nalpha : input complex\nx : input rank-1 array('D') with bounds (*)\ny : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nn : input int, optional\n    Default: ((len(x)-1-offx)/abs(incx)+1 <=(len(y)-1-offy)/abs(incy)+1 ?(len(x)-1-offx)/abs(incx)+1 :(len(y)-1-offy)/abs(incy)+1)\na : input rank-2 array('D') with bounds (n,n)\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\na : rank-2 array('D') with bounds (n,n)\n"
    ...

def zher2k(alpha, a, b, beta=..., c=..., trans=..., lower=..., overwrite_c=...) -> typing.Any:
    "c = zher2k(alpha,a,b,[beta,c,trans,lower,overwrite_c])\n\nWrapper for ``zher2k``.\n\nParameters\n----------\nalpha : input complex\na : input rank-2 array('D') with bounds (lda,ka)\nb : input rank-2 array('D') with bounds (ldb,kb)\n\nOther Parameters\n----------------\nbeta : input complex, optional\n    Default: (0.0, 0.0)\nc : input rank-2 array('D') with bounds (n,n)\noverwrite_c : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('D') with bounds (n,n)\n"
    ...

def zherk(alpha, a, beta=..., c=..., trans=..., lower=..., overwrite_c=...) -> typing.Any:
    "c = zherk(alpha,a,[beta,c,trans,lower,overwrite_c])\n\nWrapper for ``zherk``.\n\nParameters\n----------\nalpha : input complex\na : input rank-2 array('D') with bounds (lda,ka)\n\nOther Parameters\n----------------\nbeta : input complex, optional\n    Default: (0.0, 0.0)\nc : input rank-2 array('D') with bounds (n,n)\noverwrite_c : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('D') with bounds (n,n)\n"
    ...

def zhpmv(n, alpha, ap, x, incx=..., offx=..., beta=..., y=..., incy=..., offy=..., lower=..., overwrite_y=...) -> typing.Any:
    "yout = zhpmv(n,alpha,ap,x,[incx,offx,beta,y,incy,offy,lower,overwrite_y])\n\nWrapper for ``zhpmv``.\n\nParameters\n----------\nn : input int\nalpha : input complex\nap : input rank-1 array('D') with bounds (*)\nx : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nbeta : input complex, optional\n    Default: (0.0, 0.0)\ny : input rank-1 array('D') with bounds (ly)\noverwrite_y : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nyout : rank-1 array('D') with bounds (ly) and y storage\n"
    ...

def zhpr(n, alpha, x, ap, incx=..., offx=..., lower=..., overwrite_ap=...) -> typing.Any:
    "apu = zhpr(n,alpha,x,ap,[incx,offx,lower,overwrite_ap])\n\nWrapper for ``zhpr``.\n\nParameters\n----------\nn : input int\nalpha : input float\nx : input rank-1 array('D') with bounds (*)\nap : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\noverwrite_ap : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\napu : rank-1 array('D') with bounds (*) and ap storage\n"
    ...

def zhpr2(n, alpha, x, y, ap, incx=..., offx=..., incy=..., offy=..., lower=..., overwrite_ap=...) -> typing.Any:
    "apu = zhpr2(n,alpha,x,y,ap,[incx,offx,incy,offy,lower,overwrite_ap])\n\nWrapper for ``zhpr2``.\n\nParameters\n----------\nn : input int\nalpha : input complex\nx : input rank-1 array('D') with bounds (*)\ny : input rank-1 array('D') with bounds (*)\nap : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\noverwrite_ap : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\napu : rank-1 array('D') with bounds (*) and ap storage\n"
    ...

def zrotg(a, b) -> typing.Any:
    'c,s = zrotg(a,b)\n\nWrapper for ``zrotg``.\n\nParameters\n----------\na : input complex\nb : input complex\n\nReturns\n-------\nc : complex\ns : complex\n'
    ...

def zscal(a, x, n=..., offx=..., incx=...) -> typing.Any:
    "x = zscal(a,x,[n,offx,incx])\n\nWrapper for ``zscal``.\n\nParameters\n----------\na : input complex\nx : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\n\nReturns\n-------\nx : rank-1 array('D') with bounds (*)\n"
    ...

def zspmv(n, alpha, ap, x, incx=..., offx=..., beta=..., y=..., incy=..., offy=..., lower=..., overwrite_y=...) -> typing.Any:
    "yout = zspmv(n,alpha,ap,x,[incx,offx,beta,y,incy,offy,lower,overwrite_y])\n\nWrapper for ``zspmv``.\n\nParameters\n----------\nn : input int\nalpha : input complex\nap : input rank-1 array('D') with bounds (*)\nx : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nbeta : input complex, optional\n    Default: (0.0, 0.0)\ny : input rank-1 array('D') with bounds (ly)\noverwrite_y : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nyout : rank-1 array('D') with bounds (ly) and y storage\n"
    ...

def zspr(n, alpha, x, ap, incx=..., offx=..., lower=..., overwrite_ap=...) -> typing.Any:
    "apu = zspr(n,alpha,x,ap,[incx,offx,lower,overwrite_ap])\n\nWrapper for ``zspr``.\n\nParameters\n----------\nn : input int\nalpha : input complex\nx : input rank-1 array('D') with bounds (*)\nap : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\noverwrite_ap : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\napu : rank-1 array('D') with bounds (*) and ap storage\n"
    ...

def zswap(x, y, n=..., offx=..., incx=..., offy=..., incy=...) -> typing.Any:
    "x,y = zswap(x,y,[n,offx,incx,offy,incy])\n\nWrapper for ``zswap``.\n\nParameters\n----------\nx : input rank-1 array('D') with bounds (*)\ny : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\n\nReturns\n-------\nx : rank-1 array('D') with bounds (*)\ny : rank-1 array('D') with bounds (*)\n"
    ...

def zsymm(alpha, a, b, beta=..., c=..., side=..., lower=..., overwrite_c=...) -> typing.Any:
    "c = zsymm(alpha,a,b,[beta,c,side,lower,overwrite_c])\n\nWrapper for ``zsymm``.\n\nParameters\n----------\nalpha : input complex\na : input rank-2 array('D') with bounds (lda,ka)\nb : input rank-2 array('D') with bounds (ldb,kb)\n\nOther Parameters\n----------------\nbeta : input complex, optional\n    Default: (0.0, 0.0)\nc : input rank-2 array('D') with bounds (m,n)\noverwrite_c : input int, optional\n    Default: 0\nside : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('D') with bounds (m,n)\n"
    ...

def zsyr(alpha, x, lower=..., incx=..., offx=..., n=..., a=..., overwrite_a=...) -> typing.Any:
    "a = zsyr(alpha,x,[lower,incx,offx,n,a,overwrite_a])\n\nWrapper for ``zsyr``.\n\nParameters\n----------\nalpha : input complex\nx : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nn : input int, optional\n    Default: (len(x)-1-offx)/abs(incx)+1\na : input rank-2 array('D') with bounds (n,n)\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\na : rank-2 array('D') with bounds (n,n)\n"
    ...

def zsyr2k(alpha, a, b, beta=..., c=..., trans=..., lower=..., overwrite_c=...) -> typing.Any:
    "c = zsyr2k(alpha,a,b,[beta,c,trans,lower,overwrite_c])\n\nWrapper for ``zsyr2k``.\n\nParameters\n----------\nalpha : input complex\na : input rank-2 array('D') with bounds (lda,ka)\nb : input rank-2 array('D') with bounds (ldb,kb)\n\nOther Parameters\n----------------\nbeta : input complex, optional\n    Default: (0.0, 0.0)\nc : input rank-2 array('D') with bounds (n,n)\noverwrite_c : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('D') with bounds (n,n)\n"
    ...

def zsyrk(alpha, a, beta=..., c=..., trans=..., lower=..., overwrite_c=...) -> typing.Any:
    "c = zsyrk(alpha,a,[beta,c,trans,lower,overwrite_c])\n\nWrapper for ``zsyrk``.\n\nParameters\n----------\nalpha : input complex\na : input rank-2 array('D') with bounds (lda,ka)\n\nOther Parameters\n----------------\nbeta : input complex, optional\n    Default: (0.0, 0.0)\nc : input rank-2 array('D') with bounds (n,n)\noverwrite_c : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('D') with bounds (n,n)\n"
    ...

def ztbmv(k, a, x, incx=..., offx=..., lower=..., trans=..., diag=..., overwrite_x=...) -> typing.Any:
    "xout = ztbmv(k,a,x,[incx,offx,lower,trans,diag,overwrite_x])\n\nWrapper for ``ztbmv``.\n\nParameters\n----------\nk : input int\na : input rank-2 array('D') with bounds (lda,n)\nx : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nxout : rank-1 array('D') with bounds (*) and x storage\n"
    ...

def ztbsv(k, a, x, incx=..., offx=..., lower=..., trans=..., diag=..., overwrite_x=...) -> typing.Any:
    "xout = ztbsv(k,a,x,[incx,offx,lower,trans,diag,overwrite_x])\n\nWrapper for ``ztbsv``.\n\nParameters\n----------\nk : input int\na : input rank-2 array('D') with bounds (lda,n)\nx : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nxout : rank-1 array('D') with bounds (*) and x storage\n"
    ...

def ztpmv(n, ap, x, incx=..., offx=..., lower=..., trans=..., diag=..., overwrite_x=...) -> typing.Any:
    "xout = ztpmv(n,ap,x,[incx,offx,lower,trans,diag,overwrite_x])\n\nWrapper for ``ztpmv``.\n\nParameters\n----------\nn : input int\nap : input rank-1 array('D') with bounds (*)\nx : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nxout : rank-1 array('D') with bounds (*) and x storage\n"
    ...

def ztpsv(n, ap, x, incx=..., offx=..., lower=..., trans=..., diag=..., overwrite_x=...) -> typing.Any:
    "xout = ztpsv(n,ap,x,[incx,offx,lower,trans,diag,overwrite_x])\n\nWrapper for ``ztpsv``.\n\nParameters\n----------\nn : input int\nap : input rank-1 array('D') with bounds (*)\nx : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nxout : rank-1 array('D') with bounds (*) and x storage\n"
    ...

def ztrmm(alpha, a, b, side=..., lower=..., trans_a=..., diag=..., overwrite_b=...) -> typing.Any:
    "b = ztrmm(alpha,a,b,[side,lower,trans_a,diag,overwrite_b])\n\nWrapper for ``ztrmm``.\n\nParameters\n----------\nalpha : input complex\na : input rank-2 array('D') with bounds (lda,k)\nb : input rank-2 array('D') with bounds (ldb,n)\n\nOther Parameters\n----------------\noverwrite_b : input int, optional\n    Default: 0\nside : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\ntrans_a : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nb : rank-2 array('D') with bounds (ldb,n)\n"
    ...

def ztrmv(a, x, offx=..., incx=..., lower=..., trans=..., diag=..., overwrite_x=...) -> typing.Any:
    "x = ztrmv(a,x,[offx,incx,lower,trans,diag,overwrite_x])\n\nWrapper for ``ztrmv``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (n,n)\nx : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\nlower : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-1 array('D') with bounds (*)\n"
    ...

def ztrsm(alpha, a, b, side=..., lower=..., trans_a=..., diag=..., overwrite_b=...) -> typing.Any:
    "x = ztrsm(alpha,a,b,[side,lower,trans_a,diag,overwrite_b])\n\nWrapper for ``ztrsm``.\n\nParameters\n----------\nalpha : input complex\na : input rank-2 array('D') with bounds (lda,*)\nb : input rank-2 array('D') with bounds (ldb,n)\n\nOther Parameters\n----------------\noverwrite_b : input int, optional\n    Default: 0\nside : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\ntrans_a : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('D') with bounds (ldb,n) and b storage\n"
    ...

def ztrsv(a, x, incx=..., offx=..., lower=..., trans=..., diag=..., overwrite_x=...) -> typing.Any:
    "xout = ztrsv(a,x,[incx,offx,lower,trans,diag,overwrite_x])\n\nWrapper for ``ztrsv``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (n,n)\nx : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nxout : rank-1 array('D') with bounds (*) and x storage\n"
    ...

def __getattr__(name) -> typing.Any:
    ...

