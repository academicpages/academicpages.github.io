from _typeshed import Incomplete
from typing import Any

from ...client import Pipeline as ClientPipeline
from .commands import JSONCommands

class JSON(JSONCommands):
    MODULE_CALLBACKS: dict[str, Any]
    client: Any
    execute_command: Any
    MODULE_VERSION: Incomplete | None
    def __init__(self, client, version: Incomplete | None = ..., decoder=..., encoder=...) -> None: ...
    def pipeline(self, transaction: bool = ..., shard_hint: Incomplete | None = ...) -> Pipeline: ...

class Pipeline(JSONCommands, ClientPipeline[Incomplete]): ...  # type: ignore[misc]
