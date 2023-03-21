import linecache
import re
import uuid
from dataclasses import is_dataclass
from threading import local
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Dict,
    Iterable,
    Mapping,
    Optional,
    Tuple,
    Type,
    TypeVar,
)

import attr
from attr import NOTHING, frozen, resolve_types

from cattrs.errors import (
    ClassValidationError,
    ForbiddenExtraKeysError,
    IterableValidationError,
    StructureHandlerNotFoundError,
)

from ._compat import (
    adapted_fields,
    get_args,
    get_origin,
    is_annotated,
    is_bare,
    is_generic,
)
from ._generics import deep_copy_with

if TYPE_CHECKING:  # pragma: no cover
    from cattr.converters import BaseConverter


@frozen
class AttributeOverride:
    omit_if_default: Optional[bool] = None
    rename: Optional[str] = None
    omit: bool = False  # Omit the field completely.


def override(
    omit_if_default: Optional[bool] = None,
    rename: Optional[str] = None,
    omit: bool = False,
):
    return AttributeOverride(omit_if_default=omit_if_default, rename=rename, omit=omit)


_neutral = AttributeOverride()
_already_generating = local()
T = TypeVar("T")


def make_dict_unstructure_fn(
    cl: Type[T],
    converter: "BaseConverter",
    _cattrs_omit_if_default: bool = False,
    _cattrs_use_linecache: bool = True,
    **kwargs: AttributeOverride,
) -> Callable[[T], Dict[str, Any]]:
    """
    Generate a specialized dict unstructuring function for an attrs class or a
    dataclass.
    """
    origin = get_origin(cl)
    attrs = adapted_fields(origin or cl)  # type: ignore

    if any(isinstance(a.type, str) for a in attrs):
        # PEP 563 annotations - need to be resolved.
        resolve_types(cl)

    mapping = {}
    if is_generic(cl):
        mapping = _generate_mapping(cl, mapping)

        for base in getattr(origin, "__orig_bases__", ()):
            if is_generic(base) and not str(base).startswith("typing.Generic"):
                mapping = _generate_mapping(base, mapping)
                break
        cl = origin

    cl_name = cl.__name__
    fn_name = "unstructure_" + cl_name
    globs = {}
    lines = []
    invocation_lines = []
    internal_arg_parts = {}

    # We keep track of what we're generating to help with recursive
    # class graphs.
    try:
        working_set = _already_generating.working_set
    except AttributeError:
        working_set = set()
        _already_generating.working_set = working_set
    if cl in working_set:
        raise RecursionError()
    else:
        working_set.add(cl)

    try:
        for a in attrs:
            attr_name = a.name
            override = kwargs.pop(attr_name, _neutral)
            if override.omit:
                continue
            kn = attr_name if override.rename is None else override.rename
            d = a.default

            # For each attribute, we try resolving the type here and now.
            # If a type is manually overwritten, this function should be
            # regenerated.
            handler = None
            if a.type is not None:
                t = a.type
                if isinstance(t, TypeVar):
                    if t.__name__ in mapping:
                        t = mapping[t.__name__]
                    else:
                        handler = converter.unstructure
                elif is_generic(t) and not is_bare(t) and not is_annotated(t):
                    t = deep_copy_with(t, mapping)

                if handler is None:
                    try:
                        handler = converter._unstructure_func.dispatch(t)
                    except RecursionError:
                        # There's a circular reference somewhere down the line
                        handler = converter.unstructure
            else:
                handler = converter.unstructure

            is_identity = handler == converter._unstructure_identity

            if not is_identity:
                unstruct_handler_name = f"__c_unstr_{attr_name}"
                globs[unstruct_handler_name] = handler
                internal_arg_parts[unstruct_handler_name] = handler
                invoke = f"{unstruct_handler_name}(instance.{attr_name})"
            else:
                invoke = f"instance.{attr_name}"

            if d is not attr.NOTHING and (
                (_cattrs_omit_if_default and override.omit_if_default is not False)
                or override.omit_if_default
            ):
                def_name = f"__c_def_{attr_name}"

                if isinstance(d, attr.Factory):
                    globs[def_name] = d.factory
                    internal_arg_parts[def_name] = d.factory
                    if d.takes_self:
                        lines.append(
                            f"  if instance.{attr_name} != {def_name}(instance):"
                        )
                    else:
                        lines.append(f"  if instance.{attr_name} != {def_name}():")
                    lines.append(f"    res['{kn}'] = {invoke}")
                else:
                    globs[def_name] = d
                    internal_arg_parts[def_name] = d
                    lines.append(f"  if instance.{attr_name} != {def_name}:")
                    lines.append(f"    res['{kn}'] = {invoke}")

            else:
                # No default or no override.
                invocation_lines.append(f"'{kn}': {invoke},")

        internal_arg_line = ", ".join([f"{i}={i}" for i in internal_arg_parts])
        if internal_arg_line:
            internal_arg_line = f", {internal_arg_line}"
        for k, v in internal_arg_parts.items():
            globs[k] = v

        total_lines = (
            [f"def {fn_name}(instance{internal_arg_line}):"]
            + ["  res = {"]
            + [f"    {line}" for line in invocation_lines]
            + ["  }"]
            + lines
            + ["  return res"]
        )
        script = "\n".join(total_lines)

        fname = _generate_unique_filename(
            cl, "unstructure", reserve=_cattrs_use_linecache
        )

        eval(compile(script, fname, "exec"), globs)

        fn = globs[fn_name]
        if _cattrs_use_linecache:
            linecache.cache[fname] = len(script), None, total_lines, fname
    finally:
        working_set.remove(cl)

    return fn


