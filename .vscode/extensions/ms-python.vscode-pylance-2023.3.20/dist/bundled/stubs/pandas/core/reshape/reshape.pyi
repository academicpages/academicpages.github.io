import numpy as np
from pandas.core.frame import DataFrame

def unstack(obj, level, fill_value=...): ...
def stack(frame, level: int = ..., dropna: bool = ...): ...
def stack_multiple(frame, level, dropna: bool = ...): ...
def get_dummies(
    data,
    prefix=...,
    prefix_sep=...,
    dummy_na=...,
    columns=...,
    sparse=...,
    drop_first=...,
    dtype=...,
) -> DataFrame: ...
