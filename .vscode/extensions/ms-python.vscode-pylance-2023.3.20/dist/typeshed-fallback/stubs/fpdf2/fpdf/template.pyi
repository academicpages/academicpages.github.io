from _typeshed import Incomplete
from typing import Any

__author__: str
__copyright__: str
__license__: str

class FlexTemplate:
    pdf: Any
    splitting_pdf: Any
    handlers: Any
    texts: Any
    def __init__(self, pdf, elements: Incomplete | None = ...) -> None: ...
    elements: Any
    keys: Any
    def load_elements(self, elements) -> None: ...
    def parse_csv(self, infile, delimiter: str = ..., decimal_sep: str = ..., encoding: Incomplete | None = ...): ...
    def __setitem__(self, name, value) -> None: ...
    set: Any
    def __contains__(self, name): ...
    def __getitem__(self, name): ...
    def split_multicell(self, text, element_name): ...
    def render(self, offsetx: float = ..., offsety: float = ..., rotate: float = ..., scale: float = ...): ...

class Template(FlexTemplate):
    def __init__(
        self,
        infile: Incomplete | None = ...,
        elements: Incomplete | None = ...,
        format: str = ...,
        orientation: str = ...,
        unit: str = ...,
        title: str = ...,
        author: str = ...,
        subject: str = ...,
        creator: str = ...,
        keywords: str = ...,
    ) -> None: ...
    def add_page(self) -> None: ...
    def render(self, outfile: Incomplete | None = ..., dest: Incomplete | None = ...) -> None: ...  # type: ignore[override]
