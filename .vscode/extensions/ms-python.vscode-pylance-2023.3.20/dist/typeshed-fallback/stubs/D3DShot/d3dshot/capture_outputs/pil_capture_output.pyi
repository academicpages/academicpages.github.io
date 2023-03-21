from _typeshed import Unused
from collections.abc import Sequence
from ctypes import _CVoidConstPLike
from typing import TypeVar

from d3dshot.capture_output import CaptureOutput
from PIL import Image

_ImageT = TypeVar("_ImageT", bound=Image.Image)

class PILCaptureOutput(CaptureOutput):
    def __init__(self) -> None: ...
    def process(
        self,
        pointer: _CVoidConstPLike,
        pitch: int,
        size: int,
        width: int,
        height: int,
        region: tuple[int, int, int, int],
        rotation: int,
    ) -> Image.Image: ...
    def to_pil(self, frame: _ImageT) -> _ImageT: ...
    def stack(self, frames: Sequence[_ImageT], stack_dimension: Unused) -> Sequence[_ImageT]: ...
