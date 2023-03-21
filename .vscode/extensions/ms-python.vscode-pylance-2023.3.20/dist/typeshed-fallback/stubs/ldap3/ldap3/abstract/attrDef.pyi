from _typeshed import Incomplete
from typing import Any

class AttrDef:
    name: Any
    key: Any
    validate: Any
    pre_query: Any
    post_query: Any
    default: Any
    dereference_dn: Any
    description: Any
    mandatory: Any
    single_value: Any
    oid_info: Any
    other_names: Any
    def __init__(
        self,
        name,
        key: Incomplete | None = ...,
        validate: Incomplete | None = ...,
        pre_query: Incomplete | None = ...,
        post_query: Incomplete | None = ...,
        default=...,
        dereference_dn: Incomplete | None = ...,
        description: Incomplete | None = ...,
        mandatory: bool = ...,
        single_value: Incomplete | None = ...,
        alias: Incomplete | None = ...,
    ) -> None: ...
    def __eq__(self, other): ...
    def __lt__(self, other): ...
    def __hash__(self) -> int: ...
    def __setattr__(self, key: str, value) -> None: ...
