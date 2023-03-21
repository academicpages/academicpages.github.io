# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: scipy, version: 1.6.2
# Module: scipy.linalg._interpolative, version: $Revision: $
import typing
import builtins as _mod_builtins

__doc__: str
__file__: str
__name__: str
__package__: str
__version__: bytes
def id_srand(n) -> typing.Any:
    "r = id_srand(n)\n\nWrapper for ``id_srand``.\n\nParameters\n----------\nn : input int\n\nReturns\n-------\nr : rank-1 array('d') with bounds (n)\n"
    ...

def id_srandi(t) -> typing.Any:
    "id_srandi(t)\n\nWrapper for ``id_srandi``.\n\nParameters\n----------\nt : input rank-1 array('d') with bounds (55)\n"
    ...

def id_srando() -> typing.Any:
    'id_srando()\n\nWrapper for ``id_srando``.\n\n'
    ...

def idd_copycols(a, krank, list, m=..., n=...) -> typing.Any:
    "col = idd_copycols(a,krank,list,[m,n])\n\nWrapper for ``idd_copycols``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (m,n)\nkrank : input int\nlist : input rank-1 array('i') with bounds (*)\n\nOther Parameters\n----------------\nm : input int, optional\n    Default: shape(a,0)\nn : input int, optional\n    Default: shape(a,1)\n\nReturns\n-------\ncol : rank-2 array('d') with bounds (m,krank)\n"
    ...

def idd_diffsnorm(m, n, matvect, matvect2, matvec, matvec2, its, p1t=..., p2t=..., p3t=..., p4t=..., p1t2=..., p2t2=..., p3t2=..., p4t2=..., p1=..., p2=..., p3=..., p4=..., p12=..., p22=..., p32=..., p42=..., w=..., matvect_extra_args=..., matvect2_extra_args=..., matvec_extra_args=..., matvec2_extra_args=...) -> typing.Any:
    "snorm = idd_diffsnorm(m,n,matvect,matvect2,matvec,matvec2,its,[p1t,p2t,p3t,p4t,p1t2,p2t2,p3t2,p4t2,p1,p2,p3,p4,p12,p22,p32,p42,w,matvect_extra_args,matvect2_extra_args,matvec_extra_args,matvec2_extra_args])\n\nWrapper for ``idd_diffsnorm``.\n\nParameters\n----------\nm : input int\nn : input int\nmatvect : call-back function\nmatvect2 : call-back function\nmatvec : call-back function\nmatvec2 : call-back function\nits : input int\n\nOther Parameters\n----------------\nmatvect_extra_args : input tuple, optional\n    Default: ()\np1t : input float\np2t : input float\np3t : input float\np4t : input float\nmatvect2_extra_args : input tuple, optional\n    Default: ()\np1t2 : input float\np2t2 : input float\np3t2 : input float\np4t2 : input float\nmatvec_extra_args : input tuple, optional\n    Default: ()\np1 : input float\np2 : input float\np3 : input float\np4 : input float\nmatvec2_extra_args : input tuple, optional\n    Default: ()\np12 : input float\np22 : input float\np32 : input float\np42 : input float\nw : input rank-1 array('d') with bounds (3*(m+n))\n\nReturns\n-------\nsnorm : float\n\nNotes\n-----\nCall-back functions::\n\n  def matvect(x,[m,n,p1,p2,p3,p4]): return y\n  Required arguments:\n    x : input rank-1 array('d') with bounds (m)\n  Optional arguments:\n    m : input int, optional\n    Default: len(x)\n    n : input int\n    p1 : input float\n    p2 : input float\n    p3 : input float\n    p4 : input float\n  Return objects:\n    y : rank-1 array('d') with bounds (n)\n  def matvect2(x,[m,n,p1,p2,p3,p4]): return y\n  Required arguments:\n    x : input rank-1 array('d') with bounds (m)\n  Optional arguments:\n    m : input int, optional\n    Default: len(x)\n    n : input int\n    p1 : input float\n    p2 : input float\n    p3 : input float\n    p4 : input float\n  Return objects:\n    y : rank-1 array('d') with bounds (n)\n  def matvec(x,[n,m,p1,p2,p3,p4]): return y\n  Required arguments:\n    x : input rank-1 array('d') with bounds (n)\n  Optional arguments:\n    n : input int, optional\n    Default: len(x)\n    m : input int\n    p1 : input float\n    p2 : input float\n    p3 : input float\n    p4 : input float\n  Return objects:\n    y : rank-1 array('d') with bounds (m)\n  def matvec2(x,[n,m,p1,p2,p3,p4]): return y\n  Required arguments:\n    x : input rank-1 array('d') with bounds (n)\n  Optional arguments:\n    n : input int, optional\n    Default: len(x)\n    m : input int\n    p1 : input float\n    p2 : input float\n    p3 : input float\n    p4 : input float\n  Return objects:\n    y : rank-1 array('d') with bounds (m)\n"
    ...

def idd_estrank(eps, a, w, ra, m=..., n=...) -> typing.Any:
    "krank,ra = idd_estrank(eps,a,w,ra,[m,n])\n\nWrapper for ``idd_estrank``.\n\nParameters\n----------\neps : input float\na : input rank-2 array('d') with bounds (m,n)\nw : input rank-1 array('d') with bounds (17 * m + 70)\nra : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\nm : input int, optional\n    Default: shape(a,0)\nn : input int, optional\n    Default: shape(a,1)\n\nReturns\n-------\nkrank : int\nra : rank-1 array('d') with bounds (*)\n"
    ...

def idd_findrank(eps, m, n, matvect, p1=..., p2=..., p3=..., p4=..., w=..., matvect_extra_args=...) -> typing.Any:
    "krank,ra,ier = idd_findrank(eps,m,n,matvect,[p1,p2,p3,p4,w,matvect_extra_args])\n\nWrapper for ``idd_findrank``.\n\nParameters\n----------\neps : input float\nm : input int\nn : input int\nmatvect : call-back function\n\nOther Parameters\n----------------\nmatvect_extra_args : input tuple, optional\n    Default: ()\np1 : input float\np2 : input float\np3 : input float\np4 : input float\nw : input rank-1 array('d') with bounds (m+2*n+1)\n\nReturns\n-------\nkrank : int\nra : rank-1 array('d') with bounds (2*n*min(m,n))\nier : int\n\nNotes\n-----\nCall-back functions::\n\n  def matvect(x,[m,n,p1,p2,p3,p4]): return y\n  Required arguments:\n    x : input rank-1 array('d') with bounds (m)\n  Optional arguments:\n    m : input int, optional\n    Default: len(x)\n    n : input int\n    p1 : input float\n    p2 : input float\n    p3 : input float\n    p4 : input float\n  Return objects:\n    y : rank-1 array('d') with bounds (n)\n"
    ...

