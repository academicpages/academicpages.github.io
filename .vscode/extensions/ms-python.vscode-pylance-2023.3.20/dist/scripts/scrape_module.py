# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

# WARNING: DO run scraper from 32-bit command line or else output may be UTF-16.
#
# Scraping most modules does not require search path. Example:
#     c:\python3\python -W ignore -B -E scrape_module.py lxml.etree > etree.pyi
#
# However, some compiled modules do need explicit search path. For example, cv2 is
# actually compiled 'cv2.cp36-win_amd64.pyd' under 'site-packages/cv2'. Thus the
# compiled module is actually cv2.cv2 (which cv2 imports via *). So for the scraped
# stub to work cv2.cv2 has to be scraped but stored in 'native-stubs' as cv2.
#
# Scraping then requires explicit search path to local cv2.cv2.
#     c:\python3\python -W ignore -B -E scrape_module.py cv2.cv2 C:\Python3\Lib\site-packages > cv2.pyi
#

import ast
import builtins
import importlib
import inspect
import io
import keyword
import sys
import tokenize
import warnings

if sys.version_info[0] < 3:
    raise Exception("Python 2 is unsupported")


class InspectWarning(UserWarning):
    pass


def get_module_version(module):
    try:
        version = getattr(module, "__version__")
        if isinstance(version, bytes):
            return version.decode()
        else:
            return version
    except AttributeError:
        return "unspecified"


def print_module_version(module, out):
    module_name = getattr(module, "__name__")
    module_version = get_module_version(module)

    library_name = module_name.split(".")[0]

    if library_name == module_name:
        package_name = getattr(module, "__package__", None)
        if package_name:
            library_name = package_name.split(".")[0]

    library = importlib.import_module(library_name)
    library_version = get_module_version(library)

    print(
        "# Python: "
        + sys.version
        + "\n# Library: "
        + library_name
        + ", version: "
        + library_version
        + "\n# Module: "
        + module_name
        + ", version: "
        + module_version,
        file=out
    )


def can_eval(s):
    """Returns True if the string can be evaluated."""
    if not s:
        return False
    try:
        ast.parse(s, mode="eval")
    except SyntaxError:
        return False
    else:
        return True


def is_callable(v):
    """Returns True if v has __call__."""
    try:
        return hasattr(v, "__call__")
    except Exception:
        return False


def safe_module_name(n):
    """Returns a module name which should not conflict with any other symbol."""
    if n:
        return "_mod_" + n.replace(".", "_")
    return n


def do_not_inspect(v):
    """Returns True if this value should not be inspected due to potential bugs."""
    # https://github.com/Microsoft/python-language-server/issues/740
    # https://github.com/cython/cython/issues/1470
    if type(v).__name__ != "fused_cython_function":
        return False

    # If a fused function has __defaults__, then attempting to access
    # __kwdefaults__ will fail if generated before cython 0.29.6.
    return bool(getattr(v, "__defaults__", False))


class SeenNames(object):
    """Tracks unique names."""

    def __init__(self, s=None):
        self.seen = set() if s is None else s.copy()

    def make_unique(self, name):
        if name not in self.seen:
            self.seen.add(name)
            return name

        n = name + "_"
        if n not in self.seen:
            self.seen.add(n)
            return n

        i = 0
        while True:
            i += 1
            n = name + "_" + str(i)
            if n not in self.seen:
                self.seen.add(n)
                return n

        raise RuntimeError("Unreachable")


class DefaultRepr(object):
    """
    A value whose repr is an exact string representation.

    For example, ``DefaultRepr("...")`` would be printed in
    an inspect.Parameter exactly as ``...``, whereas actually
    using ``...`` as a default value would print as ``Ellipsis``.
    """

    def __init__(self, v):
        self.v = v

    def __repr__(self):
        return self.v


ELLIPSIS_DEFAULT = DefaultRepr("...")

try:
    # Fragile; this member isn't officially documented.
    EXACT_TOKEN_TYPES = tokenize.EXACT_TOKEN_TYPES
except AttributeError:
    # Bare minimum that we need here
    EXACT_TOKEN_TYPES = {
        "(": tokenize.LPAR,
        ")": tokenize.RPAR,
        "[": tokenize.LSQB,
        "]": tokenize.RSQB,
        "{": tokenize.LBRACE,
        "}": tokenize.RBRACE,
        ",": tokenize.COMMA,
        ":": tokenize.COLON,
        "*": tokenize.STAR,
        "**": tokenize.DOUBLESTAR,
        "=": tokenize.EQUAL,
    }

PAREN_TOKEN_MAP = {
    tokenize.LPAR: tokenize.RPAR,
    tokenize.LBRACE: tokenize.RBRACE,
    tokenize.LSQB: tokenize.RSQB,
}


