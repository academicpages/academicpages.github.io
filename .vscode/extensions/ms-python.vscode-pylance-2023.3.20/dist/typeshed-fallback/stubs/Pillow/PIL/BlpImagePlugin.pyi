from enum import IntEnum
from typing import Any, ClassVar
from typing_extensions import Literal

from .ImageFile import ImageFile, PyDecoder

class Format(IntEnum):
    JPEG: int

BLP_FORMAT_JPEG: Literal[Format.JPEG]

class Encoding(IntEnum):
    UNCOMPRESSED: int
    DXT: int
    UNCOMPRESSED_RAW_BGRA: int

BLP_ENCODING_UNCOMPRESSED: Literal[Encoding.UNCOMPRESSED]
BLP_ENCODING_DXT: Literal[Encoding.DXT]
BLP_ENCODING_UNCOMPRESSED_RAW_BGRA: Literal[Encoding.UNCOMPRESSED_RAW_BGRA]

class AlphaEncoding(IntEnum):
    DXT1: int
    DXT3: int
    DXT5: int

BLP_ALPHA_ENCODING_DXT1: Literal[AlphaEncoding.DXT1]
BLP_ALPHA_ENCODING_DXT3: Literal[AlphaEncoding.DXT3]
BLP_ALPHA_ENCODING_DXT5: Literal[AlphaEncoding.DXT5]

def unpack_565(i): ...
def decode_dxt1(data, alpha: bool = ...): ...
def decode_dxt3(data): ...
def decode_dxt5(data): ...

class BLPFormatError(NotImplementedError): ...

class BlpImageFile(ImageFile):
    format: ClassVar[Literal["BLP"]]
    format_description: ClassVar[str]

class _BLPBaseDecoder(PyDecoder):
    magic: Any
    def decode(self, buffer): ...

class BLP1Decoder(_BLPBaseDecoder): ...
class BLP2Decoder(_BLPBaseDecoder): ...
