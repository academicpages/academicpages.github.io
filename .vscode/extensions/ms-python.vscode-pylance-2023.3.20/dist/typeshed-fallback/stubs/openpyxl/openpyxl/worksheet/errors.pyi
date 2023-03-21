from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

class Extension(Serialisable):
    tagname: str
    uri: Incomplete
    def __init__(self, uri: Incomplete | None = ...) -> None: ...

class ExtensionList(Serialisable):
    tagname: str
    ext: Incomplete
    __elements__: Incomplete
    def __init__(self, ext=...) -> None: ...

class IgnoredError(Serialisable):
    tagname: str
    sqref: Incomplete
    evalError: Incomplete
    twoDigitTextYear: Incomplete
    numberStoredAsText: Incomplete
    formula: Incomplete
    formulaRange: Incomplete
    unlockedFormula: Incomplete
    emptyCellReference: Incomplete
    listDataValidation: Incomplete
    calculatedColumn: Incomplete
    def __init__(
        self,
        sqref: Incomplete | None = ...,
        evalError: bool = ...,
        twoDigitTextYear: bool = ...,
        numberStoredAsText: bool = ...,
        formula: bool = ...,
        formulaRange: bool = ...,
        unlockedFormula: bool = ...,
        emptyCellReference: bool = ...,
        listDataValidation: bool = ...,
        calculatedColumn: bool = ...,
    ) -> None: ...

class IgnoredErrors(Serialisable):
    tagname: str
    ignoredError: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(self, ignoredError=..., extLst: Incomplete | None = ...) -> None: ...
