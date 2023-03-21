# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: scipy, version: 1.6.2
# Module: scipy.signal._spectral, version: unspecified
import typing
import builtins as _mod_builtins

__all__: list
__doc__: str
__file__: str
__name__: str
__package__: str
__test__: dict
def _lombscargle(x, y, freqs) -> typing.Any:
    '\n    _lombscargle(x, y, freqs)\n\n    Computes the Lomb-Scargle periodogram.\n\n    Parameters\n    ----------\n    x : array_like\n        Sample times.\n    y : array_like\n        Measurement values (must be registered so the mean is zero).\n    freqs : array_like\n        Angular frequencies for output periodogram.\n\n    Returns\n    -------\n    pgram : array_like\n        Lomb-Scargle periodogram.\n\n    Raises\n    ------\n    ValueError\n        If the input arrays `x` and `y` do not have the same shape.\n\n    See also\n    --------\n    lombscargle\n\n    '
    ...

def __getattr__(name) -> typing.Any:
    ...

