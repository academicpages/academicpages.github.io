from _typeshed import Incomplete, SupportsItems, SupportsRead, SupportsReadline
from collections.abc import Callable, Collection, Generator, Iterable, Mapping
from os import PathLike
from typing import Any, AnyStr, Protocol, overload
from typing_extensions import TypeAlias, TypedDict

_Keyword: TypeAlias = tuple[int | tuple[int, int] | tuple[int, str], ...] | None

GROUP_NAME: str
DEFAULT_KEYWORDS: dict[str, _Keyword]
DEFAULT_MAPPING: list[tuple[str, str]]
empty_msgid_warning: str

@overload
def extract_from_dir(
    dirname: AnyStr | PathLike[AnyStr],
    method_map: Iterable[tuple[str, str]] = ...,
    options_map: SupportsItems[str, dict[str, Any]] | None = ...,
    keywords: Mapping[str, _Keyword] = ...,
    comment_tags: Collection[str] = ...,
    callback: Callable[[AnyStr, str, dict[str, Any]], object] | None = ...,
    strip_comment_tags: bool = ...,
    directory_filter: Callable[[str], bool] | None = ...,
) -> Generator[tuple[AnyStr, int, str | tuple[str, ...], list[str], str | None], None, None]: ...
@overload
def extract_from_dir(
    dirname: None = ...,  # No dirname causes os.getcwd() to be used, producing str.
    method_map: Iterable[tuple[str, str]] = ...,
    options_map: SupportsItems[str, dict[str, Any]] | None = ...,
    keywords: Mapping[str, _Keyword] = ...,
    comment_tags: Collection[str] = ...,
    callback: Callable[[str, str, dict[str, Any]], object] | None = ...,
    strip_comment_tags: bool = ...,
    directory_filter: Callable[[str], bool] | None = ...,
) -> Generator[tuple[str, int, str | tuple[str, ...], list[str], str | None], None, None]: ...
def check_and_call_extract_file(
    filepath: AnyStr | PathLike[AnyStr],
    method_map: Iterable[tuple[str, str]],
    options_map: SupportsItems[str, dict[str, Any]],
    callback: Callable[[AnyStr, str, dict[str, Any]], object] | None,
    keywords: Mapping[str, _Keyword],
    comment_tags: Collection[str],
    strip_comment_tags,
    dirpath: Incomplete | None = ...,
) -> Generator[tuple[AnyStr, int, str | tuple[str, ...], list[str], str | None], None, None]: ...
def extract_from_file(
    method,
    filename: AnyStr | PathLike[AnyStr],
    keywords: Mapping[str, _Keyword] = ...,
    comment_tags: Collection[str] = ...,
    options: dict[str, Any] | None = ...,
    strip_comment_tags: bool = ...,
) -> list[tuple[AnyStr, int, str | tuple[str, ...], list[str], str | None]]: ...

class _FileObj(SupportsRead[bytes], SupportsReadline[bytes], Protocol):
    def seek(self, __offset: int, __whence: int = ...) -> int: ...
    def tell(self) -> int: ...

def extract(
    method,
    fileobj: _FileObj,
    keywords: Mapping[str, _Keyword] = ...,
    comment_tags: Collection[str] = ...,
    options: dict[str, Any] | None = ...,
    strip_comment_tags: bool = ...,
) -> Iterable[tuple[int, str | tuple[str, ...], list[str], str | None]]: ...
def extract_nothing(
    fileobj: _FileObj, keywords: Mapping[str, _Keyword], comment_tags: Collection[str], options: dict[str, Any]
) -> Iterable[tuple[int, str | tuple[str, ...], list[str], str | None]]: ...

class _PyOptions(TypedDict, total=False):
    encoding: str

def extract_python(
    fileobj: _FileObj, keywords: Mapping[str, _Keyword], comment_tags: Collection[str], options: _PyOptions
) -> Iterable[tuple[int, str | tuple[str, ...], list[str], str | None]]: ...

class _JSOptions(TypedDict, total=False):
    encoding: str
    jsx: bool
    template_string: bool

def extract_javascript(
    fileobj: _FileObj, keywords: Mapping[str, _Keyword], comment_tags: Collection[str], options: _JSOptions
) -> Iterable[tuple[int, str | tuple[str, ...], list[str], str | None]]: ...
