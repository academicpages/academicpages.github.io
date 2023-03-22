# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root
# for license information.

from __future__ import absolute_import, division, print_function, unicode_literals

"""Provides facilities to use objects as modules, enabling __getattr__, __call__
etc on module level.
"""

import sys
import types


def module(name):
    """A decorator for classes that implement modules.

    Idiomatic usage is with __name__, so that an instance of the class replaces the
    module in which it is defined::

        # foo.py
        @module(__name__)
        class Foo(object):
            def __call__(self): ...

        # bar.py
        import foo
        foo()

    "Regular" globals, including imports, don't work with class modules. Class or
    instance attributes must be used consistently for this purpose, and accessed via
    self inside method bodies::

        @module(__name__)
        class Foo(object):
            import sys

            def __call__(self):
                if self.sys.version_info < (3,): ...
    """

    def decorate(cls):
        class Module(cls, types.ModuleType):
            def __init__(self):
                # Set self up as a proper module, and copy pre-existing globals.
                types.ModuleType.__init__(self, name)
                self.__dict__.update(sys.modules[name].__dict__)

                cls.__init__(self)

        Module.__name__ = cls.__name__
        sys.modules[name] = Module()

    return decorate
