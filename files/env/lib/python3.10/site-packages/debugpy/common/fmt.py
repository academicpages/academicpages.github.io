# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root
# for license information.

from __future__ import absolute_import, division, print_function, unicode_literals

"""Provides a custom string.Formatter with JSON support.

The formatter object is directly exposed as a module, such that all its members
can be invoked directly after it has been imported::

    from debugpy.common import fmt
    fmt("{0} is {value}", name, value=x)
"""

import string
import sys
import types


class Formatter(string.Formatter, types.ModuleType):
    """A custom string.Formatter with support for JSON pretty-printing.

    Adds {!j} format specification. When used, the corresponding value is converted
    to string using json_encoder.encode().

    Since string.Formatter in Python <3.4 does not support unnumbered placeholders,
    they must always be numbered explicitly - "{0} {1}" rather than "{} {}". Named
    placeholders are supported.
    """

    # Because globals() go away after the module object substitution, all method bodies
    # below must access globals via self instead, or re-import modules locally.

    from debugpy.common import json

    def __init__(self):
        # Set self up as a proper module, and copy globals.
        # types must be re-imported, because globals aren't there yet at this point.
        import types

        types.ModuleType.__init__(self, __name__)
        self.__dict__.update(sys.modules[__name__].__dict__)

    def __call__(self, format_string, *args, **kwargs):
        """Same as self.format().
        """
        return self.format(format_string, *args, **kwargs)

    def convert_field(self, value, conversion):
        if conversion == "j":
            return self.json.JsonObject(value)
        return super(self.Formatter, self).convert_field(value, conversion)


# Replace the standard module object for this module with a Formatter instance.
sys.modules[__name__] = Formatter()
