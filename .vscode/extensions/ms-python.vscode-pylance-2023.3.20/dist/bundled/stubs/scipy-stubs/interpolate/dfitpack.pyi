# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: scipy, version: 1.6.2
# Module: scipy.interpolate.dfitpack, version: $Revision: $
import typing
import builtins as _mod_builtins

__doc__: str
__file__: str
__name__: str
__package__: str
__version__: bytes
def bispeu(tx, ty, c, kx, ky, x, y) -> typing.Any:
    "z,ier = bispeu(tx,ty,c,kx,ky,x,y)\n\nWrapper for ``bispeu``.\n\nParameters\n----------\ntx : input rank-1 array('d') with bounds (nx)\nty : input rank-1 array('d') with bounds (ny)\nc : input rank-1 array('d') with bounds ((nx-kx-1)*(ny-ky-1))\nkx : input int\nky : input int\nx : input rank-1 array('d') with bounds (m)\ny : input rank-1 array('d') with bounds (m)\n\nReturns\n-------\nz : rank-1 array('d') with bounds (m)\nier : int\n"
    ...

def bispev(tx, ty, c, kx, ky, x, y) -> typing.Any:
    "z,ier = bispev(tx,ty,c,kx,ky,x,y)\n\nWrapper for ``bispev``.\n\nParameters\n----------\ntx : input rank-1 array('d') with bounds (nx)\nty : input rank-1 array('d') with bounds (ny)\nc : input rank-1 array('d') with bounds ((nx-kx-1)*(ny-ky-1))\nkx : input int\nky : input int\nx : input rank-1 array('d') with bounds (mx)\ny : input rank-1 array('d') with bounds (my)\n\nReturns\n-------\nz : rank-2 array('d') with bounds (mx,my)\nier : int\n"
    ...

def curfit(iopt, x, y, w, t, wrk, iwrk, xb=..., xe=..., k=..., s=...) -> typing.Any:
    "n,c,fp,ier = curfit(iopt,x,y,w,t,wrk,iwrk,[xb,xe,k,s])\n\nWrapper for ``curfit``.\n\nParameters\n----------\niopt : input int\nx : input rank-1 array('d') with bounds (m)\ny : input rank-1 array('d') with bounds (m)\nw : input rank-1 array('d') with bounds (m)\nt : in/output rank-1 array('d') with bounds (nest)\nwrk : in/output rank-1 array('d') with bounds (lwrk)\niwrk : in/output rank-1 array('i') with bounds (nest)\n\nOther Parameters\n----------------\nxb : input float, optional\n    Default: x[0]\nxe : input float, optional\n    Default: x[m-1]\nk : input int, optional\n    Default: 3\ns : input float, optional\n    Default: 0.0\n\nReturns\n-------\nn : int\nc : rank-1 array('d') with bounds (n)\nfp : float\nier : int\n"
    ...

def dblint(tx, ty, c, kx, ky, xb, xe, yb, ye) -> typing.Any:
    "dblint = dblint(tx,ty,c,kx,ky,xb,xe,yb,ye)\n\nWrapper for ``dblint``.\n\nParameters\n----------\ntx : input rank-1 array('d') with bounds (nx)\nty : input rank-1 array('d') with bounds (ny)\nc : input rank-1 array('d') with bounds ((nx-kx-1)*(ny-ky-1))\nkx : input int\nky : input int\nxb : input float\nxe : input float\nyb : input float\nye : input float\n\nReturns\n-------\ndblint : float\n"
    ...

def fpchec(x, t, k) -> typing.Any:
    "ier = fpchec(x,t,k)\n\nWrapper for ``fpchec``.\n\nParameters\n----------\nx : input rank-1 array('d') with bounds (m)\nt : input rank-1 array('d') with bounds (n)\nk : input int\n\nReturns\n-------\nier : int\n"
    ...

def fpcurf0(x, y, k, w=..., xb=..., xe=..., s=..., nest=...) -> typing.Any:
    "x,y,w,xb,xe,k,s,n,t,c,fp,fpint,nrdata,ier = fpcurf0(x,y,k,[w,xb,xe,s,nest])\n\nWrapper for ``fpcurf0``.\n\nParameters\n----------\nx : input rank-1 array('d') with bounds (m)\ny : input rank-1 array('d') with bounds (m)\nk : input int\n\nOther Parameters\n----------------\nw : input rank-1 array('d') with bounds (m), optional\n    Default: 1.0\nxb : input float, optional\n    Default: x[0]\nxe : input float, optional\n    Default: x[m-1]\ns : input float, optional\n    Default: m\nnest : input int, optional\n    Default: (s==0.0?m+k+1:MAX(m/2,2*k1))\n\nReturns\n-------\nx : rank-1 array('d') with bounds (m)\ny : rank-1 array('d') with bounds (m)\nw : rank-1 array('d') with bounds (m)\nxb : float\nxe : float\nk : int\ns : float\nn : int\nt : rank-1 array('d') with bounds (nest)\nc : rank-1 array('d') with bounds (nest)\nfp : float\nfpint : rank-1 array('d') with bounds (nest)\nnrdata : rank-1 array('i') with bounds (nest)\nier : int\n"
    ...