def idd_frm(n, w, x, m=...) -> typing.Any:
    "y = idd_frm(n,w,x,[m])\n\nWrapper for ``idd_frm``.\n\nParameters\n----------\nn : input int\nw : input rank-1 array('d') with bounds (17 * m + 70)\nx : input rank-1 array('d') with bounds (m)\n\nOther Parameters\n----------------\nm : input int, optional\n    Default: len(x)\n\nReturns\n-------\ny : rank-1 array('d') with bounds (n)\n"
    ...

def idd_frmi(m) -> typing.Any:
    "n,w = idd_frmi(m)\n\nWrapper for ``idd_frmi``.\n\nParameters\n----------\nm : input int\n\nReturns\n-------\nn : int\nw : rank-1 array('d') with bounds (17 * m + 70)\n"
    ...

def idd_id2svd(b, list, proj, m=..., krank=..., n=..., w=...) -> typing.Any:
    "u,v,s,ier = idd_id2svd(b,list,proj,[m,krank,n,w])\n\nWrapper for ``idd_id2svd``.\n\nParameters\n----------\nb : input rank-2 array('d') with bounds (m,krank)\nlist : input rank-1 array('i') with bounds (n)\nproj : input rank-2 array('d') with bounds (krank,n-krank)\n\nOther Parameters\n----------------\nm : input int, optional\n    Default: shape(b,0)\nkrank : input int, optional\n    Default: shape(b,1)\nn : input int, optional\n    Default: len(list)\nw : input rank-1 array('d') with bounds ((krank+1)*(m+3*n)+26*pow(krank,2))\n\nReturns\n-------\nu : rank-2 array('d') with bounds (m,krank)\nv : rank-2 array('d') with bounds (n,krank)\ns : rank-1 array('d') with bounds (krank)\nier : int\n"
    ...

def idd_reconid(col, list, proj, m=..., krank=..., n=...) -> typing.Any:
    "approx = idd_reconid(col,list,proj,[m,krank,n])\n\nWrapper for ``idd_reconid``.\n\nParameters\n----------\ncol : input rank-2 array('d') with bounds (m,krank)\nlist : input rank-1 array('i') with bounds (n)\nproj : input rank-2 array('d') with bounds (krank,n-krank)\n\nOther Parameters\n----------------\nm : input int, optional\n    Default: shape(col,0)\nkrank : input int, optional\n    Default: shape(col,1)\nn : input int, optional\n    Default: len(list)\n\nReturns\n-------\napprox : rank-2 array('d') with bounds (m,n)\n"
    ...

def idd_reconint(list, proj, n=..., krank=...) -> typing.Any:
    "p = idd_reconint(list,proj,[n,krank])\n\nWrapper for ``idd_reconint``.\n\nParameters\n----------\nlist : input rank-1 array('i') with bounds (n)\nproj : input rank-2 array('d') with bounds (krank,n-krank)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: len(list)\nkrank : input int, optional\n    Default: shape(proj,0)\n\nReturns\n-------\np : rank-2 array('d') with bounds (krank,n)\n"
    ...

def idd_sfrm(l, n, w, x, m=...) -> typing.Any:
    "y = idd_sfrm(l,n,w,x,[m])\n\nWrapper for ``idd_sfrm``.\n\nParameters\n----------\nl : input int\nn : input int\nw : input rank-1 array('d') with bounds (27 * m + 90)\nx : input rank-1 array('d') with bounds (m)\n\nOther Parameters\n----------------\nm : input int, optional\n    Default: len(x)\n\nReturns\n-------\ny : rank-1 array('d') with bounds (l)\n"
    ...

def idd_sfrmi(l, m) -> typing.Any:
    "n,w = idd_sfrmi(l,m)\n\nWrapper for ``idd_sfrmi``.\n\nParameters\n----------\nl : input int\nm : input int\n\nReturns\n-------\nn : int\nw : rank-1 array('d') with bounds (27 * m + 90)\n"
    ...

def idd_snorm(m, n, matvect, matvec, its, p1t=..., p2t=..., p3t=..., p4t=..., p1=..., p2=..., p3=..., p4=..., u=..., matvect_extra_args=..., matvec_extra_args=...) -> typing.Any:
    "snorm,v = idd_snorm(m,n,matvect,matvec,its,[p1t,p2t,p3t,p4t,p1,p2,p3,p4,u,matvect_extra_args,matvec_extra_args])\n\nWrapper for ``idd_snorm``.\n\nParameters\n----------\nm : input int\nn : input int\nmatvect : call-back function\nmatvec : call-back function\nits : input int\n\nOther Parameters\n----------------\nmatvect_extra_args : input tuple, optional\n    Default: ()\np1t : input float\np2t : input float\np3t : input float\np4t : input float\nmatvec_extra_args : input tuple, optional\n    Default: ()\np1 : input float\np2 : input float\np3 : input float\np4 : input float\nu : input rank-1 array('d') with bounds (m)\n\nReturns\n-------\nsnorm : float\nv : rank-1 array('d') with bounds (n)\n\nNotes\n-----\nCall-back functions::\n\n  def matvect(x,[m,n,p1,p2,p3,p4]): return y\n  Required arguments:\n    x : input rank-1 array('d') with bounds (m)\n  Optional arguments:\n    m : input int, optional\n    Default: len(x)\n    n : input int\n    p1 : input float\n    p2 : input float\n    p3 : input float\n    p4 : input float\n  Return objects:\n    y : rank-1 array('d') with bounds (n)\n  def matvec(x,[n,m,p1,p2,p3,p4]): return y\n  Required arguments:\n    x : input rank-1 array('d') with bounds (n)\n  Optional arguments:\n    n : input int, optional\n    Default: len(x)\n    m : input int\n    p1 : input float\n    p2 : input float\n    p3 : input float\n    p4 : input float\n  Return objects:\n    y : rank-1 array('d') with bounds (m)\n"
    ...

