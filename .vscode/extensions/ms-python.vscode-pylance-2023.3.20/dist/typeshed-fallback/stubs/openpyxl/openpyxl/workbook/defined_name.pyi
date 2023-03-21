from _typeshed import Incomplete
from collections.abc import Generator

from openpyxl.descriptors.serialisable import Serialisable

RESERVED: Incomplete
RESERVED_REGEX: Incomplete
COL_RANGE: str
COL_RANGE_RE: Incomplete
ROW_RANGE: str
ROW_RANGE_RE: Incomplete
TITLES_REGEX: Incomplete

class DefinedName(Serialisable):
    tagname: str
    name: Incomplete
    comment: Incomplete
    customMenu: Incomplete
    description: Incomplete
    help: Incomplete
    statusBar: Incomplete
    localSheetId: Incomplete
    hidden: Incomplete
    function: Incomplete
    vbProcedure: Incomplete
    xlm: Incomplete
    functionGroupId: Incomplete
    shortcutKey: Incomplete
    publishToServer: Incomplete
    workbookParameter: Incomplete
    attr_text: Incomplete
    value: Incomplete
    def __init__(
        self,
        name: Incomplete | None = ...,
        comment: Incomplete | None = ...,
        customMenu: Incomplete | None = ...,
        description: Incomplete | None = ...,
        help: Incomplete | None = ...,
        statusBar: Incomplete | None = ...,
        localSheetId: Incomplete | None = ...,
        hidden: Incomplete | None = ...,
        function: Incomplete | None = ...,
        vbProcedure: Incomplete | None = ...,
        xlm: Incomplete | None = ...,
        functionGroupId: Incomplete | None = ...,
        shortcutKey: Incomplete | None = ...,
        publishToServer: Incomplete | None = ...,
        workbookParameter: Incomplete | None = ...,
        attr_text: Incomplete | None = ...,
    ) -> None: ...
    @property
    def type(self): ...
    @property
    def destinations(self) -> Generator[Incomplete, None, None]: ...
    @property
    def is_reserved(self): ...
    @property
    def is_external(self): ...
    def __iter__(self): ...

class DefinedNameList(Serialisable):
    tagname: str
    definedName: Incomplete
    def __init__(self, definedName=...) -> None: ...
    def append(self, defn) -> None: ...
    def __len__(self) -> int: ...
    def __contains__(self, name): ...
    def __getitem__(self, name): ...
    def get(self, name, scope: Incomplete | None = ...): ...
    def __delitem__(self, name) -> None: ...
    def delete(self, name, scope: Incomplete | None = ...): ...
    def localnames(self, scope): ...
