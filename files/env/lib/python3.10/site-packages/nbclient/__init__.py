import subprocess
import sys

from ._version import __version__  # noqa
from ._version import version_info  # noqa
from .client import NotebookClient, execute  # noqa: F401


def _cleanup() -> None:
    pass


# patch subprocess on Windows for python<3.7
# see https://bugs.python.org/issue37380
# the fix for python3.7: https://github.com/python/cpython/pull/15706/files
if sys.platform == 'win32':
    if sys.version_info < (3, 7):
        subprocess._cleanup = _cleanup
        subprocess._active = None
