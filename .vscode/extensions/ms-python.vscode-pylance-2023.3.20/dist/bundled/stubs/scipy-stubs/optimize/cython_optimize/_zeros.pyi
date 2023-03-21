# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: scipy, version: 1.6.2
# Module: scipy.optimize.cython_optimize._zeros, version: unspecified
import typing
import builtins as _mod_builtins

EXAMPLES_MAP: dict
__doc__: str
__file__: str
__name__: str
__package__: str
__pyx_capi__: dict
__test__: dict
def full_output_example() -> typing.Any:
    '\n    Example of Cython optimize zeros functions with full output.\n\n    Parameters\n    ----------\n    args : sequence of float\n        extra arguments of zero function\n    xa : float\n        first boundary of zero function\n    xb : float\n        second boundary of zero function\n    xtol : float\n        absolute tolerance of zero function\n    rtol : float\n        relative tolerance of zero function\n    mitr : int\n        max. iteration of zero function\n\n    Returns\n    -------\n    full_output : dict\n        the root, number of function calls, number of iterations, and the zero\n        function error number \n\n    This example finds the roots of a 3rd order polynomial with coefficients\n    given as `args`.\n    '
    ...

def loop_example() -> typing.Any:
    '\n    Example of Cython optimize zeros functions with map.\n\n    Parameters\n    ----------\n    method : str\n        name of the Cython optimize zeros function to call\n    a0 : sequence of float\n        first extra argument which is mapped to output\n    args : sequence of float\n        the remaining extra arguments which are constant\n    xa : float\n        first bound of zero function\n    xb : float\n        second bound of zero function\n    xtol : float\n        absolute tolerance of zero function\n    rtol : float\n        relative tolerance of zero function\n    mitr : int\n        max. iteration of zero function\n\n    Returns\n    -------\n    roots : sequence of float\n        the root for each of the values of `a0`\n\n    This example finds the roots of a 3rd order polynomial given a sequence of\n    constant terms as `a0` and fixed 1st, 2nd, and 3rd order terms in `args`.\n    '
    ...

def __getattr__(name) -> typing.Any:
    ...

