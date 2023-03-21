from _typeshed import Incomplete
from typing import Any
from typing_extensions import Literal, TypeAlias

from PIL.Image import Resampling

_ImageFilter: TypeAlias = Literal["AUTO", "FlateDecode", "DCTDecode", "JPXDecode"]

RESAMPLE: Resampling
SUPPORTED_IMAGE_FILTERS: tuple[_ImageFilter, ...]

def load_image(filename): ...

# Returned dict could be typed as a TypedDict.
def get_img_info(img, image_filter: _ImageFilter = ..., dims: Incomplete | None = ...) -> dict[str, Any]: ...
