# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: scipy, version: 1.6.2
# Module: scipy.interpolate.interpnd, version: unspecified
import typing
import builtins as _mod_builtins

class CloughTocher2DInterpolator(NDInterpolatorBase):
    '\n    CloughTocher2DInterpolator(points, values, tol=1e-6)\n\n    Piecewise cubic, C1 smooth, curvature-minimizing interpolant in 2D.\n\n    .. versionadded:: 0.9\n\n    Methods\n    -------\n    __call__\n\n    Parameters\n    ----------\n    points : ndarray of floats, shape (npoints, ndims); or Delaunay\n        Data point coordinates, or a precomputed Delaunay triangulation.\n    values : ndarray of float or complex, shape (npoints, ...)\n        Data values.\n    fill_value : float, optional\n        Value used to fill in for requested points outside of the\n        convex hull of the input points.  If not provided, then\n        the default is ``nan``.\n    tol : float, optional\n        Absolute/relative tolerance for gradient estimation.\n    maxiter : int, optional\n        Maximum number of iterations in gradient estimation.\n    rescale : bool, optional\n        Rescale points to unit cube before performing interpolation.\n        This is useful if some of the input dimensions have\n        incommensurable units and differ by many orders of magnitude.\n\n    Notes\n    -----\n    The interpolant is constructed by triangulating the input data\n    with Qhull [1]_, and constructing a piecewise cubic\n    interpolating Bezier polynomial on each triangle, using a\n    Clough-Tocher scheme [CT]_.  The interpolant is guaranteed to be\n    continuously differentiable.\n\n    The gradients of the interpolant are chosen so that the curvature\n    of the interpolating surface is approximatively minimized. The\n    gradients necessary for this are estimated using the global\n    algorithm described in [Nielson83]_ and [Renka84]_.\n\n    Examples\n    --------\n    We can interpolate values on a 2D plane:\n\n    >>> from scipy.interpolate import CloughTocher2DInterpolator\n    >>> import matplotlib.pyplot as plt\n    >>> np.random.seed(0)\n    >>> x = np.random.random(10) - 0.5\n    >>> y = np.random.random(10) - 0.5\n    >>> z = np.hypot(x, y)\n    >>> X = np.linspace(min(x), max(x))\n    >>> Y = np.linspace(min(y), max(y))\n    >>> X, Y = np.meshgrid(X, Y)  # 2D grid for interpolation\n    >>> interp = CloughTocher2DInterpolator(list(zip(x, y)), z)\n    >>> Z = interp(X, Y)\n    >>> plt.pcolormesh(X, Y, Z, shading=\'auto\')\n    >>> plt.plot(x, y, "ok", label="input point")\n    >>> plt.legend()\n    >>> plt.colorbar()\n    >>> plt.axis("equal")\n    >>> plt.show()\n\n    See also\n    --------\n    griddata :\n        Interpolate unstructured D-D data.\n    LinearNDInterpolator :\n        Piecewise linear interpolant in N dimensions.\n    NearestNDInterpolator :\n        Nearest-neighbor interpolation in N dimensions.\n\n    References\n    ----------\n    .. [1] http://www.qhull.org/\n\n    .. [CT] See, for example,\n       P. Alfeld,\n       \'\'A trivariate Clough-Tocher scheme for tetrahedral data\'\'.\n       Computer Aided Geometric Design, 1, 169 (1984);\n       G. Farin,\n       \'\'Triangular Bernstein-Bezier patches\'\'.\n       Computer Aided Geometric Design, 3, 83 (1986).\n\n    .. [Nielson83] G. Nielson,\n       \'\'A method for interpolating scattered data based upon a minimum norm\n       network\'\'.\n       Math. Comp., 40, 253 (1983).\n\n    .. [Renka84] R. J. Renka and A. K. Cline.\n       \'\'A Triangle-based C1 interpolation method.\'\',\n       Rocky Mountain J. Math., 14, 223 (1984).\n\n    '
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, points, values, tol=...) -> None:
        '\n    CloughTocher2DInterpolator(points, values, tol=1e-6)\n\n    Piecewise cubic, C1 smooth, curvature-minimizing interpolant in 2D.\n\n    .. versionadded:: 0.9\n\n    Methods\n    -------\n    __call__\n\n    Parameters\n    ----------\n    points : ndarray of floats, shape (npoints, ndims); or Delaunay\n        Data point coordinates, or a precomputed Delaunay triangulation.\n    values : ndarray of float or complex, shape (npoints, ...)\n        Data values.\n    fill_value : float, optional\n        Value used to fill in for requested points outside of the\n        convex hull of the input points.  If not provided, then\n        the default is ``nan``.\n    tol : float, optional\n        Absolute/relative tolerance for gradient estimation.\n    maxiter : int, optional\n        Maximum number of iterations in gradient estimation.\n    rescale : bool, optional\n        Rescale points to unit cube before performing interpolation.\n        This is useful if some of the input dimensions have\n        incommensurable units and differ by many orders of magnitude.\n\n    Notes\n    -----\n    The interpolant is constructed by triangulating the input data\n    with Qhull [1]_, and constructing a piecewise cubic\n    interpolating Bezier polynomial on each triangle, using a\n    Clough-Tocher scheme [CT]_.  The interpolant is guaranteed to be\n    continuously differentiable.\n\n    The gradients of the interpolant are chosen so that the curvature\n    of the interpolating surface is approximatively minimized. The\n    gradients necessary for this are estimated using the global\n    algorithm described in [Nielson83]_ and [Renka84]_.\n\n    Examples\n    --------\n    We can interpolate values on a 2D plane:\n\n    >>> from scipy.interpolate import CloughTocher2DInterpolator\n    >>> import matplotlib.pyplot as plt\n    >>> np.random.seed(0)\n    >>> x = np.random.random(10) - 0.5\n    >>> y = np.random.random(10) - 0.5\n    >>> z = np.hypot(x, y)\n    >>> X = np.linspace(min(x), max(x))\n    >>> Y = np.linspace(min(y), max(y))\n    >>> X, Y = np.meshgrid(X, Y)  # 2D grid for interpolation\n    >>> interp = CloughTocher2DInterpolator(list(zip(x, y)), z)\n    >>> Z = interp(X, Y)\n    >>> plt.pcolormesh(X, Y, Z, shading=\'auto\')\n    >>> plt.plot(x, y, "ok", label="input point")\n    >>> plt.legend()\n    >>> plt.colorbar()\n    >>> plt.axis("equal")\n    >>> plt.show()\n\n    See also\n    --------\n    griddata :\n        Interpolate unstructured D-D data.\n    LinearNDInterpolator :\n        Piecewise linear interpolant in N dimensions.\n    NearestNDInterpolator :\n        Nearest-neighbor interpolation in N dimensions.\n\n    References\n    ----------\n    .. [1] http://www.qhull.org/\n\n    .. [CT] See, for example,\n       P. Alfeld,\n       \'\'A trivariate Clough-Tocher scheme for tetrahedral data\'\'.\n       Computer Aided Geometric Design, 1, 169 (1984);\n       G. Farin,\n       \'\'Triangular Bernstein-Bezier patches\'\'.\n       Computer Aided Geometric Design, 3, 83 (1986).\n\n    .. [Nielson83] G. Nielson,\n       \'\'A method for interpolating scattered data based upon a minimum norm\n       network\'\'.\n       Math. Comp., 40, 253 (1983).\n\n    .. [Renka84] R. J. Renka and A. K. Cline.\n       \'\'A Triangle-based C1 interpolation method.\'\',\n       Rocky Mountain J. Math., 14, 223 (1984).\n\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def _do_evaluate(self, xi, dummy) -> typing.Any:
        ...
    
    def _evaluate_complex(self, xi) -> typing.Any:
        ...
    
    def _evaluate_double(self, xi) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class GradientEstimationWarning(_mod_builtins.Warning):
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __module__: str
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
    