def _generate_mapping(cl: Type, old_mapping: Dict[str, type]) -> Dict[str, type]:
    mapping = {}

    # To handle the cases where classes in the typing module are using
    # the GenericAlias structure but aren’t a Generic and hence
    # end up in this function but do not have an `__parameters__`
    # attribute. These classes are interface types, for example
    # `typing.Hashable`.
    parameters = getattr(get_origin(cl), "__parameters__", None)
    if parameters is None:
        return old_mapping

    for p, t in zip(parameters, get_args(cl)):
        if isinstance(t, TypeVar):
            continue
        mapping[p.__name__] = t

    if not mapping:
        return old_mapping

    return mapping


DictStructureFn = Callable[[Mapping[str, Any], Any], T]


def make_dict_structure_fn(
    cl: Type[T],
    converter: "BaseConverter",
    _cattrs_forbid_extra_keys: bool = False,
    _cattrs_use_linecache: bool = True,
    _cattrs_prefer_attrib_converters: bool = False,
    _cattrs_detailed_validation: bool = True,
    **kwargs: AttributeOverride,
) -> DictStructureFn[T]:
    """Generate a specialized dict structuring function for an attrs class."""

    mapping = {}
    if is_generic(cl):
        base = get_origin(cl)
        mapping = _generate_mapping(cl, mapping)
        cl = base

    for base in getattr(cl, "__orig_bases__", ()):
        if is_generic(base) and not str(base).startswith("typing.Generic"):
            mapping = _generate_mapping(base, mapping)
            break

    if isinstance(cl, TypeVar):
        cl = mapping.get(cl.__name__, cl)

    cl_name = cl.__name__
    fn_name = "structure_" + cl_name

    # We have generic parameters and need to generate a unique name for the function
    for p in getattr(cl, "__parameters__", ()):
        # This is nasty, I am not sure how best to handle `typing.List[str]` or `TClass[int, int]` as a parameter type here
        try:
            name_base = mapping[p.__name__]
        except KeyError:
            raise StructureHandlerNotFoundError(
                f"Missing type for generic argument {p.__name__}, specify it when structuring.",
                p,
            ) from None
        name = getattr(name_base, "__name__", None) or str(name_base)
        name = re.sub(r"[\[\.\] ,]", "_", name)
        fn_name += f"_{name}"

    internal_arg_parts = {"__cl": cl}
    globs = {}
    lines = []
    post_lines = []
    invocation_lines = []

    attrs = adapted_fields(cl)
    is_dc = is_dataclass(cl)

    if any(isinstance(a.type, str) for a in attrs):
        # PEP 563 annotations - need to be resolved.
        resolve_types(cl)

    allowed_fields = set()
    if _cattrs_forbid_extra_keys:
        globs["__c_a"] = allowed_fields
        globs["__c_feke"] = ForbiddenExtraKeysError

    if _cattrs_detailed_validation:
        lines.append("  res = {}")
        lines.append("  errors = []")
        invocation_lines.append("**res,")
        internal_arg_parts["__c_cve"] = ClassValidationError
        for a in attrs:
            an = a.name
            override = kwargs.get(an, _neutral)
            if override.omit:
                continue
            t = a.type
            if isinstance(t, TypeVar):
                t = mapping.get(t.__name__, t)
            elif is_generic(t) and not is_bare(t) and not is_annotated(t):
                t = deep_copy_with(t, mapping)

            # For each attribute, we try resolving the type here and now.
            # If a type is manually overwritten, this function should be
            # regenerated.
            if a.converter is not None and _cattrs_prefer_attrib_converters:
                handler = None
            elif (
                a.converter is not None
                and not _cattrs_prefer_attrib_converters
                and t is not None
            ):
                handler = converter._structure_func.dispatch(t)
                if handler == converter._structure_error:
                    handler = None
            elif t is not None:
                handler = converter._structure_func.dispatch(t)
            else:
                handler = converter.structure

            struct_handler_name = f"__c_structure_{an}"
            internal_arg_parts[struct_handler_name] = handler

            ian = an if (is_dc or an[0] != "_") else an[1:]
            kn = an if override.rename is None else override.rename
            allowed_fields.add(kn)
            i = "  "
            if a.default is not NOTHING:
                lines.append(f"{i}if '{kn}' in o:")
                i = f"{i}  "
            lines.append(f"{i}try:")
            i = f"{i}  "
            if handler:
                if handler == converter._structure_call:
                    internal_arg_parts[struct_handler_name] = t
                    lines.append(f"{i}res['{ian}'] = {struct_handler_name}(o['{kn}'])")
                else:
                    type_name = f"__c_type_{an}"
                    internal_arg_parts[type_name] = t
                    lines.append(
                        f"{i}res['{ian}'] = {struct_handler_name}(o['{kn}'], {type_name})"
                    )
            else:
                lines.append(f"{i}res['{ian}'] = o['{kn}']")
            i = i[:-2]
            lines.append(f"{i}except Exception as e:")
            i = f"{i}  "
            lines.append(
                f"{i}e.__notes__ = getattr(e, '__notes__', []) + [\"Structuring class {cl.__qualname__} @ attribute {an}\"]"
            )
            lines.append(f"{i}errors.append(e)")

        if _cattrs_forbid_extra_keys:
            post_lines += [
                "  unknown_fields = set(o.keys()) - __c_a",
                "  if unknown_fields:",
                "    errors.append(__c_feke('', __cl, unknown_fields))",
            ]

        post_lines.append(
            f"  if errors: raise __c_cve('While structuring ' + {cl.__name__!r}, errors, __cl)"
        )
        instantiation_lines = (
            ["  try:"]
            + ["    return __cl("]
            + [f"      {line}" for line in invocation_lines]
            + ["    )"]
            + [
                f"  except Exception as exc: raise __c_cve('While structuring ' + {cl.__name__!r}, [exc], __cl)"
            ]
        )
    else:
        non_required = []
        # The first loop deals with required args.
        for a in attrs:
            an = a.name
            override = kwargs.get(an, _neutral)
            if override.omit:
                continue
            if a.default is not NOTHING:
                non_required.append(a)
                continue
            t = a.type
            if isinstance(t, TypeVar):
                t = mapping.get(t.__name__, t)
            elif is_generic(t) and not is_bare(t) and not is_annotated(t):
                t = deep_copy_with(t, mapping)

            # For each attribute, we try resolving the type here and now.
            # If a type is manually overwritten, this function should be
            # regenerated.
            if a.converter is not None and _cattrs_prefer_attrib_converters:
                handler = None
            elif (
                a.converter is not None
                and not _cattrs_prefer_attrib_converters
                and t is not None
            ):
                handler = converter._structure_func.dispatch(t)
                if handler == converter._structure_error:
                    handler = None
            elif t is not None:
                handler = converter._structure_func.dispatch(t)
            else:
                handler = converter.structure

            kn = an if override.rename is None else override.rename
            allowed_fields.add(kn)

            if handler:
                struct_handler_name = f"__c_structure_{an}"
                internal_arg_parts[struct_handler_name] = handler
                if handler == converter._structure_call:
                    internal_arg_parts[struct_handler_name] = t
                    invocation_line = f"{struct_handler_name}(o['{kn}']),"
                else:
                    type_name = f"__c_type_{an}"
                    internal_arg_parts[type_name] = t
                    invocation_line = f"{struct_handler_name}(o['{kn}'], {type_name}),"
            else:
                invocation_line = f"o['{kn}'],"

            if a.kw_only:
                ian = an if (is_dc or an[0] != "_") else an[1:]
                invocation_line = f"{ian}={invocation_line}"
            invocation_lines.append(invocation_line)

        # The second loop is for optional args.
        if non_required:
            invocation_lines.append("**res,")
            lines.append("  res = {}")

            for a in non_required:
                an = a.name
                override = kwargs.get(an, _neutral)
                t = a.type
                if isinstance(t, TypeVar):
                    t = mapping.get(t.__name__, t)
                elif is_generic(t) and not is_bare(t) and not is_annotated(t):
                    t = deep_copy_with(t, mapping)

                # For each attribute, we try resolving the type here and now.
                # If a type is manually overwritten, this function should be
                # regenerated.
                if a.converter is not None and _cattrs_prefer_attrib_converters:
                    handler = None
                elif (
                    a.converter is not None
                    and not _cattrs_prefer_attrib_converters
                    and t is not None
                ):
                    handler = converter._structure_func.dispatch(t)
                    if handler == converter._structure_error:
                        handler = None
                elif t is not None:
                    handler = converter._structure_func.dispatch(t)
                else:
                    handler = converter.structure

                struct_handler_name = f"__c_structure_{an}"
                internal_arg_parts[struct_handler_name] = handler

                ian = an if (is_dc or an[0] != "_") else an[1:]
                kn = an if override.rename is None else override.rename
                allowed_fields.add(kn)
                post_lines.append(f"  if '{kn}' in o:")
                if handler:
                    if handler == converter._structure_call:
                        internal_arg_parts[struct_handler_name] = t
                        post_lines.append(
                            f"    res['{ian}'] = {struct_handler_name}(o['{kn}'])"
                        )
                    else:
                        type_name = f"__c_type_{an}"
                        internal_arg_parts[type_name] = t
                        post_lines.append(
                            f"    res['{ian}'] = {struct_handler_name}(o['{kn}'], {type_name})"
                        )
                else:
                    post_lines.append(f"    res['{ian}'] = o['{kn}']")
        instantiation_lines = (
            ["  return __cl("] + [f"    {line}" for line in invocation_lines] + ["  )"]
        )

        if _cattrs_forbid_extra_keys:
            post_lines += [
                "  unknown_fields = set(o.keys()) - __c_a",
                "  if unknown_fields:",
                "    raise __c_feke('', __cl, unknown_fields)",
            ]

    # At the end, we create the function header.
    internal_arg_line = ", ".join([f"{i}={i}" for i in internal_arg_parts])
    for k, v in internal_arg_parts.items():
        globs[k] = v

    total_lines = (
        [f"def {fn_name}(o, _, *, {internal_arg_line}):"]
        + lines
        + post_lines
        + instantiation_lines
    )

    fname = _generate_unique_filename(cl, "structure", reserve=_cattrs_use_linecache)
    script = "\n".join(total_lines)
    eval(compile(script, fname, "exec"), globs)
    if _cattrs_use_linecache:
        linecache.cache[fname] = len(script), None, total_lines, fname

    return globs[fn_name]