def fpcurf1(x, y, w, xb, xe, k, s, n, t, c, fp, fpint, nrdata, ier, overwrite_x=..., overwrite_y=..., overwrite_w=..., overwrite_t=..., overwrite_c=..., overwrite_fpint=..., overwrite_nrdata=...) -> typing.Any:
    "x,y,w,xb,xe,k,s,n,t,c,fp,fpint,nrdata,ier = fpcurf1(x,y,w,xb,xe,k,s,n,t,c,fp,fpint,nrdata,ier,[overwrite_x,overwrite_y,overwrite_w,overwrite_t,overwrite_c,overwrite_fpint,overwrite_nrdata])\n\nWrapper for ``fpcurf1``.\n\nParameters\n----------\nx : input rank-1 array('d') with bounds (m)\ny : input rank-1 array('d') with bounds (m)\nw : input rank-1 array('d') with bounds (m)\nxb : input float\nxe : input float\nk : input int\ns : input float\nn : input int\nt : input rank-1 array('d') with bounds (nest)\nc : input rank-1 array('d') with bounds (nest)\nfp : input float\nfpint : input rank-1 array('d') with bounds (nest)\nnrdata : input rank-1 array('i') with bounds (nest)\nier : input int\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 1\noverwrite_y : input int, optional\n    Default: 1\noverwrite_w : input int, optional\n    Default: 1\noverwrite_t : input int, optional\n    Default: 1\noverwrite_c : input int, optional\n    Default: 1\noverwrite_fpint : input int, optional\n    Default: 1\noverwrite_nrdata : input int, optional\n    Default: 1\n\nReturns\n-------\nx : rank-1 array('d') with bounds (m)\ny : rank-1 array('d') with bounds (m)\nw : rank-1 array('d') with bounds (m)\nxb : float\nxe : float\nk : int\ns : float\nn : int\nt : rank-1 array('d') with bounds (nest)\nc : rank-1 array('d') with bounds (nest)\nfp : float\nfpint : rank-1 array('d') with bounds (nest)\nnrdata : rank-1 array('i') with bounds (nest)\nier : int\n"
    ...

def fpcurfm1(x, y, k, t, w=..., xb=..., xe=..., overwrite_t=...) -> typing.Any:
    "x,y,w,xb,xe,k,s,n,t,c,fp,fpint,nrdata,ier = fpcurfm1(x,y,k,t,[w,xb,xe,overwrite_t])\n\nWrapper for ``fpcurfm1``.\n\nParameters\n----------\nx : input rank-1 array('d') with bounds (m)\ny : input rank-1 array('d') with bounds (m)\nk : input int\nt : input rank-1 array('d') with bounds (n)\n\nOther Parameters\n----------------\nw : input rank-1 array('d') with bounds (m), optional\n    Default: 1.0\nxb : input float, optional\n    Default: x[0]\nxe : input float, optional\n    Default: x[m-1]\noverwrite_t : input int, optional\n    Default: 1\n\nReturns\n-------\nx : rank-1 array('d') with bounds (m)\ny : rank-1 array('d') with bounds (m)\nw : rank-1 array('d') with bounds (m)\nxb : float\nxe : float\nk : int\ns : float\nn : int\nt : rank-1 array('d') with bounds (n)\nc : rank-1 array('d') with bounds (nest)\nfp : float\nfpint : rank-1 array('d') with bounds (nest)\nnrdata : rank-1 array('i') with bounds (nest)\nier : int\n"
    ...

def parcur(iopt, ipar, idim, u, x, w, ub, ue, t, wrk, iwrk, k=..., s=...) -> typing.Any:
    "n,c,fp,ier = parcur(iopt,ipar,idim,u,x,w,ub,ue,t,wrk,iwrk,[k,s])\n\nWrapper for ``parcur``.\n\nParameters\n----------\niopt : input int\nipar : input int\nidim : input int\nu : in/output rank-1 array('d') with bounds (m)\nx : input rank-1 array('d') with bounds (mx)\nw : input rank-1 array('d') with bounds (m)\nub : input float\nue : input float\nt : in/output rank-1 array('d') with bounds (nest)\nwrk : in/output rank-1 array('d') with bounds (lwrk)\niwrk : in/output rank-1 array('i') with bounds (nest)\n\nOther Parameters\n----------------\nk : input int, optional\n    Default: 3.0\ns : input float, optional\n    Default: 0.0\n\nReturns\n-------\nn : int\nc : rank-1 array('d') with bounds (nc)\nfp : float\nier : int\n"
    ...

