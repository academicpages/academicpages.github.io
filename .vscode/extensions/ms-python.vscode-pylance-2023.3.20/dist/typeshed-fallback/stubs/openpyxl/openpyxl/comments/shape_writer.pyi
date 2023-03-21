from _typeshed import Incomplete

vmlns: str
officens: str
excelns: str

class ShapeWriter:
    vml: Incomplete
    vml_path: Incomplete
    comments: Incomplete
    def __init__(self, comments) -> None: ...
    def add_comment_shapetype(self, root) -> None: ...
    def add_comment_shape(self, root, idx, coord, height, width) -> None: ...
    def write(self, root): ...
