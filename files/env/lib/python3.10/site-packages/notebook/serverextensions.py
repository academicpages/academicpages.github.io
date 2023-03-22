"""Utilities for installing server extensions for the notebook"""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

import importlib
import sys

from jupyter_core.paths import jupyter_config_path
from ._version import __version__
from .config_manager import BaseJSONConfigManager
from .extensions import (
    BaseExtensionApp, _get_config_dir, GREEN_ENABLED, RED_DISABLED, GREEN_OK, RED_X
)
from traitlets import Bool
from traitlets.utils.importstring import import_item


# ------------------------------------------------------------------------------
# Public API
# ------------------------------------------------------------------------------

def toggle_serverextension_python(import_name, enabled=None, parent=None,
                                  user=True, sys_prefix=False, logger=None):
    """Toggle a server extension.

    By default, toggles the extension in the system-wide Jupyter configuration
    location (e.g. /usr/local/etc/jupyter).

    Parameters
    ----------

    import_name : str
        Importable Python module (dotted-notation) exposing the magic-named
        `load_jupyter_server_extension` function
    enabled : bool [default: None]
        Toggle state for the extension.  Set to None to toggle, True to enable,
        and False to disable the extension.
    parent : Configurable [default: None]
    user : bool [default: True]
        Toggle in the user's configuration location (e.g. ~/.jupyter).
    sys_prefix : bool [default: False]
        Toggle in the current Python environment's configuration location
        (e.g. ~/.envs/my-env/etc/jupyter). Will override `user`.
    logger : Jupyter logger [optional]
        Logger instance to use
    """
    user = False if sys_prefix else user
    config_dir = _get_config_dir(user=user, sys_prefix=sys_prefix)
    cm = BaseJSONConfigManager(parent=parent, config_dir=config_dir)
    cfg = cm.get("jupyter_notebook_config")
    server_extensions = (
        cfg.setdefault("NotebookApp", {})
        .setdefault("nbserver_extensions", {})
    )

    old_enabled = server_extensions.get(import_name, None)
    new_enabled = enabled if enabled is not None else not old_enabled

    if logger:
        if new_enabled:
            logger.info(f"Enabling: {import_name}")
        else:
            logger.info(f"Disabling: {import_name}")

    server_extensions[import_name] = new_enabled

    if logger:
        logger.info(f"- Writing config: {config_dir}")

    cm.update("jupyter_notebook_config", cfg)

    if new_enabled:
        validate_serverextension(import_name, logger)


def validate_serverextension(import_name, logger=None):
    """Assess the health of an installed server extension

    Returns a list of validation warnings.

    Parameters
    ----------

    import_name : str
        Importable Python module (dotted-notation) exposing the magic-named
        `load_jupyter_server_extension` function
    logger : Jupyter logger [optional]
        Logger instance to use
    """

    warnings = []
    infos = []

    func = None

    if logger:
        logger.info("    - Validating...")

    try:
        mod = importlib.import_module(import_name)
        func = getattr(mod, 'load_jupyter_server_extension', None)
        version = getattr(mod, '__version__', '')
    except Exception:
        logger.warning("Error loading server extension %s", import_name)

    import_msg = "     {} is {} importable?"
    if func is not None:
        infos.append(import_msg.format(GREEN_OK, import_name))
    else:
        warnings.append(import_msg.format(RED_X, import_name))

    post_mortem = "      {} {} {}"
    if logger:
        if warnings:
            [logger.info(info) for info in infos]
            [logger.warn(warning) for warning in warnings]
        else:
            logger.info(post_mortem.format(import_name, version, GREEN_OK))

    return warnings


# ----------------------------------------------------------------------
# Applications
# ----------------------------------------------------------------------

flags = {}
flags.update(BaseExtensionApp.flags)
flags.pop("y", None)
flags.pop("generate-config", None)
flags.update({
    "user" : ({
        "ToggleServerExtensionApp" : {
            "user" : True,
        }}, "Perform the operation for the current user"
    ),
    "system" : ({
        "ToggleServerExtensionApp" : {
            "user" : False,
            "sys_prefix": False,
        }}, "Perform the operation system-wide"
    ),
    "sys-prefix" : ({
        "ToggleServerExtensionApp" : {
            "sys_prefix" : True,
        }}, "Use sys.prefix as the prefix for installing server extensions"
    ),
    "py" : ({
        "ToggleServerExtensionApp" : {
            "python" : True,
        }}, "Install from a Python package"
    ),
})
flags['python'] = flags['py']


