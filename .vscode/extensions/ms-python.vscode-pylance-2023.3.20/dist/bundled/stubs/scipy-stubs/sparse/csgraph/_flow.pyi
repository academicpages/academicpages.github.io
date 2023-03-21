# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: scipy, version: 1.6.2
# Module: scipy.sparse.csgraph._flow, version: unspecified
import typing
import builtins as _mod_builtins
import numpy as _mod_numpy
import scipy.sparse.csr as _mod_scipy_sparse_csr

DTYPE = _mod_numpy.float64
ITYPE = _mod_numpy.int32
class MaximumFlowResult(_mod_builtins.object):
    'Represents the result of a maximum flow calculation.\n\n    Attributes\n    ----------\n    flow_value : int\n        The value of the maximum flow.\n    residual : csr_matrix\n        The residual graph with respect to the maximum flow.\n    '
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, flow_value, residual) -> None:
        'Represents the result of a maximum flow calculation.\n\n    Attributes\n    ----------\n    flow_value : int\n        The value of the maximum flow.\n    residual : csr_matrix\n        The residual graph with respect to the maximum flow.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __module__: str
    def __repr__(self) -> str:
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @property
    def __weakref__(self) -> typing.Any:
        'list of weak references to the object (if defined)'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

__doc__: typing.Any
__file__: str
__name__: str
__package__: str
def __pyx_unpickle_Enum() -> typing.Any:
    ...

__test__: dict
def _add_reverse_edges() -> typing.Any:
    'Add reversed edges to all edges in a graph.\n\n    This adds to a given directed weighted graph all edges in the reverse\n    direction and give them weight 0, unless they already exist.\n\n    Parameters\n    ----------\n    a : csr_matrix\n        The square matrix in CSR format representing a directed graph\n\n    Returns\n    -------\n    res : csr_matrix\n        A new matrix in CSR format in which the missing edges are represented\n        by explicit zeros.\n\n    '
    ...

def _make_edge_pointers() -> typing.Any:
    'Create for each edge pointers to its reverse and its tail.'
    ...

csr_matrix = _mod_scipy_sparse_csr.csr_matrix
def isspmatrix_csr(x) -> typing.Any:
    'Is x of csr_matrix type?\n\n    Parameters\n    ----------\n    x\n        object to check for being a csr matrix\n\n    Returns\n    -------\n    bool\n        True if x is a csr matrix, False otherwise\n\n    Examples\n    --------\n    >>> from scipy.sparse import csr_matrix, isspmatrix_csr\n    >>> isspmatrix_csr(csr_matrix([[5]]))\n    True\n\n    >>> from scipy.sparse import csc_matrix, csr_matrix, isspmatrix_csc\n    >>> isspmatrix_csr(csc_matrix([[5]]))\n    False\n    '
    ...

