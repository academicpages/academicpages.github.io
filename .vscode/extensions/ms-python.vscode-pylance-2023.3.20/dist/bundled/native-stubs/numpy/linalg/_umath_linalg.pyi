# Python: 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)]
# Library: numpy, version: 1.20.2
# Module: numpy.linalg._umath_linalg, version: 0.1.5
import typing
import builtins as _mod_builtins

__doc__: typing.Any
__file__: str
__name__: str
__package__: str
__version__: str
def cholesky_lo(x, out=..., *, casting=..., order=..., dtype=..., subok=..., signature=..., extobj=...) -> typing.Any:
    'cholesky_lo(x, /, out=None, *, casting=\'same_kind\', order=\'K\', dtype=None, subok=True[, signature, extobj])\n\ncholesky decomposition of hermitian positive-definite matrices. \nBroadcast to all outer dimensions. \n    "(m,m)->(m,m)" \n'
    ...

def det(x, out=..., *, casting=..., order=..., dtype=..., subok=..., signature=..., extobj=...) -> typing.Any:
    'det(x, /, out=None, *, casting=\'same_kind\', order=\'K\', dtype=None, subok=True[, signature, extobj])\n\ndet of the last two dimensions and broadcast on the rest. \n    "(m,m)->()" \n'
    ...

def eig(x, out1=..., out2=..., out=..., *, casting=..., order=..., dtype=..., subok=..., signature=..., extobj=...) -> typing.Any:
    'eig(x[, out1, out2], / [, out=(None, None)], *, casting=\'same_kind\', order=\'K\', dtype=None, subok=True[, signature, extobj])\n\neig on the last two dimension and broadcast to the rest. \nResults in a vector with the  eigenvalues and a matrix with the eigenvectors. \n    "(m,m)->(m),(m,m)" \n'
    ...

def eigh_lo(x, out1=..., out2=..., out=..., *, casting=..., order=..., dtype=..., subok=..., signature=..., extobj=...) -> typing.Any:
    'eigh_lo(x[, out1, out2], / [, out=(None, None)], *, casting=\'same_kind\', order=\'K\', dtype=None, subok=True[, signature, extobj])\n\neigh on the last two dimension and broadcast to the rest, using lower triangle \nResults in a vector of eigenvalues and a matrix with theeigenvectors. \n    "(m,m)->(m),(m,m)" \n'
    ...

def eigh_up(x, out1=..., out2=..., out=..., *, casting=..., order=..., dtype=..., subok=..., signature=..., extobj=...) -> typing.Any:
    'eigh_up(x[, out1, out2], / [, out=(None, None)], *, casting=\'same_kind\', order=\'K\', dtype=None, subok=True[, signature, extobj])\n\neigh on the last two dimension and broadcast to the rest, using upper triangle. \nResults in a vector of eigenvalues and a matrix with the eigenvectors. \n    "(m,m)->(m),(m,m)" \n'
    ...

def eigvals(x, out=..., *, casting=..., order=..., dtype=..., subok=..., signature=..., extobj=...) -> typing.Any:
    "eigvals(x, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])\n\neigvals on the last two dimension and broadcast to the rest. \nResults in a vector of eigenvalues. \n"
    ...

def eigvalsh_lo(x, out=..., *, casting=..., order=..., dtype=..., subok=..., signature=..., extobj=...) -> typing.Any:
    'eigvalsh_lo(x, /, out=None, *, casting=\'same_kind\', order=\'K\', dtype=None, subok=True[, signature, extobj])\n\neigh on the last two dimension and broadcast to the rest, using lower triangle. \nResults in a vector of eigenvalues and a matrix with theeigenvectors. \n    "(m,m)->(m)" \n'
    ...

def eigvalsh_up(x, out=..., *, casting=..., order=..., dtype=..., subok=..., signature=..., extobj=...) -> typing.Any:
    'eigvalsh_up(x, /, out=None, *, casting=\'same_kind\', order=\'K\', dtype=None, subok=True[, signature, extobj])\n\neigvalsh on the last two dimension and broadcast to the rest, using upper triangle. \nResults in a vector of eigenvalues and a matrix with theeigenvectors.\n    "(m,m)->(m)" \n'
    ...