IterableUnstructureFn = Callable[[Iterable[Any]], Any]


def make_iterable_unstructure_fn(
    cl: Any, converter: "BaseConverter", unstructure_to: Any = None
) -> IterableUnstructureFn:
    """Generate a specialized unstructure function for an iterable."""
    handler = converter.unstructure

    fn_name = "unstructure_iterable"

    # Let's try fishing out the type args
    # Unspecified tuples have `__args__` as empty tuples, so guard
    # against IndexError.
    if getattr(cl, "__args__", None) not in (None, ()):
        type_arg = cl.__args__[0]
        # We don't know how to handle the TypeVar on this level,
        # so we skip doing the dispatch here.
        if not isinstance(type_arg, TypeVar):
            handler = converter._unstructure_func.dispatch(type_arg)

    globs = {"__cattr_seq_cl": unstructure_to or cl, "__cattr_u": handler}
    lines = []

    lines.append(f"def {fn_name}(iterable):")
    lines.append("    res = __cattr_seq_cl(__cattr_u(i) for i in iterable)")

    total_lines = lines + ["    return res"]

    eval(compile("\n".join(total_lines), "", "exec"), globs)

    fn = globs[fn_name]

    return fn


HeteroTupleUnstructureFn = Callable[[Tuple[Any, ...]], Any]


