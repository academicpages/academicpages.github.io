from typing import Literal, Callable

from sympy.core import Expr

def powsimp(
    expr: Expr,
    deep: bool = ...,
    combine: Literal["all", "base", "exp"] = ...,
    force: bool = ...,
    measure: Callable[[Expr], int] = ...,
) -> Expr: ...
def powdenest(eq: Expr, force: bool = ..., polar: bool = ...) -> Expr: ...