def inv(x, out=..., *, casting=..., order=..., dtype=..., subok=..., signature=..., extobj=...) -> typing.Any:
    'inv(x, /, out=None, *, casting=\'same_kind\', order=\'K\', dtype=None, subok=True[, signature, extobj])\n\ncompute the inverse of the last two dimensions and broadcast to the rest. \nResults in the inverse matrices. \n    "(m,m)->(m,m)" \n'
    ...

def lstsq_m(x1, x2, x3, out1=..., out2=..., out3=..., out4=..., out=..., *, casting=..., order=..., dtype=..., subok=..., signature=..., extobj=...) -> typing.Any:
    "lstsq_m(x1, x2, x3[, out1, out2, out3, out4], / [, out=(None, None, None, None)], *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])\n\nleast squares on the last two dimensions and broadcast to the rest. \nFor m <= n. \n"
    ...

def lstsq_n(x1, x2, x3, out1=..., out2=..., out3=..., out4=..., out=..., *, casting=..., order=..., dtype=..., subok=..., signature=..., extobj=...) -> typing.Any:
    "lstsq_n(x1, x2, x3[, out1, out2, out3, out4], / [, out=(None, None, None, None)], *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])\n\nleast squares on the last two dimensions and broadcast to the rest. \nFor m >= n, meaning that residuals are produced. \n"
    ...

def slogdet(x, out1=..., out2=..., out=..., *, casting=..., order=..., dtype=..., subok=..., signature=..., extobj=...) -> typing.Any:
    'slogdet(x[, out1, out2], / [, out=(None, None)], *, casting=\'same_kind\', order=\'K\', dtype=None, subok=True[, signature, extobj])\n\nslogdet on the last two dimensions and broadcast on the rest. \nResults in two arrays, one with sign and the other with log of the determinants. \n    "(m,m)->(),()" \n'
    ...

def solve(x1, x2, out=..., *, casting=..., order=..., dtype=..., subok=..., signature=..., extobj=...) -> typing.Any:
    'solve(x1, x2, /, out=None, *, casting=\'same_kind\', order=\'K\', dtype=None, subok=True[, signature, extobj])\n\nsolve the system a x = b, on the last two dimensions, broadcast to the rest. \nResults in a matrices with the solutions. \n    "(m,m),(m,n)->(m,n)" \n'
    ...

def solve1(x1, x2, out=..., *, casting=..., order=..., dtype=..., subok=..., signature=..., extobj=...) -> typing.Any:
    'solve1(x1, x2, /, out=None, *, casting=\'same_kind\', order=\'K\', dtype=None, subok=True[, signature, extobj])\n\nsolve the system a x = b, for b being a vector, broadcast in the outer dimensions. \nResults in vectors with the solutions. \n    "(m,m),(m)->(m)" \n'
    ...

def svd_m(x, out=..., *, casting=..., order=..., dtype=..., subok=..., signature=..., extobj=...) -> typing.Any:
    "svd_m(x, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])\n\nsvd when n>=m. "
    ...

def svd_m_f(x, out1=..., out2=..., out3=..., out=..., *, casting=..., order=..., dtype=..., subok=..., signature=..., extobj=...) -> typing.Any:
    "svd_m_f(x[, out1, out2, out3], / [, out=(None, None, None)], *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])\n\nsvd when m<=n"
    ...

def svd_m_s(x, out1=..., out2=..., out3=..., out=..., *, casting=..., order=..., dtype=..., subok=..., signature=..., extobj=...) -> typing.Any:
    "svd_m_s(x[, out1, out2, out3], / [, out=(None, None, None)], *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])\n\nsvd when m<=n"
    ...

def svd_n(x, out=..., *, casting=..., order=..., dtype=..., subok=..., signature=..., extobj=...) -> typing.Any:
    "svd_n(x, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])\n\nsvd when n<=m"
    ...

def svd_n_f(x, out1=..., out2=..., out3=..., out=..., *, casting=..., order=..., dtype=..., subok=..., signature=..., extobj=...) -> typing.Any:
    "svd_n_f(x[, out1, out2, out3], / [, out=(None, None, None)], *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])\n\nsvd when m>=n"
    ...

def svd_n_s(x, out1=..., out2=..., out3=..., out=..., *, casting=..., order=..., dtype=..., subok=..., signature=..., extobj=...) -> typing.Any:
    "svd_n_s(x[, out1, out2, out3], / [, out=(None, None, None)], *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])\n\nsvd when m>=n"
    ...

def __getattr__(name) -> typing.Any:
    ...

