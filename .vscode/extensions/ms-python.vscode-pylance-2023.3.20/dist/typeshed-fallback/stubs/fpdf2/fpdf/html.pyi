from _typeshed import Incomplete, Unused
from collections.abc import Callable
from html.parser import HTMLParser
from logging import Logger
from re import Match, Pattern
from typing import ClassVar
from typing_extensions import Final

from fpdf import FPDF

__author__: Final[str]
__copyright__: Final[str]
__license__: Final[str]

LOGGER: Logger
BULLET_WIN1252: Final[str]
DEFAULT_HEADING_SIZES: dict[str, int]
LEADING_SPACE: Pattern[str]
WHITESPACE: Pattern[str]
TRAILING_SPACE: Pattern[str]

COLOR_DICT: Final[dict[str, str]]

def px2mm(px: float) -> float: ...
def color_as_decimal(color: str | None = ...) -> tuple[int, int, int] | None: ...

class HTML2FPDF(HTMLParser):
    HTML_UNCLOSED_TAGS: ClassVar[tuple[str, ...]]
    pdf: Incomplete
    image_map: Incomplete
    li_tag_indent: Incomplete
    table_line_separators: Incomplete
    ul_bullet_char: Incomplete
    style: Incomplete
    href: str
    align: str
    page_links: Incomplete
    font_stack: Incomplete
    indent: int
    bullet: Incomplete
    font_size: Incomplete
    font_color: Incomplete
    table: Incomplete
    table_col_width: Incomplete
    table_col_index: Incomplete
    td: Incomplete
    th: Incomplete
    tr: Incomplete
    thead: Incomplete
    tfoot: Incomplete
    tr_index: Incomplete
    theader: Incomplete
    tfooter: Incomplete
    theader_out: bool
    table_row_height: int
    heading_level: Incomplete
    heading_sizes: Incomplete
    heading_above: float
    heading_below: float
    warn_on_tags_not_matching: bool
    def __init__(
        self,
        pdf: FPDF,
        image_map: Callable[[str], str] | None = None,
        li_tag_indent: int = 5,
        dd_tag_indent: int = 10,
        table_line_separators: bool = False,
        ul_bullet_char: str = ...,
        heading_sizes: Incomplete | None = None,
        warn_on_tags_not_matching: bool = True,
        **_: Unused,
    ): ...
    def width2unit(self, length): ...
    def handle_data(self, data) -> None: ...
    def box_shadow(self, w, h, bgcolor) -> None: ...
    def output_table_header(self) -> None: ...
    tfooter_out: bool
    def output_table_footer(self) -> None: ...
    def output_table_sep(self) -> None: ...
    font_face: Incomplete
    table_offset: Incomplete
    def handle_starttag(self, tag, attrs) -> None: ...
    tbody: Incomplete
    def handle_endtag(self, tag) -> None: ...
    h: Incomplete
    def set_font(self, face: Incomplete | None = ..., size: Incomplete | None = ...) -> None: ...
    def set_style(self, tag: Incomplete | None = ..., enable: bool = ...) -> None: ...
    def set_text_color(self, r: Incomplete | None = ..., g: int = ..., b: int = ...) -> None: ...
    def put_link(self, txt) -> None: ...
    def render_toc(self, pdf, outline) -> None: ...
    def error(self, message: str) -> None: ...

def leading_whitespace_repl(matchobj: Match[str]) -> str: ...
def whitespace_repl(matchobj: Match[str]) -> str: ...

class HTMLMixin:
    def __init__(self, *args: Incomplete, **kwargs: Incomplete) -> None: ...
