from typing import (
    Any,
    Callable,
)

from pandas._typing import Scalar

def make_rolling_apply(
    func: Callable[..., Scalar],
    args: tuple,
    nogil: bool,
    parallel: bool,
    nopython: bool,
): ...
def generate_numba_apply_func(
    args: tuple,
    kwargs: dict[str, Any],
    func: Callable[..., Scalar],
    engine_kwargs: dict[str, bool] | None,
): ...
