from typing import Any


def lobpcg(
    A,
    X,
    B=...,
    M=...,
    Y=...,
    tol=...,
    maxiter=...,
    largest=...,
    verbosityLevel=...,
    retLambdaHistory=...,
    retResidualNormsHistory=...,
) -> Any:
    """Locally Optimal Block Preconditioned Conjugate Gradient Method (LOBPCG)

    LOBPCG is a preconditioned eigensolver for large symmetric positive
    definite (SPD) generalized eigenproblems.

    Parameters
    ----------
    A : {sparse matrix, dense matrix, LinearOperator}
        The symmetric linear operator of the problem, usually a
        sparse matrix.  Often called the "stiffness matrix".
    X : ndarray, float32 or float64
        Initial approximation to the ``k`` eigenvectors (non-sparse). If `A`
        has ``shape=(n,n)`` then `X` should have shape ``shape=(n,k)``.
    B : {dense matrix, sparse matrix, LinearOperator}, optional
        The right hand side operator in a generalized eigenproblem.
        By default, ``B = Identity``.  Often called the "mass matrix".
    M : {dense matrix, sparse matrix, LinearOperator}, optional
        Preconditioner to `A`; by default ``M = Identity``.
        `M` should approximate the inverse of `A`.
    Y : ndarray, float32 or float64, optional
        n-by-sizeY matrix of constraints (non-sparse), sizeY < n
        The iterations will be performed in the B-orthogonal complement
        of the column-space of Y. Y must be full rank.
    tol : scalar, optional
        Solver tolerance (stopping criterion).
        The default is ``tol=n*sqrt(eps)``.
    maxiter : int, optional
        Maximum number of iterations.  The default is ``maxiter = 20``.
    largest : bool, optional
        When True, solve for the largest eigenvalues, otherwise the smallest.
    verbosityLevel : int, optional
        Controls solver output.  The default is ``verbosityLevel=0``.
    retLambdaHistory : bool, optional
        Whether to return eigenvalue history.  Default is False.
    retResidualNormsHistory : bool, optional
        Whether to return history of residual norms.  Default is False.

    Returns
    -------
    w : ndarray
        Array of ``k`` eigenvalues
    v : ndarray
        An array of ``k`` eigenvectors.  `v` has the same shape as `X`.
    lambdas : list of ndarray, optional
        The eigenvalue history, if `retLambdaHistory` is True.
    rnorms : list of ndarray, optional
        The history of residual norms, if `retResidualNormsHistory` is True.

    Notes
    -----
    If both ``retLambdaHistory`` and ``retResidualNormsHistory`` are True,
    the return tuple has the following format
    ``(lambda, V, lambda history, residual norms history)``.

    In the following ``n`` denotes the matrix size and ``m`` the number
    of required eigenvalues (smallest or largest).

    The LOBPCG code internally solves eigenproblems of the size ``3m`` on every
    iteration by calling the "standard" dense eigensolver, so if ``m`` is not
    small enough compared to ``n``, it does not make sense to call the LOBPCG
    code, but rather one should use the "standard" eigensolver, e.g. numpy or
    scipy function in this case.
    If one calls the LOBPCG algorithm for ``5m > n``, it will most likely break
    internally, so the code tries to call the standard function instead.

    It is not that ``n`` should be large for the LOBPCG to work, but rather the
    ratio ``n / m`` should be large. It you call LOBPCG with ``m=1``
    and ``n=10``, it works though ``n`` is small. The method is intended
    for extremely large ``n / m``.

    The convergence speed depends basically on two factors:

    1. How well relatively separated the seeking eigenvalues are from the rest
    of the eigenvalues. One can try to vary ``m`` to make this better.

    2. How well conditioned the problem is. This can be changed by using proper
    preconditioning. For example, a rod vibration test problem (under tests
    directory) is ill-conditioned for large ``n``, so convergence will be
    slow, unless efficient preconditioning is used. For this specific
    problem, a good simple preconditioner function would be a linear solve
    for `A`, which is easy to code since A is tridiagonal.

    References
    ----------
    .. [1] A. V. Knyazev (2001),
        Toward the Optimal Preconditioned Eigensolver: Locally Optimal
        Block Preconditioned Conjugate Gradient Method.
        SIAM Journal on Scientific Computing 23, no. 2,
        pp. 517-541. :doi:`10.1137/S1064827500366124`

    .. [2] A. V. Knyazev, I. Lashuk, M. E. Argentati, and E. Ovchinnikov
        (2007), Block Locally Optimal Preconditioned Eigenvalue Xolvers
        (BLOPEX) in hypre and PETSc. :arxiv:`0705.2626`

    .. [3] A. V. Knyazev's C and MATLAB implementations:
        https://github.com/lobpcg/blopex

    Examples
    --------

    Solve ``A x = lambda x`` with constraints and preconditioning.

    >>> import numpy as np
    >>> from scipy.sparse import spdiags, issparse
    >>> from scipy.sparse.linalg import lobpcg, LinearOperator
    >>> n = 100
    >>> vals = np.arange(1, n + 1)
    >>> A = spdiags(vals, 0, n, n)
    >>> A.toarray()
    array([[  1.,   0.,   0., ...,   0.,   0.,   0.],
        [  0.,   2.,   0., ...,   0.,   0.,   0.],
        [  0.,   0.,   3., ...,   0.,   0.,   0.],
        ...,
        [  0.,   0.,   0., ...,  98.,   0.,   0.],
        [  0.,   0.,   0., ...,   0.,  99.,   0.],
        [  0.,   0.,   0., ...,   0.,   0., 100.]])

    Constraints:

    >>> Y = np.eye(n, 3)

    Initial guess for eigenvectors, should have linearly independent
    columns. Column dimension = number of requested eigenvalues.

    >>> rng = np.random.default_rng()
    >>> X = rng.random((n, 3))

    Preconditioner in the inverse of A in this example:

    >>> invA = spdiags([1./vals], 0, n, n)

    The preconditiner must be defined by a function:

    >>> def precond( x ):
    ...     return invA @ x

    The argument x of the preconditioner function is a matrix inside `lobpcg`,
    thus the use of matrix-matrix product ``@``.

    The preconditioner function is passed to lobpcg as a `LinearOperator`:

    >>> M = LinearOperator(matvec=precond, matmat=precond,
    ...                    shape=(n, n), dtype=np.float64)

    Let us now solve the eigenvalue problem for the matrix A:

    >>> eigenvalues, _ = lobpcg(A, X, Y=Y, M=M, largest=False)
    >>> eigenvalues
    array([4., 5., 6.])

    Note that the vectors passed in Y are the eigenvectors of the 3 smallest
    eigenvalues. The results returned are orthogonal to those.

    """
    ...