# Copyright (c) Microsoft Corporation. All rights reserved.
# # Licensed under the MIT License. See LICENSE in the project root
# for license information.

from __future__ import absolute_import, division, print_function, unicode_literals

"""Python 2/3 compatibility helpers.
"""

import functools
import inspect
import itertools
import sys

from debugpy.common import fmt

if sys.version_info[0] < 3:
    # Py2
    import __builtin__ as builtins  # noqa
    from __builtin__ import unicode, bytes, xrange, reload  # noqa

    izip = itertools.izip

    import Queue as queue  # noqa

    def force_str(s, encoding="ascii", errors="strict"):
        """Converts s to str (which is bytes on Python 2, and unicode on Python 3), using
        the provided encoding if necessary. If s is already str, it is returned as is.
    
        If errors="strict", str is bytes, and s is str, its encoding is verified by decoding
        it; UnicodeError is raised if it cannot be decoded.
        """
        return force_bytes(s, encoding, errors)


else:
    # Py3
    import builtins  # noqa
    from builtins import bytes  # noqa

    unicode = str
    xrange = range
    izip = zip
    from importlib import reload  # noqa
    import queue  # noqa

    def force_str(s, encoding="ascii", errors="strict"):
        """Converts s to str (which is bytes on Python 2, and unicode on Python 3), using
        the provided encoding if necessary. If s is already str, it is returned as is.
    
        If errors="strict", str is bytes, and s is str, its encoding is verified by decoding
        it; UnicodeError is raised if it cannot be decoded.
        """
        return force_unicode(s, encoding, errors)


def force_unicode(s, encoding, errors="strict"):
    """Converts s to Unicode, using the provided encoding. If s is already Unicode,
    it is returned as is.
    """
    return s.decode(encoding, errors) if isinstance(s, bytes) else unicode(s)


def force_bytes(s, encoding, errors="strict"):
    """Converts s to bytes, using the provided encoding. If s is already bytes,
    it is returned as is.

    If errors="strict" and s is bytes, its encoding is verified by decoding it;
    UnicodeError is raised if it cannot be decoded.
    """
    if isinstance(s, unicode):
        return s.encode(encoding, errors)
    else:
        s = bytes(s)
        if errors == "strict":
            # Return value ignored - invoked solely for verification.
            s.decode(encoding, errors)
        return s


def force_ascii(s, errors="strict"):
    """Same as force_bytes(s, "ascii", errors)
    """
    return force_bytes(s, "ascii", errors)


def force_utf8(s, errors="strict"):
    """Same as force_bytes(s, "utf8", errors)
    """
    return force_bytes(s, "utf8", errors)


def filename(s, errors="strict"):
    """Same as force_unicode(s, sys.getfilesystemencoding(), errors)
    """
    return force_unicode(s, sys.getfilesystemencoding(), errors)


def filename_bytes(s, errors="strict"):
    """Same as force_bytes(s, sys.getfilesystemencoding(), errors)
    """
    return force_bytes(s, sys.getfilesystemencoding(), errors)


def filename_str(s, errors="strict"):
    """Same as force_str(s, sys.getfilesystemencoding(), errors)
    """
    return force_str(s, sys.getfilesystemencoding(), errors)


def nameof(obj, quote=False):
    """Returns the most descriptive name of a Python module, class, or function,
    as a Unicode string

    If quote=True, name is quoted with repr().

    Best-effort, but guaranteed to not fail - always returns something.
    """

    try:
        name = obj.__qualname__
    except Exception:
        try:
            name = obj.__name__
        except Exception:
            # Fall back to raw repr(), and skip quoting.
            try:
                name = repr(obj)
            except Exception:
                return "<unknown>"
            else:
                quote = False

    if quote:
        try:
            name = repr(name)
        except Exception:
            pass

    return force_unicode(name, "utf-8", "replace")


def unicode_repr(obj):
    """Like repr(), but guarantees that the result is Unicode even on Python 2.
    """
    return force_unicode(repr(obj), "ascii")


def srcnameof(obj):
    """Returns the most descriptive name of a Python module, class, or function,
    including source information (filename and linenumber), if available.

    Best-effort, but guaranteed to not fail - always returns something.
    """

    name = nameof(obj, quote=True)

    # Get the source information if possible.
    try:
        src_file = filename(inspect.getsourcefile(obj), "replace")
    except Exception:
        pass
    else:
        name += fmt(" (file {0!r}", src_file)
        try:
            _, src_lineno = inspect.getsourcelines(obj)
        except Exception:
            pass
        else:
            name += fmt(", line {0}", src_lineno)
        name += ")"

    return name


def kwonly(f):
    """Makes all arguments with default values keyword-only.

    If the default value is kwonly.required, then the argument must be specified.
    """

    try:
        inspect.getfullargspec
    except AttributeError:
        arg_names, args_name, kwargs_name, arg_defaults = inspect.getargspec(f)
    else:
        arg_names, args_name, kwargs_name, arg_defaults, _, _, _ = inspect.getfullargspec(
            f
        )

    assert args_name is None and kwargs_name is None
    argc = len(arg_names)
    pos_argc = argc - len(arg_defaults)
    required_names = {
        name
        for name, val in zip(arg_names[pos_argc:], arg_defaults)
        if val is kwonly.required
    }

    @functools.wraps(f)
    def kwonly_f(*args, **kwargs):
        if len(args) > pos_argc:
            raise TypeError("too many positional arguments")
        if not required_names.issubset(kwargs):
            missing_names = required_names.difference(kwargs)
            missing_names = ", ".join(repr(s) for s in missing_names)
            raise TypeError("missing required keyword-only arguments: " + missing_names)
        return f(*args, **kwargs)

    return kwonly_f


kwonly.required = object()
