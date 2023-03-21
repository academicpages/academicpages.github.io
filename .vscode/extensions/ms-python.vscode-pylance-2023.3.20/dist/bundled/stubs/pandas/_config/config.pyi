from collections.abc import (
    Callable,
    Iterable,
)
from contextlib import ContextDecorator
from typing import (
    Any,
    Literal,
    overload,
)

def get_option(pat: str) -> Any: ...
def set_option(pat: str, val: object) -> None: ...
def reset_option(pat: str) -> None: ...
@overload
def describe_option(pat: str, _print_desc: Literal[False]) -> str: ...
@overload
def describe_option(pat: str, _print_desc: Literal[True] = ...) -> None: ...

class DictWrapper:
    def __init__(self, d: dict[str, Any], prefix: str = ...) -> None: ...
    def __setattr__(
        self, key: str, val: str | bool | int | DictWrapper | None
    ) -> None: ...
    def __getattr__(self, key: str) -> str | bool | int | DictWrapper | None: ...
    def __dir__(self) -> Iterable[str]: ...

class Compute(DictWrapper):
    use_bottleneck: bool
    use_numba: bool
    use_numexpr: bool

class DisplayHTML(DictWrapper):
    border: int
    table_schema: bool
    use_mathjax: bool

class DisplayLaTeX(DictWrapper):
    escape: bool
    longtable: bool
    multicolumn: bool
    multicolumn_format: str
    multirow: bool
    repr: bool

class DisplayUnicode(DictWrapper):
    ambiguous_as_wide: bool
    east_asian_width: bool

class Display(DictWrapper):
    chop_threshold: int | None
    colheader_justify: str
    date_dayfirst: bool
    date_yearfirst: bool
    encoding: str
    expand_frame_repr: bool
    float_format: Callable[[float], str] | None
    html: DisplayHTML
    large_repr: str
    latex: DisplayLaTeX
    max_categories: int
    max_columns: int
    max_colwidth: int
    max_dir_items: int
    max_info_columns: int
    max_info_rows: int
    max_rows: int
    max_seq_items: int
    memory_usage: bool
    min_rows: int
    multi_sparse: bool
    notebook_repr_html: bool
    pprint_nest_depth: int
    precision: int
    show_dimensions: str
    unicode: DisplayUnicode
    width: int

class IOExcelODS(DictWrapper):
    reader: str
    writer: str

class IOExcelXLS(DictWrapper):
    writer: str

class IOExcelXLSB(DictWrapper):
    reader: str

class IOExcelXLSM(DictWrapper):
    reader: str
    writer: str

class IOExcelXLSX(DictWrapper):
    reader: str
    writer: str

class IOExcel(DictWrapper):
    ods: IOExcelODS
    xls: DictWrapper
    xlsb: DictWrapper
    xlsm: DictWrapper
    xlsx: DictWrapper

class IOHDF(DictWrapper):
    default_format: Literal["table", "fixed"] | None
    dropna_table: bool

class IOParquet(DictWrapper):
    engine: str

class IOSQL(DictWrapper):
    engine: str

class IO(DictWrapper):
    excel: IOExcel
    hdf: IOHDF
    parquet: IOParquet
    sql: IOSQL

class Mode(DictWrapper):
    chained_assignment: str
    data_manager: str
    sim_interactive: bool
    string_storage: str
    use_inf_as_na: bool

class PlottingMatplotlib(DictWrapper):
    register_converters: str

class Plotting(DictWrapper):
    backend: str
    matplotlib: PlottingMatplotlib

class StylerFormat:
    decimal: str
    escape: str | None
    formatter: str | None
    na_rep: str | None
    precision: int
    thousands: str | None

class StylerHTML:
    mathjax: bool

class StylerLatex:
    environment: str | None
    hrules: bool
    multicol_align: str
    multirow_align: str

class StylerRender:
    encoding: str
    max_columns: int | None
    max_elements: int
    max_rows: int | None
    repr: str

class StylerSparse:
    columns: bool
    index: bool

class Styler(DictWrapper):
    format: StylerFormat
    html: StylerHTML
    latex: StylerLatex
    render: StylerRender
    sparse: StylerSparse

class Options(DictWrapper):
    compute: Compute
    display: Display
    io: IO
    mode: Mode
    plotting: Plotting
    styler: Styler

options: Options

class option_context(ContextDecorator):
    def __init__(self, /, pat: str, val: Any, *args: Any) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, *args: object) -> None: ...

class OptionError(AttributeError, KeyError): ...
