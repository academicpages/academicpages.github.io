import numpy as np

def is_list_like_indexer(key) -> bool: ...
def is_scalar_indexer(indexer, arr_value) -> bool: ...
def is_empty_indexer(indexer, arr_value: np.ndarray) -> bool: ...
def check_setitem_lengths(indexer, value, values) -> None: ...
def validate_indices(indices: np.ndarray, n: int) -> None: ...
def maybe_convert_indices(indices, n: int): ...
def length_of_indexer(indexer, target=...) -> int: ...
def deprecate_ndim_indexing(result) -> None: ...
def check_array_indexer(arrayArrayLike, indexer): ...

class BaseIndexer:
    def __init__(
        self,
        index_array: np.ndarray | None = ...,
        window_size: int = ...,
        **kwargs,
    ): ...
    def get_window_bounds(
        self,
        num_values: int = ...,
        min_periods: int | None = ...,
        center: bool | None = ...,
        closed: str | None = ...,
    ) -> tuple[np.ndarray, np.ndarray]: ...

class VariableOffsetWindowIndexer(BaseIndexer):
    def __init__(
        self,
        index_array: np.ndarray | None = ...,
        window_size: int = ...,
        index=...,
        offset=...,
        **kwargs,
    ): ...
    def get_window_bounds(
        self,
        num_values: int = ...,
        min_periods: int | None = ...,
        center: bool | None = ...,
        closed: str | None = ...,
    ) -> tuple[np.ndarray, np.ndarray]: ...

class FixedForwardWindowIndexer(BaseIndexer):
    def get_window_bounds(
        self,
        num_values: int = ...,
        min_periods: int | None = ...,
        center: bool | None = ...,
        closed: str | None = ...,
    ) -> tuple[np.ndarray, np.ndarray]: ...
