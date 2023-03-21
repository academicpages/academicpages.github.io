from _typeshed import Incomplete
from typing import Any

from ..util import HasMemoized
from .base import Executable, Generative
from .elements import BinaryExpression, ColumnElement, NamedColumn
from .selectable import FromClause, TableValuedAlias
from .visitors import TraversibleType

def register_function(identifier, fn, package: str = ...) -> None: ...

class FunctionElement(Executable, ColumnElement[Any], FromClause, Generative):  # type: ignore[misc]
    packagenames: Incomplete
    clause_expr: Incomplete
    def __init__(self, *clauses, **kwargs) -> None: ...
    def scalar_table_valued(self, name, type_: Incomplete | None = ...): ...
    def table_valued(self, *expr, **kw): ...
    def column_valued(self, name: str | None = ..., joins_implicitly: bool = ...): ...
    @property
    def columns(self): ...
    @property
    def exported_columns(self): ...
    @HasMemoized.memoized_attribute
    def clauses(self): ...
    def over(
        self,
        partition_by: Incomplete | None = ...,
        order_by: Incomplete | None = ...,
        rows: Incomplete | None = ...,
        range_: Incomplete | None = ...,
    ): ...
    def within_group(self, *order_by): ...
    def filter(self, *criterion): ...
    def as_comparison(self, left_index, right_index): ...
    def within_group_type(self, within_group) -> None: ...
    def alias(self, name: str | None = ..., joins_implicitly: bool = ...) -> TableValuedAlias: ...  # type: ignore[override]
    def select(self): ...
    def scalar(self): ...
    def execute(self): ...
    def self_group(self, against: Incomplete | None = ...): ...
    @property
    def entity_namespace(self): ...

class FunctionAsBinary(BinaryExpression):
    sql_function: Incomplete
    left_index: Incomplete
    right_index: Incomplete
    operator: Incomplete
    type: Incomplete
    negate: Incomplete
    modifiers: Incomplete
    def __init__(self, fn, left_index, right_index) -> None: ...
    @property
    def left(self): ...
    @left.setter
    def left(self, value) -> None: ...
    @property
    def right(self): ...
    @right.setter
    def right(self, value) -> None: ...

class ScalarFunctionColumn(NamedColumn):
    __visit_name__: str
    is_literal: bool
    table: Incomplete
    fn: Incomplete
    name: Incomplete
    type: Incomplete
    def __init__(self, fn, name, type_: Incomplete | None = ...) -> None: ...

class _FunctionGenerator:
    opts: Incomplete
    def __init__(self, **opts) -> None: ...
    def __getattr__(self, name: str): ...
    def __call__(self, *c, **kwargs): ...

func: Incomplete
modifier: Incomplete

class Function(FunctionElement):
    __visit_name__: str
    type: Incomplete
    packagenames: Incomplete
    name: Incomplete
    def __init__(self, name, *clauses, **kw) -> None: ...

class _GenericMeta(TraversibleType):
    def __init__(cls, clsname, bases, clsdict) -> None: ...

class GenericFunction:
    name: Incomplete
    identifier: Incomplete
    coerce_arguments: bool
    inherit_cache: bool
    packagenames: Incomplete
    clause_expr: Incomplete
    type: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class next_value(GenericFunction):
    type: Incomplete
    name: str
    sequence: Incomplete
    def __init__(self, seq, **kw) -> None: ...
    def compare(self, other, **kw): ...

class AnsiFunction(GenericFunction):
    inherit_cache: bool
    def __init__(self, *args, **kwargs) -> None: ...

class ReturnTypeFromArgs(GenericFunction):
    inherit_cache: bool
    def __init__(self, *args, **kwargs) -> None: ...

class coalesce(ReturnTypeFromArgs):
    inherit_cache: bool

class max(ReturnTypeFromArgs):
    inherit_cache: bool

class min(ReturnTypeFromArgs):
    inherit_cache: bool

class sum(ReturnTypeFromArgs):
    inherit_cache: bool

class now(GenericFunction):
    type: Incomplete
    inherit_cache: bool

class concat(GenericFunction):
    type: Incomplete
    inherit_cache: bool

class char_length(GenericFunction):
    type: Incomplete
    inherit_cache: bool
    def __init__(self, arg, **kwargs) -> None: ...

class random(GenericFunction):
    inherit_cache: bool

class count(GenericFunction):
    type: Incomplete
    inherit_cache: bool
    def __init__(self, expression: Incomplete | None = ..., **kwargs) -> None: ...

class current_date(AnsiFunction):
    type: Incomplete
    inherit_cache: bool

class current_time(AnsiFunction):
    type: Incomplete
    inherit_cache: bool

class current_timestamp(AnsiFunction):
    type: Incomplete
    inherit_cache: bool

class current_user(AnsiFunction):
    type: Incomplete
    inherit_cache: bool

class localtime(AnsiFunction):
    type: Incomplete
    inherit_cache: bool

class localtimestamp(AnsiFunction):
    type: Incomplete
    inherit_cache: bool

class session_user(AnsiFunction):
    type: Incomplete
    inherit_cache: bool

class sysdate(AnsiFunction):
    type: Incomplete
    inherit_cache: bool

class user(AnsiFunction):
    type: Incomplete
    inherit_cache: bool

class array_agg(GenericFunction):
    type: Incomplete
    inherit_cache: bool
    def __init__(self, *args, **kwargs) -> None: ...

class OrderedSetAgg(GenericFunction):
    array_for_multi_clause: bool
    inherit_cache: bool
    def within_group_type(self, within_group): ...

class mode(OrderedSetAgg):
    inherit_cache: bool

class percentile_cont(OrderedSetAgg):
    array_for_multi_clause: bool
    inherit_cache: bool

class percentile_disc(OrderedSetAgg):
    array_for_multi_clause: bool
    inherit_cache: bool

class rank(GenericFunction):
    type: Incomplete
    inherit_cache: bool

class dense_rank(GenericFunction):
    type: Incomplete
    inherit_cache: bool

class percent_rank(GenericFunction):
    type: Incomplete
    inherit_cache: bool

class cume_dist(GenericFunction):
    type: Incomplete
    inherit_cache: bool

class cube(GenericFunction):
    inherit_cache: bool

class rollup(GenericFunction):
    inherit_cache: bool

class grouping_sets(GenericFunction):
    inherit_cache: bool
