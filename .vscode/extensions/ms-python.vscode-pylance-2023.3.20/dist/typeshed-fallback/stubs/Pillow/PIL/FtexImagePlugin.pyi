from enum import IntEnum
from typing import ClassVar
from typing_extensions import Literal

from .ImageFile import ImageFile

MAGIC: bytes

class Format(IntEnum):
    DXT1: int
    UNCOMPRESSED: int

FORMAT_DXT1: Literal[Format.DXT1]
FORMAT_UNCOMPRESSED: Literal[Format.UNCOMPRESSED]

class FtexImageFile(ImageFile):
    format: ClassVar[Literal["FTEX"]]
    format_description: ClassVar[str]
    def load_seek(self, pos) -> None: ...
