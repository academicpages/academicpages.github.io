from _typeshed import Incomplete

from .commands import SearchCommands

class Search(SearchCommands):
    class BatchIndexer:
        def __init__(self, client, chunk_size: int = ...) -> None: ...
        def add_document(
            self,
            doc_id,
            nosave: bool = ...,
            score: float = ...,
            payload: Incomplete | None = ...,
            replace: bool = ...,
            partial: bool = ...,
            no_create: bool = ...,
            **fields,
        ): ...
        def add_document_hash(self, doc_id, score: float = ..., replace: bool = ...): ...
        def commit(self): ...

    def __init__(self, client, index_name: str = ...) -> None: ...
