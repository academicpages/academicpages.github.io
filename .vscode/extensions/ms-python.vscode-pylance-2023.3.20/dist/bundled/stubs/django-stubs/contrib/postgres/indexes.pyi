from typing import Any, Optional, Sequence

from django.db.models import Func, Index
from django.db.models.query_utils import Q

class PostgresIndex(Index): ...

class BrinIndex(PostgresIndex):
    def __init__(
        self,
        *expressions: Any,
        autosummarize: Optional[bool] = ...,
        pages_per_range: Optional[int] = ...,
        fields: Sequence[str] = ...,
        name: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        opclasses: Sequence[str] = ...,
        condition: Optional[Q] = ...
    ) -> None: ...

class BTreeIndex(PostgresIndex):
    def __init__(
        self,
        *expressions: Any,
        fillfactor: Optional[int] = ...,
        fields: Sequence[str] = ...,
        name: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        opclasses: Sequence[str] = ...,
        condition: Optional[Q] = ...
    ) -> None: ...

class GinIndex(PostgresIndex):
    def __init__(
        self,
        *expressions: Any,
        fastupdate: Optional[bool] = ...,
        gin_pending_list_limit: Optional[int] = ...,
        fields: Sequence[str] = ...,
        name: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        opclasses: Sequence[str] = ...,
        condition: Optional[Q] = ...
    ) -> None: ...

class GistIndex(PostgresIndex):
    def __init__(
        self,
        *expressions: Any,
        buffering: Optional[bool] = ...,
        fillfactor: Optional[int] = ...,
        fields: Sequence[str] = ...,
        name: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        opclasses: Sequence[str] = ...,
        condition: Optional[Q] = ...
    ) -> None: ...

class HashIndex(PostgresIndex):
    def __init__(
        self,
        *expressions: Any,
        fillfactor: Optional[int] = ...,
        fields: Sequence[str] = ...,
        name: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        opclasses: Sequence[str] = ...,
        condition: Optional[Q] = ...
    ) -> None: ...

class SpGistIndex(PostgresIndex):
    def __init__(
        self,
        *expressions: Any,
        fillfactor: Optional[int] = ...,
        fields: Sequence[str] = ...,
        name: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        opclasses: Sequence[str] = ...,
        condition: Optional[Q] = ...
    ) -> None: ...

class OpClass(Func):
    template: str = ...
    def __init__(
        self,
        expression: Any,
        name: str,
    ) -> None: ...
