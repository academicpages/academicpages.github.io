from _typeshed import Incomplete
from typing import Generic, TypeVar

from . import elements, roles
from .base import Options
from .operators import ColumnOperators

_T = TypeVar("_T")

class LambdaOptions(Options):
    enable_tracking: bool
    track_closure_variables: bool
    track_on: Incomplete
    global_track_bound_values: bool
    track_bound_values: bool
    lambda_cache: Incomplete

def lambda_stmt(
    lmb,
    enable_tracking: bool = ...,
    track_closure_variables: bool = ...,
    track_on: Incomplete | None = ...,
    global_track_bound_values: bool = ...,
    track_bound_values: bool = ...,
    lambda_cache: Incomplete | None = ...,
): ...

class LambdaElement(elements.ClauseElement):
    __visit_name__: str
    parent_lambda: Incomplete
    fn: Incomplete
    role: Incomplete
    tracker_key: Incomplete
    opts: Incomplete
    def __init__(self, fn, role, opts=..., apply_propagate_attrs: Incomplete | None = ...) -> None: ...
    def __getattr__(self, key: str): ...

class DeferredLambdaElement(LambdaElement):
    lambda_args: Incomplete
    def __init__(self, fn, role, opts=..., lambda_args=...) -> None: ...

class StatementLambdaElement(roles.AllowsLambdaRole, LambdaElement):
    def __add__(self, other): ...
    def add_criteria(
        self,
        other,
        enable_tracking: bool = ...,
        track_on: Incomplete | None = ...,
        track_closure_variables: bool = ...,
        track_bound_values: bool = ...,
    ): ...
    def spoil(self): ...

class NullLambdaStatement(roles.AllowsLambdaRole, elements.ClauseElement):
    __visit_name__: str
    def __init__(self, statement) -> None: ...
    def __getattr__(self, key: str): ...
    def __add__(self, other): ...
    def add_criteria(self, other, **kw): ...

class LinkedLambdaElement(StatementLambdaElement):
    role: Incomplete
    opts: Incomplete
    fn: Incomplete
    parent_lambda: Incomplete
    tracker_key: Incomplete
    def __init__(self, fn, parent_lambda, opts) -> None: ...

class AnalyzedCode:
    @classmethod
    def get(cls, fn, lambda_element, lambda_kw, **kw): ...
    track_bound_values: Incomplete
    track_closure_variables: Incomplete
    bindparam_trackers: Incomplete
    closure_trackers: Incomplete
    build_py_wrappers: Incomplete
    def __init__(self, fn, lambda_element, opts) -> None: ...

class NonAnalyzedFunction:
    closure_bindparams: Incomplete
    bindparam_trackers: Incomplete
    expr: Incomplete
    def __init__(self, expr) -> None: ...
    @property
    def expected_expr(self): ...

class AnalyzedFunction:
    analyzed_code: Incomplete
    fn: Incomplete
    closure_pywrappers: Incomplete
    tracker_instrumented_fn: Incomplete
    expr: Incomplete
    bindparam_trackers: Incomplete
    expected_expr: Incomplete
    is_sequence: Incomplete
    propagate_attrs: Incomplete
    closure_bindparams: Incomplete
    def __init__(self, analyzed_code, lambda_element, apply_propagate_attrs, fn) -> None: ...

class PyWrapper(ColumnOperators[_T], Generic[_T]):
    fn: Incomplete
    track_bound_values: Incomplete
    def __init__(
        self,
        fn,
        name,
        to_evaluate,
        closure_index: Incomplete | None = ...,
        getter: Incomplete | None = ...,
        track_bound_values: bool = ...,
    ) -> None: ...
    def __call__(self, *arg, **kw): ...
    def operate(self, op, *other, **kwargs): ...
    def reverse_operate(self, op, other, **kwargs): ...
    def __clause_element__(self): ...  # Field not always present.
    def __bool__(self) -> bool: ...
    def __nonzero__(self) -> bool: ...
    def __getattribute__(self, key: str): ...
    def __iter__(self): ...
    def __getitem__(self, key) -> ColumnOperators[_T]: ...

def insp(lmb): ...