class LinearNDInterpolator(NDInterpolatorBase):
    '\n    LinearNDInterpolator(points, values, fill_value=np.nan, rescale=False)\n\n    Piecewise linear interpolant in N dimensions.\n\n    .. versionadded:: 0.9\n\n    Methods\n    -------\n    __call__\n\n    Parameters\n    ----------\n    points : ndarray of floats, shape (npoints, ndims); or Delaunay\n        Data point coordinates, or a precomputed Delaunay triangulation.\n    values : ndarray of float or complex, shape (npoints, ...)\n        Data values.\n    fill_value : float, optional\n        Value used to fill in for requested points outside of the\n        convex hull of the input points.  If not provided, then\n        the default is ``nan``.\n    rescale : bool, optional\n        Rescale points to unit cube before performing interpolation.\n        This is useful if some of the input dimensions have\n        incommensurable units and differ by many orders of magnitude.\n\n    Notes\n    -----\n    The interpolant is constructed by triangulating the input data\n    with Qhull [1]_, and on each triangle performing linear\n    barycentric interpolation.\n\n    Examples\n    --------\n    We can interpolate values on a 2D plane:\n\n    >>> from scipy.interpolate import LinearNDInterpolator\n    >>> import matplotlib.pyplot as plt\n    >>> np.random.seed(0)\n    >>> x = np.random.random(10) - 0.5\n    >>> y = np.random.random(10) - 0.5\n    >>> z = np.hypot(x, y)\n    >>> X = np.linspace(min(x), max(x))\n    >>> Y = np.linspace(min(y), max(y))\n    >>> X, Y = np.meshgrid(X, Y)  # 2D grid for interpolation\n    >>> interp = LinearNDInterpolator(list(zip(x, y)), z)\n    >>> Z = interp(X, Y)\n    >>> plt.pcolormesh(X, Y, Z, shading=\'auto\')\n    >>> plt.plot(x, y, "ok", label="input point")\n    >>> plt.legend()\n    >>> plt.colorbar()\n    >>> plt.axis("equal")\n    >>> plt.show()\n\n    See also\n    --------\n    griddata :\n        Interpolate unstructured D-D data.\n    NearestNDInterpolator :\n        Nearest-neighbor interpolation in N dimensions.\n    CloughTocher2DInterpolator :\n        Piecewise cubic, C1 smooth, curvature-minimizing interpolant in 2D.\n\n    References\n    ----------\n    .. [1] http://www.qhull.org/\n\n    '
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, points, values, fill_value=..., rescale=...) -> None:
        '\n    LinearNDInterpolator(points, values, fill_value=np.nan, rescale=False)\n\n    Piecewise linear interpolant in N dimensions.\n\n    .. versionadded:: 0.9\n\n    Methods\n    -------\n    __call__\n\n    Parameters\n    ----------\n    points : ndarray of floats, shape (npoints, ndims); or Delaunay\n        Data point coordinates, or a precomputed Delaunay triangulation.\n    values : ndarray of float or complex, shape (npoints, ...)\n        Data values.\n    fill_value : float, optional\n        Value used to fill in for requested points outside of the\n        convex hull of the input points.  If not provided, then\n        the default is ``nan``.\n    rescale : bool, optional\n        Rescale points to unit cube before performing interpolation.\n        This is useful if some of the input dimensions have\n        incommensurable units and differ by many orders of magnitude.\n\n    Notes\n    -----\n    The interpolant is constructed by triangulating the input data\n    with Qhull [1]_, and on each triangle performing linear\n    barycentric interpolation.\n\n    Examples\n    --------\n    We can interpolate values on a 2D plane:\n\n    >>> from scipy.interpolate import LinearNDInterpolator\n    >>> import matplotlib.pyplot as plt\n    >>> np.random.seed(0)\n    >>> x = np.random.random(10) - 0.5\n    >>> y = np.random.random(10) - 0.5\n    >>> z = np.hypot(x, y)\n    >>> X = np.linspace(min(x), max(x))\n    >>> Y = np.linspace(min(y), max(y))\n    >>> X, Y = np.meshgrid(X, Y)  # 2D grid for interpolation\n    >>> interp = LinearNDInterpolator(list(zip(x, y)), z)\n    >>> Z = interp(X, Y)\n    >>> plt.pcolormesh(X, Y, Z, shading=\'auto\')\n    >>> plt.plot(x, y, "ok", label="input point")\n    >>> plt.legend()\n    >>> plt.colorbar()\n    >>> plt.axis("equal")\n    >>> plt.show()\n\n    See also\n    --------\n    griddata :\n        Interpolate unstructured D-D data.\n    NearestNDInterpolator :\n        Nearest-neighbor interpolation in N dimensions.\n    CloughTocher2DInterpolator :\n        Piecewise cubic, C1 smooth, curvature-minimizing interpolant in 2D.\n\n    References\n    ----------\n    .. [1] http://www.qhull.org/\n\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def _do_evaluate(self, xi, dummy) -> typing.Any:
        ...
    
    def _evaluate_complex(self, xi) -> typing.Any:
        ...
    
    def _evaluate_double(self, xi) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class NDInterpolatorBase(_mod_builtins.object):
    '\n    Common routines for interpolators.\n\n    .. versionadded:: 0.9\n\n    '
    def __call__(self, *args) -> typing.Any:
        '\n        interpolator(xi)\n\n        Evaluate interpolator at given points.\n\n        Parameters\n        ----------\n        x1, x2, ... xn: array-like of float\n            Points where to interpolate data at.\n            x1, x2, ... xn can be array-like of float with broadcastable shape.\n            or x1 can be array-like of float with shape ``(..., ndim)``\n\n        '
        ...
    
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, points, values, fill_value, ndim, rescale, need_contiguous, need_values) -> None:
        '\n        Check shape of points and values arrays, and reshape values to\n        (npoints, nvalues).  Ensure the `points` and values arrays are\n        C-contiguous, and of correct type.\n        '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __module__: str
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @property
    def __weakref__(self) -> typing.Any:
        'list of weak references to the object (if defined)'
        ...
    
    def _check_call_shape(self, xi) -> typing.Any:
        ...
    
    def _scale_x(self, xi) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

__doc__: str
__file__: str
__name__: str
__package__: str
def __pyx_unpickle_Enum() -> typing.Any:
    ...

__test__: dict
def _ndim_coords_from_arrays() -> typing.Any:
    '\n    Convert a tuple of coordinate arrays to a (..., ndim)-shaped array.\n\n    '
    ...

def estimate_gradients_2d_global() -> typing.Any:
    ...

def __getattr__(name) -> typing.Any:
    ...

