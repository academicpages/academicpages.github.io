from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

def collapse_cell_addresses(cells, input_ranges=...): ...
def expand_cell_ranges(range_string): ...

class DataValidation(Serialisable):
    tagname: str
    sqref: Incomplete
    cells: Incomplete
    ranges: Incomplete
    showErrorMessage: Incomplete
    showDropDown: Incomplete
    hide_drop_down: Incomplete
    showInputMessage: Incomplete
    allowBlank: Incomplete
    allow_blank: Incomplete
    errorTitle: Incomplete
    error: Incomplete
    promptTitle: Incomplete
    prompt: Incomplete
    formula1: Incomplete
    formula2: Incomplete
    type: Incomplete
    errorStyle: Incomplete
    imeMode: Incomplete
    operator: Incomplete
    validation_type: Incomplete
    def __init__(
        self,
        type: Incomplete | None = ...,
        formula1: Incomplete | None = ...,
        formula2: Incomplete | None = ...,
        showErrorMessage: bool = ...,
        showInputMessage: bool = ...,
        showDropDown: Incomplete | None = ...,
        allowBlank: Incomplete | None = ...,
        sqref=...,
        promptTitle: Incomplete | None = ...,
        errorStyle: Incomplete | None = ...,
        error: Incomplete | None = ...,
        prompt: Incomplete | None = ...,
        errorTitle: Incomplete | None = ...,
        imeMode: Incomplete | None = ...,
        operator: Incomplete | None = ...,
        allow_blank: Incomplete | None = ...,
    ) -> None: ...
    def add(self, cell) -> None: ...
    def __contains__(self, cell): ...

class DataValidationList(Serialisable):
    tagname: str
    disablePrompts: Incomplete
    xWindow: Incomplete
    yWindow: Incomplete
    dataValidation: Incomplete
    __elements__: Incomplete
    __attrs__: Incomplete
    def __init__(
        self,
        disablePrompts: Incomplete | None = ...,
        xWindow: Incomplete | None = ...,
        yWindow: Incomplete | None = ...,
        count: Incomplete | None = ...,
        dataValidation=...,
    ) -> None: ...
    @property
    def count(self): ...
    def __len__(self) -> int: ...
    def append(self, dv) -> None: ...
    def to_tree(self, tagname: Incomplete | None = ...): ...  # type: ignore[override]
