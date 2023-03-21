from _typeshed import FileDescriptorOrPath, Incomplete, SupportsRead
from enum import IntEnum
from typing import Protocol
from typing_extensions import Literal

class Layout(IntEnum):
    BASIC: Literal[0]
    RAQM: Literal[1]

LAYOUT_BASIC: Literal[Layout.BASIC]
LAYOUT_RAQM: Literal[Layout.RAQM]

class _Font(Protocol):
    def getmask(self, text: str | bytes, mode: str = ..., direction=..., features=...): ...

class ImageFont:
    def getsize(self, text: str | bytes, *args, **kwargs) -> tuple[int, int]: ...
    def getmask(self, text: str | bytes, mode: str = ..., direction=..., features=...): ...

class FreeTypeFont:
    path: str | bytes | SupportsRead[bytes] | None
    size: int
    index: int
    encoding: str
    layout_engine: Layout
    def __init__(
        self,
        font: str | bytes | SupportsRead[bytes] | None = ...,
        size: int = ...,
        index: int = ...,
        encoding: str = ...,
        layout_engine: Layout | None = ...,
    ) -> None: ...
    def getname(self) -> tuple[str, str]: ...
    def getmetrics(self) -> tuple[int, int]: ...
    def getlength(
        self,
        text: str | bytes,
        mode: str = ...,
        direction: Literal["ltr", "rtl", "ttb"] | None = ...,
        features: Incomplete | None = ...,
        language: str | None = ...,
    ) -> int: ...
    def getbbox(
        self,
        text: str | bytes,
        mode: str = ...,
        direction=...,
        features=...,
        language: str | None = ...,
        stroke_width: int = ...,
        anchor: str | None = ...,
    ) -> tuple[int, int, int, int]: ...
    def getsize(
        self,
        text: str | bytes,
        direction: Literal["ltr", "rtl", "ttb"] | None = ...,
        features: Incomplete | None = ...,
        language: str | None = ...,
        stroke_width: int = ...,
    ) -> tuple[int, int]: ...
    def getsize_multiline(
        self,
        text: str | bytes,
        direction: Literal["ltr", "rtl", "ttb"] | None = ...,
        spacing: float = ...,
        features: Incomplete | None = ...,
        language: str | None = ...,
        stroke_width: float = ...,
    ) -> tuple[int, int]: ...
    def getoffset(self, text: str | bytes) -> tuple[int, int]: ...
    def getmask(
        self,
        text: str | bytes,
        mode: str = ...,
        direction: Literal["ltr", "rtl", "ttb"] | None = ...,
        features: Incomplete | None = ...,
        language: str | None = ...,
        stroke_width: float = ...,
        anchor: str | None = ...,
        ink=...,
        start: tuple[float, float] | None = ...,
    ): ...
    def getmask2(
        self,
        text: str | bytes,
        mode: str = ...,
        fill=...,
        direction: Literal["ltr", "rtl", "ttb"] | None = ...,
        features: Incomplete | None = ...,
        language: str | None = ...,
        stroke_width: float = ...,
        anchor: str | None = ...,
        ink=...,
        start: tuple[float, float] | None = ...,
        *args,
        **kwargs,
    ): ...
    def font_variant(
        self,
        font: str | bytes | SupportsRead[bytes] | None = ...,
        size: int | None = ...,
        index: int | None = ...,
        encoding: str | None = ...,
        layout_engine: Layout | None = ...,
    ) -> FreeTypeFont: ...
    def get_variation_names(self): ...
    def set_variation_by_name(self, name): ...
    def get_variation_axes(self): ...
    def set_variation_by_axes(self, axes): ...

class TransposedFont:
    def __init__(self, font: _Font, orientation: int | None = ...) -> None: ...
    def getsize(self, text: str | bytes, *args, **kwargs) -> tuple[int, int]: ...
    def getmask(self, text: str | bytes, mode: str = ..., *args, **kwargs): ...

def load(filename: FileDescriptorOrPath) -> ImageFont: ...
def truetype(
    font: str | bytes | SupportsRead[bytes] | None = ...,
    size: int = ...,
    index: int = ...,
    encoding: str = ...,
    layout_engine: Layout | None = ...,
) -> FreeTypeFont: ...
def load_path(filename: str | bytes) -> ImageFont: ...
def load_default() -> ImageFont: ...
