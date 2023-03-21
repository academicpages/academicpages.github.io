from typing import Optional

from ..core import Env, Wrapper

class TimeLimit(Wrapper):
    def __init__(self, env: Env, max_episode_steps: Optional[int] = ...) -> None: ...
