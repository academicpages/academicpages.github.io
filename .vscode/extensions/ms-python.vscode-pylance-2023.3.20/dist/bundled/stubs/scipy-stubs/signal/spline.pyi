# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: scipy, version: 1.6.2
# Module: scipy.signal.spline, version: 0.2
import typing
import builtins as _mod_builtins

__doc__: typing.Any
__file__: str
__name__: str
__package__: str
__version__: str
def cspline2d(input, lambda_=..., precision=...) -> typing.Any:
    'out = cspline2d(input, lambda=0.0, precision=-1.0)\n\n    Coefficients for 2-D cubic (3rd order) B-spline.\n\n    Return the third-order B-spline coefficients over a regularly spaced\n    input grid for the two-dimensional input image.\n\n    Parameters\n    ----------\n    input : ndarray\n        The input signal.\n    lambda : float\n        Specifies the amount of smoothing in the transfer function.\n    precision : float\n        Specifies the precision for computing the infinite sum needed to apply mirror-\n        symmetric boundary conditions.\n\n    Returns\n    -------\n    output : ndarray\n        The filtered signal.\n\n    Examples\n    --------\n    Examples are given :ref:`in the tutorial <tutorial-signal-bsplines>`.\n\n'
    ...

def qspline2d(input, lambda_=..., precision=...) -> typing.Any:
    'out = qspline2d(input, lambda=0.0, precision=-1.0)\n\n    Coefficients for 2-D quadratic (2nd order) B-spline:\n\n    Return the second-order B-spline coefficients over a regularly spaced\n    input grid for the two-dimensional input image.\n\n    Parameters\n    ----------\n    input : ndarray\n        The input signal.\n    lambda : float\n        Specifies the amount of smoothing in the transfer function.\n    precision : float\n        Specifies the precision for computing the infinite sum needed to apply mirror-\n        symmetric boundary conditions.\n\n    Returns\n    -------\n    output : ndarray\n        The filtered signal.\n\n    Examples\n    --------\n    Examples are given :ref:`in the tutorial <tutorial-signal-bsplines>`.\n\n'
    ...

def sepfir2d(input, hrow, hcol) -> typing.Any:
    'out = sepfir2d(input, hrow, hcol)\n\n    Convolve with a 2-D separable FIR filter.\n\n    Convolve the rank-2 input array with the separable filter defined by the\n    rank-1 arrays hrow, and hcol. Mirror symmetric boundary conditions are\n    assumed. This function can be used to find an image given its B-spline\n    representation.\n\n    Parameters\n    ----------\n    input : ndarray\n        The input signal. Must be a rank-2 array.\n    hrow : ndarray\n        A rank-1 array defining the row direction of the filter.\n        Must be odd-length\n    hcol : ndarray\n        A rank-1 array defining the column direction of the filter.\n        Must be odd-length\n\n    Returns\n    -------\n    output : ndarray\n        The filtered signal.\n\n    Examples\n    --------\n    Examples are given :ref:`in the tutorial <tutorial-signal-bsplines>`.\n\n'
    ...

def symiirorder1(input, c0, z1, precision=...) -> typing.Any:
    'out = symiirorder1(input, c0, z1, precision=-1.0)\n\n    Implement a smoothing IIR filter with mirror-symmetric boundary conditions\n    using a cascade of first-order sections.  The second section uses a\n    reversed sequence.  This implements a system with the following\n    transfer function and mirror-symmetric boundary conditions::\n\n                           c0              \n           H(z) = ---------------------    \n                   (1-z1/z) (1 - z1 z)     \n\n    The resulting signal will have mirror symmetric boundary conditions as well.\n\n    Parameters\n    ----------\n    input : ndarray\n        The input signal.\n    c0, z1 : scalar\n        Parameters in the transfer function.\n    precision :\n        Specifies the precision for calculating initial conditions\n        of the recursive filter based on mirror-symmetric input.\n\n    Returns\n    -------\n    output : ndarray\n        The filtered signal.'
    ...

def symiirorder2(input, r, omega, precision=...) -> typing.Any:
    'out = symiirorder2(input, r, omega, precision=-1.0)\n\n    Implement a smoothing IIR filter with mirror-symmetric boundary conditions\n    using a cascade of second-order sections.  The second section uses a\n    reversed sequence.  This implements the following transfer function::\n\n                                  cs^2\n         H(z) = ---------------------------------------\n                (1 - a2/z - a3/z^2) (1 - a2 z - a3 z^2 )\n\n    where::\n\n          a2 = (2 r cos omega)\n          a3 = - r^2\n          cs = 1 - 2 r cos omega + r^2\n\n    Parameters\n    ----------\n    input : ndarray\n        The input signal.\n    r, omega : float\n        Parameters in the transfer function.\n    precision : float\n        Specifies the precision for calculating initial conditions\n        of the recursive filter based on mirror-symmetric input.\n\n    Returns\n    -------\n    output : ndarray\n        The filtered signal.'
    ...

def __getattr__(name) -> typing.Any:
    ...

