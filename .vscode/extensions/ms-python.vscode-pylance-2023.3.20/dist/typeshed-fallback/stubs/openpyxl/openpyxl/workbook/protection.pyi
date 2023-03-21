from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

class WorkbookProtection(Serialisable):
    tagname: str
    workbook_password: Incomplete
    workbookPasswordCharacterSet: Incomplete
    revision_password: Incomplete
    revisionsPasswordCharacterSet: Incomplete
    lockStructure: Incomplete
    lock_structure: Incomplete
    lockWindows: Incomplete
    lock_windows: Incomplete
    lockRevision: Incomplete
    lock_revision: Incomplete
    revisionsAlgorithmName: Incomplete
    revisionsHashValue: Incomplete
    revisionsSaltValue: Incomplete
    revisionsSpinCount: Incomplete
    workbookAlgorithmName: Incomplete
    workbookHashValue: Incomplete
    workbookSaltValue: Incomplete
    workbookSpinCount: Incomplete
    __attrs__: Incomplete
    def __init__(
        self,
        workbookPassword: Incomplete | None = ...,
        workbookPasswordCharacterSet: Incomplete | None = ...,
        revisionsPassword: Incomplete | None = ...,
        revisionsPasswordCharacterSet: Incomplete | None = ...,
        lockStructure: Incomplete | None = ...,
        lockWindows: Incomplete | None = ...,
        lockRevision: Incomplete | None = ...,
        revisionsAlgorithmName: Incomplete | None = ...,
        revisionsHashValue: Incomplete | None = ...,
        revisionsSaltValue: Incomplete | None = ...,
        revisionsSpinCount: Incomplete | None = ...,
        workbookAlgorithmName: Incomplete | None = ...,
        workbookHashValue: Incomplete | None = ...,
        workbookSaltValue: Incomplete | None = ...,
        workbookSpinCount: Incomplete | None = ...,
    ) -> None: ...
    def set_workbook_password(self, value: str = ..., already_hashed: bool = ...) -> None: ...
    @property
    def workbookPassword(self): ...
    @workbookPassword.setter
    def workbookPassword(self, value) -> None: ...
    def set_revisions_password(self, value: str = ..., already_hashed: bool = ...) -> None: ...
    @property
    def revisionsPassword(self): ...
    @revisionsPassword.setter
    def revisionsPassword(self, value) -> None: ...
    @classmethod
    def from_tree(cls, node): ...

DocumentSecurity = WorkbookProtection

class FileSharing(Serialisable):
    tagname: str
    readOnlyRecommended: Incomplete
    userName: Incomplete
    reservationPassword: Incomplete
    algorithmName: Incomplete
    hashValue: Incomplete
    saltValue: Incomplete
    spinCount: Incomplete
    def __init__(
        self,
        readOnlyRecommended: Incomplete | None = ...,
        userName: Incomplete | None = ...,
        reservationPassword: Incomplete | None = ...,
        algorithmName: Incomplete | None = ...,
        hashValue: Incomplete | None = ...,
        saltValue: Incomplete | None = ...,
        spinCount: Incomplete | None = ...,
    ) -> None: ...
