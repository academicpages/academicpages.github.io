# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: scipy, version: 1.6.2
# Module: _odrpack, version: unspecified
import typing
import builtins as _mod_builtins

__doc__: typing.Any
__file__: str
__name__: str
__package__: str
def _set_exceptions(odr_error, odr_stop) -> typing.Any:
    '_set_exceptions(odr_error, odr_stop)\n\n    Internal function: set exception classes.'
    ...

def odr(fcn, beta0, y, x, we=..., wd=..., fjacb=..., fjacd=..., extra_args=..., ifixx=..., ifixb=..., job=..., iprint=..., errfile=..., rptfile=..., ndigit=..., taufac=..., sstol=..., partol=..., maxit=..., stpb=..., stpd=..., sclb=..., scld=..., work=..., iwork=..., full_output=...) -> typing.Any:
    'odr(fcn, beta0, y, x, we=None, wd=None, fjacb=None, fjacd=None, extra_args=None, ifixx=None, ifixb=None, job=0, iprint=0, errfile=None, rptfile=None, ndigit=0, taufac=0.0, sstol=-1.0, partol=-1.0, maxit=-1, stpb=None, stpd=None, sclb=None, scld=None, work=None, iwork=None, full_output=0)\n\n    Low-level function for ODR.\n\n    See Also\n    --------\n    ODR : The ODR class gathers all information and coordinates the running of the main fitting routine.\n    Model : The Model class stores information about the function you wish to fit.\n    Data : The data to fit.\n    RealData : Data with weights as actual std. dev.s and/or covariances.\n\n    Notes\n    -----\n    This is a function performing the same operation as the `ODR`,\n    `Model`, and `Data` classes together. The parameters of this\n    function are explained in the class documentation.'
    ...

def __getattr__(name) -> typing.Any:
    ...

