"""Terminals served to xterm.js using Tornado websockets"""

# Copyright (c) Jupyter Development Team
# Copyright (c) 2014, Ramalingam Saravanan <sarava@sarava.net>
# Distributed under the terms of the Simplified BSD License.

from ._version import __version__  # noqa
from .management import NamedTermManager  # noqa
from .management import SingleTermManager  # noqa
from .management import TermManagerBase  # noqa
from .management import UniqueTermManager  # noqa
from .websocket import TermSocket  # noqa
