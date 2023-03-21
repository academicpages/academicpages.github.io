import datetime
from _typeshed import Incomplete, StrPath
from collections.abc import Callable, Iterable, Sequence
from contextlib import _GeneratorContextManager
from io import BytesIO
from pathlib import PurePath
from re import Pattern
from typing import Any, ClassVar, NamedTuple, overload
from typing_extensions import Literal, TypeAlias

from fpdf import ViewerPreferences
from PIL import Image

from .annotations import AnnotationDict, PDFEmbeddedFile
from .drawing import DrawingContext, PaintedPath
from .enums import (
    Align,
    AnnotationFlag,
    AnnotationName,
    Corner,
    FileAttachmentAnnotationName,
    PageLayout,
    PathPaintRule,
    RenderStyle,
    TextMarkupType,
    TextMode as TextMode,
    XPos as XPos,
    YPos as YPos,
)
from .html import HTML2FPDF
from .output import PDFPage
from .recorder import FPDFRecorder
from .structure_tree import StructureTreeBuilder
from .syntax import DestinationXYZ
from .util import _Unit

__all__ = ["FPDF", "XPos", "YPos", "get_page_format", "TextMode", "TitleStyle", "PAGE_FORMATS"]

_Orientation: TypeAlias = Literal["", "portrait", "p", "P", "landscape", "l", "L"]
_Format: TypeAlias = Literal["", "a3", "A3", "a4", "A4", "a5", "A5", "letter", "Letter", "legal", "Legal"]
_FontStyle: TypeAlias = Literal["", "B", "I"]
_FontStyles: TypeAlias = Literal["", "B", "I", "U", "BU", "UB", "BI", "IB", "IU", "UI", "BIU", "BUI", "IBU", "IUB", "UBI", "UIB"]
PAGE_FORMATS: dict[_Format, tuple[float, float]]

class TitleStyle(NamedTuple):
    font_family: str | None = ...
    font_style: str | None = ...
    font_size_pt: int | None = ...
    color: int | tuple[int, int, int] | None = ...
    underline: bool = ...
    t_margin: int | None = ...
    l_margin: int | None = ...
    b_margin: int | None = ...

class ToCPlaceholder(NamedTuple):
    render_function: Callable[[FPDF, Any], object]
    start_page: int
    y: int
    pages: int = ...

class SubsetMap:
    def __init__(self, identities: Iterable[int]) -> None: ...
    def __len__(self) -> int: ...
    def pick(self, unicode: int) -> int: ...
    def dict(self) -> dict[int, int]: ...

def get_page_format(format: _Format | tuple[float, float], k: float | None = ...) -> tuple[float, float]: ...

# TODO: TypedDicts
_Font: TypeAlias = dict[str, Any]
_Image: TypeAlias = dict[str, Any]

