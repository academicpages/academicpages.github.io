"""Jedi Language Server."""
import sys

if sys.version_info < (3, 8):
    from importlib_metadata import version
else:
    from importlib.metadata import version

__version__ = version("jedi-language-server")
