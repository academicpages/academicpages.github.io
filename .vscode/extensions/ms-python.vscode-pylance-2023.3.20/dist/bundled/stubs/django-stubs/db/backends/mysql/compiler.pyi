from typing import Any

from django.db.models.sql import compiler as compiler

class SQLCompiler(compiler.SQLCompiler):
    def as_subquery_condition(self, alias: Any, columns: Any, compiler: Any) -> Any: ...

class SQLInsertCompiler(compiler.SQLInsertCompiler, SQLCompiler): ...

class SQLDeleteCompiler(compiler.SQLDeleteCompiler, SQLCompiler):
    def as_sql(self) -> Any: ...  # type: ignore [override]

class SQLUpdateCompiler(compiler.SQLUpdateCompiler, SQLCompiler): ...
class SQLAggregateCompiler(compiler.SQLAggregateCompiler, SQLCompiler): ...
