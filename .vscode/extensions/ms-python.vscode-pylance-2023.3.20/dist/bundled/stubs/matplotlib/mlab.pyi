import numpy as np
from typing import Callable, Literal, Sequence
from ._typing import *

def window_hanning(x): ...
def window_none(x): ...
def detrend(
    x: Sequence,
    key: Literal["default", "constant", "mean", "linear", "none"] | Callable = ...,
    axis: int = ...,
) -> Sequence: ...
def detrend_mean(x: Sequence, axis: int = ...) -> Sequence: ...
def detrend_none(x, axis: int = ...): ...
def detrend_linear(y: Sequence) -> Sequence: ...
def stride_windows(x: Sequence, n: int, noverlap: int = ..., axis: int = ...): ...
def psd(
    x: Sequence,
    NFFT: int = ...,
    Fs: float = ...,
    detrend: Literal["none", "mean", "linear"] | Callable = ...,
    window: Callable | np.ndarray = ...,
    noverlap: int = 0,
    pad_to: int = ...,
    sides: Literal["default", "onesided", "twosided"] = ...,
    scale_by_freq: bool = ...,
) -> tuple[np.ndarray, np.ndarray]: ...
def csd(
    x: ArrayLike,
    y: ArrayLike,
    NFFT: int = ...,
    Fs: float = ...,
    detrend: Literal["none", "mean", "linear"] | Callable = ...,
    window: Callable | np.ndarray = ...,
    noverlap: int = 0,
    pad_to: int = ...,
    sides: Literal["default", "onesided", "twosided"] = ...,
    scale_by_freq: bool = ...,
) -> tuple[np.ndarray, np.ndarray]: ...

complex_spectrum = ...
magnitude_spectrum = ...
angle_spectrum = ...
phase_spectrum = ...

def specgram(
    x: ArrayLike,
    NFFT: int = ...,
    Fs: float = ...,
    detrend: Literal["none", "mean", "linear"] | Callable = ...,
    window: Callable | np.ndarray = ...,
    noverlap: int = 0,
    pad_to: int = ...,
    sides: Literal["default", "onesided", "twosided"] = ...,
    scale_by_freq: bool = ...,
    mode: str = ...,
) -> tuple[ArrayLike, ArrayLike, ArrayLike]: ...
def cohere(
    x,
    y,
    NFFT: int = ...,
    Fs: float = ...,
    detrend: Literal["none", "mean", "linear"] | Callable = ...,
    window: Callable | np.ndarray = ...,
    noverlap: int = 0,
    pad_to: int = ...,
    sides: Literal["default", "onesided", "twosided"] = ...,
    scale_by_freq: bool = ...,
) -> tuple[np.ndarray, np.ndarray]: ...

class GaussianKDE:
    def __init__(
        self, dataset: ArrayLike, bw_method: str | Scalar | Callable = ...
    ) -> None: ...
    def scotts_factor(self): ...
    def silverman_factor(self): ...

    covariance_factor = ...
    def evaluate(self, points) -> np.ndarray: ...
