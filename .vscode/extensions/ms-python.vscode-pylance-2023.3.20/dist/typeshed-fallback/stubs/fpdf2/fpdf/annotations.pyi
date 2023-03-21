from _typeshed import Incomplete
from datetime import datetime
from typing import NamedTuple

from .actions import Action
from .enums import AnnotationFlag, AnnotationName, FileAttachmentAnnotationName
from .syntax import Destination, Name, PDFContentStream, PDFObject

DEFAULT_ANNOT_FLAGS: Incomplete

class AnnotationMixin:
    type: Name
    subtype: Name
    rect: str
    border: str
    f_t: Name | None
    v: Incomplete | None
    f: int  # AnnotationFlags
    contents: str | None
    a: Action | None
    dest: Destination | None
    c: str | None
    t: str | None
    m: str | None
    quad_points: str | None
    p: Incomplete | None
    name: AnnotationName | FileAttachmentAnnotationName | None
    ink_list: str | None
    f_s: str | None
    def __init__(
        self,
        subtype: str,
        x: int,
        y: int,
        width: int,
        height: int,
        flags: tuple[AnnotationFlag, ...] = ...,
        contents: str | None = ...,
        dest: Destination | None = ...,
        action: Action | None = ...,
        color: tuple[int, int, int] | None = ...,
        modification_time: datetime | None = ...,
        title: str | None = ...,
        quad_points: tuple[float, ...] | None = ...,  # multiple of 8 floats
        border_width: int = ...,
        name: AnnotationName | FileAttachmentAnnotationName | None = ...,
        ink_list: tuple[int, ...] = ...,
        file_spec: str | None = ...,
        field_type: str | None = ...,
        value: Incomplete | None = ...,
    ) -> None: ...

class PDFAnnotation(AnnotationMixin, PDFObject): ...

class AnnotationDict(AnnotationMixin):
    def serialize(self) -> str: ...

class PDFEmbeddedFile(PDFContentStream):
    type: Name
    params: str
    def __init__(
        self,
        basename: str,
        contents: bytes,
        desc: str = ...,
        creation_date: datetime | None = ...,
        modification_date: datetime | None = ...,
        compress: bool = ...,
        checksum: bool = ...,
    ) -> None: ...
    def globally_enclosed(self) -> bool: ...
    def set_globally_enclosed(self, value: bool) -> None: ...
    def basename(self) -> str: ...
    def file_spec(self) -> FileSpec: ...

class FileSpec(NamedTuple):
    embedded_file: PDFEmbeddedFile
    basename: str
    desc: str
    def serialize(self) -> str: ...
