# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""Debugging support for LSP."""

import os
import pathlib
import runpy
import sys


def update_sys_path(path_to_add: str) -> None:
    """Add given path to `sys.path`."""
    if path_to_add not in sys.path and os.path.isdir(path_to_add):
        sys.path.append(path_to_add)


# Ensure debugger is loaded before we load anything else, to debug initialization.
if os.getenv("USE_DEBUGPY", None) in ["True", "TRUE", "1", "T"]:
    debugger_path = os.getenv("DEBUGPY_PATH", None)

    if debugger_path:
        if debugger_path.endswith("debugpy"):
            debugger_path = os.fspath(pathlib.Path(debugger_path).parent)

        update_sys_path(debugger_path)

        # pylint: disable=wrong-import-position,import-error
        import debugpy

        # 5678 is the default port, If you need to change it update it here
        # and in launch.json.
        debugpy.connect(5678)

        # This will ensure that execution is paused as soon as the debugger
        # connects to VS Code. If you don't want to pause here comment this
        # line and set breakpoints as appropriate.
        debugpy.breakpoint()

SERVER_PATH = os.fspath(pathlib.Path(__file__).parent / "server.py")
# NOTE: Set breakpoint in `server.py` before continuing.
runpy.run_path(SERVER_PATH, run_name="__main__")
