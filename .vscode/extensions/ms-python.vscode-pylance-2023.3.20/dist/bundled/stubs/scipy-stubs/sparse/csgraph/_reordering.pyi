# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: scipy, version: 1.6.2
# Module: scipy.sparse.csgraph._reordering, version: unspecified
import typing
import builtins as _mod_builtins
import numpy as _mod_numpy
import scipy.sparse.base as _mod_scipy_sparse_base
import scipy.sparse.csc as _mod_scipy_sparse_csc
import scipy.sparse.csr as _mod_scipy_sparse_csr

DTYPE = _mod_numpy.float64
ITYPE = _mod_numpy.int32
SparseEfficiencyWarning = _mod_scipy_sparse_base.SparseEfficiencyWarning
__doc__: typing.Any
__file__: str
__name__: str
__package__: str
def __pyx_unpickle_Enum() -> typing.Any:
    ...

__test__: dict
def _reverse_cuthill_mckee(ind, ptr, num_rows) -> typing.Any:
    '\n    Reverse Cuthill-McKee ordering of a sparse symmetric CSR or CSC matrix.  \n    We follow the original Cuthill-McKee paper and always start the routine\n    at a node of lowest degree for each connected component.\n    '
    ...

csc_matrix = _mod_scipy_sparse_csc.csc_matrix
csr_matrix = _mod_scipy_sparse_csr.csr_matrix
def isspmatrix(x) -> typing.Any:
    'Is x of a sparse matrix type?\n\n    Parameters\n    ----------\n    x\n        object to check for being a sparse matrix\n\n    Returns\n    -------\n    bool\n        True if x is a sparse matrix, False otherwise\n\n    Notes\n    -----\n    issparse and isspmatrix are aliases for the same function.\n\n    Examples\n    --------\n    >>> from scipy.sparse import csr_matrix, isspmatrix\n    >>> isspmatrix(csr_matrix([[5]]))\n    True\n\n    >>> from scipy.sparse import isspmatrix\n    >>> isspmatrix(5)\n    False\n    '
    ...

def isspmatrix_coo(x) -> typing.Any:
    'Is x of coo_matrix type?\n\n    Parameters\n    ----------\n    x\n        object to check for being a coo matrix\n\n    Returns\n    -------\n    bool\n        True if x is a coo matrix, False otherwise\n\n    Examples\n    --------\n    >>> from scipy.sparse import coo_matrix, isspmatrix_coo\n    >>> isspmatrix_coo(coo_matrix([[5]]))\n    True\n\n    >>> from scipy.sparse import coo_matrix, csr_matrix, isspmatrix_coo\n    >>> isspmatrix_coo(csr_matrix([[5]]))\n    False\n    '
    ...

def isspmatrix_csc(x) -> typing.Any:
    'Is x of csc_matrix type?\n\n    Parameters\n    ----------\n    x\n        object to check for being a csc matrix\n\n    Returns\n    -------\n    bool\n        True if x is a csc matrix, False otherwise\n\n    Examples\n    --------\n    >>> from scipy.sparse import csc_matrix, isspmatrix_csc\n    >>> isspmatrix_csc(csc_matrix([[5]]))\n    True\n\n    >>> from scipy.sparse import csc_matrix, csr_matrix, isspmatrix_csc\n    >>> isspmatrix_csc(csr_matrix([[5]]))\n    False\n    '
    ...

def isspmatrix_csr(x) -> typing.Any:
    'Is x of csr_matrix type?\n\n    Parameters\n    ----------\n    x\n        object to check for being a csr matrix\n\n    Returns\n    -------\n    bool\n        True if x is a csr matrix, False otherwise\n\n    Examples\n    --------\n    >>> from scipy.sparse import csr_matrix, isspmatrix_csr\n    >>> isspmatrix_csr(csr_matrix([[5]]))\n    True\n\n    >>> from scipy.sparse import csc_matrix, csr_matrix, isspmatrix_csc\n    >>> isspmatrix_csr(csc_matrix([[5]]))\n    False\n    '
    ...