def iddp_aid(eps, a, work, proj, m=..., n=...) -> typing.Any:
    "krank,list,proj = iddp_aid(eps,a,work,proj,[m,n])\n\nWrapper for ``iddp_aid``.\n\nParameters\n----------\neps : input float\na : input rank-2 array('d') with bounds (m,n)\nwork : input rank-1 array('d') with bounds (17 * m + 70)\nproj : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\nm : input int, optional\n    Default: shape(a,0)\nn : input int, optional\n    Default: shape(a,1)\n\nReturns\n-------\nkrank : int\nlist : rank-1 array('i') with bounds (n)\nproj : rank-1 array('d') with bounds (*)\n"
    ...

def iddp_asvd(eps, a, winit, w, m=..., n=...) -> typing.Any:
    "krank,iu,iv,is,w,ier = iddp_asvd(eps,a,winit,w,[m,n])\n\nWrapper for ``iddp_asvd``.\n\nParameters\n----------\neps : input float\na : input rank-2 array('d') with bounds (m,n)\nwinit : input rank-1 array('d') with bounds (17 * m + 70)\nw : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\nm : input int, optional\n    Default: shape(a,0)\nn : input int, optional\n    Default: shape(a,1)\n\nReturns\n-------\nkrank : int\niu : int\niv : int\nis : int\nw : rank-1 array('d') with bounds (*)\nier : int\n"
    ...

def iddp_id(eps, a, m=..., n=...) -> typing.Any:
    "krank,list,rnorms = iddp_id(eps,a,[m,n])\n\nWrapper for ``iddp_id``.\n\nParameters\n----------\neps : input float\na : input rank-2 array('d') with bounds (m,n)\n\nOther Parameters\n----------------\nm : input int, optional\n    Default: shape(a,0)\nn : input int, optional\n    Default: shape(a,1)\n\nReturns\n-------\nkrank : int\nlist : rank-1 array('i') with bounds (n)\nrnorms : rank-1 array('d') with bounds (n)\n"
    ...

def iddp_rid(eps, m, n, matvect, proj, p1=..., p2=..., p3=..., p4=..., matvect_extra_args=...) -> typing.Any:
    "krank,list,proj,ier = iddp_rid(eps,m,n,matvect,proj,[p1,p2,p3,p4,matvect_extra_args])\n\nWrapper for ``iddp_rid``.\n\nParameters\n----------\neps : input float\nm : input int\nn : input int\nmatvect : call-back function\nproj : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\nmatvect_extra_args : input tuple, optional\n    Default: ()\np1 : input float\np2 : input float\np3 : input float\np4 : input float\n\nReturns\n-------\nkrank : int\nlist : rank-1 array('i') with bounds (n)\nproj : rank-1 array('d') with bounds (*)\nier : int\n\nNotes\n-----\nCall-back functions::\n\n  def matvect(x,[m,n,p1,p2,p3,p4]): return y\n  Required arguments:\n    x : input rank-1 array('d') with bounds (m)\n  Optional arguments:\n    m : input int, optional\n    Default: len(x)\n    n : input int\n    p1 : input float\n    p2 : input float\n    p3 : input float\n    p4 : input float\n  Return objects:\n    y : rank-1 array('d') with bounds (n)\n"
    ...

def iddp_rsvd(eps, m, n, matvect, matvec, p1t=..., p2t=..., p3t=..., p4t=..., p1=..., p2=..., p3=..., p4=..., matvect_extra_args=..., matvec_extra_args=...) -> typing.Any:
    "krank,iu,iv,is,w,ier = iddp_rsvd(eps,m,n,matvect,matvec,[p1t,p2t,p3t,p4t,p1,p2,p3,p4,matvect_extra_args,matvec_extra_args])\n\nWrapper for ``iddp_rsvd``.\n\nParameters\n----------\neps : input float\nm : input int\nn : input int\nmatvect : call-back function\nmatvec : call-back function\n\nOther Parameters\n----------------\nmatvect_extra_args : input tuple, optional\n    Default: ()\np1t : input float\np2t : input float\np3t : input float\np4t : input float\nmatvec_extra_args : input tuple, optional\n    Default: ()\np1 : input float\np2 : input float\np3 : input float\np4 : input float\n\nReturns\n-------\nkrank : int\niu : int\niv : int\nis : int\nw : rank-1 array('d') with bounds ((min(m,n)+1)*(3*m+5*n+1)+25*pow(min(m,n),2))\nier : int\n\nNotes\n-----\nCall-back functions::\n\n  def matvect(x,[m,n,p1,p2,p3,p4]): return y\n  Required arguments:\n    x : input rank-1 array('d') with bounds (m)\n  Optional arguments:\n    m : input int, optional\n    Default: len(x)\n    n : input int\n    p1 : input float\n    p2 : input float\n    p3 : input float\n    p4 : input float\n  Return objects:\n    y : rank-1 array('d') with bounds (n)\n  def matvec(x,[n,m,p1,p2,p3,p4]): return y\n  Required arguments:\n    x : input rank-1 array('d') with bounds (n)\n  Optional arguments:\n    n : input int, optional\n    Default: len(x)\n    m : input int\n    p1 : input float\n    p2 : input float\n    p3 : input float\n    p4 : input float\n  Return objects:\n    y : rank-1 array('d') with bounds (m)\n"
    ...

def iddp_svd(eps, a, m=..., n=...) -> typing.Any:
    "krank,iu,iv,is,w,ier = iddp_svd(eps,a,[m,n])\n\nWrapper for ``iddp_svd``.\n\nParameters\n----------\neps : input float\na : input rank-2 array('d') with bounds (m,n)\n\nOther Parameters\n----------------\nm : input int, optional\n    Default: shape(a,0)\nn : input int, optional\n    Default: shape(a,1)\n\nReturns\n-------\nkrank : int\niu : int\niv : int\nis : int\nw : rank-1 array('d') with bounds ((min(m,n)+1)*(m+2*n+9)+8*min(m,n)+15*pow(min(m,n),2))\nier : int\n"
    ...