def parder(tx, ty, c, kx, ky, nux, nuy, x, y) -> typing.Any:
    "z,ier = parder(tx,ty,c,kx,ky,nux,nuy,x,y)\n\nWrapper for ``parder``.\n\nParameters\n----------\ntx : input rank-1 array('d') with bounds (nx)\nty : input rank-1 array('d') with bounds (ny)\nc : input rank-1 array('d') with bounds ((nx-kx-1)*(ny-ky-1))\nkx : input int\nky : input int\nnux : input int\nnuy : input int\nx : input rank-1 array('d') with bounds (mx)\ny : input rank-1 array('d') with bounds (my)\n\nReturns\n-------\nz : rank-2 array('d') with bounds (mx,my)\nier : int\n"
    ...

def pardeu(tx, ty, c, kx, ky, nux, nuy, x, y) -> typing.Any:
    "z,ier = pardeu(tx,ty,c,kx,ky,nux,nuy,x,y)\n\nWrapper for ``pardeu``.\n\nParameters\n----------\ntx : input rank-1 array('d') with bounds (nx)\nty : input rank-1 array('d') with bounds (ny)\nc : input rank-1 array('d') with bounds ((nx-kx-1)*(ny-ky-1))\nkx : input int\nky : input int\nnux : input int\nnuy : input int\nx : input rank-1 array('d') with bounds (m)\ny : input rank-1 array('d') with bounds (m)\n\nReturns\n-------\nz : rank-1 array('d') with bounds (m)\nier : int\n"
    ...

def percur(iopt, x, y, w, t, wrk, iwrk, k=..., s=...) -> typing.Any:
    "n,c,fp,ier = percur(iopt,x,y,w,t,wrk,iwrk,[k,s])\n\nWrapper for ``percur``.\n\nParameters\n----------\niopt : input int\nx : input rank-1 array('d') with bounds (m)\ny : input rank-1 array('d') with bounds (m)\nw : input rank-1 array('d') with bounds (m)\nt : in/output rank-1 array('d') with bounds (nest)\nwrk : in/output rank-1 array('d') with bounds (lwrk)\niwrk : in/output rank-1 array('i') with bounds (nest)\n\nOther Parameters\n----------------\nk : input int, optional\n    Default: 3\ns : input float, optional\n    Default: 0.0\n\nReturns\n-------\nn : int\nc : rank-1 array('d') with bounds (n)\nfp : float\nier : int\n"
    ...

def regrid_smth(x, y, z, xb=..., xe=..., yb=..., ye=..., kx=..., ky=..., s=...) -> typing.Any:
    "nx,tx,ny,ty,c,fp,ier = regrid_smth(x,y,z,[xb,xe,yb,ye,kx,ky,s])\n\nWrapper for ``regrid_smth``.\n\nParameters\n----------\nx : input rank-1 array('d') with bounds (mx)\ny : input rank-1 array('d') with bounds (my)\nz : input rank-1 array('d') with bounds (mx*my)\n\nOther Parameters\n----------------\nxb : input float, optional\n    Default: dmin(x,mx)\nxe : input float, optional\n    Default: dmax(x,mx)\nyb : input float, optional\n    Default: dmin(y,my)\nye : input float, optional\n    Default: dmax(y,my)\nkx : input int, optional\n    Default: 3\nky : input int, optional\n    Default: 3\ns : input float, optional\n    Default: 0.0\n\nReturns\n-------\nnx : int\ntx : rank-1 array('d') with bounds (nxest)\nny : int\nty : rank-1 array('d') with bounds (nyest)\nc : rank-1 array('d') with bounds ((nxest-kx-1)*(nyest-ky-1))\nfp : float\nier : int\n"
    ...

