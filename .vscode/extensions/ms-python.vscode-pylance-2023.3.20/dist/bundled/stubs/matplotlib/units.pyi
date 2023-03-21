from typing import Iterable, Sequence
from ._typing import *
from .ticker import Formatter, Locator
from .axis import Axis
from datetime import date

class ConversionError(TypeError): ...

class AxisInfo:
    def __init__(
        self,
        majloc: Locator = ...,
        minloc: Locator = ...,
        majfmt: Formatter = ...,
        minfmt: Formatter = ...,
        label: str | None = ...,
        default_limits: Sequence[date] = ...,
    ) -> None: ...

class ConversionInterface:
    @staticmethod
    def axisinfo(unit, axis: Axis) -> AxisInfo: ...
    @staticmethod
    def default_units(x, axis: Axis): ...
    @staticmethod
    def convert(obj, unit, axis: Axis): ...
    @staticmethod
    def is_numlike(x: str) -> bool: ...

class DecimalConverter(ConversionInterface):
    @staticmethod
    def convert(value: Decimal | Iterable, unit, axis: Axis): ...

class Registry(dict):
    def get_converter(self, x) -> ConversionInterface | None: ...

registry: dict = ...
