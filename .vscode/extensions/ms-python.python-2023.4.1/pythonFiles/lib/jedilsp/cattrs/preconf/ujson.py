"""Preconfigured converters for ujson."""
from base64 import b85decode, b85encode
from datetime import datetime
from typing import Any, AnyStr, Type, TypeVar

from ujson import dumps, loads

from cattrs._compat import AbstractSet

from ..converters import BaseConverter, Converter

T = TypeVar("T")


class UjsonConverter(Converter):
    def dumps(self, obj: Any, unstructure_as=None, **kwargs) -> str:
        return dumps(self.unstructure(obj, unstructure_as=unstructure_as), **kwargs)

    def loads(self, data: AnyStr, cl: Type[T], **kwargs) -> T:
        return self.structure(loads(data, **kwargs), cl)


def configure_converter(converter: BaseConverter):
    """
    Configure the converter for use with the ujson library.

    * bytes are serialized as base64 strings
    * datetimes are serialized as ISO 8601
    * sets are serialized as lists
    """
    converter.register_unstructure_hook(
        bytes, lambda v: (b85encode(v) if v else b"").decode("utf8")
    )
    converter.register_structure_hook(bytes, lambda v, _: b85decode(v))

    converter.register_unstructure_hook(datetime, lambda v: v.isoformat())
    converter.register_structure_hook(datetime, lambda v, _: datetime.fromisoformat(v))


def make_converter(*args, **kwargs) -> UjsonConverter:
    kwargs["unstruct_collection_overrides"] = {
        **kwargs.get("unstruct_collection_overrides", {}),
        AbstractSet: list,
    }
    res = UjsonConverter(*args, **kwargs)
    configure_converter(res)

    return res
