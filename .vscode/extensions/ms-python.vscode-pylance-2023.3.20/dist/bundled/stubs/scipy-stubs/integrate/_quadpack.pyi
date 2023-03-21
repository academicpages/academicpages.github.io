# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: scipy, version: 1.6.2
# Module: scipy.integrate._quadpack, version:  1.13 
import typing
import builtins as _mod_builtins
import quadpack as _mod_quadpack

__doc__: typing.Any
__file__: str
__name__: str
__package__: str
__version__: str
def _qagie(fun, bound, inf, args, full_output, epsabs, epsrel, limit) -> typing.Any:
    '[result,abserr,infodict,ier] = _qagie(fun, bound, inf, | args, full_output, epsabs, epsrel, limit)'
    ...

def _qagpe(fun, a, b, points, args, full_output, epsabs, epsrel, limit) -> typing.Any:
    '[result,abserr,infodict,ier] = _qagpe(fun, a, b, points, | args, full_output, epsabs, epsrel, limit)'
    ...

def _qagse(fun, a, b, args, full_output, epsabs, epsrel, limit) -> typing.Any:
    '[result,abserr,infodict,ier] = _qagse(fun, a, b, | args, full_output, epsabs, epsrel, limit)'
    ...

def _qawce(fun, a, b, c, args, full_output, epsabs, epsrel, limit) -> typing.Any:
    '[result,abserr,infodict,ier] = _qawce(fun, a, b, c, | args, full_output, epsabs, epsrel, limit)'
    ...

def _qawfe(fun, a, omega, integr, args, full_output, epsabs, limlst, limit, maxp1) -> typing.Any:
    '[result,abserr,infodict,ier] = _qawfe(fun, a, omega, integr, | args, full_output, epsabs, limlst, limit, maxp1)'
    ...

def _qawoe(fun, a, b, omega, integr, args, full_output, epsabs, epsrel, limit, maxp1, icall, momcom, chebmo) -> typing.Any:
    '[result,abserr,infodict,ier] = _qawoe(fun, a, b, omega, integr, | args, full_output, epsabs, epsrel, limit, maxp1, icall, momcom, chebmo)'
    ...

def _qawse(fun, a, b, alfa, beta) -> typing.Any:
    '[result,abserr,infodict,ier] = _qawse(fun, a, b, (alfa, beta), integr, | args, full_output, epsabs, epsrel, limit)'
    ...

error = _mod_quadpack.error
def __getattr__(name) -> typing.Any:
    ...

