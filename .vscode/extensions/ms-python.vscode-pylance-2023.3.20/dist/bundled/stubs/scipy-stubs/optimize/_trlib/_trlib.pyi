# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: scipy, version: 1.6.2
# Module: scipy.optimize._trlib._trlib, version: unspecified
import typing
import builtins as _mod_builtins
import scipy.optimize._trustregion as _mod_scipy_optimize__trustregion

BaseQuadraticSubproblem = _mod_scipy_optimize__trustregion.BaseQuadraticSubproblem
class TRLIBQuadraticSubproblem(_mod_scipy_optimize__trustregion.BaseQuadraticSubproblem):
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, x, fun, jac, hess, hessp, tol_rel_i, tol_rel_b, disp) -> None:
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
    
    def solve(self, trust_radius) -> typing.Any:
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
def _minimize_trust_region(fun, x0, args, jac, hess, hessp, subproblem, initial_trust_radius, max_trust_radius, eta, gtol, maxiter, disp, return_all, callback, inexact, **unknown_options) -> typing.Any:
    '\n    Minimization of scalar function of one or more variables using a\n    trust-region algorithm.\n\n    Options for the trust-region algorithm are:\n        initial_trust_radius : float\n            Initial trust radius.\n        max_trust_radius : float\n            Never propose steps that are longer than this value.\n        eta : float\n            Trust region related acceptance stringency for proposed steps.\n        gtol : float\n            Gradient norm must be less than `gtol`\n            before successful termination.\n        maxiter : int\n            Maximum number of iterations to perform.\n        disp : bool\n            If True, print convergence message.\n        inexact : bool\n            Accuracy to solve subproblems. If True requires less nonlinear\n            iterations, but more vector products. Only effective for method\n            trust-krylov.\n\n    This function is called by the `minimize` function.\n    It is not supposed to be called directly.\n    '
    ...

def __getattr__(name) -> typing.Any:
    ...

