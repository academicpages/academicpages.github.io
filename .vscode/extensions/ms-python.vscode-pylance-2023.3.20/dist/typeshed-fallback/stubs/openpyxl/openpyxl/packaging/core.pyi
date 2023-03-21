from _typeshed import Incomplete

from openpyxl.descriptors import DateTime
from openpyxl.descriptors.nested import NestedText
from openpyxl.descriptors.serialisable import Serialisable

class NestedDateTime(DateTime, NestedText):
    expected_type: Incomplete
    def to_tree(self, tagname: Incomplete | None = ..., value: Incomplete | None = ..., namespace: Incomplete | None = ...): ...

class QualifiedDateTime(NestedDateTime):
    def to_tree(self, tagname: Incomplete | None = ..., value: Incomplete | None = ..., namespace: Incomplete | None = ...): ...

class DocumentProperties(Serialisable):
    tagname: str
    namespace: Incomplete
    category: Incomplete
    contentStatus: Incomplete
    keywords: Incomplete
    lastModifiedBy: Incomplete
    lastPrinted: Incomplete
    revision: Incomplete
    version: Incomplete
    last_modified_by: Incomplete
    subject: Incomplete
    title: Incomplete
    creator: Incomplete
    description: Incomplete
    identifier: Incomplete
    language: Incomplete
    created: Incomplete
    modified: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        category: Incomplete | None = ...,
        contentStatus: Incomplete | None = ...,
        keywords: Incomplete | None = ...,
        lastModifiedBy: Incomplete | None = ...,
        lastPrinted: Incomplete | None = ...,
        revision: Incomplete | None = ...,
        version: Incomplete | None = ...,
        created=...,
        creator: str = ...,
        description: Incomplete | None = ...,
        identifier: Incomplete | None = ...,
        language: Incomplete | None = ...,
        modified=...,
        subject: Incomplete | None = ...,
        title: Incomplete | None = ...,
    ) -> None: ...