def iddr_aid(a, krank, w, m=..., n=...) -> typing.Any:
    "list,proj = iddr_aid(a,krank,w,[m,n])\n\nWrapper for ``iddr_aid``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (m,n)\nkrank : input int\nw : input rank-1 array('d') with bounds ((2*krank+17)*n+27*m+100)\n\nOther Parameters\n----------------\nm : input int, optional\n    Default: shape(a,0)\nn : input int, optional\n    Default: shape(a,1)\n\nReturns\n-------\nlist : rank-1 array('i') with bounds (n)\nproj : rank-1 array('d') with bounds (max(krank*(n-krank),1))\n"
    ...

def iddr_aidi(m, n, krank) -> typing.Any:
    "w = iddr_aidi(m,n,krank)\n\nWrapper for ``iddr_aidi``.\n\nParameters\n----------\nm : input int\nn : input int\nkrank : input int\n\nReturns\n-------\nw : rank-1 array('d') with bounds ((2*krank+17)*n+27*m+100)\n"
    ...

def iddr_asvd(a, krank, w, m=..., n=...) -> typing.Any:
    "u,v,s,ier = iddr_asvd(a,krank,w,[m,n])\n\nWrapper for ``iddr_asvd``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (m,n)\nkrank : input int\nw : input rank-1 array('d') with bounds ((2*krank+28)*m+(6*krank+21)*n+25*pow(krank,2)+100)\n\nOther Parameters\n----------------\nm : input int, optional\n    Default: shape(a,0)\nn : input int, optional\n    Default: shape(a,1)\n\nReturns\n-------\nu : rank-2 array('d') with bounds (m,krank)\nv : rank-2 array('d') with bounds (n,krank)\ns : rank-1 array('d') with bounds (krank)\nier : int\n"
    ...

def iddr_id(a, krank, m=..., n=...) -> typing.Any:
    "list,rnorms = iddr_id(a,krank,[m,n])\n\nWrapper for ``iddr_id``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (m,n)\nkrank : input int\n\nOther Parameters\n----------------\nm : input int, optional\n    Default: shape(a,0)\nn : input int, optional\n    Default: shape(a,1)\n\nReturns\n-------\nlist : rank-1 array('i') with bounds (n)\nrnorms : rank-1 array('d') with bounds (n)\n"
    ...

def iddr_rid(m, n, matvect, krank, p1=..., p2=..., p3=..., p4=..., matvect_extra_args=...) -> typing.Any:
    "list,proj = iddr_rid(m,n,matvect,krank,[p1,p2,p3,p4,matvect_extra_args])\n\nWrapper for ``iddr_rid``.\n\nParameters\n----------\nm : input int\nn : input int\nmatvect : call-back function\nkrank : input int\n\nOther Parameters\n----------------\nmatvect_extra_args : input tuple, optional\n    Default: ()\np1 : input float\np2 : input float\np3 : input float\np4 : input float\n\nReturns\n-------\nlist : rank-1 array('i') with bounds (n)\nproj : rank-1 array('d') with bounds (m+(krank+3)*n)\n\nNotes\n-----\nCall-back functions::\n\n  def matvect(x,[m,n,p1,p2,p3,p4]): return y\n  Required arguments:\n    x : input rank-1 array('d') with bounds (m)\n  Optional arguments:\n    m : input int, optional\n    Default: len(x)\n    n : input int\n    p1 : input float\n    p2 : input float\n    p3 : input float\n    p4 : input float\n  Return objects:\n    y : rank-1 array('d') with bounds (n)\n"
    ...

def iddr_rsvd(m, n, matvect, matvec, krank, p1t=..., p2t=..., p3t=..., p4t=..., p1=..., p2=..., p3=..., p4=..., w=..., matvect_extra_args=..., matvec_extra_args=...) -> typing.Any:
    "u,v,s,ier = iddr_rsvd(m,n,matvect,matvec,krank,[p1t,p2t,p3t,p4t,p1,p2,p3,p4,w,matvect_extra_args,matvec_extra_args])\n\nWrapper for ``iddr_rsvd``.\n\nParameters\n----------\nm : input int\nn : input int\nmatvect : call-back function\nmatvec : call-back function\nkrank : input int\n\nOther Parameters\n----------------\nmatvect_extra_args : input tuple, optional\n    Default: ()\np1t : input float\np2t : input float\np3t : input float\np4t : input float\nmatvec_extra_args : input tuple, optional\n    Default: ()\np1 : input float\np2 : input float\np3 : input float\np4 : input float\nw : input rank-1 array('d') with bounds ((krank+1)*(2*m+4*n)+25*pow(krank,2))\n\nReturns\n-------\nu : rank-2 array('d') with bounds (m,krank)\nv : rank-2 array('d') with bounds (n,krank)\ns : rank-1 array('d') with bounds (krank)\nier : int\n\nNotes\n-----\nCall-back functions::\n\n  def matvect(x,[m,n,p1,p2,p3,p4]): return y\n  Required arguments:\n    x : input rank-1 array('d') with bounds (m)\n  Optional arguments:\n    m : input int, optional\n    Default: len(x)\n    n : input int\n    p1 : input float\n    p2 : input float\n    p3 : input float\n    p4 : input float\n  Return objects:\n    y : rank-1 array('d') with bounds (n)\n  def matvec(x,[n,m,p1,p2,p3,p4]): return y\n  Required arguments:\n    x : input rank-1 array('d') with bounds (n)\n  Optional arguments:\n    n : input int, optional\n    Default: len(x)\n    m : input int\n    p1 : input float\n    p2 : input float\n    p3 : input float\n    p4 : input float\n  Return objects:\n    y : rank-1 array('d') with bounds (m)\n"
    ...

def iddr_svd(a, krank, m=..., n=..., r=...) -> typing.Any:
    "u,v,s,ier = iddr_svd(a,krank,[m,n,r])\n\nWrapper for ``iddr_svd``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (m,n)\nkrank : input int\n\nOther Parameters\n----------------\nm : input int, optional\n    Default: shape(a,0)\nn : input int, optional\n    Default: shape(a,1)\nr : input rank-1 array('d') with bounds ((krank+2)*n+8*min(m,n)+15*pow(krank,2)+8*krank)\n\nReturns\n-------\nu : rank-2 array('d') with bounds (m,krank)\nv : rank-2 array('d') with bounds (n,krank)\ns : rank-1 array('d') with bounds (krank)\nier : int\n"
    ...

