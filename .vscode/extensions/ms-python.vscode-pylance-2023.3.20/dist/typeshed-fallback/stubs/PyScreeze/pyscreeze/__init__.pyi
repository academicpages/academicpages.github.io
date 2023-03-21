from _typeshed import Incomplete, StrOrBytesPath, Unused
from collections.abc import Callable, Generator
from typing import NamedTuple, SupportsFloat, TypeVar, overload
from typing_extensions import Final, ParamSpec, SupportsIndex, TypeAlias

from PIL import Image

_P = ParamSpec("_P")
_R = TypeVar("_R")
# TODO: cv2.Mat is not available as a type yet:
# https://github.com/microsoft/python-type-stubs/issues/211
# https://github.com/microsoft/python-type-stubs/tree/main/cv2
# https://github.com/opencv/opencv/pull/20370
# cv2.Mat is just an alias for a numpy NDArray, but can't import that either.
# Because pyscreeze does not declare it as a dependency, stub_uploader won't let it.
_Mat: TypeAlias = Incomplete

useOpenCV: Final[bool]
RUNNING_PYTHON_2: Final = False
GRAYSCALE_DEFAULT: Final = False
scrotExists: Final[bool]
# Meant to be overridable for backward-compatibility
USE_IMAGE_NOT_FOUND_EXCEPTION: bool

class Box(NamedTuple):
    left: int
    top: int
    width: int
    height: int

class Point(NamedTuple):
    x: int
    y: int

class RGB(NamedTuple):
    red: int
    green: int
    blue: int

class PyScreezeException(Exception): ...
class ImageNotFoundException(PyScreezeException): ...

# _locateAll_opencv
def requiresPillow(wrappedFunction: Callable[_P, _R]) -> Callable[_P, _R]: ...
@overload
def locate(
    needleImage: str | Image.Image | _Mat,
    haystackImage: str | Image.Image | _Mat,
    *,
    grayscale: bool | None = None,
    limit: Unused = 1,
    region: tuple[int, int, int, int] | None = None,
    step: int = 1,
    confidence: SupportsFloat | SupportsIndex | str = 0.999,
) -> Box | None: ...

# _locateAll_python / _locateAll_pillow
@overload
def locate(
    needleImage: str | Image.Image,
    haystackImage: str | Image.Image,
    *,
    grayscale: bool | None = None,
    limit: Unused = 1,
    region: tuple[int, int, int, int] | None = None,
    step: int = 1,
    confidence: None = None,
) -> Box | None: ...

# _locateAll_opencv
@overload
def locateOnScreen(
    image: str | Image.Image | _Mat,
    minSearchTime: float = 0,
    *,
    grayscale: bool | None = None,
    limit: Unused = 1,
    region: tuple[int, int, int, int] | None = None,
    step: int = 1,
    confidence: SupportsFloat | SupportsIndex | str = 0.999,
) -> Box | None: ...

# _locateAll_python / _locateAll_pillow
@overload
def locateOnScreen(
    image: str | Image.Image,
    minSearchTime: float = 0,
    *,
    grayscale: bool | None = None,
    limit: Unused = 1,
    region: tuple[int, int, int, int] | None = None,
    step: int = 1,
    confidence: None = None,
) -> Box | None: ...

# _locateAll_opencv
@overload
def locateAllOnScreen(
    image: str | Image.Image | _Mat,
    *,
    grayscale: bool | None = None,
    limit: int = 1000,
    region: tuple[int, int, int, int] | None = None,
    step: int = 1,
    confidence: SupportsFloat | SupportsIndex | str = 0.999,
) -> Generator[Box, None, None]: ...

# _locateAll_python / _locateAll_pillow
@overload
def locateAllOnScreen(
    image: str | Image.Image,
    *,
    grayscale: bool | None = None,
    limit: int | None = None,
    region: tuple[int, int, int, int] | None = None,
    step: int = 1,
    confidence: None = None,
) -> Generator[Box, None, None]: ...

# _locateAll_opencv
@overload
def locateCenterOnScreen(
    image: str | Image.Image | _Mat,
    *,
    minSearchTime: float,
    grayscale: bool | None = None,
    limit: Unused = 1,
    region: tuple[int, int, int, int] | None = None,
    step: int = 1,
    confidence: SupportsFloat | SupportsIndex | str = 0.999,
) -> Point | None: ...

# _locateAll_python / _locateAll_pillow
@overload
def locateCenterOnScreen(
    image: str | Image.Image,
    *,
    minSearchTime: float,
    grayscale: bool | None = None,
    limit: Unused = 1,
    region: tuple[int, int, int, int] | None = None,
    step: int = 1,
    confidence: None = None,
) -> Point | None: ...

# _locateAll_opencv
@overload
def locateOnWindow(
    image: str | Image.Image | _Mat,
    title: str,
    *,
    grayscale: bool | None = None,
    limit: Unused = 1,
    step: int = 1,
    confidence: SupportsFloat | SupportsIndex | str = 0.999,
) -> Box | None: ...

# _locateAll_python / _locateAll_pillow
@overload
def locateOnWindow(
    image: str | Image.Image,
    title: str,
    *,
    grayscale: bool | None = None,
    limit: Unused = 1,
    step: int = 1,
    confidence: None = None,
) -> Box | None: ...
def showRegionOnScreen(
    region: tuple[int, int, int, int], outlineColor: str = "red", filename: str = "_showRegionOnScreen.png"
) -> None: ...
def center(coords: tuple[int, int, int, int]) -> Point: ...
def pixelMatchesColor(
    x: int, y: int, expectedRGBColor: tuple[int, int, int] | tuple[int, int, int, int], tolerance: int = 0
) -> bool: ...
def pixel(x: int, y: int) -> tuple[int, int, int]: ...
def screenshot(imageFilename: StrOrBytesPath | None = None, region: tuple[int, int, int, int] | None = None) -> Image.Image: ...

grab = screenshot

# _locateAll_opencv
@overload
def locateAll(
    needleImage: str | Image.Image | _Mat,
    haystackImage: str | Image.Image | _Mat,
    grayscale: bool | None = None,
    limit: int = 1000,
    region: tuple[int, int, int, int] | None = None,
    step: int = 1,
    confidence: SupportsFloat | SupportsIndex | str = 0.999,
) -> Generator[Box, None, None]: ...

# _locateAll_python / _locateAll_pillow
@overload
def locateAll(
    needleImage: str | Image.Image,
    haystackImage: str | Image.Image,
    grayscale: bool | None = None,
    limit: int | None = None,
    region: tuple[int, int, int, int] | None = None,
    step: int = 1,
    confidence: None = None,
) -> Generator[Box, None, None]: ...
