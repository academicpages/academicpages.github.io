# Copyright 2013 Hardcoded Software (http://www.hardcoded.net)

# This software is licensed under the "BSD" License as described in the "LICENSE" file,
# which should be included with this package. The terms are also available at
# http://www.hardcoded.net/licenses/bsd_license

import sys

from .exceptions import TrashPermissionError  # noqa: F401

if sys.platform == "darwin":
    from .plat_osx import send2trash
elif sys.platform == "win32":
    from .plat_win import send2trash
else:
    try:
        # If we can use gio, let's use it
        from .plat_gio import send2trash
    except ImportError:
        # Oh well, let's fallback to our own Freedesktop trash implementation
        from .plat_other import send2trash  # noqa: F401