def maximum_flow(csgraph, source, sink) -> typing.Any:
    "\n    maximum_flow(csgraph, source, sink)\n\n    Maximize the flow between two vertices in a graph.\n\n    .. versionadded:: 1.4.0\n\n    Parameters\n    ----------\n    csgraph : csr_matrix\n        The square matrix representing a directed graph whose (i, j)'th entry\n        is an integer representing the capacity of the edge between\n        vertices i and j.\n    source : int\n        The source vertex from which the flow flows.\n    sink : int\n        The sink vertex to which the flow flows.\n\n    Returns\n    -------\n    res : MaximumFlowResult\n        A maximum flow represented by a ``MaximumFlowResult``\n        which includes the value of the flow in ``flow_value``,\n        and the residual graph in ``residual``.\n\n    Raises\n    ------\n    TypeError:\n        if the input graph is not in CSR format.\n\n    ValueError:\n        if the capacity values are not integers, or the source or sink are out\n        of bounds.\n\n    Notes\n    -----\n    This solves the maximum flow problem on a given directed weighted graph:\n    A flow associates to every edge a value, also called a flow, less than the\n    capacity of the edge, so that for every vertex (apart from the source and\n    the sink vertices), the total incoming flow is equal to the total outgoing\n    flow. The value of a flow is the sum of the flow of all edges leaving the\n    source vertex, and the maximum flow problem consists of finding a flow\n    whose value is maximal.\n\n    By the max-flow min-cut theorem, the maximal value of the flow is also the\n    total weight of the edges in a minimum cut.\n\n    To solve the problem, we use the Edmonds--Karp algorithm. [1]_ This\n    particular implementation strives to exploit sparsity. Its time complexity\n    is :math:`O(VE^2)` and its space complexity is :math:`O(E)`.\n\n    The maximum flow problem is usually defined with real valued capacities,\n    but we require that all capacities are integral to ensure convergence. When\n    dealing with rational capacities, or capacities belonging to\n    :math:`x\\mathbb{Q}` for some fixed :math:`x \\in \\mathbb{R}`, it is possible\n    to reduce the problem to the integral case by scaling all capacities\n    accordingly.\n\n    Solving a maximum-flow problem can be used for example for graph cuts\n    optimization in computer vision [3]_.\n\n    References\n    ----------\n    .. [1] Edmonds, J. and Karp, R. M.\n           Theoretical improvements in algorithmic efficiency for network flow\n           problems. 1972. Journal of the ACM. 19 (2): pp. 248-264\n    .. [2] Cormen, T. H. and Leiserson, C. E. and Rivest, R. L. and Stein C.\n           Introduction to Algorithms. Second Edition. 2001. MIT Press.\n    .. [3] https://en.wikipedia.org/wiki/Graph_cuts_in_computer_vision\n\n    Examples\n    --------\n    Perhaps the simplest flow problem is that of a graph of only two vertices\n    with an edge from source (0) to sink (1)::\n\n        (0) --5--> (1)\n\n    Here, the maximum flow is simply the capacity of the edge:\n\n    >>> from scipy.sparse import csr_matrix\n    >>> from scipy.sparse.csgraph import maximum_flow\n    >>> graph = csr_matrix([[0, 5], [0, 0]])\n    >>> maximum_flow(graph, 0, 1).flow_value\n    5\n\n    If, on the other hand, there is a bottleneck between source and sink, that\n    can reduce the maximum flow::\n\n        (0) --5--> (1) --3--> (2)\n\n    >>> graph = csr_matrix([[0, 5, 0], [0, 0, 3], [0, 0, 0]])\n    >>> maximum_flow(graph, 0, 2).flow_value\n    3\n\n    A less trivial example is given in [2]_, Chapter 26.1:\n\n    >>> graph = csr_matrix([[0, 16, 13,  0,  0,  0],\n    ...                     [0, 10,  0, 12,  0,  0],\n    ...                     [0,  4,  0,  0, 14,  0],\n    ...                     [0,  0,  9,  0,  0, 20],\n    ...                     [0,  0,  0,  7,  0,  4],\n    ...                     [0,  0,  0,  0,  0,  0]])\n    >>> maximum_flow(graph, 0, 5).flow_value\n    23\n\n    It is possible to reduce the problem of finding a maximum matching in a\n    bipartite graph to a maximum flow problem: Let :math:`G = ((U, V), E)` be a\n    bipartite graph. Then, add to the graph a source vertex with edges to every\n    vertex in :math:`U` and a sink vertex with edges from every vertex in\n    :math:`V`. Finally, give every edge in the resulting graph a capacity of 1.\n    Then, a maximum flow in the new graph gives a maximum matching in the\n    original graph consisting of the edges in :math:`E` whose flow is positive.\n\n    Assume that the edges are represented by a\n    :math:`\\lvert U \\rvert \\times \\lvert V \\rvert` matrix in CSR format whose\n    :math:`(i, j)`'th entry is 1 if there is an edge from :math:`i \\in U` to\n    :math:`j \\in V` and 0 otherwise; that is, the input is of the form required\n    by :func:`maximum_bipartite_matching`. Then the CSR representation of the\n    graph constructed above contains this matrix as a block. Here's an example:\n\n    >>> graph = csr_matrix([[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 1, 0]])\n    >>> print(graph.toarray())\n    [[0 1 0 1]\n     [1 0 1 0]\n     [0 1 1 0]]\n    >>> i, j = graph.shape\n    >>> n = graph.nnz\n    >>> indptr = np.concatenate([[0],\n    ...                          graph.indptr + i,\n    ...                          np.arange(n + i + 1, n + i + j + 1),\n    ...                          [n + i + j]])\n    >>> indices = np.concatenate([np.arange(1, i + 1),\n    ...                           graph.indices + i + 1,\n    ...                           np.repeat(i + j + 1, j)])\n    >>> data = np.ones(n + i + j, dtype=int)\n    >>>\n    >>> graph_flow = csr_matrix((data, indices, indptr))\n    >>> print(graph_flow.toarray())\n    [[0 1 1 1 0 0 0 0 0]\n     [0 0 0 0 0 1 0 1 0]\n     [0 0 0 0 1 0 1 0 0]\n     [0 0 0 0 0 1 1 0 0]\n     [0 0 0 0 0 0 0 0 1]\n     [0 0 0 0 0 0 0 0 1]\n     [0 0 0 0 0 0 0 0 1]\n     [0 0 0 0 0 0 0 0 1]\n     [0 0 0 0 0 0 0 0 0]]\n\n    At this point, we can find the maximum flow between the added sink and the\n    added source and the desired matching can be obtained by restricting the\n    residual graph to the block corresponding to the original graph:\n\n    >>> flow = maximum_flow(graph_flow, 0, i+j+1)\n    >>> matching = flow.residual[1:i+1, i+1:i+j+1]\n    >>> print(matching.toarray())\n    [[0 1 0 0]\n     [1 0 0 0]\n     [0 0 1 0]]\n\n    This tells us that the first, second, and third vertex in :math:`U` are\n    matched with the second, first, and third vertex in :math:`V` respectively.\n\n    While this solves the maximum bipartite matching problem in general, note\n    that algorithms specialized to that problem, such as\n    :func:`maximum_bipartite_matching`, will generally perform better.\n\n    This approach can also be used to solve various common generalizations of\n    the maximum bipartite matching problem. If, for instance, some vertices can\n    be matched with more than one other vertex, this may be handled by\n    modifying the capacities of the new graph appropriately.\n\n    "
    ...

def __getattr__(name) -> typing.Any:
    ...