class FPDF:
    MARKDOWN_BOLD_MARKER: ClassVar[str]
    MARKDOWN_ITALICS_MARKER: ClassVar[str]
    MARKDOWN_UNDERLINE_MARKER: ClassVar[str]
    MARKDOWN_LINK_REGEX: ClassVar[Pattern[str]]
    MARKDOWN_LINK_COLOR: ClassVar[Incomplete | None]

    HTML2FPDF_CLASS: ClassVar[type[HTML2FPDF]]

    page: int
    pages: dict[int, PDFPage]
    fonts: dict[str, _Font]
    images: dict[str, _Image]
    links: dict[int, DestinationXYZ]
    embedded_files: list[PDFEmbeddedFile]

    in_footer: bool
    str_alias_nb_pages: str

    xmp_metadata: str | None
    image_filter: str
    page_duration: int
    page_transition: Incomplete | None
    allow_images_transparency: bool
    oversized_images: Incomplete | None
    oversized_images_ratio: float
    struct_builder: StructureTreeBuilder
    section_title_styles: dict[int, Incomplete]

    core_fonts: dict[str, str]
    core_fonts_encoding: str
    font_aliases: dict[str, str]
    k: float

    font_family: str
    font_style: str
    font_size_pt: float
    font_stretching: float
    char_spacing: float
    underline: bool
    current_font: _Font
    draw_color: str
    fill_color: str
    text_color: str
    page_background: Incomplete | None
    dash_pattern: dict[str, int]  # TODO: TypedDict
    line_width: float
    text_mode: TextMode

    dw_pt: float
    dh_pt: float
    def_orientation: Literal["P", "L"]
    x: float
    y: float
    l_margin: float
    t_margin: float
    c_margin: float
    viewer_preferences: ViewerPreferences | None
    compress: bool
    pdf_version: str
    creation_date: datetime.datetime

    buffer: bytearray | None

    # Set during call to _set_orientation(), called from __init__().
    cur_orientation: Literal["P", "L"]
    w_pt: float
    h_pt: float
    w: float
    h: float

    def __init__(
        self,
        orientation: _Orientation = ...,
        unit: _Unit | float = ...,
        format: _Format | tuple[float, float] = ...,
        font_cache_dir: Literal["DEPRECATED"] = ...,
    ) -> None: ...
    # The following definition crashes stubtest 0.991, but seems to be fixed
    # in later versions.
    # def set_encryption(
    #    self,
    #    owner_password: str,
    #    user_password: str | None = None,
    #    encryption_method: EncryptionMethod | str = ...,
    #    permissions: AccessPermission = ...,
    #    encrypt_metadata: bool = False,
    # ) -> None: ...
    # args and kwargs are passed to HTML2FPDF_CLASS constructor.
    def write_html(self, text: str, *args: Any, **kwargs: Any) -> None: ...
    @property
    def is_ttf_font(self) -> bool: ...
    @property
    def page_mode(self): ...
    @property
    def epw(self) -> float: ...
    @property
    def eph(self) -> float: ...
    @property
    def pages_count(self) -> int: ...
    def set_margin(self, margin: float) -> None: ...
    def set_margins(self, left: float, top: float, right: float = ...) -> None: ...
    def set_left_margin(self, margin: float) -> None: ...
    def set_top_margin(self, margin: float) -> None: ...
    r_margin: float
    def set_right_margin(self, margin: float) -> None: ...
    auto_page_break: bool
    b_margin: float
    page_break_trigger: float
    def set_auto_page_break(self, auto: bool, margin: float = ...) -> None: ...
    @property
    def default_page_dimensions(self) -> tuple[float, float]: ...
    zoom_mode: Literal["fullpage", "fullwidth", "real", "default"] | float
    page_layout: PageLayout | None
    def set_display_mode(
        self,
        zoom: Literal["fullpage", "fullwidth", "real", "default"] | float,
        layout: Literal["single", "continuous", "two", "default"] = ...,
    ) -> None: ...
    def set_compression(self, compress: bool) -> None: ...
    title: str
    def set_title(self, title: str) -> None: ...
    lang: str
    def set_lang(self, lang: str) -> None: ...
    subject: str
    def set_subject(self, subject: str) -> None: ...
    author: str
    def set_author(self, author: str) -> None: ...
    keywords: str
    def set_keywords(self, keywords: str) -> None: ...
    creator: str
    def set_creator(self, creator: str) -> None: ...
    producer: str
    def set_producer(self, producer: str) -> None: ...
    def set_creation_date(self, date: datetime.datetime) -> None: ...
    def set_xmp_metadata(self, xmp_metadata: str) -> None: ...
    def set_doc_option(self, opt: str, value: str) -> None: ...
    def set_image_filter(self, image_filter: str) -> None: ...
    def alias_nb_pages(self, alias: str = ...) -> None: ...
    def add_page(
        self,
        orientation: _Orientation = ...,
        format: _Format | tuple[float, float] = ...,
        same: bool = ...,
        duration: int = ...,
        transition: Incomplete | None = ...,
    ) -> None: ...
    def header(self) -> None: ...
    def footer(self) -> None: ...
    def page_no(self) -> int: ...
    def set_draw_color(self, r: int, g: int = ..., b: int = ...) -> None: ...
    def set_fill_color(self, r: int, g: int = ..., b: int = ...) -> None: ...
    def set_text_color(self, r: int, g: int = ..., b: int = ...) -> None: ...
    def get_string_width(self, s: str, normalized: bool = ..., markdown: bool = ...) -> float: ...
    def set_line_width(self, width: float) -> None: ...
    def set_page_background(self, background) -> None: ...
    def drawing_context(self, debug_stream: Incomplete | None = ...) -> _GeneratorContextManager[DrawingContext]: ...
    def new_path(
        self, x: float = ..., y: float = ..., paint_rule: PathPaintRule = ..., debug_stream: Incomplete | None = ...
    ) -> _GeneratorContextManager[PaintedPath]: ...
    def draw_path(self, path: PaintedPath, debug_stream: Incomplete | None = ...) -> None: ...
    def set_dash_pattern(self, dash: float = ..., gap: float = ..., phase: float = ...) -> None: ...
    def line(self, x1: float, y1: float, x2: float, y2: float) -> None: ...
    def polyline(
        self, point_list: list[tuple[float, float]], fill: bool = ..., polygon: bool = ..., style: RenderStyle | str | None = ...
    ) -> None: ...
    def polygon(self, point_list: list[tuple[float, float]], fill: bool = ..., style: RenderStyle | str | None = ...) -> None: ...
    def dashed_line(self, x1, y1, x2, y2, dash_length: int = ..., space_length: int = ...) -> None: ...
    def rect(
        self,
        x: float,
        y: float,
        w: float,
        h: float,
        style: RenderStyle | str | None = ...,
        round_corners: tuple[str, ...] | tuple[Corner, ...] | bool = ...,
        corner_radius: float = ...,
    ) -> None: ...
    def ellipse(self, x: float, y: float, w: float, h: float, style: RenderStyle | str | None = ...) -> None: ...
    def circle(self, x: float, y: float, r, style: RenderStyle | str | None = ...) -> None: ...
    def regular_polygon(
        self,
        x: float,
        y: float,
        numSides: int,
        polyWidth: float,
        rotateDegrees: float = ...,
        style: RenderStyle | str | None = ...,
    ): ...
    def star(
        self,
        x: float,
        y: float,
        r_in: float,
        r_out: float,
        corners: int,
        rotate_degrees: float = ...,
        style: RenderStyle | str | None = ...,
    ): ...
    def arc(
        self,
        x: float,
        y: float,
        a: float,
        start_angle: float,
        end_angle: float,
        b: float | None = ...,
        inclination: float = ...,
        clockwise: bool = ...,
        start_from_center: bool = ...,
        end_at_center: bool = ...,
        style: RenderStyle | str | None = ...,
    ) -> None: ...
    def solid_arc(
        self,
        x: float,
        y: float,
        a: float,
        start_angle: float,
        end_angle: float,
        b: float | None = ...,
        inclination: float = ...,
        clockwise: bool = ...,
        style: RenderStyle | str | None = ...,
    ) -> None: ...
    def add_font(
        self,
        family: str | None = None,
        style: _FontStyle = "",
        fname: str | PurePath | None = None,
        uni: bool | Literal["DEPRECATED"] = "DEPRECATED",
    ) -> None: ...
    def set_font(self, family: str | None = ..., style: _FontStyles = ..., size: int = ...) -> None: ...
    def set_font_size(self, size: float) -> None: ...
    def set_char_spacing(self, spacing: float) -> None: ...
    def set_stretching(self, stretching: float) -> None: ...
    def add_link(self, y: float = 0, x: float = 0, page: int = -1, zoom: float | Literal["null"] = "null") -> int: ...
    def set_link(self, link, y: float = 0, x: float = 0, page: int = -1, zoom: float | Literal["null"] = "null") -> None: ...
    def link(
        self, x: float, y: float, w: float, h: float, link: str | int, alt_text: str | None = ..., border_width: int = ...
    ) -> AnnotationDict: ...
    def embed_file(
        self,
        file_path: StrPath | None = ...,
        bytes: bytes | None = ...,
        basename: str | None = ...,
        modification_date: datetime.datetime | None = ...,
        *,
        creation_date: datetime.datetime | None = ...,
        desc: str = ...,
        compress: bool = ...,
        checksum: bool = ...,
    ) -> str: ...
    def file_attachment_annotation(
        self,
        file_path: StrPath,
        x: float,
        y: float,
        w: float = ...,
        h: float = ...,
        name: FileAttachmentAnnotationName | str | None = ...,
        flags: Iterable[AnnotationFlag | str] = ...,
        *,
        bytes: bytes | None = ...,
        basename: str | None = ...,
        creation_date: datetime.datetime | None = ...,
        modification_date: datetime.datetime | None = ...,
        desc: str = ...,
        compress: bool = ...,
        checksum: bool = ...,
    ) -> AnnotationDict: ...
    def text_annotation(
        self,
        x: float,
        y: float,
        text: str,
        w: float = ...,
        h: float = ...,
        name: AnnotationName | str | None = ...,
        flags: tuple[AnnotationFlag, ...] | tuple[str, ...] = ...,
    ) -> None: ...
    def add_action(self, action, x: float, y: float, w: float, h: float) -> None: ...
    def highlight(
        self,
        text: str,
        title: str = ...,
        type: TextMarkupType | str = ...,
        color: tuple[float, float, float] = ...,
        modification_time: datetime.datetime | None = ...,
    ) -> _GeneratorContextManager[None]: ...
    add_highlight = highlight
    def add_text_markup_annotation(
        self,
        type: str,
        text: str,
        quad_points: Sequence[int],
        title: str = ...,
        color: tuple[float, float, float] = ...,
        modification_time: datetime.datetime | None = ...,
        page: int | None = ...,
    ) -> AnnotationDict: ...
    def ink_annotation(
        self,
        coords: Iterable[Incomplete],
        contents: str = ...,
        title: str = ...,
        color: Sequence[float] = ...,
        border_width: int = ...,
    ) -> AnnotationDict: ...
    def text(self, x: float, y: float, txt: str = ...) -> None: ...
    def rotate(self, angle: float, x: float | None = ..., y: float | None = ...) -> None: ...
    def rotation(self, angle: float, x: float | None = ..., y: float | None = ...) -> _GeneratorContextManager[None]: ...
    def skew(
        self, ax: float = 0, ay: float = 0, x: float | None = None, y: float | None = None
    ) -> _GeneratorContextManager[None]: ...
    def local_context(
        self,
        font_family: Incomplete | None = ...,
        font_style: Incomplete | None = ...,
        font_size: Incomplete | None = ...,
        line_width: Incomplete | None = ...,
        draw_color: Incomplete | None = ...,
        fill_color: Incomplete | None = ...,
        text_color: Incomplete | None = ...,
        dash_pattern: Incomplete | None = ...,
        **kwargs,
    ) -> _GeneratorContextManager[None]: ...
    @property
    def accept_page_break(self) -> bool: ...
    def cell(
        self,
        w: float | None = ...,
        h: float | None = ...,
        txt: str = ...,
        border: bool | Literal[0, 1] | str = ...,
        ln: int | Literal["DEPRECATED"] = ...,
        align: str | Align = ...,
        fill: bool = ...,
        link: str = ...,
        center: bool | Literal["DEPRECATED"] = ...,
        markdown: bool = ...,
        new_x: XPos | str = ...,
        new_y: YPos | str = ...,
    ) -> bool: ...
    def will_page_break(self, height: float) -> bool: ...
    def multi_cell(
        self,
        w: float,
        h: float | None = ...,
        txt: str = ...,
        border: bool | Literal[0, 1] | str = ...,
        align: str | Align = ...,
        fill: bool = ...,
        split_only: bool = ...,
        link: str | int = ...,
        ln: int | Literal["DEPRECATED"] = ...,
        max_line_height: float | None = ...,
        markdown: bool = ...,
        print_sh: bool = ...,
        new_x: XPos | str = ...,
        new_y: YPos | str = ...,
    ): ...
    def write(self, h: float | None = ..., txt: str = ..., link: str = ..., print_sh: bool = ...) -> None: ...
    def image(
        self,
        name: str | Image.Image | BytesIO | StrPath,
        x: float | Align | None = None,
        y: float | None = None,
        w: float = 0,
        h: float = 0,
        type: str = "",
        link: str = "",
        title: str | None = None,
        alt_text: str | None = None,
        dims: tuple[float, float] | None = None,
    ) -> _Image: ...
    def ln(self, h: float | None = ...) -> None: ...
    def get_x(self) -> float: ...
    def set_x(self, x: float) -> None: ...
    def get_y(self) -> float: ...
    def set_y(self, y: float) -> None: ...
    def set_xy(self, x: float, y: float) -> None: ...
    @overload
    def output(self, name: Literal[""] = ...) -> bytearray: ...  # type: ignore[misc]
    @overload
    def output(self, name: str) -> None: ...
    def normalize_text(self, txt: str) -> str: ...
    def sign_pkcs12(
        self,
        pkcs_filepath: str,
        password: bytes | None = ...,
        hashalgo: str = ...,
        contact_info: str | None = ...,
        location: str | None = ...,
        signing_time: datetime.datetime | None = ...,
        reason: str | None = ...,
        flags: tuple[AnnotationFlag, ...] = ...,
    ) -> None: ...
    def sign(
        self,
        key,
        cert,
        extra_certs: Sequence[Incomplete] = ...,
        hashalgo: str = ...,
        contact_info: str | None = ...,
        location: str | None = ...,
        signing_time: datetime.datetime | None = ...,
        reason: str | None = ...,
        flags: tuple[AnnotationFlag, ...] = ...,
    ) -> None: ...
    def file_id(self) -> str: ...
    def interleaved2of5(self, txt, x: float, y: float, w: float = ..., h: float = ...) -> None: ...
    def code39(self, txt, x: float, y: float, w: float = ..., h: float = ...) -> None: ...
    def rect_clip(self, x: float, y: float, w: float, h: float) -> _GeneratorContextManager[None]: ...
    def elliptic_clip(self, x: float, y: float, w: float, h: float) -> _GeneratorContextManager[None]: ...
    def round_clip(self, x: float, y: float, r: float) -> _GeneratorContextManager[None]: ...
    def unbreakable(self) -> _GeneratorContextManager[FPDFRecorder]: ...
    def offset_rendering(self) -> _GeneratorContextManager[FPDFRecorder]: ...
    def insert_toc_placeholder(self, render_toc_function, pages: int = ...) -> None: ...
    def set_section_title_styles(
        self,
        level0: TitleStyle,
        level1: TitleStyle | None = ...,
        level2: TitleStyle | None = ...,
        level3: TitleStyle | None = ...,
        level4: TitleStyle | None = ...,
        level5: TitleStyle | None = ...,
        level6: TitleStyle | None = ...,
    ) -> None: ...
    def start_section(self, name: str, level: int = 0, strict: bool = True) -> None: ...
