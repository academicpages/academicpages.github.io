# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root
# for license information.

from __future__ import absolute_import, division, print_function, unicode_literals

"""Provides monotonic timestamps with a resetable zero.
"""

import sys
import time

__all__ = ["current", "reset"]


if sys.version_info >= (3, 5):
    clock = time.monotonic
else:
    clock = time.clock


def current():
    return clock() - timestamp_zero


def reset():
    global timestamp_zero
    timestamp_zero = clock()


reset()