class DocstringSigParser(object):
    """Spooky docstring parsing logic."""

    def __init__(self, callable, expected_name, defaults=None):
        self.callable = callable
        self.name = expected_name
        self._defaults = defaults

    def restype(self):
        doc = getattr(self.callable, "__doc__", None)
        if not isinstance(doc, str):
            return None

        doc = doc.lstrip()

        first_line = doc.partition("\n")[0].strip()
        if not "->" in first_line:
            return None

        index = first_line.index("->")
        typeName = first_line[index + 2 :].strip()

        if typeName.startswith("str"):
            return "str"
        if typeName.startswith("float"):
            return "float"
        if typeName.startswith("int"):
            return "int"
        if typeName.startswith("long"):
            return "int"
        if typeName.startswith("list"):
            return "typing.List[typing.Any]"
        if typeName.startswith("dict"):
            return "typing.Dict[typing.Any, typing.Any]"
        if typeName.startswith("("):
            return "typing.Tuple[typing.Any, ...]"
        if typeName.startswith("bool"):
            return "bool"
        if "Return a string" in first_line:
            return "str"
        return None

    def argspec(self, doc=None, override_name=None):
        if not doc:
            doc = getattr(self.callable, "__doc__", None)
        if not isinstance(doc, str):
            return None

        doc = doc.lstrip()

        # TODO: Support overloads by reading multiple lines?
        doc = self._get_first_function_call(doc, override_name)
        if not doc:
            return None

        if override_name:
            allow_name_mismatch = override_name not in doc
        else:
            allow_name_mismatch = False

        return self._parse_funcdef(
            doc, allow_name_mismatch, self._defaults, override_name
        )

    def _tokenize(self, expr):
        if sys.version_info[0] == 3 and sys.version_info[1] <= 2:
            expr = "# coding: utf-8\n" + expr
        buf = io.BytesIO(expr.strip().encode("utf-8"))
        tokens = tokenize.tokenize(buf.readline)
        return [
            (EXACT_TOKEN_TYPES.get(s, tt) if tt == tokenize.OP else tt, s)
            for tt, s, _, _, _ in tokens
        ]

    def _parse_take_expr(self, tokens, *stop_at):
        nesting = []
        expr = []
        while tokens:
            tt, s = tokens[0]
            if tt == tokenize.LSQB and len(tokens) > 2 and tokens[1][0] in stop_at:
                return expr
            if tt in PAREN_TOKEN_MAP:
                expr.append((tt, s))
                nesting.append(PAREN_TOKEN_MAP[tt])
            elif nesting and tt == nesting[-1]:
                expr.append((tt, s))
                nesting.pop()
            elif tt in (tokenize.RPAR, tokenize.RBRACE, tokenize.RSQB):
                return expr
            elif not nesting and tt in stop_at:
                return expr
            else:
                expr.append((tt, s))
            tokens.pop(0)
        return expr

    def _parse_format_arg(self, name, args, defaults):
        defaults = list(defaults)
        default_set = set(defaults)
        seen_names = SeenNames(INVALID_ARGNAMES)
        parts = [name or "<function>", "("]
        arg_parts = []
        any_default = False

        for a_names, a_ann, a_def, a_opt in args:
            if not a_names:
                continue
            a_name = "".join(a_names)
            if a_name in default_set:
                default_set.discard(a_name)

            arg_parts.append(seen_names.make_unique(a_name))
            if can_eval("".join(a_ann)):
                # TODO: Fix unqualified typing annotations, rather than omitting them.
                # arg_parts.append(": ")
                # arg_parts.extend(a_ann)
                pass
            if can_eval("".join(a_def)):
                arg_parts.append("=")
                # arg_parts.extend(a_def)
                arg_parts.extend("...")
                any_default = True
            elif a_opt[0] or (any_default and "*" not in a_name and "**" not in a_name):
                # arg_parts.append("=None")
                arg_parts.append("=...")
                any_default = True
            if a_name.startswith("*"):
                any_default = True
            arg_parts.append(", ")

        if default_set:
            for a in defaults:
                if a in default_set:
                    parts.append(a)
                    parts.append(", ")
        parts.extend(arg_parts)
        if parts[-1] == ", ":
            parts.pop()
        if parts and parts[-1] in ("*", "**"):
            parts[-1] += seen_names.make_unique("_")

        parts.append(")")

        return "".join(parts)

    def _parse_funcdef(self, expr, allow_name_mismatch, defaults, override_name=None):
        """Takes a call expression that was part of a docstring
        and parses the AST as if it were a definition. If the parsed
        AST matches the callable we are wrapping, returns the node.
        """
        try:
            tokens = self._tokenize(expr)
        except (TypeError, tokenize.TokenError):
            warnings.warn("failed to tokenize " + expr, InspectWarning)
            return None

        name = None
        seen_open_paren = False
        args = [([], [], [], [False])]
        optional = False

        while tokens:
            tt, s = tokens.pop(0)
            if tt == tokenize.NAME:
                if override_name is not None and s == override_name:
                    name = s

                if name is None:
                    name = s
                elif seen_open_paren:
                    args[-1][0].append(s)
                    args[-1][3][0] = optional
            elif tt in (tokenize.STAR, tokenize.DOUBLESTAR):
                args[-1][0].append(s)
            elif tt == tokenize.COLON:
                e = self._parse_take_expr(tokens, tokenize.EQUAL, tokenize.COMMA)
                args[-1][1].append("".join(i[1] for i in e))
            elif tt == tokenize.EQUAL:
                if not seen_open_paren:
                    name = None
                    continue
                e = self._parse_take_expr(tokens, tokenize.COMMA)
                args[-1][2].append("".join(i[1] for i in e))
            elif tt == tokenize.COMMA:
                args.append(([], [], [], [False]))
            elif tt == tokenize.LSQB:
                optional = True
            elif tt == tokenize.RSQB:
                optional = False
            elif tt == tokenize.LPAR:
                seen_open_paren = True
            elif tt == tokenize.RPAR:
                break
            elif s in ("->", "..."):
                return None

            # TODO: Handle '/', the positional-only argument separator, when stubs support them.

        if name and (allow_name_mismatch or name == self.name):
            return self._parse_format_arg(override_name or name, args, defaults)

    def _get_first_function_call(self, expr: str, name: str):
        """Scans the string for the first closing parenthesis,
        handling nesting, which is the best heuristic we have for
        an example call at the start of the docstring."""
        # Note: line may or may not contain complete (...) and closing ')' may be on another line.
        # We also prevent going too far into the expression so it does not pick random x() in comments.
        if "\n\n" not in expr and name not in expr:
            return None

        expr = expr.split("\n\n")[0]
        if not expr or ")" not in expr:
            return None

        found = []
        n = 0
        expr = expr.replace("\r", " ").replace("\n", " ").replace("\t", " ")

        # See whether string before open paren is valid.
        openParenIndex = expr.find("(")
        if openParenIndex < 0:
            return None

        header = expr[:openParenIndex].strip()
        tokens = header.split(" ")
        tokenLength = len(tokens)
        if tokenLength == 0:
            # Nothing before "("
            return None

        if not tokens[tokenLength - 1].isidentifier() and name not in tokens[tokenLength - 1]:
            # Token before "(" is not valid identifier.
            return None

        if tokenLength > 1 and tokens[tokenLength - 2].isidentifier():
            # 2 consecutive words separated by a space. probably not a function call.
            return None

        expr = expr.replace(" ", "")

        for i, c in enumerate(expr):
            if c == ")":
                n -= 1
                if n == 0:
                    return expr[: i + 1]
            elif c == "(":
                n += 1

        return None


