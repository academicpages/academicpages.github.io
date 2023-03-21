from enum import Enum
from typing import Any, Callable, Iterable, Optional

import numpy as np

from ..core import Env
from ..spaces.space import Space
from .vector_env import VectorEnv

__all__ = ["AsyncVectorEnv"]

class AsyncState(Enum):
    DEFAULT = "default"
    WAITING_RESET = "reset"
    WAITING_STEP = "step"

class AsyncVectorEnv(VectorEnv):
    def __init__(
        self,
        env_fns: Iterable[Callable[[], Env]],
        observation_space: Optional[Space] = ...,
        action_space: Optional[Space] = ...,
        shared_memory: bool = ...,
        copy: bool = ...,
        context: Optional[str] = ...,
        daemon: bool = ...,
        worker: Optional[Any] = ...,
    ) -> None: ...
