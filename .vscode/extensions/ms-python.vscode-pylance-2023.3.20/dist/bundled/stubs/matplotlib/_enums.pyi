from enum import Enum

class _AutoStringNameEnum(Enum):
    def __hash__(self) -> int: ...

class JoinStyle(str, _AutoStringNameEnum):

    miter: JoinStyle 
    round: JoinStyle 
    bevel: JoinStyle 
    @staticmethod
    def demo() -> None: ...

class CapStyle(str, _AutoStringNameEnum):
    butt: CapStyle
    projecting: CapStyle
    round: CapStyle
    @staticmethod
    def demo() -> None: ...
