# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root
# for license information.

from __future__ import absolute_import, division, print_function, unicode_literals

import os
import sys

from debugpy.common import compat


def evaluate(code, path=__file__, mode="eval"):
    # Setting file path here to avoid breaking here if users have set
    # "break on exception raised" setting. This code can potentially run
    # in user process and is indistinguishable if the path is not set.
    # We use the path internally to skip exception inside the debugger.
    expr = compile(code, path, "eval")
    return eval(expr, {}, sys.modules)


class Observable(object):
    """An object with change notifications."""

    observers = ()  # used when attributes are set before __init__ is invoked

    def __init__(self):
        self.observers = []

    def __setattr__(self, name, value):
        try:
            return super(Observable, self).__setattr__(name, value)
        finally:
            for ob in self.observers:
                ob(self, name)


class Env(dict):
    """A dict for environment variables.
    """

    @staticmethod
    def snapshot():
        """Returns a snapshot of the current environment.
        """
        return Env(os.environ)

    def copy(self, updated_from=None):
        result = Env(self)
        if updated_from is not None:
            result.update(updated_from)
        return result

    def prepend_to(self, key, entry):
        """Prepends a new entry to a PATH-style environment variable, creating
        it if it doesn't exist already.
        """
        try:
            tail = os.path.pathsep + self[key]
        except KeyError:
            tail = ""
        self[key] = entry + tail

    def for_popen(self):
        """Returns a copy of this dict, with all strings converted to the type
        suitable for subprocess.Popen() and other similar APIs.
        """
        return {compat.filename_str(k): compat.filename_str(v) for k, v in self.items()}
