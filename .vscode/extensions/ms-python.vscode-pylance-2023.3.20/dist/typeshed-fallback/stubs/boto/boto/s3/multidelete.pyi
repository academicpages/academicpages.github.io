from _typeshed import Incomplete
from typing import Any

class Deleted:
    key: Any
    version_id: Any
    delete_marker: Any
    delete_marker_version_id: Any
    def __init__(
        self,
        key: Incomplete | None = ...,
        version_id: Incomplete | None = ...,
        delete_marker: bool = ...,
        delete_marker_version_id: Incomplete | None = ...,
    ) -> None: ...
    def startElement(self, name, attrs, connection): ...
    def endElement(self, name, value, connection): ...

class Error:
    key: Any
    version_id: Any
    code: Any
    message: Any
    def __init__(
        self,
        key: Incomplete | None = ...,
        version_id: Incomplete | None = ...,
        code: Incomplete | None = ...,
        message: Incomplete | None = ...,
    ) -> None: ...
    def startElement(self, name, attrs, connection): ...
    def endElement(self, name, value, connection): ...

class MultiDeleteResult:
    bucket: Any
    deleted: Any
    errors: Any
    def __init__(self, bucket: Incomplete | None = ...) -> None: ...
    def startElement(self, name, attrs, connection): ...
    def endElement(self, name, value, connection): ...