def maximum_bipartite_matching(graph, perm_type=...) -> typing.Any:
    '\n    maximum_bipartite_matching(graph, perm_type=\'row\')\n\n    Returns a matching of a bipartite graph whose cardinality is as least that\n    of any given matching of the graph.\n\n    Parameters\n    ----------\n    graph : sparse matrix\n        Input sparse in CSR format whose rows represent one partition of the\n        graph and whose columns represent the other partition. An edge between\n        two vertices is indicated by the corresponding entry in the matrix\n        existing in its sparse representation.\n    perm_type : str, {\'row\', \'column\'}\n        Which partition to return the matching in terms of: If ``\'row\'``, the\n        function produces an array whose length is the number of columns in the\n        input, and whose :math:`j`\'th element is the row matched to the\n        :math:`j`\'th column. Conversely, if ``perm_type`` is ``\'column\'``, this\n        returns the columns matched to each row.\n\n    Returns\n    -------\n    perm : ndarray\n        A matching of the vertices in one of the two partitions. Unmatched\n        vertices are represented by a ``-1`` in the result.\n\n    Notes\n    -----\n    This function implements the Hopcroft--Karp algorithm [1]_. Its time\n    complexity is :math:`O(\\lvert E \\rvert \\sqrt{\\lvert V \\rvert})`, and its\n    space complexity is linear in the number of rows. In practice, this\n    asymmetry between rows and columns means that it can be more efficient to\n    transpose the input if it contains more columns than rows.\n\n    By Konig\'s theorem, the cardinality of the matching is also the number of\n    vertices appearing in a minimum vertex cover of the graph.\n\n    Note that if the sparse representation contains explicit zeros, these are\n    still counted as edges.\n\n    The implementation was changed in SciPy 1.4.0 to allow matching of general\n    bipartite graphs, where previous versions would assume that a perfect\n    matching existed. As such, code written against 1.4.0 will not necessarily\n    work on older versions.\n\n    References\n    ----------\n    .. [1] John E. Hopcroft and Richard M. Karp. "An n^{5 / 2} Algorithm for\n           Maximum Matchings in Bipartite Graphs" In: SIAM Journal of Computing\n           2.4 (1973), pp. 225--231. :doi:`10.1137/0202019`\n\n    Examples\n    --------\n    >>> from scipy.sparse import csr_matrix\n    >>> from scipy.sparse.csgraph import maximum_bipartite_matching\n\n    As a simple example, consider a bipartite graph in which the partitions\n    contain 2 and 3 elements respectively. Suppose that one partition contains\n    vertices labelled 0 and 1, and that the other partition contains vertices\n    labelled A, B, and C. Suppose that there are edges connecting 0 and C,\n    1 and A, and 1 and B. This graph would then be represented by the following\n    sparse matrix:\n\n    >>> graph = csr_matrix([[0, 0, 1], [1, 1, 0]])\n\n    Here, the 1s could be anything, as long as they end up being stored as\n    elements in the sparse matrix. We can now calculate maximum matchings as\n    follows:\n\n    >>> print(maximum_bipartite_matching(graph, perm_type=\'column\'))\n    [2 0]\n    >>> print(maximum_bipartite_matching(graph, perm_type=\'row\'))\n    [ 1 -1  0]\n\n    The first output tells us that 1 and 2 are matched with C and A\n    respectively, and the second output tells us that A, B, and C are matched\n    with 1, nothing, and 0 respectively.\n\n    Note that explicit zeros are still converted to edges. This means that a\n    different way to represent the above graph is by using the CSR structure\n    directly as follows:\n\n    >>> data = [0, 0, 0]\n    >>> indices = [2, 0, 1]\n    >>> indptr = [0, 1, 3]\n    >>> graph = csr_matrix((data, indices, indptr))\n    >>> print(maximum_bipartite_matching(graph, perm_type=\'column\'))\n    [2 0]\n    >>> print(maximum_bipartite_matching(graph, perm_type=\'row\'))\n    [ 1 -1  0]\n\n    When one or both of the partitions are empty, the matching is empty as\n    well:\n\n    >>> graph = csr_matrix((2, 0))\n    >>> print(maximum_bipartite_matching(graph, perm_type=\'column\'))\n    [-1 -1]\n    >>> print(maximum_bipartite_matching(graph, perm_type=\'row\'))\n    []\n\n    When the input matrix is square, and the graph is known to admit a perfect\n    matching, i.e. a matching with the property that every vertex in the graph\n    belongs to some edge in the matching, then one can view the output as the\n    permutation of rows (or columns) turning the input matrix into one with the\n    property that all diagonal elements are non-empty:\n\n    >>> a = [[0, 1, 2, 0], [1, 0, 0, 1], [2, 0, 0, 3], [0, 1, 3, 0]]\n    >>> graph = csr_matrix(a)\n    >>> perm = maximum_bipartite_matching(graph, perm_type=\'row\')\n    >>> print(graph[perm].toarray())\n    [[1 0 0 1]\n     [0 1 2 0]\n     [0 1 3 0]\n     [2 0 0 3]]\n\n    '
    ...

