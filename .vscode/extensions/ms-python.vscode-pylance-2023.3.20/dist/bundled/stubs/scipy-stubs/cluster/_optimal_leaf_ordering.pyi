# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: scipy, version: 1.6.2
# Module: scipy.cluster._optimal_leaf_ordering, version: unspecified
import typing
import builtins as _mod_builtins

__doc__: typing.Any
__file__: str
__name__: str
__package__: str
def __pyx_unpickle_Enum() -> typing.Any:
    ...

__test__: dict
def is_valid_dm(D, tol, throw, name, warning) -> typing.Any:
    '\n    Return True if input array is a valid distance matrix.\n\n    Distance matrices must be 2-dimensional numpy arrays.\n    They must have a zero-diagonal, and they must be symmetric.\n\n    Parameters\n    ----------\n    D : ndarray\n        The candidate object to test for validity.\n    tol : float, optional\n        The distance matrix should be symmetric. `tol` is the maximum\n        difference between entries ``ij`` and ``ji`` for the distance\n        metric to be considered symmetric.\n    throw : bool, optional\n        An exception is thrown if the distance matrix passed is not valid.\n    name : str, optional\n        The name of the variable to checked. This is useful if\n        throw is set to True so the offending variable can be identified\n        in the exception message when an exception is thrown.\n    warning : bool, optional\n        Instead of throwing an exception, a warning message is\n        raised.\n\n    Returns\n    -------\n    valid : bool\n        True if the variable `D` passed is a valid distance matrix.\n\n    Notes\n    -----\n    Small numerical differences in `D` and `D.T` and non-zeroness of\n    the diagonal are ignored if they are within the tolerance specified\n    by `tol`.\n\n    '
    ...

def is_valid_y(y, warning, throw, name) -> typing.Any:
    '\n    Return True if the input array is a valid condensed distance matrix.\n\n    Condensed distance matrices must be 1-dimensional numpy arrays.\n    Their length must be a binomial coefficient :math:`{n \\choose 2}`\n    for some positive integer n.\n\n    Parameters\n    ----------\n    y : ndarray\n        The condensed distance matrix.\n    warning : bool, optional\n        Invokes a warning if the variable passed is not a valid\n        condensed distance matrix. The warning message explains why\n        the distance matrix is not valid.  `name` is used when\n        referencing the offending variable.\n    throw : bool, optional\n        Throws an exception if the variable passed is not a valid\n        condensed distance matrix.\n    name : bool, optional\n        Used when referencing the offending variable in the\n        warning or exception message.\n\n    '
    ...

def optimal_leaf_ordering() -> typing.Any:
    '\n    Compute the optimal leaf order for Z (according to D) and return an \n    optimally sorted Z. \n\n    We start by sorting and relabelling Z and D according to the current leaf \n    order in Z.\n    \n    This is because when everything is sorted each cluster (including\n    singletons) can be defined by its range over (0...n_points).\n\n    This is used extensively to loop efficiently over the various arrays in the \n    algorithm.\n\n    '
    ...

def squareform(X, force, checks) -> typing.Any:
    "\n    Convert a vector-form distance vector to a square-form distance\n    matrix, and vice-versa.\n\n    Parameters\n    ----------\n    X : ndarray\n        Either a condensed or redundant distance matrix.\n    force : str, optional\n        As with MATLAB(TM), if force is equal to ``'tovector'`` or\n        ``'tomatrix'``, the input will be treated as a distance matrix or\n        distance vector respectively.\n    checks : bool, optional\n        If set to False, no checks will be made for matrix\n        symmetry nor zero diagonals. This is useful if it is known that\n        ``X - X.T1`` is small and ``diag(X)`` is close to zero.\n        These values are ignored any way so they do not disrupt the\n        squareform transformation.\n\n    Returns\n    -------\n    Y : ndarray\n        If a condensed distance matrix is passed, a redundant one is\n        returned, or if a redundant one is passed, a condensed distance\n        matrix is returned.\n\n    Notes\n    -----\n    1. ``v = squareform(X)``\n\n       Given a square n-by-n symmetric distance matrix ``X``,\n       ``v = squareform(X)`` returns a ``n * (n-1) / 2``\n       (i.e. binomial coefficient n choose 2) sized vector `v`\n       where :math:`v[{n \\choose 2} - {n-i \\choose 2} + (j-i-1)]`\n       is the distance between distinct points ``i`` and ``j``.\n       If ``X`` is non-square or asymmetric, an error is raised.\n\n    2. ``X = squareform(v)``\n\n       Given a ``n * (n-1) / 2`` sized vector ``v``\n       for some integer ``n >= 1`` encoding distances as described,\n       ``X = squareform(v)`` returns a n-by-n distance matrix ``X``.\n       The ``X[i, j]`` and ``X[j, i]`` values are set to\n       :math:`v[{n \\choose 2} - {n-i \\choose 2} + (j-i-1)]`\n       and all diagonal elements are zero.\n\n    In SciPy 0.19.0, ``squareform`` stopped casting all input types to\n    float64, and started returning arrays of the same dtype as the input.\n\n    "
    ...

def __getattr__(name) -> typing.Any:
    ...

