# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: scipy, version: 1.6.2
# Module: scipy.cluster._hierarchy, version: unspecified
import typing
import builtins as _mod_builtins

class Heap(_mod_builtins.object):
    'Binary heap.\n\n    Heap stores values and keys. Values are passed explicitly, whereas keys\n    are assigned implicitly to natural numbers (from 0 to n - 1).\n\n    The supported operations (all have O(log n) time complexity):\n\n        * Return the current minimum value and the corresponding key.\n        * Remove the current minimum value.\n        * Change the value of the given key. Note that the key must be still\n          in the heap.\n\n    The heap is stored as an array, where children of parent i have indices\n    2 * i + 1 and 2 * i + 2. All public methods are based on  `sift_down` and\n    `sift_up` methods, which restore the heap property by moving an element\n    down or up in the heap.\n    '
    def __init__(self, *args, **kwargs) -> None:
        'Binary heap.\n\n    Heap stores values and keys. Values are passed explicitly, whereas keys\n    are assigned implicitly to natural numbers (from 0 to n - 1).\n\n    The supported operations (all have O(log n) time complexity):\n\n        * Return the current minimum value and the corresponding key.\n        * Remove the current minimum value.\n        * Change the value of the given key. Note that the key must be still\n          in the heap.\n\n    The heap is stored as an array, where children of parent i have indices\n    2 * i + 1 and 2 * i + 2. All public methods are based on  `sift_down` and\n    `sift_up` methods, which restore the heap property by moving an element\n    down or up in the heap.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    def __reduce__(self) -> typing.Union[str, typing.Tuple[typing.Any, ...]]:
        ...
    
    def __setstate__(self, state: typing.Any) -> None:
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def change_value(self) -> typing.Any:
        ...
    
    def get_min(self) -> typing.Any:
        ...
    
    def remove_min(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class LinkageUnionFind(_mod_builtins.object):
    'Structure for fast cluster labeling in unsorted dendrogram.'
    def __init__(self, *args, **kwargs) -> None:
        'Structure for fast cluster labeling in unsorted dendrogram.'
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    def __reduce__(self) -> typing.Union[str, typing.Tuple[typing.Any, ...]]:
        ...
    
    def __setstate__(self, state: typing.Any) -> None:
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

__doc__: typing.Any
__file__: str
__name__: str
__package__: str
def __pyx_unpickle_Enum() -> typing.Any:
    ...

def __pyx_unpickle_Heap() -> typing.Any:
    ...

def __pyx_unpickle_LinkageUnionFind() -> typing.Any:
    ...

__test__: dict
def calculate_cluster_sizes() -> typing.Any:
    '\n    Calculate the size of each cluster. The result is the fourth column of\n    the linkage matrix.\n\n    Parameters\n    ----------\n    Z : ndarray\n        The linkage matrix. The fourth column can be empty.\n    cs : ndarray\n        The array to store the sizes.\n    n : ndarray\n        The number of observations.\n    '
    ...

def cluster_dist() -> typing.Any:
    "\n    Form flat clusters by distance criterion.\n\n    Parameters\n    ----------\n    Z : ndarray\n        The linkage matrix.\n    T : ndarray\n        The array to store the cluster numbers. The i'th observation belongs to\n        cluster `T[i]`.\n    cutoff : double\n        Clusters are formed when distances are less than or equal to `cutoff`.\n    n : int\n        The number of observations.\n    "
    ...

def cluster_in() -> typing.Any:
    "\n    Form flat clusters by inconsistent criterion.\n\n    Parameters\n    ----------\n    Z : ndarray\n        The linkage matrix.\n    R : ndarray\n        The inconsistent matrix.\n    T : ndarray\n        The array to store the cluster numbers. The i'th observation belongs to\n        cluster `T[i]`.\n    cutoff : double\n        Clusters are formed when the inconsistent values are less than or\n        or equal to `cutoff`.\n    n : int\n        The number of observations.\n    "
    ...

def cluster_maxclust_dist() -> typing.Any:
    "\n    Form flat clusters by maxclust criterion.\n\n    Parameters\n    ----------\n    Z : ndarray\n        The linkage matrix.\n    T : ndarray\n        The array to store the cluster numbers. The i'th observation belongs to\n        cluster `T[i]`.\n    n : int\n        The number of observations.\n    mc : int\n        The maximum number of clusters.\n    "
    ...

def cluster_maxclust_monocrit() -> typing.Any:
    "\n    Form flat clusters by maxclust_monocrit criterion.\n\n    Parameters\n    ----------\n    Z : ndarray\n        The linkage matrix.\n    MC : ndarray\n        The monotonic criterion array.\n    T : ndarray\n        The array to store the cluster numbers. The i'th observation belongs to\n        cluster `T[i]`.\n    n : int\n        The number of observations.\n    max_nc : int\n        The maximum number of clusters.\n    "
    ...

def cluster_monocrit() -> typing.Any:
    "\n    Form flat clusters by monocrit criterion.\n\n    Parameters\n    ----------\n    Z : ndarray\n        The linkage matrix.\n    MC : ndarray\n        The monotonic criterion array.\n    T : ndarray\n        The array to store the cluster numbers. The i'th observation belongs to\n        cluster `T[i]`.\n    cutoff : double\n        Clusters are formed when the MC values are less than or equal to\n        `cutoff`.\n    n : int\n        The number of observations.\n    "
    ...

def cophenetic_distances() -> typing.Any:
    '\n    Calculate the cophenetic distances between each observation\n\n    Parameters\n    ----------\n    Z : ndarray\n        The linkage matrix.\n    d : ndarray\n        The condensed matrix to store the cophenetic distances.\n    n : int\n        The number of observations.\n    '
    ...

def fast_linkage() -> typing.Any:
    'Perform hierarchy clustering.\n\n    It implements "Generic Clustering Algorithm" from [1]. The worst case\n    time complexity is O(N^3), but the best case time complexity is O(N^2) and\n    it usually works quite close to the best case.\n\n    Parameters\n    ----------\n    dists : ndarray\n        A condensed matrix stores the pairwise distances of the observations.\n    n : int\n        The number of observations.\n    method : int\n        The linkage method. 0: single 1: complete 2: average 3: centroid\n        4: median 5: ward 6: weighted\n\n    Returns\n    -------\n    Z : ndarray, shape (n - 1, 4)\n        Computed linkage matrix.\n\n    References\n    ----------\n    .. [1] Daniel Mullner, "Modern hierarchical, agglomerative clustering\n       algorithms", :arXiv:`1109.2378v1`.\n    '
    ...

def get_max_Rfield_for_each_cluster() -> typing.Any:
    "\n    Get the maximum statistic for each non-singleton cluster. For the i'th\n    non-singleton cluster, max_rfs[i] = max{R[j, rf] j is a descendent of i}.\n\n    Parameters\n    ----------\n    Z : ndarray\n        The linkage matrix.\n    R : ndarray\n        The R matrix.\n    max_rfs : ndarray\n        The array to store the result.\n    n : int\n        The number of observations.\n    rf : int\n        Indicate which column of `R` is used.\n    "
    ...

def get_max_dist_for_each_cluster() -> typing.Any:
    '\n    Get the maximum inconsistency coefficient for each non-singleton cluster.\n\n    Parameters\n    ----------\n    Z : ndarray\n        The linkage matrix.\n    MD : ndarray\n        The array to store the result.\n    n : int\n        The number of observations.\n    '
    ...

def inconsistent() -> typing.Any:
    '\n    Calculate the inconsistency statistics.\n\n    Parameters\n    ----------\n    Z : ndarray\n        The linkage matrix.\n    R : ndarray\n        A (n - 1) x 4 matrix to store the result. The inconsistency statistics\n        `R[i]` are calculated over `d` levels below cluster i. `R[i, 0]` is the\n        mean of distances. `R[i, 1]` is the standard deviation of distances.\n        `R[i, 2]` is the number of clusters included. `R[i, 3]` is the\n        inconsistency coefficient.\n\n        .. math:: \\frac{\\mathtt{Z[i,2]}-\\mathtt{R[i,0]}} {R[i,1]}\n\n    n : int\n        The number of observations.\n    d : int\n        The number of levels included in calculation below a node.\n    '
    ...

def leaders() -> typing.Any:
    '\n    Find the leader (root) of each flat cluster.\n\n    Parameters\n    ----------\n    Z : ndarray\n        The linkage matrix.\n    T : ndarray\n        The flat clusters assignment returned by `fcluster` or `fclusterdata`.\n    L : ndarray\n        `L` and `M` store the result. The leader of flat cluster `L[i]` is\n        node `M[i]`.\n    M : ndarray\n        `L` and `M` store the result. The leader of flat cluster `L[i]` is\n        node `M[i]`.\n    nc : int\n        The number of flat clusters.\n    n : int\n        The number of observations.\n\n    Returns\n    -------\n    err_node : int\n        Found that `T` is invalid when examining node `err_node`.\n        `-1` indicates success.\n    '
    ...

def linkage() -> typing.Any:
    '\n    Perform hierarchy clustering.\n\n    Parameters\n    ----------\n    dists : ndarray\n        A condensed matrix stores the pairwise distances of the observations.\n    n : int\n        The number of observations.\n    method : int\n        The linkage method. 0: single 1: complete 2: average 3: centroid\n        4: median 5: ward 6: weighted\n\n    Returns\n    -------\n    Z : ndarray, shape (n - 1, 4)\n        Computed linkage matrix.\n    '
    ...

def mst_single_linkage() -> typing.Any:
    'Perform hierarchy clustering using MST algorithm for single linkage.\n\n    Parameters\n    ----------\n    dists : ndarray\n        A condensed matrix stores the pairwise distances of the observations.\n    n : int\n        The number of observations.\n\n    Returns\n    -------\n    Z : ndarray, shape (n - 1, 4)\n        Computed linkage matrix.\n    '
    ...

def nn_chain() -> typing.Any:
    'Perform hierarchy clustering using nearest-neighbor chain algorithm.\n\n    Parameters\n    ----------\n    dists : ndarray\n        A condensed matrix stores the pairwise distances of the observations.\n    n : int\n        The number of observations.\n    method : int\n        The linkage method. 0: single 1: complete 2: average 3: centroid\n        4: median 5: ward 6: weighted\n\n    Returns\n    -------\n    Z : ndarray, shape (n - 1, 4)\n        Computed linkage matrix.\n    '
    ...

def prelist() -> typing.Any:
    '\n    Perform a pre-order traversal on the linkage tree and get a list of ids\n    of the leaves.\n\n    Parameters\n    ----------\n    Z : ndarray\n        The linkage matrix.\n    members : ndarray\n        The array to store the result.\n    n : int\n        The number of observations.\n    '
    ...

def __getattr__(name) -> typing.Any:
    ...

