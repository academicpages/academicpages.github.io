"""Module containing the InitializationOptions parser.

Provides a fully defaulted pydantic model for this language server's
initialization options.
"""

from typing import List, Optional, Pattern, Set

from lsprotocol.types import MarkupKind
from pydantic import BaseModel, Field

# pylint: disable=missing-class-docstring
# pylint: disable=too-few-public-methods


def snake_to_camel(string: str) -> str:
    """Convert from snake_case to camelCase."""
    return "".join(
        word.capitalize() if idx > 0 else word
        for idx, word in enumerate(string.split("_"))
    )


class Model(BaseModel):
    class Config:
        alias_generator = snake_to_camel


class CodeAction(Model):
    name_extract_variable: str = "jls_extract_var"
    name_extract_function: str = "jls_extract_def"


class Completion(Model):
    disable_snippets: bool = False
    resolve_eagerly: bool = False
    ignore_patterns: List[Pattern] = []


class Diagnostics(Model):
    enable: bool = True
    did_open: bool = True
    did_save: bool = True
    did_change: bool = True


class HoverDisableOptions(Model):
    all: bool = False
    names: Set[str] = set()
    full_names: Set[str] = set()


class HoverDisable(Model):
    """All Attributes have _ appended to avoid syntax conflicts.

    For example, the keyword class would have required a special case.
    To get around this, I decided it's simpler to always assume an
    underscore at the end.
    """

    keyword_: HoverDisableOptions = Field(
        default=HoverDisableOptions(), alias="keyword"
    )
    module_: HoverDisableOptions = Field(
        default=HoverDisableOptions(), alias="module"
    )
    class_: HoverDisableOptions = Field(
        default=HoverDisableOptions(), alias="class"
    )
    instance_: HoverDisableOptions = Field(
        default=HoverDisableOptions(), alias="instance"
    )
    function_: HoverDisableOptions = Field(
        default=HoverDisableOptions(), alias="function"
    )
    param_: HoverDisableOptions = Field(
        default=HoverDisableOptions(), alias="param"
    )
    path_: HoverDisableOptions = Field(
        default=HoverDisableOptions(), alias="path"
    )
    property_: HoverDisableOptions = Field(
        default=HoverDisableOptions(), alias="property"
    )
    statement_: HoverDisableOptions = Field(
        default=HoverDisableOptions(), alias="statement"
    )


class Hover(Model):
    enable: bool = True
    disable: HoverDisable = HoverDisable()


class JediSettings(Model):
    auto_import_modules: List[str] = []
    case_insensitive_completion: bool = True
    debug: bool = False


class Symbols(Model):
    ignore_folders: List[str] = [".nox", ".tox", ".venv", "__pycache__"]
    max_symbols: int = 20


class Workspace(Model):
    environment_path: Optional[str] = None
    extra_paths: List[str] = []
    symbols: Symbols = Symbols()


class InitializationOptions(Model):
    code_action: CodeAction = CodeAction()
    completion: Completion = Completion()
    diagnostics: Diagnostics = Diagnostics()
    hover: Hover = Hover()
    jedi_settings: JediSettings = JediSettings()
    markup_kind_preferred: Optional[MarkupKind]
    workspace: Workspace = Workspace()