def make_hetero_tuple_unstructure_fn(
    cl: Any, converter: "BaseConverter", unstructure_to: Any = None
) -> HeteroTupleUnstructureFn:
    """Generate a specialized unstructure function for a heterogenous tuple."""
    fn_name = "unstructure_tuple"

    type_args = get_args(cl)

    # We can do the dispatch here and now.
    handlers = [
        converter._unstructure_func.dispatch(type_arg) for type_arg in type_args
    ]

    globs = {f"__cattr_u_{i}": h for i, h in enumerate(handlers)}
    if unstructure_to is not tuple:
        globs["__cattr_seq_cl"] = unstructure_to or cl
    lines = []

    lines.append(f"def {fn_name}(tup):")
    if unstructure_to is not tuple:
        lines.append("    res = __cattr_seq_cl((")
    else:
        lines.append("    res = (")
    for i in range(len(handlers)):
        if handlers[i] == converter._unstructure_identity:
            lines.append(f"        tup[{i}],")
        else:
            lines.append(f"        __cattr_u_{i}(tup[{i}]),")

    if unstructure_to is not tuple:
        lines.append("    ))")
    else:
        lines.append("    )")

    total_lines = lines + ["    return res"]

    eval(compile("\n".join(total_lines), "", "exec"), globs)

    fn = globs[fn_name]

    return fn


