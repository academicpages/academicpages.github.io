"""Preconfigured converters for pyyaml."""
from datetime import datetime
from typing import Any, Type, TypeVar

from yaml import safe_dump, safe_load

from cattrs._compat import FrozenSetSubscriptable

from ..converters import BaseConverter, Converter
from . import validate_datetime

T = TypeVar("T")


class PyyamlConverter(Converter):
    def dumps(self, obj: Any, unstructure_as=None, **kwargs) -> str:
        return safe_dump(self.unstructure(obj, unstructure_as=unstructure_as), **kwargs)

    def loads(self, data: str, cl: Type[T]) -> T:
        return self.structure(safe_load(data), cl)


def configure_converter(converter: BaseConverter):
    """
    Configure the converter for use with the pyyaml library.

    * frozensets are serialized as lists
    * string enums are converted into strings explicitly
    """
    converter.register_unstructure_hook(
        str, lambda v: v if v.__class__ is str else v.value
    )
    converter.register_structure_hook(datetime, validate_datetime)


def make_converter(*args, **kwargs) -> PyyamlConverter:
    kwargs["unstruct_collection_overrides"] = {
        **kwargs.get("unstruct_collection_overrides", {}),
        FrozenSetSubscriptable: list,
    }
    res = PyyamlConverter(*args, **kwargs)
    configure_converter(res)

    return res
