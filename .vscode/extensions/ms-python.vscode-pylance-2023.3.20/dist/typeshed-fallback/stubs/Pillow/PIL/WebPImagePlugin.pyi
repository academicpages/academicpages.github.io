from typing import Any, ClassVar
from typing_extensions import Literal, TypeAlias

from .ImageFile import ImageFile

SUPPORTED: bool
_XMP_Tags: TypeAlias = dict[str, str | _XMP_Tags]

class WebPImageFile(ImageFile):
    format: ClassVar[Literal["WEBP"]]
    format_description: ClassVar[str]
    def getxmp(self) -> _XMP_Tags: ...
    def seek(self, frame) -> None: ...
    fp: Any
    tile: Any
    def load(self): ...
    def tell(self): ...