MappingUnstructureFn = Callable[[Mapping[Any, Any]], Any]


def make_mapping_unstructure_fn(
    cl: Any,
    converter: "BaseConverter",
    unstructure_to: Any = None,
    key_handler: Optional[Callable[[Any, Optional[Any]], Any]] = None,
) -> MappingUnstructureFn:
    """Generate a specialized unstructure function for a mapping."""
    kh = key_handler or converter.unstructure
    val_handler = converter.unstructure

    fn_name = "unstructure_mapping"

    # Let's try fishing out the type args.
    if getattr(cl, "__args__", None) is not None:
        args = get_args(cl)
        if len(args) == 2:
            key_arg, val_arg = args
        else:
            # Probably a Counter
            key_arg, val_arg = args, Any
        # We can do the dispatch here and now.
        kh = key_handler or converter._unstructure_func.dispatch(key_arg)
        if kh == converter._unstructure_identity:
            kh = None

        val_handler = converter._unstructure_func.dispatch(val_arg)
        if val_handler == converter._unstructure_identity:
            val_handler = None

    globs = {
        "__cattr_mapping_cl": unstructure_to or cl,
        "__cattr_k_u": kh,
        "__cattr_v_u": val_handler,
    }

    k_u = "__cattr_k_u(k)" if kh is not None else "k"
    v_u = "__cattr_v_u(v)" if val_handler is not None else "v"

    lines = []

    lines.append(f"def {fn_name}(mapping):")
    lines.append(
        f"    res = __cattr_mapping_cl(({k_u}, {v_u}) for k, v in mapping.items())"
    )

    total_lines = lines + ["    return res"]

    eval(compile("\n".join(total_lines), "", "exec"), globs)

    fn = globs[fn_name]

    return fn


MappingStructureFn = Callable[[Mapping[Any, Any], Any], T]