SKIP_TYPENAME_FOR_TYPES = bool, str, bytes, int, float
STATICMETHOD_TYPES = ()
CLASSMETHOD_TYPES = (type(float.fromhex),)
PROPERTY_TYPES = type(int.real), type(property.fget)

INVALID_ARGNAMES = set(keyword.kwlist)

# These full names are known to be lies. When we encounter
# them while scraping a module, assume that we need to write
# out the full type rather than including them by reference.
# TODO: Which of these are still needed?
LIES_ABOUT_MODULE = frozenset(
    [
        builtins.__name__ + ".weakcallableproxy",
        builtins.__name__ + ".weakproxy",
        builtins.__name__ + ".weakref",
        "ctypes.ArgumentError",
        "os.stat_result",
        "os.statvfs_result",
        "xml.parsers.expat.ExpatError",
        "numpy.broadcast",
        "numpy.busdaycalendar",
        "numpy.dtype",
        "numpy.flagsobj",
        "numpy.flatiter",
        "numpy.ndarray",
        "numpy.nditer",
        # These modules contain multiple members that lie about their
        # module. Always write out all members of these in full.
        "_asyncio.*",
        "_bsddb.*",
        "_decimal.*",
        "_elementtree.*",
        "_socket.*",
        "_sqlite3.*",
        "_ssl.*",
        "_testmultiphase.*",
    ]
)

# These symbols have decls but doc strings are not on them.
# Make sure we write them down on scraped file.
MUST_EMIT_DOCSTRINGS = frozenset(
    [
        "_collections.defaultdict",
        "_collections.deque",
    ]
)