def idz_copycols(a, krank, list, m=..., n=...) -> typing.Any:
    "col = idz_copycols(a,krank,list,[m,n])\n\nWrapper for ``idz_copycols``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (m,n)\nkrank : input int\nlist : input rank-1 array('i') with bounds (*)\n\nOther Parameters\n----------------\nm : input int, optional\n    Default: shape(a,0)\nn : input int, optional\n    Default: shape(a,1)\n\nReturns\n-------\ncol : rank-2 array('D') with bounds (m,krank)\n"
    ...

def idz_diffsnorm(m, n, matveca, matveca2, matvec, matvec2, its, p1a=..., p2a=..., p3a=..., p4a=..., p1a2=..., p2a2=..., p3a2=..., p4a2=..., p1=..., p2=..., p3=..., p4=..., p12=..., p22=..., p32=..., p42=..., w=..., matveca_extra_args=..., matveca2_extra_args=..., matvec_extra_args=..., matvec2_extra_args=...) -> typing.Any:
    "snorm = idz_diffsnorm(m,n,matveca,matveca2,matvec,matvec2,its,[p1a,p2a,p3a,p4a,p1a2,p2a2,p3a2,p4a2,p1,p2,p3,p4,p12,p22,p32,p42,w,matveca_extra_args,matveca2_extra_args,matvec_extra_args,matvec2_extra_args])\n\nWrapper for ``idz_diffsnorm``.\n\nParameters\n----------\nm : input int\nn : input int\nmatveca : call-back function\nmatveca2 : call-back function\nmatvec : call-back function\nmatvec2 : call-back function\nits : input int\n\nOther Parameters\n----------------\nmatveca_extra_args : input tuple, optional\n    Default: ()\np1a : input complex\np2a : input complex\np3a : input complex\np4a : input complex\nmatveca2_extra_args : input tuple, optional\n    Default: ()\np1a2 : input complex\np2a2 : input complex\np3a2 : input complex\np4a2 : input complex\nmatvec_extra_args : input tuple, optional\n    Default: ()\np1 : input complex\np2 : input complex\np3 : input complex\np4 : input complex\nmatvec2_extra_args : input tuple, optional\n    Default: ()\np12 : input complex\np22 : input complex\np32 : input complex\np42 : input complex\nw : input rank-1 array('D') with bounds (3*(m+n))\n\nReturns\n-------\nsnorm : float\n\nNotes\n-----\nCall-back functions::\n\n  def matveca(x,[m,n,p1,p2,p3,p4]): return y\n  Required arguments:\n    x : input rank-1 array('D') with bounds (m)\n  Optional arguments:\n    m : input int, optional\n    Default: len(x)\n    n : input int\n    p1 : input complex\n    p2 : input complex\n    p3 : input complex\n    p4 : input complex\n  Return objects:\n    y : rank-1 array('D') with bounds (n)\n  def matveca2(x,[m,n,p1,p2,p3,p4]): return y\n  Required arguments:\n    x : input rank-1 array('D') with bounds (m)\n  Optional arguments:\n    m : input int, optional\n    Default: len(x)\n    n : input int\n    p1 : input complex\n    p2 : input complex\n    p3 : input complex\n    p4 : input complex\n  Return objects:\n    y : rank-1 array('D') with bounds (n)\n  def matvec(x,[n,m,p1,p2,p3,p4]): return y\n  Required arguments:\n    x : input rank-1 array('D') with bounds (n)\n  Optional arguments:\n    n : input int, optional\n    Default: len(x)\n    m : input int\n    p1 : input complex\n    p2 : input complex\n    p3 : input complex\n    p4 : input complex\n  Return objects:\n    y : rank-1 array('D') with bounds (m)\n  def matvec2(x,[n,m,p1,p2,p3,p4]): return y\n  Required arguments:\n    x : input rank-1 array('D') with bounds (n)\n  Optional arguments:\n    n : input int, optional\n    Default: len(x)\n    m : input int\n    p1 : input complex\n    p2 : input complex\n    p3 : input complex\n    p4 : input complex\n  Return objects:\n    y : rank-1 array('D') with bounds (m)\n"
    ...

def idz_estrank(eps, a, w, ra, m=..., n=...) -> typing.Any:
    "krank,ra = idz_estrank(eps,a,w,ra,[m,n])\n\nWrapper for ``idz_estrank``.\n\nParameters\n----------\neps : input float\na : input rank-2 array('D') with bounds (m,n)\nw : input rank-1 array('D') with bounds (17 * m + 70)\nra : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\nm : input int, optional\n    Default: shape(a,0)\nn : input int, optional\n    Default: shape(a,1)\n\nReturns\n-------\nkrank : int\nra : rank-1 array('D') with bounds (*)\n"
    ...

def idz_findrank(eps, m, n, matveca, p1=..., p2=..., p3=..., p4=..., w=..., matveca_extra_args=...) -> typing.Any:
    "krank,ra,ier = idz_findrank(eps,m,n,matveca,[p1,p2,p3,p4,w,matveca_extra_args])\n\nWrapper for ``idz_findrank``.\n\nParameters\n----------\neps : input float\nm : input int\nn : input int\nmatveca : call-back function\n\nOther Parameters\n----------------\nmatveca_extra_args : input tuple, optional\n    Default: ()\np1 : input complex\np2 : input complex\np3 : input complex\np4 : input complex\nw : input rank-1 array('D') with bounds (m+2*n+1)\n\nReturns\n-------\nkrank : int\nra : rank-1 array('D') with bounds (2*n*min(m,n))\nier : int\n\nNotes\n-----\nCall-back functions::\n\n  def matveca(x,[m,n,p1,p2,p3,p4]): return y\n  Required arguments:\n    x : input rank-1 array('D') with bounds (m)\n  Optional arguments:\n    m : input int, optional\n    Default: len(x)\n    n : input int\n    p1 : input complex\n    p2 : input complex\n    p3 : input complex\n    p4 : input complex\n  Return objects:\n    y : rank-1 array('D') with bounds (n)\n"
    ...

