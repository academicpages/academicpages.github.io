from collections.abc import Mapping
from typing import (
    Any,
    Literal,
)

from pandas import (
    DataFrame,
    Series,
)
from pandas.core.computation.ops import BinOp

from pandas._typing import (
    Scalar,
    npt,
)

def eval(
    expr: str | BinOp,
    parser: Literal["pandas", "python"] = ...,
    engine: Literal["python", "numexpr"] | None = ...,
    local_dict: dict[str, Any] | None = ...,
    global_dict: dict[str, Any] | None = ...,
    resolvers: list[Mapping] | None = ...,
    level: int = ...,
    target: object | None = ...,
    inplace: bool = ...,
) -> npt.NDArray | Scalar | DataFrame | Series | None: ...