# These type names cause conflicts with their values, so
# we need to forcibly rename them.
# TODO: Which of these are still needed?
SYS_INFO_TYPES = frozenset(
    (
        "float_info",
        "hash_info",
        "int_info",
        "thread_info",
        "version_info",
    )
)

VALUE_REPR_FIX = {
    float("inf"): "float('inf')",
    float("-inf"): "float('-inf')",
}

IMPLICIT_CLASSMETHOD = ("__new__",)


# TODO: Canonicalize internal storage as an inspect.Signature.
class Signature(object):
    KNOWN_RESTYPES = {
        "__abs__": "__T__",
        "__add__": "__T__",
        "__and__": "__T__",
        "__annotations__": "typing.Dict[str, typing.Any]",
        "__base__": "type",
        "__bases__": "typing.Tuple[type, ...]",
        "__bool__": "bool",
        "__call__": "typing.Any",
        "__ceil__": "__T__",
        "__code__": "types.CodeType",
        "__contains__": "bool",
        "__del__": "None",
        "__delattr__": "None",
        "__delitem__": "None",
        "__dict__": "typing.Dict[str, typing.Any]",
        "__dir__": "typing.Iterable[str]",
        "__divmod__": "typing.Tuple[__T__, __T__]",
        "__eq__": "bool",
        "__format__": "str",
        "__float__": "float",
        "__floor__": "__T__",
        "__floordiv__": "int",
        "__ge__": "bool",
        "__get__": "__T__",
        "__getattr__": "typing.Any",
        "__getattribute__": "typing.Any",
        "__getitem__": "typing.Any",
        "__getnewargs__": "typing.Tuple[__T__]",
        "__getnewargs_ex__": "typing.Tuple[typing.Tuple[typing.Any, ...], typing.Dict[str, typing.Any]]",
        "__getslice__": "__T__",
        "__globals__": "typing.Dict[str, typing.Any]",
        "__gt__": "bool",
        "__hash__": "int",
        "__iadd__": "None",
        "__iand__": "None",
        "__imul__": "None",
        "__index__": "int",
        "__init__": "None",
        "__init_subclass__": "None",
        "__int__": "int",
        "__invert__": "__T__",
        "__ior__": "None",
        "__isub__": "None",
        "__iter__": "__T__",
        "__ixor__": "None",
        "__le__": "bool",
        "__len__": "int",
        "__length_hint__": "int",
        "__lshift__": "__T__",
        "__lt__": "bool",
        "__mod__": "__T__",
        "__mul__": "__T__",
        "__ne__": "bool",
        "__neg__": "__T__",
        "__next__": "typing.Any",
        "__pos__": "__T__",
        "__pow__": "__T__",
        "__or__": "__T__",
        "__radd__": "__T__",
        "__rand__": "__T__",
        "__rdivmod__": "typing.Tuple[__T__, __T__]",
        "__rfloordiv__": "__T__",
        "__rlshift__": "__T__",
        "__rmod__": "__T__",
        "__rmul__": "__T__",
        "__ror__": "__T__",
        "__round__": "__T__",
        "__rpow__": "__T__",
        "__rrshift__": "__T__",
        "__rshift__": "__T__",
        "__rsub__": "__T__",
        "__rtruediv__": "__T__",
        "__rxor__": "__T__",
        "__reduce__": "typing.Union[str, typing.Tuple[typing.Any, ...]]",
        "__reduce_ex__": "typing.Union[str, typing.Tuple[typing.Any, ...]]",
        "__repr__": "str",
        "__set__": "None",
        "__setattr__": "None",
        "__setitem__": "None",
        "__setstate__": "None",
        "__sizeof__": "int",
        "__str__": "str",
        "__sub__": "__T__",
        "__truediv__": "float",
        "__trunc__": "__T__",
        "__xor__": "__T__",
        "__subclasscheck__": "bool",
        "__subclasshook__": "bool",
    }

    KNOWN_ARGSPECS = {
        "__contains__": "(self, value: typing.Any)",
        "__del__": "(self)",
        "__dir__": "(self)",
        "__floor__": "(self)",
        "__format__": "(self, format_spec: str)",
        "__getitem__": "(self, index: int)",
        "__getnewargs__": "(self)",
        "__getnewargs_ex__": "(self)",
        "__init_subclass__": "(cls)",
        "__instancecheck__": "(self, instance: typing.Any)",
        "__length_hint__": "(self)",
        "__prepare__": "(cls, name: str, bases: typing.Tuple[type, ...], **kwds: typing.Any)",  # TODO: ???
        "__round__": "(self, ndigits: int = ...)",
        "__reduce__": "(self)",
        "__reduce_ex__": "(self, protocol: int)",
        "__reversed__": "(self)",
        "__setitem__": "(self, index: typing.Any, value: typing.Any)",
        "__setstate__": "(self, state: typing.Any)",
        "__sizeof__": "(self)",
        "__subclasses__": "(cls)",
        "__subclasscheck__": "(cls, subclass: typing.Any)",
        "__subclasshook__": "(cls, subclass: typing.Any)",
        "__trunc__": "(self)",
    }

    def __init__(
        self,
        name,
        callable,
        scope=None,
        defaults=None,
        scope_alias=None,
        decorators=None,
        fallback_doc=None,
    ):
        self.callable = callable
        self.name = name
        self.scope = scope
        self.decorators = decorators or ()
        self._signature = None
        self._defaults = defaults or ()

        if scope and "@staticmethod" not in self.decorators:
            def_arg = (
                "cls"
                if ("@classmethod" in self.decorators or name in IMPLICIT_CLASSMETHOD)
                else "self"
            )
            if len(self._defaults) == 0 or self._defaults[0] != def_arg:
                self._defaults = (def_arg,) + self._defaults

        ds_parser = DocstringSigParser(self.callable, self.name, self._defaults)

        self.fullsig = None
        self.restype = None

        # TODO: Combine this with the check for "See help(type(self))" in MemberInfo.
        if self.name in ("__init__", "__new__") and fallback_doc:
            self.fullsig = ds_parser.argspec(doc=fallback_doc, override_name=self.name)
        elif not hasattr(self.callable, "__call__") and hasattr(
            self.callable, "__get__"
        ):
            # We have a property
            self.decorators = ("@property",)
            self.fullsig = self.name + "(" + ", ".join(self._defaults) + ")"

        if scope == "object" and name == "__init__":
            self.fullsig = "__init__(self)"
            self.restype = "None"

        # TODO: Strip defaults, replace the "restype" with an actual type that is added after the "->".

        self.fullsig = (
            self.fullsig
            # Disable fromsignature() because it doesn't work as well as argspec
            # or self._init_argspec_fromsignature()
            or self._init_argspec_fromargspec()
            or self._init_argspec_fromknown(scope_alias)
            or ds_parser.argspec(override_name=self.name)
            or (self.name + "(" + ", ".join(self._defaults) + ")")
        )

        self.restype = (
            self.restype
            or self._init_restype_fromsignature()
            or self._init_restype_fromknown(scope_alias)
            or ds_parser.restype()
        )

        if self.restype and scope:
            self.restype = self.restype.replace("__T__", scope)

        # Special case for 'with' statement and built-ins like open() or memoryview
        if name == "__enter__" and self.restype == "pass":
            self.restype = scope

    def __str__(self):
        return self.fullsig

    def _init_argspec_fromsignature(self):
        if do_not_inspect(self.callable):
            return None

        try:
            sig = inspect.signature(self.callable)
        except Exception:
            return None

        new_args = []
        for arg in sig.parameters:
            p = sig.parameters[arg]
            if p.default != inspect.Signature.empty:
                # TODO: Replace deafult with ELLIPSIS_DEFAULT
                # TODO: Figure out how to qualify things inside the type annotation.
                try:
                    ast.literal_eval(repr(p.default))
                except Exception:
                    p = p.replace(default=None)
            if p.kind == inspect.Parameter.POSITIONAL_ONLY:
                p = p.replace(kind=inspect.Parameter.POSITIONAL_OR_KEYWORD)
            new_args.append(p)
        sig = sig.replace(parameters=new_args)

        # TODO: This duplicates return types, since str(sig) contains the return annotation.
        return self.name + str(sig)

    def _init_restype_fromsignature(self):
        if do_not_inspect(self.callable):
            return None

        try:
            sig = inspect.signature(self.callable)
        except Exception:
            return None

        # If signature has a return annotation, it's in the
        # full signature and we don't need it from here.
        if not sig or sig.return_annotation == inspect._empty:
            return None
        ann = inspect.formatannotation(sig.return_annotation)
        if not ann or not can_eval(ann):
            return None
        return ann

    def _init_argspec_fromargspec(self):
        if do_not_inspect(self.callable):
            return None

        try:
            args = inspect.getfullargspec(self.callable)
        except Exception:
            return None

        argn = []
        seen_names = SeenNames(INVALID_ARGNAMES)
        defaults = list(self._defaults)
        default_set = set(defaults)

        for a in args.args:
            if a in default_set:
                default_set.discard(a)
            argn.append(seen_names.make_unique(a))
        if default_set:
            argn[:0] = [a for a in defaults if a in default_set]

        if getattr(args, "varargs", None):
            argn.append("*" + args.varargs)
        if getattr(args, "varkw", None):
            argn.append("**" + args.varkw)

        if argn and argn[-1] in ("*", "**"):
            argn[-1] += seen_names.make_unique("_")

        return self.name + "(" + ", ".join(argn) + ")"

    def _init_argspec_fromknown(self, scope_alias):
        spec = None
        if scope_alias and not spec:
            spec = self.KNOWN_ARGSPECS.get(scope_alias + "." + self.name)
        if self.scope and not spec:
            spec = self.KNOWN_ARGSPECS.get(self.scope + "." + self.name)
        if not spec:
            spec = self.KNOWN_ARGSPECS.get(self.name)
        if not spec:
            return None

        return self.name + spec

    def _init_restype_fromknown(self, scope_alias):
        restype = None
        if scope_alias and not restype:
            restype = self.KNOWN_RESTYPES.get(scope_alias + "." + self.name)
        if self.scope and not restype:
            restype = self.KNOWN_RESTYPES.get(self.scope + "." + self.name)
        if not restype:
            restype = self.KNOWN_RESTYPES.get(self.name)
        if not restype:
            return None

        return restype


