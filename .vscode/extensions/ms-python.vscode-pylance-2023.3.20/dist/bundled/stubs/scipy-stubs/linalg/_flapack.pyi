# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: scipy, version: 1.6.2
# Module: scipy.linalg._flapack, version: $Revision: $
import typing
import builtins as _mod_builtins

__doc__: str
__file__: str
__name__: str
__package__: str
__version__: bytes
def cgbsv(kl, ku, ab, b, overwrite_ab=..., overwrite_b=...) -> typing.Any:
    "lub,piv,x,info = cgbsv(kl,ku,ab,b,[overwrite_ab,overwrite_b])\n\nWrapper for ``cgbsv``.\n\nParameters\n----------\nkl : input int\nku : input int\nab : input rank-2 array('F') with bounds (2*kl+ku+1,n)\nb : input rank-2 array('F') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_ab : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nlub : rank-2 array('F') with bounds (2*kl+ku+1,n) and ab storage\npiv : rank-1 array('i') with bounds (n)\nx : rank-2 array('F') with bounds (n,nrhs) and b storage\ninfo : int\n"
    ...

def cgbtrf(ab, kl, ku, m=..., n=..., ldab=..., overwrite_ab=...) -> typing.Any:
    "lu,ipiv,info = cgbtrf(ab,kl,ku,[m,n,ldab,overwrite_ab])\n\nWrapper for ``cgbtrf``.\n\nParameters\n----------\nab : input rank-2 array('F') with bounds (ldab,n)\nkl : input int\nku : input int\n\nOther Parameters\n----------------\nm : input int, optional\n    Default: shape(ab,1)\nn : input int, optional\n    Default: shape(ab,1)\noverwrite_ab : input int, optional\n    Default: 0\nldab : input int, optional\n    Default: max(shape(ab,0),1)\n\nReturns\n-------\nlu : rank-2 array('F') with bounds (ldab,n) and ab storage\nipiv : rank-1 array('i') with bounds (MIN(m,n))\ninfo : int\n"
    ...

def cgbtrs(ab, kl, ku, b, ipiv, trans=..., n=..., ldab=..., ldb=..., overwrite_b=...) -> typing.Any:
    "x,info = cgbtrs(ab,kl,ku,b,ipiv,[trans,n,ldab,ldb,overwrite_b])\n\nWrapper for ``cgbtrs``.\n\nParameters\n----------\nab : input rank-2 array('F') with bounds (ldab,n)\nkl : input int\nku : input int\nb : input rank-2 array('F') with bounds (ldb,nrhs)\nipiv : input rank-1 array('i') with bounds (n)\n\nOther Parameters\n----------------\noverwrite_b : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\nn : input int, optional\n    Default: shape(ab,1)\nldab : input int, optional\n    Default: shape(ab,0)\nldb : input int, optional\n    Default: shape(b,0)\n\nReturns\n-------\nx : rank-2 array('F') with bounds (ldb,nrhs) and b storage\ninfo : int\n"
    ...

def cgebal(a, scale=..., permute=..., overwrite_a=...) -> typing.Any:
    "ba,lo,hi,pivscale,info = cgebal(a,[scale,permute,overwrite_a])\n\nWrapper for ``cgebal``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (m,n)\n\nOther Parameters\n----------------\nscale : input int, optional\n    Default: 0\npermute : input int, optional\n    Default: 0\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\nba : rank-2 array('F') with bounds (m,n) and a storage\nlo : int\nhi : int\npivscale : rank-1 array('f') with bounds (n)\ninfo : int\n"
    ...

def cgecon(a, anorm, norm=...) -> typing.Any:
    "rcond,info = cgecon(a,anorm,[norm])\n\nWrapper for ``cgecon``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (n,n)\nanorm : input float\n\nOther Parameters\n----------------\nnorm : input string(len=1), optional\n    Default: '1'\n\nReturns\n-------\nrcond : float\ninfo : int\n"
    ...

def cgeequ(a) -> typing.Any:
    "r,c,rowcnd,colcnd,amax,info = cgeequ(a)\n\nWrapper for ``cgeequ``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (m,n)\n\nReturns\n-------\nr : rank-1 array('f') with bounds (m)\nc : rank-1 array('f') with bounds (n)\nrowcnd : float\ncolcnd : float\namax : float\ninfo : int\n"
    ...

def cgeequb(a) -> typing.Any:
    "r,c,rowcnd,colcnd,amax,info = cgeequb(a)\n\nWrapper for ``cgeequb``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (m,n)\n\nReturns\n-------\nr : rank-1 array('f') with bounds (m)\nc : rank-1 array('f') with bounds (n)\nrowcnd : float\ncolcnd : float\namax : float\ninfo : int\n"
    ...

def cgees(cselect, a, compute_v=..., sort_t=..., lwork=..., cselect_extra_args=..., overwrite_a=...) -> typing.Any:
    "t,sdim,w,vs,work,info = cgees(cselect,a,[compute_v,sort_t,lwork,cselect_extra_args,overwrite_a])\n\nWrapper for ``cgees``.\n\nParameters\n----------\ncselect : call-back function\na : input rank-2 array('F') with bounds (n,n)\n\nOther Parameters\n----------------\ncompute_v : input int, optional\n    Default: 1\nsort_t : input int, optional\n    Default: 0\ncselect_extra_args : input tuple, optional\n    Default: ()\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(3*n,1)\n\nReturns\n-------\nt : rank-2 array('F') with bounds (n,n) and a storage\nsdim : int\nw : rank-1 array('F') with bounds (n)\nvs : rank-2 array('F') with bounds (ldvs,n)\nwork : rank-1 array('F') with bounds (MAX(lwork,1))\ninfo : int\n\nNotes\n-----\nCall-back functions::\n\n  def cselect(arg): return cselect\n  Required arguments:\n    arg : input complex\n  Return objects:\n    cselect : int\n"
    ...

def cgeev(a, compute_vl=..., compute_vr=..., lwork=..., overwrite_a=...) -> typing.Any:
    "w,vl,vr,info = cgeev(a,[compute_vl,compute_vr,lwork,overwrite_a])\n\nWrapper for ``cgeev``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (n,n)\n\nOther Parameters\n----------------\ncompute_vl : input int, optional\n    Default: 1\ncompute_vr : input int, optional\n    Default: 1\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(2*n,1)\n\nReturns\n-------\nw : rank-1 array('F') with bounds (n)\nvl : rank-2 array('F') with bounds (ldvl,n)\nvr : rank-2 array('F') with bounds (ldvr,n)\ninfo : int\n"
    ...

def cgeev_lwork(n, compute_vl=..., compute_vr=...) -> typing.Any:
    'work,info = cgeev_lwork(n,[compute_vl,compute_vr])\n\nWrapper for ``cgeev_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\ncompute_vl : input int, optional\n    Default: 1\ncompute_vr : input int, optional\n    Default: 1\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    ...

def cgegv(*args, **kwds) -> typing.Any:
    "`cgegv` is deprecated!\nThe `*gegv` family of routines has been deprecated in\nLAPACK 3.6.0 in favor of the `*ggev` family of routines.\nThe corresponding wrappers will be removed from SciPy in\na future release.\n\nalpha,beta,vl,vr,info = cgegv(a,b,[compute_vl,compute_vr,lwork,overwrite_a,overwrite_b])\n\nWrapper for ``cgegv``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (n,n)\nb : input rank-2 array('F') with bounds (n,n)\n\nOther Parameters\n----------------\ncompute_vl : input int, optional\n    Default: 1\ncompute_vr : input int, optional\n    Default: 1\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(2*n,1)\n\nReturns\n-------\nalpha : rank-1 array('F') with bounds (n)\nbeta : rank-1 array('F') with bounds (n)\nvl : rank-2 array('F') with bounds (ldvl,n)\nvr : rank-2 array('F') with bounds (ldvr,n)\ninfo : int\n"
    ...

def cgehrd(a, lo=..., hi=..., lwork=..., overwrite_a=...) -> typing.Any:
    "ht,tau,info = cgehrd(a,[lo,hi,lwork,overwrite_a])\n\nWrapper for ``cgehrd``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (n,n)\n\nOther Parameters\n----------------\nlo : input int, optional\n    Default: 0\nhi : input int, optional\n    Default: n-1\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: MAX(n,1)\n\nReturns\n-------\nht : rank-2 array('F') with bounds (n,n) and a storage\ntau : rank-1 array('F') with bounds (n - 1)\ninfo : int\n"
    ...

def cgehrd_lwork(n, lo=..., hi=...) -> typing.Any:
    'work,info = cgehrd_lwork(n,[lo,hi])\n\nWrapper for ``cgehrd_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlo : input int, optional\n    Default: 0\nhi : input int, optional\n    Default: n-1\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    ...

def cgels(a, b, trans=..., lwork=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "lqr,x,info = cgels(a,b,[trans,lwork,overwrite_a,overwrite_b])\n\nWrapper for ``cgels``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (m,n)\nb : input rank-2 array('F') with bounds (MAX(m,n),nrhs)\n\nOther Parameters\n----------------\ntrans : input string(len=1), optional\n    Default: 'N'\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: MAX(MIN(m,n)+MAX(MIN(m,n),nrhs),1)\n\nReturns\n-------\nlqr : rank-2 array('F') with bounds (m,n) and a storage\nx : rank-2 array('F') with bounds (MAX(m,n),nrhs) and b storage\ninfo : int\n"
    ...

def cgels_lwork(m, n, nrhs, trans=...) -> typing.Any:
    "work,info = cgels_lwork(m,n,nrhs,[trans])\n\nWrapper for ``cgels_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\nnrhs : input int\n\nOther Parameters\n----------------\ntrans : input string(len=1), optional\n    Default: 'N'\n\nReturns\n-------\nwork : complex\ninfo : int\n"
    ...

def cgelsd(a, b, lwork, size_rwork, size_iwork, cond=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "x,s,rank,info = cgelsd(a,b,lwork,size_rwork,size_iwork,[cond,overwrite_a,overwrite_b])\n\nWrapper for ``cgelsd``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (m,n)\nb : input rank-2 array('F') with bounds (maxmn,nrhs)\nlwork : input int\nsize_rwork : input int\nsize_iwork : input int\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\ncond : input float, optional\n    Default: -1.0\n\nReturns\n-------\nx : rank-2 array('F') with bounds (maxmn,nrhs) and b storage\ns : rank-1 array('f') with bounds (minmn)\nrank : int\ninfo : int\n"
    ...

def cgelsd_lwork(m, n, nrhs, cond=..., lwork=...) -> typing.Any:
    'work,rwork,iwork,info = cgelsd_lwork(m,n,nrhs,[cond,lwork])\n\nWrapper for ``cgelsd_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\nnrhs : input int\n\nOther Parameters\n----------------\ncond : input float, optional\n    Default: -1.0\nlwork : input int, optional\n    Default: -1\n\nReturns\n-------\nwork : complex\nrwork : float\niwork : int\ninfo : int\n'
    ...

def cgelss(a, b, cond=..., lwork=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "v,x,s,rank,work,info = cgelss(a,b,[cond,lwork,overwrite_a,overwrite_b])\n\nWrapper for ``cgelss``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (m,n)\nb : input rank-2 array('F') with bounds (maxmn,nrhs)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\ncond : input float, optional\n    Default: -1.0\nlwork : input int, optional\n    Default: max(2*minmn+MAX(maxmn,nrhs),1)\n\nReturns\n-------\nv : rank-2 array('F') with bounds (m,n) and a storage\nx : rank-2 array('F') with bounds (maxmn,nrhs) and b storage\ns : rank-1 array('f') with bounds (minmn)\nrank : int\nwork : rank-1 array('F') with bounds (MAX(lwork,1))\ninfo : int\n"
    ...

def cgelss_lwork(m, n, nrhs, cond=..., lwork=...) -> typing.Any:
    'work,info = cgelss_lwork(m,n,nrhs,[cond,lwork])\n\nWrapper for ``cgelss_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\nnrhs : input int\n\nOther Parameters\n----------------\ncond : input float, optional\n    Default: -1.0\nlwork : input int, optional\n    Default: -1\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    ...

def cgelsy(a, b, jptv, cond, lwork, overwrite_a=..., overwrite_b=...) -> typing.Any:
    "v,x,j,rank,info = cgelsy(a,b,jptv,cond,lwork,[overwrite_a,overwrite_b])\n\nWrapper for ``cgelsy``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (m,n)\nb : input rank-2 array('F') with bounds (maxmn,nrhs)\njptv : input rank-1 array('i') with bounds (n)\ncond : input float\nlwork : input int\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nv : rank-2 array('F') with bounds (m,n) and a storage\nx : rank-2 array('F') with bounds (maxmn,nrhs) and b storage\nj : rank-1 array('i') with bounds (n) and jptv storage\nrank : int\ninfo : int\n"
    ...

def cgelsy_lwork(m, n, nrhs, cond, lwork=...) -> typing.Any:
    'work,info = cgelsy_lwork(m,n,nrhs,cond,[lwork])\n\nWrapper for ``cgelsy_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\nnrhs : input int\ncond : input float\n\nOther Parameters\n----------------\nlwork : input int, optional\n    Default: -1\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    ...

def cgemqrt(v, t, c, side=..., trans=..., overwrite_c=...) -> typing.Any:
    "c,info = cgemqrt(v,t,c,[side,trans,overwrite_c])\n\nWrapper for ``cgemqrt``.\n\nParameters\n----------\nv : input rank-2 array('F') with bounds ((side[0]=='L'?m:n),k)\nt : input rank-2 array('F') with bounds (nb,k)\nc : input rank-2 array('F') with bounds (m,n)\n\nOther Parameters\n----------------\nside : input string(len=1), optional\n    Default: 'L'\ntrans : input string(len=1), optional\n    Default: 'N'\noverwrite_c : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('F') with bounds (m,n)\ninfo : int\n"
    ...

def cgeqp3(a, lwork=..., overwrite_a=...) -> typing.Any:
    "qr,jpvt,tau,work,info = cgeqp3(a,[lwork,overwrite_a])\n\nWrapper for ``cgeqp3``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(3*(n+1),1)\n\nReturns\n-------\nqr : rank-2 array('F') with bounds (m,n) and a storage\njpvt : rank-1 array('i') with bounds (n)\ntau : rank-1 array('F') with bounds (MIN(m,n))\nwork : rank-1 array('F') with bounds (MAX(lwork,1))\ninfo : int\n"
    ...

def cgeqrf(a, lwork=..., overwrite_a=...) -> typing.Any:
    "qr,tau,work,info = cgeqrf(a,[lwork,overwrite_a])\n\nWrapper for ``cgeqrf``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(3*n,1)\n\nReturns\n-------\nqr : rank-2 array('F') with bounds (m,n) and a storage\ntau : rank-1 array('F') with bounds (MIN(m,n))\nwork : rank-1 array('F') with bounds (MAX(lwork,1))\ninfo : int\n"
    ...

def cgeqrf_lwork(m, n) -> typing.Any:
    'work,info = cgeqrf_lwork(m,n)\n\nWrapper for ``cgeqrf_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    ...

def cgeqrfp(a, lwork=..., overwrite_a=...) -> typing.Any:
    "qr,tau,info = cgeqrfp(a,[lwork,overwrite_a])\n\nWrapper for ``cgeqrfp``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: MAX(1, n)\n\nReturns\n-------\nqr : rank-2 array('F') with bounds (m,n) and a storage\ntau : rank-1 array('F') with bounds (MIN(m,n))\ninfo : int\n"
    ...

def cgeqrfp_lwork(m, n) -> typing.Any:
    'work,info = cgeqrfp_lwork(m,n)\n\nWrapper for ``cgeqrfp_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    ...

def cgeqrt(nb, a, overwrite_a=...) -> typing.Any:
    "a,t,info = cgeqrt(nb,a,[overwrite_a])\n\nWrapper for ``cgeqrt``.\n\nParameters\n----------\nnb : input int\na : input rank-2 array('F') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\na : rank-2 array('F') with bounds (m,n)\nt : rank-2 array('F') with bounds (nb,MIN(m,n))\ninfo : int\n"
    ...

def cgerqf(a, lwork=..., overwrite_a=...) -> typing.Any:
    "qr,tau,work,info = cgerqf(a,[lwork,overwrite_a])\n\nWrapper for ``cgerqf``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(3*m,1)\n\nReturns\n-------\nqr : rank-2 array('F') with bounds (m,n) and a storage\ntau : rank-1 array('F') with bounds (MIN(m,n))\nwork : rank-1 array('F') with bounds (MAX(lwork,1))\ninfo : int\n"
    ...

def cgesc2(lu, rhs, ipiv, jpiv, overwrite_rhs=...) -> typing.Any:
    "x,scale = cgesc2(lu,rhs,ipiv,jpiv,[overwrite_rhs])\n\nWrapper for ``cgesc2``.\n\nParameters\n----------\nlu : input rank-2 array('F') with bounds (n,n)\nrhs : input rank-1 array('F') with bounds (n)\nipiv : input rank-1 array('i') with bounds (n)\njpiv : input rank-1 array('i') with bounds (n)\n\nOther Parameters\n----------------\noverwrite_rhs : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-1 array('F') with bounds (n) and rhs storage\nscale : float\n"
    ...

def cgesdd(a, compute_uv=..., full_matrices=..., lwork=..., overwrite_a=...) -> typing.Any:
    "u,s,vt,info = cgesdd(a,[compute_uv,full_matrices,lwork,overwrite_a])\n\nWrapper for ``cgesdd``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\ncompute_uv : input int, optional\n    Default: 1\nfull_matrices : input int, optional\n    Default: 1\nlwork : input int, optional\n    Default: max((compute_uv?2*minmn*minmn+MAX(m,n)+2*minmn:2*minmn+MAX(m,n)),1)\n\nReturns\n-------\nu : rank-2 array('F') with bounds (u0,u1)\ns : rank-1 array('f') with bounds (minmn)\nvt : rank-2 array('F') with bounds (vt0,vt1)\ninfo : int\n"
    ...

def cgesdd_lwork(m, n, compute_uv=..., full_matrices=...) -> typing.Any:
    'work,info = cgesdd_lwork(m,n,[compute_uv,full_matrices])\n\nWrapper for ``cgesdd_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\n\nOther Parameters\n----------------\ncompute_uv : input int, optional\n    Default: 1\nfull_matrices : input int, optional\n    Default: 1\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    ...

def cgesv(a, b, overwrite_a=..., overwrite_b=...) -> typing.Any:
    "lu,piv,x,info = cgesv(a,b,[overwrite_a,overwrite_b])\n\nWrapper for ``cgesv``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (n,n)\nb : input rank-2 array('F') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nlu : rank-2 array('F') with bounds (n,n) and a storage\npiv : rank-1 array('i') with bounds (n)\nx : rank-2 array('F') with bounds (n,nrhs) and b storage\ninfo : int\n"
    ...

def cgesvd(a, compute_uv=..., full_matrices=..., lwork=..., overwrite_a=...) -> typing.Any:
    "u,s,vt,info = cgesvd(a,[compute_uv,full_matrices,lwork,overwrite_a])\n\nWrapper for ``cgesvd``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\ncompute_uv : input int, optional\n    Default: 1\nfull_matrices : input int, optional\n    Default: 1\nlwork : input int, optional\n    Default: MAX(2*minmn+MAX(m,n),1)\n\nReturns\n-------\nu : rank-2 array('F') with bounds (u0,u1)\ns : rank-1 array('f') with bounds (minmn)\nvt : rank-2 array('F') with bounds (vt0,vt1)\ninfo : int\n"
    ...

def cgesvd_lwork(m, n, compute_uv=..., full_matrices=...) -> typing.Any:
    'work,info = cgesvd_lwork(m,n,[compute_uv,full_matrices])\n\nWrapper for ``cgesvd_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\n\nOther Parameters\n----------------\ncompute_uv : input int, optional\n    Default: 1\nfull_matrices : input int, optional\n    Default: 1\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    ...

def cgesvx(a, b, fact=..., trans=..., af=..., ipiv=..., equed=..., r=..., c=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "as,lu,ipiv,equed,rs,cs,bs,x,rcond,ferr,berr,info = cgesvx(a,b,[fact,trans,af,ipiv,equed,r,c,overwrite_a,overwrite_b])\n\nWrapper for ``cgesvx``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (n,n)\nb : input rank-2 array('F') with bounds (n,nrhs)\n\nOther Parameters\n----------------\nfact : input string(len=1), optional\n    Default: 'E'\ntrans : input string(len=1), optional\n    Default: 'N'\noverwrite_a : input int, optional\n    Default: 0\naf : input rank-2 array('F') with bounds (n,n)\nipiv : input rank-1 array('i') with bounds (n)\nequed : input string(len=1), optional\n    Default: 'B'\nr : input rank-1 array('f') with bounds (n)\nc : input rank-1 array('f') with bounds (n)\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nas : rank-2 array('F') with bounds (n,n) and a storage\nlu : rank-2 array('F') with bounds (n,n) and af storage\nipiv : rank-1 array('i') with bounds (n)\nequed : string(len=1)\nrs : rank-1 array('f') with bounds (n) and r storage\ncs : rank-1 array('f') with bounds (n) and c storage\nbs : rank-2 array('F') with bounds (n,nrhs) and b storage\nx : rank-2 array('F') with bounds (n,nrhs)\nrcond : float\nferr : rank-1 array('f') with bounds (nrhs)\nberr : rank-1 array('f') with bounds (nrhs)\ninfo : int\n"
    ...

def cgetc2(a, overwrite_a=...) -> typing.Any:
    "lu,ipiv,jpiv,info = cgetc2(a,[overwrite_a])\n\nWrapper for ``cgetc2``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\nlu : rank-2 array('F') with bounds (n,n) and a storage\nipiv : rank-1 array('i') with bounds (n)\njpiv : rank-1 array('i') with bounds (n)\ninfo : int\n"
    ...

def cgetrf(a, overwrite_a=...) -> typing.Any:
    "lu,piv,info = cgetrf(a,[overwrite_a])\n\nWrapper for ``cgetrf``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\nlu : rank-2 array('F') with bounds (m,n) and a storage\npiv : rank-1 array('i') with bounds (MIN(m,n))\ninfo : int\n"
    ...

def cgetri(lu, piv, lwork=..., overwrite_lu=...) -> typing.Any:
    "inv_a,info = cgetri(lu,piv,[lwork,overwrite_lu])\n\nWrapper for ``cgetri``.\n\nParameters\n----------\nlu : input rank-2 array('F') with bounds (n,n)\npiv : input rank-1 array('i') with bounds (n)\n\nOther Parameters\n----------------\noverwrite_lu : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(3*n,1)\n\nReturns\n-------\ninv_a : rank-2 array('F') with bounds (n,n) and lu storage\ninfo : int\n"
    ...

def cgetri_lwork(n) -> typing.Any:
    'work,info = cgetri_lwork(n)\n\nWrapper for ``cgetri_lwork``.\n\nParameters\n----------\nn : input int\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    ...

def cgetrs(lu, piv, b, trans=..., overwrite_b=...) -> typing.Any:
    "x,info = cgetrs(lu,piv,b,[trans,overwrite_b])\n\nWrapper for ``cgetrs``.\n\nParameters\n----------\nlu : input rank-2 array('F') with bounds (n,n)\npiv : input rank-1 array('i') with bounds (n)\nb : input rank-2 array('F') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_b : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('F') with bounds (n,nrhs) and b storage\ninfo : int\n"
    ...

def cgges(cselect, a, b, jobvsl=..., jobvsr=..., sort_t=..., ldvsl=..., ldvsr=..., lwork=..., cselect_extra_args=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "a,b,sdim,alpha,beta,vsl,vsr,work,info = cgges(cselect,a,b,[jobvsl,jobvsr,sort_t,ldvsl,ldvsr,lwork,cselect_extra_args,overwrite_a,overwrite_b])\n\nWrapper for ``cgges``.\n\nParameters\n----------\ncselect : call-back function\na : input rank-2 array('F') with bounds (lda,n)\nb : input rank-2 array('F') with bounds (ldb,n)\n\nOther Parameters\n----------------\njobvsl : input int, optional\n    Default: 1\njobvsr : input int, optional\n    Default: 1\nsort_t : input int, optional\n    Default: 0\ncselect_extra_args : input tuple, optional\n    Default: ()\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nldvsl : input int, optional\n    Default: ((jobvsl==1)?n:1)\nldvsr : input int, optional\n    Default: ((jobvsr==1)?n:1)\nlwork : input int, optional\n    Default: max(2*n,1)\n\nReturns\n-------\na : rank-2 array('F') with bounds (lda,n)\nb : rank-2 array('F') with bounds (ldb,n)\nsdim : int\nalpha : rank-1 array('F') with bounds (n)\nbeta : rank-1 array('F') with bounds (n)\nvsl : rank-2 array('F') with bounds (ldvsl,n)\nvsr : rank-2 array('F') with bounds (ldvsr,n)\nwork : rank-1 array('F') with bounds (MAX(lwork,1))\ninfo : int\n\nNotes\n-----\nCall-back functions::\n\n  def cselect(alpha,beta): return cselect\n  Required arguments:\n    alpha : input complex\n    beta : input complex\n  Return objects:\n    cselect : int\n"
    ...

def cggev(a, b, compute_vl=..., compute_vr=..., lwork=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "alpha,beta,vl,vr,work,info = cggev(a,b,[compute_vl,compute_vr,lwork,overwrite_a,overwrite_b])\n\nWrapper for ``cggev``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (n,n)\nb : input rank-2 array('F') with bounds (n,n)\n\nOther Parameters\n----------------\ncompute_vl : input int, optional\n    Default: 1\ncompute_vr : input int, optional\n    Default: 1\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(2*n,1)\n\nReturns\n-------\nalpha : rank-1 array('F') with bounds (n)\nbeta : rank-1 array('F') with bounds (n)\nvl : rank-2 array('F') with bounds (ldvl,n)\nvr : rank-2 array('F') with bounds (ldvr,n)\nwork : rank-1 array('F') with bounds (MAX(lwork,1))\ninfo : int\n"
    ...

def cgglse(a, b, c, d, lwork=..., overwrite_a=..., overwrite_b=..., overwrite_c=..., overwrite_d=...) -> typing.Any:
    "t,r,res,x,info = cgglse(a,b,c,d,[lwork,overwrite_a,overwrite_b,overwrite_c,overwrite_d])\n\nWrapper for ``cgglse``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (m,n)\nb : input rank-2 array('F') with bounds (p,n)\nc : input rank-1 array('F') with bounds (m)\nd : input rank-1 array('F') with bounds (p)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\noverwrite_c : input int, optional\n    Default: 0\noverwrite_d : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(m+n+p,1)\n\nReturns\n-------\nt : rank-2 array('F') with bounds (m,n) and a storage\nr : rank-2 array('F') with bounds (p,n) and b storage\nres : rank-1 array('F') with bounds (m) and c storage\nx : rank-1 array('F') with bounds (n)\ninfo : int\n"
    ...

def cgglse_lwork(m, n, p) -> typing.Any:
    'work,info = cgglse_lwork(m,n,p)\n\nWrapper for ``cgglse_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\np : input int\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    ...

def cgtsv(dl, d, du, b, overwrite_dl=..., overwrite_d=..., overwrite_du=..., overwrite_b=...) -> typing.Any:
    "du2,d,du,x,info = cgtsv(dl,d,du,b,[overwrite_dl,overwrite_d,overwrite_du,overwrite_b])\n\nWrapper for ``cgtsv``.\n\nParameters\n----------\ndl : input rank-1 array('F') with bounds (n - 1)\nd : input rank-1 array('F') with bounds (n)\ndu : input rank-1 array('F') with bounds (n - 1)\nb : input rank-2 array('F') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_dl : input int, optional\n    Default: 0\noverwrite_d : input int, optional\n    Default: 0\noverwrite_du : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\ndu2 : rank-1 array('F') with bounds (n - 1) and dl storage\nd : rank-1 array('F') with bounds (n)\ndu : rank-1 array('F') with bounds (n - 1)\nx : rank-2 array('F') with bounds (n,nrhs) and b storage\ninfo : int\n"
    ...

def cgtsvx(dl, d, du, b, fact=..., trans=..., dlf=..., df=..., duf=..., du2=..., ipiv=...) -> typing.Any:
    "dlf,df,duf,du2,ipiv,x,rcond,ferr,berr,info = cgtsvx(dl,d,du,b,[fact,trans,dlf,df,duf,du2,ipiv])\n\nWrapper for ``cgtsvx``.\n\nParameters\n----------\ndl : input rank-1 array('F') with bounds (MAX(0, n-1))\nd : input rank-1 array('F') with bounds (n)\ndu : input rank-1 array('F') with bounds (MAX(0, n-1))\nb : input rank-2 array('F') with bounds (ldb,nrhs)\n\nOther Parameters\n----------------\nfact : input string(len=1), optional\n    Default: 'N'\ntrans : input string(len=1), optional\n    Default: 'N'\ndlf : input rank-1 array('F') with bounds (MAX(0,n-1))\ndf : input rank-1 array('F') with bounds (n)\nduf : input rank-1 array('F') with bounds (MAX(0,n-1))\ndu2 : input rank-1 array('F') with bounds (MAX(0,n-2))\nipiv : input rank-1 array('i') with bounds (n)\n\nReturns\n-------\ndlf : rank-1 array('F') with bounds (MAX(0,n-1))\ndf : rank-1 array('F') with bounds (n)\nduf : rank-1 array('F') with bounds (MAX(0,n-1))\ndu2 : rank-1 array('F') with bounds (MAX(0,n-2))\nipiv : rank-1 array('i') with bounds (n)\nx : rank-2 array('F') with bounds (ldx,nrhs)\nrcond : float\nferr : rank-1 array('f') with bounds (nrhs)\nberr : rank-1 array('f') with bounds (nrhs)\ninfo : int\n"
    ...

def cgttrf(dl, d, du, overwrite_dl=..., overwrite_d=..., overwrite_du=...) -> typing.Any:
    "dl,d,du,du2,ipiv,info = cgttrf(dl,d,du,[overwrite_dl,overwrite_d,overwrite_du])\n\nWrapper for ``cgttrf``.\n\nParameters\n----------\ndl : input rank-1 array('F') with bounds (n - 1)\nd : input rank-1 array('F') with bounds (n)\ndu : input rank-1 array('F') with bounds (n - 1)\n\nOther Parameters\n----------------\noverwrite_dl : input int, optional\n    Default: 0\noverwrite_d : input int, optional\n    Default: 0\noverwrite_du : input int, optional\n    Default: 0\n\nReturns\n-------\ndl : rank-1 array('F') with bounds (n - 1)\nd : rank-1 array('F') with bounds (n)\ndu : rank-1 array('F') with bounds (n - 1)\ndu2 : rank-1 array('F') with bounds (n - 2)\nipiv : rank-1 array('i') with bounds (n)\ninfo : int\n"
    ...

def cgttrs(dl, d, du, du2, ipiv, b, trans=..., overwrite_b=...) -> typing.Any:
    "x,info = cgttrs(dl,d,du,du2,ipiv,b,[trans,overwrite_b])\n\nWrapper for ``cgttrs``.\n\nParameters\n----------\ndl : input rank-1 array('F') with bounds (n - 1)\nd : input rank-1 array('F') with bounds (n)\ndu : input rank-1 array('F') with bounds (n - 1)\ndu2 : input rank-1 array('F') with bounds (n - 2)\nipiv : input rank-1 array('i') with bounds (n)\nb : input rank-2 array('F') with bounds (ldb,nrhs)\n\nOther Parameters\n----------------\ntrans : input string(len=1), optional\n    Default: 'N'\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('F') with bounds (ldb,nrhs) and b storage\ninfo : int\n"
    ...

def chbevd(ab, compute_v=..., lower=..., ldab=..., lrwork=..., liwork=..., overwrite_ab=...) -> typing.Any:
    "w,z,info = chbevd(ab,[compute_v,lower,ldab,lrwork,liwork,overwrite_ab])\n\nWrapper for ``chbevd``.\n\nParameters\n----------\nab : input rank-2 array('F') with bounds (ldab,n)\n\nOther Parameters\n----------------\noverwrite_ab : input int, optional\n    Default: 1\ncompute_v : input int, optional\n    Default: 1\nlower : input int, optional\n    Default: 0\nldab : input int, optional\n    Default: shape(ab,0)\nlrwork : input int, optional\n    Default: (compute_v?1+5*n+2*n*n:n)\nliwork : input int, optional\n    Default: (compute_v?3+5*n:1)\n\nReturns\n-------\nw : rank-1 array('f') with bounds (n)\nz : rank-2 array('F') with bounds (ldz,ldz)\ninfo : int\n"
    ...

def chbevx(ab, vl, vu, il, iu, ldab=..., compute_v=..., range=..., lower=..., abstol=..., mmax=..., overwrite_ab=...) -> typing.Any:
    "w,z,m,ifail,info = chbevx(ab,vl,vu,il,iu,[ldab,compute_v,range,lower,abstol,mmax,overwrite_ab])\n\nWrapper for ``chbevx``.\n\nParameters\n----------\nab : input rank-2 array('F') with bounds (ldab,n)\nvl : input float\nvu : input float\nil : input int\niu : input int\n\nOther Parameters\n----------------\noverwrite_ab : input int, optional\n    Default: 1\nldab : input int, optional\n    Default: shape(ab,0)\ncompute_v : input int, optional\n    Default: 1\nrange : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\nabstol : input float, optional\n    Default: 0.0\nmmax : input int, optional\n    Default: (compute_v?(range==2?(iu-il+1):n):1)\n\nReturns\n-------\nw : rank-1 array('f') with bounds (n)\nz : rank-2 array('F') with bounds (ldz,mmax)\nm : int\nifail : rank-1 array('i') with bounds ((compute_v?n:1))\ninfo : int\n"
    ...

def checon(a, ipiv, anorm, lower=...) -> typing.Any:
    "rcond,info = checon(a,ipiv,anorm,[lower])\n\nWrapper for ``checon``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (n,n)\nipiv : input rank-1 array('i') with bounds (n)\nanorm : input float\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nrcond : float\ninfo : int\n"
    ...

def cheequb(a, lower=...) -> typing.Any:
    "s,scond,amax,info = cheequb(a,[lower])\n\nWrapper for ``cheequb``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (lda,n)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\ns : rank-1 array('f') with bounds (n)\nscond : float\namax : float\ninfo : int\n"
    ...

def cheev(a, compute_v=..., lower=..., lwork=..., overwrite_a=...) -> typing.Any:
    "w,v,info = cheev(a,[compute_v,lower,lwork,overwrite_a])\n\nWrapper for ``cheev``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (n,n)\n\nOther Parameters\n----------------\ncompute_v : input int, optional\n    Default: 1\nlower : input int, optional\n    Default: 0\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(2*n-1,1)\n\nReturns\n-------\nw : rank-1 array('f') with bounds (n)\nv : rank-2 array('F') with bounds (n,n) and a storage\ninfo : int\n"
    ...

def cheev_lwork(n, lower=...) -> typing.Any:
    'work,info = cheev_lwork(n,[lower])\n\nWrapper for ``cheev_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    ...

def cheevd(a, compute_v=..., lower=..., lwork=..., liwork=..., lrwork=..., overwrite_a=...) -> typing.Any:
    "w,v,info = cheevd(a,[compute_v,lower,lwork,liwork,lrwork,overwrite_a])\n\nWrapper for ``cheevd``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (n,n)\n\nOther Parameters\n----------------\ncompute_v : input int, optional\n    Default: 1\nlower : input int, optional\n    Default: 0\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max((compute_v?2*n+n*n:n+1),1)\nliwork : input int, optional\n    Default: (compute_v?3+5*n:1)\nlrwork : input int, optional\n    Default: (compute_v?1+5*n+2*n*n:n)\n\nReturns\n-------\nw : rank-1 array('f') with bounds (n)\nv : rank-2 array('F') with bounds (n,n) and a storage\ninfo : int\n"
    ...

def cheevd_lwork(n, compute_v=..., lower=...) -> typing.Any:
    'work,iwork,rwork,info = cheevd_lwork(n,[compute_v,lower])\n\nWrapper for ``cheevd_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\ncompute_v : input int, optional\n    Default: 1\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nwork : complex\niwork : int\nrwork : float\ninfo : int\n'
    ...

def cheevr(a, compute_v=..., range=..., lower=..., vl=..., vu=..., il=..., iu=..., abstol=..., lwork=..., lrwork=..., liwork=..., overwrite_a=...) -> typing.Any:
    "w,z,m,isuppz,info = cheevr(a,[compute_v,range,lower,vl,vu,il,iu,abstol,lwork,lrwork,liwork,overwrite_a])\n\nWrapper for ``cheevr``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds ``(n,n)``\n\nOther Parameters\n----------------\ncompute_v : input int, optional\n    Default ``1``\nrange : input string(len=1), optional\n    Default ``'A'``\nlower : input int, optional\n    Default ``0``\noverwrite_a : input int, optional\n    Default ``0``\nvl : input float, optional\n    Default ``0.0``\nvu : input float, optional\n    Default ``1.0``\nil : input int, optional\n    Default ``1``\niu : input int, optional\n    Default ``n``\nabstol : input float, optional\n    Default ``0.0``\nlwork : input int, optional\n    Default ``max(2*n,1)``\nlrwork : input int, optional\n    Default ``max(24*n,1)``\nliwork : input int, optional\n    Default ``max(1,10*n)``\n\nReturns\n-------\nw : rank-1 array('f') with bounds ``(n)``\nz : rank-2 array('F') with bounds ``((compute_v?MAX(0,n):0),(compute_v?(*range=='I'?iu-il+1:MAX(1,n)):0))``\nm : int\nisuppz : rank-1 array('i') with bounds ``(2*max(1,n))``\ninfo : int\n"
    ...

def cheevr_lwork(n, lower=...) -> typing.Any:
    'work,rwork,iwork,info = cheevr_lwork(n,[lower])\n\nWrapper for ``cheevr_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nwork : complex\nrwork : float\niwork : int\ninfo : int\n'
    ...

def cheevx(a, compute_v=..., range=..., lower=..., vl=..., vu=..., il=..., iu=..., abstol=..., lwork=..., overwrite_a=...) -> typing.Any:
    "w,z,m,ifail,info = cheevx(a,[compute_v,range,lower,vl,vu,il,iu,abstol,lwork,overwrite_a])\n\nWrapper for ``cheevx``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds ``(n,n)``\n\nOther Parameters\n----------------\ncompute_v : input int, optional\n    Default ``1``\nrange : input string(len=1), optional\n    Default ``'A'``\nlower : input int, optional\n    Default ``0``\noverwrite_a : input int, optional\n    Default ``0``\nvl : input float, optional\n    Default ``0.0``\nvu : input float, optional\n    Default ``1.0``\nil : input int, optional\n    Default ``1``\niu : input int, optional\n    Default ``n``\nabstol : input float, optional\n    Default ``0.0``\nlwork : input int, optional\n    Default ``max(2*n,1)``\n\nReturns\n-------\nw : rank-1 array('f') with bounds ``(n)``\nz : rank-2 array('F') with bounds ``((compute_v*n),(compute_v?(*range=='I'?iu-il+1:MAX(1,n)):0))``\nm : int\nifail : rank-1 array('i') with bounds ``(compute_v*n)``\ninfo : int\n"
    ...

def cheevx_lwork(n, lower=...) -> typing.Any:
    'work,info = cheevx_lwork(n,[lower])\n\nWrapper for ``cheevx_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    ...

def chegst(a, b, itype=..., lower=..., overwrite_a=...) -> typing.Any:
    "c,info = chegst(a,b,[itype,lower,overwrite_a])\n\nWrapper for ``chegst``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (n,n)\nb : input rank-2 array('F') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nitype : input int, optional\n    Default: 1\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('F') with bounds (n,n) and a storage\ninfo : int\n"
    ...

def chegv(a, b, itype=..., jobz=..., uplo=..., lwork=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "w,v,info = chegv(a,b,[itype,jobz,uplo,lwork,overwrite_a,overwrite_b])\n\nWrapper for ``chegv``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (n,n)\nb : input rank-2 array('F') with bounds (n,n)\n\nOther Parameters\n----------------\nitype : input int, optional\n    Default: 1\njobz : input string(len=1), optional\n    Default: 'V'\nuplo : input string(len=1), optional\n    Default: 'L'\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(2*n-1,1)\n\nReturns\n-------\nw : rank-1 array('f') with bounds (n)\nv : rank-2 array('F') with bounds (n,n) and a storage\ninfo : int\n"
    ...

def chegv_lwork(n, uplo=...) -> typing.Any:
    "work,info = chegv_lwork(n,[uplo])\n\nWrapper for ``chegv_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nuplo : input string(len=1), optional\n    Default: 'L'\n\nReturns\n-------\nwork : complex\ninfo : int\n"
    ...

def chegvd(a, b, itype=..., jobz=..., uplo=..., lwork=..., lrwork=..., liwork=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "w,v,info = chegvd(a,b,[itype,jobz,uplo,lwork,lrwork,liwork,overwrite_a,overwrite_b])\n\nWrapper for ``chegvd``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds ``(n,n)``\nb : input rank-2 array('F') with bounds ``(n,n)``\n\nOther Parameters\n----------------\nitype : input int, optional\n    Default ``1``\njobz : input string(len=1), optional\n    Default ``'V'``\nuplo : input string(len=1), optional\n    Default ``'L'``\noverwrite_a : input int, optional\n    Default ``0``\noverwrite_b : input int, optional\n    Default ``0``\nlwork : input int, optional\n    Default ``(*jobz=='N'?n+1:n*(n+2))``\nlrwork : input int, optional\n    Default ``max((*jobz=='N'?n:2*n*n+5*n+1),1)``\nliwork : input int, optional\n    Default ``(*jobz=='N'?1:5*n+3)``\n\nReturns\n-------\nw : rank-1 array('f') with bounds ``(n)``\nv : rank-2 array('F') with bounds ``(n,n)`` with ``a`` storage\ninfo : int\n"
    ...

def chegvx(a, b, itype=..., jobz=..., range=..., uplo=..., vl=..., vu=..., il=..., iu=..., abstol=..., lwork=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "w,z,m,ifail,info = chegvx(a,b,[itype,jobz,range,uplo,vl,vu,il,iu,abstol,lwork,overwrite_a,overwrite_b])\n\nWrapper for ``chegvx``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (n,n)\nb : input rank-2 array('F') with bounds (n,n)\n\nOther Parameters\n----------------\nitype : input int, optional\n    Default: 1\njobz : input string(len=1), optional\n    Default: 'V'\nrange : input string(len=1), optional\n    Default: 'A'\nuplo : input string(len=1), optional\n    Default: 'L'\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nvl : input float, optional\n    Default: 0.0\nvu : input float, optional\n    Default: 1.0\nil : input int, optional\n    Default: 1\niu : input int, optional\n    Default: n\nabstol : input float, optional\n    Default: 0.0\nlwork : input int, optional\n    Default: max(2*n,1)\n\nReturns\n-------\nw : rank-1 array('f') with bounds (n)\nz : rank-2 array('F') with bounds ((jobz[0]=='V'?MAX(0,n):0),(jobz[0]=='V'?(range[0]=='I'?iu-il+1:MAX(1,n)):0))\nm : int\nifail : rank-1 array('i') with bounds ((jobz[0]=='N'?0:n))\ninfo : int\n"
    ...

def chegvx_lwork(n, uplo=...) -> typing.Any:
    "work,info = chegvx_lwork(n,[uplo])\n\nWrapper for ``chegvx_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nuplo : input string(len=1), optional\n    Default: 'L'\n\nReturns\n-------\nwork : complex\ninfo : int\n"
    ...

def chesv(a, b, lwork=..., lower=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "uduh,ipiv,x,info = chesv(a,b,[lwork,lower,overwrite_a,overwrite_b])\n\nWrapper for ``chesv``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (n,n)\nb : input rank-2 array('F') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(n,1)\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nuduh : rank-2 array('F') with bounds (n,n) and a storage\nipiv : rank-1 array('i') with bounds (n)\nx : rank-2 array('F') with bounds (n,nrhs) and b storage\ninfo : int\n"
    ...

def chesv_lwork(n, lower=...) -> typing.Any:
    'work,info = chesv_lwork(n,[lower])\n\nWrapper for ``chesv_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    ...

def chesvx(a, b, af=..., ipiv=..., lwork=..., factored=..., lower=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "uduh,ipiv,x,rcond,ferr,berr,info = chesvx(a,b,[af,ipiv,lwork,factored,lower,overwrite_a,overwrite_b])\n\nWrapper for ``chesvx``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (n,n)\nb : input rank-2 array('F') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\naf : input rank-2 array('F') with bounds (n,n)\nipiv : input rank-1 array('i') with bounds (n)\noverwrite_b : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(2*n,1)\nfactored : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nuduh : rank-2 array('F') with bounds (n,n) and af storage\nipiv : rank-1 array('i') with bounds (n)\nx : rank-2 array('F') with bounds (n,nrhs)\nrcond : float\nferr : rank-1 array('f') with bounds (nrhs)\nberr : rank-1 array('f') with bounds (nrhs)\ninfo : int\n"
    ...

def chesvx_lwork(n, lower=...) -> typing.Any:
    'work,info = chesvx_lwork(n,[lower])\n\nWrapper for ``chesvx_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    ...

def chetrd(a, lower=..., lwork=..., overwrite_a=...) -> typing.Any:
    "c,d,e,tau,info = chetrd(a,[lower,lwork,overwrite_a])\n\nWrapper for ``chetrd``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (lda,n)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: MAX(n,1)\n\nReturns\n-------\nc : rank-2 array('F') with bounds (lda,n) and a storage\nd : rank-1 array('f') with bounds (n)\ne : rank-1 array('f') with bounds (n - 1)\ntau : rank-1 array('F') with bounds (n - 1)\ninfo : int\n"
    ...

def chetrd_lwork(n, lower=...) -> typing.Any:
    'work,info = chetrd_lwork(n,[lower])\n\nWrapper for ``chetrd_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    ...

def chetrf(a, lower=..., lwork=..., overwrite_a=...) -> typing.Any:
    "ldu,ipiv,info = chetrf(a,[lower,lwork,overwrite_a])\n\nWrapper for ``chetrf``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (n,n)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(n,1)\n\nReturns\n-------\nldu : rank-2 array('F') with bounds (n,n) and a storage\nipiv : rank-1 array('i') with bounds (n)\ninfo : int\n"
    ...

def chetrf_lwork(n, lower=...) -> typing.Any:
    'work,info = chetrf_lwork(n,[lower])\n\nWrapper for ``chetrf_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    ...

def chfrk(n, k, alpha, a, beta, c, transr=..., uplo=..., trans=..., overwrite_c=...) -> typing.Any:
    "cout = chfrk(n,k,alpha,a,beta,c,[transr,uplo,trans,overwrite_c])\n\nWrapper for ``chfrk``.\n\nParameters\n----------\nn : input int\nk : input int\nalpha : input float\na : input rank-2 array('F') with bounds (lda,ka)\nbeta : input float\nc : input rank-1 array('F') with bounds (nt)\n\nOther Parameters\n----------------\ntransr : input string(len=1), optional\n    Default: 'N'\nuplo : input string(len=1), optional\n    Default: 'U'\ntrans : input string(len=1), optional\n    Default: 'N'\noverwrite_c : input int, optional\n    Default: 0\n\nReturns\n-------\ncout : rank-1 array('F') with bounds (nt) and c storage\n"
    ...

def clange(norm, a) -> typing.Any:
    "n2 = clange(norm,a)\n\nWrapper for ``clange``.\n\nParameters\n----------\nnorm : input string(len=1)\na : input rank-2 array('F') with bounds (m,n)\n\nReturns\n-------\nn2 : float\n"
    ...

def clarf(v, tau, c, work, side=..., incv=..., overwrite_c=...) -> typing.Any:
    "c = clarf(v,tau,c,work,[side,incv,overwrite_c])\n\nWrapper for ``clarf``.\n\nParameters\n----------\nv : input rank-1 array('F') with bounds ((side[0]=='L'?(1 + (m-1)*abs(incv)):(1 + (n-1)*abs(incv))))\ntau : input complex\nc : input rank-2 array('F') with bounds (m,n)\nwork : input rank-1 array('F') with bounds (lwork)\n\nOther Parameters\n----------------\nside : input string(len=1), optional\n    Default: 'L'\nincv : input int, optional\n    Default: 1\noverwrite_c : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('F') with bounds (m,n)\n"
    ...

def clarfg(n, alpha, x, incx=..., overwrite_x=...) -> typing.Any:
    "alpha,x,tau = clarfg(n,alpha,x,[incx,overwrite_x])\n\nWrapper for ``clarfg``.\n\nParameters\n----------\nn : input int\nalpha : input complex\nx : input rank-1 array('F') with bounds (lx)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\n\nReturns\n-------\nalpha : complex\nx : rank-1 array('F') with bounds (lx)\ntau : complex\n"
    ...

def clartg(f, g) -> typing.Any:
    'cs,sn,r = clartg(f,g)\n\nWrapper for ``clartg``.\n\nParameters\n----------\nf : input complex\ng : input complex\n\nReturns\n-------\ncs : float\nsn : complex\nr : complex\n'
    ...

def claswp(a, piv, k1=..., k2=..., off=..., inc=..., overwrite_a=...) -> typing.Any:
    "a = claswp(a,piv,[k1,k2,off,inc,overwrite_a])\n\nWrapper for ``claswp``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (nrows,n)\npiv : input rank-1 array('i') with bounds (npiv)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nk1 : input int, optional\n    Default: 0\nk2 : input int, optional\n    Default: npiv-1\noff : input int, optional\n    Default: 0\ninc : input int, optional\n    Default: 1\n\nReturns\n-------\na : rank-2 array('F') with bounds (nrows,n)\n"
    ...

def clauum(c, lower=..., overwrite_c=...) -> typing.Any:
    "a,info = clauum(c,[lower,overwrite_c])\n\nWrapper for ``clauum``.\n\nParameters\n----------\nc : input rank-2 array('F') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_c : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\na : rank-2 array('F') with bounds (n,n) and c storage\ninfo : int\n"
    ...

def cpbsv(ab, b, lower=..., ldab=..., overwrite_ab=..., overwrite_b=...) -> typing.Any:
    "c,x,info = cpbsv(ab,b,[lower,ldab,overwrite_ab,overwrite_b])\n\nWrapper for ``cpbsv``.\n\nParameters\n----------\nab : input rank-2 array('F') with bounds (ldab,n)\nb : input rank-2 array('F') with bounds (ldb,nrhs)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\noverwrite_ab : input int, optional\n    Default: 0\nldab : input int, optional\n    Default: shape(ab,0)\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('F') with bounds (ldab,n) and ab storage\nx : rank-2 array('F') with bounds (ldb,nrhs) and b storage\ninfo : int\n"
    ...

def cpbtrf(ab, lower=..., ldab=..., overwrite_ab=...) -> typing.Any:
    "c,info = cpbtrf(ab,[lower,ldab,overwrite_ab])\n\nWrapper for ``cpbtrf``.\n\nParameters\n----------\nab : input rank-2 array('F') with bounds (ldab,n)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\noverwrite_ab : input int, optional\n    Default: 0\nldab : input int, optional\n    Default: shape(ab,0)\n\nReturns\n-------\nc : rank-2 array('F') with bounds (ldab,n) and ab storage\ninfo : int\n"
    ...

def cpbtrs(ab, b, lower=..., ldab=..., overwrite_b=...) -> typing.Any:
    "x,info = cpbtrs(ab,b,[lower,ldab,overwrite_b])\n\nWrapper for ``cpbtrs``.\n\nParameters\n----------\nab : input rank-2 array('F') with bounds (ldab,n)\nb : input rank-2 array('F') with bounds (ldb,nrhs)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\nldab : input int, optional\n    Default: shape(ab,0)\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('F') with bounds (ldb,nrhs) and b storage\ninfo : int\n"
    ...

def cpftrf(n, a, transr=..., uplo=..., overwrite_a=...) -> typing.Any:
    "achol,info = cpftrf(n,a,[transr,uplo,overwrite_a])\n\nWrapper for ``cpftrf``.\n\nParameters\n----------\nn : input int\na : input rank-1 array('F') with bounds (nt)\n\nOther Parameters\n----------------\ntransr : input string(len=1), optional\n    Default: 'N'\nuplo : input string(len=1), optional\n    Default: 'U'\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\nachol : rank-1 array('F') with bounds (nt) and a storage\ninfo : int\n"
    ...

def cpftri(n, a, transr=..., uplo=..., overwrite_a=...) -> typing.Any:
    "ainv,info = cpftri(n,a,[transr,uplo,overwrite_a])\n\nWrapper for ``cpftri``.\n\nParameters\n----------\nn : input int\na : input rank-1 array('F') with bounds (nt)\n\nOther Parameters\n----------------\ntransr : input string(len=1), optional\n    Default: 'N'\nuplo : input string(len=1), optional\n    Default: 'U'\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\nainv : rank-1 array('F') with bounds (nt) and a storage\ninfo : int\n"
    ...

def cpftrs(n, a, b, transr=..., uplo=..., overwrite_b=...) -> typing.Any:
    "x,info = cpftrs(n,a,b,[transr,uplo,overwrite_b])\n\nWrapper for ``cpftrs``.\n\nParameters\n----------\nn : input int\na : input rank-1 array('F') with bounds (nt)\nb : input rank-2 array('F') with bounds (ldb,nhrs)\n\nOther Parameters\n----------------\ntransr : input string(len=1), optional\n    Default: 'N'\nuplo : input string(len=1), optional\n    Default: 'U'\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('F') with bounds (ldb,nhrs) and b storage\ninfo : int\n"
    ...

def cpocon(a, anorm, uplo=...) -> typing.Any:
    "rcond,info = cpocon(a,anorm,[uplo])\n\nWrapper for ``cpocon``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (n,n)\nanorm : input float\n\nOther Parameters\n----------------\nuplo : input string(len=1), optional\n    Default: 'U'\n\nReturns\n-------\nrcond : float\ninfo : int\n"
    ...

def cposv(a, b, lower=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "c,x,info = cposv(a,b,[lower,overwrite_a,overwrite_b])\n\nWrapper for ``cposv``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (n,n)\nb : input rank-2 array('F') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('F') with bounds (n,n) and a storage\nx : rank-2 array('F') with bounds (n,nrhs) and b storage\ninfo : int\n"
    ...

def cposvx(a, b, fact=..., af=..., equed=..., s=..., lower=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "a_s,lu,equed,s,b_s,x,rcond,ferr,berr,info = cposvx(a,b,[fact,af,equed,s,lower,overwrite_a,overwrite_b])\n\nWrapper for ``cposvx``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (n,n)\nb : input rank-2 array('F') with bounds (n,nrhs)\n\nOther Parameters\n----------------\nfact : input string(len=1), optional\n    Default: 'E'\noverwrite_a : input int, optional\n    Default: 0\naf : input rank-2 array('F') with bounds (n,n)\nequed : input string(len=1), optional\n    Default: 'Y'\ns : input rank-1 array('f') with bounds (n)\noverwrite_b : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\na_s : rank-2 array('F') with bounds (n,n) and a storage\nlu : rank-2 array('F') with bounds (n,n) and af storage\nequed : string(len=1)\ns : rank-1 array('f') with bounds (n)\nb_s : rank-2 array('F') with bounds (n,nrhs) and b storage\nx : rank-2 array('F') with bounds (n,nrhs)\nrcond : float\nferr : rank-1 array('f') with bounds (nrhs)\nberr : rank-1 array('f') with bounds (nrhs)\ninfo : int\n"
    ...

def cpotrf(a, lower=..., clean=..., overwrite_a=...) -> typing.Any:
    "c,info = cpotrf(a,[lower,clean,overwrite_a])\n\nWrapper for ``cpotrf``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\nclean : input int, optional\n    Default: 1\n\nReturns\n-------\nc : rank-2 array('F') with bounds (n,n) and a storage\ninfo : int\n"
    ...

def cpotri(c, lower=..., overwrite_c=...) -> typing.Any:
    "inv_a,info = cpotri(c,[lower,overwrite_c])\n\nWrapper for ``cpotri``.\n\nParameters\n----------\nc : input rank-2 array('F') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_c : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\ninv_a : rank-2 array('F') with bounds (n,n) and c storage\ninfo : int\n"
    ...

def cpotrs(c, b, lower=..., overwrite_b=...) -> typing.Any:
    "x,info = cpotrs(c,b,[lower,overwrite_b])\n\nWrapper for ``cpotrs``.\n\nParameters\n----------\nc : input rank-2 array('F') with bounds (n,n)\nb : input rank-2 array('F') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_b : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('F') with bounds (n,nrhs) and b storage\ninfo : int\n"
    ...

def cppcon(n, ap, anorm, lower=...) -> typing.Any:
    "rcond,info = cppcon(n,ap,anorm,[lower])\n\nWrapper for ``cppcon``.\n\nParameters\n----------\nn : input int\nap : input rank-1 array('F') with bounds (L)\nanorm : input float\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nrcond : float\ninfo : int\n"
    ...

def cppsv(n, ap, b, lower=..., overwrite_b=...) -> typing.Any:
    "x,info = cppsv(n,ap,b,[lower,overwrite_b])\n\nWrapper for ``cppsv``.\n\nParameters\n----------\nn : input int\nap : input rank-1 array('F') with bounds (L)\nb : input rank-2 array('F') with bounds (ldb,nrhs)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('F') with bounds (ldb,nrhs) and b storage\ninfo : int\n"
    ...

def cpptrf(n, ap, lower=..., overwrite_ap=...) -> typing.Any:
    "ul,info = cpptrf(n,ap,[lower,overwrite_ap])\n\nWrapper for ``cpptrf``.\n\nParameters\n----------\nn : input int\nap : input rank-1 array('F') with bounds (L)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\noverwrite_ap : input int, optional\n    Default: 0\n\nReturns\n-------\nul : rank-1 array('F') with bounds (L) and ap storage\ninfo : int\n"
    ...

def cpptri(n, ap, lower=..., overwrite_ap=...) -> typing.Any:
    "uli,info = cpptri(n,ap,[lower,overwrite_ap])\n\nWrapper for ``cpptri``.\n\nParameters\n----------\nn : input int\nap : input rank-1 array('F') with bounds (L)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\noverwrite_ap : input int, optional\n    Default: 0\n\nReturns\n-------\nuli : rank-1 array('F') with bounds (L) and ap storage\ninfo : int\n"
    ...

def cpptrs(n, ap, b, lower=..., overwrite_b=...) -> typing.Any:
    "x,info = cpptrs(n,ap,b,[lower,overwrite_b])\n\nWrapper for ``cpptrs``.\n\nParameters\n----------\nn : input int\nap : input rank-1 array('F') with bounds (L)\nb : input rank-2 array('F') with bounds (ldb,nrhs)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('F') with bounds (ldb,nrhs) and b storage\ninfo : int\n"
    ...

def cpstf2(a, tol=..., lower=..., overwrite_a=...) -> typing.Any:
    "c,piv,rank_c,info = cpstf2(a,[tol,lower,overwrite_a])\n\nWrapper for ``cpstf2``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\ntol : input float, optional\n    Default: -1.0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('F') with bounds (n,n) and a storage\npiv : rank-1 array('i') with bounds (n)\nrank_c : int\ninfo : int\n"
    ...

def cpstrf(a, tol=..., lower=..., overwrite_a=...) -> typing.Any:
    "c,piv,rank_c,info = cpstrf(a,[tol,lower,overwrite_a])\n\nWrapper for ``cpstrf``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\ntol : input float, optional\n    Default: -1.0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('F') with bounds (n,n) and a storage\npiv : rank-1 array('i') with bounds (n)\nrank_c : int\ninfo : int\n"
    ...

def cpteqr(d, e, z, compute_z=..., overwrite_d=..., overwrite_e=..., overwrite_z=...) -> typing.Any:
    "d,e,z,info = cpteqr(d,e,z,[compute_z,overwrite_d,overwrite_e,overwrite_z])\n\nWrapper for ``cpteqr``.\n\nParameters\n----------\nd : input rank-1 array('f') with bounds (n)\ne : input rank-1 array('f') with bounds ((n>0?n-1:0))\nz : input rank-2 array('F') with bounds ((compute_z==0?shape(z, 0):max(1,n)),(compute_z==0?shape(z, 1):n))\n\nOther Parameters\n----------------\ncompute_z : input int, optional\n    Default: 0\noverwrite_d : input int, optional\n    Default: 0\noverwrite_e : input int, optional\n    Default: 0\noverwrite_z : input int, optional\n    Default: 0\n\nReturns\n-------\nd : rank-1 array('f') with bounds (n)\ne : rank-1 array('f') with bounds ((n>0?n-1:0))\nz : rank-2 array('F') with bounds ((compute_z==0?shape(z, 0):max(1,n)),(compute_z==0?shape(z, 1):n))\ninfo : int\n"
    ...

def cptsv(d, e, b, overwrite_d=..., overwrite_e=..., overwrite_b=...) -> typing.Any:
    "d,du,x,info = cptsv(d,e,b,[overwrite_d,overwrite_e,overwrite_b])\n\nWrapper for ``cptsv``.\n\nParameters\n----------\nd : input rank-1 array('f') with bounds (n)\ne : input rank-1 array('F') with bounds (n - 1)\nb : input rank-2 array('F') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_d : input int, optional\n    Default: 0\noverwrite_e : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nd : rank-1 array('f') with bounds (n)\ndu : rank-1 array('F') with bounds (n - 1) and e storage\nx : rank-2 array('F') with bounds (n,nrhs) and b storage\ninfo : int\n"
    ...

def cptsvx(d, e, b, fact=..., df=..., ef=...) -> typing.Any:
    "df,ef,x,rcond,ferr,berr,info = cptsvx(d,e,b,[fact,df,ef])\n\nWrapper for ``cptsvx``.\n\nParameters\n----------\nd : input rank-1 array('f') with bounds (n)\ne : input rank-1 array('F') with bounds (max(0, n-1))\nb : input rank-2 array('F') with bounds (ldb,nrhs)\n\nOther Parameters\n----------------\nfact : input string(len=1), optional\n    Default: 'N'\ndf : input rank-1 array('f') with bounds (n)\nef : input rank-1 array('F') with bounds (max(0, n-1))\n\nReturns\n-------\ndf : rank-1 array('f') with bounds (n)\nef : rank-1 array('F') with bounds (max(0, n-1))\nx : rank-2 array('F') with bounds (ldx,nrhs)\nrcond : float\nferr : rank-1 array('f') with bounds (nrhs)\nberr : rank-1 array('f') with bounds (nrhs)\ninfo : int\n"
    ...

def cpttrf(d, e, overwrite_d=..., overwrite_e=...) -> typing.Any:
    "d,e,info = cpttrf(d,e,[overwrite_d,overwrite_e])\n\nWrapper for ``cpttrf``.\n\nParameters\n----------\nd : input rank-1 array('f') with bounds (n)\ne : input rank-1 array('F') with bounds ((n>0?n-1:0))\n\nOther Parameters\n----------------\noverwrite_d : input int, optional\n    Default: 0\noverwrite_e : input int, optional\n    Default: 0\n\nReturns\n-------\nd : rank-1 array('f') with bounds (n)\ne : rank-1 array('F') with bounds ((n>0?n-1:0))\ninfo : int\n"
    ...

def cpttrs(d, e, b, lower=..., overwrite_b=...) -> typing.Any:
    "x,info = cpttrs(d,e,b,[lower,overwrite_b])\n\nWrapper for ``cpttrs``.\n\nParameters\n----------\nd : input rank-1 array('f') with bounds (n)\ne : input rank-1 array('F') with bounds ((n>0?n-1:0))\nb : input rank-2 array('F') with bounds (ldb,nrhs)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('F') with bounds (ldb,nrhs) and b storage\ninfo : int\n"
    ...

def crot(x, y, c, s, n=..., offx=..., incx=..., offy=..., incy=..., overwrite_x=..., overwrite_y=...) -> typing.Any:
    "x,y = crot(x,y,c,s,[n,offx,incx,offy,incy,overwrite_x,overwrite_y])\n\nWrapper for ``crot``.\n\nParameters\n----------\nx : input rank-1 array('F') with bounds (lx)\ny : input rank-1 array('F') with bounds (ly)\nc : input float\ns : input complex\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (lx-1-offx)/abs(incx)+1\noverwrite_x : input int, optional\n    Default: 0\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noverwrite_y : input int, optional\n    Default: 0\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\n\nReturns\n-------\nx : rank-1 array('F') with bounds (lx)\ny : rank-1 array('F') with bounds (ly)\n"
    ...

def csycon(a, ipiv, anorm, lower=...) -> typing.Any:
    "rcond,info = csycon(a,ipiv,anorm,[lower])\n\nWrapper for ``csycon``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (n,n)\nipiv : input rank-1 array('i') with bounds (n)\nanorm : input float\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nrcond : float\ninfo : int\n"
    ...

def csyconv(a, ipiv, lower=..., way=..., overwrite_a=...) -> typing.Any:
    "a,e,info = csyconv(a,ipiv,[lower,way,overwrite_a])\n\nWrapper for ``csyconv``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (n,n)\nipiv : input rank-1 array('i') with bounds (n)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\nway : input int, optional\n    Default: 0\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\na : rank-2 array('F') with bounds (n,n)\ne : rank-1 array('F') with bounds (n)\ninfo : int\n"
    ...

def csyequb(a, lower=...) -> typing.Any:
    "s,scond,amax,info = csyequb(a,[lower])\n\nWrapper for ``csyequb``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (lda,n)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\ns : rank-1 array('f') with bounds (n)\nscond : float\namax : float\ninfo : int\n"
    ...

def csysv(a, b, lwork=..., lower=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "udut,ipiv,x,info = csysv(a,b,[lwork,lower,overwrite_a,overwrite_b])\n\nWrapper for ``csysv``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (n,n)\nb : input rank-2 array('F') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(n,1)\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nudut : rank-2 array('F') with bounds (n,n) and a storage\nipiv : rank-1 array('i') with bounds (n)\nx : rank-2 array('F') with bounds (n,nrhs) and b storage\ninfo : int\n"
    ...

def csysv_lwork(n, lower=...) -> typing.Any:
    'work,info = csysv_lwork(n,[lower])\n\nWrapper for ``csysv_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    ...

def csysvx(a, b, af=..., ipiv=..., lwork=..., factored=..., lower=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "a_s,udut,ipiv,b_s,x,rcond,ferr,berr,info = csysvx(a,b,[af,ipiv,lwork,factored,lower,overwrite_a,overwrite_b])\n\nWrapper for ``csysvx``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (n,n)\nb : input rank-2 array('F') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\naf : input rank-2 array('F') with bounds (n,n)\nipiv : input rank-1 array('i') with bounds (n)\noverwrite_b : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(3*n,1)\nfactored : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\na_s : rank-2 array('F') with bounds (n,n) and a storage\nudut : rank-2 array('F') with bounds (n,n) and af storage\nipiv : rank-1 array('i') with bounds (n)\nb_s : rank-2 array('F') with bounds (n,nrhs) and b storage\nx : rank-2 array('F') with bounds (n,nrhs)\nrcond : float\nferr : rank-1 array('f') with bounds (nrhs)\nberr : rank-1 array('f') with bounds (nrhs)\ninfo : int\n"
    ...

def csysvx_lwork(n, lower=...) -> typing.Any:
    'work,info = csysvx_lwork(n,[lower])\n\nWrapper for ``csysvx_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    ...

def csytf2(a, lower=..., overwrite_a=...) -> typing.Any:
    "ldu,ipiv,info = csytf2(a,[lower,overwrite_a])\n\nWrapper for ``csytf2``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (n,n)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\nldu : rank-2 array('F') with bounds (n,n) and a storage\nipiv : rank-1 array('i') with bounds (n)\ninfo : int\n"
    ...

def csytrf(a, lower=..., lwork=..., overwrite_a=...) -> typing.Any:
    "ldu,ipiv,info = csytrf(a,[lower,lwork,overwrite_a])\n\nWrapper for ``csytrf``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (n,n)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(n,1)\n\nReturns\n-------\nldu : rank-2 array('F') with bounds (n,n) and a storage\nipiv : rank-1 array('i') with bounds (n)\ninfo : int\n"
    ...

def csytrf_lwork(n, lower=...) -> typing.Any:
    'work,info = csytrf_lwork(n,[lower])\n\nWrapper for ``csytrf_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    ...

def ctbtrs(ab, b, uplo=..., trans=..., diag=..., overwrite_b=...) -> typing.Any:
    "x,info = ctbtrs(ab,b,[uplo,trans,diag,overwrite_b])\n\nWrapper for ``ctbtrs``.\n\nParameters\n----------\nab : input rank-2 array('F') with bounds (ldab,n)\nb : input rank-2 array('F') with bounds (ldb,nrhs)\n\nOther Parameters\n----------------\nuplo : input string(len=1), optional\n    Default: 'U'\ntrans : input string(len=1), optional\n    Default: 'N'\ndiag : input string(len=1), optional\n    Default: 'N'\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('F') with bounds (ldb,nrhs) and b storage\ninfo : int\n"
    ...

def ctfsm(alpha, a, b, transr=..., side=..., uplo=..., trans=..., diag=..., overwrite_b=...) -> typing.Any:
    "x = ctfsm(alpha,a,b,[transr,side,uplo,trans,diag,overwrite_b])\n\nWrapper for ``ctfsm``.\n\nParameters\n----------\nalpha : input complex\na : input rank-1 array('F') with bounds (nt)\nb : input rank-2 array('F') with bounds (m,n)\n\nOther Parameters\n----------------\ntransr : input string(len=1), optional\n    Default: 'N'\nside : input string(len=1), optional\n    Default: 'L'\nuplo : input string(len=1), optional\n    Default: 'U'\ntrans : input string(len=1), optional\n    Default: 'N'\ndiag : input string(len=1), optional\n    Default: 'N'\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('F') with bounds (m,n) and b storage\n"
    ...

def ctfttp(n, arf, transr=..., uplo=...) -> typing.Any:
    "ap,info = ctfttp(n,arf,[transr,uplo])\n\nWrapper for ``ctfttp``.\n\nParameters\n----------\nn : input int\narf : input rank-1 array('F') with bounds (nt)\n\nOther Parameters\n----------------\ntransr : input string(len=1), optional\n    Default: 'N'\nuplo : input string(len=1), optional\n    Default: 'U'\n\nReturns\n-------\nap : rank-1 array('F') with bounds (nt)\ninfo : int\n"
    ...

def ctfttr(n, arf, transr=..., uplo=...) -> typing.Any:
    "a,info = ctfttr(n,arf,[transr,uplo])\n\nWrapper for ``ctfttr``.\n\nParameters\n----------\nn : input int\narf : input rank-1 array('F') with bounds (nt)\n\nOther Parameters\n----------------\ntransr : input string(len=1), optional\n    Default: 'N'\nuplo : input string(len=1), optional\n    Default: 'U'\n\nReturns\n-------\na : rank-2 array('F') with bounds (lda,n)\ninfo : int\n"
    ...

def ctgsen(select, a, b, q, z, lwork=..., liwork=..., overwrite_a=..., overwrite_b=..., overwrite_q=..., overwrite_z=...) -> typing.Any:
    "a,b,alpha,beta,q,z,m,pl,pr,dif,work,iwork,info = ctgsen(select,a,b,q,z,[lwork,liwork,overwrite_a,overwrite_b,overwrite_q,overwrite_z])\n\nWrapper for ``ctgsen``.\n\nParameters\n----------\nselect : input rank-1 array('i') with bounds (n)\na : input rank-2 array('F') with bounds (lda,n)\nb : input rank-2 array('F') with bounds (ldb,n)\nq : input rank-2 array('F') with bounds (ldq,n)\nz : input rank-2 array('F') with bounds (ldz,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\noverwrite_q : input int, optional\n    Default: 0\noverwrite_z : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(2*m*(n-m),1)\nliwork : input int, optional\n    Default: n+2\n\nReturns\n-------\na : rank-2 array('F') with bounds (lda,n)\nb : rank-2 array('F') with bounds (ldb,n)\nalpha : rank-1 array('F') with bounds (n)\nbeta : rank-1 array('F') with bounds (n)\nq : rank-2 array('F') with bounds (ldq,n)\nz : rank-2 array('F') with bounds (ldz,n)\nm : int\npl : float\npr : float\ndif : rank-1 array('f') with bounds (2)\nwork : rank-1 array('F') with bounds (MAX(lwork,1))\niwork : rank-1 array('i') with bounds (MAX(1,liwork))\ninfo : int\n"
    ...

def ctpmqrt(l, v, t, a, b, side=..., trans=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "a,b,info = ctpmqrt(l,v,t,a,b,[side,trans,overwrite_a,overwrite_b])\n\nWrapper for ``ctpmqrt``.\n\nParameters\n----------\nl : input int\nv : input rank-2 array('F') with bounds ((side[0]=='L'?m:n),k)\nt : input rank-2 array('F') with bounds (nb,k)\na : input rank-2 array('F') with bounds ((side[0]=='L'?k:m),(side[0]=='L'?n:k))\nb : input rank-2 array('F') with bounds (m,n)\n\nOther Parameters\n----------------\nside : input string(len=1), optional\n    Default: 'L'\ntrans : input string(len=1), optional\n    Default: 'N'\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\na : rank-2 array('F') with bounds ((side[0]=='L'?k:m),(side[0]=='L'?n:k))\nb : rank-2 array('F') with bounds (m,n)\ninfo : int\n"
    ...

def ctpqrt(l, nb, a, b, overwrite_a=..., overwrite_b=...) -> typing.Any:
    "a,b,t,info = ctpqrt(l,nb,a,b,[overwrite_a,overwrite_b])\n\nWrapper for ``ctpqrt``.\n\nParameters\n----------\nl : input int\nnb : input int\na : input rank-2 array('F') with bounds (n,n)\nb : input rank-2 array('F') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\na : rank-2 array('F') with bounds (n,n)\nb : rank-2 array('F') with bounds (m,n)\nt : rank-2 array('F') with bounds (nb,n)\ninfo : int\n"
    ...

def ctpttf(n, ap, transr=..., uplo=...) -> typing.Any:
    "arf,info = ctpttf(n,ap,[transr,uplo])\n\nWrapper for ``ctpttf``.\n\nParameters\n----------\nn : input int\nap : input rank-1 array('F') with bounds (nt)\n\nOther Parameters\n----------------\ntransr : input string(len=1), optional\n    Default: 'N'\nuplo : input string(len=1), optional\n    Default: 'U'\n\nReturns\n-------\narf : rank-1 array('F') with bounds (nt)\ninfo : int\n"
    ...

def ctpttr(n, ap, uplo=...) -> typing.Any:
    "a,info = ctpttr(n,ap,[uplo])\n\nWrapper for ``ctpttr``.\n\nParameters\n----------\nn : input int\nap : input rank-1 array('F') with bounds (nt)\n\nOther Parameters\n----------------\nuplo : input string(len=1), optional\n    Default: 'U'\n\nReturns\n-------\na : rank-2 array('F') with bounds (n,n)\ninfo : int\n"
    ...

def ctrsyl(a, b, c, trana=..., tranb=..., isgn=..., overwrite_c=...) -> typing.Any:
    "x,scale,info = ctrsyl(a,b,c,[trana,tranb,isgn,overwrite_c])\n\nWrapper for ``ctrsyl``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (m,m)\nb : input rank-2 array('F') with bounds (n,n)\nc : input rank-2 array('F') with bounds (m,n)\n\nOther Parameters\n----------------\ntrana : input string(len=1), optional\n    Default: 'N'\ntranb : input string(len=1), optional\n    Default: 'N'\nisgn : input int, optional\n    Default: 1\noverwrite_c : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('F') with bounds (m,n) and c storage\nscale : float\ninfo : int\n"
    ...

def ctrtri(c, lower=..., unitdiag=..., overwrite_c=...) -> typing.Any:
    "inv_c,info = ctrtri(c,[lower,unitdiag,overwrite_c])\n\nWrapper for ``ctrtri``.\n\nParameters\n----------\nc : input rank-2 array('F') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_c : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\nunitdiag : input int, optional\n    Default: 0\n\nReturns\n-------\ninv_c : rank-2 array('F') with bounds (n,n) and c storage\ninfo : int\n"
    ...

def ctrtrs(a, b, lower=..., trans=..., unitdiag=..., lda=..., overwrite_b=...) -> typing.Any:
    "x,info = ctrtrs(a,b,[lower,trans,unitdiag,lda,overwrite_b])\n\nWrapper for ``ctrtrs``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (lda,n)\nb : input rank-2 array('F') with bounds (ldb,nrhs)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\nunitdiag : input int, optional\n    Default: 0\nlda : input int, optional\n    Default: shape(a,0)\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('F') with bounds (ldb,nrhs) and b storage\ninfo : int\n"
    ...

def ctrttf(a, transr=..., uplo=...) -> typing.Any:
    "arf,info = ctrttf(a,[transr,uplo])\n\nWrapper for ``ctrttf``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (lda,n)\n\nOther Parameters\n----------------\ntransr : input string(len=1), optional\n    Default: 'N'\nuplo : input string(len=1), optional\n    Default: 'U'\n\nReturns\n-------\narf : rank-1 array('F') with bounds (n*(n+1)/2)\ninfo : int\n"
    ...

def ctrttp(a, uplo=...) -> typing.Any:
    "ap,info = ctrttp(a,[uplo])\n\nWrapper for ``ctrttp``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (lda,n)\n\nOther Parameters\n----------------\nuplo : input string(len=1), optional\n    Default: 'U'\n\nReturns\n-------\nap : rank-1 array('F') with bounds (n*(n+1)/2)\ninfo : int\n"
    ...

def ctzrzf(a, lwork=..., overwrite_a=...) -> typing.Any:
    "rz,tau,info = ctzrzf(a,[lwork,overwrite_a])\n\nWrapper for ``ctzrzf``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: MAX(m,1)\n\nReturns\n-------\nrz : rank-2 array('F') with bounds (m,n) and a storage\ntau : rank-1 array('F') with bounds (m)\ninfo : int\n"
    ...

def ctzrzf_lwork(m, n) -> typing.Any:
    'work,info = ctzrzf_lwork(m,n)\n\nWrapper for ``ctzrzf_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    ...

def cuncsd(x11, x12, x21, x22, compute_u1=..., compute_u2=..., compute_v1t=..., compute_v2t=..., trans=..., signs=..., lwork=..., lrwork=..., overwrite_x11=..., overwrite_x12=..., overwrite_x21=..., overwrite_x22=...) -> typing.Any:
    "cs11,cs12,cs21,cs22,theta,u1,u2,v1t,v2t,info = cuncsd(x11,x12,x21,x22,[compute_u1,compute_u2,compute_v1t,compute_v2t,trans,signs,lwork,lrwork,overwrite_x11,overwrite_x12,overwrite_x21,overwrite_x22])\n\nWrapper for ``cuncsd``.\n\nParameters\n----------\nx11 : input rank-2 array('F') with bounds (p,q)\nx12 : input rank-2 array('F') with bounds (p,mmq)\nx21 : input rank-2 array('F') with bounds (mmp,q)\nx22 : input rank-2 array('F') with bounds (mmp,mmq)\n\nOther Parameters\n----------------\ncompute_u1 : input int, optional\n    Default: 1\ncompute_u2 : input int, optional\n    Default: 1\ncompute_v1t : input int, optional\n    Default: 1\ncompute_v2t : input int, optional\n    Default: 1\ntrans : input int, optional\n    Default: 0\nsigns : input int, optional\n    Default: 0\noverwrite_x11 : input int, optional\n    Default: 0\noverwrite_x12 : input int, optional\n    Default: 0\noverwrite_x21 : input int, optional\n    Default: 0\noverwrite_x22 : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: 2*m+MAX(1,MAX(mmp,mmq))+1\nlrwork : input int, optional\n    Default: 5*MAX(1,q-1)+4*MAX(1,q)+8*q+1\n\nReturns\n-------\ncs11 : rank-2 array('F') with bounds (p,q) and x11 storage\ncs12 : rank-2 array('F') with bounds (p,mmq) and x12 storage\ncs21 : rank-2 array('F') with bounds (mmp,q) and x21 storage\ncs22 : rank-2 array('F') with bounds (mmp,mmq) and x22 storage\ntheta : rank-1 array('f') with bounds (min(min(p,mmp),min(q,mmq)))\nu1 : rank-2 array('F') with bounds ((compute_u1?p:0),(compute_u1?p:0))\nu2 : rank-2 array('F') with bounds ((compute_u2?mmp:0),(compute_u2?mmp:0))\nv1t : rank-2 array('F') with bounds ((compute_v1t?q:0),(compute_v1t?q:0))\nv2t : rank-2 array('F') with bounds ((compute_v2t?mmq:0),(compute_v2t?mmq:0))\ninfo : int\n"
    ...

def cuncsd_lwork(m, p, q) -> typing.Any:
    'work,rwork,info = cuncsd_lwork(m,p,q)\n\nWrapper for ``cuncsd_lwork``.\n\nParameters\n----------\nm : input int\np : input int\nq : input int\n\nReturns\n-------\nwork : complex\nrwork : float\ninfo : int\n'
    ...

def cunghr(a, tau, lo=..., hi=..., lwork=..., overwrite_a=...) -> typing.Any:
    "ht,info = cunghr(a,tau,[lo,hi,lwork,overwrite_a])\n\nWrapper for ``cunghr``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (n,n)\ntau : input rank-1 array('F') with bounds (n - 1)\n\nOther Parameters\n----------------\nlo : input int, optional\n    Default: 0\nhi : input int, optional\n    Default: n-1\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(hi-lo,1)\n\nReturns\n-------\nht : rank-2 array('F') with bounds (n,n) and a storage\ninfo : int\n"
    ...

def cunghr_lwork(n, lo=..., hi=...) -> typing.Any:
    'work,info = cunghr_lwork(n,[lo,hi])\n\nWrapper for ``cunghr_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlo : input int, optional\n    Default: 0\nhi : input int, optional\n    Default: n-1\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    ...

def cungqr(a, tau, lwork=..., overwrite_a=...) -> typing.Any:
    "q,work,info = cungqr(a,tau,[lwork,overwrite_a])\n\nWrapper for ``cungqr``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (m,n)\ntau : input rank-1 array('F') with bounds (k)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(3*n,1)\n\nReturns\n-------\nq : rank-2 array('F') with bounds (m,n) and a storage\nwork : rank-1 array('F') with bounds (MAX(lwork,1))\ninfo : int\n"
    ...

def cungrq(a, tau, lwork=..., overwrite_a=...) -> typing.Any:
    "q,work,info = cungrq(a,tau,[lwork,overwrite_a])\n\nWrapper for ``cungrq``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (m,n)\ntau : input rank-1 array('F') with bounds (k)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(3*m,1)\n\nReturns\n-------\nq : rank-2 array('F') with bounds (m,n) and a storage\nwork : rank-1 array('F') with bounds (MAX(lwork,1))\ninfo : int\n"
    ...

def cunmqr(side, trans, a, tau, c, lwork, overwrite_c=...) -> typing.Any:
    "cq,work,info = cunmqr(side,trans,a,tau,c,lwork,[overwrite_c])\n\nWrapper for ``cunmqr``.\n\nParameters\n----------\nside : input string(len=1)\ntrans : input string(len=1)\na : input rank-2 array('F') with bounds (lda,k)\ntau : input rank-1 array('F') with bounds (k)\nc : input rank-2 array('F') with bounds (ldc,n)\nlwork : input int\n\nOther Parameters\n----------------\noverwrite_c : input int, optional\n    Default: 0\n\nReturns\n-------\ncq : rank-2 array('F') with bounds (ldc,n) and c storage\nwork : rank-1 array('F') with bounds (MAX(lwork,1))\ninfo : int\n"
    ...

def cunmrz(a, tau, c, side=..., trans=..., lwork=..., overwrite_c=...) -> typing.Any:
    "cq,info = cunmrz(a,tau,c,[side,trans,lwork,overwrite_c])\n\nWrapper for ``cunmrz``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (k,nt)\ntau : input rank-1 array('F') with bounds (k)\nc : input rank-2 array('F') with bounds (m,n)\n\nOther Parameters\n----------------\nside : input string(len=1), optional\n    Default: 'L'\ntrans : input string(len=1), optional\n    Default: 'N'\noverwrite_c : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: MAX((side[0]=='L'?n:m),1)\n\nReturns\n-------\ncq : rank-2 array('F') with bounds (m,n) and c storage\ninfo : int\n"
    ...

def cunmrz_lwork(m, n, side=..., trans=...) -> typing.Any:
    "work,info = cunmrz_lwork(m,n,[side,trans])\n\nWrapper for ``cunmrz_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\n\nOther Parameters\n----------------\nside : input string(len=1), optional\n    Default: 'L'\ntrans : input string(len=1), optional\n    Default: 'N'\n\nReturns\n-------\nwork : complex\ninfo : int\n"
    ...

def dgbsv(kl, ku, ab, b, overwrite_ab=..., overwrite_b=...) -> typing.Any:
    "lub,piv,x,info = dgbsv(kl,ku,ab,b,[overwrite_ab,overwrite_b])\n\nWrapper for ``dgbsv``.\n\nParameters\n----------\nkl : input int\nku : input int\nab : input rank-2 array('d') with bounds (2*kl+ku+1,n)\nb : input rank-2 array('d') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_ab : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nlub : rank-2 array('d') with bounds (2*kl+ku+1,n) and ab storage\npiv : rank-1 array('i') with bounds (n)\nx : rank-2 array('d') with bounds (n,nrhs) and b storage\ninfo : int\n"
    ...

def dgbtrf(ab, kl, ku, m=..., n=..., ldab=..., overwrite_ab=...) -> typing.Any:
    "lu,ipiv,info = dgbtrf(ab,kl,ku,[m,n,ldab,overwrite_ab])\n\nWrapper for ``dgbtrf``.\n\nParameters\n----------\nab : input rank-2 array('d') with bounds (ldab,n)\nkl : input int\nku : input int\n\nOther Parameters\n----------------\nm : input int, optional\n    Default: shape(ab,1)\nn : input int, optional\n    Default: shape(ab,1)\noverwrite_ab : input int, optional\n    Default: 0\nldab : input int, optional\n    Default: max(shape(ab,0),1)\n\nReturns\n-------\nlu : rank-2 array('d') with bounds (ldab,n) and ab storage\nipiv : rank-1 array('i') with bounds (MIN(m,n))\ninfo : int\n"
    ...

def dgbtrs(ab, kl, ku, b, ipiv, trans=..., n=..., ldab=..., ldb=..., overwrite_b=...) -> typing.Any:
    "x,info = dgbtrs(ab,kl,ku,b,ipiv,[trans,n,ldab,ldb,overwrite_b])\n\nWrapper for ``dgbtrs``.\n\nParameters\n----------\nab : input rank-2 array('d') with bounds (ldab,n)\nkl : input int\nku : input int\nb : input rank-2 array('d') with bounds (ldb,nrhs)\nipiv : input rank-1 array('i') with bounds (n)\n\nOther Parameters\n----------------\noverwrite_b : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\nn : input int, optional\n    Default: shape(ab,1)\nldab : input int, optional\n    Default: shape(ab,0)\nldb : input int, optional\n    Default: shape(b,0)\n\nReturns\n-------\nx : rank-2 array('d') with bounds (ldb,nrhs) and b storage\ninfo : int\n"
    ...

def dgebal(a, scale=..., permute=..., overwrite_a=...) -> typing.Any:
    "ba,lo,hi,pivscale,info = dgebal(a,[scale,permute,overwrite_a])\n\nWrapper for ``dgebal``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (m,n)\n\nOther Parameters\n----------------\nscale : input int, optional\n    Default: 0\npermute : input int, optional\n    Default: 0\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\nba : rank-2 array('d') with bounds (m,n) and a storage\nlo : int\nhi : int\npivscale : rank-1 array('d') with bounds (n)\ninfo : int\n"
    ...

def dgecon(a, anorm, norm=...) -> typing.Any:
    "rcond,info = dgecon(a,anorm,[norm])\n\nWrapper for ``dgecon``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (n,n)\nanorm : input float\n\nOther Parameters\n----------------\nnorm : input string(len=1), optional\n    Default: '1'\n\nReturns\n-------\nrcond : float\ninfo : int\n"
    ...

def dgeequ(a) -> typing.Any:
    "r,c,rowcnd,colcnd,amax,info = dgeequ(a)\n\nWrapper for ``dgeequ``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (m,n)\n\nReturns\n-------\nr : rank-1 array('d') with bounds (m)\nc : rank-1 array('d') with bounds (n)\nrowcnd : float\ncolcnd : float\namax : float\ninfo : int\n"
    ...

def dgeequb(a) -> typing.Any:
    "r,c,rowcnd,colcnd,amax,info = dgeequb(a)\n\nWrapper for ``dgeequb``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (m,n)\n\nReturns\n-------\nr : rank-1 array('d') with bounds (m)\nc : rank-1 array('d') with bounds (n)\nrowcnd : float\ncolcnd : float\namax : float\ninfo : int\n"
    ...

def dgees(dselect, a, compute_v=..., sort_t=..., lwork=..., dselect_extra_args=..., overwrite_a=...) -> typing.Any:
    "t,sdim,wr,wi,vs,work,info = dgees(dselect,a,[compute_v,sort_t,lwork,dselect_extra_args,overwrite_a])\n\nWrapper for ``dgees``.\n\nParameters\n----------\ndselect : call-back function\na : input rank-2 array('d') with bounds (n,n)\n\nOther Parameters\n----------------\ncompute_v : input int, optional\n    Default: 1\nsort_t : input int, optional\n    Default: 0\ndselect_extra_args : input tuple, optional\n    Default: ()\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(3*n,1)\n\nReturns\n-------\nt : rank-2 array('d') with bounds (n,n) and a storage\nsdim : int\nwr : rank-1 array('d') with bounds (n)\nwi : rank-1 array('d') with bounds (n)\nvs : rank-2 array('d') with bounds (ldvs,n)\nwork : rank-1 array('d') with bounds (MAX(lwork,1))\ninfo : int\n\nNotes\n-----\nCall-back functions::\n\n  def dselect(arg1,arg2): return dselect\n  Required arguments:\n    arg1 : input float\n    arg2 : input float\n  Return objects:\n    dselect : int\n"
    ...

def dgeev(a, compute_vl=..., compute_vr=..., lwork=..., overwrite_a=...) -> typing.Any:
    "wr,wi,vl,vr,info = dgeev(a,[compute_vl,compute_vr,lwork,overwrite_a])\n\nWrapper for ``dgeev``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (n,n)\n\nOther Parameters\n----------------\ncompute_vl : input int, optional\n    Default: 1\ncompute_vr : input int, optional\n    Default: 1\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(4*n,1)\n\nReturns\n-------\nwr : rank-1 array('d') with bounds (n)\nwi : rank-1 array('d') with bounds (n)\nvl : rank-2 array('d') with bounds (ldvl,n)\nvr : rank-2 array('d') with bounds (ldvr,n)\ninfo : int\n"
    ...

def dgeev_lwork(n, compute_vl=..., compute_vr=...) -> typing.Any:
    'work,info = dgeev_lwork(n,[compute_vl,compute_vr])\n\nWrapper for ``dgeev_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\ncompute_vl : input int, optional\n    Default: 1\ncompute_vr : input int, optional\n    Default: 1\n\nReturns\n-------\nwork : float\ninfo : int\n'
    ...

def dgegv(*args, **kwds) -> typing.Any:
    "`dgegv` is deprecated!\nThe `*gegv` family of routines has been deprecated in\nLAPACK 3.6.0 in favor of the `*ggev` family of routines.\nThe corresponding wrappers will be removed from SciPy in\na future release.\n\nalphar,alphai,beta,vl,vr,info = dgegv(a,b,[compute_vl,compute_vr,lwork,overwrite_a,overwrite_b])\n\nWrapper for ``dgegv``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (n,n)\nb : input rank-2 array('d') with bounds (n,n)\n\nOther Parameters\n----------------\ncompute_vl : input int, optional\n    Default: 1\ncompute_vr : input int, optional\n    Default: 1\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(8*n,1)\n\nReturns\n-------\nalphar : rank-1 array('d') with bounds (n)\nalphai : rank-1 array('d') with bounds (n)\nbeta : rank-1 array('d') with bounds (n)\nvl : rank-2 array('d') with bounds (ldvl,n)\nvr : rank-2 array('d') with bounds (ldvr,n)\ninfo : int\n"
    ...

def dgehrd(a, lo=..., hi=..., lwork=..., overwrite_a=...) -> typing.Any:
    "ht,tau,info = dgehrd(a,[lo,hi,lwork,overwrite_a])\n\nWrapper for ``dgehrd``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (n,n)\n\nOther Parameters\n----------------\nlo : input int, optional\n    Default: 0\nhi : input int, optional\n    Default: n-1\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: MAX(n,1)\n\nReturns\n-------\nht : rank-2 array('d') with bounds (n,n) and a storage\ntau : rank-1 array('d') with bounds (n - 1)\ninfo : int\n"
    ...

def dgehrd_lwork(n, lo=..., hi=...) -> typing.Any:
    'work,info = dgehrd_lwork(n,[lo,hi])\n\nWrapper for ``dgehrd_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlo : input int, optional\n    Default: 0\nhi : input int, optional\n    Default: n-1\n\nReturns\n-------\nwork : float\ninfo : int\n'
    ...

def dgejsv(a, joba=..., jobu=..., jobv=..., jobr=..., jobt=..., jobp=..., lwork=..., overwrite_a=...) -> typing.Any:
    "sva,u,v,workout,iworkout,info = dgejsv(a,[joba,jobu,jobv,jobr,jobt,jobp,lwork,overwrite_a])\n\nWrapper for ``dgejsv``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (lda,n)\n\nOther Parameters\n----------------\njoba : input int, optional\n    Default: 4\njobu : input int, optional\n    Default: 0\njobv : input int, optional\n    Default: 0\njobr : input int, optional\n    Default: 1\njobt : input int, optional\n    Default: 0\njobp : input int, optional\n    Default: 1\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(6*n+2*n*n, max(2*m+n, max(4*n+n*n, max(2*n+n*n+6, 7))))\n\nReturns\n-------\nsva : rank-1 array('d') with bounds (n)\nu : rank-2 array('d') with bounds (((jobt == 0)&&(jobu == 3)?0:m),((jobt == 0)&&(jobu == 3)?0:(jobu == 1?m:n)))\nv : rank-2 array('d') with bounds (((jobt == 0)&&(jobv == 3)?0:ldv),((jobt == 0)&&(jobv == 3)?0:n))\nworkout : rank-1 array('d') with bounds (7)\niworkout : rank-1 array('i') with bounds (3)\ninfo : int\n"
    ...

def dgels(a, b, trans=..., lwork=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "lqr,x,info = dgels(a,b,[trans,lwork,overwrite_a,overwrite_b])\n\nWrapper for ``dgels``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (m,n)\nb : input rank-2 array('d') with bounds (MAX(m,n),nrhs)\n\nOther Parameters\n----------------\ntrans : input string(len=1), optional\n    Default: 'N'\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: MAX(MIN(m,n)+MAX(MIN(m,n),nrhs),1)\n\nReturns\n-------\nlqr : rank-2 array('d') with bounds (m,n) and a storage\nx : rank-2 array('d') with bounds (MAX(m,n),nrhs) and b storage\ninfo : int\n"
    ...

def dgels_lwork(m, n, nrhs, trans=...) -> typing.Any:
    "work,info = dgels_lwork(m,n,nrhs,[trans])\n\nWrapper for ``dgels_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\nnrhs : input int\n\nOther Parameters\n----------------\ntrans : input string(len=1), optional\n    Default: 'N'\n\nReturns\n-------\nwork : float\ninfo : int\n"
    ...

def dgelsd(a, b, lwork, size_iwork, cond=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "x,s,rank,info = dgelsd(a,b,lwork,size_iwork,[cond,overwrite_a,overwrite_b])\n\nWrapper for ``dgelsd``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (m,n)\nb : input rank-2 array('d') with bounds (maxmn,nrhs)\nlwork : input int\nsize_iwork : input int\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\ncond : input float, optional\n    Default: -1.0\n\nReturns\n-------\nx : rank-2 array('d') with bounds (maxmn,nrhs) and b storage\ns : rank-1 array('d') with bounds (minmn)\nrank : int\ninfo : int\n"
    ...

def dgelsd_lwork(m, n, nrhs, cond=..., lwork=...) -> typing.Any:
    'work,iwork,info = dgelsd_lwork(m,n,nrhs,[cond,lwork])\n\nWrapper for ``dgelsd_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\nnrhs : input int\n\nOther Parameters\n----------------\ncond : input float, optional\n    Default: -1.0\nlwork : input int, optional\n    Default: -1\n\nReturns\n-------\nwork : float\niwork : int\ninfo : int\n'
    ...

def dgelss(a, b, cond=..., lwork=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "v,x,s,rank,work,info = dgelss(a,b,[cond,lwork,overwrite_a,overwrite_b])\n\nWrapper for ``dgelss``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (m,n)\nb : input rank-2 array('d') with bounds (maxmn,nrhs)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\ncond : input float, optional\n    Default: -1.0\nlwork : input int, optional\n    Default: max(3*minmn+MAX(2*minmn,MAX(maxmn,nrhs)),1)\n\nReturns\n-------\nv : rank-2 array('d') with bounds (m,n) and a storage\nx : rank-2 array('d') with bounds (maxmn,nrhs) and b storage\ns : rank-1 array('d') with bounds (minmn)\nrank : int\nwork : rank-1 array('d') with bounds (MAX(lwork,1))\ninfo : int\n"
    ...

def dgelss_lwork(m, n, nrhs, cond=..., lwork=...) -> typing.Any:
    'work,info = dgelss_lwork(m,n,nrhs,[cond,lwork])\n\nWrapper for ``dgelss_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\nnrhs : input int\n\nOther Parameters\n----------------\ncond : input float, optional\n    Default: -1.0\nlwork : input int, optional\n    Default: -1\n\nReturns\n-------\nwork : float\ninfo : int\n'
    ...

def dgelsy(a, b, jptv, cond, lwork, overwrite_a=..., overwrite_b=...) -> typing.Any:
    "v,x,j,rank,info = dgelsy(a,b,jptv,cond,lwork,[overwrite_a,overwrite_b])\n\nWrapper for ``dgelsy``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (m,n)\nb : input rank-2 array('d') with bounds (maxmn,nrhs)\njptv : input rank-1 array('i') with bounds (n)\ncond : input float\nlwork : input int\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nv : rank-2 array('d') with bounds (m,n) and a storage\nx : rank-2 array('d') with bounds (maxmn,nrhs) and b storage\nj : rank-1 array('i') with bounds (n) and jptv storage\nrank : int\ninfo : int\n"
    ...

def dgelsy_lwork(m, n, nrhs, cond, lwork=...) -> typing.Any:
    'work,info = dgelsy_lwork(m,n,nrhs,cond,[lwork])\n\nWrapper for ``dgelsy_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\nnrhs : input int\ncond : input float\n\nOther Parameters\n----------------\nlwork : input int, optional\n    Default: -1\n\nReturns\n-------\nwork : float\ninfo : int\n'
    ...

def dgemqrt(v, t, c, side=..., trans=..., overwrite_c=...) -> typing.Any:
    "c,info = dgemqrt(v,t,c,[side,trans,overwrite_c])\n\nWrapper for ``dgemqrt``.\n\nParameters\n----------\nv : input rank-2 array('d') with bounds ((side[0]=='L'?m:n),k)\nt : input rank-2 array('d') with bounds (nb,k)\nc : input rank-2 array('d') with bounds (m,n)\n\nOther Parameters\n----------------\nside : input string(len=1), optional\n    Default: 'L'\ntrans : input string(len=1), optional\n    Default: 'N'\noverwrite_c : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('d') with bounds (m,n)\ninfo : int\n"
    ...

def dgeqp3(a, lwork=..., overwrite_a=...) -> typing.Any:
    "qr,jpvt,tau,work,info = dgeqp3(a,[lwork,overwrite_a])\n\nWrapper for ``dgeqp3``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(3*(n+1),1)\n\nReturns\n-------\nqr : rank-2 array('d') with bounds (m,n) and a storage\njpvt : rank-1 array('i') with bounds (n)\ntau : rank-1 array('d') with bounds (MIN(m,n))\nwork : rank-1 array('d') with bounds (MAX(lwork,1))\ninfo : int\n"
    ...

def dgeqrf(a, lwork=..., overwrite_a=...) -> typing.Any:
    "qr,tau,work,info = dgeqrf(a,[lwork,overwrite_a])\n\nWrapper for ``dgeqrf``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(3*n,1)\n\nReturns\n-------\nqr : rank-2 array('d') with bounds (m,n) and a storage\ntau : rank-1 array('d') with bounds (MIN(m,n))\nwork : rank-1 array('d') with bounds (MAX(lwork,1))\ninfo : int\n"
    ...

def dgeqrf_lwork(m, n) -> typing.Any:
    'work,info = dgeqrf_lwork(m,n)\n\nWrapper for ``dgeqrf_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\n\nReturns\n-------\nwork : float\ninfo : int\n'
    ...

def dgeqrfp(a, lwork=..., overwrite_a=...) -> typing.Any:
    "qr,tau,info = dgeqrfp(a,[lwork,overwrite_a])\n\nWrapper for ``dgeqrfp``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: MAX(1, n)\n\nReturns\n-------\nqr : rank-2 array('d') with bounds (m,n) and a storage\ntau : rank-1 array('d') with bounds (MIN(m,n))\ninfo : int\n"
    ...

def dgeqrfp_lwork(m, n) -> typing.Any:
    'work,info = dgeqrfp_lwork(m,n)\n\nWrapper for ``dgeqrfp_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\n\nReturns\n-------\nwork : float\ninfo : int\n'
    ...

def dgeqrt(nb, a, overwrite_a=...) -> typing.Any:
    "a,t,info = dgeqrt(nb,a,[overwrite_a])\n\nWrapper for ``dgeqrt``.\n\nParameters\n----------\nnb : input int\na : input rank-2 array('d') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\na : rank-2 array('d') with bounds (m,n)\nt : rank-2 array('d') with bounds (nb,MIN(m,n))\ninfo : int\n"
    ...

def dgerqf(a, lwork=..., overwrite_a=...) -> typing.Any:
    "qr,tau,work,info = dgerqf(a,[lwork,overwrite_a])\n\nWrapper for ``dgerqf``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(3*m,1)\n\nReturns\n-------\nqr : rank-2 array('d') with bounds (m,n) and a storage\ntau : rank-1 array('d') with bounds (MIN(m,n))\nwork : rank-1 array('d') with bounds (MAX(lwork,1))\ninfo : int\n"
    ...

def dgesc2(lu, rhs, ipiv, jpiv, overwrite_rhs=...) -> typing.Any:
    "x,scale = dgesc2(lu,rhs,ipiv,jpiv,[overwrite_rhs])\n\nWrapper for ``dgesc2``.\n\nParameters\n----------\nlu : input rank-2 array('d') with bounds (n,n)\nrhs : input rank-1 array('d') with bounds (n)\nipiv : input rank-1 array('i') with bounds (n)\njpiv : input rank-1 array('i') with bounds (n)\n\nOther Parameters\n----------------\noverwrite_rhs : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-1 array('d') with bounds (n) and rhs storage\nscale : float\n"
    ...

def dgesdd(a, compute_uv=..., full_matrices=..., lwork=..., overwrite_a=...) -> typing.Any:
    "u,s,vt,info = dgesdd(a,[compute_uv,full_matrices,lwork,overwrite_a])\n\nWrapper for ``dgesdd``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\ncompute_uv : input int, optional\n    Default: 1\nfull_matrices : input int, optional\n    Default: 1\nlwork : input int, optional\n    Default: max((compute_uv?4*minmn*minmn+MAX(m,n)+9*minmn:MAX(14*minmn+4,10*minmn+2+25*(25+8))+MAX(m,n)),1)\n\nReturns\n-------\nu : rank-2 array('d') with bounds (u0,u1)\ns : rank-1 array('d') with bounds (minmn)\nvt : rank-2 array('d') with bounds (vt0,vt1)\ninfo : int\n"
    ...

def dgesdd_lwork(m, n, compute_uv=..., full_matrices=...) -> typing.Any:
    'work,info = dgesdd_lwork(m,n,[compute_uv,full_matrices])\n\nWrapper for ``dgesdd_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\n\nOther Parameters\n----------------\ncompute_uv : input int, optional\n    Default: 1\nfull_matrices : input int, optional\n    Default: 1\n\nReturns\n-------\nwork : float\ninfo : int\n'
    ...

def dgesv(a, b, overwrite_a=..., overwrite_b=...) -> typing.Any:
    "lu,piv,x,info = dgesv(a,b,[overwrite_a,overwrite_b])\n\nWrapper for ``dgesv``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (n,n)\nb : input rank-2 array('d') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nlu : rank-2 array('d') with bounds (n,n) and a storage\npiv : rank-1 array('i') with bounds (n)\nx : rank-2 array('d') with bounds (n,nrhs) and b storage\ninfo : int\n"
    ...

def dgesvd(a, compute_uv=..., full_matrices=..., lwork=..., overwrite_a=...) -> typing.Any:
    "u,s,vt,info = dgesvd(a,[compute_uv,full_matrices,lwork,overwrite_a])\n\nWrapper for ``dgesvd``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\ncompute_uv : input int, optional\n    Default: 1\nfull_matrices : input int, optional\n    Default: 1\nlwork : input int, optional\n    Default: max(MAX(3*minmn+MAX(m,n),5*minmn),1)\n\nReturns\n-------\nu : rank-2 array('d') with bounds (u0,u1)\ns : rank-1 array('d') with bounds (minmn)\nvt : rank-2 array('d') with bounds (vt0,vt1)\ninfo : int\n"
    ...

def dgesvd_lwork(m, n, compute_uv=..., full_matrices=...) -> typing.Any:
    'work,info = dgesvd_lwork(m,n,[compute_uv,full_matrices])\n\nWrapper for ``dgesvd_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\n\nOther Parameters\n----------------\ncompute_uv : input int, optional\n    Default: 1\nfull_matrices : input int, optional\n    Default: 1\n\nReturns\n-------\nwork : float\ninfo : int\n'
    ...

def dgesvx(a, b, fact=..., trans=..., af=..., ipiv=..., equed=..., r=..., c=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "as,lu,ipiv,equed,rs,cs,bs,x,rcond,ferr,berr,info = dgesvx(a,b,[fact,trans,af,ipiv,equed,r,c,overwrite_a,overwrite_b])\n\nWrapper for ``dgesvx``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (n,n)\nb : input rank-2 array('d') with bounds (n,nrhs)\n\nOther Parameters\n----------------\nfact : input string(len=1), optional\n    Default: 'E'\ntrans : input string(len=1), optional\n    Default: 'N'\noverwrite_a : input int, optional\n    Default: 0\naf : input rank-2 array('d') with bounds (n,n)\nipiv : input rank-1 array('i') with bounds (n)\nequed : input string(len=1), optional\n    Default: 'B'\nr : input rank-1 array('d') with bounds (n)\nc : input rank-1 array('d') with bounds (n)\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nas : rank-2 array('d') with bounds (n,n) and a storage\nlu : rank-2 array('d') with bounds (n,n) and af storage\nipiv : rank-1 array('i') with bounds (n)\nequed : string(len=1)\nrs : rank-1 array('d') with bounds (n) and r storage\ncs : rank-1 array('d') with bounds (n) and c storage\nbs : rank-2 array('d') with bounds (n,nrhs) and b storage\nx : rank-2 array('d') with bounds (n,nrhs)\nrcond : float\nferr : rank-1 array('d') with bounds (nrhs)\nberr : rank-1 array('d') with bounds (nrhs)\ninfo : int\n"
    ...

def dgetc2(a, overwrite_a=...) -> typing.Any:
    "lu,ipiv,jpiv,info = dgetc2(a,[overwrite_a])\n\nWrapper for ``dgetc2``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\nlu : rank-2 array('d') with bounds (n,n) and a storage\nipiv : rank-1 array('i') with bounds (n)\njpiv : rank-1 array('i') with bounds (n)\ninfo : int\n"
    ...

def dgetrf(a, overwrite_a=...) -> typing.Any:
    "lu,piv,info = dgetrf(a,[overwrite_a])\n\nWrapper for ``dgetrf``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\nlu : rank-2 array('d') with bounds (m,n) and a storage\npiv : rank-1 array('i') with bounds (MIN(m,n))\ninfo : int\n"
    ...

def dgetri(lu, piv, lwork=..., overwrite_lu=...) -> typing.Any:
    "inv_a,info = dgetri(lu,piv,[lwork,overwrite_lu])\n\nWrapper for ``dgetri``.\n\nParameters\n----------\nlu : input rank-2 array('d') with bounds (n,n)\npiv : input rank-1 array('i') with bounds (n)\n\nOther Parameters\n----------------\noverwrite_lu : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(3*n,1)\n\nReturns\n-------\ninv_a : rank-2 array('d') with bounds (n,n) and lu storage\ninfo : int\n"
    ...

def dgetri_lwork(n) -> typing.Any:
    'work,info = dgetri_lwork(n)\n\nWrapper for ``dgetri_lwork``.\n\nParameters\n----------\nn : input int\n\nReturns\n-------\nwork : float\ninfo : int\n'
    ...

def dgetrs(lu, piv, b, trans=..., overwrite_b=...) -> typing.Any:
    "x,info = dgetrs(lu,piv,b,[trans,overwrite_b])\n\nWrapper for ``dgetrs``.\n\nParameters\n----------\nlu : input rank-2 array('d') with bounds (n,n)\npiv : input rank-1 array('i') with bounds (n)\nb : input rank-2 array('d') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_b : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('d') with bounds (n,nrhs) and b storage\ninfo : int\n"
    ...

def dgges(dselect, a, b, jobvsl=..., jobvsr=..., sort_t=..., ldvsl=..., ldvsr=..., lwork=..., dselect_extra_args=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "a,b,sdim,alphar,alphai,beta,vsl,vsr,work,info = dgges(dselect,a,b,[jobvsl,jobvsr,sort_t,ldvsl,ldvsr,lwork,dselect_extra_args,overwrite_a,overwrite_b])\n\nWrapper for ``dgges``.\n\nParameters\n----------\ndselect : call-back function\na : input rank-2 array('d') with bounds (lda,n)\nb : input rank-2 array('d') with bounds (ldb,n)\n\nOther Parameters\n----------------\njobvsl : input int, optional\n    Default: 1\njobvsr : input int, optional\n    Default: 1\nsort_t : input int, optional\n    Default: 0\ndselect_extra_args : input tuple, optional\n    Default: ()\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nldvsl : input int, optional\n    Default: ((jobvsl==1)?n:1)\nldvsr : input int, optional\n    Default: ((jobvsr==1)?n:1)\nlwork : input int, optional\n    Default: max(8*n+16,1)\n\nReturns\n-------\na : rank-2 array('d') with bounds (lda,n)\nb : rank-2 array('d') with bounds (ldb,n)\nsdim : int\nalphar : rank-1 array('d') with bounds (n)\nalphai : rank-1 array('d') with bounds (n)\nbeta : rank-1 array('d') with bounds (n)\nvsl : rank-2 array('d') with bounds (ldvsl,n)\nvsr : rank-2 array('d') with bounds (ldvsr,n)\nwork : rank-1 array('d') with bounds (MAX(lwork,1))\ninfo : int\n\nNotes\n-----\nCall-back functions::\n\n  def dselect(alphar,alphai,beta): return dselect\n  Required arguments:\n    alphar : input float\n    alphai : input float\n    beta : input float\n  Return objects:\n    dselect : int\n"
    ...

def dggev(a, b, compute_vl=..., compute_vr=..., lwork=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "alphar,alphai,beta,vl,vr,work,info = dggev(a,b,[compute_vl,compute_vr,lwork,overwrite_a,overwrite_b])\n\nWrapper for ``dggev``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (n,n)\nb : input rank-2 array('d') with bounds (n,n)\n\nOther Parameters\n----------------\ncompute_vl : input int, optional\n    Default: 1\ncompute_vr : input int, optional\n    Default: 1\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(8*n,1)\n\nReturns\n-------\nalphar : rank-1 array('d') with bounds (n)\nalphai : rank-1 array('d') with bounds (n)\nbeta : rank-1 array('d') with bounds (n)\nvl : rank-2 array('d') with bounds (ldvl,n)\nvr : rank-2 array('d') with bounds (ldvr,n)\nwork : rank-1 array('d') with bounds (MAX(lwork,1))\ninfo : int\n"
    ...

def dgglse(a, b, c, d, lwork=..., overwrite_a=..., overwrite_b=..., overwrite_c=..., overwrite_d=...) -> typing.Any:
    "t,r,res,x,info = dgglse(a,b,c,d,[lwork,overwrite_a,overwrite_b,overwrite_c,overwrite_d])\n\nWrapper for ``dgglse``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (m,n)\nb : input rank-2 array('d') with bounds (p,n)\nc : input rank-1 array('d') with bounds (m)\nd : input rank-1 array('d') with bounds (p)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\noverwrite_c : input int, optional\n    Default: 0\noverwrite_d : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(m+n+p,1)\n\nReturns\n-------\nt : rank-2 array('d') with bounds (m,n) and a storage\nr : rank-2 array('d') with bounds (p,n) and b storage\nres : rank-1 array('d') with bounds (m) and c storage\nx : rank-1 array('d') with bounds (n)\ninfo : int\n"
    ...

def dgglse_lwork(m, n, p) -> typing.Any:
    'work,info = dgglse_lwork(m,n,p)\n\nWrapper for ``dgglse_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\np : input int\n\nReturns\n-------\nwork : float\ninfo : int\n'
    ...

def dgtsv(dl, d, du, b, overwrite_dl=..., overwrite_d=..., overwrite_du=..., overwrite_b=...) -> typing.Any:
    "du2,d,du,x,info = dgtsv(dl,d,du,b,[overwrite_dl,overwrite_d,overwrite_du,overwrite_b])\n\nWrapper for ``dgtsv``.\n\nParameters\n----------\ndl : input rank-1 array('d') with bounds (n - 1)\nd : input rank-1 array('d') with bounds (n)\ndu : input rank-1 array('d') with bounds (n - 1)\nb : input rank-2 array('d') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_dl : input int, optional\n    Default: 0\noverwrite_d : input int, optional\n    Default: 0\noverwrite_du : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\ndu2 : rank-1 array('d') with bounds (n - 1) and dl storage\nd : rank-1 array('d') with bounds (n)\ndu : rank-1 array('d') with bounds (n - 1)\nx : rank-2 array('d') with bounds (n,nrhs) and b storage\ninfo : int\n"
    ...

def dgtsvx(dl, d, du, b, fact=..., trans=..., dlf=..., df=..., duf=..., du2=..., ipiv=...) -> typing.Any:
    "dlf,df,duf,du2,ipiv,x,rcond,ferr,berr,info = dgtsvx(dl,d,du,b,[fact,trans,dlf,df,duf,du2,ipiv])\n\nWrapper for ``dgtsvx``.\n\nParameters\n----------\ndl : input rank-1 array('d') with bounds (MAX(0, n-1))\nd : input rank-1 array('d') with bounds (n)\ndu : input rank-1 array('d') with bounds (MAX(0, n-1))\nb : input rank-2 array('d') with bounds (ldb,nrhs)\n\nOther Parameters\n----------------\nfact : input string(len=1), optional\n    Default: 'N'\ntrans : input string(len=1), optional\n    Default: 'N'\ndlf : input rank-1 array('d') with bounds (MAX(0,n-1))\ndf : input rank-1 array('d') with bounds (n)\nduf : input rank-1 array('d') with bounds (MAX(0,n-1))\ndu2 : input rank-1 array('d') with bounds (MAX(0,n-2))\nipiv : input rank-1 array('i') with bounds (n)\n\nReturns\n-------\ndlf : rank-1 array('d') with bounds (MAX(0,n-1))\ndf : rank-1 array('d') with bounds (n)\nduf : rank-1 array('d') with bounds (MAX(0,n-1))\ndu2 : rank-1 array('d') with bounds (MAX(0,n-2))\nipiv : rank-1 array('i') with bounds (n)\nx : rank-2 array('d') with bounds (ldx,nrhs)\nrcond : float\nferr : rank-1 array('d') with bounds (nrhs)\nberr : rank-1 array('d') with bounds (nrhs)\ninfo : int\n"
    ...

def dgttrf(dl, d, du, overwrite_dl=..., overwrite_d=..., overwrite_du=...) -> typing.Any:
    "dl,d,du,du2,ipiv,info = dgttrf(dl,d,du,[overwrite_dl,overwrite_d,overwrite_du])\n\nWrapper for ``dgttrf``.\n\nParameters\n----------\ndl : input rank-1 array('d') with bounds (n - 1)\nd : input rank-1 array('d') with bounds (n)\ndu : input rank-1 array('d') with bounds (n - 1)\n\nOther Parameters\n----------------\noverwrite_dl : input int, optional\n    Default: 0\noverwrite_d : input int, optional\n    Default: 0\noverwrite_du : input int, optional\n    Default: 0\n\nReturns\n-------\ndl : rank-1 array('d') with bounds (n - 1)\nd : rank-1 array('d') with bounds (n)\ndu : rank-1 array('d') with bounds (n - 1)\ndu2 : rank-1 array('d') with bounds (n - 2)\nipiv : rank-1 array('i') with bounds (n)\ninfo : int\n"
    ...

def dgttrs(dl, d, du, du2, ipiv, b, trans=..., overwrite_b=...) -> typing.Any:
    "x,info = dgttrs(dl,d,du,du2,ipiv,b,[trans,overwrite_b])\n\nWrapper for ``dgttrs``.\n\nParameters\n----------\ndl : input rank-1 array('d') with bounds (n - 1)\nd : input rank-1 array('d') with bounds (n)\ndu : input rank-1 array('d') with bounds (n - 1)\ndu2 : input rank-1 array('d') with bounds (n - 2)\nipiv : input rank-1 array('i') with bounds (n)\nb : input rank-2 array('d') with bounds (ldb,nrhs)\n\nOther Parameters\n----------------\ntrans : input string(len=1), optional\n    Default: 'N'\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('d') with bounds (ldb,nrhs) and b storage\ninfo : int\n"
    ...

def dlamch(cmach) -> typing.Any:
    'dlamch = dlamch(cmach)\n\nWrapper for ``dlamch``.\n\nParameters\n----------\ncmach : input string(len=1)\n\nReturns\n-------\ndlamch : float\n'
    ...

def dlange(norm, a) -> typing.Any:
    "n2 = dlange(norm,a)\n\nWrapper for ``dlange``.\n\nParameters\n----------\nnorm : input string(len=1)\na : input rank-2 array('d') with bounds (m,n)\n\nReturns\n-------\nn2 : float\n"
    ...

def dlarf(v, tau, c, work, side=..., incv=..., overwrite_c=...) -> typing.Any:
    "c = dlarf(v,tau,c,work,[side,incv,overwrite_c])\n\nWrapper for ``dlarf``.\n\nParameters\n----------\nv : input rank-1 array('d') with bounds ((side[0]=='L'?(1 + (m-1)*abs(incv)):(1 + (n-1)*abs(incv))))\ntau : input float\nc : input rank-2 array('d') with bounds (m,n)\nwork : input rank-1 array('d') with bounds (lwork)\n\nOther Parameters\n----------------\nside : input string(len=1), optional\n    Default: 'L'\nincv : input int, optional\n    Default: 1\noverwrite_c : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('d') with bounds (m,n)\n"
    ...

def dlarfg(n, alpha, x, incx=..., overwrite_x=...) -> typing.Any:
    "alpha,x,tau = dlarfg(n,alpha,x,[incx,overwrite_x])\n\nWrapper for ``dlarfg``.\n\nParameters\n----------\nn : input int\nalpha : input float\nx : input rank-1 array('d') with bounds (lx)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\n\nReturns\n-------\nalpha : float\nx : rank-1 array('d') with bounds (lx)\ntau : float\n"
    ...

def dlartg(f, g) -> typing.Any:
    'cs,sn,r = dlartg(f,g)\n\nWrapper for ``dlartg``.\n\nParameters\n----------\nf : input float\ng : input float\n\nReturns\n-------\ncs : float\nsn : float\nr : float\n'
    ...

def dlasd4(i, d, z, rho=...) -> typing.Any:
    "delta,sigma,work,info = dlasd4(i,d,z,[rho])\n\nWrapper for ``dlasd4``.\n\nParameters\n----------\ni : input int\nd : input rank-1 array('d') with bounds (n)\nz : input rank-1 array('d') with bounds (n)\n\nOther Parameters\n----------------\nrho : input float, optional\n    Default: 1.0\n\nReturns\n-------\ndelta : rank-1 array('d') with bounds (n)\nsigma : float\nwork : rank-1 array('d') with bounds (n)\ninfo : int\n"
    ...

def dlaswp(a, piv, k1=..., k2=..., off=..., inc=..., overwrite_a=...) -> typing.Any:
    "a = dlaswp(a,piv,[k1,k2,off,inc,overwrite_a])\n\nWrapper for ``dlaswp``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (nrows,n)\npiv : input rank-1 array('i') with bounds (npiv)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nk1 : input int, optional\n    Default: 0\nk2 : input int, optional\n    Default: npiv-1\noff : input int, optional\n    Default: 0\ninc : input int, optional\n    Default: 1\n\nReturns\n-------\na : rank-2 array('d') with bounds (nrows,n)\n"
    ...

def dlauum(c, lower=..., overwrite_c=...) -> typing.Any:
    "a,info = dlauum(c,[lower,overwrite_c])\n\nWrapper for ``dlauum``.\n\nParameters\n----------\nc : input rank-2 array('d') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_c : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\na : rank-2 array('d') with bounds (n,n) and c storage\ninfo : int\n"
    ...

def dorcsd(x11, x12, x21, x22, compute_u1=..., compute_u2=..., compute_v1t=..., compute_v2t=..., trans=..., signs=..., lwork=..., overwrite_x11=..., overwrite_x12=..., overwrite_x21=..., overwrite_x22=...) -> typing.Any:
    "cs11,cs12,cs21,cs22,theta,u1,u2,v1t,v2t,info = dorcsd(x11,x12,x21,x22,[compute_u1,compute_u2,compute_v1t,compute_v2t,trans,signs,lwork,overwrite_x11,overwrite_x12,overwrite_x21,overwrite_x22])\n\nWrapper for ``dorcsd``.\n\nParameters\n----------\nx11 : input rank-2 array('d') with bounds (p,q)\nx12 : input rank-2 array('d') with bounds (p,mmq)\nx21 : input rank-2 array('d') with bounds (mmp,q)\nx22 : input rank-2 array('d') with bounds (mmp,mmq)\n\nOther Parameters\n----------------\ncompute_u1 : input int, optional\n    Default: 1\ncompute_u2 : input int, optional\n    Default: 1\ncompute_v1t : input int, optional\n    Default: 1\ncompute_v2t : input int, optional\n    Default: 1\ntrans : input int, optional\n    Default: 0\nsigns : input int, optional\n    Default: 0\noverwrite_x11 : input int, optional\n    Default: 0\noverwrite_x12 : input int, optional\n    Default: 0\noverwrite_x21 : input int, optional\n    Default: 0\noverwrite_x22 : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: 2+2*m+5*MAX(1,q-1)+4*MAX(1,q)+8*q\n\nReturns\n-------\ncs11 : rank-2 array('d') with bounds (p,q) and x11 storage\ncs12 : rank-2 array('d') with bounds (p,mmq) and x12 storage\ncs21 : rank-2 array('d') with bounds (mmp,q) and x21 storage\ncs22 : rank-2 array('d') with bounds (mmp,mmq) and x22 storage\ntheta : rank-1 array('d') with bounds (min(min(p,mmp),min(q,mmq)))\nu1 : rank-2 array('d') with bounds ((compute_u1?p:0),(compute_u1?p:0))\nu2 : rank-2 array('d') with bounds ((compute_u2?mmp:0),(compute_u2?mmp:0))\nv1t : rank-2 array('d') with bounds ((compute_v1t?q:0),(compute_v1t?q:0))\nv2t : rank-2 array('d') with bounds ((compute_v2t?mmq:0),(compute_v2t?mmq:0))\ninfo : int\n"
    ...

def dorcsd_lwork(m, p, q) -> typing.Any:
    'work,info = dorcsd_lwork(m,p,q)\n\nWrapper for ``dorcsd_lwork``.\n\nParameters\n----------\nm : input int\np : input int\nq : input int\n\nReturns\n-------\nwork : float\ninfo : int\n'
    ...

def dorghr(a, tau, lo=..., hi=..., lwork=..., overwrite_a=...) -> typing.Any:
    "ht,info = dorghr(a,tau,[lo,hi,lwork,overwrite_a])\n\nWrapper for ``dorghr``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (n,n)\ntau : input rank-1 array('d') with bounds (n - 1)\n\nOther Parameters\n----------------\nlo : input int, optional\n    Default: 0\nhi : input int, optional\n    Default: n-1\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(hi-lo,1)\n\nReturns\n-------\nht : rank-2 array('d') with bounds (n,n) and a storage\ninfo : int\n"
    ...

def dorghr_lwork(n, lo=..., hi=...) -> typing.Any:
    'work,info = dorghr_lwork(n,[lo,hi])\n\nWrapper for ``dorghr_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlo : input int, optional\n    Default: 0\nhi : input int, optional\n    Default: n-1\n\nReturns\n-------\nwork : float\ninfo : int\n'
    ...

def dorgqr(a, tau, lwork=..., overwrite_a=...) -> typing.Any:
    "q,work,info = dorgqr(a,tau,[lwork,overwrite_a])\n\nWrapper for ``dorgqr``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (m,n)\ntau : input rank-1 array('d') with bounds (k)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(3*n,1)\n\nReturns\n-------\nq : rank-2 array('d') with bounds (m,n) and a storage\nwork : rank-1 array('d') with bounds (MAX(lwork,1))\ninfo : int\n"
    ...

def dorgrq(a, tau, lwork=..., overwrite_a=...) -> typing.Any:
    "q,work,info = dorgrq(a,tau,[lwork,overwrite_a])\n\nWrapper for ``dorgrq``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (m,n)\ntau : input rank-1 array('d') with bounds (k)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(3*m,1)\n\nReturns\n-------\nq : rank-2 array('d') with bounds (m,n) and a storage\nwork : rank-1 array('d') with bounds (MAX(lwork,1))\ninfo : int\n"
    ...

def dormqr(side, trans, a, tau, c, lwork, overwrite_c=...) -> typing.Any:
    "cq,work,info = dormqr(side,trans,a,tau,c,lwork,[overwrite_c])\n\nWrapper for ``dormqr``.\n\nParameters\n----------\nside : input string(len=1)\ntrans : input string(len=1)\na : input rank-2 array('d') with bounds (lda,k)\ntau : input rank-1 array('d') with bounds (k)\nc : input rank-2 array('d') with bounds (ldc,n)\nlwork : input int\n\nOther Parameters\n----------------\noverwrite_c : input int, optional\n    Default: 0\n\nReturns\n-------\ncq : rank-2 array('d') with bounds (ldc,n) and c storage\nwork : rank-1 array('d') with bounds (MAX(lwork,1))\ninfo : int\n"
    ...

def dormrz(a, tau, c, side=..., trans=..., lwork=..., overwrite_c=...) -> typing.Any:
    "cq,info = dormrz(a,tau,c,[side,trans,lwork,overwrite_c])\n\nWrapper for ``dormrz``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (k,nt)\ntau : input rank-1 array('d') with bounds (k)\nc : input rank-2 array('d') with bounds (m,n)\n\nOther Parameters\n----------------\nside : input string(len=1), optional\n    Default: 'L'\ntrans : input string(len=1), optional\n    Default: 'N'\noverwrite_c : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: MAX((side[0]=='L'?n:m),1)\n\nReturns\n-------\ncq : rank-2 array('d') with bounds (m,n) and c storage\ninfo : int\n"
    ...

def dormrz_lwork(m, n, side=..., trans=...) -> typing.Any:
    "work,info = dormrz_lwork(m,n,[side,trans])\n\nWrapper for ``dormrz_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\n\nOther Parameters\n----------------\nside : input string(len=1), optional\n    Default: 'L'\ntrans : input string(len=1), optional\n    Default: 'N'\n\nReturns\n-------\nwork : float\ninfo : int\n"
    ...

def dpbsv(ab, b, lower=..., ldab=..., overwrite_ab=..., overwrite_b=...) -> typing.Any:
    "c,x,info = dpbsv(ab,b,[lower,ldab,overwrite_ab,overwrite_b])\n\nWrapper for ``dpbsv``.\n\nParameters\n----------\nab : input rank-2 array('d') with bounds (ldab,n)\nb : input rank-2 array('d') with bounds (ldb,nrhs)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\noverwrite_ab : input int, optional\n    Default: 0\nldab : input int, optional\n    Default: shape(ab,0)\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('d') with bounds (ldab,n) and ab storage\nx : rank-2 array('d') with bounds (ldb,nrhs) and b storage\ninfo : int\n"
    ...

def dpbtrf(ab, lower=..., ldab=..., overwrite_ab=...) -> typing.Any:
    "c,info = dpbtrf(ab,[lower,ldab,overwrite_ab])\n\nWrapper for ``dpbtrf``.\n\nParameters\n----------\nab : input rank-2 array('d') with bounds (ldab,n)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\noverwrite_ab : input int, optional\n    Default: 0\nldab : input int, optional\n    Default: shape(ab,0)\n\nReturns\n-------\nc : rank-2 array('d') with bounds (ldab,n) and ab storage\ninfo : int\n"
    ...

def dpbtrs(ab, b, lower=..., ldab=..., overwrite_b=...) -> typing.Any:
    "x,info = dpbtrs(ab,b,[lower,ldab,overwrite_b])\n\nWrapper for ``dpbtrs``.\n\nParameters\n----------\nab : input rank-2 array('d') with bounds (ldab,n)\nb : input rank-2 array('d') with bounds (ldb,nrhs)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\nldab : input int, optional\n    Default: shape(ab,0)\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('d') with bounds (ldb,nrhs) and b storage\ninfo : int\n"
    ...

def dpftrf(n, a, transr=..., uplo=..., overwrite_a=...) -> typing.Any:
    "achol,info = dpftrf(n,a,[transr,uplo,overwrite_a])\n\nWrapper for ``dpftrf``.\n\nParameters\n----------\nn : input int\na : input rank-1 array('d') with bounds (nt)\n\nOther Parameters\n----------------\ntransr : input string(len=1), optional\n    Default: 'N'\nuplo : input string(len=1), optional\n    Default: 'U'\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\nachol : rank-1 array('d') with bounds (nt) and a storage\ninfo : int\n"
    ...

def dpftri(n, a, transr=..., uplo=..., overwrite_a=...) -> typing.Any:
    "ainv,info = dpftri(n,a,[transr,uplo,overwrite_a])\n\nWrapper for ``dpftri``.\n\nParameters\n----------\nn : input int\na : input rank-1 array('d') with bounds (nt)\n\nOther Parameters\n----------------\ntransr : input string(len=1), optional\n    Default: 'N'\nuplo : input string(len=1), optional\n    Default: 'U'\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\nainv : rank-1 array('d') with bounds (nt) and a storage\ninfo : int\n"
    ...

def dpftrs(n, a, b, transr=..., uplo=..., overwrite_b=...) -> typing.Any:
    "x,info = dpftrs(n,a,b,[transr,uplo,overwrite_b])\n\nWrapper for ``dpftrs``.\n\nParameters\n----------\nn : input int\na : input rank-1 array('d') with bounds (nt)\nb : input rank-2 array('d') with bounds (ldb,nhrs)\n\nOther Parameters\n----------------\ntransr : input string(len=1), optional\n    Default: 'N'\nuplo : input string(len=1), optional\n    Default: 'U'\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('d') with bounds (ldb,nhrs) and b storage\ninfo : int\n"
    ...

def dpocon(a, anorm, uplo=...) -> typing.Any:
    "rcond,info = dpocon(a,anorm,[uplo])\n\nWrapper for ``dpocon``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (n,n)\nanorm : input float\n\nOther Parameters\n----------------\nuplo : input string(len=1), optional\n    Default: 'U'\n\nReturns\n-------\nrcond : float\ninfo : int\n"
    ...

def dposv(a, b, lower=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "c,x,info = dposv(a,b,[lower,overwrite_a,overwrite_b])\n\nWrapper for ``dposv``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (n,n)\nb : input rank-2 array('d') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('d') with bounds (n,n) and a storage\nx : rank-2 array('d') with bounds (n,nrhs) and b storage\ninfo : int\n"
    ...

def dposvx(a, b, fact=..., af=..., equed=..., s=..., lower=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "a_s,lu,equed,s,b_s,x,rcond,ferr,berr,info = dposvx(a,b,[fact,af,equed,s,lower,overwrite_a,overwrite_b])\n\nWrapper for ``dposvx``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (n,n)\nb : input rank-2 array('d') with bounds (n,nrhs)\n\nOther Parameters\n----------------\nfact : input string(len=1), optional\n    Default: 'E'\noverwrite_a : input int, optional\n    Default: 0\naf : input rank-2 array('d') with bounds (n,n)\nequed : input string(len=1), optional\n    Default: 'Y'\ns : input rank-1 array('d') with bounds (n)\noverwrite_b : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\na_s : rank-2 array('d') with bounds (n,n) and a storage\nlu : rank-2 array('d') with bounds (n,n) and af storage\nequed : string(len=1)\ns : rank-1 array('d') with bounds (n)\nb_s : rank-2 array('d') with bounds (n,nrhs) and b storage\nx : rank-2 array('d') with bounds (n,nrhs)\nrcond : float\nferr : rank-1 array('d') with bounds (nrhs)\nberr : rank-1 array('d') with bounds (nrhs)\ninfo : int\n"
    ...

def dpotrf(a, lower=..., clean=..., overwrite_a=...) -> typing.Any:
    "c,info = dpotrf(a,[lower,clean,overwrite_a])\n\nWrapper for ``dpotrf``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\nclean : input int, optional\n    Default: 1\n\nReturns\n-------\nc : rank-2 array('d') with bounds (n,n) and a storage\ninfo : int\n"
    ...

def dpotri(c, lower=..., overwrite_c=...) -> typing.Any:
    "inv_a,info = dpotri(c,[lower,overwrite_c])\n\nWrapper for ``dpotri``.\n\nParameters\n----------\nc : input rank-2 array('d') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_c : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\ninv_a : rank-2 array('d') with bounds (n,n) and c storage\ninfo : int\n"
    ...

def dpotrs(c, b, lower=..., overwrite_b=...) -> typing.Any:
    "x,info = dpotrs(c,b,[lower,overwrite_b])\n\nWrapper for ``dpotrs``.\n\nParameters\n----------\nc : input rank-2 array('d') with bounds (n,n)\nb : input rank-2 array('d') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_b : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('d') with bounds (n,nrhs) and b storage\ninfo : int\n"
    ...

def dppcon(n, ap, anorm, lower=...) -> typing.Any:
    "rcond,info = dppcon(n,ap,anorm,[lower])\n\nWrapper for ``dppcon``.\n\nParameters\n----------\nn : input int\nap : input rank-1 array('d') with bounds (L)\nanorm : input float\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nrcond : float\ninfo : int\n"
    ...

def dppsv(n, ap, b, lower=..., overwrite_b=...) -> typing.Any:
    "x,info = dppsv(n,ap,b,[lower,overwrite_b])\n\nWrapper for ``dppsv``.\n\nParameters\n----------\nn : input int\nap : input rank-1 array('d') with bounds (L)\nb : input rank-2 array('d') with bounds (ldb,nrhs)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('d') with bounds (ldb,nrhs) and b storage\ninfo : int\n"
    ...

def dpptrf(n, ap, lower=..., overwrite_ap=...) -> typing.Any:
    "ul,info = dpptrf(n,ap,[lower,overwrite_ap])\n\nWrapper for ``dpptrf``.\n\nParameters\n----------\nn : input int\nap : input rank-1 array('d') with bounds (L)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\noverwrite_ap : input int, optional\n    Default: 0\n\nReturns\n-------\nul : rank-1 array('d') with bounds (L) and ap storage\ninfo : int\n"
    ...

def dpptri(n, ap, lower=..., overwrite_ap=...) -> typing.Any:
    "uli,info = dpptri(n,ap,[lower,overwrite_ap])\n\nWrapper for ``dpptri``.\n\nParameters\n----------\nn : input int\nap : input rank-1 array('d') with bounds (L)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\noverwrite_ap : input int, optional\n    Default: 0\n\nReturns\n-------\nuli : rank-1 array('d') with bounds (L) and ap storage\ninfo : int\n"
    ...

def dpptrs(n, ap, b, lower=..., overwrite_b=...) -> typing.Any:
    "x,info = dpptrs(n,ap,b,[lower,overwrite_b])\n\nWrapper for ``dpptrs``.\n\nParameters\n----------\nn : input int\nap : input rank-1 array('d') with bounds (L)\nb : input rank-2 array('d') with bounds (ldb,nrhs)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('d') with bounds (ldb,nrhs) and b storage\ninfo : int\n"
    ...

def dpstf2(a, tol=..., lower=..., overwrite_a=...) -> typing.Any:
    "c,piv,rank_c,info = dpstf2(a,[tol,lower,overwrite_a])\n\nWrapper for ``dpstf2``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\ntol : input float, optional\n    Default: -1.0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('d') with bounds (n,n) and a storage\npiv : rank-1 array('i') with bounds (n)\nrank_c : int\ninfo : int\n"
    ...

def dpstrf(a, tol=..., lower=..., overwrite_a=...) -> typing.Any:
    "c,piv,rank_c,info = dpstrf(a,[tol,lower,overwrite_a])\n\nWrapper for ``dpstrf``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\ntol : input float, optional\n    Default: -1.0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('d') with bounds (n,n) and a storage\npiv : rank-1 array('i') with bounds (n)\nrank_c : int\ninfo : int\n"
    ...

def dpteqr(d, e, z, compute_z=..., overwrite_d=..., overwrite_e=..., overwrite_z=...) -> typing.Any:
    "d,e,z,info = dpteqr(d,e,z,[compute_z,overwrite_d,overwrite_e,overwrite_z])\n\nWrapper for ``dpteqr``.\n\nParameters\n----------\nd : input rank-1 array('d') with bounds (n)\ne : input rank-1 array('d') with bounds ((n>0?n-1:0))\nz : input rank-2 array('d') with bounds ((compute_z==0?shape(z, 0):max(1,n)),(compute_z==0?shape(z, 1):n))\n\nOther Parameters\n----------------\ncompute_z : input int, optional\n    Default: 0\noverwrite_d : input int, optional\n    Default: 0\noverwrite_e : input int, optional\n    Default: 0\noverwrite_z : input int, optional\n    Default: 0\n\nReturns\n-------\nd : rank-1 array('d') with bounds (n)\ne : rank-1 array('d') with bounds ((n>0?n-1:0))\nz : rank-2 array('d') with bounds ((compute_z==0?shape(z, 0):max(1,n)),(compute_z==0?shape(z, 1):n))\ninfo : int\n"
    ...

def dptsv(d, e, b, overwrite_d=..., overwrite_e=..., overwrite_b=...) -> typing.Any:
    "d,du,x,info = dptsv(d,e,b,[overwrite_d,overwrite_e,overwrite_b])\n\nWrapper for ``dptsv``.\n\nParameters\n----------\nd : input rank-1 array('d') with bounds (n)\ne : input rank-1 array('d') with bounds (n - 1)\nb : input rank-2 array('d') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_d : input int, optional\n    Default: 0\noverwrite_e : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nd : rank-1 array('d') with bounds (n)\ndu : rank-1 array('d') with bounds (n - 1) and e storage\nx : rank-2 array('d') with bounds (n,nrhs) and b storage\ninfo : int\n"
    ...

def dptsvx(d, e, b, fact=..., df=..., ef=...) -> typing.Any:
    "df,ef,x,rcond,ferr,berr,info = dptsvx(d,e,b,[fact,df,ef])\n\nWrapper for ``dptsvx``.\n\nParameters\n----------\nd : input rank-1 array('d') with bounds (n)\ne : input rank-1 array('d') with bounds (max(0, n-1))\nb : input rank-2 array('d') with bounds (ldb,nrhs)\n\nOther Parameters\n----------------\nfact : input string(len=1), optional\n    Default: 'N'\ndf : input rank-1 array('d') with bounds (n)\nef : input rank-1 array('d') with bounds (max(0, n-1))\n\nReturns\n-------\ndf : rank-1 array('d') with bounds (n)\nef : rank-1 array('d') with bounds (max(0, n-1))\nx : rank-2 array('d') with bounds (ldx,nrhs)\nrcond : float\nferr : rank-1 array('d') with bounds (nrhs)\nberr : rank-1 array('d') with bounds (nrhs)\ninfo : int\n"
    ...

def dpttrf(d, e, overwrite_d=..., overwrite_e=...) -> typing.Any:
    "d,e,info = dpttrf(d,e,[overwrite_d,overwrite_e])\n\nWrapper for ``dpttrf``.\n\nParameters\n----------\nd : input rank-1 array('d') with bounds (n)\ne : input rank-1 array('d') with bounds ((n>0?n-1:0))\n\nOther Parameters\n----------------\noverwrite_d : input int, optional\n    Default: 0\noverwrite_e : input int, optional\n    Default: 0\n\nReturns\n-------\nd : rank-1 array('d') with bounds (n)\ne : rank-1 array('d') with bounds ((n>0?n-1:0))\ninfo : int\n"
    ...

def dpttrs(d, e, b, overwrite_b=...) -> typing.Any:
    "x,info = dpttrs(d,e,b,[overwrite_b])\n\nWrapper for ``dpttrs``.\n\nParameters\n----------\nd : input rank-1 array('d') with bounds (n)\ne : input rank-1 array('d') with bounds ((n>0?n-1:0))\nb : input rank-2 array('d') with bounds (ldb,nrhs)\n\nOther Parameters\n----------------\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('d') with bounds (ldb,nrhs) and b storage\ninfo : int\n"
    ...

def dsbev(ab, compute_v=..., lower=..., ldab=..., overwrite_ab=...) -> typing.Any:
    "w,z,info = dsbev(ab,[compute_v,lower,ldab,overwrite_ab])\n\nWrapper for ``dsbev``.\n\nParameters\n----------\nab : input rank-2 array('d') with bounds (ldab,n)\n\nOther Parameters\n----------------\noverwrite_ab : input int, optional\n    Default: 1\ncompute_v : input int, optional\n    Default: 1\nlower : input int, optional\n    Default: 0\nldab : input int, optional\n    Default: shape(ab,0)\n\nReturns\n-------\nw : rank-1 array('d') with bounds (n)\nz : rank-2 array('d') with bounds (ldz,ldz)\ninfo : int\n"
    ...

def dsbevd(ab, compute_v=..., lower=..., ldab=..., liwork=..., overwrite_ab=...) -> typing.Any:
    "w,z,info = dsbevd(ab,[compute_v,lower,ldab,liwork,overwrite_ab])\n\nWrapper for ``dsbevd``.\n\nParameters\n----------\nab : input rank-2 array('d') with bounds (ldab,n)\n\nOther Parameters\n----------------\noverwrite_ab : input int, optional\n    Default: 1\ncompute_v : input int, optional\n    Default: 1\nlower : input int, optional\n    Default: 0\nldab : input int, optional\n    Default: shape(ab,0)\nliwork : input int, optional\n    Default: (compute_v?3+5*n:1)\n\nReturns\n-------\nw : rank-1 array('d') with bounds (n)\nz : rank-2 array('d') with bounds (ldz,ldz)\ninfo : int\n"
    ...

def dsbevx(ab, vl, vu, il, iu, ldab=..., compute_v=..., range=..., lower=..., abstol=..., mmax=..., overwrite_ab=...) -> typing.Any:
    "w,z,m,ifail,info = dsbevx(ab,vl,vu,il,iu,[ldab,compute_v,range,lower,abstol,mmax,overwrite_ab])\n\nWrapper for ``dsbevx``.\n\nParameters\n----------\nab : input rank-2 array('d') with bounds (ldab,n)\nvl : input float\nvu : input float\nil : input int\niu : input int\n\nOther Parameters\n----------------\noverwrite_ab : input int, optional\n    Default: 1\nldab : input int, optional\n    Default: shape(ab,0)\ncompute_v : input int, optional\n    Default: 1\nrange : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\nabstol : input float, optional\n    Default: 0.0\nmmax : input int, optional\n    Default: (compute_v?(range==2?(iu-il+1):n):1)\n\nReturns\n-------\nw : rank-1 array('d') with bounds (n)\nz : rank-2 array('d') with bounds (ldz,mmax)\nm : int\nifail : rank-1 array('i') with bounds ((compute_v?n:1))\ninfo : int\n"
    ...

def dsfrk(n, k, alpha, a, beta, c, transr=..., uplo=..., trans=..., overwrite_c=...) -> typing.Any:
    "cout = dsfrk(n,k,alpha,a,beta,c,[transr,uplo,trans,overwrite_c])\n\nWrapper for ``dsfrk``.\n\nParameters\n----------\nn : input int\nk : input int\nalpha : input float\na : input rank-2 array('d') with bounds (lda,ka)\nbeta : input float\nc : input rank-1 array('d') with bounds (nt)\n\nOther Parameters\n----------------\ntransr : input string(len=1), optional\n    Default: 'N'\nuplo : input string(len=1), optional\n    Default: 'U'\ntrans : input string(len=1), optional\n    Default: 'N'\noverwrite_c : input int, optional\n    Default: 0\n\nReturns\n-------\ncout : rank-1 array('d') with bounds (nt) and c storage\n"
    ...

def dstebz(d, e, range, vl, vu, il, iu, tol, order) -> typing.Any:
    "m,w,iblock,isplit,info = dstebz(d,e,range,vl,vu,il,iu,tol,order)\n\nWrapper for ``dstebz``.\n\nParameters\n----------\nd : input rank-1 array('d') with bounds (n)\ne : input rank-1 array('d') with bounds (n - 1)\nrange : input int\nvl : input float\nvu : input float\nil : input int\niu : input int\ntol : input float\norder : input string(len=1)\n\nReturns\n-------\nm : int\nw : rank-1 array('d') with bounds (n)\niblock : rank-1 array('i') with bounds (n)\nisplit : rank-1 array('i') with bounds (n)\ninfo : int\n"
    ...

def dstein(d, e, w, iblock, isplit) -> typing.Any:
    "z,info = dstein(d,e,w,iblock,isplit)\n\nWrapper for ``dstein``.\n\nParameters\n----------\nd : input rank-1 array('d') with bounds (n)\ne : input rank-1 array('d') with bounds (n - 1)\nw : input rank-1 array('d') with bounds (m)\niblock : input rank-1 array('i') with bounds (n)\nisplit : input rank-1 array('i') with bounds (n)\n\nReturns\n-------\nz : rank-2 array('d') with bounds (ldz,m)\ninfo : int\n"
    ...

def dstemr(d, e, range, vl, vu, il, iu, compute_v=..., lwork=..., liwork=..., overwrite_d=...) -> typing.Any:
    "m,w,z,info = dstemr(d,e,range,vl,vu,il,iu,[compute_v,lwork,liwork,overwrite_d])\n\nWrapper for ``dstemr``.\n\nParameters\n----------\nd : input rank-1 array('d') with bounds (n)\ne : input rank-1 array('d') with bounds (n)\nrange : input int\nvl : input float\nvu : input float\nil : input int\niu : input int\n\nOther Parameters\n----------------\noverwrite_d : input int, optional\n    Default: 0\ncompute_v : input int, optional\n    Default: 1\nlwork : input int, optional\n    Default: max((compute_v?18*n:12*n),1)\nliwork : input int, optional\n    Default: (compute_v?10*n:8*n)\n\nReturns\n-------\nm : int\nw : rank-1 array('d') with bounds (n)\nz : rank-2 array('d') with bounds (n,n)\ninfo : int\n"
    ...

def dstemr_lwork(d, e, range, vl, vu, il, iu, compute_v=..., overwrite_d=..., overwrite_e=...) -> typing.Any:
    "work,iwork,info = dstemr_lwork(d,e,range,vl,vu,il,iu,[compute_v,overwrite_d,overwrite_e])\n\nWrapper for ``dstemr_lwork``.\n\nParameters\n----------\nd : input rank-1 array('d') with bounds (n)\ne : input rank-1 array('d') with bounds (n)\nrange : input int\nvl : input float\nvu : input float\nil : input int\niu : input int\n\nOther Parameters\n----------------\noverwrite_d : input int, optional\n    Default: 0\noverwrite_e : input int, optional\n    Default: 0\ncompute_v : input int, optional\n    Default: 1\n\nReturns\n-------\nwork : float\niwork : int\ninfo : int\n"
    ...

def dsterf(d, e, overwrite_d=..., overwrite_e=...) -> typing.Any:
    "vals,info = dsterf(d,e,[overwrite_d,overwrite_e])\n\nWrapper for ``dsterf``.\n\nParameters\n----------\nd : input rank-1 array('d') with bounds (n)\ne : input rank-1 array('d') with bounds (n - 1)\n\nOther Parameters\n----------------\noverwrite_d : input int, optional\n    Default: 0\noverwrite_e : input int, optional\n    Default: 0\n\nReturns\n-------\nvals : rank-1 array('d') with bounds (n) and d storage\ninfo : int\n"
    ...

def dstev(d, e, compute_v=..., overwrite_d=..., overwrite_e=...) -> typing.Any:
    "vals,z,info = dstev(d,e,[compute_v,overwrite_d,overwrite_e])\n\nWrapper for ``dstev``.\n\nParameters\n----------\nd : input rank-1 array('d') with bounds (n)\ne : input rank-1 array('d') with bounds (MAX(n-1,1))\n\nOther Parameters\n----------------\noverwrite_d : input int, optional\n    Default: 0\noverwrite_e : input int, optional\n    Default: 0\ncompute_v : input int, optional\n    Default: 1\n\nReturns\n-------\nvals : rank-1 array('d') with bounds (n) and d storage\nz : rank-2 array('d') with bounds (ldz,(compute_v?n:1))\ninfo : int\n"
    ...

def dsycon(a, ipiv, anorm, lower=...) -> typing.Any:
    "rcond,info = dsycon(a,ipiv,anorm,[lower])\n\nWrapper for ``dsycon``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (n,n)\nipiv : input rank-1 array('i') with bounds (n)\nanorm : input float\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nrcond : float\ninfo : int\n"
    ...

def dsyconv(a, ipiv, lower=..., way=..., overwrite_a=...) -> typing.Any:
    "a,e,info = dsyconv(a,ipiv,[lower,way,overwrite_a])\n\nWrapper for ``dsyconv``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (n,n)\nipiv : input rank-1 array('i') with bounds (n)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\nway : input int, optional\n    Default: 0\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\na : rank-2 array('d') with bounds (n,n)\ne : rank-1 array('d') with bounds (n)\ninfo : int\n"
    ...

def dsyequb(a, lower=...) -> typing.Any:
    "s,scond,amax,info = dsyequb(a,[lower])\n\nWrapper for ``dsyequb``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (lda,n)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\ns : rank-1 array('d') with bounds (n)\nscond : float\namax : float\ninfo : int\n"
    ...

def dsyev(a, compute_v=..., lower=..., lwork=..., overwrite_a=...) -> typing.Any:
    "w,v,info = dsyev(a,[compute_v,lower,lwork,overwrite_a])\n\nWrapper for ``dsyev``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (n,n)\n\nOther Parameters\n----------------\ncompute_v : input int, optional\n    Default: 1\nlower : input int, optional\n    Default: 0\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(3*n-1,1)\n\nReturns\n-------\nw : rank-1 array('d') with bounds (n)\nv : rank-2 array('d') with bounds (n,n) and a storage\ninfo : int\n"
    ...

def dsyev_lwork(n, lower=...) -> typing.Any:
    'work,info = dsyev_lwork(n,[lower])\n\nWrapper for ``dsyev_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nwork : float\ninfo : int\n'
    ...

def dsyevd(a, compute_v=..., lower=..., lwork=..., liwork=..., overwrite_a=...) -> typing.Any:
    "w,v,info = dsyevd(a,[compute_v,lower,lwork,liwork,overwrite_a])\n\nWrapper for ``dsyevd``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (n,n)\n\nOther Parameters\n----------------\ncompute_v : input int, optional\n    Default: 1\nlower : input int, optional\n    Default: 0\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max((compute_v?1+6*n+2*n*n:2*n+1),1)\nliwork : input int, optional\n    Default: (compute_v?3+5*n:1)\n\nReturns\n-------\nw : rank-1 array('d') with bounds (n)\nv : rank-2 array('d') with bounds (n,n) and a storage\ninfo : int\n"
    ...

def dsyevd_lwork(n, compute_v=..., lower=...) -> typing.Any:
    'work,iwork,info = dsyevd_lwork(n,[compute_v,lower])\n\nWrapper for ``dsyevd_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\ncompute_v : input int, optional\n    Default: 1\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nwork : float\niwork : int\ninfo : int\n'
    ...

def dsyevr(a, compute_v=..., range=..., lower=..., vl=..., vu=..., il=..., iu=..., abstol=..., lwork=..., liwork=..., overwrite_a=...) -> typing.Any:
    "w,z,m,isuppz,info = dsyevr(a,[compute_v,range,lower,vl,vu,il,iu,abstol,lwork,liwork,overwrite_a])\n\nWrapper for ``dsyevr``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds ``(n,n)``\n\nOther Parameters\n----------------\ncompute_v : input int, optional\n    Default ``1``\nrange : input string(len=1), optional\n    Default ``'A'``\nlower : input int, optional\n    Default ``0``\noverwrite_a : input int, optional\n    Default ``0``\nvl : input float, optional\n    Default ``0.0``\nvu : input float, optional\n    Default ``1.0``\nil : input int, optional\n    Default ``1``\niu : input int, optional\n    Default ``n``\nabstol : input float, optional\n    Default ``0.0``\nlwork : input int, optional\n    Default ``max(26*n,1)``\nliwork : input int, optional\n    Default ``max(1,10*n)``\n\nReturns\n-------\nw : rank-1 array('d') with bounds ``(n)``\nz : rank-2 array('d') with bounds ``((compute_v?MAX(0,n):0),(compute_v?(*range=='I'?iu-il+1:MAX(1,n)):0))``\nm : int\nisuppz : rank-1 array('i') with bounds ``((compute_v?(2*(*range=='A'||(*range=='I' && iu-il+1==n)?n:0)):0))``\ninfo : int\n"
    ...

def dsyevr_lwork(n, lower=...) -> typing.Any:
    'work,iwork,info = dsyevr_lwork(n,[lower])\n\nWrapper for ``dsyevr_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nwork : float\niwork : int\ninfo : int\n'
    ...

def dsyevx(a, compute_v=..., range=..., lower=..., vl=..., vu=..., il=..., iu=..., abstol=..., lwork=..., overwrite_a=...) -> typing.Any:
    "w,z,m,ifail,info = dsyevx(a,[compute_v,range,lower,vl,vu,il,iu,abstol,lwork,overwrite_a])\n\nWrapper for ``dsyevx``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds ``(n,n)``\n\nOther Parameters\n----------------\ncompute_v : input int, optional\n    Default ``1``\nrange : input string(len=1), optional\n    Default ``'A'``\nlower : input int, optional\n    Default ``0``\noverwrite_a : input int, optional\n    Default ``0``\nvl : input float, optional\n    Default ``0.0``\nvu : input float, optional\n    Default ``1.0``\nil : input int, optional\n    Default ``1``\niu : input int, optional\n    Default ``n``\nabstol : input float, optional\n    Default ``0.0``\nlwork : input int, optional\n    Default ``max(8*n,1)``\n\nReturns\n-------\nw : rank-1 array('d') with bounds ``(n)``\nz : rank-2 array('d') with bounds ``((compute_v?MAX(0,n):0),(compute_v?(*range=='I'?iu-il+1:MAX(1,n)):0))``\nm : int\nifail : rank-1 array('i') with bounds ``((compute_v?n:0))``\ninfo : int\n"
    ...

def dsyevx_lwork(n, lower=...) -> typing.Any:
    'work,info = dsyevx_lwork(n,[lower])\n\nWrapper for ``dsyevx_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nwork : float\ninfo : int\n'
    ...

def dsygst(a, b, itype=..., lower=..., overwrite_a=...) -> typing.Any:
    "c,info = dsygst(a,b,[itype,lower,overwrite_a])\n\nWrapper for ``dsygst``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (n,n)\nb : input rank-2 array('d') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nitype : input int, optional\n    Default: 1\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('d') with bounds (n,n) and a storage\ninfo : int\n"
    ...

def dsygv(a, b, itype=..., jobz=..., uplo=..., lwork=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "w,v,info = dsygv(a,b,[itype,jobz,uplo,lwork,overwrite_a,overwrite_b])\n\nWrapper for ``dsygv``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (n,n)\nb : input rank-2 array('d') with bounds (n,n)\n\nOther Parameters\n----------------\nitype : input int, optional\n    Default: 1\njobz : input string(len=1), optional\n    Default: 'V'\nuplo : input string(len=1), optional\n    Default: 'L'\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(3*n-1,1)\n\nReturns\n-------\nw : rank-1 array('d') with bounds (n)\nv : rank-2 array('d') with bounds (n,n) and a storage\ninfo : int\n"
    ...

def dsygv_lwork(n, uplo=...) -> typing.Any:
    "work,info = dsygv_lwork(n,[uplo])\n\nWrapper for ``dsygv_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nuplo : input string(len=1), optional\n    Default: 'L'\n\nReturns\n-------\nwork : float\ninfo : int\n"
    ...

def dsygvd(a, b, itype=..., jobz=..., uplo=..., lwork=..., liwork=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "w,v,info = dsygvd(a,b,[itype,jobz,uplo,lwork,liwork,overwrite_a,overwrite_b])\n\nWrapper for ``dsygvd``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds ``(n,n)``\nb : input rank-2 array('d') with bounds ``(n,n)``\n\nOther Parameters\n----------------\nitype : input int, optional\n    Default ``1``\njobz : input string(len=1), optional\n    Default ``'V'``\nuplo : input string(len=1), optional\n    Default ``'L'``\noverwrite_a : input int, optional\n    Default ``0``\noverwrite_b : input int, optional\n    Default ``0``\nlwork : input int, optional\n    Default ``(*jobz=='N'?2*n+1:1+6*n+2*n*n)``\nliwork : input int, optional\n    Default ``(*jobz=='N'?1:5*n+3)``\n\nReturns\n-------\nw : rank-1 array('d') with bounds ``(n)``\nv : rank-2 array('d') with bounds ``(n,n)`` with ``a`` storage\ninfo : int\n"
    ...

def dsygvx(a, b, itype=..., jobz=..., range=..., uplo=..., vl=..., vu=..., il=..., iu=..., abstol=..., lwork=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "w,z,m,ifail,info = dsygvx(a,b,[itype,jobz,range,uplo,vl,vu,il,iu,abstol,lwork,overwrite_a,overwrite_b])\n\nWrapper for ``dsygvx``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (n,n)\nb : input rank-2 array('d') with bounds (n,n)\n\nOther Parameters\n----------------\nitype : input int, optional\n    Default: 1\njobz : input string(len=1), optional\n    Default: 'V'\nrange : input string(len=1), optional\n    Default: 'A'\nuplo : input string(len=1), optional\n    Default: 'L'\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nvl : input float, optional\n    Default: 0.0\nvu : input float, optional\n    Default: 1.0\nil : input int, optional\n    Default: 1\niu : input int, optional\n    Default: n\nabstol : input float, optional\n    Default: 0.0\nlwork : input int, optional\n    Default: max(8*n,1)\n\nReturns\n-------\nw : rank-1 array('d') with bounds (n)\nz : rank-2 array('d') with bounds ((jobz[0]=='V'?MAX(0,n):0),(jobz[0]=='V'?(range[0]=='I'?iu-il+1:MAX(1,n)):0))\nm : int\nifail : rank-1 array('i') with bounds ((jobz[0]=='N'?0:n))\ninfo : int\n"
    ...

def dsygvx_lwork(n, uplo=...) -> typing.Any:
    "work,info = dsygvx_lwork(n,[uplo])\n\nWrapper for ``dsygvx_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nuplo : input string(len=1), optional\n    Default: 'L'\n\nReturns\n-------\nwork : float\ninfo : int\n"
    ...

def dsysv(a, b, lwork=..., lower=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "udut,ipiv,x,info = dsysv(a,b,[lwork,lower,overwrite_a,overwrite_b])\n\nWrapper for ``dsysv``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (n,n)\nb : input rank-2 array('d') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(n,1)\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nudut : rank-2 array('d') with bounds (n,n) and a storage\nipiv : rank-1 array('i') with bounds (n)\nx : rank-2 array('d') with bounds (n,nrhs) and b storage\ninfo : int\n"
    ...

def dsysv_lwork(n, lower=...) -> typing.Any:
    'work,info = dsysv_lwork(n,[lower])\n\nWrapper for ``dsysv_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nwork : float\ninfo : int\n'
    ...

def dsysvx(a, b, af=..., ipiv=..., lwork=..., factored=..., lower=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "a_s,udut,ipiv,b_s,x,rcond,ferr,berr,info = dsysvx(a,b,[af,ipiv,lwork,factored,lower,overwrite_a,overwrite_b])\n\nWrapper for ``dsysvx``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (n,n)\nb : input rank-2 array('d') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\naf : input rank-2 array('d') with bounds (n,n)\nipiv : input rank-1 array('i') with bounds (n)\noverwrite_b : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(3*n,1)\nfactored : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\na_s : rank-2 array('d') with bounds (n,n) and a storage\nudut : rank-2 array('d') with bounds (n,n) and af storage\nipiv : rank-1 array('i') with bounds (n)\nb_s : rank-2 array('d') with bounds (n,nrhs) and b storage\nx : rank-2 array('d') with bounds (n,nrhs)\nrcond : float\nferr : rank-1 array('d') with bounds (nrhs)\nberr : rank-1 array('d') with bounds (nrhs)\ninfo : int\n"
    ...

def dsysvx_lwork(n, lower=...) -> typing.Any:
    'work,info = dsysvx_lwork(n,[lower])\n\nWrapper for ``dsysvx_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nwork : float\ninfo : int\n'
    ...

def dsytf2(a, lower=..., overwrite_a=...) -> typing.Any:
    "ldu,ipiv,info = dsytf2(a,[lower,overwrite_a])\n\nWrapper for ``dsytf2``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (n,n)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\nldu : rank-2 array('d') with bounds (n,n) and a storage\nipiv : rank-1 array('i') with bounds (n)\ninfo : int\n"
    ...

def dsytrd(a, lower=..., lwork=..., overwrite_a=...) -> typing.Any:
    "c,d,e,tau,info = dsytrd(a,[lower,lwork,overwrite_a])\n\nWrapper for ``dsytrd``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (lda,n)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: MAX(n,1)\n\nReturns\n-------\nc : rank-2 array('d') with bounds (lda,n) and a storage\nd : rank-1 array('d') with bounds (n)\ne : rank-1 array('d') with bounds (n - 1)\ntau : rank-1 array('d') with bounds (n - 1)\ninfo : int\n"
    ...

def dsytrd_lwork(n, lower=...) -> typing.Any:
    'work,info = dsytrd_lwork(n,[lower])\n\nWrapper for ``dsytrd_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nwork : float\ninfo : int\n'
    ...

def dsytrf(a, lower=..., lwork=..., overwrite_a=...) -> typing.Any:
    "ldu,ipiv,info = dsytrf(a,[lower,lwork,overwrite_a])\n\nWrapper for ``dsytrf``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (n,n)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(n,1)\n\nReturns\n-------\nldu : rank-2 array('d') with bounds (n,n) and a storage\nipiv : rank-1 array('i') with bounds (n)\ninfo : int\n"
    ...

def dsytrf_lwork(n, lower=...) -> typing.Any:
    'work,info = dsytrf_lwork(n,[lower])\n\nWrapper for ``dsytrf_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nwork : float\ninfo : int\n'
    ...

def dtbtrs(ab, b, uplo=..., trans=..., diag=..., overwrite_b=...) -> typing.Any:
    "x,info = dtbtrs(ab,b,[uplo,trans,diag,overwrite_b])\n\nWrapper for ``dtbtrs``.\n\nParameters\n----------\nab : input rank-2 array('d') with bounds (ldab,n)\nb : input rank-2 array('d') with bounds (ldb,nrhs)\n\nOther Parameters\n----------------\nuplo : input string(len=1), optional\n    Default: 'U'\ntrans : input string(len=1), optional\n    Default: 'N'\ndiag : input string(len=1), optional\n    Default: 'N'\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('d') with bounds (ldb,nrhs) and b storage\ninfo : int\n"
    ...

def dtfsm(alpha, a, b, transr=..., side=..., uplo=..., trans=..., diag=..., overwrite_b=...) -> typing.Any:
    "x = dtfsm(alpha,a,b,[transr,side,uplo,trans,diag,overwrite_b])\n\nWrapper for ``dtfsm``.\n\nParameters\n----------\nalpha : input float\na : input rank-1 array('d') with bounds (nt)\nb : input rank-2 array('d') with bounds (m,n)\n\nOther Parameters\n----------------\ntransr : input string(len=1), optional\n    Default: 'N'\nside : input string(len=1), optional\n    Default: 'L'\nuplo : input string(len=1), optional\n    Default: 'U'\ntrans : input string(len=1), optional\n    Default: 'N'\ndiag : input string(len=1), optional\n    Default: 'N'\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('d') with bounds (m,n) and b storage\n"
    ...

def dtfttp(n, arf, transr=..., uplo=...) -> typing.Any:
    "ap,info = dtfttp(n,arf,[transr,uplo])\n\nWrapper for ``dtfttp``.\n\nParameters\n----------\nn : input int\narf : input rank-1 array('d') with bounds (nt)\n\nOther Parameters\n----------------\ntransr : input string(len=1), optional\n    Default: 'N'\nuplo : input string(len=1), optional\n    Default: 'U'\n\nReturns\n-------\nap : rank-1 array('d') with bounds (nt)\ninfo : int\n"
    ...

def dtfttr(n, arf, transr=..., uplo=...) -> typing.Any:
    "a,info = dtfttr(n,arf,[transr,uplo])\n\nWrapper for ``dtfttr``.\n\nParameters\n----------\nn : input int\narf : input rank-1 array('d') with bounds (nt)\n\nOther Parameters\n----------------\ntransr : input string(len=1), optional\n    Default: 'N'\nuplo : input string(len=1), optional\n    Default: 'U'\n\nReturns\n-------\na : rank-2 array('d') with bounds (lda,n)\ninfo : int\n"
    ...

def dtgsen(select, a, b, q, z, lwork=..., liwork=..., overwrite_a=..., overwrite_b=..., overwrite_q=..., overwrite_z=...) -> typing.Any:
    "a,b,alphar,alphai,beta,q,z,m,pl,pr,dif,work,iwork,info = dtgsen(select,a,b,q,z,[lwork,liwork,overwrite_a,overwrite_b,overwrite_q,overwrite_z])\n\nWrapper for ``dtgsen``.\n\nParameters\n----------\nselect : input rank-1 array('i') with bounds (n)\na : input rank-2 array('d') with bounds (lda,n)\nb : input rank-2 array('d') with bounds (ldb,n)\nq : input rank-2 array('d') with bounds (ldq,n)\nz : input rank-2 array('d') with bounds (ldz,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\noverwrite_q : input int, optional\n    Default: 0\noverwrite_z : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(MAX(4*n+16,2*m*(n-m)),1)\nliwork : input int, optional\n    Default: n+6\n\nReturns\n-------\na : rank-2 array('d') with bounds (lda,n)\nb : rank-2 array('d') with bounds (ldb,n)\nalphar : rank-1 array('d') with bounds (n)\nalphai : rank-1 array('d') with bounds (n)\nbeta : rank-1 array('d') with bounds (n)\nq : rank-2 array('d') with bounds (ldq,n)\nz : rank-2 array('d') with bounds (ldz,n)\nm : int\npl : float\npr : float\ndif : rank-1 array('d') with bounds (2)\nwork : rank-1 array('d') with bounds (MAX(lwork,1))\niwork : rank-1 array('i') with bounds (MAX(1,liwork))\ninfo : int\n"
    ...

def dtpmqrt(l, v, t, a, b, side=..., trans=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "a,b,info = dtpmqrt(l,v,t,a,b,[side,trans,overwrite_a,overwrite_b])\n\nWrapper for ``dtpmqrt``.\n\nParameters\n----------\nl : input int\nv : input rank-2 array('d') with bounds ((side[0]=='L'?m:n),k)\nt : input rank-2 array('d') with bounds (nb,k)\na : input rank-2 array('d') with bounds ((side[0]=='L'?k:m),(side[0]=='L'?n:k))\nb : input rank-2 array('d') with bounds (m,n)\n\nOther Parameters\n----------------\nside : input string(len=1), optional\n    Default: 'L'\ntrans : input string(len=1), optional\n    Default: 'N'\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\na : rank-2 array('d') with bounds ((side[0]=='L'?k:m),(side[0]=='L'?n:k))\nb : rank-2 array('d') with bounds (m,n)\ninfo : int\n"
    ...

def dtpqrt(l, nb, a, b, overwrite_a=..., overwrite_b=...) -> typing.Any:
    "a,b,t,info = dtpqrt(l,nb,a,b,[overwrite_a,overwrite_b])\n\nWrapper for ``dtpqrt``.\n\nParameters\n----------\nl : input int\nnb : input int\na : input rank-2 array('d') with bounds (n,n)\nb : input rank-2 array('d') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\na : rank-2 array('d') with bounds (n,n)\nb : rank-2 array('d') with bounds (m,n)\nt : rank-2 array('d') with bounds (nb,n)\ninfo : int\n"
    ...

def dtpttf(n, ap, transr=..., uplo=...) -> typing.Any:
    "arf,info = dtpttf(n,ap,[transr,uplo])\n\nWrapper for ``dtpttf``.\n\nParameters\n----------\nn : input int\nap : input rank-1 array('d') with bounds (nt)\n\nOther Parameters\n----------------\ntransr : input string(len=1), optional\n    Default: 'N'\nuplo : input string(len=1), optional\n    Default: 'U'\n\nReturns\n-------\narf : rank-1 array('d') with bounds (nt)\ninfo : int\n"
    ...

def dtpttr(n, ap, uplo=...) -> typing.Any:
    "a,info = dtpttr(n,ap,[uplo])\n\nWrapper for ``dtpttr``.\n\nParameters\n----------\nn : input int\nap : input rank-1 array('d') with bounds (nt)\n\nOther Parameters\n----------------\nuplo : input string(len=1), optional\n    Default: 'U'\n\nReturns\n-------\na : rank-2 array('d') with bounds (n,n)\ninfo : int\n"
    ...

def dtrsyl(a, b, c, trana=..., tranb=..., isgn=..., overwrite_c=...) -> typing.Any:
    "x,scale,info = dtrsyl(a,b,c,[trana,tranb,isgn,overwrite_c])\n\nWrapper for ``dtrsyl``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (m,m)\nb : input rank-2 array('d') with bounds (n,n)\nc : input rank-2 array('d') with bounds (m,n)\n\nOther Parameters\n----------------\ntrana : input string(len=1), optional\n    Default: 'N'\ntranb : input string(len=1), optional\n    Default: 'N'\nisgn : input int, optional\n    Default: 1\noverwrite_c : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('d') with bounds (m,n) and c storage\nscale : float\ninfo : int\n"
    ...

def dtrtri(c, lower=..., unitdiag=..., overwrite_c=...) -> typing.Any:
    "inv_c,info = dtrtri(c,[lower,unitdiag,overwrite_c])\n\nWrapper for ``dtrtri``.\n\nParameters\n----------\nc : input rank-2 array('d') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_c : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\nunitdiag : input int, optional\n    Default: 0\n\nReturns\n-------\ninv_c : rank-2 array('d') with bounds (n,n) and c storage\ninfo : int\n"
    ...

def dtrtrs(a, b, lower=..., trans=..., unitdiag=..., lda=..., overwrite_b=...) -> typing.Any:
    "x,info = dtrtrs(a,b,[lower,trans,unitdiag,lda,overwrite_b])\n\nWrapper for ``dtrtrs``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (lda,n)\nb : input rank-2 array('d') with bounds (ldb,nrhs)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\nunitdiag : input int, optional\n    Default: 0\nlda : input int, optional\n    Default: shape(a,0)\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('d') with bounds (ldb,nrhs) and b storage\ninfo : int\n"
    ...

def dtrttf(a, transr=..., uplo=...) -> typing.Any:
    "arf,info = dtrttf(a,[transr,uplo])\n\nWrapper for ``dtrttf``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (lda,n)\n\nOther Parameters\n----------------\ntransr : input string(len=1), optional\n    Default: 'N'\nuplo : input string(len=1), optional\n    Default: 'U'\n\nReturns\n-------\narf : rank-1 array('d') with bounds (n*(n+1)/2)\ninfo : int\n"
    ...

def dtrttp(a, uplo=...) -> typing.Any:
    "ap,info = dtrttp(a,[uplo])\n\nWrapper for ``dtrttp``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (lda,n)\n\nOther Parameters\n----------------\nuplo : input string(len=1), optional\n    Default: 'U'\n\nReturns\n-------\nap : rank-1 array('d') with bounds (n*(n+1)/2)\ninfo : int\n"
    ...

def dtzrzf(a, lwork=..., overwrite_a=...) -> typing.Any:
    "rz,tau,info = dtzrzf(a,[lwork,overwrite_a])\n\nWrapper for ``dtzrzf``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: MAX(m,1)\n\nReturns\n-------\nrz : rank-2 array('d') with bounds (m,n) and a storage\ntau : rank-1 array('d') with bounds (m)\ninfo : int\n"
    ...

def dtzrzf_lwork(m, n) -> typing.Any:
    'work,info = dtzrzf_lwork(m,n)\n\nWrapper for ``dtzrzf_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\n\nReturns\n-------\nwork : float\ninfo : int\n'
    ...

def ilaver() -> typing.Any:
    'major,minor,patch = ilaver()\n\nWrapper for ``ilaver``.\n\nReturns\n-------\nmajor : int\nminor : int\npatch : int\n'
    ...

def sgbsv(kl, ku, ab, b, overwrite_ab=..., overwrite_b=...) -> typing.Any:
    "lub,piv,x,info = sgbsv(kl,ku,ab,b,[overwrite_ab,overwrite_b])\n\nWrapper for ``sgbsv``.\n\nParameters\n----------\nkl : input int\nku : input int\nab : input rank-2 array('f') with bounds (2*kl+ku+1,n)\nb : input rank-2 array('f') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_ab : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nlub : rank-2 array('f') with bounds (2*kl+ku+1,n) and ab storage\npiv : rank-1 array('i') with bounds (n)\nx : rank-2 array('f') with bounds (n,nrhs) and b storage\ninfo : int\n"
    ...

def sgbtrf(ab, kl, ku, m=..., n=..., ldab=..., overwrite_ab=...) -> typing.Any:
    "lu,ipiv,info = sgbtrf(ab,kl,ku,[m,n,ldab,overwrite_ab])\n\nWrapper for ``sgbtrf``.\n\nParameters\n----------\nab : input rank-2 array('f') with bounds (ldab,n)\nkl : input int\nku : input int\n\nOther Parameters\n----------------\nm : input int, optional\n    Default: shape(ab,1)\nn : input int, optional\n    Default: shape(ab,1)\noverwrite_ab : input int, optional\n    Default: 0\nldab : input int, optional\n    Default: max(shape(ab,0),1)\n\nReturns\n-------\nlu : rank-2 array('f') with bounds (ldab,n) and ab storage\nipiv : rank-1 array('i') with bounds (MIN(m,n))\ninfo : int\n"
    ...

def sgbtrs(ab, kl, ku, b, ipiv, trans=..., n=..., ldab=..., ldb=..., overwrite_b=...) -> typing.Any:
    "x,info = sgbtrs(ab,kl,ku,b,ipiv,[trans,n,ldab,ldb,overwrite_b])\n\nWrapper for ``sgbtrs``.\n\nParameters\n----------\nab : input rank-2 array('f') with bounds (ldab,n)\nkl : input int\nku : input int\nb : input rank-2 array('f') with bounds (ldb,nrhs)\nipiv : input rank-1 array('i') with bounds (n)\n\nOther Parameters\n----------------\noverwrite_b : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\nn : input int, optional\n    Default: shape(ab,1)\nldab : input int, optional\n    Default: shape(ab,0)\nldb : input int, optional\n    Default: shape(b,0)\n\nReturns\n-------\nx : rank-2 array('f') with bounds (ldb,nrhs) and b storage\ninfo : int\n"
    ...

def sgebal(a, scale=..., permute=..., overwrite_a=...) -> typing.Any:
    "ba,lo,hi,pivscale,info = sgebal(a,[scale,permute,overwrite_a])\n\nWrapper for ``sgebal``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (m,n)\n\nOther Parameters\n----------------\nscale : input int, optional\n    Default: 0\npermute : input int, optional\n    Default: 0\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\nba : rank-2 array('f') with bounds (m,n) and a storage\nlo : int\nhi : int\npivscale : rank-1 array('f') with bounds (n)\ninfo : int\n"
    ...

def sgecon(a, anorm, norm=...) -> typing.Any:
    "rcond,info = sgecon(a,anorm,[norm])\n\nWrapper for ``sgecon``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (n,n)\nanorm : input float\n\nOther Parameters\n----------------\nnorm : input string(len=1), optional\n    Default: '1'\n\nReturns\n-------\nrcond : float\ninfo : int\n"
    ...

def sgeequ(a) -> typing.Any:
    "r,c,rowcnd,colcnd,amax,info = sgeequ(a)\n\nWrapper for ``sgeequ``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (m,n)\n\nReturns\n-------\nr : rank-1 array('f') with bounds (m)\nc : rank-1 array('f') with bounds (n)\nrowcnd : float\ncolcnd : float\namax : float\ninfo : int\n"
    ...

def sgeequb(a) -> typing.Any:
    "r,c,rowcnd,colcnd,amax,info = sgeequb(a)\n\nWrapper for ``sgeequb``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (m,n)\n\nReturns\n-------\nr : rank-1 array('f') with bounds (m)\nc : rank-1 array('f') with bounds (n)\nrowcnd : float\ncolcnd : float\namax : float\ninfo : int\n"
    ...

def sgees(sselect, a, compute_v=..., sort_t=..., lwork=..., sselect_extra_args=..., overwrite_a=...) -> typing.Any:
    "t,sdim,wr,wi,vs,work,info = sgees(sselect,a,[compute_v,sort_t,lwork,sselect_extra_args,overwrite_a])\n\nWrapper for ``sgees``.\n\nParameters\n----------\nsselect : call-back function\na : input rank-2 array('f') with bounds (n,n)\n\nOther Parameters\n----------------\ncompute_v : input int, optional\n    Default: 1\nsort_t : input int, optional\n    Default: 0\nsselect_extra_args : input tuple, optional\n    Default: ()\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(3*n,1)\n\nReturns\n-------\nt : rank-2 array('f') with bounds (n,n) and a storage\nsdim : int\nwr : rank-1 array('f') with bounds (n)\nwi : rank-1 array('f') with bounds (n)\nvs : rank-2 array('f') with bounds (ldvs,n)\nwork : rank-1 array('f') with bounds (MAX(lwork,1))\ninfo : int\n\nNotes\n-----\nCall-back functions::\n\n  def sselect(arg1,arg2): return sselect\n  Required arguments:\n    arg1 : input float\n    arg2 : input float\n  Return objects:\n    sselect : int\n"
    ...

def sgeev(a, compute_vl=..., compute_vr=..., lwork=..., overwrite_a=...) -> typing.Any:
    "wr,wi,vl,vr,info = sgeev(a,[compute_vl,compute_vr,lwork,overwrite_a])\n\nWrapper for ``sgeev``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (n,n)\n\nOther Parameters\n----------------\ncompute_vl : input int, optional\n    Default: 1\ncompute_vr : input int, optional\n    Default: 1\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(4*n,1)\n\nReturns\n-------\nwr : rank-1 array('f') with bounds (n)\nwi : rank-1 array('f') with bounds (n)\nvl : rank-2 array('f') with bounds (ldvl,n)\nvr : rank-2 array('f') with bounds (ldvr,n)\ninfo : int\n"
    ...

def sgeev_lwork(n, compute_vl=..., compute_vr=...) -> typing.Any:
    'work,info = sgeev_lwork(n,[compute_vl,compute_vr])\n\nWrapper for ``sgeev_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\ncompute_vl : input int, optional\n    Default: 1\ncompute_vr : input int, optional\n    Default: 1\n\nReturns\n-------\nwork : float\ninfo : int\n'
    ...

def sgegv(*args, **kwds) -> typing.Any:
    "`sgegv` is deprecated!\nThe `*gegv` family of routines has been deprecated in\nLAPACK 3.6.0 in favor of the `*ggev` family of routines.\nThe corresponding wrappers will be removed from SciPy in\na future release.\n\nalphar,alphai,beta,vl,vr,info = sgegv(a,b,[compute_vl,compute_vr,lwork,overwrite_a,overwrite_b])\n\nWrapper for ``sgegv``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (n,n)\nb : input rank-2 array('f') with bounds (n,n)\n\nOther Parameters\n----------------\ncompute_vl : input int, optional\n    Default: 1\ncompute_vr : input int, optional\n    Default: 1\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(8*n,1)\n\nReturns\n-------\nalphar : rank-1 array('f') with bounds (n)\nalphai : rank-1 array('f') with bounds (n)\nbeta : rank-1 array('f') with bounds (n)\nvl : rank-2 array('f') with bounds (ldvl,n)\nvr : rank-2 array('f') with bounds (ldvr,n)\ninfo : int\n"
    ...

def sgehrd(a, lo=..., hi=..., lwork=..., overwrite_a=...) -> typing.Any:
    "ht,tau,info = sgehrd(a,[lo,hi,lwork,overwrite_a])\n\nWrapper for ``sgehrd``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (n,n)\n\nOther Parameters\n----------------\nlo : input int, optional\n    Default: 0\nhi : input int, optional\n    Default: n-1\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: MAX(n,1)\n\nReturns\n-------\nht : rank-2 array('f') with bounds (n,n) and a storage\ntau : rank-1 array('f') with bounds (n - 1)\ninfo : int\n"
    ...

def sgehrd_lwork(n, lo=..., hi=...) -> typing.Any:
    'work,info = sgehrd_lwork(n,[lo,hi])\n\nWrapper for ``sgehrd_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlo : input int, optional\n    Default: 0\nhi : input int, optional\n    Default: n-1\n\nReturns\n-------\nwork : float\ninfo : int\n'
    ...

def sgejsv(a, joba=..., jobu=..., jobv=..., jobr=..., jobt=..., jobp=..., lwork=..., overwrite_a=...) -> typing.Any:
    "sva,u,v,workout,iworkout,info = sgejsv(a,[joba,jobu,jobv,jobr,jobt,jobp,lwork,overwrite_a])\n\nWrapper for ``sgejsv``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (lda,n)\n\nOther Parameters\n----------------\njoba : input int, optional\n    Default: 4\njobu : input int, optional\n    Default: 0\njobv : input int, optional\n    Default: 0\njobr : input int, optional\n    Default: 1\njobt : input int, optional\n    Default: 0\njobp : input int, optional\n    Default: 1\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(6*n+2*n*n, max(2*m+n, max(4*n+n*n, max(2*n+n*n+6, 7))))\n\nReturns\n-------\nsva : rank-1 array('f') with bounds (n)\nu : rank-2 array('f') with bounds (((jobt == 0)&&(jobu == 3)?0:m),((jobt == 0)&&(jobu == 3)?0:(jobu == 1?m:n)))\nv : rank-2 array('f') with bounds (((jobt == 0)&&(jobv == 3)?0:ldv),((jobt == 0)&&(jobv == 3)?0:n))\nworkout : rank-1 array('f') with bounds (7)\niworkout : rank-1 array('i') with bounds (3)\ninfo : int\n"
    ...

def sgels(a, b, trans=..., lwork=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "lqr,x,info = sgels(a,b,[trans,lwork,overwrite_a,overwrite_b])\n\nWrapper for ``sgels``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (m,n)\nb : input rank-2 array('f') with bounds (MAX(m,n),nrhs)\n\nOther Parameters\n----------------\ntrans : input string(len=1), optional\n    Default: 'N'\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: MAX(MIN(m,n)+MAX(MIN(m,n),nrhs),1)\n\nReturns\n-------\nlqr : rank-2 array('f') with bounds (m,n) and a storage\nx : rank-2 array('f') with bounds (MAX(m,n),nrhs) and b storage\ninfo : int\n"
    ...

def sgels_lwork(m, n, nrhs, trans=...) -> typing.Any:
    "work,info = sgels_lwork(m,n,nrhs,[trans])\n\nWrapper for ``sgels_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\nnrhs : input int\n\nOther Parameters\n----------------\ntrans : input string(len=1), optional\n    Default: 'N'\n\nReturns\n-------\nwork : float\ninfo : int\n"
    ...

def sgelsd(a, b, lwork, size_iwork, cond=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "x,s,rank,info = sgelsd(a,b,lwork,size_iwork,[cond,overwrite_a,overwrite_b])\n\nWrapper for ``sgelsd``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (m,n)\nb : input rank-2 array('f') with bounds (maxmn,nrhs)\nlwork : input int\nsize_iwork : input int\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\ncond : input float, optional\n    Default: -1.0\n\nReturns\n-------\nx : rank-2 array('f') with bounds (maxmn,nrhs) and b storage\ns : rank-1 array('f') with bounds (minmn)\nrank : int\ninfo : int\n"
    ...

def sgelsd_lwork(m, n, nrhs, cond=..., lwork=...) -> typing.Any:
    'work,iwork,info = sgelsd_lwork(m,n,nrhs,[cond,lwork])\n\nWrapper for ``sgelsd_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\nnrhs : input int\n\nOther Parameters\n----------------\ncond : input float, optional\n    Default: -1.0\nlwork : input int, optional\n    Default: -1\n\nReturns\n-------\nwork : float\niwork : int\ninfo : int\n'
    ...

def sgelss(a, b, cond=..., lwork=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "v,x,s,rank,work,info = sgelss(a,b,[cond,lwork,overwrite_a,overwrite_b])\n\nWrapper for ``sgelss``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (m,n)\nb : input rank-2 array('f') with bounds (maxmn,nrhs)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\ncond : input float, optional\n    Default: -1.0\nlwork : input int, optional\n    Default: max(3*minmn+MAX(2*minmn,MAX(maxmn,nrhs)),1)\n\nReturns\n-------\nv : rank-2 array('f') with bounds (m,n) and a storage\nx : rank-2 array('f') with bounds (maxmn,nrhs) and b storage\ns : rank-1 array('f') with bounds (minmn)\nrank : int\nwork : rank-1 array('f') with bounds (MAX(lwork,1))\ninfo : int\n"
    ...

def sgelss_lwork(m, n, nrhs, cond=..., lwork=...) -> typing.Any:
    'work,info = sgelss_lwork(m,n,nrhs,[cond,lwork])\n\nWrapper for ``sgelss_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\nnrhs : input int\n\nOther Parameters\n----------------\ncond : input float, optional\n    Default: -1.0\nlwork : input int, optional\n    Default: -1\n\nReturns\n-------\nwork : float\ninfo : int\n'
    ...

def sgelsy(a, b, jptv, cond, lwork, overwrite_a=..., overwrite_b=...) -> typing.Any:
    "v,x,j,rank,info = sgelsy(a,b,jptv,cond,lwork,[overwrite_a,overwrite_b])\n\nWrapper for ``sgelsy``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (m,n)\nb : input rank-2 array('f') with bounds (maxmn,nrhs)\njptv : input rank-1 array('i') with bounds (n)\ncond : input float\nlwork : input int\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nv : rank-2 array('f') with bounds (m,n) and a storage\nx : rank-2 array('f') with bounds (maxmn,nrhs) and b storage\nj : rank-1 array('i') with bounds (n) and jptv storage\nrank : int\ninfo : int\n"
    ...

def sgelsy_lwork(m, n, nrhs, cond, lwork=...) -> typing.Any:
    'work,info = sgelsy_lwork(m,n,nrhs,cond,[lwork])\n\nWrapper for ``sgelsy_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\nnrhs : input int\ncond : input float\n\nOther Parameters\n----------------\nlwork : input int, optional\n    Default: -1\n\nReturns\n-------\nwork : float\ninfo : int\n'
    ...

def sgemqrt(v, t, c, side=..., trans=..., overwrite_c=...) -> typing.Any:
    "c,info = sgemqrt(v,t,c,[side,trans,overwrite_c])\n\nWrapper for ``sgemqrt``.\n\nParameters\n----------\nv : input rank-2 array('f') with bounds ((side[0]=='L'?m:n),k)\nt : input rank-2 array('f') with bounds (nb,k)\nc : input rank-2 array('f') with bounds (m,n)\n\nOther Parameters\n----------------\nside : input string(len=1), optional\n    Default: 'L'\ntrans : input string(len=1), optional\n    Default: 'N'\noverwrite_c : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('f') with bounds (m,n)\ninfo : int\n"
    ...

def sgeqp3(a, lwork=..., overwrite_a=...) -> typing.Any:
    "qr,jpvt,tau,work,info = sgeqp3(a,[lwork,overwrite_a])\n\nWrapper for ``sgeqp3``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(3*(n+1),1)\n\nReturns\n-------\nqr : rank-2 array('f') with bounds (m,n) and a storage\njpvt : rank-1 array('i') with bounds (n)\ntau : rank-1 array('f') with bounds (MIN(m,n))\nwork : rank-1 array('f') with bounds (MAX(lwork,1))\ninfo : int\n"
    ...

def sgeqrf(a, lwork=..., overwrite_a=...) -> typing.Any:
    "qr,tau,work,info = sgeqrf(a,[lwork,overwrite_a])\n\nWrapper for ``sgeqrf``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(3*n,1)\n\nReturns\n-------\nqr : rank-2 array('f') with bounds (m,n) and a storage\ntau : rank-1 array('f') with bounds (MIN(m,n))\nwork : rank-1 array('f') with bounds (MAX(lwork,1))\ninfo : int\n"
    ...

def sgeqrf_lwork(m, n) -> typing.Any:
    'work,info = sgeqrf_lwork(m,n)\n\nWrapper for ``sgeqrf_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\n\nReturns\n-------\nwork : float\ninfo : int\n'
    ...

def sgeqrfp(a, lwork=..., overwrite_a=...) -> typing.Any:
    "qr,tau,info = sgeqrfp(a,[lwork,overwrite_a])\n\nWrapper for ``sgeqrfp``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: MAX(1, n)\n\nReturns\n-------\nqr : rank-2 array('f') with bounds (m,n) and a storage\ntau : rank-1 array('f') with bounds (MIN(m,n))\ninfo : int\n"
    ...

def sgeqrfp_lwork(m, n) -> typing.Any:
    'work,info = sgeqrfp_lwork(m,n)\n\nWrapper for ``sgeqrfp_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\n\nReturns\n-------\nwork : float\ninfo : int\n'
    ...

def sgeqrt(nb, a, overwrite_a=...) -> typing.Any:
    "a,t,info = sgeqrt(nb,a,[overwrite_a])\n\nWrapper for ``sgeqrt``.\n\nParameters\n----------\nnb : input int\na : input rank-2 array('f') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\na : rank-2 array('f') with bounds (m,n)\nt : rank-2 array('f') with bounds (nb,MIN(m,n))\ninfo : int\n"
    ...

def sgerqf(a, lwork=..., overwrite_a=...) -> typing.Any:
    "qr,tau,work,info = sgerqf(a,[lwork,overwrite_a])\n\nWrapper for ``sgerqf``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(3*m,1)\n\nReturns\n-------\nqr : rank-2 array('f') with bounds (m,n) and a storage\ntau : rank-1 array('f') with bounds (MIN(m,n))\nwork : rank-1 array('f') with bounds (MAX(lwork,1))\ninfo : int\n"
    ...

def sgesc2(lu, rhs, ipiv, jpiv, overwrite_rhs=...) -> typing.Any:
    "x,scale = sgesc2(lu,rhs,ipiv,jpiv,[overwrite_rhs])\n\nWrapper for ``sgesc2``.\n\nParameters\n----------\nlu : input rank-2 array('f') with bounds (n,n)\nrhs : input rank-1 array('f') with bounds (n)\nipiv : input rank-1 array('i') with bounds (n)\njpiv : input rank-1 array('i') with bounds (n)\n\nOther Parameters\n----------------\noverwrite_rhs : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-1 array('f') with bounds (n) and rhs storage\nscale : float\n"
    ...

def sgesdd(a, compute_uv=..., full_matrices=..., lwork=..., overwrite_a=...) -> typing.Any:
    "u,s,vt,info = sgesdd(a,[compute_uv,full_matrices,lwork,overwrite_a])\n\nWrapper for ``sgesdd``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\ncompute_uv : input int, optional\n    Default: 1\nfull_matrices : input int, optional\n    Default: 1\nlwork : input int, optional\n    Default: max((compute_uv?4*minmn*minmn+MAX(m,n)+9*minmn:MAX(14*minmn+4,10*minmn+2+25*(25+8))+MAX(m,n)),1)\n\nReturns\n-------\nu : rank-2 array('f') with bounds (u0,u1)\ns : rank-1 array('f') with bounds (minmn)\nvt : rank-2 array('f') with bounds (vt0,vt1)\ninfo : int\n"
    ...

def sgesdd_lwork(m, n, compute_uv=..., full_matrices=...) -> typing.Any:
    'work,info = sgesdd_lwork(m,n,[compute_uv,full_matrices])\n\nWrapper for ``sgesdd_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\n\nOther Parameters\n----------------\ncompute_uv : input int, optional\n    Default: 1\nfull_matrices : input int, optional\n    Default: 1\n\nReturns\n-------\nwork : float\ninfo : int\n'
    ...

def sgesv(a, b, overwrite_a=..., overwrite_b=...) -> typing.Any:
    "lu,piv,x,info = sgesv(a,b,[overwrite_a,overwrite_b])\n\nWrapper for ``sgesv``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (n,n)\nb : input rank-2 array('f') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nlu : rank-2 array('f') with bounds (n,n) and a storage\npiv : rank-1 array('i') with bounds (n)\nx : rank-2 array('f') with bounds (n,nrhs) and b storage\ninfo : int\n"
    ...

def sgesvd(a, compute_uv=..., full_matrices=..., lwork=..., overwrite_a=...) -> typing.Any:
    "u,s,vt,info = sgesvd(a,[compute_uv,full_matrices,lwork,overwrite_a])\n\nWrapper for ``sgesvd``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\ncompute_uv : input int, optional\n    Default: 1\nfull_matrices : input int, optional\n    Default: 1\nlwork : input int, optional\n    Default: max(MAX(3*minmn+MAX(m,n),5*minmn),1)\n\nReturns\n-------\nu : rank-2 array('f') with bounds (u0,u1)\ns : rank-1 array('f') with bounds (minmn)\nvt : rank-2 array('f') with bounds (vt0,vt1)\ninfo : int\n"
    ...

def sgesvd_lwork(m, n, compute_uv=..., full_matrices=...) -> typing.Any:
    'work,info = sgesvd_lwork(m,n,[compute_uv,full_matrices])\n\nWrapper for ``sgesvd_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\n\nOther Parameters\n----------------\ncompute_uv : input int, optional\n    Default: 1\nfull_matrices : input int, optional\n    Default: 1\n\nReturns\n-------\nwork : float\ninfo : int\n'
    ...

def sgesvx(a, b, fact=..., trans=..., af=..., ipiv=..., equed=..., r=..., c=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "as,lu,ipiv,equed,rs,cs,bs,x,rcond,ferr,berr,info = sgesvx(a,b,[fact,trans,af,ipiv,equed,r,c,overwrite_a,overwrite_b])\n\nWrapper for ``sgesvx``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (n,n)\nb : input rank-2 array('f') with bounds (n,nrhs)\n\nOther Parameters\n----------------\nfact : input string(len=1), optional\n    Default: 'E'\ntrans : input string(len=1), optional\n    Default: 'N'\noverwrite_a : input int, optional\n    Default: 0\naf : input rank-2 array('f') with bounds (n,n)\nipiv : input rank-1 array('i') with bounds (n)\nequed : input string(len=1), optional\n    Default: 'B'\nr : input rank-1 array('f') with bounds (n)\nc : input rank-1 array('f') with bounds (n)\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nas : rank-2 array('f') with bounds (n,n) and a storage\nlu : rank-2 array('f') with bounds (n,n) and af storage\nipiv : rank-1 array('i') with bounds (n)\nequed : string(len=1)\nrs : rank-1 array('f') with bounds (n) and r storage\ncs : rank-1 array('f') with bounds (n) and c storage\nbs : rank-2 array('f') with bounds (n,nrhs) and b storage\nx : rank-2 array('f') with bounds (n,nrhs)\nrcond : float\nferr : rank-1 array('f') with bounds (nrhs)\nberr : rank-1 array('f') with bounds (nrhs)\ninfo : int\n"
    ...

def sgetc2(a, overwrite_a=...) -> typing.Any:
    "lu,ipiv,jpiv,info = sgetc2(a,[overwrite_a])\n\nWrapper for ``sgetc2``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\nlu : rank-2 array('f') with bounds (n,n) and a storage\nipiv : rank-1 array('i') with bounds (n)\njpiv : rank-1 array('i') with bounds (n)\ninfo : int\n"
    ...

def sgetrf(a, overwrite_a=...) -> typing.Any:
    "lu,piv,info = sgetrf(a,[overwrite_a])\n\nWrapper for ``sgetrf``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\nlu : rank-2 array('f') with bounds (m,n) and a storage\npiv : rank-1 array('i') with bounds (MIN(m,n))\ninfo : int\n"
    ...

def sgetri(lu, piv, lwork=..., overwrite_lu=...) -> typing.Any:
    "inv_a,info = sgetri(lu,piv,[lwork,overwrite_lu])\n\nWrapper for ``sgetri``.\n\nParameters\n----------\nlu : input rank-2 array('f') with bounds (n,n)\npiv : input rank-1 array('i') with bounds (n)\n\nOther Parameters\n----------------\noverwrite_lu : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(3*n,1)\n\nReturns\n-------\ninv_a : rank-2 array('f') with bounds (n,n) and lu storage\ninfo : int\n"
    ...

def sgetri_lwork(n) -> typing.Any:
    'work,info = sgetri_lwork(n)\n\nWrapper for ``sgetri_lwork``.\n\nParameters\n----------\nn : input int\n\nReturns\n-------\nwork : float\ninfo : int\n'
    ...

def sgetrs(lu, piv, b, trans=..., overwrite_b=...) -> typing.Any:
    "x,info = sgetrs(lu,piv,b,[trans,overwrite_b])\n\nWrapper for ``sgetrs``.\n\nParameters\n----------\nlu : input rank-2 array('f') with bounds (n,n)\npiv : input rank-1 array('i') with bounds (n)\nb : input rank-2 array('f') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_b : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('f') with bounds (n,nrhs) and b storage\ninfo : int\n"
    ...

def sgges(sselect, a, b, jobvsl=..., jobvsr=..., sort_t=..., ldvsl=..., ldvsr=..., lwork=..., sselect_extra_args=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "a,b,sdim,alphar,alphai,beta,vsl,vsr,work,info = sgges(sselect,a,b,[jobvsl,jobvsr,sort_t,ldvsl,ldvsr,lwork,sselect_extra_args,overwrite_a,overwrite_b])\n\nWrapper for ``sgges``.\n\nParameters\n----------\nsselect : call-back function\na : input rank-2 array('f') with bounds (lda,n)\nb : input rank-2 array('f') with bounds (ldb,n)\n\nOther Parameters\n----------------\njobvsl : input int, optional\n    Default: 1\njobvsr : input int, optional\n    Default: 1\nsort_t : input int, optional\n    Default: 0\nsselect_extra_args : input tuple, optional\n    Default: ()\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nldvsl : input int, optional\n    Default: ((jobvsl==1)?n:1)\nldvsr : input int, optional\n    Default: ((jobvsr==1)?n:1)\nlwork : input int, optional\n    Default: max(8*n+16,1)\n\nReturns\n-------\na : rank-2 array('f') with bounds (lda,n)\nb : rank-2 array('f') with bounds (ldb,n)\nsdim : int\nalphar : rank-1 array('f') with bounds (n)\nalphai : rank-1 array('f') with bounds (n)\nbeta : rank-1 array('f') with bounds (n)\nvsl : rank-2 array('f') with bounds (ldvsl,n)\nvsr : rank-2 array('f') with bounds (ldvsr,n)\nwork : rank-1 array('f') with bounds (MAX(lwork,1))\ninfo : int\n\nNotes\n-----\nCall-back functions::\n\n  def sselect(alphar,alphai,beta): return sselect\n  Required arguments:\n    alphar : input float\n    alphai : input float\n    beta : input float\n  Return objects:\n    sselect : int\n"
    ...

def sggev(a, b, compute_vl=..., compute_vr=..., lwork=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "alphar,alphai,beta,vl,vr,work,info = sggev(a,b,[compute_vl,compute_vr,lwork,overwrite_a,overwrite_b])\n\nWrapper for ``sggev``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (n,n)\nb : input rank-2 array('f') with bounds (n,n)\n\nOther Parameters\n----------------\ncompute_vl : input int, optional\n    Default: 1\ncompute_vr : input int, optional\n    Default: 1\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(8*n,1)\n\nReturns\n-------\nalphar : rank-1 array('f') with bounds (n)\nalphai : rank-1 array('f') with bounds (n)\nbeta : rank-1 array('f') with bounds (n)\nvl : rank-2 array('f') with bounds (ldvl,n)\nvr : rank-2 array('f') with bounds (ldvr,n)\nwork : rank-1 array('f') with bounds (MAX(lwork,1))\ninfo : int\n"
    ...

def sgglse(a, b, c, d, lwork=..., overwrite_a=..., overwrite_b=..., overwrite_c=..., overwrite_d=...) -> typing.Any:
    "t,r,res,x,info = sgglse(a,b,c,d,[lwork,overwrite_a,overwrite_b,overwrite_c,overwrite_d])\n\nWrapper for ``sgglse``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (m,n)\nb : input rank-2 array('f') with bounds (p,n)\nc : input rank-1 array('f') with bounds (m)\nd : input rank-1 array('f') with bounds (p)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\noverwrite_c : input int, optional\n    Default: 0\noverwrite_d : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(m+n+p,1)\n\nReturns\n-------\nt : rank-2 array('f') with bounds (m,n) and a storage\nr : rank-2 array('f') with bounds (p,n) and b storage\nres : rank-1 array('f') with bounds (m) and c storage\nx : rank-1 array('f') with bounds (n)\ninfo : int\n"
    ...

def sgglse_lwork(m, n, p) -> typing.Any:
    'work,info = sgglse_lwork(m,n,p)\n\nWrapper for ``sgglse_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\np : input int\n\nReturns\n-------\nwork : float\ninfo : int\n'
    ...

def sgtsv(dl, d, du, b, overwrite_dl=..., overwrite_d=..., overwrite_du=..., overwrite_b=...) -> typing.Any:
    "du2,d,du,x,info = sgtsv(dl,d,du,b,[overwrite_dl,overwrite_d,overwrite_du,overwrite_b])\n\nWrapper for ``sgtsv``.\n\nParameters\n----------\ndl : input rank-1 array('f') with bounds (n - 1)\nd : input rank-1 array('f') with bounds (n)\ndu : input rank-1 array('f') with bounds (n - 1)\nb : input rank-2 array('f') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_dl : input int, optional\n    Default: 0\noverwrite_d : input int, optional\n    Default: 0\noverwrite_du : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\ndu2 : rank-1 array('f') with bounds (n - 1) and dl storage\nd : rank-1 array('f') with bounds (n)\ndu : rank-1 array('f') with bounds (n - 1)\nx : rank-2 array('f') with bounds (n,nrhs) and b storage\ninfo : int\n"
    ...

def sgtsvx(dl, d, du, b, fact=..., trans=..., dlf=..., df=..., duf=..., du2=..., ipiv=...) -> typing.Any:
    "dlf,df,duf,du2,ipiv,x,rcond,ferr,berr,info = sgtsvx(dl,d,du,b,[fact,trans,dlf,df,duf,du2,ipiv])\n\nWrapper for ``sgtsvx``.\n\nParameters\n----------\ndl : input rank-1 array('f') with bounds (MAX(0, n-1))\nd : input rank-1 array('f') with bounds (n)\ndu : input rank-1 array('f') with bounds (MAX(0, n-1))\nb : input rank-2 array('f') with bounds (ldb,nrhs)\n\nOther Parameters\n----------------\nfact : input string(len=1), optional\n    Default: 'N'\ntrans : input string(len=1), optional\n    Default: 'N'\ndlf : input rank-1 array('f') with bounds (MAX(0,n-1))\ndf : input rank-1 array('f') with bounds (n)\nduf : input rank-1 array('f') with bounds (MAX(0,n-1))\ndu2 : input rank-1 array('f') with bounds (MAX(0,n-2))\nipiv : input rank-1 array('i') with bounds (n)\n\nReturns\n-------\ndlf : rank-1 array('f') with bounds (MAX(0,n-1))\ndf : rank-1 array('f') with bounds (n)\nduf : rank-1 array('f') with bounds (MAX(0,n-1))\ndu2 : rank-1 array('f') with bounds (MAX(0,n-2))\nipiv : rank-1 array('i') with bounds (n)\nx : rank-2 array('f') with bounds (ldx,nrhs)\nrcond : float\nferr : rank-1 array('f') with bounds (nrhs)\nberr : rank-1 array('f') with bounds (nrhs)\ninfo : int\n"
    ...

def sgttrf(dl, d, du, overwrite_dl=..., overwrite_d=..., overwrite_du=...) -> typing.Any:
    "dl,d,du,du2,ipiv,info = sgttrf(dl,d,du,[overwrite_dl,overwrite_d,overwrite_du])\n\nWrapper for ``sgttrf``.\n\nParameters\n----------\ndl : input rank-1 array('f') with bounds (n - 1)\nd : input rank-1 array('f') with bounds (n)\ndu : input rank-1 array('f') with bounds (n - 1)\n\nOther Parameters\n----------------\noverwrite_dl : input int, optional\n    Default: 0\noverwrite_d : input int, optional\n    Default: 0\noverwrite_du : input int, optional\n    Default: 0\n\nReturns\n-------\ndl : rank-1 array('f') with bounds (n - 1)\nd : rank-1 array('f') with bounds (n)\ndu : rank-1 array('f') with bounds (n - 1)\ndu2 : rank-1 array('f') with bounds (n - 2)\nipiv : rank-1 array('i') with bounds (n)\ninfo : int\n"
    ...

def sgttrs(dl, d, du, du2, ipiv, b, trans=..., overwrite_b=...) -> typing.Any:
    "x,info = sgttrs(dl,d,du,du2,ipiv,b,[trans,overwrite_b])\n\nWrapper for ``sgttrs``.\n\nParameters\n----------\ndl : input rank-1 array('f') with bounds (n - 1)\nd : input rank-1 array('f') with bounds (n)\ndu : input rank-1 array('f') with bounds (n - 1)\ndu2 : input rank-1 array('f') with bounds (n - 2)\nipiv : input rank-1 array('i') with bounds (n)\nb : input rank-2 array('f') with bounds (ldb,nrhs)\n\nOther Parameters\n----------------\ntrans : input string(len=1), optional\n    Default: 'N'\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('f') with bounds (ldb,nrhs) and b storage\ninfo : int\n"
    ...

def slamch(cmach) -> typing.Any:
    'slamch = slamch(cmach)\n\nWrapper for ``slamch``.\n\nParameters\n----------\ncmach : input string(len=1)\n\nReturns\n-------\nslamch : float\n'
    ...

def slange(norm, a) -> typing.Any:
    "n2 = slange(norm,a)\n\nWrapper for ``slange``.\n\nParameters\n----------\nnorm : input string(len=1)\na : input rank-2 array('f') with bounds (m,n)\n\nReturns\n-------\nn2 : float\n"
    ...

def slarf(v, tau, c, work, side=..., incv=..., overwrite_c=...) -> typing.Any:
    "c = slarf(v,tau,c,work,[side,incv,overwrite_c])\n\nWrapper for ``slarf``.\n\nParameters\n----------\nv : input rank-1 array('f') with bounds ((side[0]=='L'?(1 + (m-1)*abs(incv)):(1 + (n-1)*abs(incv))))\ntau : input float\nc : input rank-2 array('f') with bounds (m,n)\nwork : input rank-1 array('f') with bounds (lwork)\n\nOther Parameters\n----------------\nside : input string(len=1), optional\n    Default: 'L'\nincv : input int, optional\n    Default: 1\noverwrite_c : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('f') with bounds (m,n)\n"
    ...

def slarfg(n, alpha, x, incx=..., overwrite_x=...) -> typing.Any:
    "alpha,x,tau = slarfg(n,alpha,x,[incx,overwrite_x])\n\nWrapper for ``slarfg``.\n\nParameters\n----------\nn : input int\nalpha : input float\nx : input rank-1 array('f') with bounds (lx)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\n\nReturns\n-------\nalpha : float\nx : rank-1 array('f') with bounds (lx)\ntau : float\n"
    ...

def slartg(f, g) -> typing.Any:
    'cs,sn,r = slartg(f,g)\n\nWrapper for ``slartg``.\n\nParameters\n----------\nf : input float\ng : input float\n\nReturns\n-------\ncs : float\nsn : float\nr : float\n'
    ...

def slasd4(i, d, z, rho=...) -> typing.Any:
    "delta,sigma,work,info = slasd4(i,d,z,[rho])\n\nWrapper for ``slasd4``.\n\nParameters\n----------\ni : input int\nd : input rank-1 array('f') with bounds (n)\nz : input rank-1 array('f') with bounds (n)\n\nOther Parameters\n----------------\nrho : input float, optional\n    Default: 1.0\n\nReturns\n-------\ndelta : rank-1 array('f') with bounds (n)\nsigma : float\nwork : rank-1 array('f') with bounds (n)\ninfo : int\n"
    ...

def slaswp(a, piv, k1=..., k2=..., off=..., inc=..., overwrite_a=...) -> typing.Any:
    "a = slaswp(a,piv,[k1,k2,off,inc,overwrite_a])\n\nWrapper for ``slaswp``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (nrows,n)\npiv : input rank-1 array('i') with bounds (npiv)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nk1 : input int, optional\n    Default: 0\nk2 : input int, optional\n    Default: npiv-1\noff : input int, optional\n    Default: 0\ninc : input int, optional\n    Default: 1\n\nReturns\n-------\na : rank-2 array('f') with bounds (nrows,n)\n"
    ...

def slauum(c, lower=..., overwrite_c=...) -> typing.Any:
    "a,info = slauum(c,[lower,overwrite_c])\n\nWrapper for ``slauum``.\n\nParameters\n----------\nc : input rank-2 array('f') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_c : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\na : rank-2 array('f') with bounds (n,n) and c storage\ninfo : int\n"
    ...

def sorcsd(x11, x12, x21, x22, compute_u1=..., compute_u2=..., compute_v1t=..., compute_v2t=..., trans=..., signs=..., lwork=..., overwrite_x11=..., overwrite_x12=..., overwrite_x21=..., overwrite_x22=...) -> typing.Any:
    "cs11,cs12,cs21,cs22,theta,u1,u2,v1t,v2t,info = sorcsd(x11,x12,x21,x22,[compute_u1,compute_u2,compute_v1t,compute_v2t,trans,signs,lwork,overwrite_x11,overwrite_x12,overwrite_x21,overwrite_x22])\n\nWrapper for ``sorcsd``.\n\nParameters\n----------\nx11 : input rank-2 array('f') with bounds (p,q)\nx12 : input rank-2 array('f') with bounds (p,mmq)\nx21 : input rank-2 array('f') with bounds (mmp,q)\nx22 : input rank-2 array('f') with bounds (mmp,mmq)\n\nOther Parameters\n----------------\ncompute_u1 : input int, optional\n    Default: 1\ncompute_u2 : input int, optional\n    Default: 1\ncompute_v1t : input int, optional\n    Default: 1\ncompute_v2t : input int, optional\n    Default: 1\ntrans : input int, optional\n    Default: 0\nsigns : input int, optional\n    Default: 0\noverwrite_x11 : input int, optional\n    Default: 0\noverwrite_x12 : input int, optional\n    Default: 0\noverwrite_x21 : input int, optional\n    Default: 0\noverwrite_x22 : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: 2+2*m+5*MAX(1,q-1)+4*MAX(1,q)+8*q\n\nReturns\n-------\ncs11 : rank-2 array('f') with bounds (p,q) and x11 storage\ncs12 : rank-2 array('f') with bounds (p,mmq) and x12 storage\ncs21 : rank-2 array('f') with bounds (mmp,q) and x21 storage\ncs22 : rank-2 array('f') with bounds (mmp,mmq) and x22 storage\ntheta : rank-1 array('f') with bounds (min(min(p,mmp),min(q,mmq)))\nu1 : rank-2 array('f') with bounds ((compute_u1?p:0),(compute_u1?p:0))\nu2 : rank-2 array('f') with bounds ((compute_u2?mmp:0),(compute_u2?mmp:0))\nv1t : rank-2 array('f') with bounds ((compute_v1t?q:0),(compute_v1t?q:0))\nv2t : rank-2 array('f') with bounds ((compute_v2t?mmq:0),(compute_v2t?mmq:0))\ninfo : int\n"
    ...

def sorcsd_lwork(m, p, q) -> typing.Any:
    'work,info = sorcsd_lwork(m,p,q)\n\nWrapper for ``sorcsd_lwork``.\n\nParameters\n----------\nm : input int\np : input int\nq : input int\n\nReturns\n-------\nwork : float\ninfo : int\n'
    ...

def sorghr(a, tau, lo=..., hi=..., lwork=..., overwrite_a=...) -> typing.Any:
    "ht,info = sorghr(a,tau,[lo,hi,lwork,overwrite_a])\n\nWrapper for ``sorghr``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (n,n)\ntau : input rank-1 array('f') with bounds (n - 1)\n\nOther Parameters\n----------------\nlo : input int, optional\n    Default: 0\nhi : input int, optional\n    Default: n-1\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(hi-lo,1)\n\nReturns\n-------\nht : rank-2 array('f') with bounds (n,n) and a storage\ninfo : int\n"
    ...

def sorghr_lwork(n, lo=..., hi=...) -> typing.Any:
    'work,info = sorghr_lwork(n,[lo,hi])\n\nWrapper for ``sorghr_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlo : input int, optional\n    Default: 0\nhi : input int, optional\n    Default: n-1\n\nReturns\n-------\nwork : float\ninfo : int\n'
    ...

def sorgqr(a, tau, lwork=..., overwrite_a=...) -> typing.Any:
    "q,work,info = sorgqr(a,tau,[lwork,overwrite_a])\n\nWrapper for ``sorgqr``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (m,n)\ntau : input rank-1 array('f') with bounds (k)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(3*n,1)\n\nReturns\n-------\nq : rank-2 array('f') with bounds (m,n) and a storage\nwork : rank-1 array('f') with bounds (MAX(lwork,1))\ninfo : int\n"
    ...

def sorgrq(a, tau, lwork=..., overwrite_a=...) -> typing.Any:
    "q,work,info = sorgrq(a,tau,[lwork,overwrite_a])\n\nWrapper for ``sorgrq``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (m,n)\ntau : input rank-1 array('f') with bounds (k)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(3*m,1)\n\nReturns\n-------\nq : rank-2 array('f') with bounds (m,n) and a storage\nwork : rank-1 array('f') with bounds (MAX(lwork,1))\ninfo : int\n"
    ...

def sormqr(side, trans, a, tau, c, lwork, overwrite_c=...) -> typing.Any:
    "cq,work,info = sormqr(side,trans,a,tau,c,lwork,[overwrite_c])\n\nWrapper for ``sormqr``.\n\nParameters\n----------\nside : input string(len=1)\ntrans : input string(len=1)\na : input rank-2 array('f') with bounds (lda,k)\ntau : input rank-1 array('f') with bounds (k)\nc : input rank-2 array('f') with bounds (ldc,n)\nlwork : input int\n\nOther Parameters\n----------------\noverwrite_c : input int, optional\n    Default: 0\n\nReturns\n-------\ncq : rank-2 array('f') with bounds (ldc,n) and c storage\nwork : rank-1 array('f') with bounds (MAX(lwork,1))\ninfo : int\n"
    ...

def sormrz(a, tau, c, side=..., trans=..., lwork=..., overwrite_c=...) -> typing.Any:
    "cq,info = sormrz(a,tau,c,[side,trans,lwork,overwrite_c])\n\nWrapper for ``sormrz``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (k,nt)\ntau : input rank-1 array('f') with bounds (k)\nc : input rank-2 array('f') with bounds (m,n)\n\nOther Parameters\n----------------\nside : input string(len=1), optional\n    Default: 'L'\ntrans : input string(len=1), optional\n    Default: 'N'\noverwrite_c : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: MAX((side[0]=='L'?n:m),1)\n\nReturns\n-------\ncq : rank-2 array('f') with bounds (m,n) and c storage\ninfo : int\n"
    ...

def sormrz_lwork(m, n, side=..., trans=...) -> typing.Any:
    "work,info = sormrz_lwork(m,n,[side,trans])\n\nWrapper for ``sormrz_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\n\nOther Parameters\n----------------\nside : input string(len=1), optional\n    Default: 'L'\ntrans : input string(len=1), optional\n    Default: 'N'\n\nReturns\n-------\nwork : float\ninfo : int\n"
    ...

def spbsv(ab, b, lower=..., ldab=..., overwrite_ab=..., overwrite_b=...) -> typing.Any:
    "c,x,info = spbsv(ab,b,[lower,ldab,overwrite_ab,overwrite_b])\n\nWrapper for ``spbsv``.\n\nParameters\n----------\nab : input rank-2 array('f') with bounds (ldab,n)\nb : input rank-2 array('f') with bounds (ldb,nrhs)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\noverwrite_ab : input int, optional\n    Default: 0\nldab : input int, optional\n    Default: shape(ab,0)\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('f') with bounds (ldab,n) and ab storage\nx : rank-2 array('f') with bounds (ldb,nrhs) and b storage\ninfo : int\n"
    ...

def spbtrf(ab, lower=..., ldab=..., overwrite_ab=...) -> typing.Any:
    "c,info = spbtrf(ab,[lower,ldab,overwrite_ab])\n\nWrapper for ``spbtrf``.\n\nParameters\n----------\nab : input rank-2 array('f') with bounds (ldab,n)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\noverwrite_ab : input int, optional\n    Default: 0\nldab : input int, optional\n    Default: shape(ab,0)\n\nReturns\n-------\nc : rank-2 array('f') with bounds (ldab,n) and ab storage\ninfo : int\n"
    ...

def spbtrs(ab, b, lower=..., ldab=..., overwrite_b=...) -> typing.Any:
    "x,info = spbtrs(ab,b,[lower,ldab,overwrite_b])\n\nWrapper for ``spbtrs``.\n\nParameters\n----------\nab : input rank-2 array('f') with bounds (ldab,n)\nb : input rank-2 array('f') with bounds (ldb,nrhs)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\nldab : input int, optional\n    Default: shape(ab,0)\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('f') with bounds (ldb,nrhs) and b storage\ninfo : int\n"
    ...

def spftrf(n, a, transr=..., uplo=..., overwrite_a=...) -> typing.Any:
    "achol,info = spftrf(n,a,[transr,uplo,overwrite_a])\n\nWrapper for ``spftrf``.\n\nParameters\n----------\nn : input int\na : input rank-1 array('f') with bounds (nt)\n\nOther Parameters\n----------------\ntransr : input string(len=1), optional\n    Default: 'N'\nuplo : input string(len=1), optional\n    Default: 'U'\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\nachol : rank-1 array('f') with bounds (nt) and a storage\ninfo : int\n"
    ...

def spftri(n, a, transr=..., uplo=..., overwrite_a=...) -> typing.Any:
    "ainv,info = spftri(n,a,[transr,uplo,overwrite_a])\n\nWrapper for ``spftri``.\n\nParameters\n----------\nn : input int\na : input rank-1 array('f') with bounds (nt)\n\nOther Parameters\n----------------\ntransr : input string(len=1), optional\n    Default: 'N'\nuplo : input string(len=1), optional\n    Default: 'U'\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\nainv : rank-1 array('f') with bounds (nt) and a storage\ninfo : int\n"
    ...

def spftrs(n, a, b, transr=..., uplo=..., overwrite_b=...) -> typing.Any:
    "x,info = spftrs(n,a,b,[transr,uplo,overwrite_b])\n\nWrapper for ``spftrs``.\n\nParameters\n----------\nn : input int\na : input rank-1 array('f') with bounds (nt)\nb : input rank-2 array('f') with bounds (ldb,nhrs)\n\nOther Parameters\n----------------\ntransr : input string(len=1), optional\n    Default: 'N'\nuplo : input string(len=1), optional\n    Default: 'U'\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('f') with bounds (ldb,nhrs) and b storage\ninfo : int\n"
    ...

def spocon(a, anorm, uplo=...) -> typing.Any:
    "rcond,info = spocon(a,anorm,[uplo])\n\nWrapper for ``spocon``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (n,n)\nanorm : input float\n\nOther Parameters\n----------------\nuplo : input string(len=1), optional\n    Default: 'U'\n\nReturns\n-------\nrcond : float\ninfo : int\n"
    ...

def sposv(a, b, lower=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "c,x,info = sposv(a,b,[lower,overwrite_a,overwrite_b])\n\nWrapper for ``sposv``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (n,n)\nb : input rank-2 array('f') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('f') with bounds (n,n) and a storage\nx : rank-2 array('f') with bounds (n,nrhs) and b storage\ninfo : int\n"
    ...

def sposvx(a, b, fact=..., af=..., equed=..., s=..., lower=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "a_s,lu,equed,s,b_s,x,rcond,ferr,berr,info = sposvx(a,b,[fact,af,equed,s,lower,overwrite_a,overwrite_b])\n\nWrapper for ``sposvx``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (n,n)\nb : input rank-2 array('f') with bounds (n,nrhs)\n\nOther Parameters\n----------------\nfact : input string(len=1), optional\n    Default: 'E'\noverwrite_a : input int, optional\n    Default: 0\naf : input rank-2 array('f') with bounds (n,n)\nequed : input string(len=1), optional\n    Default: 'Y'\ns : input rank-1 array('f') with bounds (n)\noverwrite_b : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\na_s : rank-2 array('f') with bounds (n,n) and a storage\nlu : rank-2 array('f') with bounds (n,n) and af storage\nequed : string(len=1)\ns : rank-1 array('f') with bounds (n)\nb_s : rank-2 array('f') with bounds (n,nrhs) and b storage\nx : rank-2 array('f') with bounds (n,nrhs)\nrcond : float\nferr : rank-1 array('f') with bounds (nrhs)\nberr : rank-1 array('f') with bounds (nrhs)\ninfo : int\n"
    ...

def spotrf(a, lower=..., clean=..., overwrite_a=...) -> typing.Any:
    "c,info = spotrf(a,[lower,clean,overwrite_a])\n\nWrapper for ``spotrf``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\nclean : input int, optional\n    Default: 1\n\nReturns\n-------\nc : rank-2 array('f') with bounds (n,n) and a storage\ninfo : int\n"
    ...

def spotri(c, lower=..., overwrite_c=...) -> typing.Any:
    "inv_a,info = spotri(c,[lower,overwrite_c])\n\nWrapper for ``spotri``.\n\nParameters\n----------\nc : input rank-2 array('f') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_c : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\ninv_a : rank-2 array('f') with bounds (n,n) and c storage\ninfo : int\n"
    ...

def spotrs(c, b, lower=..., overwrite_b=...) -> typing.Any:
    "x,info = spotrs(c,b,[lower,overwrite_b])\n\nWrapper for ``spotrs``.\n\nParameters\n----------\nc : input rank-2 array('f') with bounds (n,n)\nb : input rank-2 array('f') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_b : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('f') with bounds (n,nrhs) and b storage\ninfo : int\n"
    ...

def sppcon(n, ap, anorm, lower=...) -> typing.Any:
    "rcond,info = sppcon(n,ap,anorm,[lower])\n\nWrapper for ``sppcon``.\n\nParameters\n----------\nn : input int\nap : input rank-1 array('f') with bounds (L)\nanorm : input float\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nrcond : float\ninfo : int\n"
    ...

def sppsv(n, ap, b, lower=..., overwrite_b=...) -> typing.Any:
    "x,info = sppsv(n,ap,b,[lower,overwrite_b])\n\nWrapper for ``sppsv``.\n\nParameters\n----------\nn : input int\nap : input rank-1 array('f') with bounds (L)\nb : input rank-2 array('f') with bounds (ldb,nrhs)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('f') with bounds (ldb,nrhs) and b storage\ninfo : int\n"
    ...

def spptrf(n, ap, lower=..., overwrite_ap=...) -> typing.Any:
    "ul,info = spptrf(n,ap,[lower,overwrite_ap])\n\nWrapper for ``spptrf``.\n\nParameters\n----------\nn : input int\nap : input rank-1 array('f') with bounds (L)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\noverwrite_ap : input int, optional\n    Default: 0\n\nReturns\n-------\nul : rank-1 array('f') with bounds (L) and ap storage\ninfo : int\n"
    ...

def spptri(n, ap, lower=..., overwrite_ap=...) -> typing.Any:
    "uli,info = spptri(n,ap,[lower,overwrite_ap])\n\nWrapper for ``spptri``.\n\nParameters\n----------\nn : input int\nap : input rank-1 array('f') with bounds (L)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\noverwrite_ap : input int, optional\n    Default: 0\n\nReturns\n-------\nuli : rank-1 array('f') with bounds (L) and ap storage\ninfo : int\n"
    ...

def spptrs(n, ap, b, lower=..., overwrite_b=...) -> typing.Any:
    "x,info = spptrs(n,ap,b,[lower,overwrite_b])\n\nWrapper for ``spptrs``.\n\nParameters\n----------\nn : input int\nap : input rank-1 array('f') with bounds (L)\nb : input rank-2 array('f') with bounds (ldb,nrhs)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('f') with bounds (ldb,nrhs) and b storage\ninfo : int\n"
    ...

def spstf2(a, tol=..., lower=..., overwrite_a=...) -> typing.Any:
    "c,piv,rank_c,info = spstf2(a,[tol,lower,overwrite_a])\n\nWrapper for ``spstf2``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\ntol : input float, optional\n    Default: -1.0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('f') with bounds (n,n) and a storage\npiv : rank-1 array('i') with bounds (n)\nrank_c : int\ninfo : int\n"
    ...

def spstrf(a, tol=..., lower=..., overwrite_a=...) -> typing.Any:
    "c,piv,rank_c,info = spstrf(a,[tol,lower,overwrite_a])\n\nWrapper for ``spstrf``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\ntol : input float, optional\n    Default: -1.0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('f') with bounds (n,n) and a storage\npiv : rank-1 array('i') with bounds (n)\nrank_c : int\ninfo : int\n"
    ...

def spteqr(d, e, z, compute_z=..., overwrite_d=..., overwrite_e=..., overwrite_z=...) -> typing.Any:
    "d,e,z,info = spteqr(d,e,z,[compute_z,overwrite_d,overwrite_e,overwrite_z])\n\nWrapper for ``spteqr``.\n\nParameters\n----------\nd : input rank-1 array('f') with bounds (n)\ne : input rank-1 array('f') with bounds ((n>0?n-1:0))\nz : input rank-2 array('f') with bounds ((compute_z==0?shape(z, 0):max(1,n)),(compute_z==0?shape(z, 1):n))\n\nOther Parameters\n----------------\ncompute_z : input int, optional\n    Default: 0\noverwrite_d : input int, optional\n    Default: 0\noverwrite_e : input int, optional\n    Default: 0\noverwrite_z : input int, optional\n    Default: 0\n\nReturns\n-------\nd : rank-1 array('f') with bounds (n)\ne : rank-1 array('f') with bounds ((n>0?n-1:0))\nz : rank-2 array('f') with bounds ((compute_z==0?shape(z, 0):max(1,n)),(compute_z==0?shape(z, 1):n))\ninfo : int\n"
    ...

def sptsv(d, e, b, overwrite_d=..., overwrite_e=..., overwrite_b=...) -> typing.Any:
    "d,du,x,info = sptsv(d,e,b,[overwrite_d,overwrite_e,overwrite_b])\n\nWrapper for ``sptsv``.\n\nParameters\n----------\nd : input rank-1 array('f') with bounds (n)\ne : input rank-1 array('f') with bounds (n - 1)\nb : input rank-2 array('f') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_d : input int, optional\n    Default: 0\noverwrite_e : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nd : rank-1 array('f') with bounds (n)\ndu : rank-1 array('f') with bounds (n - 1) and e storage\nx : rank-2 array('f') with bounds (n,nrhs) and b storage\ninfo : int\n"
    ...

def sptsvx(d, e, b, fact=..., df=..., ef=...) -> typing.Any:
    "df,ef,x,rcond,ferr,berr,info = sptsvx(d,e,b,[fact,df,ef])\n\nWrapper for ``sptsvx``.\n\nParameters\n----------\nd : input rank-1 array('f') with bounds (n)\ne : input rank-1 array('f') with bounds (max(0, n-1))\nb : input rank-2 array('f') with bounds (ldb,nrhs)\n\nOther Parameters\n----------------\nfact : input string(len=1), optional\n    Default: 'N'\ndf : input rank-1 array('f') with bounds (n)\nef : input rank-1 array('f') with bounds (max(0, n-1))\n\nReturns\n-------\ndf : rank-1 array('f') with bounds (n)\nef : rank-1 array('f') with bounds (max(0, n-1))\nx : rank-2 array('f') with bounds (ldx,nrhs)\nrcond : float\nferr : rank-1 array('f') with bounds (nrhs)\nberr : rank-1 array('f') with bounds (nrhs)\ninfo : int\n"
    ...

def spttrf(d, e, overwrite_d=..., overwrite_e=...) -> typing.Any:
    "d,e,info = spttrf(d,e,[overwrite_d,overwrite_e])\n\nWrapper for ``spttrf``.\n\nParameters\n----------\nd : input rank-1 array('f') with bounds (n)\ne : input rank-1 array('f') with bounds ((n>0?n-1:0))\n\nOther Parameters\n----------------\noverwrite_d : input int, optional\n    Default: 0\noverwrite_e : input int, optional\n    Default: 0\n\nReturns\n-------\nd : rank-1 array('f') with bounds (n)\ne : rank-1 array('f') with bounds ((n>0?n-1:0))\ninfo : int\n"
    ...

def spttrs(d, e, b, overwrite_b=...) -> typing.Any:
    "x,info = spttrs(d,e,b,[overwrite_b])\n\nWrapper for ``spttrs``.\n\nParameters\n----------\nd : input rank-1 array('f') with bounds (n)\ne : input rank-1 array('f') with bounds ((n>0?n-1:0))\nb : input rank-2 array('f') with bounds (ldb,nrhs)\n\nOther Parameters\n----------------\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('f') with bounds (ldb,nrhs) and b storage\ninfo : int\n"
    ...

def ssbev(ab, compute_v=..., lower=..., ldab=..., overwrite_ab=...) -> typing.Any:
    "w,z,info = ssbev(ab,[compute_v,lower,ldab,overwrite_ab])\n\nWrapper for ``ssbev``.\n\nParameters\n----------\nab : input rank-2 array('f') with bounds (ldab,n)\n\nOther Parameters\n----------------\noverwrite_ab : input int, optional\n    Default: 1\ncompute_v : input int, optional\n    Default: 1\nlower : input int, optional\n    Default: 0\nldab : input int, optional\n    Default: shape(ab,0)\n\nReturns\n-------\nw : rank-1 array('f') with bounds (n)\nz : rank-2 array('f') with bounds (ldz,ldz)\ninfo : int\n"
    ...

def ssbevd(ab, compute_v=..., lower=..., ldab=..., liwork=..., overwrite_ab=...) -> typing.Any:
    "w,z,info = ssbevd(ab,[compute_v,lower,ldab,liwork,overwrite_ab])\n\nWrapper for ``ssbevd``.\n\nParameters\n----------\nab : input rank-2 array('f') with bounds (ldab,n)\n\nOther Parameters\n----------------\noverwrite_ab : input int, optional\n    Default: 1\ncompute_v : input int, optional\n    Default: 1\nlower : input int, optional\n    Default: 0\nldab : input int, optional\n    Default: shape(ab,0)\nliwork : input int, optional\n    Default: (compute_v?3+5*n:1)\n\nReturns\n-------\nw : rank-1 array('f') with bounds (n)\nz : rank-2 array('f') with bounds (ldz,ldz)\ninfo : int\n"
    ...

def ssbevx(ab, vl, vu, il, iu, ldab=..., compute_v=..., range=..., lower=..., abstol=..., mmax=..., overwrite_ab=...) -> typing.Any:
    "w,z,m,ifail,info = ssbevx(ab,vl,vu,il,iu,[ldab,compute_v,range,lower,abstol,mmax,overwrite_ab])\n\nWrapper for ``ssbevx``.\n\nParameters\n----------\nab : input rank-2 array('f') with bounds (ldab,n)\nvl : input float\nvu : input float\nil : input int\niu : input int\n\nOther Parameters\n----------------\noverwrite_ab : input int, optional\n    Default: 1\nldab : input int, optional\n    Default: shape(ab,0)\ncompute_v : input int, optional\n    Default: 1\nrange : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\nabstol : input float, optional\n    Default: 0.0\nmmax : input int, optional\n    Default: (compute_v?(range==2?(iu-il+1):n):1)\n\nReturns\n-------\nw : rank-1 array('f') with bounds (n)\nz : rank-2 array('f') with bounds (ldz,mmax)\nm : int\nifail : rank-1 array('i') with bounds ((compute_v?n:1))\ninfo : int\n"
    ...

def ssfrk(n, k, alpha, a, beta, c, transr=..., uplo=..., trans=..., overwrite_c=...) -> typing.Any:
    "cout = ssfrk(n,k,alpha,a,beta,c,[transr,uplo,trans,overwrite_c])\n\nWrapper for ``ssfrk``.\n\nParameters\n----------\nn : input int\nk : input int\nalpha : input float\na : input rank-2 array('f') with bounds (lda,ka)\nbeta : input float\nc : input rank-1 array('f') with bounds (nt)\n\nOther Parameters\n----------------\ntransr : input string(len=1), optional\n    Default: 'N'\nuplo : input string(len=1), optional\n    Default: 'U'\ntrans : input string(len=1), optional\n    Default: 'N'\noverwrite_c : input int, optional\n    Default: 0\n\nReturns\n-------\ncout : rank-1 array('f') with bounds (nt) and c storage\n"
    ...

def sstebz(d, e, range, vl, vu, il, iu, tol, order) -> typing.Any:
    "m,w,iblock,isplit,info = sstebz(d,e,range,vl,vu,il,iu,tol,order)\n\nWrapper for ``sstebz``.\n\nParameters\n----------\nd : input rank-1 array('f') with bounds (n)\ne : input rank-1 array('f') with bounds (n - 1)\nrange : input int\nvl : input float\nvu : input float\nil : input int\niu : input int\ntol : input float\norder : input string(len=1)\n\nReturns\n-------\nm : int\nw : rank-1 array('f') with bounds (n)\niblock : rank-1 array('i') with bounds (n)\nisplit : rank-1 array('i') with bounds (n)\ninfo : int\n"
    ...

def sstein(d, e, w, iblock, isplit) -> typing.Any:
    "z,info = sstein(d,e,w,iblock,isplit)\n\nWrapper for ``sstein``.\n\nParameters\n----------\nd : input rank-1 array('f') with bounds (n)\ne : input rank-1 array('f') with bounds (n - 1)\nw : input rank-1 array('f') with bounds (m)\niblock : input rank-1 array('i') with bounds (n)\nisplit : input rank-1 array('i') with bounds (n)\n\nReturns\n-------\nz : rank-2 array('f') with bounds (ldz,m)\ninfo : int\n"
    ...

def sstemr(d, e, range, vl, vu, il, iu, compute_v=..., lwork=..., liwork=..., overwrite_d=...) -> typing.Any:
    "m,w,z,info = sstemr(d,e,range,vl,vu,il,iu,[compute_v,lwork,liwork,overwrite_d])\n\nWrapper for ``sstemr``.\n\nParameters\n----------\nd : input rank-1 array('f') with bounds (n)\ne : input rank-1 array('f') with bounds (n)\nrange : input int\nvl : input float\nvu : input float\nil : input int\niu : input int\n\nOther Parameters\n----------------\noverwrite_d : input int, optional\n    Default: 0\ncompute_v : input int, optional\n    Default: 1\nlwork : input int, optional\n    Default: max((compute_v?18*n:12*n),1)\nliwork : input int, optional\n    Default: (compute_v?10*n:8*n)\n\nReturns\n-------\nm : int\nw : rank-1 array('f') with bounds (n)\nz : rank-2 array('f') with bounds (n,n)\ninfo : int\n"
    ...

def sstemr_lwork(d, e, range, vl, vu, il, iu, compute_v=..., overwrite_d=..., overwrite_e=...) -> typing.Any:
    "work,iwork,info = sstemr_lwork(d,e,range,vl,vu,il,iu,[compute_v,overwrite_d,overwrite_e])\n\nWrapper for ``sstemr_lwork``.\n\nParameters\n----------\nd : input rank-1 array('f') with bounds (n)\ne : input rank-1 array('f') with bounds (n)\nrange : input int\nvl : input float\nvu : input float\nil : input int\niu : input int\n\nOther Parameters\n----------------\noverwrite_d : input int, optional\n    Default: 0\noverwrite_e : input int, optional\n    Default: 0\ncompute_v : input int, optional\n    Default: 1\n\nReturns\n-------\nwork : float\niwork : int\ninfo : int\n"
    ...

def ssterf(d, e, overwrite_d=..., overwrite_e=...) -> typing.Any:
    "vals,info = ssterf(d,e,[overwrite_d,overwrite_e])\n\nWrapper for ``ssterf``.\n\nParameters\n----------\nd : input rank-1 array('f') with bounds (n)\ne : input rank-1 array('f') with bounds (n - 1)\n\nOther Parameters\n----------------\noverwrite_d : input int, optional\n    Default: 0\noverwrite_e : input int, optional\n    Default: 0\n\nReturns\n-------\nvals : rank-1 array('f') with bounds (n) and d storage\ninfo : int\n"
    ...

def sstev(d, e, compute_v=..., overwrite_d=..., overwrite_e=...) -> typing.Any:
    "vals,z,info = sstev(d,e,[compute_v,overwrite_d,overwrite_e])\n\nWrapper for ``sstev``.\n\nParameters\n----------\nd : input rank-1 array('f') with bounds (n)\ne : input rank-1 array('f') with bounds (MAX(n-1,1))\n\nOther Parameters\n----------------\noverwrite_d : input int, optional\n    Default: 0\noverwrite_e : input int, optional\n    Default: 0\ncompute_v : input int, optional\n    Default: 1\n\nReturns\n-------\nvals : rank-1 array('f') with bounds (n) and d storage\nz : rank-2 array('f') with bounds (ldz,(compute_v?n:1))\ninfo : int\n"
    ...

def ssycon(a, ipiv, anorm, lower=...) -> typing.Any:
    "rcond,info = ssycon(a,ipiv,anorm,[lower])\n\nWrapper for ``ssycon``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (n,n)\nipiv : input rank-1 array('i') with bounds (n)\nanorm : input float\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nrcond : float\ninfo : int\n"
    ...

def ssyconv(a, ipiv, lower=..., way=..., overwrite_a=...) -> typing.Any:
    "a,e,info = ssyconv(a,ipiv,[lower,way,overwrite_a])\n\nWrapper for ``ssyconv``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (n,n)\nipiv : input rank-1 array('i') with bounds (n)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\nway : input int, optional\n    Default: 0\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\na : rank-2 array('f') with bounds (n,n)\ne : rank-1 array('f') with bounds (n)\ninfo : int\n"
    ...

def ssyequb(a, lower=...) -> typing.Any:
    "s,scond,amax,info = ssyequb(a,[lower])\n\nWrapper for ``ssyequb``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (lda,n)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\ns : rank-1 array('f') with bounds (n)\nscond : float\namax : float\ninfo : int\n"
    ...

def ssyev(a, compute_v=..., lower=..., lwork=..., overwrite_a=...) -> typing.Any:
    "w,v,info = ssyev(a,[compute_v,lower,lwork,overwrite_a])\n\nWrapper for ``ssyev``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (n,n)\n\nOther Parameters\n----------------\ncompute_v : input int, optional\n    Default: 1\nlower : input int, optional\n    Default: 0\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(3*n-1,1)\n\nReturns\n-------\nw : rank-1 array('f') with bounds (n)\nv : rank-2 array('f') with bounds (n,n) and a storage\ninfo : int\n"
    ...

def ssyev_lwork(n, lower=...) -> typing.Any:
    'work,info = ssyev_lwork(n,[lower])\n\nWrapper for ``ssyev_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nwork : float\ninfo : int\n'
    ...

def ssyevd(a, compute_v=..., lower=..., lwork=..., liwork=..., overwrite_a=...) -> typing.Any:
    "w,v,info = ssyevd(a,[compute_v,lower,lwork,liwork,overwrite_a])\n\nWrapper for ``ssyevd``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (n,n)\n\nOther Parameters\n----------------\ncompute_v : input int, optional\n    Default: 1\nlower : input int, optional\n    Default: 0\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max((compute_v?1+6*n+2*n*n:2*n+1),1)\nliwork : input int, optional\n    Default: (compute_v?3+5*n:1)\n\nReturns\n-------\nw : rank-1 array('f') with bounds (n)\nv : rank-2 array('f') with bounds (n,n) and a storage\ninfo : int\n"
    ...

def ssyevd_lwork(n, compute_v=..., lower=...) -> typing.Any:
    'work,iwork,info = ssyevd_lwork(n,[compute_v,lower])\n\nWrapper for ``ssyevd_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\ncompute_v : input int, optional\n    Default: 1\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nwork : float\niwork : int\ninfo : int\n'
    ...

def ssyevr(a, compute_v=..., range=..., lower=..., vl=..., vu=..., il=..., iu=..., abstol=..., lwork=..., liwork=..., overwrite_a=...) -> typing.Any:
    "w,z,m,isuppz,info = ssyevr(a,[compute_v,range,lower,vl,vu,il,iu,abstol,lwork,liwork,overwrite_a])\n\nWrapper for ``ssyevr``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds ``(n,n)``\n\nOther Parameters\n----------------\ncompute_v : input int, optional\n    Default ``1``\nrange : input string(len=1), optional\n    Default ``'A'``\nlower : input int, optional\n    Default ``0``\noverwrite_a : input int, optional\n    Default ``0``\nvl : input float, optional\n    Default ``0.0``\nvu : input float, optional\n    Default ``1.0``\nil : input int, optional\n    Default ``1``\niu : input int, optional\n    Default ``n``\nabstol : input float, optional\n    Default ``0.0``\nlwork : input int, optional\n    Default ``max(26*n,1)``\nliwork : input int, optional\n    Default ``max(1,10*n)``\n\nReturns\n-------\nw : rank-1 array('f') with bounds ``(n)``\nz : rank-2 array('f') with bounds ``((compute_v?MAX(0,n):0),(compute_v?(*range=='I'?iu-il+1:MAX(1,n)):0))``\nm : int\nisuppz : rank-1 array('i') with bounds ``((compute_v?(2*(*range=='A'||(*range=='I' && iu-il+1==n)?n:0)):0))``\ninfo : int\n"
    ...

def ssyevr_lwork(n, lower=...) -> typing.Any:
    'work,iwork,info = ssyevr_lwork(n,[lower])\n\nWrapper for ``ssyevr_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nwork : float\niwork : int\ninfo : int\n'
    ...

def ssyevx(a, compute_v=..., range=..., lower=..., vl=..., vu=..., il=..., iu=..., abstol=..., lwork=..., overwrite_a=...) -> typing.Any:
    "w,z,m,ifail,info = ssyevx(a,[compute_v,range,lower,vl,vu,il,iu,abstol,lwork,overwrite_a])\n\nWrapper for ``ssyevx``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds ``(n,n)``\n\nOther Parameters\n----------------\ncompute_v : input int, optional\n    Default ``1``\nrange : input string(len=1), optional\n    Default ``'A'``\nlower : input int, optional\n    Default ``0``\noverwrite_a : input int, optional\n    Default ``0``\nvl : input float, optional\n    Default ``0.0``\nvu : input float, optional\n    Default ``1.0``\nil : input int, optional\n    Default ``1``\niu : input int, optional\n    Default ``n``\nabstol : input float, optional\n    Default ``0.0``\nlwork : input int, optional\n    Default ``max(8*n,1)``\n\nReturns\n-------\nw : rank-1 array('f') with bounds ``(n)``\nz : rank-2 array('f') with bounds ``((compute_v?MAX(0,n):0),(compute_v?(*range=='I'?iu-il+1:MAX(1,n)):0))``\nm : int\nifail : rank-1 array('i') with bounds ``((compute_v?n:0))``\ninfo : int\n"
    ...

def ssyevx_lwork(n, lower=...) -> typing.Any:
    'work,info = ssyevx_lwork(n,[lower])\n\nWrapper for ``ssyevx_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nwork : float\ninfo : int\n'
    ...

def ssygst(a, b, itype=..., lower=..., overwrite_a=...) -> typing.Any:
    "c,info = ssygst(a,b,[itype,lower,overwrite_a])\n\nWrapper for ``ssygst``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (n,n)\nb : input rank-2 array('f') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nitype : input int, optional\n    Default: 1\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('f') with bounds (n,n) and a storage\ninfo : int\n"
    ...

def ssygv(a, b, itype=..., jobz=..., uplo=..., lwork=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "w,v,info = ssygv(a,b,[itype,jobz,uplo,lwork,overwrite_a,overwrite_b])\n\nWrapper for ``ssygv``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (n,n)\nb : input rank-2 array('f') with bounds (n,n)\n\nOther Parameters\n----------------\nitype : input int, optional\n    Default: 1\njobz : input string(len=1), optional\n    Default: 'V'\nuplo : input string(len=1), optional\n    Default: 'L'\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(3*n-1,1)\n\nReturns\n-------\nw : rank-1 array('f') with bounds (n)\nv : rank-2 array('f') with bounds (n,n) and a storage\ninfo : int\n"
    ...

def ssygv_lwork(n, uplo=...) -> typing.Any:
    "work,info = ssygv_lwork(n,[uplo])\n\nWrapper for ``ssygv_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nuplo : input string(len=1), optional\n    Default: 'L'\n\nReturns\n-------\nwork : float\ninfo : int\n"
    ...

def ssygvd(a, b, itype=..., jobz=..., uplo=..., lwork=..., liwork=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "w,v,info = ssygvd(a,b,[itype,jobz,uplo,lwork,liwork,overwrite_a,overwrite_b])\n\nWrapper for ``ssygvd``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds ``(n,n)``\nb : input rank-2 array('f') with bounds ``(n,n)``\n\nOther Parameters\n----------------\nitype : input int, optional\n    Default ``1``\njobz : input string(len=1), optional\n    Default ``'V'``\nuplo : input string(len=1), optional\n    Default ``'L'``\noverwrite_a : input int, optional\n    Default ``0``\noverwrite_b : input int, optional\n    Default ``0``\nlwork : input int, optional\n    Default ``(*jobz=='N'?2*n+1:1+6*n+2*n*n)``\nliwork : input int, optional\n    Default ``(*jobz=='N'?1:5*n+3)``\n\nReturns\n-------\nw : rank-1 array('f') with bounds ``(n)``\nv : rank-2 array('f') with bounds ``(n,n)`` with ``a`` storage\ninfo : int\n"
    ...

def ssygvx(a, b, itype=..., jobz=..., range=..., uplo=..., vl=..., vu=..., il=..., iu=..., abstol=..., lwork=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "w,z,m,ifail,info = ssygvx(a,b,[itype,jobz,range,uplo,vl,vu,il,iu,abstol,lwork,overwrite_a,overwrite_b])\n\nWrapper for ``ssygvx``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (n,n)\nb : input rank-2 array('f') with bounds (n,n)\n\nOther Parameters\n----------------\nitype : input int, optional\n    Default: 1\njobz : input string(len=1), optional\n    Default: 'V'\nrange : input string(len=1), optional\n    Default: 'A'\nuplo : input string(len=1), optional\n    Default: 'L'\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nvl : input float, optional\n    Default: 0.0\nvu : input float, optional\n    Default: 1.0\nil : input int, optional\n    Default: 1\niu : input int, optional\n    Default: n\nabstol : input float, optional\n    Default: 0.0\nlwork : input int, optional\n    Default: max(8*n,1)\n\nReturns\n-------\nw : rank-1 array('f') with bounds (n)\nz : rank-2 array('f') with bounds ((jobz[0]=='V'?MAX(0,n):0),(jobz[0]=='V'?(range[0]=='I'?iu-il+1:MAX(1,n)):0))\nm : int\nifail : rank-1 array('i') with bounds ((jobz[0]=='N'?0:n))\ninfo : int\n"
    ...

def ssygvx_lwork(n, uplo=...) -> typing.Any:
    "work,info = ssygvx_lwork(n,[uplo])\n\nWrapper for ``ssygvx_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nuplo : input string(len=1), optional\n    Default: 'L'\n\nReturns\n-------\nwork : float\ninfo : int\n"
    ...

def ssysv(a, b, lwork=..., lower=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "udut,ipiv,x,info = ssysv(a,b,[lwork,lower,overwrite_a,overwrite_b])\n\nWrapper for ``ssysv``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (n,n)\nb : input rank-2 array('f') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(n,1)\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nudut : rank-2 array('f') with bounds (n,n) and a storage\nipiv : rank-1 array('i') with bounds (n)\nx : rank-2 array('f') with bounds (n,nrhs) and b storage\ninfo : int\n"
    ...

def ssysv_lwork(n, lower=...) -> typing.Any:
    'work,info = ssysv_lwork(n,[lower])\n\nWrapper for ``ssysv_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nwork : float\ninfo : int\n'
    ...

def ssysvx(a, b, af=..., ipiv=..., lwork=..., factored=..., lower=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "a_s,udut,ipiv,b_s,x,rcond,ferr,berr,info = ssysvx(a,b,[af,ipiv,lwork,factored,lower,overwrite_a,overwrite_b])\n\nWrapper for ``ssysvx``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (n,n)\nb : input rank-2 array('f') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\naf : input rank-2 array('f') with bounds (n,n)\nipiv : input rank-1 array('i') with bounds (n)\noverwrite_b : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(3*n,1)\nfactored : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\na_s : rank-2 array('f') with bounds (n,n) and a storage\nudut : rank-2 array('f') with bounds (n,n) and af storage\nipiv : rank-1 array('i') with bounds (n)\nb_s : rank-2 array('f') with bounds (n,nrhs) and b storage\nx : rank-2 array('f') with bounds (n,nrhs)\nrcond : float\nferr : rank-1 array('f') with bounds (nrhs)\nberr : rank-1 array('f') with bounds (nrhs)\ninfo : int\n"
    ...

def ssysvx_lwork(n, lower=...) -> typing.Any:
    'work,info = ssysvx_lwork(n,[lower])\n\nWrapper for ``ssysvx_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nwork : float\ninfo : int\n'
    ...

def ssytf2(a, lower=..., overwrite_a=...) -> typing.Any:
    "ldu,ipiv,info = ssytf2(a,[lower,overwrite_a])\n\nWrapper for ``ssytf2``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (n,n)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\nldu : rank-2 array('f') with bounds (n,n) and a storage\nipiv : rank-1 array('i') with bounds (n)\ninfo : int\n"
    ...

def ssytrd(a, lower=..., lwork=..., overwrite_a=...) -> typing.Any:
    "c,d,e,tau,info = ssytrd(a,[lower,lwork,overwrite_a])\n\nWrapper for ``ssytrd``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (lda,n)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: MAX(n,1)\n\nReturns\n-------\nc : rank-2 array('f') with bounds (lda,n) and a storage\nd : rank-1 array('f') with bounds (n)\ne : rank-1 array('f') with bounds (n - 1)\ntau : rank-1 array('f') with bounds (n - 1)\ninfo : int\n"
    ...

def ssytrd_lwork(n, lower=...) -> typing.Any:
    'work,info = ssytrd_lwork(n,[lower])\n\nWrapper for ``ssytrd_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nwork : float\ninfo : int\n'
    ...

def ssytrf(a, lower=..., lwork=..., overwrite_a=...) -> typing.Any:
    "ldu,ipiv,info = ssytrf(a,[lower,lwork,overwrite_a])\n\nWrapper for ``ssytrf``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (n,n)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(n,1)\n\nReturns\n-------\nldu : rank-2 array('f') with bounds (n,n) and a storage\nipiv : rank-1 array('i') with bounds (n)\ninfo : int\n"
    ...

def ssytrf_lwork(n, lower=...) -> typing.Any:
    'work,info = ssytrf_lwork(n,[lower])\n\nWrapper for ``ssytrf_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nwork : float\ninfo : int\n'
    ...

def stbtrs(ab, b, uplo=..., trans=..., diag=..., overwrite_b=...) -> typing.Any:
    "x,info = stbtrs(ab,b,[uplo,trans,diag,overwrite_b])\n\nWrapper for ``stbtrs``.\n\nParameters\n----------\nab : input rank-2 array('f') with bounds (ldab,n)\nb : input rank-2 array('f') with bounds (ldb,nrhs)\n\nOther Parameters\n----------------\nuplo : input string(len=1), optional\n    Default: 'U'\ntrans : input string(len=1), optional\n    Default: 'N'\ndiag : input string(len=1), optional\n    Default: 'N'\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('f') with bounds (ldb,nrhs) and b storage\ninfo : int\n"
    ...

def stfsm(alpha, a, b, transr=..., side=..., uplo=..., trans=..., diag=..., overwrite_b=...) -> typing.Any:
    "x = stfsm(alpha,a,b,[transr,side,uplo,trans,diag,overwrite_b])\n\nWrapper for ``stfsm``.\n\nParameters\n----------\nalpha : input float\na : input rank-1 array('f') with bounds (nt)\nb : input rank-2 array('f') with bounds (m,n)\n\nOther Parameters\n----------------\ntransr : input string(len=1), optional\n    Default: 'N'\nside : input string(len=1), optional\n    Default: 'L'\nuplo : input string(len=1), optional\n    Default: 'U'\ntrans : input string(len=1), optional\n    Default: 'N'\ndiag : input string(len=1), optional\n    Default: 'N'\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('f') with bounds (m,n) and b storage\n"
    ...

def stfttp(n, arf, transr=..., uplo=...) -> typing.Any:
    "ap,info = stfttp(n,arf,[transr,uplo])\n\nWrapper for ``stfttp``.\n\nParameters\n----------\nn : input int\narf : input rank-1 array('f') with bounds (nt)\n\nOther Parameters\n----------------\ntransr : input string(len=1), optional\n    Default: 'N'\nuplo : input string(len=1), optional\n    Default: 'U'\n\nReturns\n-------\nap : rank-1 array('f') with bounds (nt)\ninfo : int\n"
    ...

def stfttr(n, arf, transr=..., uplo=...) -> typing.Any:
    "a,info = stfttr(n,arf,[transr,uplo])\n\nWrapper for ``stfttr``.\n\nParameters\n----------\nn : input int\narf : input rank-1 array('f') with bounds (nt)\n\nOther Parameters\n----------------\ntransr : input string(len=1), optional\n    Default: 'N'\nuplo : input string(len=1), optional\n    Default: 'U'\n\nReturns\n-------\na : rank-2 array('f') with bounds (lda,n)\ninfo : int\n"
    ...

def stgsen(select, a, b, q, z, lwork=..., liwork=..., overwrite_a=..., overwrite_b=..., overwrite_q=..., overwrite_z=...) -> typing.Any:
    "a,b,alphar,alphai,beta,q,z,m,pl,pr,dif,work,iwork,info = stgsen(select,a,b,q,z,[lwork,liwork,overwrite_a,overwrite_b,overwrite_q,overwrite_z])\n\nWrapper for ``stgsen``.\n\nParameters\n----------\nselect : input rank-1 array('i') with bounds (n)\na : input rank-2 array('f') with bounds (lda,n)\nb : input rank-2 array('f') with bounds (ldb,n)\nq : input rank-2 array('f') with bounds (ldq,n)\nz : input rank-2 array('f') with bounds (ldz,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\noverwrite_q : input int, optional\n    Default: 0\noverwrite_z : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(MAX(4*n+16,2*m*(n-m)),1)\nliwork : input int, optional\n    Default: n+6\n\nReturns\n-------\na : rank-2 array('f') with bounds (lda,n)\nb : rank-2 array('f') with bounds (ldb,n)\nalphar : rank-1 array('f') with bounds (n)\nalphai : rank-1 array('f') with bounds (n)\nbeta : rank-1 array('f') with bounds (n)\nq : rank-2 array('f') with bounds (ldq,n)\nz : rank-2 array('f') with bounds (ldz,n)\nm : int\npl : float\npr : float\ndif : rank-1 array('f') with bounds (2)\nwork : rank-1 array('f') with bounds (MAX(lwork,1))\niwork : rank-1 array('i') with bounds (MAX(1,liwork))\ninfo : int\n"
    ...

def stpmqrt(l, v, t, a, b, side=..., trans=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "a,b,info = stpmqrt(l,v,t,a,b,[side,trans,overwrite_a,overwrite_b])\n\nWrapper for ``stpmqrt``.\n\nParameters\n----------\nl : input int\nv : input rank-2 array('f') with bounds ((side[0]=='L'?m:n),k)\nt : input rank-2 array('f') with bounds (nb,k)\na : input rank-2 array('f') with bounds ((side[0]=='L'?k:m),(side[0]=='L'?n:k))\nb : input rank-2 array('f') with bounds (m,n)\n\nOther Parameters\n----------------\nside : input string(len=1), optional\n    Default: 'L'\ntrans : input string(len=1), optional\n    Default: 'N'\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\na : rank-2 array('f') with bounds ((side[0]=='L'?k:m),(side[0]=='L'?n:k))\nb : rank-2 array('f') with bounds (m,n)\ninfo : int\n"
    ...

def stpqrt(l, nb, a, b, overwrite_a=..., overwrite_b=...) -> typing.Any:
    "a,b,t,info = stpqrt(l,nb,a,b,[overwrite_a,overwrite_b])\n\nWrapper for ``stpqrt``.\n\nParameters\n----------\nl : input int\nnb : input int\na : input rank-2 array('f') with bounds (n,n)\nb : input rank-2 array('f') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\na : rank-2 array('f') with bounds (n,n)\nb : rank-2 array('f') with bounds (m,n)\nt : rank-2 array('f') with bounds (nb,n)\ninfo : int\n"
    ...

def stpttf(n, ap, transr=..., uplo=...) -> typing.Any:
    "arf,info = stpttf(n,ap,[transr,uplo])\n\nWrapper for ``stpttf``.\n\nParameters\n----------\nn : input int\nap : input rank-1 array('f') with bounds (nt)\n\nOther Parameters\n----------------\ntransr : input string(len=1), optional\n    Default: 'N'\nuplo : input string(len=1), optional\n    Default: 'U'\n\nReturns\n-------\narf : rank-1 array('f') with bounds (nt)\ninfo : int\n"
    ...

def stpttr(n, ap, uplo=...) -> typing.Any:
    "a,info = stpttr(n,ap,[uplo])\n\nWrapper for ``stpttr``.\n\nParameters\n----------\nn : input int\nap : input rank-1 array('f') with bounds (nt)\n\nOther Parameters\n----------------\nuplo : input string(len=1), optional\n    Default: 'U'\n\nReturns\n-------\na : rank-2 array('f') with bounds (n,n)\ninfo : int\n"
    ...

def strsyl(a, b, c, trana=..., tranb=..., isgn=..., overwrite_c=...) -> typing.Any:
    "x,scale,info = strsyl(a,b,c,[trana,tranb,isgn,overwrite_c])\n\nWrapper for ``strsyl``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (m,m)\nb : input rank-2 array('f') with bounds (n,n)\nc : input rank-2 array('f') with bounds (m,n)\n\nOther Parameters\n----------------\ntrana : input string(len=1), optional\n    Default: 'N'\ntranb : input string(len=1), optional\n    Default: 'N'\nisgn : input int, optional\n    Default: 1\noverwrite_c : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('f') with bounds (m,n) and c storage\nscale : float\ninfo : int\n"
    ...

def strtri(c, lower=..., unitdiag=..., overwrite_c=...) -> typing.Any:
    "inv_c,info = strtri(c,[lower,unitdiag,overwrite_c])\n\nWrapper for ``strtri``.\n\nParameters\n----------\nc : input rank-2 array('f') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_c : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\nunitdiag : input int, optional\n    Default: 0\n\nReturns\n-------\ninv_c : rank-2 array('f') with bounds (n,n) and c storage\ninfo : int\n"
    ...

def strtrs(a, b, lower=..., trans=..., unitdiag=..., lda=..., overwrite_b=...) -> typing.Any:
    "x,info = strtrs(a,b,[lower,trans,unitdiag,lda,overwrite_b])\n\nWrapper for ``strtrs``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (lda,n)\nb : input rank-2 array('f') with bounds (ldb,nrhs)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\nunitdiag : input int, optional\n    Default: 0\nlda : input int, optional\n    Default: shape(a,0)\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('f') with bounds (ldb,nrhs) and b storage\ninfo : int\n"
    ...

def strttf(a, transr=..., uplo=...) -> typing.Any:
    "arf,info = strttf(a,[transr,uplo])\n\nWrapper for ``strttf``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (lda,n)\n\nOther Parameters\n----------------\ntransr : input string(len=1), optional\n    Default: 'N'\nuplo : input string(len=1), optional\n    Default: 'U'\n\nReturns\n-------\narf : rank-1 array('f') with bounds (n*(n+1)/2)\ninfo : int\n"
    ...

def strttp(a, uplo=...) -> typing.Any:
    "ap,info = strttp(a,[uplo])\n\nWrapper for ``strttp``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (lda,n)\n\nOther Parameters\n----------------\nuplo : input string(len=1), optional\n    Default: 'U'\n\nReturns\n-------\nap : rank-1 array('f') with bounds (n*(n+1)/2)\ninfo : int\n"
    ...

def stzrzf(a, lwork=..., overwrite_a=...) -> typing.Any:
    "rz,tau,info = stzrzf(a,[lwork,overwrite_a])\n\nWrapper for ``stzrzf``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: MAX(m,1)\n\nReturns\n-------\nrz : rank-2 array('f') with bounds (m,n) and a storage\ntau : rank-1 array('f') with bounds (m)\ninfo : int\n"
    ...

def stzrzf_lwork(m, n) -> typing.Any:
    'work,info = stzrzf_lwork(m,n)\n\nWrapper for ``stzrzf_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\n\nReturns\n-------\nwork : float\ninfo : int\n'
    ...

def zgbsv(kl, ku, ab, b, overwrite_ab=..., overwrite_b=...) -> typing.Any:
    "lub,piv,x,info = zgbsv(kl,ku,ab,b,[overwrite_ab,overwrite_b])\n\nWrapper for ``zgbsv``.\n\nParameters\n----------\nkl : input int\nku : input int\nab : input rank-2 array('D') with bounds (2*kl+ku+1,n)\nb : input rank-2 array('D') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_ab : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nlub : rank-2 array('D') with bounds (2*kl+ku+1,n) and ab storage\npiv : rank-1 array('i') with bounds (n)\nx : rank-2 array('D') with bounds (n,nrhs) and b storage\ninfo : int\n"
    ...

def zgbtrf(ab, kl, ku, m=..., n=..., ldab=..., overwrite_ab=...) -> typing.Any:
    "lu,ipiv,info = zgbtrf(ab,kl,ku,[m,n,ldab,overwrite_ab])\n\nWrapper for ``zgbtrf``.\n\nParameters\n----------\nab : input rank-2 array('D') with bounds (ldab,n)\nkl : input int\nku : input int\n\nOther Parameters\n----------------\nm : input int, optional\n    Default: shape(ab,1)\nn : input int, optional\n    Default: shape(ab,1)\noverwrite_ab : input int, optional\n    Default: 0\nldab : input int, optional\n    Default: max(shape(ab,0),1)\n\nReturns\n-------\nlu : rank-2 array('D') with bounds (ldab,n) and ab storage\nipiv : rank-1 array('i') with bounds (MIN(m,n))\ninfo : int\n"
    ...

def zgbtrs(ab, kl, ku, b, ipiv, trans=..., n=..., ldab=..., ldb=..., overwrite_b=...) -> typing.Any:
    "x,info = zgbtrs(ab,kl,ku,b,ipiv,[trans,n,ldab,ldb,overwrite_b])\n\nWrapper for ``zgbtrs``.\n\nParameters\n----------\nab : input rank-2 array('D') with bounds (ldab,n)\nkl : input int\nku : input int\nb : input rank-2 array('D') with bounds (ldb,nrhs)\nipiv : input rank-1 array('i') with bounds (n)\n\nOther Parameters\n----------------\noverwrite_b : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\nn : input int, optional\n    Default: shape(ab,1)\nldab : input int, optional\n    Default: shape(ab,0)\nldb : input int, optional\n    Default: shape(b,0)\n\nReturns\n-------\nx : rank-2 array('D') with bounds (ldb,nrhs) and b storage\ninfo : int\n"
    ...

def zgebal(a, scale=..., permute=..., overwrite_a=...) -> typing.Any:
    "ba,lo,hi,pivscale,info = zgebal(a,[scale,permute,overwrite_a])\n\nWrapper for ``zgebal``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (m,n)\n\nOther Parameters\n----------------\nscale : input int, optional\n    Default: 0\npermute : input int, optional\n    Default: 0\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\nba : rank-2 array('D') with bounds (m,n) and a storage\nlo : int\nhi : int\npivscale : rank-1 array('d') with bounds (n)\ninfo : int\n"
    ...

def zgecon(a, anorm, norm=...) -> typing.Any:
    "rcond,info = zgecon(a,anorm,[norm])\n\nWrapper for ``zgecon``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (n,n)\nanorm : input float\n\nOther Parameters\n----------------\nnorm : input string(len=1), optional\n    Default: '1'\n\nReturns\n-------\nrcond : float\ninfo : int\n"
    ...

def zgeequ(a) -> typing.Any:
    "r,c,rowcnd,colcnd,amax,info = zgeequ(a)\n\nWrapper for ``zgeequ``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (m,n)\n\nReturns\n-------\nr : rank-1 array('d') with bounds (m)\nc : rank-1 array('d') with bounds (n)\nrowcnd : float\ncolcnd : float\namax : float\ninfo : int\n"
    ...

def zgeequb(a) -> typing.Any:
    "r,c,rowcnd,colcnd,amax,info = zgeequb(a)\n\nWrapper for ``zgeequb``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (m,n)\n\nReturns\n-------\nr : rank-1 array('d') with bounds (m)\nc : rank-1 array('d') with bounds (n)\nrowcnd : float\ncolcnd : float\namax : float\ninfo : int\n"
    ...

def zgees(zselect, a, compute_v=..., sort_t=..., lwork=..., zselect_extra_args=..., overwrite_a=...) -> typing.Any:
    "t,sdim,w,vs,work,info = zgees(zselect,a,[compute_v,sort_t,lwork,zselect_extra_args,overwrite_a])\n\nWrapper for ``zgees``.\n\nParameters\n----------\nzselect : call-back function\na : input rank-2 array('D') with bounds (n,n)\n\nOther Parameters\n----------------\ncompute_v : input int, optional\n    Default: 1\nsort_t : input int, optional\n    Default: 0\nzselect_extra_args : input tuple, optional\n    Default: ()\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(3*n,1)\n\nReturns\n-------\nt : rank-2 array('D') with bounds (n,n) and a storage\nsdim : int\nw : rank-1 array('D') with bounds (n)\nvs : rank-2 array('D') with bounds (ldvs,n)\nwork : rank-1 array('D') with bounds (MAX(lwork,1))\ninfo : int\n\nNotes\n-----\nCall-back functions::\n\n  def zselect(arg): return zselect\n  Required arguments:\n    arg : input complex\n  Return objects:\n    zselect : int\n"
    ...

def zgeev(a, compute_vl=..., compute_vr=..., lwork=..., overwrite_a=...) -> typing.Any:
    "w,vl,vr,info = zgeev(a,[compute_vl,compute_vr,lwork,overwrite_a])\n\nWrapper for ``zgeev``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (n,n)\n\nOther Parameters\n----------------\ncompute_vl : input int, optional\n    Default: 1\ncompute_vr : input int, optional\n    Default: 1\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(2*n,1)\n\nReturns\n-------\nw : rank-1 array('D') with bounds (n)\nvl : rank-2 array('D') with bounds (ldvl,n)\nvr : rank-2 array('D') with bounds (ldvr,n)\ninfo : int\n"
    ...

def zgeev_lwork(n, compute_vl=..., compute_vr=...) -> typing.Any:
    'work,info = zgeev_lwork(n,[compute_vl,compute_vr])\n\nWrapper for ``zgeev_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\ncompute_vl : input int, optional\n    Default: 1\ncompute_vr : input int, optional\n    Default: 1\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    ...

def zgegv(*args, **kwds) -> typing.Any:
    "`zgegv` is deprecated!\nThe `*gegv` family of routines has been deprecated in\nLAPACK 3.6.0 in favor of the `*ggev` family of routines.\nThe corresponding wrappers will be removed from SciPy in\na future release.\n\nalpha,beta,vl,vr,info = zgegv(a,b,[compute_vl,compute_vr,lwork,overwrite_a,overwrite_b])\n\nWrapper for ``zgegv``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (n,n)\nb : input rank-2 array('D') with bounds (n,n)\n\nOther Parameters\n----------------\ncompute_vl : input int, optional\n    Default: 1\ncompute_vr : input int, optional\n    Default: 1\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(2*n,1)\n\nReturns\n-------\nalpha : rank-1 array('D') with bounds (n)\nbeta : rank-1 array('D') with bounds (n)\nvl : rank-2 array('D') with bounds (ldvl,n)\nvr : rank-2 array('D') with bounds (ldvr,n)\ninfo : int\n"
    ...

def zgehrd(a, lo=..., hi=..., lwork=..., overwrite_a=...) -> typing.Any:
    "ht,tau,info = zgehrd(a,[lo,hi,lwork,overwrite_a])\n\nWrapper for ``zgehrd``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (n,n)\n\nOther Parameters\n----------------\nlo : input int, optional\n    Default: 0\nhi : input int, optional\n    Default: n-1\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: MAX(n,1)\n\nReturns\n-------\nht : rank-2 array('D') with bounds (n,n) and a storage\ntau : rank-1 array('D') with bounds (n - 1)\ninfo : int\n"
    ...

def zgehrd_lwork(n, lo=..., hi=...) -> typing.Any:
    'work,info = zgehrd_lwork(n,[lo,hi])\n\nWrapper for ``zgehrd_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlo : input int, optional\n    Default: 0\nhi : input int, optional\n    Default: n-1\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    ...

def zgels(a, b, trans=..., lwork=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "lqr,x,info = zgels(a,b,[trans,lwork,overwrite_a,overwrite_b])\n\nWrapper for ``zgels``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (m,n)\nb : input rank-2 array('D') with bounds (MAX(m,n),nrhs)\n\nOther Parameters\n----------------\ntrans : input string(len=1), optional\n    Default: 'N'\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: MAX(MIN(m,n)+MAX(MIN(m,n),nrhs),1)\n\nReturns\n-------\nlqr : rank-2 array('D') with bounds (m,n) and a storage\nx : rank-2 array('D') with bounds (MAX(m,n),nrhs) and b storage\ninfo : int\n"
    ...

def zgels_lwork(m, n, nrhs, trans=...) -> typing.Any:
    "work,info = zgels_lwork(m,n,nrhs,[trans])\n\nWrapper for ``zgels_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\nnrhs : input int\n\nOther Parameters\n----------------\ntrans : input string(len=1), optional\n    Default: 'N'\n\nReturns\n-------\nwork : complex\ninfo : int\n"
    ...

def zgelsd(a, b, lwork, size_rwork, size_iwork, cond=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "x,s,rank,info = zgelsd(a,b,lwork,size_rwork,size_iwork,[cond,overwrite_a,overwrite_b])\n\nWrapper for ``zgelsd``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (m,n)\nb : input rank-2 array('D') with bounds (maxmn,nrhs)\nlwork : input int\nsize_rwork : input int\nsize_iwork : input int\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\ncond : input float, optional\n    Default: -1.0\n\nReturns\n-------\nx : rank-2 array('D') with bounds (maxmn,nrhs) and b storage\ns : rank-1 array('d') with bounds (minmn)\nrank : int\ninfo : int\n"
    ...

def zgelsd_lwork(m, n, nrhs, cond=..., lwork=...) -> typing.Any:
    'work,rwork,iwork,info = zgelsd_lwork(m,n,nrhs,[cond,lwork])\n\nWrapper for ``zgelsd_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\nnrhs : input int\n\nOther Parameters\n----------------\ncond : input float, optional\n    Default: -1.0\nlwork : input int, optional\n    Default: -1\n\nReturns\n-------\nwork : complex\nrwork : float\niwork : int\ninfo : int\n'
    ...

def zgelss(a, b, cond=..., lwork=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "v,x,s,rank,work,info = zgelss(a,b,[cond,lwork,overwrite_a,overwrite_b])\n\nWrapper for ``zgelss``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (m,n)\nb : input rank-2 array('D') with bounds (maxmn,nrhs)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\ncond : input float, optional\n    Default: -1.0\nlwork : input int, optional\n    Default: max(2*minmn+MAX(maxmn,nrhs),1)\n\nReturns\n-------\nv : rank-2 array('D') with bounds (m,n) and a storage\nx : rank-2 array('D') with bounds (maxmn,nrhs) and b storage\ns : rank-1 array('d') with bounds (minmn)\nrank : int\nwork : rank-1 array('D') with bounds (MAX(lwork,1))\ninfo : int\n"
    ...

def zgelss_lwork(m, n, nrhs, cond=..., lwork=...) -> typing.Any:
    'work,info = zgelss_lwork(m,n,nrhs,[cond,lwork])\n\nWrapper for ``zgelss_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\nnrhs : input int\n\nOther Parameters\n----------------\ncond : input float, optional\n    Default: -1.0\nlwork : input int, optional\n    Default: -1\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    ...

def zgelsy(a, b, jptv, cond, lwork, overwrite_a=..., overwrite_b=...) -> typing.Any:
    "v,x,j,rank,info = zgelsy(a,b,jptv,cond,lwork,[overwrite_a,overwrite_b])\n\nWrapper for ``zgelsy``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (m,n)\nb : input rank-2 array('D') with bounds (maxmn,nrhs)\njptv : input rank-1 array('i') with bounds (n)\ncond : input float\nlwork : input int\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nv : rank-2 array('D') with bounds (m,n) and a storage\nx : rank-2 array('D') with bounds (maxmn,nrhs) and b storage\nj : rank-1 array('i') with bounds (n) and jptv storage\nrank : int\ninfo : int\n"
    ...

def zgelsy_lwork(m, n, nrhs, cond, lwork=...) -> typing.Any:
    'work,info = zgelsy_lwork(m,n,nrhs,cond,[lwork])\n\nWrapper for ``zgelsy_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\nnrhs : input int\ncond : input float\n\nOther Parameters\n----------------\nlwork : input int, optional\n    Default: -1\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    ...

def zgemqrt(v, t, c, side=..., trans=..., overwrite_c=...) -> typing.Any:
    "c,info = zgemqrt(v,t,c,[side,trans,overwrite_c])\n\nWrapper for ``zgemqrt``.\n\nParameters\n----------\nv : input rank-2 array('D') with bounds ((side[0]=='L'?m:n),k)\nt : input rank-2 array('D') with bounds (nb,k)\nc : input rank-2 array('D') with bounds (m,n)\n\nOther Parameters\n----------------\nside : input string(len=1), optional\n    Default: 'L'\ntrans : input string(len=1), optional\n    Default: 'N'\noverwrite_c : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('D') with bounds (m,n)\ninfo : int\n"
    ...

def zgeqp3(a, lwork=..., overwrite_a=...) -> typing.Any:
    "qr,jpvt,tau,work,info = zgeqp3(a,[lwork,overwrite_a])\n\nWrapper for ``zgeqp3``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(3*(n+1),1)\n\nReturns\n-------\nqr : rank-2 array('D') with bounds (m,n) and a storage\njpvt : rank-1 array('i') with bounds (n)\ntau : rank-1 array('D') with bounds (MIN(m,n))\nwork : rank-1 array('D') with bounds (MAX(lwork,1))\ninfo : int\n"
    ...

def zgeqrf(a, lwork=..., overwrite_a=...) -> typing.Any:
    "qr,tau,work,info = zgeqrf(a,[lwork,overwrite_a])\n\nWrapper for ``zgeqrf``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(3*n,1)\n\nReturns\n-------\nqr : rank-2 array('D') with bounds (m,n) and a storage\ntau : rank-1 array('D') with bounds (MIN(m,n))\nwork : rank-1 array('D') with bounds (MAX(lwork,1))\ninfo : int\n"
    ...

def zgeqrf_lwork(m, n) -> typing.Any:
    'work,info = zgeqrf_lwork(m,n)\n\nWrapper for ``zgeqrf_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    ...

def zgeqrfp(a, lwork=..., overwrite_a=...) -> typing.Any:
    "qr,tau,info = zgeqrfp(a,[lwork,overwrite_a])\n\nWrapper for ``zgeqrfp``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: MAX(1, n)\n\nReturns\n-------\nqr : rank-2 array('D') with bounds (m,n) and a storage\ntau : rank-1 array('D') with bounds (MIN(m,n))\ninfo : int\n"
    ...

def zgeqrfp_lwork(m, n) -> typing.Any:
    'work,info = zgeqrfp_lwork(m,n)\n\nWrapper for ``zgeqrfp_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    ...

def zgeqrt(nb, a, overwrite_a=...) -> typing.Any:
    "a,t,info = zgeqrt(nb,a,[overwrite_a])\n\nWrapper for ``zgeqrt``.\n\nParameters\n----------\nnb : input int\na : input rank-2 array('D') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\na : rank-2 array('D') with bounds (m,n)\nt : rank-2 array('D') with bounds (nb,MIN(m,n))\ninfo : int\n"
    ...

def zgerqf(a, lwork=..., overwrite_a=...) -> typing.Any:
    "qr,tau,work,info = zgerqf(a,[lwork,overwrite_a])\n\nWrapper for ``zgerqf``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(3*m,1)\n\nReturns\n-------\nqr : rank-2 array('D') with bounds (m,n) and a storage\ntau : rank-1 array('D') with bounds (MIN(m,n))\nwork : rank-1 array('D') with bounds (MAX(lwork,1))\ninfo : int\n"
    ...

def zgesc2(lu, rhs, ipiv, jpiv, overwrite_rhs=...) -> typing.Any:
    "x,scale = zgesc2(lu,rhs,ipiv,jpiv,[overwrite_rhs])\n\nWrapper for ``zgesc2``.\n\nParameters\n----------\nlu : input rank-2 array('D') with bounds (n,n)\nrhs : input rank-1 array('D') with bounds (n)\nipiv : input rank-1 array('i') with bounds (n)\njpiv : input rank-1 array('i') with bounds (n)\n\nOther Parameters\n----------------\noverwrite_rhs : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-1 array('D') with bounds (n) and rhs storage\nscale : float\n"
    ...

def zgesdd(a, compute_uv=..., full_matrices=..., lwork=..., overwrite_a=...) -> typing.Any:
    "u,s,vt,info = zgesdd(a,[compute_uv,full_matrices,lwork,overwrite_a])\n\nWrapper for ``zgesdd``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\ncompute_uv : input int, optional\n    Default: 1\nfull_matrices : input int, optional\n    Default: 1\nlwork : input int, optional\n    Default: max((compute_uv?2*minmn*minmn+MAX(m,n)+2*minmn:2*minmn+MAX(m,n)),1)\n\nReturns\n-------\nu : rank-2 array('D') with bounds (u0,u1)\ns : rank-1 array('d') with bounds (minmn)\nvt : rank-2 array('D') with bounds (vt0,vt1)\ninfo : int\n"
    ...

def zgesdd_lwork(m, n, compute_uv=..., full_matrices=...) -> typing.Any:
    'work,info = zgesdd_lwork(m,n,[compute_uv,full_matrices])\n\nWrapper for ``zgesdd_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\n\nOther Parameters\n----------------\ncompute_uv : input int, optional\n    Default: 1\nfull_matrices : input int, optional\n    Default: 1\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    ...

def zgesv(a, b, overwrite_a=..., overwrite_b=...) -> typing.Any:
    "lu,piv,x,info = zgesv(a,b,[overwrite_a,overwrite_b])\n\nWrapper for ``zgesv``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (n,n)\nb : input rank-2 array('D') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nlu : rank-2 array('D') with bounds (n,n) and a storage\npiv : rank-1 array('i') with bounds (n)\nx : rank-2 array('D') with bounds (n,nrhs) and b storage\ninfo : int\n"
    ...

def zgesvd(a, compute_uv=..., full_matrices=..., lwork=..., overwrite_a=...) -> typing.Any:
    "u,s,vt,info = zgesvd(a,[compute_uv,full_matrices,lwork,overwrite_a])\n\nWrapper for ``zgesvd``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\ncompute_uv : input int, optional\n    Default: 1\nfull_matrices : input int, optional\n    Default: 1\nlwork : input int, optional\n    Default: MAX(2*minmn+MAX(m,n),1)\n\nReturns\n-------\nu : rank-2 array('D') with bounds (u0,u1)\ns : rank-1 array('d') with bounds (minmn)\nvt : rank-2 array('D') with bounds (vt0,vt1)\ninfo : int\n"
    ...

def zgesvd_lwork(m, n, compute_uv=..., full_matrices=...) -> typing.Any:
    'work,info = zgesvd_lwork(m,n,[compute_uv,full_matrices])\n\nWrapper for ``zgesvd_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\n\nOther Parameters\n----------------\ncompute_uv : input int, optional\n    Default: 1\nfull_matrices : input int, optional\n    Default: 1\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    ...

def zgesvx(a, b, fact=..., trans=..., af=..., ipiv=..., equed=..., r=..., c=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "as,lu,ipiv,equed,rs,cs,bs,x,rcond,ferr,berr,info = zgesvx(a,b,[fact,trans,af,ipiv,equed,r,c,overwrite_a,overwrite_b])\n\nWrapper for ``zgesvx``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (n,n)\nb : input rank-2 array('D') with bounds (n,nrhs)\n\nOther Parameters\n----------------\nfact : input string(len=1), optional\n    Default: 'E'\ntrans : input string(len=1), optional\n    Default: 'N'\noverwrite_a : input int, optional\n    Default: 0\naf : input rank-2 array('D') with bounds (n,n)\nipiv : input rank-1 array('i') with bounds (n)\nequed : input string(len=1), optional\n    Default: 'B'\nr : input rank-1 array('d') with bounds (n)\nc : input rank-1 array('d') with bounds (n)\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nas : rank-2 array('D') with bounds (n,n) and a storage\nlu : rank-2 array('D') with bounds (n,n) and af storage\nipiv : rank-1 array('i') with bounds (n)\nequed : string(len=1)\nrs : rank-1 array('d') with bounds (n) and r storage\ncs : rank-1 array('d') with bounds (n) and c storage\nbs : rank-2 array('D') with bounds (n,nrhs) and b storage\nx : rank-2 array('D') with bounds (n,nrhs)\nrcond : float\nferr : rank-1 array('d') with bounds (nrhs)\nberr : rank-1 array('d') with bounds (nrhs)\ninfo : int\n"
    ...

def zgetc2(a, overwrite_a=...) -> typing.Any:
    "lu,ipiv,jpiv,info = zgetc2(a,[overwrite_a])\n\nWrapper for ``zgetc2``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\nlu : rank-2 array('D') with bounds (n,n) and a storage\nipiv : rank-1 array('i') with bounds (n)\njpiv : rank-1 array('i') with bounds (n)\ninfo : int\n"
    ...

def zgetrf(a, overwrite_a=...) -> typing.Any:
    "lu,piv,info = zgetrf(a,[overwrite_a])\n\nWrapper for ``zgetrf``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\nlu : rank-2 array('D') with bounds (m,n) and a storage\npiv : rank-1 array('i') with bounds (MIN(m,n))\ninfo : int\n"
    ...

def zgetri(lu, piv, lwork=..., overwrite_lu=...) -> typing.Any:
    "inv_a,info = zgetri(lu,piv,[lwork,overwrite_lu])\n\nWrapper for ``zgetri``.\n\nParameters\n----------\nlu : input rank-2 array('D') with bounds (n,n)\npiv : input rank-1 array('i') with bounds (n)\n\nOther Parameters\n----------------\noverwrite_lu : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(3*n,1)\n\nReturns\n-------\ninv_a : rank-2 array('D') with bounds (n,n) and lu storage\ninfo : int\n"
    ...

def zgetri_lwork(n) -> typing.Any:
    'work,info = zgetri_lwork(n)\n\nWrapper for ``zgetri_lwork``.\n\nParameters\n----------\nn : input int\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    ...

def zgetrs(lu, piv, b, trans=..., overwrite_b=...) -> typing.Any:
    "x,info = zgetrs(lu,piv,b,[trans,overwrite_b])\n\nWrapper for ``zgetrs``.\n\nParameters\n----------\nlu : input rank-2 array('D') with bounds (n,n)\npiv : input rank-1 array('i') with bounds (n)\nb : input rank-2 array('D') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_b : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('D') with bounds (n,nrhs) and b storage\ninfo : int\n"
    ...

def zgges(zselect, a, b, jobvsl=..., jobvsr=..., sort_t=..., ldvsl=..., ldvsr=..., lwork=..., zselect_extra_args=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "a,b,sdim,alpha,beta,vsl,vsr,work,info = zgges(zselect,a,b,[jobvsl,jobvsr,sort_t,ldvsl,ldvsr,lwork,zselect_extra_args,overwrite_a,overwrite_b])\n\nWrapper for ``zgges``.\n\nParameters\n----------\nzselect : call-back function\na : input rank-2 array('D') with bounds (lda,n)\nb : input rank-2 array('D') with bounds (ldb,n)\n\nOther Parameters\n----------------\njobvsl : input int, optional\n    Default: 1\njobvsr : input int, optional\n    Default: 1\nsort_t : input int, optional\n    Default: 0\nzselect_extra_args : input tuple, optional\n    Default: ()\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nldvsl : input int, optional\n    Default: ((jobvsl==1)?n:1)\nldvsr : input int, optional\n    Default: ((jobvsr==1)?n:1)\nlwork : input int, optional\n    Default: max(2*n,1)\n\nReturns\n-------\na : rank-2 array('D') with bounds (lda,n)\nb : rank-2 array('D') with bounds (ldb,n)\nsdim : int\nalpha : rank-1 array('D') with bounds (n)\nbeta : rank-1 array('D') with bounds (n)\nvsl : rank-2 array('D') with bounds (ldvsl,n)\nvsr : rank-2 array('D') with bounds (ldvsr,n)\nwork : rank-1 array('D') with bounds (MAX(lwork,1))\ninfo : int\n\nNotes\n-----\nCall-back functions::\n\n  def zselect(alpha,beta): return zselect\n  Required arguments:\n    alpha : input complex\n    beta : input complex\n  Return objects:\n    zselect : int\n"
    ...

def zggev(a, b, compute_vl=..., compute_vr=..., lwork=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "alpha,beta,vl,vr,work,info = zggev(a,b,[compute_vl,compute_vr,lwork,overwrite_a,overwrite_b])\n\nWrapper for ``zggev``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (n,n)\nb : input rank-2 array('D') with bounds (n,n)\n\nOther Parameters\n----------------\ncompute_vl : input int, optional\n    Default: 1\ncompute_vr : input int, optional\n    Default: 1\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(2*n,1)\n\nReturns\n-------\nalpha : rank-1 array('D') with bounds (n)\nbeta : rank-1 array('D') with bounds (n)\nvl : rank-2 array('D') with bounds (ldvl,n)\nvr : rank-2 array('D') with bounds (ldvr,n)\nwork : rank-1 array('D') with bounds (MAX(lwork,1))\ninfo : int\n"
    ...

def zgglse(a, b, c, d, lwork=..., overwrite_a=..., overwrite_b=..., overwrite_c=..., overwrite_d=...) -> typing.Any:
    "t,r,res,x,info = zgglse(a,b,c,d,[lwork,overwrite_a,overwrite_b,overwrite_c,overwrite_d])\n\nWrapper for ``zgglse``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (m,n)\nb : input rank-2 array('D') with bounds (p,n)\nc : input rank-1 array('D') with bounds (m)\nd : input rank-1 array('D') with bounds (p)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\noverwrite_c : input int, optional\n    Default: 0\noverwrite_d : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(m+n+p,1)\n\nReturns\n-------\nt : rank-2 array('D') with bounds (m,n) and a storage\nr : rank-2 array('D') with bounds (p,n) and b storage\nres : rank-1 array('D') with bounds (m) and c storage\nx : rank-1 array('D') with bounds (n)\ninfo : int\n"
    ...

def zgglse_lwork(m, n, p) -> typing.Any:
    'work,info = zgglse_lwork(m,n,p)\n\nWrapper for ``zgglse_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\np : input int\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    ...

def zgtsv(dl, d, du, b, overwrite_dl=..., overwrite_d=..., overwrite_du=..., overwrite_b=...) -> typing.Any:
    "du2,d,du,x,info = zgtsv(dl,d,du,b,[overwrite_dl,overwrite_d,overwrite_du,overwrite_b])\n\nWrapper for ``zgtsv``.\n\nParameters\n----------\ndl : input rank-1 array('D') with bounds (n - 1)\nd : input rank-1 array('D') with bounds (n)\ndu : input rank-1 array('D') with bounds (n - 1)\nb : input rank-2 array('D') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_dl : input int, optional\n    Default: 0\noverwrite_d : input int, optional\n    Default: 0\noverwrite_du : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\ndu2 : rank-1 array('D') with bounds (n - 1) and dl storage\nd : rank-1 array('D') with bounds (n)\ndu : rank-1 array('D') with bounds (n - 1)\nx : rank-2 array('D') with bounds (n,nrhs) and b storage\ninfo : int\n"
    ...

def zgtsvx(dl, d, du, b, fact=..., trans=..., dlf=..., df=..., duf=..., du2=..., ipiv=...) -> typing.Any:
    "dlf,df,duf,du2,ipiv,x,rcond,ferr,berr,info = zgtsvx(dl,d,du,b,[fact,trans,dlf,df,duf,du2,ipiv])\n\nWrapper for ``zgtsvx``.\n\nParameters\n----------\ndl : input rank-1 array('D') with bounds (MAX(0, n-1))\nd : input rank-1 array('D') with bounds (n)\ndu : input rank-1 array('D') with bounds (MAX(0, n-1))\nb : input rank-2 array('D') with bounds (ldb,nrhs)\n\nOther Parameters\n----------------\nfact : input string(len=1), optional\n    Default: 'N'\ntrans : input string(len=1), optional\n    Default: 'N'\ndlf : input rank-1 array('D') with bounds (MAX(0,n-1))\ndf : input rank-1 array('D') with bounds (n)\nduf : input rank-1 array('D') with bounds (MAX(0,n-1))\ndu2 : input rank-1 array('D') with bounds (MAX(0,n-2))\nipiv : input rank-1 array('i') with bounds (n)\n\nReturns\n-------\ndlf : rank-1 array('D') with bounds (MAX(0,n-1))\ndf : rank-1 array('D') with bounds (n)\nduf : rank-1 array('D') with bounds (MAX(0,n-1))\ndu2 : rank-1 array('D') with bounds (MAX(0,n-2))\nipiv : rank-1 array('i') with bounds (n)\nx : rank-2 array('D') with bounds (ldx,nrhs)\nrcond : float\nferr : rank-1 array('d') with bounds (nrhs)\nberr : rank-1 array('d') with bounds (nrhs)\ninfo : int\n"
    ...

def zgttrf(dl, d, du, overwrite_dl=..., overwrite_d=..., overwrite_du=...) -> typing.Any:
    "dl,d,du,du2,ipiv,info = zgttrf(dl,d,du,[overwrite_dl,overwrite_d,overwrite_du])\n\nWrapper for ``zgttrf``.\n\nParameters\n----------\ndl : input rank-1 array('D') with bounds (n - 1)\nd : input rank-1 array('D') with bounds (n)\ndu : input rank-1 array('D') with bounds (n - 1)\n\nOther Parameters\n----------------\noverwrite_dl : input int, optional\n    Default: 0\noverwrite_d : input int, optional\n    Default: 0\noverwrite_du : input int, optional\n    Default: 0\n\nReturns\n-------\ndl : rank-1 array('D') with bounds (n - 1)\nd : rank-1 array('D') with bounds (n)\ndu : rank-1 array('D') with bounds (n - 1)\ndu2 : rank-1 array('D') with bounds (n - 2)\nipiv : rank-1 array('i') with bounds (n)\ninfo : int\n"
    ...

def zgttrs(dl, d, du, du2, ipiv, b, trans=..., overwrite_b=...) -> typing.Any:
    "x,info = zgttrs(dl,d,du,du2,ipiv,b,[trans,overwrite_b])\n\nWrapper for ``zgttrs``.\n\nParameters\n----------\ndl : input rank-1 array('D') with bounds (n - 1)\nd : input rank-1 array('D') with bounds (n)\ndu : input rank-1 array('D') with bounds (n - 1)\ndu2 : input rank-1 array('D') with bounds (n - 2)\nipiv : input rank-1 array('i') with bounds (n)\nb : input rank-2 array('D') with bounds (ldb,nrhs)\n\nOther Parameters\n----------------\ntrans : input string(len=1), optional\n    Default: 'N'\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('D') with bounds (ldb,nrhs) and b storage\ninfo : int\n"
    ...

def zhbevd(ab, compute_v=..., lower=..., ldab=..., lrwork=..., liwork=..., overwrite_ab=...) -> typing.Any:
    "w,z,info = zhbevd(ab,[compute_v,lower,ldab,lrwork,liwork,overwrite_ab])\n\nWrapper for ``zhbevd``.\n\nParameters\n----------\nab : input rank-2 array('D') with bounds (ldab,n)\n\nOther Parameters\n----------------\noverwrite_ab : input int, optional\n    Default: 1\ncompute_v : input int, optional\n    Default: 1\nlower : input int, optional\n    Default: 0\nldab : input int, optional\n    Default: shape(ab,0)\nlrwork : input int, optional\n    Default: (compute_v?1+5*n+2*n*n:n)\nliwork : input int, optional\n    Default: (compute_v?3+5*n:1)\n\nReturns\n-------\nw : rank-1 array('d') with bounds (n)\nz : rank-2 array('D') with bounds (ldz,ldz)\ninfo : int\n"
    ...

def zhbevx(ab, vl, vu, il, iu, ldab=..., compute_v=..., range=..., lower=..., abstol=..., mmax=..., overwrite_ab=...) -> typing.Any:
    "w,z,m,ifail,info = zhbevx(ab,vl,vu,il,iu,[ldab,compute_v,range,lower,abstol,mmax,overwrite_ab])\n\nWrapper for ``zhbevx``.\n\nParameters\n----------\nab : input rank-2 array('D') with bounds (ldab,n)\nvl : input float\nvu : input float\nil : input int\niu : input int\n\nOther Parameters\n----------------\noverwrite_ab : input int, optional\n    Default: 1\nldab : input int, optional\n    Default: shape(ab,0)\ncompute_v : input int, optional\n    Default: 1\nrange : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\nabstol : input float, optional\n    Default: 0.0\nmmax : input int, optional\n    Default: (compute_v?(range==2?(iu-il+1):n):1)\n\nReturns\n-------\nw : rank-1 array('d') with bounds (n)\nz : rank-2 array('D') with bounds (ldz,mmax)\nm : int\nifail : rank-1 array('i') with bounds ((compute_v?n:1))\ninfo : int\n"
    ...

def zhecon(a, ipiv, anorm, lower=...) -> typing.Any:
    "rcond,info = zhecon(a,ipiv,anorm,[lower])\n\nWrapper for ``zhecon``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (n,n)\nipiv : input rank-1 array('i') with bounds (n)\nanorm : input float\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nrcond : float\ninfo : int\n"
    ...

def zheequb(a, lower=...) -> typing.Any:
    "s,scond,amax,info = zheequb(a,[lower])\n\nWrapper for ``zheequb``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (lda,n)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\ns : rank-1 array('d') with bounds (n)\nscond : float\namax : float\ninfo : int\n"
    ...

def zheev(a, compute_v=..., lower=..., lwork=..., overwrite_a=...) -> typing.Any:
    "w,v,info = zheev(a,[compute_v,lower,lwork,overwrite_a])\n\nWrapper for ``zheev``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (n,n)\n\nOther Parameters\n----------------\ncompute_v : input int, optional\n    Default: 1\nlower : input int, optional\n    Default: 0\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(2*n-1,1)\n\nReturns\n-------\nw : rank-1 array('d') with bounds (n)\nv : rank-2 array('D') with bounds (n,n) and a storage\ninfo : int\n"
    ...

def zheev_lwork(n, lower=...) -> typing.Any:
    'work,info = zheev_lwork(n,[lower])\n\nWrapper for ``zheev_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    ...

def zheevd(a, compute_v=..., lower=..., lwork=..., liwork=..., lrwork=..., overwrite_a=...) -> typing.Any:
    "w,v,info = zheevd(a,[compute_v,lower,lwork,liwork,lrwork,overwrite_a])\n\nWrapper for ``zheevd``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (n,n)\n\nOther Parameters\n----------------\ncompute_v : input int, optional\n    Default: 1\nlower : input int, optional\n    Default: 0\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max((compute_v?2*n+n*n:n+1),1)\nliwork : input int, optional\n    Default: (compute_v?3+5*n:1)\nlrwork : input int, optional\n    Default: (compute_v?1+5*n+2*n*n:n)\n\nReturns\n-------\nw : rank-1 array('d') with bounds (n)\nv : rank-2 array('D') with bounds (n,n) and a storage\ninfo : int\n"
    ...

def zheevd_lwork(n, compute_v=..., lower=...) -> typing.Any:
    'work,iwork,rwork,info = zheevd_lwork(n,[compute_v,lower])\n\nWrapper for ``zheevd_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\ncompute_v : input int, optional\n    Default: 1\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nwork : complex\niwork : int\nrwork : float\ninfo : int\n'
    ...

def zheevr(a, compute_v=..., range=..., lower=..., vl=..., vu=..., il=..., iu=..., abstol=..., lwork=..., lrwork=..., liwork=..., overwrite_a=...) -> typing.Any:
    "w,z,m,isuppz,info = zheevr(a,[compute_v,range,lower,vl,vu,il,iu,abstol,lwork,lrwork,liwork,overwrite_a])\n\nWrapper for ``zheevr``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds ``(n,n)``\n\nOther Parameters\n----------------\ncompute_v : input int, optional\n    Default ``1``\nrange : input string(len=1), optional\n    Default ``'A'``\nlower : input int, optional\n    Default ``0``\noverwrite_a : input int, optional\n    Default ``0``\nvl : input float, optional\n    Default ``0.0``\nvu : input float, optional\n    Default ``1.0``\nil : input int, optional\n    Default ``1``\niu : input int, optional\n    Default ``n``\nabstol : input float, optional\n    Default ``0.0``\nlwork : input int, optional\n    Default ``max(2*n,1)``\nlrwork : input int, optional\n    Default ``max(24*n,1)``\nliwork : input int, optional\n    Default ``max(1,10*n)``\n\nReturns\n-------\nw : rank-1 array('d') with bounds ``(n)``\nz : rank-2 array('D') with bounds ``((compute_v?MAX(0,n):0),(compute_v?(*range=='I'?iu-il+1:MAX(1,n)):0))``\nm : int\nisuppz : rank-1 array('i') with bounds ``(2*max(1,n))``\ninfo : int\n"
    ...

def zheevr_lwork(n, lower=...) -> typing.Any:
    'work,rwork,iwork,info = zheevr_lwork(n,[lower])\n\nWrapper for ``zheevr_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nwork : complex\nrwork : float\niwork : int\ninfo : int\n'
    ...

def zheevx(a, compute_v=..., range=..., lower=..., vl=..., vu=..., il=..., iu=..., abstol=..., lwork=..., overwrite_a=...) -> typing.Any:
    "w,z,m,ifail,info = zheevx(a,[compute_v,range,lower,vl,vu,il,iu,abstol,lwork,overwrite_a])\n\nWrapper for ``zheevx``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds ``(n,n)``\n\nOther Parameters\n----------------\ncompute_v : input int, optional\n    Default ``1``\nrange : input string(len=1), optional\n    Default ``'A'``\nlower : input int, optional\n    Default ``0``\noverwrite_a : input int, optional\n    Default ``0``\nvl : input float, optional\n    Default ``0.0``\nvu : input float, optional\n    Default ``1.0``\nil : input int, optional\n    Default ``1``\niu : input int, optional\n    Default ``n``\nabstol : input float, optional\n    Default ``0.0``\nlwork : input int, optional\n    Default ``max(2*n,1)``\n\nReturns\n-------\nw : rank-1 array('d') with bounds ``(n)``\nz : rank-2 array('D') with bounds ``((compute_v*n),(compute_v?(*range=='I'?iu-il+1:MAX(1,n)):0))``\nm : int\nifail : rank-1 array('i') with bounds ``(compute_v*n)``\ninfo : int\n"
    ...

def zheevx_lwork(n, lower=...) -> typing.Any:
    'work,info = zheevx_lwork(n,[lower])\n\nWrapper for ``zheevx_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    ...

def zhegst(a, b, itype=..., lower=..., overwrite_a=...) -> typing.Any:
    "c,info = zhegst(a,b,[itype,lower,overwrite_a])\n\nWrapper for ``zhegst``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (n,n)\nb : input rank-2 array('D') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nitype : input int, optional\n    Default: 1\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('D') with bounds (n,n) and a storage\ninfo : int\n"
    ...

def zhegv(a, b, itype=..., jobz=..., uplo=..., lwork=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "w,v,info = zhegv(a,b,[itype,jobz,uplo,lwork,overwrite_a,overwrite_b])\n\nWrapper for ``zhegv``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (n,n)\nb : input rank-2 array('D') with bounds (n,n)\n\nOther Parameters\n----------------\nitype : input int, optional\n    Default: 1\njobz : input string(len=1), optional\n    Default: 'V'\nuplo : input string(len=1), optional\n    Default: 'L'\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(2*n-1,1)\n\nReturns\n-------\nw : rank-1 array('d') with bounds (n)\nv : rank-2 array('D') with bounds (n,n) and a storage\ninfo : int\n"
    ...

def zhegv_lwork(n, uplo=...) -> typing.Any:
    "work,info = zhegv_lwork(n,[uplo])\n\nWrapper for ``zhegv_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nuplo : input string(len=1), optional\n    Default: 'L'\n\nReturns\n-------\nwork : complex\ninfo : int\n"
    ...

def zhegvd(a, b, itype=..., jobz=..., uplo=..., lwork=..., lrwork=..., liwork=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "w,v,info = zhegvd(a,b,[itype,jobz,uplo,lwork,lrwork,liwork,overwrite_a,overwrite_b])\n\nWrapper for ``zhegvd``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds ``(n,n)``\nb : input rank-2 array('D') with bounds ``(n,n)``\n\nOther Parameters\n----------------\nitype : input int, optional\n    Default ``1``\njobz : input string(len=1), optional\n    Default ``'V'``\nuplo : input string(len=1), optional\n    Default ``'L'``\noverwrite_a : input int, optional\n    Default ``0``\noverwrite_b : input int, optional\n    Default ``0``\nlwork : input int, optional\n    Default ``(*jobz=='N'?n+1:n*(n+2))``\nlrwork : input int, optional\n    Default ``max((*jobz=='N'?n:2*n*n+5*n+1),1)``\nliwork : input int, optional\n    Default ``(*jobz=='N'?1:5*n+3)``\n\nReturns\n-------\nw : rank-1 array('d') with bounds ``(n)``\nv : rank-2 array('D') with bounds ``(n,n)`` with ``a`` storage\ninfo : int\n"
    ...

def zhegvx(a, b, itype=..., jobz=..., range=..., uplo=..., vl=..., vu=..., il=..., iu=..., abstol=..., lwork=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "w,z,m,ifail,info = zhegvx(a,b,[itype,jobz,range,uplo,vl,vu,il,iu,abstol,lwork,overwrite_a,overwrite_b])\n\nWrapper for ``zhegvx``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (n,n)\nb : input rank-2 array('D') with bounds (n,n)\n\nOther Parameters\n----------------\nitype : input int, optional\n    Default: 1\njobz : input string(len=1), optional\n    Default: 'V'\nrange : input string(len=1), optional\n    Default: 'A'\nuplo : input string(len=1), optional\n    Default: 'L'\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nvl : input float, optional\n    Default: 0.0\nvu : input float, optional\n    Default: 1.0\nil : input int, optional\n    Default: 1\niu : input int, optional\n    Default: n\nabstol : input float, optional\n    Default: 0.0\nlwork : input int, optional\n    Default: max(2*n,1)\n\nReturns\n-------\nw : rank-1 array('d') with bounds (n)\nz : rank-2 array('D') with bounds ((jobz[0]=='V'?MAX(0,n):0),(jobz[0]=='V'?(range[0]=='I'?iu-il+1:MAX(1,n)):0))\nm : int\nifail : rank-1 array('i') with bounds ((jobz[0]=='N'?0:n))\ninfo : int\n"
    ...

def zhegvx_lwork(n, uplo=...) -> typing.Any:
    "work,info = zhegvx_lwork(n,[uplo])\n\nWrapper for ``zhegvx_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nuplo : input string(len=1), optional\n    Default: 'L'\n\nReturns\n-------\nwork : complex\ninfo : int\n"
    ...

def zhesv(a, b, lwork=..., lower=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "uduh,ipiv,x,info = zhesv(a,b,[lwork,lower,overwrite_a,overwrite_b])\n\nWrapper for ``zhesv``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (n,n)\nb : input rank-2 array('D') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(n,1)\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nuduh : rank-2 array('D') with bounds (n,n) and a storage\nipiv : rank-1 array('i') with bounds (n)\nx : rank-2 array('D') with bounds (n,nrhs) and b storage\ninfo : int\n"
    ...

def zhesv_lwork(n, lower=...) -> typing.Any:
    'work,info = zhesv_lwork(n,[lower])\n\nWrapper for ``zhesv_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    ...

def zhesvx(a, b, af=..., ipiv=..., lwork=..., factored=..., lower=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "uduh,ipiv,x,rcond,ferr,berr,info = zhesvx(a,b,[af,ipiv,lwork,factored,lower,overwrite_a,overwrite_b])\n\nWrapper for ``zhesvx``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (n,n)\nb : input rank-2 array('D') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\naf : input rank-2 array('D') with bounds (n,n)\nipiv : input rank-1 array('i') with bounds (n)\noverwrite_b : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(2*n,1)\nfactored : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nuduh : rank-2 array('D') with bounds (n,n) and af storage\nipiv : rank-1 array('i') with bounds (n)\nx : rank-2 array('D') with bounds (n,nrhs)\nrcond : float\nferr : rank-1 array('d') with bounds (nrhs)\nberr : rank-1 array('d') with bounds (nrhs)\ninfo : int\n"
    ...

def zhesvx_lwork(n, lower=...) -> typing.Any:
    'work,info = zhesvx_lwork(n,[lower])\n\nWrapper for ``zhesvx_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    ...

def zhetrd(a, lower=..., lwork=..., overwrite_a=...) -> typing.Any:
    "c,d,e,tau,info = zhetrd(a,[lower,lwork,overwrite_a])\n\nWrapper for ``zhetrd``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (lda,n)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: MAX(n,1)\n\nReturns\n-------\nc : rank-2 array('D') with bounds (lda,n) and a storage\nd : rank-1 array('d') with bounds (n)\ne : rank-1 array('d') with bounds (n - 1)\ntau : rank-1 array('D') with bounds (n - 1)\ninfo : int\n"
    ...

def zhetrd_lwork(n, lower=...) -> typing.Any:
    'work,info = zhetrd_lwork(n,[lower])\n\nWrapper for ``zhetrd_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    ...

def zhetrf(a, lower=..., lwork=..., overwrite_a=...) -> typing.Any:
    "ldu,ipiv,info = zhetrf(a,[lower,lwork,overwrite_a])\n\nWrapper for ``zhetrf``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (n,n)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(n,1)\n\nReturns\n-------\nldu : rank-2 array('D') with bounds (n,n) and a storage\nipiv : rank-1 array('i') with bounds (n)\ninfo : int\n"
    ...

def zhetrf_lwork(n, lower=...) -> typing.Any:
    'work,info = zhetrf_lwork(n,[lower])\n\nWrapper for ``zhetrf_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    ...

def zhfrk(n, k, alpha, a, beta, c, transr=..., uplo=..., trans=..., overwrite_c=...) -> typing.Any:
    "cout = zhfrk(n,k,alpha,a,beta,c,[transr,uplo,trans,overwrite_c])\n\nWrapper for ``zhfrk``.\n\nParameters\n----------\nn : input int\nk : input int\nalpha : input float\na : input rank-2 array('D') with bounds (lda,ka)\nbeta : input float\nc : input rank-1 array('D') with bounds (nt)\n\nOther Parameters\n----------------\ntransr : input string(len=1), optional\n    Default: 'N'\nuplo : input string(len=1), optional\n    Default: 'U'\ntrans : input string(len=1), optional\n    Default: 'N'\noverwrite_c : input int, optional\n    Default: 0\n\nReturns\n-------\ncout : rank-1 array('D') with bounds (nt) and c storage\n"
    ...

def zlange(norm, a) -> typing.Any:
    "n2 = zlange(norm,a)\n\nWrapper for ``zlange``.\n\nParameters\n----------\nnorm : input string(len=1)\na : input rank-2 array('D') with bounds (m,n)\n\nReturns\n-------\nn2 : float\n"
    ...

def zlarf(v, tau, c, work, side=..., incv=..., overwrite_c=...) -> typing.Any:
    "c = zlarf(v,tau,c,work,[side,incv,overwrite_c])\n\nWrapper for ``zlarf``.\n\nParameters\n----------\nv : input rank-1 array('D') with bounds ((side[0]=='L'?(1 + (m-1)*abs(incv)):(1 + (n-1)*abs(incv))))\ntau : input complex\nc : input rank-2 array('D') with bounds (m,n)\nwork : input rank-1 array('D') with bounds (lwork)\n\nOther Parameters\n----------------\nside : input string(len=1), optional\n    Default: 'L'\nincv : input int, optional\n    Default: 1\noverwrite_c : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('D') with bounds (m,n)\n"
    ...

def zlarfg(n, alpha, x, incx=..., overwrite_x=...) -> typing.Any:
    "alpha,x,tau = zlarfg(n,alpha,x,[incx,overwrite_x])\n\nWrapper for ``zlarfg``.\n\nParameters\n----------\nn : input int\nalpha : input complex\nx : input rank-1 array('D') with bounds (lx)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\n\nReturns\n-------\nalpha : complex\nx : rank-1 array('D') with bounds (lx)\ntau : complex\n"
    ...

def zlartg(f, g) -> typing.Any:
    'cs,sn,r = zlartg(f,g)\n\nWrapper for ``zlartg``.\n\nParameters\n----------\nf : input complex\ng : input complex\n\nReturns\n-------\ncs : float\nsn : complex\nr : complex\n'
    ...

def zlaswp(a, piv, k1=..., k2=..., off=..., inc=..., overwrite_a=...) -> typing.Any:
    "a = zlaswp(a,piv,[k1,k2,off,inc,overwrite_a])\n\nWrapper for ``zlaswp``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (nrows,n)\npiv : input rank-1 array('i') with bounds (npiv)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nk1 : input int, optional\n    Default: 0\nk2 : input int, optional\n    Default: npiv-1\noff : input int, optional\n    Default: 0\ninc : input int, optional\n    Default: 1\n\nReturns\n-------\na : rank-2 array('D') with bounds (nrows,n)\n"
    ...

def zlauum(c, lower=..., overwrite_c=...) -> typing.Any:
    "a,info = zlauum(c,[lower,overwrite_c])\n\nWrapper for ``zlauum``.\n\nParameters\n----------\nc : input rank-2 array('D') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_c : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\na : rank-2 array('D') with bounds (n,n) and c storage\ninfo : int\n"
    ...

def zpbsv(ab, b, lower=..., ldab=..., overwrite_ab=..., overwrite_b=...) -> typing.Any:
    "c,x,info = zpbsv(ab,b,[lower,ldab,overwrite_ab,overwrite_b])\n\nWrapper for ``zpbsv``.\n\nParameters\n----------\nab : input rank-2 array('D') with bounds (ldab,n)\nb : input rank-2 array('D') with bounds (ldb,nrhs)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\noverwrite_ab : input int, optional\n    Default: 0\nldab : input int, optional\n    Default: shape(ab,0)\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('D') with bounds (ldab,n) and ab storage\nx : rank-2 array('D') with bounds (ldb,nrhs) and b storage\ninfo : int\n"
    ...

def zpbtrf(ab, lower=..., ldab=..., overwrite_ab=...) -> typing.Any:
    "c,info = zpbtrf(ab,[lower,ldab,overwrite_ab])\n\nWrapper for ``zpbtrf``.\n\nParameters\n----------\nab : input rank-2 array('D') with bounds (ldab,n)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\noverwrite_ab : input int, optional\n    Default: 0\nldab : input int, optional\n    Default: shape(ab,0)\n\nReturns\n-------\nc : rank-2 array('D') with bounds (ldab,n) and ab storage\ninfo : int\n"
    ...

def zpbtrs(ab, b, lower=..., ldab=..., overwrite_b=...) -> typing.Any:
    "x,info = zpbtrs(ab,b,[lower,ldab,overwrite_b])\n\nWrapper for ``zpbtrs``.\n\nParameters\n----------\nab : input rank-2 array('D') with bounds (ldab,n)\nb : input rank-2 array('D') with bounds (ldb,nrhs)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\nldab : input int, optional\n    Default: shape(ab,0)\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('D') with bounds (ldb,nrhs) and b storage\ninfo : int\n"
    ...

def zpftrf(n, a, transr=..., uplo=..., overwrite_a=...) -> typing.Any:
    "achol,info = zpftrf(n,a,[transr,uplo,overwrite_a])\n\nWrapper for ``zpftrf``.\n\nParameters\n----------\nn : input int\na : input rank-1 array('D') with bounds (nt)\n\nOther Parameters\n----------------\ntransr : input string(len=1), optional\n    Default: 'N'\nuplo : input string(len=1), optional\n    Default: 'U'\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\nachol : rank-1 array('D') with bounds (nt) and a storage\ninfo : int\n"
    ...

def zpftri(n, a, transr=..., uplo=..., overwrite_a=...) -> typing.Any:
    "ainv,info = zpftri(n,a,[transr,uplo,overwrite_a])\n\nWrapper for ``zpftri``.\n\nParameters\n----------\nn : input int\na : input rank-1 array('D') with bounds (nt)\n\nOther Parameters\n----------------\ntransr : input string(len=1), optional\n    Default: 'N'\nuplo : input string(len=1), optional\n    Default: 'U'\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\nainv : rank-1 array('D') with bounds (nt) and a storage\ninfo : int\n"
    ...

def zpftrs(n, a, b, transr=..., uplo=..., overwrite_b=...) -> typing.Any:
    "x,info = zpftrs(n,a,b,[transr,uplo,overwrite_b])\n\nWrapper for ``zpftrs``.\n\nParameters\n----------\nn : input int\na : input rank-1 array('D') with bounds (nt)\nb : input rank-2 array('D') with bounds (ldb,nhrs)\n\nOther Parameters\n----------------\ntransr : input string(len=1), optional\n    Default: 'N'\nuplo : input string(len=1), optional\n    Default: 'U'\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('D') with bounds (ldb,nhrs) and b storage\ninfo : int\n"
    ...

def zpocon(a, anorm, uplo=...) -> typing.Any:
    "rcond,info = zpocon(a,anorm,[uplo])\n\nWrapper for ``zpocon``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (n,n)\nanorm : input float\n\nOther Parameters\n----------------\nuplo : input string(len=1), optional\n    Default: 'U'\n\nReturns\n-------\nrcond : float\ninfo : int\n"
    ...

def zposv(a, b, lower=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "c,x,info = zposv(a,b,[lower,overwrite_a,overwrite_b])\n\nWrapper for ``zposv``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (n,n)\nb : input rank-2 array('D') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('D') with bounds (n,n) and a storage\nx : rank-2 array('D') with bounds (n,nrhs) and b storage\ninfo : int\n"
    ...

def zposvx(a, b, fact=..., af=..., equed=..., s=..., lower=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "a_s,lu,equed,s,b_s,x,rcond,ferr,berr,info = zposvx(a,b,[fact,af,equed,s,lower,overwrite_a,overwrite_b])\n\nWrapper for ``zposvx``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (n,n)\nb : input rank-2 array('D') with bounds (n,nrhs)\n\nOther Parameters\n----------------\nfact : input string(len=1), optional\n    Default: 'E'\noverwrite_a : input int, optional\n    Default: 0\naf : input rank-2 array('D') with bounds (n,n)\nequed : input string(len=1), optional\n    Default: 'Y'\ns : input rank-1 array('d') with bounds (n)\noverwrite_b : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\na_s : rank-2 array('D') with bounds (n,n) and a storage\nlu : rank-2 array('D') with bounds (n,n) and af storage\nequed : string(len=1)\ns : rank-1 array('d') with bounds (n)\nb_s : rank-2 array('D') with bounds (n,nrhs) and b storage\nx : rank-2 array('D') with bounds (n,nrhs)\nrcond : float\nferr : rank-1 array('d') with bounds (nrhs)\nberr : rank-1 array('d') with bounds (nrhs)\ninfo : int\n"
    ...

def zpotrf(a, lower=..., clean=..., overwrite_a=...) -> typing.Any:
    "c,info = zpotrf(a,[lower,clean,overwrite_a])\n\nWrapper for ``zpotrf``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\nclean : input int, optional\n    Default: 1\n\nReturns\n-------\nc : rank-2 array('D') with bounds (n,n) and a storage\ninfo : int\n"
    ...

def zpotri(c, lower=..., overwrite_c=...) -> typing.Any:
    "inv_a,info = zpotri(c,[lower,overwrite_c])\n\nWrapper for ``zpotri``.\n\nParameters\n----------\nc : input rank-2 array('D') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_c : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\ninv_a : rank-2 array('D') with bounds (n,n) and c storage\ninfo : int\n"
    ...

def zpotrs(c, b, lower=..., overwrite_b=...) -> typing.Any:
    "x,info = zpotrs(c,b,[lower,overwrite_b])\n\nWrapper for ``zpotrs``.\n\nParameters\n----------\nc : input rank-2 array('D') with bounds (n,n)\nb : input rank-2 array('D') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_b : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('D') with bounds (n,nrhs) and b storage\ninfo : int\n"
    ...

def zppcon(n, ap, anorm, lower=...) -> typing.Any:
    "rcond,info = zppcon(n,ap,anorm,[lower])\n\nWrapper for ``zppcon``.\n\nParameters\n----------\nn : input int\nap : input rank-1 array('D') with bounds (L)\nanorm : input float\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nrcond : float\ninfo : int\n"
    ...

def zppsv(n, ap, b, lower=..., overwrite_b=...) -> typing.Any:
    "x,info = zppsv(n,ap,b,[lower,overwrite_b])\n\nWrapper for ``zppsv``.\n\nParameters\n----------\nn : input int\nap : input rank-1 array('D') with bounds (L)\nb : input rank-2 array('D') with bounds (ldb,nrhs)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('D') with bounds (ldb,nrhs) and b storage\ninfo : int\n"
    ...

def zpptrf(n, ap, lower=..., overwrite_ap=...) -> typing.Any:
    "ul,info = zpptrf(n,ap,[lower,overwrite_ap])\n\nWrapper for ``zpptrf``.\n\nParameters\n----------\nn : input int\nap : input rank-1 array('D') with bounds (L)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\noverwrite_ap : input int, optional\n    Default: 0\n\nReturns\n-------\nul : rank-1 array('D') with bounds (L) and ap storage\ninfo : int\n"
    ...

def zpptri(n, ap, lower=..., overwrite_ap=...) -> typing.Any:
    "uli,info = zpptri(n,ap,[lower,overwrite_ap])\n\nWrapper for ``zpptri``.\n\nParameters\n----------\nn : input int\nap : input rank-1 array('D') with bounds (L)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\noverwrite_ap : input int, optional\n    Default: 0\n\nReturns\n-------\nuli : rank-1 array('D') with bounds (L) and ap storage\ninfo : int\n"
    ...

def zpptrs(n, ap, b, lower=..., overwrite_b=...) -> typing.Any:
    "x,info = zpptrs(n,ap,b,[lower,overwrite_b])\n\nWrapper for ``zpptrs``.\n\nParameters\n----------\nn : input int\nap : input rank-1 array('D') with bounds (L)\nb : input rank-2 array('D') with bounds (ldb,nrhs)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('D') with bounds (ldb,nrhs) and b storage\ninfo : int\n"
    ...

def zpstf2(a, tol=..., lower=..., overwrite_a=...) -> typing.Any:
    "c,piv,rank_c,info = zpstf2(a,[tol,lower,overwrite_a])\n\nWrapper for ``zpstf2``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\ntol : input float, optional\n    Default: -1.0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('D') with bounds (n,n) and a storage\npiv : rank-1 array('i') with bounds (n)\nrank_c : int\ninfo : int\n"
    ...

def zpstrf(a, tol=..., lower=..., overwrite_a=...) -> typing.Any:
    "c,piv,rank_c,info = zpstrf(a,[tol,lower,overwrite_a])\n\nWrapper for ``zpstrf``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\ntol : input float, optional\n    Default: -1.0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('D') with bounds (n,n) and a storage\npiv : rank-1 array('i') with bounds (n)\nrank_c : int\ninfo : int\n"
    ...

def zpteqr(d, e, z, compute_z=..., overwrite_d=..., overwrite_e=..., overwrite_z=...) -> typing.Any:
    "d,e,z,info = zpteqr(d,e,z,[compute_z,overwrite_d,overwrite_e,overwrite_z])\n\nWrapper for ``zpteqr``.\n\nParameters\n----------\nd : input rank-1 array('d') with bounds (n)\ne : input rank-1 array('d') with bounds ((n>0?n-1:0))\nz : input rank-2 array('D') with bounds ((compute_z==0?shape(z, 0):max(1,n)),(compute_z==0?shape(z, 1):n))\n\nOther Parameters\n----------------\ncompute_z : input int, optional\n    Default: 0\noverwrite_d : input int, optional\n    Default: 0\noverwrite_e : input int, optional\n    Default: 0\noverwrite_z : input int, optional\n    Default: 0\n\nReturns\n-------\nd : rank-1 array('d') with bounds (n)\ne : rank-1 array('d') with bounds ((n>0?n-1:0))\nz : rank-2 array('D') with bounds ((compute_z==0?shape(z, 0):max(1,n)),(compute_z==0?shape(z, 1):n))\ninfo : int\n"
    ...

def zptsv(d, e, b, overwrite_d=..., overwrite_e=..., overwrite_b=...) -> typing.Any:
    "d,du,x,info = zptsv(d,e,b,[overwrite_d,overwrite_e,overwrite_b])\n\nWrapper for ``zptsv``.\n\nParameters\n----------\nd : input rank-1 array('d') with bounds (n)\ne : input rank-1 array('D') with bounds (n - 1)\nb : input rank-2 array('D') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_d : input int, optional\n    Default: 0\noverwrite_e : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nd : rank-1 array('d') with bounds (n)\ndu : rank-1 array('D') with bounds (n - 1) and e storage\nx : rank-2 array('D') with bounds (n,nrhs) and b storage\ninfo : int\n"
    ...

def zptsvx(d, e, b, fact=..., df=..., ef=...) -> typing.Any:
    "df,ef,x,rcond,ferr,berr,info = zptsvx(d,e,b,[fact,df,ef])\n\nWrapper for ``zptsvx``.\n\nParameters\n----------\nd : input rank-1 array('d') with bounds (n)\ne : input rank-1 array('D') with bounds (max(0, n-1))\nb : input rank-2 array('D') with bounds (ldb,nrhs)\n\nOther Parameters\n----------------\nfact : input string(len=1), optional\n    Default: 'N'\ndf : input rank-1 array('d') with bounds (n)\nef : input rank-1 array('D') with bounds (max(0, n-1))\n\nReturns\n-------\ndf : rank-1 array('d') with bounds (n)\nef : rank-1 array('D') with bounds (max(0, n-1))\nx : rank-2 array('D') with bounds (ldx,nrhs)\nrcond : float\nferr : rank-1 array('d') with bounds (nrhs)\nberr : rank-1 array('d') with bounds (nrhs)\ninfo : int\n"
    ...

def zpttrf(d, e, overwrite_d=..., overwrite_e=...) -> typing.Any:
    "d,e,info = zpttrf(d,e,[overwrite_d,overwrite_e])\n\nWrapper for ``zpttrf``.\n\nParameters\n----------\nd : input rank-1 array('d') with bounds (n)\ne : input rank-1 array('D') with bounds ((n>0?n-1:0))\n\nOther Parameters\n----------------\noverwrite_d : input int, optional\n    Default: 0\noverwrite_e : input int, optional\n    Default: 0\n\nReturns\n-------\nd : rank-1 array('d') with bounds (n)\ne : rank-1 array('D') with bounds ((n>0?n-1:0))\ninfo : int\n"
    ...

def zpttrs(d, e, b, lower=..., overwrite_b=...) -> typing.Any:
    "x,info = zpttrs(d,e,b,[lower,overwrite_b])\n\nWrapper for ``zpttrs``.\n\nParameters\n----------\nd : input rank-1 array('d') with bounds (n)\ne : input rank-1 array('D') with bounds ((n>0?n-1:0))\nb : input rank-2 array('D') with bounds (ldb,nrhs)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('D') with bounds (ldb,nrhs) and b storage\ninfo : int\n"
    ...

def zrot(x, y, c, s, n=..., offx=..., incx=..., offy=..., incy=..., overwrite_x=..., overwrite_y=...) -> typing.Any:
    "x,y = zrot(x,y,c,s,[n,offx,incx,offy,incy,overwrite_x,overwrite_y])\n\nWrapper for ``zrot``.\n\nParameters\n----------\nx : input rank-1 array('D') with bounds (lx)\ny : input rank-1 array('D') with bounds (ly)\nc : input float\ns : input complex\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (lx-1-offx)/abs(incx)+1\noverwrite_x : input int, optional\n    Default: 0\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noverwrite_y : input int, optional\n    Default: 0\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\n\nReturns\n-------\nx : rank-1 array('D') with bounds (lx)\ny : rank-1 array('D') with bounds (ly)\n"
    ...

def zsycon(a, ipiv, anorm, lower=...) -> typing.Any:
    "rcond,info = zsycon(a,ipiv,anorm,[lower])\n\nWrapper for ``zsycon``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (n,n)\nipiv : input rank-1 array('i') with bounds (n)\nanorm : input float\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nrcond : float\ninfo : int\n"
    ...

def zsyconv(a, ipiv, lower=..., way=..., overwrite_a=...) -> typing.Any:
    "a,e,info = zsyconv(a,ipiv,[lower,way,overwrite_a])\n\nWrapper for ``zsyconv``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (n,n)\nipiv : input rank-1 array('i') with bounds (n)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\nway : input int, optional\n    Default: 0\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\na : rank-2 array('D') with bounds (n,n)\ne : rank-1 array('D') with bounds (n)\ninfo : int\n"
    ...

def zsyequb(a, lower=...) -> typing.Any:
    "s,scond,amax,info = zsyequb(a,[lower])\n\nWrapper for ``zsyequb``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (lda,n)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\ns : rank-1 array('d') with bounds (n)\nscond : float\namax : float\ninfo : int\n"
    ...

def zsysv(a, b, lwork=..., lower=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "udut,ipiv,x,info = zsysv(a,b,[lwork,lower,overwrite_a,overwrite_b])\n\nWrapper for ``zsysv``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (n,n)\nb : input rank-2 array('D') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(n,1)\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nudut : rank-2 array('D') with bounds (n,n) and a storage\nipiv : rank-1 array('i') with bounds (n)\nx : rank-2 array('D') with bounds (n,nrhs) and b storage\ninfo : int\n"
    ...

def zsysv_lwork(n, lower=...) -> typing.Any:
    'work,info = zsysv_lwork(n,[lower])\n\nWrapper for ``zsysv_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    ...

def zsysvx(a, b, af=..., ipiv=..., lwork=..., factored=..., lower=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "a_s,udut,ipiv,b_s,x,rcond,ferr,berr,info = zsysvx(a,b,[af,ipiv,lwork,factored,lower,overwrite_a,overwrite_b])\n\nWrapper for ``zsysvx``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (n,n)\nb : input rank-2 array('D') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\naf : input rank-2 array('D') with bounds (n,n)\nipiv : input rank-1 array('i') with bounds (n)\noverwrite_b : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(3*n,1)\nfactored : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\na_s : rank-2 array('D') with bounds (n,n) and a storage\nudut : rank-2 array('D') with bounds (n,n) and af storage\nipiv : rank-1 array('i') with bounds (n)\nb_s : rank-2 array('D') with bounds (n,nrhs) and b storage\nx : rank-2 array('D') with bounds (n,nrhs)\nrcond : float\nferr : rank-1 array('d') with bounds (nrhs)\nberr : rank-1 array('d') with bounds (nrhs)\ninfo : int\n"
    ...

def zsysvx_lwork(n, lower=...) -> typing.Any:
    'work,info = zsysvx_lwork(n,[lower])\n\nWrapper for ``zsysvx_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    ...

def zsytf2(a, lower=..., overwrite_a=...) -> typing.Any:
    "ldu,ipiv,info = zsytf2(a,[lower,overwrite_a])\n\nWrapper for ``zsytf2``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (n,n)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\nldu : rank-2 array('D') with bounds (n,n) and a storage\nipiv : rank-1 array('i') with bounds (n)\ninfo : int\n"
    ...

def zsytrf(a, lower=..., lwork=..., overwrite_a=...) -> typing.Any:
    "ldu,ipiv,info = zsytrf(a,[lower,lwork,overwrite_a])\n\nWrapper for ``zsytrf``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (n,n)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(n,1)\n\nReturns\n-------\nldu : rank-2 array('D') with bounds (n,n) and a storage\nipiv : rank-1 array('i') with bounds (n)\ninfo : int\n"
    ...

def zsytrf_lwork(n, lower=...) -> typing.Any:
    'work,info = zsytrf_lwork(n,[lower])\n\nWrapper for ``zsytrf_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    ...

def ztbtrs(ab, b, uplo=..., trans=..., diag=..., overwrite_b=...) -> typing.Any:
    "x,info = ztbtrs(ab,b,[uplo,trans,diag,overwrite_b])\n\nWrapper for ``ztbtrs``.\n\nParameters\n----------\nab : input rank-2 array('D') with bounds (ldab,n)\nb : input rank-2 array('D') with bounds (ldb,nrhs)\n\nOther Parameters\n----------------\nuplo : input string(len=1), optional\n    Default: 'U'\ntrans : input string(len=1), optional\n    Default: 'N'\ndiag : input string(len=1), optional\n    Default: 'N'\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('D') with bounds (ldb,nrhs) and b storage\ninfo : int\n"
    ...

def ztfsm(alpha, a, b, transr=..., side=..., uplo=..., trans=..., diag=..., overwrite_b=...) -> typing.Any:
    "x = ztfsm(alpha,a,b,[transr,side,uplo,trans,diag,overwrite_b])\n\nWrapper for ``ztfsm``.\n\nParameters\n----------\nalpha : input complex\na : input rank-1 array('D') with bounds (nt)\nb : input rank-2 array('D') with bounds (m,n)\n\nOther Parameters\n----------------\ntransr : input string(len=1), optional\n    Default: 'N'\nside : input string(len=1), optional\n    Default: 'L'\nuplo : input string(len=1), optional\n    Default: 'U'\ntrans : input string(len=1), optional\n    Default: 'N'\ndiag : input string(len=1), optional\n    Default: 'N'\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('D') with bounds (m,n) and b storage\n"
    ...

def ztfttp(n, arf, transr=..., uplo=...) -> typing.Any:
    "ap,info = ztfttp(n,arf,[transr,uplo])\n\nWrapper for ``ztfttp``.\n\nParameters\n----------\nn : input int\narf : input rank-1 array('D') with bounds (nt)\n\nOther Parameters\n----------------\ntransr : input string(len=1), optional\n    Default: 'N'\nuplo : input string(len=1), optional\n    Default: 'U'\n\nReturns\n-------\nap : rank-1 array('D') with bounds (nt)\ninfo : int\n"
    ...

def ztfttr(n, arf, transr=..., uplo=...) -> typing.Any:
    "a,info = ztfttr(n,arf,[transr,uplo])\n\nWrapper for ``ztfttr``.\n\nParameters\n----------\nn : input int\narf : input rank-1 array('D') with bounds (nt)\n\nOther Parameters\n----------------\ntransr : input string(len=1), optional\n    Default: 'N'\nuplo : input string(len=1), optional\n    Default: 'U'\n\nReturns\n-------\na : rank-2 array('D') with bounds (lda,n)\ninfo : int\n"
    ...

def ztgsen(select, a, b, q, z, lwork=..., liwork=..., overwrite_a=..., overwrite_b=..., overwrite_q=..., overwrite_z=...) -> typing.Any:
    "a,b,alpha,beta,q,z,m,pl,pr,dif,work,iwork,info = ztgsen(select,a,b,q,z,[lwork,liwork,overwrite_a,overwrite_b,overwrite_q,overwrite_z])\n\nWrapper for ``ztgsen``.\n\nParameters\n----------\nselect : input rank-1 array('i') with bounds (n)\na : input rank-2 array('D') with bounds (lda,n)\nb : input rank-2 array('D') with bounds (ldb,n)\nq : input rank-2 array('D') with bounds (ldq,n)\nz : input rank-2 array('D') with bounds (ldz,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\noverwrite_q : input int, optional\n    Default: 0\noverwrite_z : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(2*m*(n-m),1)\nliwork : input int, optional\n    Default: n+2\n\nReturns\n-------\na : rank-2 array('D') with bounds (lda,n)\nb : rank-2 array('D') with bounds (ldb,n)\nalpha : rank-1 array('D') with bounds (n)\nbeta : rank-1 array('D') with bounds (n)\nq : rank-2 array('D') with bounds (ldq,n)\nz : rank-2 array('D') with bounds (ldz,n)\nm : int\npl : float\npr : float\ndif : rank-1 array('d') with bounds (2)\nwork : rank-1 array('D') with bounds (MAX(lwork,1))\niwork : rank-1 array('i') with bounds (MAX(1,liwork))\ninfo : int\n"
    ...

def ztpmqrt(l, v, t, a, b, side=..., trans=..., overwrite_a=..., overwrite_b=...) -> typing.Any:
    "a,b,info = ztpmqrt(l,v,t,a,b,[side,trans,overwrite_a,overwrite_b])\n\nWrapper for ``ztpmqrt``.\n\nParameters\n----------\nl : input int\nv : input rank-2 array('D') with bounds ((side[0]=='L'?m:n),k)\nt : input rank-2 array('D') with bounds (nb,k)\na : input rank-2 array('D') with bounds ((side[0]=='L'?k:m),(side[0]=='L'?n:k))\nb : input rank-2 array('D') with bounds (m,n)\n\nOther Parameters\n----------------\nside : input string(len=1), optional\n    Default: 'L'\ntrans : input string(len=1), optional\n    Default: 'N'\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\na : rank-2 array('D') with bounds ((side[0]=='L'?k:m),(side[0]=='L'?n:k))\nb : rank-2 array('D') with bounds (m,n)\ninfo : int\n"
    ...

def ztpqrt(l, nb, a, b, overwrite_a=..., overwrite_b=...) -> typing.Any:
    "a,b,t,info = ztpqrt(l,nb,a,b,[overwrite_a,overwrite_b])\n\nWrapper for ``ztpqrt``.\n\nParameters\n----------\nl : input int\nnb : input int\na : input rank-2 array('D') with bounds (n,n)\nb : input rank-2 array('D') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\na : rank-2 array('D') with bounds (n,n)\nb : rank-2 array('D') with bounds (m,n)\nt : rank-2 array('D') with bounds (nb,n)\ninfo : int\n"
    ...

def ztpttf(n, ap, transr=..., uplo=...) -> typing.Any:
    "arf,info = ztpttf(n,ap,[transr,uplo])\n\nWrapper for ``ztpttf``.\n\nParameters\n----------\nn : input int\nap : input rank-1 array('D') with bounds (nt)\n\nOther Parameters\n----------------\ntransr : input string(len=1), optional\n    Default: 'N'\nuplo : input string(len=1), optional\n    Default: 'U'\n\nReturns\n-------\narf : rank-1 array('D') with bounds (nt)\ninfo : int\n"
    ...

def ztpttr(n, ap, uplo=...) -> typing.Any:
    "a,info = ztpttr(n,ap,[uplo])\n\nWrapper for ``ztpttr``.\n\nParameters\n----------\nn : input int\nap : input rank-1 array('D') with bounds (nt)\n\nOther Parameters\n----------------\nuplo : input string(len=1), optional\n    Default: 'U'\n\nReturns\n-------\na : rank-2 array('D') with bounds (n,n)\ninfo : int\n"
    ...

def ztrsyl(a, b, c, trana=..., tranb=..., isgn=..., overwrite_c=...) -> typing.Any:
    "x,scale,info = ztrsyl(a,b,c,[trana,tranb,isgn,overwrite_c])\n\nWrapper for ``ztrsyl``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (m,m)\nb : input rank-2 array('D') with bounds (n,n)\nc : input rank-2 array('D') with bounds (m,n)\n\nOther Parameters\n----------------\ntrana : input string(len=1), optional\n    Default: 'N'\ntranb : input string(len=1), optional\n    Default: 'N'\nisgn : input int, optional\n    Default: 1\noverwrite_c : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('D') with bounds (m,n) and c storage\nscale : float\ninfo : int\n"
    ...

def ztrtri(c, lower=..., unitdiag=..., overwrite_c=...) -> typing.Any:
    "inv_c,info = ztrtri(c,[lower,unitdiag,overwrite_c])\n\nWrapper for ``ztrtri``.\n\nParameters\n----------\nc : input rank-2 array('D') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_c : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\nunitdiag : input int, optional\n    Default: 0\n\nReturns\n-------\ninv_c : rank-2 array('D') with bounds (n,n) and c storage\ninfo : int\n"
    ...

def ztrtrs(a, b, lower=..., trans=..., unitdiag=..., lda=..., overwrite_b=...) -> typing.Any:
    "x,info = ztrtrs(a,b,[lower,trans,unitdiag,lda,overwrite_b])\n\nWrapper for ``ztrtrs``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (lda,n)\nb : input rank-2 array('D') with bounds (ldb,nrhs)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\nunitdiag : input int, optional\n    Default: 0\nlda : input int, optional\n    Default: shape(a,0)\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('D') with bounds (ldb,nrhs) and b storage\ninfo : int\n"
    ...

def ztrttf(a, transr=..., uplo=...) -> typing.Any:
    "arf,info = ztrttf(a,[transr,uplo])\n\nWrapper for ``ztrttf``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (lda,n)\n\nOther Parameters\n----------------\ntransr : input string(len=1), optional\n    Default: 'N'\nuplo : input string(len=1), optional\n    Default: 'U'\n\nReturns\n-------\narf : rank-1 array('D') with bounds (n*(n+1)/2)\ninfo : int\n"
    ...

def ztrttp(a, uplo=...) -> typing.Any:
    "ap,info = ztrttp(a,[uplo])\n\nWrapper for ``ztrttp``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (lda,n)\n\nOther Parameters\n----------------\nuplo : input string(len=1), optional\n    Default: 'U'\n\nReturns\n-------\nap : rank-1 array('D') with bounds (n*(n+1)/2)\ninfo : int\n"
    ...

def ztzrzf(a, lwork=..., overwrite_a=...) -> typing.Any:
    "rz,tau,info = ztzrzf(a,[lwork,overwrite_a])\n\nWrapper for ``ztzrzf``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: MAX(m,1)\n\nReturns\n-------\nrz : rank-2 array('D') with bounds (m,n) and a storage\ntau : rank-1 array('D') with bounds (m)\ninfo : int\n"
    ...

def ztzrzf_lwork(m, n) -> typing.Any:
    'work,info = ztzrzf_lwork(m,n)\n\nWrapper for ``ztzrzf_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    ...

def zuncsd(x11, x12, x21, x22, compute_u1=..., compute_u2=..., compute_v1t=..., compute_v2t=..., trans=..., signs=..., lwork=..., lrwork=..., overwrite_x11=..., overwrite_x12=..., overwrite_x21=..., overwrite_x22=...) -> typing.Any:
    "cs11,cs12,cs21,cs22,theta,u1,u2,v1t,v2t,info = zuncsd(x11,x12,x21,x22,[compute_u1,compute_u2,compute_v1t,compute_v2t,trans,signs,lwork,lrwork,overwrite_x11,overwrite_x12,overwrite_x21,overwrite_x22])\n\nWrapper for ``zuncsd``.\n\nParameters\n----------\nx11 : input rank-2 array('D') with bounds (p,q)\nx12 : input rank-2 array('D') with bounds (p,mmq)\nx21 : input rank-2 array('D') with bounds (mmp,q)\nx22 : input rank-2 array('D') with bounds (mmp,mmq)\n\nOther Parameters\n----------------\ncompute_u1 : input int, optional\n    Default: 1\ncompute_u2 : input int, optional\n    Default: 1\ncompute_v1t : input int, optional\n    Default: 1\ncompute_v2t : input int, optional\n    Default: 1\ntrans : input int, optional\n    Default: 0\nsigns : input int, optional\n    Default: 0\noverwrite_x11 : input int, optional\n    Default: 0\noverwrite_x12 : input int, optional\n    Default: 0\noverwrite_x21 : input int, optional\n    Default: 0\noverwrite_x22 : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: 2*m+MAX(1,MAX(mmp,mmq))+1\nlrwork : input int, optional\n    Default: 5*MAX(1,q-1)+4*MAX(1,q)+8*q+1\n\nReturns\n-------\ncs11 : rank-2 array('D') with bounds (p,q) and x11 storage\ncs12 : rank-2 array('D') with bounds (p,mmq) and x12 storage\ncs21 : rank-2 array('D') with bounds (mmp,q) and x21 storage\ncs22 : rank-2 array('D') with bounds (mmp,mmq) and x22 storage\ntheta : rank-1 array('d') with bounds (min(min(p,mmp),min(q,mmq)))\nu1 : rank-2 array('D') with bounds ((compute_u1?p:0),(compute_u1?p:0))\nu2 : rank-2 array('D') with bounds ((compute_u2?mmp:0),(compute_u2?mmp:0))\nv1t : rank-2 array('D') with bounds ((compute_v1t?q:0),(compute_v1t?q:0))\nv2t : rank-2 array('D') with bounds ((compute_v2t?mmq:0),(compute_v2t?mmq:0))\ninfo : int\n"
    ...

def zuncsd_lwork(m, p, q) -> typing.Any:
    'work,rwork,info = zuncsd_lwork(m,p,q)\n\nWrapper for ``zuncsd_lwork``.\n\nParameters\n----------\nm : input int\np : input int\nq : input int\n\nReturns\n-------\nwork : complex\nrwork : float\ninfo : int\n'
    ...

def zunghr(a, tau, lo=..., hi=..., lwork=..., overwrite_a=...) -> typing.Any:
    "ht,info = zunghr(a,tau,[lo,hi,lwork,overwrite_a])\n\nWrapper for ``zunghr``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (n,n)\ntau : input rank-1 array('D') with bounds (n - 1)\n\nOther Parameters\n----------------\nlo : input int, optional\n    Default: 0\nhi : input int, optional\n    Default: n-1\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(hi-lo,1)\n\nReturns\n-------\nht : rank-2 array('D') with bounds (n,n) and a storage\ninfo : int\n"
    ...

def zunghr_lwork(n, lo=..., hi=...) -> typing.Any:
    'work,info = zunghr_lwork(n,[lo,hi])\n\nWrapper for ``zunghr_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlo : input int, optional\n    Default: 0\nhi : input int, optional\n    Default: n-1\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    ...

def zungqr(a, tau, lwork=..., overwrite_a=...) -> typing.Any:
    "q,work,info = zungqr(a,tau,[lwork,overwrite_a])\n\nWrapper for ``zungqr``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (m,n)\ntau : input rank-1 array('D') with bounds (k)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(3*n,1)\n\nReturns\n-------\nq : rank-2 array('D') with bounds (m,n) and a storage\nwork : rank-1 array('D') with bounds (MAX(lwork,1))\ninfo : int\n"
    ...

def zungrq(a, tau, lwork=..., overwrite_a=...) -> typing.Any:
    "q,work,info = zungrq(a,tau,[lwork,overwrite_a])\n\nWrapper for ``zungrq``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (m,n)\ntau : input rank-1 array('D') with bounds (k)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: max(3*m,1)\n\nReturns\n-------\nq : rank-2 array('D') with bounds (m,n) and a storage\nwork : rank-1 array('D') with bounds (MAX(lwork,1))\ninfo : int\n"
    ...

def zunmqr(side, trans, a, tau, c, lwork, overwrite_c=...) -> typing.Any:
    "cq,work,info = zunmqr(side,trans,a,tau,c,lwork,[overwrite_c])\n\nWrapper for ``zunmqr``.\n\nParameters\n----------\nside : input string(len=1)\ntrans : input string(len=1)\na : input rank-2 array('D') with bounds (lda,k)\ntau : input rank-1 array('D') with bounds (k)\nc : input rank-2 array('D') with bounds (ldc,n)\nlwork : input int\n\nOther Parameters\n----------------\noverwrite_c : input int, optional\n    Default: 0\n\nReturns\n-------\ncq : rank-2 array('D') with bounds (ldc,n) and c storage\nwork : rank-1 array('D') with bounds (MAX(lwork,1))\ninfo : int\n"
    ...

def zunmrz(a, tau, c, side=..., trans=..., lwork=..., overwrite_c=...) -> typing.Any:
    "cq,info = zunmrz(a,tau,c,[side,trans,lwork,overwrite_c])\n\nWrapper for ``zunmrz``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (k,nt)\ntau : input rank-1 array('D') with bounds (k)\nc : input rank-2 array('D') with bounds (m,n)\n\nOther Parameters\n----------------\nside : input string(len=1), optional\n    Default: 'L'\ntrans : input string(len=1), optional\n    Default: 'N'\noverwrite_c : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: MAX((side[0]=='L'?n:m),1)\n\nReturns\n-------\ncq : rank-2 array('D') with bounds (m,n) and c storage\ninfo : int\n"
    ...

def zunmrz_lwork(m, n, side=..., trans=...) -> typing.Any:
    "work,info = zunmrz_lwork(m,n,[side,trans])\n\nWrapper for ``zunmrz_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\n\nOther Parameters\n----------------\nside : input string(len=1), optional\n    Default: 'L'\ntrans : input string(len=1), optional\n    Default: 'N'\n\nReturns\n-------\nwork : complex\ninfo : int\n"
    ...

def __getattr__(name) -> typing.Any:
    ...

