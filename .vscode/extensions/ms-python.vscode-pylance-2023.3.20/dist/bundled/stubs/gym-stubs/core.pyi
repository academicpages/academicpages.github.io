from typing import Any, Dict, List, Literal, Mapping, Tuple, TypeVar, overload

import numpy as np

from .envs.registration import EnvSpec
from .spaces import Space

_ActionType = Any
_OperationType = Any

_Action = TypeVar("_Action")
_Operation = TypeVar("_Operation")

class Env(object):
    metadata: Dict[str, List[str]]
    reward_range: Tuple[float, float]
    spec: EnvSpec

    action_space: Space
    observation_space: Space

    unwrapped: Env
    def step(
        self, action: _ActionType
    ) -> Tuple[_OperationType, float, bool, Dict[str, Any]]: ...
    def reset(self) -> Any: ...
    @overload
    def render(self, mode: Literal["human"]) -> None: ...
    @overload
    def render(self, mode: Literal["rgb_array"]) -> np.ndarray: ...
    @overload
    def render(self, mode: Literal["ansi"]) -> Any: ...
    @overload
    def render(self, mode: str = ...) -> Any: ...
    def close(self) -> None: ...
    def seed(self, seed: int = ...) -> List[int]: ...

class GoalEnv(Env):
    def compute_reward(
        self, achieved_goal: object, desired_goal: object, info: Mapping[str, Any]
    ) -> float: ...

class Wrapper(Env):
    def __init__(self, env: Env) -> None: ...
    def compute_reward(
        self, achieved_goal: object, desired_goal: object, info: Mapping[str, Any]
    ) -> float: ...
    @classmethod
    def class_name(cls) -> str: ...

class ObservationWrapper(Wrapper):
    def observation(self, observation: _Operation) -> _Operation: ...

class RewardWrapper(Wrapper):
    def reward(self, reward: float) -> float: ...

class ActionWrapper(Wrapper):
    def action(self, action: _Action) -> _Action: ...
    def reverse_action(self, action: _Action) -> _Action: ...
