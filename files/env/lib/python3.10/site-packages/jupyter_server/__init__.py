"""The Jupyter Server"""
import os
import subprocess
import sys

DEFAULT_STATIC_FILES_PATH = os.path.join(os.path.dirname(__file__), "static")
DEFAULT_TEMPLATE_PATH_LIST = [
    os.path.dirname(__file__),
    os.path.join(os.path.dirname(__file__), "templates"),
]

DEFAULT_JUPYTER_SERVER_PORT = 8888

del os

from ._version import __version__, version_info  # noqa


def _cleanup():
    pass


# patch subprocess on Windows for python<3.7
# see https://bugs.python.org/issue37380
# the fix for python3.7: https://github.com/python/cpython/pull/15706/files
if sys.platform == "win32":
    if sys.version_info < (3, 7):
        subprocess._cleanup = _cleanup
        subprocess._active = None
