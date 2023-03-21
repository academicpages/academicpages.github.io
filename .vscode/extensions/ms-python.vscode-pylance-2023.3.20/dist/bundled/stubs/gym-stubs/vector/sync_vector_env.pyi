from typing import Callable, Iterable, Optional

import numpy as np

from ..core import Env
from ..spaces.space import Space
from .vector_env import VectorEnv

__all__ = ["SyncVectorEnv"]

class SyncVectorEnv(VectorEnv):
    def __init__(
        self,
        env_fns: Iterable[Callable[[], Env]],
        observation_space: Optional[Space] = ...,
        action_space: Optional[Space] = ...,
        copy: bool = ...,
    ) -> None: ...
