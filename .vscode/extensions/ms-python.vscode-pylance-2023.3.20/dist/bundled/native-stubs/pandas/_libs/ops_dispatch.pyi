# Python: 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)]
# Library: pandas, version: 1.2.4
# Module: pandas._libs.ops_dispatch, version: unspecified
import typing
import builtins as _mod_builtins

DISPATCHED_UFUNCS: set
REVERSED_NAMES: dict
UFUNC_ALIASES: dict
__doc__: typing.Any
__file__: str
__name__: str
__package__: str
__test__: dict
def maybe_dispatch_ufunc_to_dunder_op() -> typing.Any:
    "\n    Dispatch a ufunc to the equivalent dunder method.\n\n    Parameters\n    ----------\n    self : ArrayLike\n        The array whose dunder method we dispatch to\n    ufunc : Callable\n        A NumPy ufunc\n    method : {'reduce', 'accumulate', 'reduceat', 'outer', 'at', '__call__'}\n    inputs : ArrayLike\n        The input arrays.\n    kwargs : Any\n        The additional keyword arguments, e.g. ``out``.\n\n    Returns\n    -------\n    result : Any\n        The result of applying the ufunc\n    "
    ...

def __getattr__(name) -> typing.Any:
    ...

