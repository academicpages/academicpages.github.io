from _typeshed import Incomplete

def paged_search_generator(
    connection,
    search_base,
    search_filter,
    search_scope=...,
    dereference_aliases=...,
    attributes: Incomplete | None = ...,
    size_limit: int = ...,
    time_limit: int = ...,
    types_only: bool = ...,
    get_operational_attributes: bool = ...,
    controls: Incomplete | None = ...,
    paged_size: int = ...,
    paged_criticality: bool = ...,
) -> None: ...
def paged_search_accumulator(
    connection,
    search_base,
    search_filter,
    search_scope=...,
    dereference_aliases=...,
    attributes: Incomplete | None = ...,
    size_limit: int = ...,
    time_limit: int = ...,
    types_only: bool = ...,
    get_operational_attributes: bool = ...,
    controls: Incomplete | None = ...,
    paged_size: int = ...,
    paged_criticality: bool = ...,
): ...