def reverse_cuthill_mckee(graph, symmetric_mode=...) -> typing.Any:
    '\n    reverse_cuthill_mckee(graph, symmetric_mode=False)\n    \n    Returns the permutation array that orders a sparse CSR or CSC matrix\n    in Reverse-Cuthill McKee ordering.  \n    \n    It is assumed by default, ``symmetric_mode=False``, that the input matrix \n    is not symmetric and works on the matrix ``A+A.T``. If you are \n    guaranteed that the matrix is symmetric in structure (values of matrix \n    elements do not matter) then set ``symmetric_mode=True``.\n    \n    Parameters\n    ----------\n    graph : sparse matrix\n        Input sparse in CSC or CSR sparse matrix format.\n    symmetric_mode : bool, optional\n        Is input matrix guaranteed to be symmetric.\n\n    Returns\n    -------\n    perm : ndarray\n        Array of permuted row and column indices.\n \n    Notes\n    -----\n    .. versionadded:: 0.15.0\n\n    References\n    ----------\n    E. Cuthill and J. McKee, "Reducing the Bandwidth of Sparse Symmetric Matrices",\n    ACM \'69 Proceedings of the 1969 24th national conference, (1969).\n\n    Examples\n    --------\n    >>> from scipy.sparse import csr_matrix\n    >>> from scipy.sparse.csgraph import reverse_cuthill_mckee\n\n    >>> graph = [\n    ... [0, 1 , 2, 0],\n    ... [0, 0, 0, 1],\n    ... [2, 0, 0, 3],\n    ... [0, 0, 0, 0]\n    ... ]\n    >>> graph = csr_matrix(graph)\n    >>> print(graph)\n      (0, 1)\t1\n      (0, 2)\t2\n      (1, 3)\t1\n      (2, 0)\t2\n      (2, 3)\t3\n\n    >>> reverse_cuthill_mckee(graph)\n    array([3, 2, 1, 0], dtype=int32)\n    \n    '
    ...

def structural_rank(graph) -> typing.Any:
    '\n    structural_rank(graph)\n    \n    Compute the structural rank of a graph (matrix) with a given \n    sparsity pattern.\n\n    The structural rank of a matrix is the number of entries in the maximum \n    transversal of the corresponding bipartite graph, and is an upper bound \n    on the numerical rank of the matrix. A graph has full structural rank \n    if it is possible to permute the elements to make the diagonal zero-free.\n\n    .. versionadded:: 0.19.0\n\n    Parameters\n    ----------\n    graph : sparse matrix\n        Input sparse matrix.\n\n    Returns\n    -------\n    rank : int\n        The structural rank of the sparse graph.\n    \n    References\n    ----------\n    .. [1] I. S. Duff, "Computing the Structural Index", SIAM J. Alg. Disc. \n            Meth., Vol. 7, 594 (1986).\n    \n    .. [2] http://www.cise.ufl.edu/research/sparse/matrices/legend.html\n\n    Examples\n    --------\n    >>> from scipy.sparse import csr_matrix\n    >>> from scipy.sparse.csgraph import structural_rank\n\n    >>> graph = [\n    ... [0, 1, 2, 0],\n    ... [1, 0, 0, 1],\n    ... [2, 0, 0, 3],\n    ... [0, 1, 3, 0]\n    ... ]\n    >>> graph = csr_matrix(graph)\n    >>> print(graph)\n      (0, 1)\t1\n      (0, 2)\t2\n      (1, 0)\t1\n      (1, 3)\t1\n      (2, 0)\t2\n      (2, 3)\t3\n      (3, 1)\t1\n      (3, 2)\t3\n\n    >>> structural_rank(graph)\n    4\n\n    '
    ...

def warn(message, category, stacklevel, source) -> typing.Any:
    'Issue a warning, or maybe ignore it or raise an exception.'
    ...

def __getattr__(name) -> typing.Any:
    ...

