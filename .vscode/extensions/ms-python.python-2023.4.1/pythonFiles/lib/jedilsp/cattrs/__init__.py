from .converters import BaseConverter, Converter, GenConverter, UnstructureStrategy
from .errors import (
    BaseValidationError,
    ClassValidationError,
    ForbiddenExtraKeysError,
    IterableValidationError,
    StructureHandlerNotFoundError,
)
from .gen import override

__all__ = (
    "BaseConverter",
    "BaseValidationError",
    "ClassValidationError",
    "Converter",
    "converters",
    "disambiguators",
    "dispatch",
    "errors",
    "ForbiddenExtraKeysError",
    "gen",
    "GenConverter",
    "global_converter",
    "IterableValidationError",
    "override",
    "preconf",
    "register_structure_hook",
    "register_structure_hook_func",
    "register_unstructure_hook",
    "register_unstructure_hook_func",
    "structure",
    "structure_attrs_fromdict",
    "structure_attrs_fromtuple",
    "StructureHandlerNotFoundError",
    "unstructure",
    "UnstructureStrategy",
)


global_converter = Converter()

unstructure = global_converter.unstructure
structure = global_converter.structure
structure_attrs_fromtuple = global_converter.structure_attrs_fromtuple
structure_attrs_fromdict = global_converter.structure_attrs_fromdict
register_structure_hook = global_converter.register_structure_hook
register_structure_hook_func = global_converter.register_structure_hook_func
register_unstructure_hook = global_converter.register_unstructure_hook
register_unstructure_hook_func = global_converter.register_unstructure_hook_func