def idz_frm(n, w, x, m=...) -> typing.Any:
    "y = idz_frm(n,w,x,[m])\n\nWrapper for ``idz_frm``.\n\nParameters\n----------\nn : input int\nw : input rank-1 array('D') with bounds (17 * m + 70)\nx : input rank-1 array('D') with bounds (m)\n\nOther Parameters\n----------------\nm : input int, optional\n    Default: len(x)\n\nReturns\n-------\ny : rank-1 array('D') with bounds (n)\n"
    ...

def idz_frmi(m) -> typing.Any:
    "n,w = idz_frmi(m)\n\nWrapper for ``idz_frmi``.\n\nParameters\n----------\nm : input int\n\nReturns\n-------\nn : int\nw : rank-1 array('D') with bounds (17 * m + 70)\n"
    ...

def idz_id2svd(b, list, proj, m=..., krank=..., n=..., w=...) -> typing.Any:
    "u,v,s,ier = idz_id2svd(b,list,proj,[m,krank,n,w])\n\nWrapper for ``idz_id2svd``.\n\nParameters\n----------\nb : input rank-2 array('D') with bounds (m,krank)\nlist : input rank-1 array('i') with bounds (n)\nproj : input rank-2 array('D') with bounds (krank,n-krank)\n\nOther Parameters\n----------------\nm : input int, optional\n    Default: shape(b,0)\nkrank : input int, optional\n    Default: shape(b,1)\nn : input int, optional\n    Default: len(list)\nw : input rank-1 array('D') with bounds ((krank+1)*(m+3*n+10)+9*pow(krank,2))\n\nReturns\n-------\nu : rank-2 array('D') with bounds (m,krank)\nv : rank-2 array('D') with bounds (n,krank)\ns : rank-1 array('d') with bounds (krank)\nier : int\n"
    ...

def idz_reconid(col, list, proj, m=..., krank=..., n=...) -> typing.Any:
    "approx = idz_reconid(col,list,proj,[m,krank,n])\n\nWrapper for ``idz_reconid``.\n\nParameters\n----------\ncol : input rank-2 array('D') with bounds (m,krank)\nlist : input rank-1 array('i') with bounds (n)\nproj : input rank-2 array('D') with bounds (krank,n-krank)\n\nOther Parameters\n----------------\nm : input int, optional\n    Default: shape(col,0)\nkrank : input int, optional\n    Default: shape(col,1)\nn : input int, optional\n    Default: len(list)\n\nReturns\n-------\napprox : rank-2 array('D') with bounds (m,n)\n"
    ...

def idz_reconint(list, proj, n=..., krank=...) -> typing.Any:
    "p = idz_reconint(list,proj,[n,krank])\n\nWrapper for ``idz_reconint``.\n\nParameters\n----------\nlist : input rank-1 array('i') with bounds (n)\nproj : input rank-2 array('D') with bounds (krank,n-krank)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: len(list)\nkrank : input int, optional\n    Default: shape(proj,0)\n\nReturns\n-------\np : rank-2 array('D') with bounds (krank,n)\n"
    ...

def idz_sfrm(l, n, w, x, m=...) -> typing.Any:
    "y = idz_sfrm(l,n,w,x,[m])\n\nWrapper for ``idz_sfrm``.\n\nParameters\n----------\nl : input int\nn : input int\nw : input rank-1 array('D') with bounds (27 * m + 90)\nx : input rank-1 array('D') with bounds (m)\n\nOther Parameters\n----------------\nm : input int, optional\n    Default: len(x)\n\nReturns\n-------\ny : rank-1 array('D') with bounds (l)\n"
    ...

def idz_sfrmi(l, m) -> typing.Any:
    "n,w = idz_sfrmi(l,m)\n\nWrapper for ``idz_sfrmi``.\n\nParameters\n----------\nl : input int\nm : input int\n\nReturns\n-------\nn : int\nw : rank-1 array('D') with bounds (27 * m + 90)\n"
    ...

def idz_snorm(m, n, matveca, matvec, its, p1a=..., p2a=..., p3a=..., p4a=..., p1=..., p2=..., p3=..., p4=..., u=..., matveca_extra_args=..., matvec_extra_args=...) -> typing.Any:
    "snorm,v = idz_snorm(m,n,matveca,matvec,its,[p1a,p2a,p3a,p4a,p1,p2,p3,p4,u,matveca_extra_args,matvec_extra_args])\n\nWrapper for ``idz_snorm``.\n\nParameters\n----------\nm : input int\nn : input int\nmatveca : call-back function\nmatvec : call-back function\nits : input int\n\nOther Parameters\n----------------\nmatveca_extra_args : input tuple, optional\n    Default: ()\np1a : input complex\np2a : input complex\np3a : input complex\np4a : input complex\nmatvec_extra_args : input tuple, optional\n    Default: ()\np1 : input complex\np2 : input complex\np3 : input complex\np4 : input complex\nu : input rank-1 array('D') with bounds (m)\n\nReturns\n-------\nsnorm : float\nv : rank-1 array('D') with bounds (n)\n\nNotes\n-----\nCall-back functions::\n\n  def matveca(x,[m,n,p1,p2,p3,p4]): return y\n  Required arguments:\n    x : input rank-1 array('D') with bounds (m)\n  Optional arguments:\n    m : input int, optional\n    Default: len(x)\n    n : input int\n    p1 : input complex\n    p2 : input complex\n    p3 : input complex\n    p4 : input complex\n  Return objects:\n    y : rank-1 array('D') with bounds (n)\n  def matvec(x,[n,m,p1,p2,p3,p4]): return y\n  Required arguments:\n    x : input rank-1 array('D') with bounds (n)\n  Optional arguments:\n    n : input int, optional\n    Default: len(x)\n    m : input int\n    p1 : input complex\n    p2 : input complex\n    p3 : input complex\n    p4 : input complex\n  Return objects:\n    y : rank-1 array('D') with bounds (m)\n"
    ...

