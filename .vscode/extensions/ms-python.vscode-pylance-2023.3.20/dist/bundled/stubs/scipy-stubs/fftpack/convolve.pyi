# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: scipy, version: 1.6.2
# Module: scipy.fftpack.convolve, version: unspecified
import typing
import builtins as _mod_builtins

__all__: list
__doc__: typing.Any
__file__: str
__name__: str
__package__: str
def __pyx_unpickle_Enum() -> typing.Any:
    ...

__test__: dict
def convolve(x, omega, swap_real_imag=..., overwrite_x=...) -> typing.Any:
    "y = convolve(x,omega,[swap_real_imag,overwrite_x])\n\n    Wrapper for ``convolve``.\n\n    Parameters\n    ----------\n    x : input rank-1 array('d') with bounds (n)\n    omega : input rank-1 array('d') with bounds (n)\n\n    Other Parameters\n    ----------------\n    overwrite_x : input int, optional\n        Default: 0\n    swap_real_imag : input int, optional\n         Default: 0\n\n    Returns\n    -------\n    y : rank-1 array('d') with bounds (n) and x storage\n    "
    ...

def convolve_z(x, omega_real, omega_imag, overwrite_x=...) -> typing.Any:
    "y = convolve_z(x,omega_real,omega_imag,[overwrite_x])\n\n    Wrapper for ``convolve_z``.\n\n    Parameters\n    ----------\n    x : input rank-1 array('d') with bounds (n)\n    omega_real : input rank-1 array('d') with bounds (n)\n    omega_imag : input rank-1 array('d') with bounds (n)\n\n    Other Parameters\n    ----------------\n    overwrite_x : input int, optional\n        Default: 0\n\n    Returns\n    -------\n    y : rank-1 array('d') with bounds (n) and x storage\n    "
    ...

def destroy_convolve_cache() -> typing.Any:
    ...

def init_convolution_kernel(n, kernel_func, d=..., zero_nyquist=..., kernel_func_extra_args=...) -> typing.Any:
    "omega = init_convolution_kernel(n,kernel_func,[d,zero_nyquist,kernel_func_extra_args])\n\n    Wrapper for ``init_convolution_kernel``.\n\n    Parameters\n    ----------\n    n : input int\n    kernel_func : call-back function\n\n    Other Parameters\n    ----------------\n    d : input int, optional\n        Default: 0\n    kernel_func_extra_args : input tuple, optional\n        Default: ()\n    zero_nyquist : input int, optional\n        Default: d%2\n\n    Returns\n    -------\n    omega : rank-1 array('d') with bounds (n)\n\n    Notes\n    -----\n    Call-back functions::\n\n      def kernel_func(k): return kernel_func\n      Required arguments:\n        k : input int\n      Return objects:\n        kernel_func : float\n    "
    ...

def r2r_fftpack(a, axes, real2hermitian, forward, inorm=..., out=..., nthreads=...) -> typing.Any:
    "r2r_fftpack(a: array, axes: object, real2hermitian: bool, forward: bool, inorm: int = 0, out: object = None, nthreads: int = 1) -> array\n\nPerforms a real-valued FFT using the FFTPACK storage scheme.\n\nParameters\n----------\na : numpy.ndarray (any real type)\n    The input data\naxes : list of integers\n    The axes along which the FFT is carried out.\n    If not set, all axes will be transformed.\nreal2hermitian : bool\n    if True, the input is purely real and the output will have Hermitian\n    symmetry and be stored in FFTPACK's halfcomplex ordering, otherwise the\n    opposite.\nforward : bool\n    If `True`, a negative sign is used in the exponent, else a positive one.\ninorm : int\n    Normalization type\n      0 : no normalization\n      1 : divide by sqrt(N)\n      2 : divide by N\n    where N is the length of `axis`.\nout : numpy.ndarray (same shape and data type as `a`)\n    May be identical to `a`, but if it isn't, it must not overlap with `a`.\n    If None, a new array is allocated to store the output.\nnthreads : int\n    Number of threads to use. If 0, use the system default (typically governed\n    by the `OMP_NUM_THREADS` environment variable).\n\nReturns\n-------\nnumpy.ndarray (same shape and data type as `a`)\n    The transformed data. The shape is identical to that of the input array.\n\n"
    ...

def __getattr__(name) -> typing.Any:
    ...