def regrid_smth_spher(iopt, ider, u, v, r, r0=..., r1=..., s=...) -> typing.Any:
    "nu,tu,nv,tv,c,fp,ier = regrid_smth_spher(iopt,ider,u,v,r,[r0,r1,s])\n\nWrapper for ``regrid_smth_spher``.\n\nParameters\n----------\niopt : input rank-1 array('i') with bounds (3)\nider : input rank-1 array('i') with bounds (4)\nu : input rank-1 array('d') with bounds (mu)\nv : input rank-1 array('d') with bounds (mv)\nr : input rank-1 array('d') with bounds (mu*mv)\n\nOther Parameters\n----------------\nr0 : input float\nr1 : input float\ns : input float, optional\n    Default: 0.0\n\nReturns\n-------\nnu : int\ntu : rank-1 array('d') with bounds (nuest)\nnv : int\ntv : rank-1 array('d') with bounds (nvest)\nc : rank-1 array('d') with bounds ((nuest-4)*(nvest-4))\nfp : float\nier : int\n"
    ...

def spalde(t, c, k, x) -> typing.Any:
    "d,ier = spalde(t,c,k,x)\n\nWrapper for ``spalde``.\n\nParameters\n----------\nt : input rank-1 array('d') with bounds (n)\nc : input rank-1 array('d') with bounds (n)\nk : input int\nx : input float\n\nReturns\n-------\nd : rank-1 array('d') with bounds (k + 1)\nier : int\n"
    ...

def spherfit_lsq(teta, phi, r, tt, tp, w=..., eps=..., overwrite_tt=..., overwrite_tp=...) -> typing.Any:
    "tt,tp,c,fp,ier = spherfit_lsq(teta,phi,r,tt,tp,[w,eps,overwrite_tt,overwrite_tp])\n\nWrapper for ``spherfit_lsq``.\n\nParameters\n----------\nteta : input rank-1 array('d') with bounds (m)\nphi : input rank-1 array('d') with bounds (m)\nr : input rank-1 array('d') with bounds (m)\ntt : input rank-1 array('d') with bounds (ntest)\ntp : input rank-1 array('d') with bounds (npest)\n\nOther Parameters\n----------------\nw : input rank-1 array('d') with bounds (m), optional\n    Default: 1.0\neps : input float, optional\n    Default: 1e-16\noverwrite_tt : input int, optional\n    Default: 1\noverwrite_tp : input int, optional\n    Default: 1\n\nReturns\n-------\ntt : rank-1 array('d') with bounds (ntest)\ntp : rank-1 array('d') with bounds (npest)\nc : rank-1 array('d') with bounds ((nt-4)*(np-4))\nfp : float\nier : int\n"
    ...

def spherfit_smth(teta, phi, r, w=..., s=..., eps=...) -> typing.Any:
    "nt,tt,np,tp,c,fp,ier = spherfit_smth(teta,phi,r,[w,s,eps])\n\nWrapper for ``spherfit_smth``.\n\nParameters\n----------\nteta : input rank-1 array('d') with bounds (m)\nphi : input rank-1 array('d') with bounds (m)\nr : input rank-1 array('d') with bounds (m)\n\nOther Parameters\n----------------\nw : input rank-1 array('d') with bounds (m), optional\n    Default: 1.0\ns : input float, optional\n    Default: m\neps : input float, optional\n    Default: 1e-16\n\nReturns\n-------\nnt : int\ntt : rank-1 array('d') with bounds (ntest)\nnp : int\ntp : rank-1 array('d') with bounds (npest)\nc : rank-1 array('d') with bounds ((ntest-4)*(npest-4))\nfp : float\nier : int\n"
    ...

def splder(t, c, k, x, nu=..., e=...) -> typing.Any:
    "y = splder(t,c,k,x,[nu,e])\n\nWrapper for ``splder``.\n\nParameters\n----------\nt : input rank-1 array('d') with bounds (n)\nc : input rank-1 array('d') with bounds (n)\nk : input int\nx : input rank-1 array('d') with bounds (m)\n\nOther Parameters\n----------------\nnu : input int, optional\n    Default: 1\ne : input int, optional\n    Default: 0\n\nReturns\n-------\ny : rank-1 array('d') with bounds (m)\n"
    ...

def splev(t, c, k, x, e=...) -> typing.Any:
    "y = splev(t,c,k,x,[e])\n\nWrapper for ``splev``.\n\nParameters\n----------\nt : input rank-1 array('d') with bounds (n)\nc : input rank-1 array('d') with bounds (n)\nk : input int\nx : input rank-1 array('d') with bounds (m)\n\nOther Parameters\n----------------\ne : input int, optional\n    Default: 0\n\nReturns\n-------\ny : rank-1 array('d') with bounds (m)\n"
    ...

def splint(t, c, k, a, b) -> typing.Any:
    "splint = splint(t,c,k,a,b)\n\nWrapper for ``splint``.\n\nParameters\n----------\nt : input rank-1 array('d') with bounds (n)\nc : input rank-1 array('d') with bounds (n)\nk : input int\na : input float\nb : input float\n\nReturns\n-------\nsplint : float\n"
    ...

