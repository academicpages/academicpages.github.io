# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: scipy, version: 1.6.2
# Module: scipy.interpolate._bspl, version: unspecified
import typing
import builtins as _mod_builtins

__doc__: str
__file__: str
__name__: str
__package__: str
def __pyx_unpickle_Enum() -> typing.Any:
    ...

__test__: dict
def _colloc() -> typing.Any:
    'Build the B-spline collocation matrix.\n\n    The collocation matrix is defined as :math:`B_{j,l} = B_l(x_j)`,\n    so that row ``j`` contains all the B-splines which are non-zero\n    at ``x_j``.\n\n    The matrix is constructed in the LAPACK banded storage.\n    Basically, for an N-by-N matrix A with ku upper diagonals and\n    kl lower diagonals, the shape of the array Ab is (2*kl + ku +1, N),\n    where the last kl+ku+1 rows of Ab contain the diagonals of A, and\n    the first kl rows of Ab are not referenced.\n    For more info see, e.g. the docs for the ``*gbsv`` routine.\n\n    This routine is not supposed to be called directly, and\n    does no error checking.\n\n    Parameters\n    ----------\n    x : ndarray, shape (n,)\n        sorted 1D array of x values\n    t : ndarray, shape (nt + k + 1,)\n        sorted 1D array of knots\n    k : int\n        spline order\n    ab : ndarray, shape (2*kl + ku + 1, nt), F-order\n        This parameter is modified in-place.\n        On exit: zeroed out.\n        On exit: B-spline collocation matrix in the band storage with\n        ``ku`` upper diagonals and ``kl`` lower diagonals.\n        Here ``kl = ku = k``.\n    offset : int, optional\n        skip this many rows\n\n    '
    ...

def _handle_lhs_derivatives() -> typing.Any:
    ' Fill in the entries of the collocation matrix corresponding to known\n    derivatives at xval.\n\n    The collocation matrix is in the banded storage, as prepared by _colloc.\n    No error checking.\n\n    Parameters\n    ----------\n    t : ndarray, shape (nt + k + 1,)\n        knots\n    k : integer\n        B-spline order\n    xval : float\n        The value at which to evaluate the derivatives at.\n    ab : ndarray, shape(2*kl + ku + 1, nt), Fortran order\n        B-spline collocation matrix.\n        This argument is modified *in-place*.\n    kl : integer\n        Number of lower diagonals of ab.\n    ku : integer\n        Number of upper diagonals of ab.\n    deriv_ords : 1D ndarray\n        Orders of derivatives known at xval\n    offset : integer, optional\n        Skip this many rows of the matrix ab.\n\n    '
    ...

def _norm_eq_lsq(x, t, k, y, w, ab, rhs) -> typing.Any:
    'Construct the normal equations for the B-spline LSQ problem.\n\n    The observation equations are ``A @ c = y``, and the normal equations are\n    ``A.T @ A @ c = A.T @ y``. This routine fills in the rhs and lhs for the\n    latter.\n\n    The B-spline collocation matrix is defined as :math:`A_{j,l} = B_l(x_j)`,\n    so that row ``j`` contains all the B-splines which are non-zero\n    at ``x_j``.\n\n    The normal eq matrix has at most `2k+1` bands and is constructed in the\n    LAPACK symmetrix banded storage: ``A[i, j] == ab[i-j, j]`` with `i >= j`.\n    See the doctsring for `scipy.linalg.cholesky_banded` for more info.\n\n    This routine is not supposed to be called directly, and\n    does no error checking.\n\n    Parameters\n    ----------\n    x : ndarray, shape (n,)\n        sorted 1D array of x values\n    t : ndarray, shape (nt + k + 1,)\n        sorted 1D array of knots\n    k : int\n        spline order\n    y : ndarray, shape (n, s)\n        a 2D array of y values. The second dimension contains all trailing\n        dimensions of the original array of ordinates.\n    w : ndarray, shape(n,)\n        Weights.\n    ab : ndarray, shape (k+1, n), in Fortran order.\n        This parameter is modified in-place.\n        On entry: should be zeroed out.\n        On exit: LHS of the normal equations.\n    rhs : ndarray, shape (n, s), in Fortran order.\n        This parameter is modified in-place.\n        On entry: should be zeroed out.\n        On exit: RHS of the normal equations.\n\n    '
    ...

def evaluate_all_bspl() -> typing.Any:
    "Evaluate the ``k+1`` B-splines which are non-zero on interval ``m``.\n\n    Parameters\n    ----------\n    t : ndarray, shape (nt + k + 1,)\n        sorted 1D array of knots\n    k : int\n        spline order\n    xval: float\n        argument at which to evaluate the B-splines\n    m : int\n        index of the left edge of the evaluation interval, ``t[m] <= x < t[m+1]``\n    nu : int, optional\n        Evaluate derivatives order `nu`. Default is zero.\n\n    Returns\n    -------\n    ndarray, shape (k+1,)\n        The values of B-splines :math:`[B_{m-k}(xval), ..., B_{m}(xval)]` if\n        `nu` is zero, otherwise the derivatives of order `nu`.\n\n    Examples\n    --------\n\n    A textbook use of this sort of routine is plotting the ``k+1`` polynomial\n    pieces which make up a B-spline of order `k`.\n\n    Consider a cubic spline\n\n    >>> k = 3\n    >>> t = [0., 2., 2., 3., 4.]   # internal knots\n    >>> a, b = t[0], t[-1]    # base interval is [a, b)\n    >>> t = [a]*k + t + [b]*k  # add boundary knots\n\n    >>> import matplotlib.pyplot as plt\n    >>> xx = np.linspace(a, b, 100)\n    >>> plt.plot(xx, BSpline.basis_element(t[k:-k])(xx),\n    ...          'r-', lw=5, alpha=0.5)\n    >>> c = ['b', 'g', 'c', 'k']\n\n    Now we use slide an interval ``t[m]..t[m+1]`` along the base interval\n    ``a..b`` and use `evaluate_all_bspl` to compute the restriction of\n    the B-spline of interest to this interval:\n\n    >>> for i in range(k+1):\n    ...    x1, x2 = t[2*k - i], t[2*k - i + 1]\n    ...    xx = np.linspace(x1 - 0.5, x2 + 0.5)\n    ...    yy = [evaluate_all_bspl(t, k, x, 2*k - i)[i] for x in xx]\n    ...    plt.plot(xx, yy, c[i] + '--', lw=3, label=str(i))\n    ...\n    >>> plt.grid(True)\n    >>> plt.legend()\n    >>> plt.show()\n\n    "
    ...

def evaluate_spline(t, c, k, xp, nu, extrapolate, out) -> typing.Any:
    '\n    Evaluate a spline in the B-spline basis.\n\n    Parameters\n    ----------\n    t : ndarray, shape (n+k+1)\n        knots\n    c : ndarray, shape (n, m)\n        B-spline coefficients\n    xp : ndarray, shape (s,)\n        Points to evaluate the spline at.\n    nu : int\n        Order of derivative to evaluate.\n    extrapolate : int, optional\n        Whether to extrapolate to ouf-of-bounds points, or to return NaNs.\n    out : ndarray, shape (s, m)\n        Computed values of the spline at each of the input points.\n        This argument is modified in-place.\n\n    '
    ...

def __getattr__(name) -> typing.Any:
    ...