def idzp_aid(eps, a, work, proj, m=..., n=...) -> typing.Any:
    "krank,list,proj = idzp_aid(eps,a,work,proj,[m,n])\n\nWrapper for ``idzp_aid``.\n\nParameters\n----------\neps : input float\na : input rank-2 array('D') with bounds (m,n)\nwork : input rank-1 array('D') with bounds (17 * m + 70)\nproj : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\nm : input int, optional\n    Default: shape(a,0)\nn : input int, optional\n    Default: shape(a,1)\n\nReturns\n-------\nkrank : int\nlist : rank-1 array('i') with bounds (n)\nproj : rank-1 array('D') with bounds (*)\n"
    ...

def idzp_asvd(eps, a, winit, w, m=..., n=...) -> typing.Any:
    "krank,iu,iv,is,w,ier = idzp_asvd(eps,a,winit,w,[m,n])\n\nWrapper for ``idzp_asvd``.\n\nParameters\n----------\neps : input float\na : input rank-2 array('D') with bounds (m,n)\nwinit : input rank-1 array('D') with bounds (17 * m + 70)\nw : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\nm : input int, optional\n    Default: shape(a,0)\nn : input int, optional\n    Default: shape(a,1)\n\nReturns\n-------\nkrank : int\niu : int\niv : int\nis : int\nw : rank-1 array('D') with bounds (*)\nier : int\n"
    ...

def idzp_id(eps, a, m=..., n=...) -> typing.Any:
    "krank,list,rnorms = idzp_id(eps,a,[m,n])\n\nWrapper for ``idzp_id``.\n\nParameters\n----------\neps : input float\na : input rank-2 array('D') with bounds (m,n)\n\nOther Parameters\n----------------\nm : input int, optional\n    Default: shape(a,0)\nn : input int, optional\n    Default: shape(a,1)\n\nReturns\n-------\nkrank : int\nlist : rank-1 array('i') with bounds (n)\nrnorms : rank-1 array('d') with bounds (n)\n"
    ...

def idzp_rid(eps, m, n, matveca, proj, p1=..., p2=..., p3=..., p4=..., matveca_extra_args=...) -> typing.Any:
    "krank,list,proj,ier = idzp_rid(eps,m,n,matveca,proj,[p1,p2,p3,p4,matveca_extra_args])\n\nWrapper for ``idzp_rid``.\n\nParameters\n----------\neps : input float\nm : input int\nn : input int\nmatveca : call-back function\nproj : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\nmatveca_extra_args : input tuple, optional\n    Default: ()\np1 : input complex\np2 : input complex\np3 : input complex\np4 : input complex\n\nReturns\n-------\nkrank : int\nlist : rank-1 array('i') with bounds (n)\nproj : rank-1 array('D') with bounds (*)\nier : int\n\nNotes\n-----\nCall-back functions::\n\n  def matveca(x,[m,n,p1,p2,p3,p4]): return y\n  Required arguments:\n    x : input rank-1 array('D') with bounds (m)\n  Optional arguments:\n    m : input int, optional\n    Default: len(x)\n    n : input int\n    p1 : input complex\n    p2 : input complex\n    p3 : input complex\n    p4 : input complex\n  Return objects:\n    y : rank-1 array('D') with bounds (n)\n"
    ...

def idzp_rsvd(eps, m, n, matveca, matvec, p1a=..., p2a=..., p3a=..., p4a=..., p1=..., p2=..., p3=..., p4=..., matveca_extra_args=..., matvec_extra_args=...) -> typing.Any:
    "krank,iu,iv,is,w,ier = idzp_rsvd(eps,m,n,matveca,matvec,[p1a,p2a,p3a,p4a,p1,p2,p3,p4,matveca_extra_args,matvec_extra_args])\n\nWrapper for ``idzp_rsvd``.\n\nParameters\n----------\neps : input float\nm : input int\nn : input int\nmatveca : call-back function\nmatvec : call-back function\n\nOther Parameters\n----------------\nmatveca_extra_args : input tuple, optional\n    Default: ()\np1a : input complex\np2a : input complex\np3a : input complex\np4a : input complex\nmatvec_extra_args : input tuple, optional\n    Default: ()\np1 : input complex\np2 : input complex\np3 : input complex\np4 : input complex\n\nReturns\n-------\nkrank : int\niu : int\niv : int\nis : int\nw : rank-1 array('D') with bounds ((min(m,n)+1)*(3*m+5*n+11)+8*pow(min(m,n),2))\nier : int\n\nNotes\n-----\nCall-back functions::\n\n  def matveca(x,[m,n,p1,p2,p3,p4]): return y\n  Required arguments:\n    x : input rank-1 array('D') with bounds (m)\n  Optional arguments:\n    m : input int, optional\n    Default: len(x)\n    n : input int\n    p1 : input complex\n    p2 : input complex\n    p3 : input complex\n    p4 : input complex\n  Return objects:\n    y : rank-1 array('D') with bounds (n)\n  def matvec(x,[n,m,p1,p2,p3,p4]): return y\n  Required arguments:\n    x : input rank-1 array('D') with bounds (n)\n  Optional arguments:\n    n : input int, optional\n    Default: len(x)\n    m : input int\n    p1 : input complex\n    p2 : input complex\n    p3 : input complex\n    p4 : input complex\n  Return objects:\n    y : rank-1 array('D') with bounds (m)\n"
    ...

def idzp_svd(eps, a, m=..., n=...) -> typing.Any:
    "krank,iu,iv,is,w,ier = idzp_svd(eps,a,[m,n])\n\nWrapper for ``idzp_svd``.\n\nParameters\n----------\neps : input float\na : input rank-2 array('D') with bounds (m,n)\n\nOther Parameters\n----------------\nm : input int, optional\n    Default: shape(a,0)\nn : input int, optional\n    Default: shape(a,1)\n\nReturns\n-------\nkrank : int\niu : int\niv : int\nis : int\nw : rank-1 array('D') with bounds ((min(m,n)+1)*(m+2*n+9)+8*min(m,n)+6*pow(min(m,n),2))\nier : int\n"
    ...

def idzr_aid(a, krank, w, m=..., n=...) -> typing.Any:
    "list,proj = idzr_aid(a,krank,w,[m,n])\n\nWrapper for ``idzr_aid``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (m,n)\nkrank : input int\nw : input rank-1 array('D') with bounds ((2*krank+17)*n+21*m+80)\n\nOther Parameters\n----------------\nm : input int, optional\n    Default: shape(a,0)\nn : input int, optional\n    Default: shape(a,1)\n\nReturns\n-------\nlist : rank-1 array('i') with bounds (n)\nproj : rank-1 array('D') with bounds (max(krank*(n-krank),1))\n"
    ...