def sproot(t, c, mest=...) -> typing.Any:
    "zero,m,ier = sproot(t,c,[mest])\n\nWrapper for ``sproot``.\n\nParameters\n----------\nt : input rank-1 array('d') with bounds (n)\nc : input rank-1 array('d') with bounds (n)\n\nOther Parameters\n----------------\nmest : input int, optional\n    Default: 3*(n-7)\n\nReturns\n-------\nzero : rank-1 array('d') with bounds (mest)\nm : int\nier : int\n"
    ...

def surfit_lsq(x, y, z, nx, tx, ny, ty, w=..., xb=..., xe=..., yb=..., ye=..., kx=..., ky=..., eps=..., lwrk2=..., overwrite_tx=..., overwrite_ty=...) -> typing.Any:
    "tx,ty,c,fp,ier = surfit_lsq(x,y,z,nx,tx,ny,ty,[w,xb,xe,yb,ye,kx,ky,eps,lwrk2,overwrite_tx,overwrite_ty])\n\nWrapper for ``surfit_lsq``.\n\nParameters\n----------\nx : input rank-1 array('d') with bounds (m)\ny : input rank-1 array('d') with bounds (m)\nz : input rank-1 array('d') with bounds (m)\nnx : input int\ntx : input rank-1 array('d') with bounds (nmax)\nny : input int\nty : input rank-1 array('d') with bounds (nmax)\n\nOther Parameters\n----------------\nw : input rank-1 array('d') with bounds (m), optional\n    Default: 1.0\nxb : input float, optional\n    Default: calc_b(x,m,tx,nx)\nxe : input float, optional\n    Default: calc_e(x,m,tx,nx)\nyb : input float, optional\n    Default: calc_b(y,m,ty,ny)\nye : input float, optional\n    Default: calc_e(y,m,ty,ny)\nkx : input int, optional\n    Default: 3\nky : input int, optional\n    Default: 3\neps : input float, optional\n    Default: 1e-16\noverwrite_tx : input int, optional\n    Default: 1\noverwrite_ty : input int, optional\n    Default: 1\nlwrk2 : input int, optional\n    Default: calc_surfit_lwrk2(m,kx,ky,nxest,nyest)\n\nReturns\n-------\ntx : rank-1 array('d') with bounds (nmax)\nty : rank-1 array('d') with bounds (nmax)\nc : rank-1 array('d') with bounds ((nx-kx-1)*(ny-ky-1))\nfp : float\nier : int\n"
    ...

def surfit_smth(x, y, z, w=..., xb=..., xe=..., yb=..., ye=..., kx=..., ky=..., s=..., nxest=..., nyest=..., eps=..., lwrk2=...) -> typing.Any:
    "nx,tx,ny,ty,c,fp,wrk1,ier = surfit_smth(x,y,z,[w,xb,xe,yb,ye,kx,ky,s,nxest,nyest,eps,lwrk2])\n\nWrapper for ``surfit_smth``.\n\nParameters\n----------\nx : input rank-1 array('d') with bounds (m)\ny : input rank-1 array('d') with bounds (m)\nz : input rank-1 array('d') with bounds (m)\n\nOther Parameters\n----------------\nw : input rank-1 array('d') with bounds (m), optional\n    Default: 1.0\nxb : input float, optional\n    Default: dmin(x,m)\nxe : input float, optional\n    Default: dmax(x,m)\nyb : input float, optional\n    Default: dmin(y,m)\nye : input float, optional\n    Default: dmax(y,m)\nkx : input int, optional\n    Default: 3\nky : input int, optional\n    Default: 3\ns : input float, optional\n    Default: m\nnxest : input int, optional\n    Default: imax(kx+1+sqrt(m/2),2*(kx+1))\nnyest : input int, optional\n    Default: imax(ky+1+sqrt(m/2),2*(ky+1))\neps : input float, optional\n    Default: 1e-16\nlwrk2 : input int, optional\n    Default: calc_surfit_lwrk2(m,kx,ky,nxest,nyest)\n\nReturns\n-------\nnx : int\ntx : rank-1 array('d') with bounds (nmax)\nny : int\nty : rank-1 array('d') with bounds (nmax)\nc : rank-1 array('d') with bounds ((nxest-kx-1)*(nyest-ky-1))\nfp : float\nwrk1 : rank-1 array('d') with bounds (lwrk1)\nier : int\n"
    ...

def types() -> typing.Any:
    "'i'-scalar\n"
    ...

def __getattr__(name) -> typing.Any:
    ...