class MemberInfo(object):
    NO_VALUE = object()

    def __init__(
        self,
        name,
        value,
        literal=None,
        type_literal=None,
        scope=None,
        module=None,
        alias=None,
        fallback_doc=None,
        scope_alias=None,
    ):
        self.name = name
        self.module = module
        self.value = value
        self.literal = literal
        self.type_literal = type_literal
        self.members = []
        self.values = []
        self.need_imports = ()
        self.type_name = None
        self.scope_name = None
        self.bases = ()
        self.signature = None
        self.documentation = getattr(value, "__doc__", None)
        self.alias = alias
        self.instance = True

        if not isinstance(self.documentation, str):
            self.documentation = None

        # Special case for __init__ that refers to class docs
        if self.name == "__init__" and (
            not self.documentation or "See help(type(self))" in self.documentation
        ):
            self.documentation = fallback_doc

        if self.name:
            self.name = self.name.replace("-", "_")

        value_type = type(value)
        if issubclass(value_type, type):
            self.instance = False
            self.need_imports, type_name = self._get_typename(value, module)
            if "." in type_name:
                m, s, n = type_name.rpartition(".")
                self.literal = safe_module_name(m) + s + n
            else:
                self.scope_name = self.type_name = type_name
                self._collect_bases(value, module, self.type_name)

        elif is_callable(value):
            dec = ()
            if scope:
                if value_type in STATICMETHOD_TYPES:
                    dec += ("@staticmethod",)
                elif value_type in CLASSMETHOD_TYPES:
                    dec += ("@classmethod",)
            self.signature = Signature(
                name,
                value,
                scope,
                scope_alias=scope_alias,
                decorators=dec,
                fallback_doc=fallback_doc,
            )

        elif value is not None:
            if value_type in PROPERTY_TYPES:
                self.signature = Signature(name, value, scope, scope_alias=scope_alias)
            if value_type not in ():  # SKIP_TYPENAME_FOR_TYPES:
                self.need_imports, self.type_name = self._get_typename(
                    value_type, module
                )
                self._collect_bases(value_type, module, self.type_name)
            # if isinstance(value, float) and repr(value) == "nan":
            #     self.literal = "float('nan')"
            # try:
            #     self.literal = VALUE_REPR_FIX[value]
            # except Exception:
            #     pass

        # elif not self.literal:
        #     self.literal = "None"

    def _collect_bases(self, value_type, module, type_name):
        try:
            bases = getattr(value_type, "__bases__", ())
        except Exception:
            pass
        else:
            self.bases = []
            self.need_imports = list(self.need_imports)
            for ni, t in (self._get_typename(b, module) for b in bases):
                if not t:
                    continue
                if t == type_name and module in ni:
                    continue
                self.bases.append(t)
                self.need_imports.extend(ni)

    @classmethod
    def _get_typename(cls, value_type, in_module):
        try:
            type_name = value_type.__name__.replace("-", "_")
            module = getattr(value_type, "__module__", None)

            if module and module != "<unknown>":
                if module == in_module:
                    return (module,), type_name

                fullname = module + "." + type_name

                if in_module and (
                    fullname in LIES_ABOUT_MODULE
                    or (in_module + ".*") in LIES_ABOUT_MODULE
                ):
                    # Treat the type as if it came from the current module
                    return (in_module,), type_name

                return (module,), fullname

            return (), type_name
        except Exception:
            warnings.warn("could not get type of " + repr(value_type), InspectWarning)
            raise

    def _str_from_typename(self, type_name):
        mod_name, sep, name = type_name.rpartition(".")
        if mod_name == "builtins":
            type_name = name
        else:
            type_name = safe_module_name(mod_name) + sep + name

        s = self.name + ": " + type_name
        # s = s + "()"
        if not self.instance:
            # TODO: Handle non-instances
            pass
        return s

    def _lines_with_members(self):
        if self.bases:
            split_bases = [n.rpartition(".") for n in self.bases]
            bases = ",".join(
                (safe_module_name(n[0]) + n[1] + n[2]) for n in split_bases
            )
            yield "class " + self.name + "(" + bases + "):"
        else:
            yield "class " + self.name + ":"
        if self.documentation:
            yield "    " + repr(self.documentation)
        if self.members:
            for mi in self.members:
                if (
                    hasattr(mi, "documentation")
                    and mi.documentation != None
                    and not isinstance(mi.documentation, str)
                ):
                    continue
                if mi is not MemberInfo.NO_VALUE:
                    yield mi.as_str("    ")
        else:
            yield "    pass"
        yield ""

    def _lines_with_signature(self):
        seen_decorators = set()
        for d in self.signature.decorators:
            d = str(d)
            if d not in seen_decorators:
                seen_decorators.add(d)
                yield d

        line = "def " + str(self.signature)

        restype = self.signature.restype
        if restype is None:
            restype = "typing.Any"

        line += " -> " + restype
        yield line + ":"

        if self.documentation:
            yield "    " + repr(self.documentation)

        yield "    ..."

        yield ""

    def as_str(self, indent=""):
        if self.literal:
            literal = indent + self.name + " = " + self.literal

            # Put doc string next to reference.
            if self.module + "." + self.name in MUST_EMIT_DOCSTRINGS:
                literal += "\n" + indent + repr(self.documentation)

            return literal

        if self.type_literal:
            return indent + self.name + ": " + self.type_literal

        if self.members:
            return "\n".join(indent + s for s in self._lines_with_members())

        if self.signature:
            return "\n".join(indent + s for s in self._lines_with_signature())

        if self.type_name is not None:
            return indent + self._str_from_typename(self.type_name)

        if self.value is not None:
            return indent + self.name + " = " + repr(self.value)

        return indent + self.name + ": typing.Any"