def make_mapping_structure_fn(
    cl: Type[T],
    converter: "BaseConverter",
    structure_to: Type = dict,
    key_type=NOTHING,
    val_type=NOTHING,
    detailed_validation: bool = True,
) -> MappingStructureFn[T]:
    """Generate a specialized unstructure function for a mapping."""
    fn_name = "structure_mapping"

    globs: Dict[str, Type] = {"__cattr_mapping_cl": structure_to}

    lines = []
    lines.append(f"def {fn_name}(mapping, _):")

    # Let's try fishing out the type args.
    if not is_bare(cl):
        args = get_args(cl)
        if len(args) == 2:
            key_arg_cand, val_arg_cand = args
            if key_type is NOTHING:
                key_type = key_arg_cand
            if val_type is NOTHING:
                val_type = val_arg_cand
        else:
            if key_type is not NOTHING and val_type is NOTHING:
                (val_type,) = args
            elif key_type is NOTHING and val_type is not NOTHING:
                (key_type,) = args
            else:
                # Probably a Counter
                (key_type,) = args
                val_type = Any

        is_bare_dict = val_type is Any and key_type is Any
        if not is_bare_dict:
            # We can do the dispatch here and now.
            key_handler = converter._structure_func.dispatch(key_type)
            if key_handler == converter._structure_call:
                key_handler = key_type

            val_handler = converter._structure_func.dispatch(val_type)
            if val_handler == converter._structure_call:
                val_handler = val_type

            globs["__cattr_k_t"] = key_type
            globs["__cattr_v_t"] = val_type
            globs["__cattr_k_s"] = key_handler
            globs["__cattr_v_s"] = val_handler
            k_s = (
                "__cattr_k_s(k, __cattr_k_t)"
                if key_handler != key_type
                else "__cattr_k_s(k)"
            )
            v_s = (
                "__cattr_v_s(v, __cattr_v_t)"
                if val_handler != val_type
                else "__cattr_v_s(v)"
            )
    else:
        is_bare_dict = True

    if is_bare_dict:
        # No args, it's a bare dict.
        lines.append("  res = dict(mapping)")
    else:
        if detailed_validation:
            globs["enumerate"] = enumerate
            globs["IterableValidationError"] = IterableValidationError
            lines.append("  res = {}; errors = []")
            lines.append("  for ix, (k, v) in enumerate(mapping.items()):")
            lines.append("    try:")
            lines.append(f"      value = {v_s}")
            lines.append("    except Exception as e:")
            lines.append(
                "      e.__notes__ = getattr(e, '__notes__', []) + ['Structuring mapping value @ key ' + repr(k)]"
            )
            lines.append("      errors.append(e)")
            lines.append("      continue")
            lines.append("    try:")
            lines.append(f"      key = {k_s}")
            lines.append("      res[key] = value")
            lines.append("    except Exception as e:")
            lines.append(
                "      e.__notes__ = getattr(e, '__notes__', []) + ['Structuring mapping key @ key ' + repr(k)]"
            )
            lines.append("      errors.append(e)")
            lines.append("  if errors:")
            lines.append(
                f"    raise IterableValidationError('While structuring ' + {repr(cl)!r}, errors, __cattr_mapping_cl)"
            )
        else:
            lines.append(f"  res = {{{k_s}: {v_s} for k, v in mapping.items()}}")
    if structure_to is not dict:
        lines.append("  res = __cattr_mapping_cl(res)")

    total_lines = lines + ["  return res"]
    script = "\n".join(total_lines)

    eval(compile(script, "", "exec"), globs)

    fn = globs[fn_name]

    return fn


def _generate_unique_filename(cls: Any, func_name: str, reserve: bool = True) -> str:
    """
    Create a "filename" suitable for a function being generated.
    """
    unique_id = uuid.uuid4()
    extra = ""
    count = 1

    while True:
        unique_filename = "<cattrs generated {0} {1}.{2}{3}>".format(
            func_name, cls.__module__, getattr(cls, "__qualname__", cls.__name__), extra
        )
        if not reserve:
            return unique_filename
        # To handle concurrency we essentially "reserve" our spot in
        # the linecache with a dummy line.  The caller can then
        # set this value correctly.
        cache_line = (1, None, (str(unique_id),), unique_filename)
        if linecache.cache.setdefault(unique_filename, cache_line) == cache_line:
            return unique_filename

        # Looks like this spot is taken. Try again.
        count += 1
        extra = "-{0}".format(count)
