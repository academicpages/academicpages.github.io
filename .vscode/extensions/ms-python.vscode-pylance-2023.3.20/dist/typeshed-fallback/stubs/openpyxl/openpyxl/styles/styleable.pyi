from _typeshed import Incomplete
from warnings import warn as warn

class StyleDescriptor:
    collection: Incomplete
    key: Incomplete
    def __init__(self, collection, key) -> None: ...
    def __set__(self, instance, value) -> None: ...
    def __get__(self, instance, cls): ...

class NumberFormatDescriptor:
    key: str
    collection: str
    def __set__(self, instance, value) -> None: ...
    def __get__(self, instance, cls): ...

class NamedStyleDescriptor:
    key: str
    collection: str
    def __set__(self, instance, value) -> None: ...
    def __get__(self, instance, cls): ...

class StyleArrayDescriptor:
    key: Incomplete
    def __init__(self, key) -> None: ...
    def __set__(self, instance, value) -> None: ...
    def __get__(self, instance, cls): ...

class StyleableObject:
    font: Incomplete
    fill: Incomplete
    border: Incomplete
    number_format: Incomplete
    protection: Incomplete
    alignment: Incomplete
    style: Incomplete
    quotePrefix: Incomplete
    pivotButton: Incomplete
    parent: Incomplete
    def __init__(self, sheet, style_array: Incomplete | None = ...) -> None: ...
    @property
    def style_id(self): ...
    @property
    def has_style(self): ...
