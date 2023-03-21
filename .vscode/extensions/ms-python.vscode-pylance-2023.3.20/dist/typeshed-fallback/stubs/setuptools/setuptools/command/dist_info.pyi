from typing import Any

from .._distutils.cmd import Command

class dist_info(Command):
    description: str
    user_options: Any
    egg_base: Any
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    def run(self) -> None: ...
