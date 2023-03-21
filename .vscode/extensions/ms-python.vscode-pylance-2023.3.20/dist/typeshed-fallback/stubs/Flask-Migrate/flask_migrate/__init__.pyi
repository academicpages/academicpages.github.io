from collections.abc import Callable, Iterable, Sequence
from logging import Logger
from typing import Any, TypeVar
from typing_extensions import ParamSpec, TypeAlias

import flask
from flask_sqlalchemy import SQLAlchemy

_T = TypeVar("_T")
_P = ParamSpec("_P")
_ConfigureCallback: TypeAlias = Callable[[Config], Config]

alembic_version: tuple[int, int, int]
log: Logger

class Config:  # should inherit from alembic.config.Config which is not possible yet
    template_directory: str | None
    def __init__(self, *args, **kwargs) -> None: ...
    def get_template_directory(self) -> str: ...

class Migrate:
    configure_callbacks: list[_ConfigureCallback]
    db: SQLAlchemy | None
    directory: str
    alembic_ctx_kwargs: dict[str, Any]
    def __init__(
        self,
        app: flask.Flask | None = ...,
        db: SQLAlchemy | None = ...,
        directory: str = ...,
        command: str = ...,
        compare_type: bool = ...,
        render_as_batch: bool = ...,
        **kwargs,
    ) -> None: ...
    def init_app(
        self,
        app: flask.Flask,
        db: SQLAlchemy | None = ...,
        directory: str | None = ...,
        command: str | None = ...,
        compare_type: bool | None = ...,
        render_as_batch: bool | None = ...,
        **kwargs,
    ) -> None: ...
    def configure(self, f: _ConfigureCallback) -> _ConfigureCallback: ...
    def call_configure_callbacks(self, config: Config): ...
    def get_config(
        self, directory: str | None = ..., x_arg: str | Sequence[str] | None = ..., opts: Iterable[str] | None = ...
    ): ...

def catch_errors(f: Callable[_P, _T]) -> Callable[_P, _T]: ...
def list_templates() -> None: ...
def init(directory: str | None = ..., multidb: bool = ..., template: str | None = ..., package: bool = ...) -> None: ...
def revision(
    directory: str | None = ...,
    message: str | None = ...,
    autogenerate: bool = ...,
    sql: bool = ...,
    head: str = ...,
    splice: bool = ...,
    branch_label: str | None = ...,
    version_path: str | None = ...,
    rev_id: str | None = ...,
) -> None: ...
def migrate(
    directory: str | None = ...,
    message: str | None = ...,
    sql: bool = ...,
    head: str = ...,
    splice: bool = ...,
    branch_label: str | None = ...,
    version_path: str | None = ...,
    rev_id: str | None = ...,
    x_arg: str | Sequence[str] | None = ...,
) -> None: ...
def edit(directory: str | None = ..., revision: str = ...) -> None: ...
def merge(
    directory: str | None = ...,
    revisions: str = ...,
    message: str | None = ...,
    branch_label: str | None = ...,
    rev_id: str | None = ...,
) -> None: ...
def upgrade(
    directory: str | None = ...,
    revision: str = ...,
    sql: bool = ...,
    tag: str | None = ...,
    x_arg: str | Sequence[str] | None = ...,
) -> None: ...
def downgrade(
    directory: str | None = ...,
    revision: str = ...,
    sql: bool = ...,
    tag: str | None = ...,
    x_arg: str | Sequence[str] | None = ...,
) -> None: ...
def show(directory: str | None = ..., revision: str = ...) -> None: ...
def history(
    directory: str | None = ..., rev_range: str | None = ..., verbose: bool = ..., indicate_current: bool = ...
) -> None: ...
def heads(directory: str | None = ..., verbose: bool = ..., resolve_dependencies: bool = ...) -> None: ...
def branches(directory: str | None = ..., verbose: bool = ...) -> None: ...
def current(directory: str | None = ..., verbose: bool = ...) -> None: ...
def stamp(directory: str | None = ..., revision: str = ..., sql: bool = ..., tag: str | None = ...) -> None: ...