class ToggleServerExtensionApp(BaseExtensionApp):
    """A base class for enabling/disabling extensions"""
    name = "jupyter serverextension enable/disable"
    description = "Enable/disable a server extension using frontend configuration files."

    flags = flags

    user = Bool(True, config=True, help="Whether to do a user install")
    sys_prefix = Bool(False, config=True, help="Use the sys.prefix as the prefix")
    python = Bool(False, config=True, help="Install from a Python package")

    def toggle_server_extension(self, import_name):
        """Change the status of a named server extension.

        Uses the value of `self._toggle_value`.

        Parameters
        ---------

        import_name : str
            Importable Python module (dotted-notation) exposing the magic-named
            `load_jupyter_server_extension` function
        """
        toggle_serverextension_python(
            import_name, self._toggle_value, parent=self, user=self.user,
            sys_prefix=self.sys_prefix, logger=self.log)

    def toggle_server_extension_python(self, package):
        """Change the status of some server extensions in a Python package.

        Uses the value of `self._toggle_value`.

        Parameters
        ---------

        package : str
            Importable Python module exposing the
            magic-named `_jupyter_server_extension_paths` function
        """
        m, server_exts = _get_server_extension_metadata(package)
        for server_ext in server_exts:
            module = server_ext['module']
            self.toggle_server_extension(module)

    def start(self):
        """Perform the App's actions as configured"""
        if not self.extra_args:
            sys.exit('Please specify a server extension/package to enable or disable')
        for arg in self.extra_args:
            if self.python:
                self.toggle_server_extension_python(arg)
            else:
                self.toggle_server_extension(arg)


class EnableServerExtensionApp(ToggleServerExtensionApp):
    """An App that enables (and validates) Server Extensions"""
    name = "jupyter serverextension enable"
    description = """
    Enable a serverextension in configuration.

    Usage
        jupyter serverextension enable [--system|--sys-prefix]
    """
    _toggle_value = True


class DisableServerExtensionApp(ToggleServerExtensionApp):
    """An App that disables Server Extensions"""
    name = "jupyter serverextension disable"
    description = """
    Disable a serverextension in configuration.

    Usage
        jupyter serverextension disable [--system|--sys-prefix]
    """
    _toggle_value = False


class ListServerExtensionsApp(BaseExtensionApp):
    """An App that lists (and validates) Server Extensions"""
    name = "jupyter serverextension list"
    version = __version__
    description = "List all server extensions known by the configuration system"

    def list_server_extensions(self):
        """List all enabled and disabled server extensions, by config path

        Enabled extensions are validated, potentially generating warnings.
        """
        config_dirs = jupyter_config_path()
        for config_dir in config_dirs:
            cm = BaseJSONConfigManager(parent=self, config_dir=config_dir)
            data = cm.get("jupyter_notebook_config")
            server_extensions = (
                data.setdefault("NotebookApp", {})
                .setdefault("nbserver_extensions", {})
            )
            if server_extensions:
                print(f'config dir: {config_dir}')
            for import_name, enabled in server_extensions.items():
                print(f'    {import_name} {GREEN_ENABLED if enabled else RED_DISABLED}')
                validate_serverextension(import_name, self.log)

    def start(self):
        """Perform the App's actions as configured"""
        self.list_server_extensions()


_examples = """
jupyter serverextension list                        # list all configured server extensions
jupyter serverextension enable --py <packagename>   # enable all server extensions in a Python package
jupyter serverextension disable --py <packagename>  # disable all server extensions in a Python package
"""


class ServerExtensionApp(BaseExtensionApp):
    """Root level server extension app"""
    name = "jupyter serverextension"
    version = __version__
    description = "Work with Jupyter server extensions"
    examples = _examples

    subcommands = dict(
        enable=(EnableServerExtensionApp, "Enable a server extension"),
        disable=(DisableServerExtensionApp, "Disable a server extension"),
        list=(ListServerExtensionsApp, "List server extensions")
    )

    def start(self):
        """Perform the App's actions as configured"""
        super().start()

        # The above should have called a subcommand and raised NoStart; if we
        # get here, it didn't, so we should self.log.info a message.
        subcmds = ", ".join(sorted(self.subcommands))
        sys.exit(f"Please supply at least one subcommand: {subcmds}")


main = ServerExtensionApp.launch_instance

# ------------------------------------------------------------------------------
# Private API
# ------------------------------------------------------------------------------


def _get_server_extension_metadata(module):
    """Load server extension metadata from a module.

    Returns a tuple of (
        the package as loaded
        a list of server extension specs: [
            {
                "module": "mockextension"
            }
        ]
    )

    Parameters
    ----------

    module : str
        Importable Python module exposing the
        magic-named `_jupyter_server_extension_paths` function
    """
    m = import_item(module)
    if not hasattr(m, '_jupyter_server_extension_paths'):
        raise KeyError(f'The Python module {module} does not include any valid server extensions')
    return m, m._jupyter_server_extension_paths()

if __name__ == '__main__':
    main()
