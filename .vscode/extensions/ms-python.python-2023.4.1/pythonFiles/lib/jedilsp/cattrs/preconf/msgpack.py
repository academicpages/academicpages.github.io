"""Preconfigured converters for msgpack."""
from datetime import datetime, timezone
from typing import Any, Type, TypeVar

from msgpack import dumps, loads

from cattrs._compat import AbstractSet

from ..converters import BaseConverter, Converter

T = TypeVar("T")


class MsgpackConverter(Converter):
    def dumps(self, obj: Any, unstructure_as=None, **kwargs) -> bytes:
        return dumps(self.unstructure(obj, unstructure_as=unstructure_as), **kwargs)

    def loads(self, data: bytes, cl: Type[T], **kwargs) -> T:
        return self.structure(loads(data, **kwargs), cl)


def configure_converter(converter: BaseConverter):
    """
    Configure the converter for use with the msgpack library.

    * datetimes are serialized as timestamp floats
    * sets are serialized as lists
    """
    converter.register_unstructure_hook(datetime, lambda v: v.timestamp())
    converter.register_structure_hook(
        datetime, lambda v, _: datetime.fromtimestamp(v, timezone.utc)
    )


def make_converter(*args, **kwargs) -> MsgpackConverter:
    kwargs["unstruct_collection_overrides"] = {
        **kwargs.get("unstruct_collection_overrides", {}),
        AbstractSet: list,
    }
    res = MsgpackConverter(*args, **kwargs)
    configure_converter(res)

    return res