def idzr_aidi(m, n, krank) -> typing.Any:
    "w = idzr_aidi(m,n,krank)\n\nWrapper for ``idzr_aidi``.\n\nParameters\n----------\nm : input int\nn : input int\nkrank : input int\n\nReturns\n-------\nw : rank-1 array('D') with bounds ((2*krank+17)*n+21*m+80)\n"
    ...

def idzr_asvd(a, krank, w, m=..., n=...) -> typing.Any:
    "u,v,s,ier = idzr_asvd(a,krank,w,[m,n])\n\nWrapper for ``idzr_asvd``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (m,n)\nkrank : input int\nw : input rank-1 array('D') with bounds ((2*krank+22)*m+(6*krank+21)*n+8*pow(krank,2)+10*krank+90)\n\nOther Parameters\n----------------\nm : input int, optional\n    Default: shape(a,0)\nn : input int, optional\n    Default: shape(a,1)\n\nReturns\n-------\nu : rank-2 array('D') with bounds (m,krank)\nv : rank-2 array('D') with bounds (n,krank)\ns : rank-1 array('d') with bounds (krank)\nier : int\n"
    ...

def idzr_id(a, krank, m=..., n=...) -> typing.Any:
    "list,rnorms = idzr_id(a,krank,[m,n])\n\nWrapper for ``idzr_id``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (m,n)\nkrank : input int\n\nOther Parameters\n----------------\nm : input int, optional\n    Default: shape(a,0)\nn : input int, optional\n    Default: shape(a,1)\n\nReturns\n-------\nlist : rank-1 array('i') with bounds (n)\nrnorms : rank-1 array('d') with bounds (n)\n"
    ...

def idzr_rid(m, n, matveca, krank, p1=..., p2=..., p3=..., p4=..., matveca_extra_args=...) -> typing.Any:
    "list,proj = idzr_rid(m,n,matveca,krank,[p1,p2,p3,p4,matveca_extra_args])\n\nWrapper for ``idzr_rid``.\n\nParameters\n----------\nm : input int\nn : input int\nmatveca : call-back function\nkrank : input int\n\nOther Parameters\n----------------\nmatveca_extra_args : input tuple, optional\n    Default: ()\np1 : input complex\np2 : input complex\np3 : input complex\np4 : input complex\n\nReturns\n-------\nlist : rank-1 array('i') with bounds (n)\nproj : rank-1 array('D') with bounds (m+(krank+3)*n)\n\nNotes\n-----\nCall-back functions::\n\n  def matveca(x,[m,n,p1,p2,p3,p4]): return y\n  Required arguments:\n    x : input rank-1 array('D') with bounds (m)\n  Optional arguments:\n    m : input int, optional\n    Default: len(x)\n    n : input int\n    p1 : input complex\n    p2 : input complex\n    p3 : input complex\n    p4 : input complex\n  Return objects:\n    y : rank-1 array('D') with bounds (n)\n"
    ...

def idzr_rsvd(m, n, matveca, matvec, krank, p1a=..., p2a=..., p3a=..., p4a=..., p1=..., p2=..., p3=..., p4=..., w=..., matveca_extra_args=..., matvec_extra_args=...) -> typing.Any:
    "u,v,s,ier = idzr_rsvd(m,n,matveca,matvec,krank,[p1a,p2a,p3a,p4a,p1,p2,p3,p4,w,matveca_extra_args,matvec_extra_args])\n\nWrapper for ``idzr_rsvd``.\n\nParameters\n----------\nm : input int\nn : input int\nmatveca : call-back function\nmatvec : call-back function\nkrank : input int\n\nOther Parameters\n----------------\nmatveca_extra_args : input tuple, optional\n    Default: ()\np1a : input complex\np2a : input complex\np3a : input complex\np4a : input complex\nmatvec_extra_args : input tuple, optional\n    Default: ()\np1 : input complex\np2 : input complex\np3 : input complex\np4 : input complex\nw : input rank-1 array('D') with bounds ((krank+1)*(2*m+4*n+10)+8*pow(krank,2))\n\nReturns\n-------\nu : rank-2 array('D') with bounds (m,krank)\nv : rank-2 array('D') with bounds (n,krank)\ns : rank-1 array('d') with bounds (krank)\nier : int\n\nNotes\n-----\nCall-back functions::\n\n  def matveca(x,[m,n,p1,p2,p3,p4]): return y\n  Required arguments:\n    x : input rank-1 array('D') with bounds (m)\n  Optional arguments:\n    m : input int, optional\n    Default: len(x)\n    n : input int\n    p1 : input complex\n    p2 : input complex\n    p3 : input complex\n    p4 : input complex\n  Return objects:\n    y : rank-1 array('D') with bounds (n)\n  def matvec(x,[n,m,p1,p2,p3,p4]): return y\n  Required arguments:\n    x : input rank-1 array('D') with bounds (n)\n  Optional arguments:\n    n : input int, optional\n    Default: len(x)\n    m : input int\n    p1 : input complex\n    p2 : input complex\n    p3 : input complex\n    p4 : input complex\n  Return objects:\n    y : rank-1 array('D') with bounds (m)\n"
    ...

def idzr_svd(a, krank, m=..., n=..., r=...) -> typing.Any:
    "u,v,s,ier = idzr_svd(a,krank,[m,n,r])\n\nWrapper for ``idzr_svd``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (m,n)\nkrank : input int\n\nOther Parameters\n----------------\nm : input int, optional\n    Default: shape(a,0)\nn : input int, optional\n    Default: shape(a,1)\nr : input rank-1 array('D') with bounds ((krank+2)*n+8*min(m,n)+6*pow(krank,2)+8*krank)\n\nReturns\n-------\nu : rank-2 array('D') with bounds (m,krank)\nv : rank-2 array('D') with bounds (n,krank)\ns : rank-1 array('d') with bounds (krank)\nier : int\n"
    ...

def __getattr__(name) -> typing.Any:
    ...

