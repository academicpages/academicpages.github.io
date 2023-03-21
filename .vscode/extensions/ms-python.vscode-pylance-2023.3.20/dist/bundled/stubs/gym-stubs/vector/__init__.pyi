from typing import Any, Callable, Iterable, Optional, Union

from .async_vector_env import AsyncVectorEnv
from .sync_vector_env import SyncVectorEnv
from .vector_env import VectorEnv, VectorEnvWrapper

__all__ = ["AsyncVectorEnv", "SyncVectorEnv", "VectorEnv", "VectorEnvWrapper", "make"]

def make(
    id: str,
    num_envs: int = ...,
    asynchronous: bool = ...,
    wrappers: Optional[Union[Callable[...,Any], Iterable[Callable[...,Any]]]] = ...,
    **kwargs: Any
) -> VectorEnv: ...
