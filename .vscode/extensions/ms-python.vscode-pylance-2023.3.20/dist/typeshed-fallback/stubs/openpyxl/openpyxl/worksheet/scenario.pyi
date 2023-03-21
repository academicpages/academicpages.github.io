from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

class InputCells(Serialisable):
    tagname: str
    r: Incomplete
    deleted: Incomplete
    undone: Incomplete
    val: Incomplete
    numFmtId: Incomplete
    def __init__(
        self,
        r: Incomplete | None = ...,
        deleted: bool = ...,
        undone: bool = ...,
        val: Incomplete | None = ...,
        numFmtId: Incomplete | None = ...,
    ) -> None: ...

class Scenario(Serialisable):
    tagname: str
    inputCells: Incomplete
    name: Incomplete
    locked: Incomplete
    hidden: Incomplete
    user: Incomplete
    comment: Incomplete
    __elements__: Incomplete
    __attrs__: Incomplete
    def __init__(
        self,
        inputCells=...,
        name: Incomplete | None = ...,
        locked: bool = ...,
        hidden: bool = ...,
        count: Incomplete | None = ...,
        user: Incomplete | None = ...,
        comment: Incomplete | None = ...,
    ) -> None: ...
    @property
    def count(self): ...

class ScenarioList(Serialisable):
    tagname: str
    scenario: Incomplete
    current: Incomplete
    show: Incomplete
    sqref: Incomplete
    __elements__: Incomplete
    def __init__(
        self, scenario=..., current: Incomplete | None = ..., show: Incomplete | None = ..., sqref: Incomplete | None = ...
    ) -> None: ...
    def append(self, scenario) -> None: ...
    def __bool__(self) -> bool: ...
