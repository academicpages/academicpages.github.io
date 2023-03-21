# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: scipy, version: 1.6.2
# Module: scipy.spatial.ckdtree, version: unspecified
import typing
import builtins as _mod_builtins

__all__: list
__doc__: typing.Any
__file__: str
__name__: str
__package__: str
def __pyx_unpickle_Enum() -> typing.Any:
    ...

def __pyx_unpickle_cKDTreeNode() -> typing.Any:
    ...

__test__: dict
class cKDTree(_mod_builtins.object):
    '\n    cKDTree(data, leafsize=16, compact_nodes=True, copy_data=False,\n            balanced_tree=True, boxsize=None)\n\n    kd-tree for quick nearest-neighbor lookup\n\n    This class provides an index into a set of k-dimensional points\n    which can be used to rapidly look up the nearest neighbors of any\n    point.\n\n    Parameters\n    ----------\n    data : array_like, shape (n,m)\n        The n data points of dimension m to be indexed. This array is\n        not copied unless this is necessary to produce a contiguous\n        array of doubles, and so modifying this data will result in\n        bogus results. The data are also copied if the kd-tree is built\n        with copy_data=True.\n    leafsize : positive int, optional\n        The number of points at which the algorithm switches over to\n        brute-force. Default: 16.\n    compact_nodes : bool, optional\n        If True, the kd-tree is built to shrink the hyperrectangles to\n        the actual data range. This usually gives a more compact tree that\n        is robust against degenerated input data and gives faster queries\n        at the expense of longer build time. Default: True.\n    copy_data : bool, optional\n        If True the data is always copied to protect the kd-tree against\n        data corruption. Default: False.\n    balanced_tree : bool, optional\n        If True, the median is used to split the hyperrectangles instead of\n        the midpoint. This usually gives a more compact tree and\n        faster queries at the expense of longer build time. Default: True.\n    boxsize : array_like or scalar, optional\n        Apply a m-d toroidal topology to the KDTree.. The topology is generated\n        by :math:`x_i + n_i L_i` where :math:`n_i` are integers and :math:`L_i`\n        is the boxsize along i-th dimension. The input data shall be wrapped\n        into :math:`[0, L_i)`. A ValueError is raised if any of the data is\n        outside of this bound.\n\n    Notes\n    -----\n    The algorithm used is described in Maneewongvatana and Mount 1999.\n    The general idea is that the kd-tree is a binary tree, each of whose\n    nodes represents an axis-aligned hyperrectangle. Each node specifies\n    an axis and splits the set of points based on whether their coordinate\n    along that axis is greater than or less than a particular value.\n\n    During construction, the axis and splitting point are chosen by the\n    "sliding midpoint" rule, which ensures that the cells do not all\n    become long and thin.\n\n    The tree can be queried for the r closest neighbors of any given point\n    (optionally returning only those within some maximum distance of the\n    point). It can also be queried, with a substantial gain in efficiency,\n    for the r approximate closest neighbors.\n\n    For large dimensions (20 is already large) do not expect this to run\n    significantly faster than brute force. High-dimensional nearest-neighbor\n    queries are a substantial open problem in computer science.\n\n    Attributes\n    ----------\n    data : ndarray, shape (n,m)\n        The n data points of dimension m to be indexed. This array is\n        not copied unless this is necessary to produce a contiguous\n        array of doubles. The data are also copied if the kd-tree is built\n        with `copy_data=True`.\n    leafsize : positive int\n        The number of points at which the algorithm switches over to\n        brute-force.\n    m : int\n        The dimension of a single data-point.\n    n : int\n        The number of data points.\n    maxes : ndarray, shape (m,)\n        The maximum value in each dimension of the n data points.\n    mins : ndarray, shape (m,)\n        The minimum value in each dimension of the n data points.\n    tree : object, class cKDTreeNode\n        This attribute exposes a Python view of the root node in the cKDTree\n        object. A full Python view of the kd-tree is created dynamically\n        on the first access. This attribute allows you to create your own\n        query functions in Python.\n    size : int\n        The number of nodes in the tree.\n\n    '
    def __getstate__(self) -> typing.Any:
        ...
    
    def __init__(self, data, leafsize=..., compact_nodes=..., copy_data=..., balanced_tree=..., boxsize=...) -> None:
        '\n    cKDTree(data, leafsize=16, compact_nodes=True, copy_data=False,\n            balanced_tree=True, boxsize=None)\n\n    kd-tree for quick nearest-neighbor lookup\n\n    This class provides an index into a set of k-dimensional points\n    which can be used to rapidly look up the nearest neighbors of any\n    point.\n\n    Parameters\n    ----------\n    data : array_like, shape (n,m)\n        The n data points of dimension m to be indexed. This array is\n        not copied unless this is necessary to produce a contiguous\n        array of doubles, and so modifying this data will result in\n        bogus results. The data are also copied if the kd-tree is built\n        with copy_data=True.\n    leafsize : positive int, optional\n        The number of points at which the algorithm switches over to\n        brute-force. Default: 16.\n    compact_nodes : bool, optional\n        If True, the kd-tree is built to shrink the hyperrectangles to\n        the actual data range. This usually gives a more compact tree that\n        is robust against degenerated input data and gives faster queries\n        at the expense of longer build time. Default: True.\n    copy_data : bool, optional\n        If True the data is always copied to protect the kd-tree against\n        data corruption. Default: False.\n    balanced_tree : bool, optional\n        If True, the median is used to split the hyperrectangles instead of\n        the midpoint. This usually gives a more compact tree and\n        faster queries at the expense of longer build time. Default: True.\n    boxsize : array_like or scalar, optional\n        Apply a m-d toroidal topology to the KDTree.. The topology is generated\n        by :math:`x_i + n_i L_i` where :math:`n_i` are integers and :math:`L_i`\n        is the boxsize along i-th dimension. The input data shall be wrapped\n        into :math:`[0, L_i)`. A ValueError is raised if any of the data is\n        outside of this bound.\n\n    Notes\n    -----\n    The algorithm used is described in Maneewongvatana and Mount 1999.\n    The general idea is that the kd-tree is a binary tree, each of whose\n    nodes represents an axis-aligned hyperrectangle. Each node specifies\n    an axis and splits the set of points based on whether their coordinate\n    along that axis is greater than or less than a particular value.\n\n    During construction, the axis and splitting point are chosen by the\n    "sliding midpoint" rule, which ensures that the cells do not all\n    become long and thin.\n\n    The tree can be queried for the r closest neighbors of any given point\n    (optionally returning only those within some maximum distance of the\n    point). It can also be queried, with a substantial gain in efficiency,\n    for the r approximate closest neighbors.\n\n    For large dimensions (20 is already large) do not expect this to run\n    significantly faster than brute force. High-dimensional nearest-neighbor\n    queries are a substantial open problem in computer science.\n\n    Attributes\n    ----------\n    data : ndarray, shape (n,m)\n        The n data points of dimension m to be indexed. This array is\n        not copied unless this is necessary to produce a contiguous\n        array of doubles. The data are also copied if the kd-tree is built\n        with `copy_data=True`.\n    leafsize : positive int\n        The number of points at which the algorithm switches over to\n        brute-force.\n    m : int\n        The dimension of a single data-point.\n    n : int\n        The number of data points.\n    maxes : ndarray, shape (m,)\n        The maximum value in each dimension of the n data points.\n    mins : ndarray, shape (m,)\n        The minimum value in each dimension of the n data points.\n    tree : object, class cKDTreeNode\n        This attribute exposes a Python view of the root node in the cKDTree\n        object. A full Python view of the kd-tree is created dynamically\n        on the first access. This attribute allows you to create your own\n        query functions in Python.\n    size : int\n        The number of nodes in the tree.\n\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    def __reduce_cython__(self) -> typing.Any:
        ...
    
    def __setstate__(self, state: typing.Any) -> None:
        ...
    
    def __setstate_cython__(self) -> typing.Any:
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def _build_weights(self, weights) -> typing.Any:
        '\n        _build_weights(weights)\n\n        Compute weights of nodes from weights of data points. This will sum\n        up the total weight per node. This function is used internally.\n\n        Parameters\n        ----------\n        weights : array_like\n            weights of data points; must be the same length as the data points.\n            currently only scalar weights are supported. Therefore the weights\n            array must be 1 dimensional.\n\n        Returns\n        -------\n        node_weights : array_like\n            total weight for each KD-Tree node.\n\n        '
        ...
    
    @property
    def boxsize(self) -> typing.Any:
        ...
    
    def count_neighbors(self, other, r, p=..., weights=..., cumulative=...) -> typing.Any:
        '\n        count_neighbors(self, other, r, p=2., weights=None, cumulative=True)\n\n        Count how many nearby pairs can be formed.\n\n        Count the number of pairs ``(x1,x2)`` can be formed, with ``x1`` drawn\n        from ``self`` and ``x2`` drawn from ``other``, and where\n        ``distance(x1, x2, p) <= r``.\n\n        Data points on ``self`` and ``other`` are optionally weighted by the\n        ``weights`` argument. (See below)\n\n        This is adapted from the "two-point correlation" algorithm described by\n        Gray and Moore [1]_.  See notes for further discussion.\n\n        Parameters\n        ----------\n        other : cKDTree instance\n            The other tree to draw points from, can be the same tree as self.\n        r : float or one-dimensional array of floats\n            The radius to produce a count for. Multiple radii are searched with\n            a single tree traversal.\n            If the count is non-cumulative(``cumulative=False``), ``r`` defines\n            the edges of the bins, and must be non-decreasing.\n        p : float, optional\n            1<=p<=infinity.\n            Which Minkowski p-norm to use.\n            Default 2.0.\n            A finite large p may cause a ValueError if overflow can occur.\n        weights : tuple, array_like, or None, optional\n            If None, the pair-counting is unweighted.\n            If given as a tuple, weights[0] is the weights of points in ``self``, and\n            weights[1] is the weights of points in ``other``; either can be None to\n            indicate the points are unweighted.\n            If given as an array_like, weights is the weights of points in ``self``\n            and ``other``. For this to make sense, ``self`` and ``other`` must be the\n            same tree. If ``self`` and ``other`` are two different trees, a ``ValueError``\n            is raised.\n            Default: None\n        cumulative : bool, optional\n            Whether the returned counts are cumulative. When cumulative is set to ``False``\n            the algorithm is optimized to work with a large number of bins (>10) specified\n            by ``r``. When ``cumulative`` is set to True, the algorithm is optimized to work\n            with a small number of ``r``. Default: True\n\n        Returns\n        -------\n        result : scalar or 1-D array\n            The number of pairs. For unweighted counts, the result is integer.\n            For weighted counts, the result is float.\n            If cumulative is False, ``result[i]`` contains the counts with\n            ``(-inf if i == 0 else r[i-1]) < R <= r[i]``\n\n        Notes\n        -----\n        Pair-counting is the basic operation used to calculate the two point\n        correlation functions from a data set composed of position of objects.\n\n        Two point correlation function measures the clustering of objects and\n        is widely used in cosmology to quantify the large scale structure\n        in our Universe, but it may be useful for data analysis in other fields\n        where self-similar assembly of objects also occur.\n\n        The Landy-Szalay estimator for the two point correlation function of\n        ``D`` measures the clustering signal in ``D``. [2]_\n\n        For example, given the position of two sets of objects,\n\n        - objects ``D`` (data) contains the clustering signal, and\n\n        - objects ``R`` (random) that contains no signal,\n\n        .. math::\n\n             \\xi(r) = \\frac{<D, D> - 2 f <D, R> + f^2<R, R>}{f^2<R, R>},\n\n        where the brackets represents counting pairs between two data sets\n        in a finite bin around ``r`` (distance), corresponding to setting\n        `cumulative=False`, and ``f = float(len(D)) / float(len(R))`` is the\n        ratio between number of objects from data and random.\n\n        The algorithm implemented here is loosely based on the dual-tree\n        algorithm described in [1]_. We switch between two different\n        pair-cumulation scheme depending on the setting of ``cumulative``.\n        The computing time of the method we use when for\n        ``cumulative == False`` does not scale with the total number of bins.\n        The algorithm for ``cumulative == True`` scales linearly with the\n        number of bins, though it is slightly faster when only\n        1 or 2 bins are used. [5]_.\n\n        As an extension to the naive pair-counting,\n        weighted pair-counting counts the product of weights instead\n        of number of pairs.\n        Weighted pair-counting is used to estimate marked correlation functions\n        ([3]_, section 2.2),\n        or to properly calculate the average of data per distance bin\n        (e.g. [4]_, section 2.1 on redshift).\n\n        .. [1] Gray and Moore,\n               "N-body problems in statistical learning",\n               Mining the sky, 2000, :arxiv:`astro-ph/0012333`\n\n        .. [2] Landy and Szalay,\n               "Bias and variance of angular correlation functions",\n               The Astrophysical Journal, 1993, :doi:`10.1086/172900`\n\n        .. [3] Sheth, Connolly and Skibba,\n               "Marked correlations in galaxy formation models",\n               2005, :arxiv:`astro-ph/0511773`\n\n        .. [4] Hawkins, et al.,\n               "The 2dF Galaxy Redshift Survey: correlation functions,\n               peculiar velocities and the matter density of the Universe",\n               Monthly Notices of the Royal Astronomical Society, 2002,\n               :doi:`10.1046/j.1365-2966.2003.07063.x`\n\n        .. [5] https://github.com/scipy/scipy/pull/5647#issuecomment-168474926\n\n        Examples\n        --------\n        You can count neighbors number between two kd-trees within a distance:\n\n        >>> import numpy as np\n        >>> from scipy.spatial import cKDTree\n        >>> np.random.seed(21701)\n        >>> points1 = np.random.random((5, 2))\n        >>> points2 = np.random.random((5, 2))\n        >>> kd_tree1 = cKDTree(points1)\n        >>> kd_tree2 = cKDTree(points2)\n        >>> kd_tree1.count_neighbors(kd_tree2, 0.2)\n        9\n\n        This number is same as the total pair number calculated by\n        `query_ball_tree`:\n\n        >>> indexes = kd_tree1.query_ball_tree(kd_tree2, r=0.2)\n        >>> sum([len(i) for i in indexes])\n        9\n\n        '
        ...
    
    @property
    def data(self) -> typing.Any:
        ...
    
    @property
    def indices(self) -> typing.Any:
        ...
    
    @property
    def leafsize(self) -> typing.Any:
        ...
    
    @property
    def m(self) -> typing.Any:
        ...
    
    @property
    def maxes(self) -> typing.Any:
        ...
    
    @property
    def mins(self) -> typing.Any:
        ...
    
    @property
    def n(self) -> typing.Any:
        ...
    
    def query(self, x, k=..., eps=..., p=..., distance_upper_bound=..., workers=...) -> typing.Any:
        '\n        query(self, x, k=1, eps=0, p=2, distance_upper_bound=np.inf, workers=1)\n\n        Query the kd-tree for nearest neighbors\n\n        Parameters\n        ----------\n        x : array_like, last dimension self.m\n            An array of points to query.\n        k : list of integer or integer\n            The list of k-th nearest neighbors to return. If k is an\n            integer it is treated as a list of [1, ... k] (range(1, k+1)).\n            Note that the counting starts from 1.\n        eps : non-negative float\n            Return approximate nearest neighbors; the k-th returned value\n            is guaranteed to be no further than (1+eps) times the\n            distance to the real k-th nearest neighbor.\n        p : float, 1<=p<=infinity\n            Which Minkowski p-norm to use.\n            1 is the sum-of-absolute-values "Manhattan" distance\n            2 is the usual Euclidean distance\n            infinity is the maximum-coordinate-difference distance\n            A finite large p may cause a ValueError if overflow can occur.\n        distance_upper_bound : nonnegative float\n            Return only neighbors within this distance.  This is used to prune\n            tree searches, so if you are doing a series of nearest-neighbor\n            queries, it may help to supply the distance to the nearest neighbor\n            of the most recent point.\n        workers : int, optional\n            Number of workers to use for parallel processing. If -1 is given\n            all CPU threads are used. Default: 1.\n\n            .. versionchanged:: 1.6.0\n               The "n_jobs" argument was renamed "workers". The old name\n               "n_jobs" is deprecated and will stop working in SciPy 1.8.0.\n\n        Returns\n        -------\n        d : array of floats\n            The distances to the nearest neighbors.\n            If ``x`` has shape ``tuple+(self.m,)``, then ``d`` has shape ``tuple+(k,)``.\n            When k == 1, the last dimension of the output is squeezed.\n            Missing neighbors are indicated with infinite distances.\n        i : ndarray of ints\n            The index of each neighbor in ``self.data``.\n            If ``x`` has shape ``tuple+(self.m,)``, then ``i`` has shape ``tuple+(k,)``.\n            When k == 1, the last dimension of the output is squeezed.\n            Missing neighbors are indicated with ``self.n``.\n\n        Notes\n        -----\n        If the KD-Tree is periodic, the position ``x`` is wrapped into the\n        box.\n\n        When the input k is a list, a query for arange(max(k)) is performed, but\n        only columns that store the requested values of k are preserved. This is\n        implemented in a manner that reduces memory usage.\n\n        Examples\n        --------\n\n        >>> import numpy as np\n        >>> from scipy.spatial import cKDTree\n        >>> x, y = np.mgrid[0:5, 2:8]\n        >>> tree = cKDTree(np.c_[x.ravel(), y.ravel()])\n\n        To query the nearest neighbours and return squeezed result, use\n\n        >>> dd, ii = tree.query([[0, 0], [2.1, 2.9]], k=1)\n        >>> print(dd, ii)\n        [2.         0.14142136] [ 0 13]\n\n        To query the nearest neighbours and return unsqueezed result, use\n\n        >>> dd, ii = tree.query([[0, 0], [2.1, 2.9]], k=[1])\n        >>> print(dd, ii)\n        [[2.        ]\n         [0.14142136]] [[ 0]\n         [13]]\n\n        To query the second nearest neighbours and return unsqueezed result, use\n\n        >>> dd, ii = tree.query([[0, 0], [2.1, 2.9]], k=[2])\n        >>> print(dd, ii)\n        [[2.23606798]\n         [0.90553851]] [[ 6]\n         [12]]\n\n        To query the first and second nearest neighbours, use\n\n        >>> dd, ii = tree.query([[0, 0], [2.1, 2.9]], k=2)\n        >>> print(dd, ii)\n        [[2.         2.23606798]\n         [0.14142136 0.90553851]] [[ 0  6]\n         [13 12]]\n\n        or, be more specific\n\n        >>> dd, ii = tree.query([[0, 0], [2.1, 2.9]], k=[1, 2])\n        >>> print(dd, ii)\n        [[2.         2.23606798]\n         [0.14142136 0.90553851]] [[ 0  6]\n         [13 12]]\n\n        '
        ...
    
    def query_ball_point(self, x, r, p=..., eps=..., workers=..., return_sorted=..., return_length=...) -> typing.Any:
        '\n        query_ball_point(self, x, r, p=2., eps=0, workers=1, return_sorted=None,\n                         return_length=False)\n\n        Find all points within distance r of point(s) x.\n\n        Parameters\n        ----------\n        x : array_like, shape tuple + (self.m,)\n            The point or points to search for neighbors of.\n        r : array_like, float\n            The radius of points to return, shall broadcast to the length of x.\n        p : float, optional\n            Which Minkowski p-norm to use.  Should be in the range [1, inf].\n            A finite large p may cause a ValueError if overflow can occur.\n        eps : nonnegative float, optional\n            Approximate search. Branches of the tree are not explored if their\n            nearest points are further than ``r / (1 + eps)``, and branches are\n            added in bulk if their furthest points are nearer than\n            ``r * (1 + eps)``.\n        workers : int, optional\n            Number of jobs to schedule for parallel processing. If -1 is given\n            all processors are used. Default: 1.\n\n            .. versionchanged:: 1.6.0\n               The "n_jobs" argument was renamed "workers". The old name\n               "n_jobs" is deprecated and will stop working in SciPy 1.8.0.\n\n        return_sorted : bool, optional\n            Sorts returned indicies if True and does not sort them if False. If\n            None, does not sort single point queries, but does sort\n            multi-point queries which was the behavior before this option\n            was added.\n\n            .. versionadded:: 1.2.0\n        return_length: bool, optional\n            Return the number of points inside the radius instead of a list\n            of the indices.\n            .. versionadded:: 1.3.0\n\n        Returns\n        -------\n        results : list or array of lists\n            If `x` is a single point, returns a list of the indices of the\n            neighbors of `x`. If `x` is an array of points, returns an object\n            array of shape tuple containing lists of neighbors.\n\n        Notes\n        -----\n        If you have many points whose neighbors you want to find, you may save\n        substantial amounts of time by putting them in a cKDTree and using\n        query_ball_tree.\n\n        Examples\n        --------\n        >>> from scipy import spatial\n        >>> x, y = np.mgrid[0:4, 0:4]\n        >>> points = np.c_[x.ravel(), y.ravel()]\n        >>> tree = spatial.cKDTree(points)\n        >>> tree.query_ball_point([2, 0], 1)\n        [4, 8, 9, 12]\n\n        Query multiple points and plot the results:\n\n        >>> import matplotlib.pyplot as plt\n        >>> points = np.asarray(points)\n        >>> plt.plot(points[:,0], points[:,1], \'.\')\n        >>> for results in tree.query_ball_point(([2, 0], [3, 3]), 1):\n        ...     nearby_points = points[results]\n        ...     plt.plot(nearby_points[:,0], nearby_points[:,1], \'o\')\n        >>> plt.margins(0.1, 0.1)\n        >>> plt.show()\n\n        '
        ...
    
    def query_ball_tree(self, other, r, p=..., eps=...) -> typing.Any:
        '\n        query_ball_tree(self, other, r, p=2., eps=0)\n\n        Find all pairs of points between `self` and `other` whose distance is at most r\n\n        Parameters\n        ----------\n        other : cKDTree instance\n            The tree containing points to search against.\n        r : float\n            The maximum distance, has to be positive.\n        p : float, optional\n            Which Minkowski norm to use.  `p` has to meet the condition\n            ``1 <= p <= infinity``.\n            A finite large p may cause a ValueError if overflow can occur.\n        eps : float, optional\n            Approximate search.  Branches of the tree are not explored\n            if their nearest points are further than ``r/(1+eps)``, and\n            branches are added in bulk if their furthest points are nearer\n            than ``r * (1+eps)``.  `eps` has to be non-negative.\n\n        Returns\n        -------\n        results : list of lists\n            For each element ``self.data[i]`` of this tree, ``results[i]`` is a\n            list of the indices of its neighbors in ``other.data``.\n\n        Examples\n        --------\n        You can search all pairs of points between two kd-trees within a distance:\n\n        >>> import matplotlib.pyplot as plt\n        >>> import numpy as np\n        >>> from scipy.spatial import cKDTree\n        >>> np.random.seed(21701)\n        >>> points1 = np.random.random((15, 2))\n        >>> points2 = np.random.random((15, 2))\n        >>> plt.figure(figsize=(6, 6))\n        >>> plt.plot(points1[:, 0], points1[:, 1], "xk", markersize=14)\n        >>> plt.plot(points2[:, 0], points2[:, 1], "og", markersize=14)\n        >>> kd_tree1 = cKDTree(points1)\n        >>> kd_tree2 = cKDTree(points2)\n        >>> indexes = kd_tree1.query_ball_tree(kd_tree2, r=0.2)\n        >>> for i in range(len(indexes)):\n        ...     for j in indexes[i]:\n        ...         plt.plot([points1[i, 0], points2[j, 0]],\n        ...             [points1[i, 1], points2[j, 1]], "-r")\n        >>> plt.show()\n\n        '
        ...
    
    def query_pairs(self, r, p=..., eps=...) -> typing.Any:
        '\n        query_pairs(self, r, p=2., eps=0)\n\n        Find all pairs of points in `self` whose distance is at most r.\n\n        Parameters\n        ----------\n        r : positive float\n            The maximum distance.\n        p : float, optional\n            Which Minkowski norm to use.  ``p`` has to meet the condition\n            ``1 <= p <= infinity``.\n            A finite large p may cause a ValueError if overflow can occur.\n        eps : float, optional\n            Approximate search.  Branches of the tree are not explored\n            if their nearest points are further than ``r/(1+eps)``, and\n            branches are added in bulk if their furthest points are nearer\n            than ``r * (1+eps)``.  `eps` has to be non-negative.\n        output_type : string, optional\n            Choose the output container, \'set\' or \'ndarray\'. Default: \'set\'\n\n        Returns\n        -------\n        results : set or ndarray\n            Set of pairs ``(i,j)``, with ``i < j``, for which the corresponding\n            positions are close. If output_type is \'ndarray\', an ndarry is\n            returned instead of a set.\n\n        Examples\n        --------\n        You can search all pairs of points in a kd-tree within a distance:\n\n        >>> import matplotlib.pyplot as plt\n        >>> import numpy as np\n        >>> from scipy.spatial import cKDTree\n        >>> np.random.seed(21701)\n        >>> points = np.random.random((20, 2))\n        >>> plt.figure(figsize=(6, 6))\n        >>> plt.plot(points[:, 0], points[:, 1], "xk", markersize=14)\n        >>> kd_tree = cKDTree(points)\n        >>> pairs = kd_tree.query_pairs(r=0.2)\n        >>> for (i, j) in pairs:\n        ...     plt.plot([points[i, 0], points[j, 0]],\n        ...             [points[i, 1], points[j, 1]], "-r")\n        >>> plt.show()\n\n        '
        ...
    
    @property
    def size(self) -> typing.Any:
        ...
    
    def sparse_distance_matrix(self, other, max_distance, p=...) -> typing.Any:
        '\n        sparse_distance_matrix(self, other, max_distance, p=2.)\n\n        Compute a sparse distance matrix\n\n        Computes a distance matrix between two cKDTrees, leaving as zero\n        any distance greater than max_distance.\n\n        Parameters\n        ----------\n        other : cKDTree\n\n        max_distance : positive float\n\n        p : float, 1<=p<=infinity\n            Which Minkowski p-norm to use.\n            A finite large p may cause a ValueError if overflow can occur.\n\n        output_type : string, optional\n            Which container to use for output data. Options: \'dok_matrix\',\n            \'coo_matrix\', \'dict\', or \'ndarray\'. Default: \'dok_matrix\'.\n\n        Returns\n        -------\n        result : dok_matrix, coo_matrix, dict or ndarray\n            Sparse matrix representing the results in "dictionary of keys"\n            format. If a dict is returned the keys are (i,j) tuples of indices.\n            If output_type is \'ndarray\' a record array with fields \'i\', \'j\',\n            and \'v\' is returned,\n\n        Examples\n        --------\n        You can compute a sparse distance matrix between two kd-trees:\n\n        >>> import numpy as np\n        >>> from scipy.spatial import cKDTree\n        >>> np.random.seed(21701)\n        >>> points1 = np.random.random((5, 2))\n        >>> points2 = np.random.random((5, 2))\n        >>> kd_tree1 = cKDTree(points1)\n        >>> kd_tree2 = cKDTree(points2)\n        >>> sdm = kd_tree1.sparse_distance_matrix(kd_tree2, 0.3)\n        >>> sdm.toarray()\n        array([[0.20220215, 0.14538496, 0.,         0.10257199, 0.        ],\n            [0.13491385, 0.27251306, 0.,         0.18793787, 0.        ],\n            [0.19262396, 0.,         0.,         0.25795122, 0.        ],\n            [0.14859639, 0.07076002, 0.,         0.04065851, 0.        ],\n            [0.17308768, 0.,         0.,         0.24823138, 0.        ]])\n\n        You can check distances above the `max_distance` are zeros:\n\n        >>> from scipy.spatial import distance_matrix\n        >>> distance_matrix(points1, points2)\n        array([[0.20220215, 0.14538496, 0.43588092, 0.10257199, 0.4555495 ],\n            [0.13491385, 0.27251306, 0.65944131, 0.18793787, 0.68184154],\n            [0.19262396, 0.34121593, 0.72176889, 0.25795122, 0.74538858],\n            [0.14859639, 0.07076002, 0.48505773, 0.04065851, 0.50043591],\n            [0.17308768, 0.32837991, 0.72760803, 0.24823138, 0.75017239]])\n\n        '
        ...
    
    @property
    def tree(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class cKDTreeNode(_mod_builtins.object):
    "\n    class cKDTreeNode\n\n    This class exposes a Python view of a node in the cKDTree object.\n\n    All attributes are read-only.\n\n    Attributes\n    ----------\n    level : int\n        The depth of the node. 0 is the level of the root node.\n    split_dim : int\n        The dimension along which this node is split. If this value is -1\n        the node is a leafnode in the kd-tree. Leafnodes are not split further\n        and scanned by brute force.\n    split : float\n        The value used to separate split this node. Points with value >= split\n        in the split_dim dimension are sorted to the 'greater' subnode\n        whereas those with value < split are sorted to the 'lesser' subnode.\n    children : int\n        The number of data points sorted to this node.\n    data_points : ndarray of float64\n        An array with the data points sorted to this node.\n    indices : ndarray of intp\n        An array with the indices of the data points sorted to this node. The\n        indices refer to the position in the data set used to construct the\n        kd-tree.\n    lesser : cKDTreeNode or None\n        Subnode with the 'lesser' data points. This attribute is None for\n        leafnodes.\n    greater : cKDTreeNode or None\n        Subnode with the 'greater' data points. This attribute is None for\n        leafnodes.\n\n    "
    def __init__(self, *args, **kwargs) -> None:
        "\n    class cKDTreeNode\n\n    This class exposes a Python view of a node in the cKDTree object.\n\n    All attributes are read-only.\n\n    Attributes\n    ----------\n    level : int\n        The depth of the node. 0 is the level of the root node.\n    split_dim : int\n        The dimension along which this node is split. If this value is -1\n        the node is a leafnode in the kd-tree. Leafnodes are not split further\n        and scanned by brute force.\n    split : float\n        The value used to separate split this node. Points with value >= split\n        in the split_dim dimension are sorted to the 'greater' subnode\n        whereas those with value < split are sorted to the 'lesser' subnode.\n    children : int\n        The number of data points sorted to this node.\n    data_points : ndarray of float64\n        An array with the data points sorted to this node.\n    indices : ndarray of intp\n        An array with the indices of the data points sorted to this node. The\n        indices refer to the position in the data set used to construct the\n        kd-tree.\n    lesser : cKDTreeNode or None\n        Subnode with the 'lesser' data points. This attribute is None for\n        leafnodes.\n    greater : cKDTreeNode or None\n        Subnode with the 'greater' data points. This attribute is None for\n        leafnodes.\n\n    "
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
    
    @property
    def children(self) -> typing.Any:
        ...
    
    @property
    def data_points(self) -> typing.Any:
        ...
    
    @property
    def end_idx(self) -> typing.Any:
        ...
    
    @property
    def greater(self) -> typing.Any:
        ...
    
    @property
    def indices(self) -> typing.Any:
        ...
    
    @property
    def lesser(self) -> typing.Any:
        ...
    
    @property
    def level(self) -> typing.Any:
        ...
    
    @property
    def split(self) -> typing.Any:
        ...
    
    @property
    def split_dim(self) -> typing.Any:
        ...
    
    @property
    def start_idx(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class coo_entries(_mod_builtins.object):
    @property
    def __array_interface__(self) -> typing.Any:
        ...
    
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __reduce__(self) -> typing.Union[str, typing.Tuple[typing.Any, ...]]:
        ...
    
    def __setstate__(self, state: typing.Any) -> None:
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def coo_matrix(self) -> typing.Any:
        ...
    
    def dict(self) -> typing.Any:
        ...
    
    def dok_matrix(self) -> typing.Any:
        ...
    
    def ndarray(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class ordered_pairs(_mod_builtins.object):
    @property
    def __array_interface__(self) -> typing.Any:
        ...
    
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __reduce__(self) -> typing.Union[str, typing.Tuple[typing.Any, ...]]:
        ...
    
    def __setstate__(self, state: typing.Any) -> None:
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def ndarray(self) -> typing.Any:
        ...
    
    def set(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

def __getattr__(name) -> typing.Any:
    ...