MODULE_MEMBER_SUBSTITUTE = {
    "__spec__": None,
    "__loader__": None,
}

CLASS_MEMBER_SUBSTITUTE = {
    "__bases__": MemberInfo("__bases__", None, type_literal="typing.Tuple[type, ...]"),
    "__mro__": MemberInfo("__mro__", None, type_literal="typing.Tuple[type, ...]"),
    # TODO: Only expose this on object and not every other class?
    "__dict__": MemberInfo(
        "__dict__", None, type_literal="typing.Dict[str, typing.Any]"
    ),
    "__doc__": None,
    "__new__": None,
}


def do_import(module_name, search_path=None):
    """
    Imports a module by name and returns the module.
    If the import fails, the exception is analyzed for a fix and retried.
    """
    if search_path:
        sys.path.insert(0, search_path)

    try:
        return importlib.import_module(module_name)
    except Exception:
        ex_msg = str(sys.exc_info()[1])
        warnings.warn("Working around " + ex_msg, InspectWarning)
        if ex_msg == "This must be an MFC application - try 'import win32ui' first":
            importlib.import_module("win32ui")
        elif (
            ex_msg == "Could not find TCL routines"
            or module_name == "matplotlib.backends._tkagg"
        ):
            importlib.import_module("tkinter")
        else:
            raise
    finally:
        if search_path:
            del sys.path[0]

    return importlib.import_module(module_name)


