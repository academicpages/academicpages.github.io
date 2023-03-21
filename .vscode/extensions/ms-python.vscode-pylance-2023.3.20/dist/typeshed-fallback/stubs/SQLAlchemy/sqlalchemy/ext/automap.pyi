from _typeshed import Incomplete
from typing import Any

def classname_for_table(base, tablename, table): ...
def name_for_scalar_relationship(base, local_cls, referred_cls, constraint): ...
def name_for_collection_relationship(base, local_cls, referred_cls, constraint): ...
def generate_relationship(base, direction, return_fn, attrname, local_cls, referred_cls, **kw): ...

class AutomapBase:
    __abstract__: bool
    classes: Any
    @classmethod
    def prepare(
        cls,
        autoload_with: Incomplete | None = ...,
        engine: Incomplete | None = ...,
        reflect: bool = ...,
        schema: Incomplete | None = ...,
        classname_for_table: Incomplete | None = ...,
        collection_class: Incomplete | None = ...,
        name_for_scalar_relationship: Incomplete | None = ...,
        name_for_collection_relationship: Incomplete | None = ...,
        generate_relationship: Incomplete | None = ...,
        reflection_options=...,
    ) -> None: ...

def automap_base(declarative_base: Incomplete | None = ..., **kw): ...
