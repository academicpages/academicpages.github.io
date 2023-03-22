"""Utilities for installing extensions"""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

import os
from tornado.log import LogFormatter
from traitlets import Bool, Any
from jupyter_core.application import JupyterApp
from jupyter_core.paths import (
    jupyter_config_dir, ENV_CONFIG_PATH, SYSTEM_CONFIG_PATH
)
from ._version import __version__

class ArgumentConflict(ValueError):
    pass

_base_flags = {}
_base_flags.update(JupyterApp.flags)
_base_flags.pop("y", None)
_base_flags.pop("generate-config", None)
_base_flags.update({
    "user" : ({
        "BaseExtensionApp" : {
            "user" : True,
        }}, "Apply the operation only for the given user"
    ),
    "system" : ({
        "BaseExtensionApp" : {
            "user" : False,
            "sys_prefix": False,
        }}, "Apply the operation system-wide"
    ),
    "sys-prefix" : ({
        "BaseExtensionApp" : {
            "sys_prefix" : True,
        }}, "Use sys.prefix as the prefix for installing nbextensions (for environments, packaging)"
    ),
    "py" : ({
        "BaseExtensionApp" : {
            "python" : True,
        }}, "Install from a Python package"
    )
})
_base_flags['python'] = _base_flags['py']

_base_aliases = {}
_base_aliases.update(JupyterApp.aliases)


class BaseExtensionApp(JupyterApp):
    """Base nbextension installer app"""
    _log_formatter_cls = LogFormatter
    flags = _base_flags
    aliases = _base_aliases
    version = __version__

    user = Bool(False, config=True, help="Whether to do a user install")
    sys_prefix = Bool(False, config=True, help="Use the sys.prefix as the prefix")
    python = Bool(False, config=True, help="Install from a Python package")

    # Remove for 5.0...
    verbose = Any(None, config=True, help="DEPRECATED: Verbosity level")

    def _verbose_changed(self):
        """Warn about verbosity changes"""
        import warnings
        warnings.warn(
            f"`verbose` traits of `{type(self).__name__}` has been deprecated, "
            f"has no effects and will be removed in notebook 5.0.",
            DeprecationWarning
        )

    def _log_format_default(self):
        """A default format for messages"""
        return "%(message)s"

def _get_config_dir(user=False, sys_prefix=False):
    """Get the location of config files for the current context

    Returns the string to the environment

    Parameters
    ----------

    user : bool [default: False]
        Get the user's .jupyter config directory
    sys_prefix : bool [default: False]
        Get sys.prefix, i.e. ~/.envs/my-env/etc/jupyter
    """
    user = False if sys_prefix else user
    if user and sys_prefix:
        raise ArgumentConflict("Cannot specify more than one of user or sys_prefix")
    if user:
        nbext = jupyter_config_dir()
    elif sys_prefix:
        nbext = ENV_CONFIG_PATH[0]
    else:
        nbext = SYSTEM_CONFIG_PATH[0]
    return nbext

# Constants for pretty print extension listing function.
# Window doesn't support coloring in the commandline
GREEN_ENABLED = '\033[32m enabled \033[0m' if os.name != 'nt' else 'enabled '
RED_DISABLED = '\033[31mdisabled\033[0m' if os.name != 'nt' else 'disabled'
GREEN_OK = '\033[32mOK\033[0m' if os.name != 'nt' else 'ok'
RED_X = '\033[31m X\033[0m' if os.name != 'nt' else ' X'