def mro_contains(mro, name, value):
    for m in mro:
        try:
            mro_value = getattr(m, name)
        except Exception:
            pass
        else:
            if mro_value is value:
                return True
    return False


class ScrapeState(object):
    def __init__(self, module_name, search_path):
        self.root_module = None
        self.module_name = module_name
        self.module = do_import(self.module_name, search_path)
        self.members = []

    def collect_top_level_members(self):
        self._collect_members(self.module, self.members, MODULE_MEMBER_SUBSTITUTE, None)

        if self.module_name == "sys":
            sysinfo = [m for m in self.members if m.type_name in SYS_INFO_TYPES]
            for m in sysinfo:
                self.members.append(
                    MemberInfo(m.name, None, literal="__" + m.name + "()")
                )
                m.name = m.scope_name = m.type_name = "__" + m.type_name

        m_names = set(m.name for m in self.members)
        undeclared = []
        for m in self.members:
            if (
                m.value is not None
                and m.type_name
                and "." not in m.type_name
                and m.type_name not in m_names
            ):
                undeclared.append(
                    MemberInfo(m.type_name, type(m.value), module=self.module_name)
                )

        self.members[:0] = undeclared

    def _should_collect_members(self, member):
        if self.module_name in member.need_imports and member.name == member.type_name:
            return True

        # Support cffi libs
        if member.type_name == builtins.__name__ + ".CompiledLib":
            return True

        return False

    def collect_second_level_members(self):
        for mi in self.members:
            if not self._should_collect_members(mi):
                continue

            substitutes = dict(CLASS_MEMBER_SUBSTITUTE)
            # substitutes["__class__"] = MemberInfo(
            #     "__class__", None, literal=mi.type_name
            # )
            self._collect_members(mi.value, mi.members, substitutes, mi)

            if mi.scope_name == mi.type_name:
                continue

            # When the scope and type names are different, we have a static
            # class. To emulate this, we add '@staticmethod' decorators to
            # all members.
            for mi2 in mi.members:
                if mi2.signature:
                    mi2.signature.decorators += ("@staticmethod",)

    def _collect_members(self, mod, members, substitutes, outer_member):
        """Fills the members attribute with a dictionary containing
        all members from the module."""
        if not mod:
            raise RuntimeError("failed to import module")
        if mod is MemberInfo.NO_VALUE:
            return

        existing_names = set(m.name for m in members)

        if outer_member:
            scope = outer_member.scope_name
            scope_alias = outer_member.alias
        else:
            scope, scope_alias = None, None

        mod_scope = (self.module_name + "." + scope) if scope else self.module_name
        fallback_doc = getattr(mod, "__doc__", None)
        mro = (getattr(mod, "__mro__", None) or ())[1:]
        for name in dir(mod):
            if keyword.iskeyword(name):
                continue
            try:
                m = substitutes[name]
                if m:
                    members.append(m)
                continue
            except LookupError:
                pass
            try:
                m = substitutes[mod_scope + "." + name]
                if m:
                    members.append(m)
                continue
            except LookupError:
                pass

            if name in existing_names:
                continue

            try:
                value = getattr(mod, name)
            except AttributeError:
                warnings.warn(
                    "attribute "
                    + name
                    + " on "
                    + repr(mod)
                    + " was in dir() but not getattr()",
                    InspectWarning,
                )
            except Exception:
                warnings.warn(
                    "error getting " + name + " for " + repr(mod), InspectWarning
                )
            else:
                if not self._should_add_value(value):
                    continue
                if name != "__init__" and mro_contains(mro, name, value):
                    continue
                members.append(
                    MemberInfo(
                        name,
                        value,
                        scope=scope,
                        module=self.module_name,
                        fallback_doc=fallback_doc,
                        scope_alias=scope_alias,
                    )
                )
        if not "__getattr__" in existing_names:
            value = (
                self.__getattr__dummy if scope else ScrapeState.__getattr__dummy_module
            )
            members.append(
                MemberInfo(
                    "__getattr__",
                    value,
                    scope=None,
                    module=self.module_name,
                )
            )

    def __getattr__dummy(self, name):
        pass

    @classmethod
    def __getattr__dummy_module(name):
        pass

    def _should_add_value(self, value):
        try:
            value_type = type(value)
            mod = getattr(value_type, "__module__", None)
            name = value_type.__name__
        except Exception:
            warnings.warn("error getting typename", InspectWarning)
            return False

        if (mod, name) == (builtins.__name__, "CompiledLib"):
            # Always allow CFFI lib
            return True

        if issubclass(value_type, (type(sys), type(inspect))):
            # Disallow nested modules
            return False

        # By default, include all values
        return True

    def dump(self, out):
        print_module_version(self.module, out)

        documentation = getattr(self.module, "__doc__", None)
        if isinstance(documentation, str):
            print("", file=out)
            print(repr(documentation), file=out)
            print("", file=out)

        print("import typing", file=out)

        imports = set()
        for value in self.members:
            for mod in value.need_imports:
                imports.add(mod)
        imports.discard(self.module_name)

        if imports:
            for mod in sorted(imports):
                print("import " + mod + " as " + safe_module_name(mod), file=out)
            print("", file=out)

        for value in self.members:
            s = value.as_str("")
            try:
                print(s, file=out)
            except TypeError:
                print(repr(s), file=sys.stderr)
                raise


def main():
    module_name = sys.argv[1] if len(sys.argv) > 1 else "builtins"
    search_path = sys.argv[2] if len(sys.argv) > 2 else None

    state = ScrapeState(module_name, search_path)
    state.collect_top_level_members()

    state.members[:] = [m for m in state.members if m.name not in keyword.kwlist]

    state.collect_second_level_members()

    state.dump(sys.stdout)


if __name__ == "__main__":
    main()
