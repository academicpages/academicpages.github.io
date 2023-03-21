"""Preconfigured converters for tomlkit."""
from base64 import b85decode, b85encode
from datetime import datetime
from enum import Enum
from operator import attrgetter
from typing import Any, Type, TypeVar

from tomlkit import dumps, loads

from cattrs._compat import AbstractSet, is_mapping

from ..converters import BaseConverter, Converter
from . import validate_datetime

T = TypeVar("T")
_enum_value_getter = attrgetter("_value_")


class TomlkitConverter(Converter):
    def dumps(self, obj: Any, unstructure_as=None, **kwargs) -> str:
        return dumps(self.unstructure(obj, unstructure_as=unstructure_as), **kwargs)

    def loads(self, data: str, cl: Type[T]) -> T:
        return self.structure(loads(data), cl)


def configure_converter(converter: BaseConverter):
    """
    Configure the converter for use with the tomlkit library.

    * bytes are serialized as base85 strings
    * sets are serialized as lists
    * tuples are serializas as lists
    * mapping keys are coerced into strings when unstructuring
    """
    converter.register_structure_hook(bytes, lambda v, _: b85decode(v))
    converter.register_unstructure_hook(
        bytes, lambda v: (b85encode(v) if v else b"").decode("utf8")
    )

    def gen_unstructure_mapping(cl: Any, unstructure_to=None):
        key_handler = str
        args = getattr(cl, "__args__", None)
        if args:
            # Currently, tomlkit has inconsistent behavior on 3.11
            # so we paper over it here.
            # https://github.com/sdispater/tomlkit/issues/237
            if issubclass(args[0], str):
                if issubclass(args[0], Enum):
                    key_handler = _enum_value_getter
                else:
                    key_handler = None
            elif issubclass(args[0], bytes):

                def key_handler(k: bytes):
                    return b85encode(k).decode("utf8")

        return converter.gen_unstructure_mapping(
            cl, unstructure_to=unstructure_to, key_handler=key_handler
        )

    converter._unstructure_func.register_func_list(
        [(is_mapping, gen_unstructure_mapping, True)]
    )
    converter.register_structure_hook(datetime, validate_datetime)


def make_converter(*args, **kwargs) -> TomlkitConverter:
    kwargs["unstruct_collection_overrides"] = {
        **kwargs.get("unstruct_collection_overrides", {}),
        AbstractSet: list,
        tuple: list,
    }
    res = TomlkitConverter(*args, **kwargs)
    configure_converter(res)

    return res
