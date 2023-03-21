# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os as _VSCODE_os
import site as _VSCODE_site

# Copied from site-packages/jupyter_core/paths.py

if _VSCODE_site.ENABLE_USER_SITE:
    # Check if site.getuserbase() exists to be compatible with virtualenv,
    # which often does not have this method.
    if hasattr(_VSCODE_site, "getuserbase"):
        _VSCODE_userbase = _VSCODE_site.getuserbase()
    else:
        _VSCODE_userbase = _VSCODE_site.USER_BASE

    if _VSCODE_userbase:
        _VSCODE_userbase = _VSCODE_os.path.join(_VSCODE_userbase, "share", "jupyter")
        print(_VSCODE_userbase)

    del _VSCODE_userbase

del _VSCODE_os, _VSCODE_site
