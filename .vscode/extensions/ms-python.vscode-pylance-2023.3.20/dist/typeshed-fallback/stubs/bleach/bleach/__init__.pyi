from collections.abc import Container, Iterable
from typing_extensions import TypeAlias

from .callbacks import _Callback
from .css_sanitizer import CSSSanitizer
from .linkifier import DEFAULT_CALLBACKS as DEFAULT_CALLBACKS, Linker as Linker
from .sanitizer import (
    ALLOWED_ATTRIBUTES as ALLOWED_ATTRIBUTES,
    ALLOWED_PROTOCOLS as ALLOWED_PROTOCOLS,
    ALLOWED_TAGS as ALLOWED_TAGS,
    Cleaner as Cleaner,
    _Attributes,
)

__all__ = ["clean", "linkify"]

__releasedate__: str
__version__: str

_HTMLAttrKey: TypeAlias = tuple[str | None, str]  # noqa: Y047

def clean(
    text: str,
    tags: Iterable[str] = ...,
    attributes: _Attributes = ...,
    protocols: Iterable[str] = ...,
    strip: bool = ...,
    strip_comments: bool = ...,
    css_sanitizer: CSSSanitizer | None = ...,
) -> str: ...
def linkify(
    text: str, callbacks: Iterable[_Callback] = ..., skip_tags: Container[str] | None = ..., parse_email: bool = ...
) -> str: ...
