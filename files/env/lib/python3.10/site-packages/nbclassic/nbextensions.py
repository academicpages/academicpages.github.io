"""Utilities for installing Javascript extensions for the notebook"""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

import os
import shutil
import sys
import tarfile
import zipfile
from os.path import basename, join as pjoin, normpath

from urllib.parse import urlparse
from urllib.request import urlretrieve
from jupyter_core.paths import (
    jupyter_data_dir, jupyter_config_path, jupyter_path,
    SYSTEM_JUPYTER_PATH, ENV_JUPYTER_PATH,
)
from jupyter_core.utils import ensure_dir_exists
from ipython_genutils.py3compat import string_types, cast_unicode_py2
from ipython_genutils.tempdir import TemporaryDirectory
from ._version import __version__
from .config_manager import BaseJSONConfigManager

from traitlets.utils.importstring import import_item

DEPRECATED_ARGUMENT = object()

NBCONFIG_SECTIONS = ['common', 'notebook', 'tree', 'edit', 'terminal']


#------------------------------------------------------------------------------
# Public API
#------------------------------------------------------------------------------

def check_nbextension(files, user=False, prefix=None, nbextensions_dir=None, sys_prefix=False):
    """Check whether nbextension files have been installed

    Returns True if all files are found, False if any are missing.

    Parameters
    ----------

    files : list(paths)
        a list of relative paths within nbextensions.
    user : bool [default: False]
        Whether to check the user's .jupyter/nbextensions directory.
        Otherwise check a system-wide install (e.g. /usr/local/share/jupyter/nbextensions).
    prefix : str [optional]
        Specify install prefix, if it should differ from default (e.g. /usr/local).
        Will check prefix/share/jupyter/nbextensions
    nbextensions_dir : str [optional]
        Specify absolute path of nbextensions directory explicitly.
    sys_prefix : bool [default: False]
        Install into the sys.prefix, i.e. environment
    """
    nbext = _get_nbextension_dir(user=user, sys_prefix=sys_prefix, prefix=prefix, nbextensions_dir=nbextensions_dir)
    # make sure nbextensions dir exists
    if not os.path.exists(nbext):
        return False

    if isinstance(files, string_types):
        # one file given, turn it into a list
        files = [files]

    return all(os.path.exists(pjoin(nbext, f)) for f in files)


def install_nbextension(path, overwrite=False, symlink=False,
                        user=False, prefix=None, nbextensions_dir=None,
                        destination=None, verbose=DEPRECATED_ARGUMENT,
                        logger=None, sys_prefix=False
                        ):
    """Install a Javascript extension for the notebook

    Stages files and/or directories into the nbextensions directory.
    By default, this compares modification time, and only stages files that need updating.
    If `overwrite` is specified, matching files are purged before proceeding.

    Parameters
    ----------

    path : path to file, directory, zip or tarball archive, or URL to install
        By default, the file will be installed with its base name, so '/path/to/foo'
        will install to 'nbextensions/foo'. See the destination argument below to change this.
        Archives (zip or tarballs) will be extracted into the nbextensions directory.
    overwrite : bool [default: False]
        If True, always install the files, regardless of what may already be installed.
    symlink : bool [default: False]
        If True, create a symlink in nbextensions, rather than copying files.
        Not allowed with URLs or archives. Windows support for symlinks requires
        Vista or above, Python 3, and a permission bit which only admin users
        have by default, so don't rely on it.
    user : bool [default: False]
        Whether to install to the user's nbextensions directory.
        Otherwise do a system-wide install (e.g. /usr/local/share/jupyter/nbextensions).
    prefix : str [optional]
        Specify install prefix, if it should differ from default (e.g. /usr/local).
        Will install to ``<prefix>/share/jupyter/nbextensions``
    nbextensions_dir : str [optional]
        Specify absolute path of nbextensions directory explicitly.
    destination : str [optional]
        name the nbextension is installed to.  For example, if destination is 'foo', then
        the source file will be installed to 'nbextensions/foo', regardless of the source name.
        This cannot be specified if an archive is given as the source.
    logger : Jupyter logger [optional]
        Logger instance to use
    """
    if verbose != DEPRECATED_ARGUMENT:
        import warnings
        warnings.warn("`install_nbextension`'s `verbose` parameter is deprecated, it will have no effects and will be removed in Notebook 5.0", DeprecationWarning)

    # the actual path to which we eventually installed
    full_dest = None

    nbext = _get_nbextension_dir(user=user, sys_prefix=sys_prefix, prefix=prefix, nbextensions_dir=nbextensions_dir)
    # make sure nbextensions dir exists
    ensure_dir_exists(nbext)

    # forcing symlink parameter to False if os.symlink does not exist (e.g., on Windows machines running python 2)
    if not hasattr(os, 'symlink'):
        symlink = False

    if isinstance(path, (list, tuple)):
        raise TypeError("path must be a string pointing to a single extension to install; call this function multiple times to install multiple extensions")

    path = cast_unicode_py2(path)

    if path.startswith(('https://', 'http://')):
        if symlink:
            raise ValueError("Cannot symlink from URLs")
        # Given a URL, download it
        with TemporaryDirectory() as td:
            filename = urlparse(path).path.split('/')[-1]
            local_path = os.path.join(td, filename)
            if logger:
                logger.info(f"Downloading: {path} -> {local_path}")
            urlretrieve(path, local_path)
            # now install from the local copy
            full_dest = install_nbextension(local_path, overwrite=overwrite, symlink=symlink,
                nbextensions_dir=nbext, destination=destination, logger=logger)
    elif path.endswith('.zip') or _safe_is_tarfile(path):
        if symlink:
            raise ValueError("Cannot symlink from archives")
        if destination:
            raise ValueError("Cannot give destination for archives")
        if logger:
            logger.info(f"Extracting: {path} -> {nbext}")

        if path.endswith('.zip'):
            archive = zipfile.ZipFile(path)
        elif _safe_is_tarfile(path):
            archive = tarfile.open(path)
        archive.extractall(nbext)
        archive.close()
        # TODO: what to do here
        full_dest = None
    else:
        if not destination:
            destination = basename(normpath(path))
        destination = cast_unicode_py2(destination)
        full_dest = normpath(pjoin(nbext, destination))
        if overwrite and os.path.lexists(full_dest):
            if logger:
                logger.info(f"Removing: {full_dest}")
            if os.path.isdir(full_dest) and not os.path.islink(full_dest):
                shutil.rmtree(full_dest)
            else:
                os.remove(full_dest)

        if symlink:
            path = os.path.abspath(path)
            if not os.path.exists(full_dest):
                if logger:
                    logger.info(f"Symlinking: {full_dest} -> {path}")
                os.symlink(path, full_dest)
        elif os.path.isdir(path):
            path = pjoin(os.path.abspath(path), '') # end in path separator
            for parent, dirs, files in os.walk(path):
                dest_dir = pjoin(full_dest, parent[len(path):])
                if not os.path.exists(dest_dir):
                    if logger:
                        logger.info(f"Making directory: {dest_dir}")
                    os.makedirs(dest_dir)
                for file_name in files:
                    src = pjoin(parent, file_name)
                    dest_file = pjoin(dest_dir, file_name)
                    _maybe_copy(src, dest_file, logger=logger)
        else:
            src = path
            _maybe_copy(src, full_dest, logger=logger)

    return full_dest


def install_nbextension_python(module, overwrite=False, symlink=False,
                        user=False, sys_prefix=False, prefix=None, nbextensions_dir=None, logger=None):
    """Install an nbextension bundled in a Python package.

    Returns a list of installed/updated directories.

    See install_nbextension for parameter information."""
    m, nbexts = _get_nbextension_metadata(module)
    base_path = os.path.split(m.__file__)[0]

    full_dests = []

    for nbext in nbexts:
        src = os.path.join(base_path, nbext['src'])
        dest = nbext['dest']

        if logger:
            logger.info(f"Installing {src} -> {dest}")
        full_dest = install_nbextension(
            src, overwrite=overwrite, symlink=symlink,
            user=user, sys_prefix=sys_prefix, prefix=prefix, nbextensions_dir=nbextensions_dir,
            destination=dest, logger=logger
            )
        validate_nbextension_python(nbext, full_dest, logger)
        full_dests.append(full_dest)

    return full_dests


def uninstall_nbextension(dest, require=None, user=False, sys_prefix=False, prefix=None,
                          nbextensions_dir=None, logger=None):
    """Uninstall a Javascript extension of the notebook

    Removes staged files and/or directories in the nbextensions directory and
    removes the extension from the frontend config.

    Parameters
    ----------

    dest : str
        path to file, directory, zip or tarball archive, or URL to install
        name the nbextension is installed to.  For example, if destination is 'foo', then
        the source file will be installed to 'nbextensions/foo', regardless of the source name.
        This cannot be specified if an archive is given as the source.
    require : str [optional]
        require.js path used to load the extension.
        If specified, frontend config loading extension will be removed.
    user : bool [default: False]
        Whether to install to the user's nbextensions directory.
        Otherwise do a system-wide install (e.g. /usr/local/share/jupyter/nbextensions).
    prefix : str [optional]
        Specify install prefix, if it should differ from default (e.g. /usr/local).
        Will install to ``<prefix>/share/jupyter/nbextensions``
    nbextensions_dir : str [optional]
        Specify absolute path of nbextensions directory explicitly.
    logger : Jupyter logger [optional]
        Logger instance to use
    """
    nbext = _get_nbextension_dir(user=user, sys_prefix=sys_prefix, prefix=prefix, nbextensions_dir=nbextensions_dir)
    dest = cast_unicode_py2(dest)
    full_dest = pjoin(nbext, dest)
    if os.path.lexists(full_dest):
        if logger:
            logger.info(f"Removing: {full_dest}")
        if os.path.isdir(full_dest) and not os.path.islink(full_dest):
            shutil.rmtree(full_dest)
        else:
            os.remove(full_dest)

    # Look through all of the config sections making sure that the nbextension
    # doesn't exist.
    config_dir = os.path.join(_get_config_dir(user=user, sys_prefix=sys_prefix), 'nbconfig')
    cm = BaseJSONConfigManager(config_dir=config_dir)
    if require:
        for section in NBCONFIG_SECTIONS:
            cm.update(section, {"load_extensions": {require: None}})


def _find_uninstall_nbextension(filename, logger=None):
    """Remove nbextension files from the first location they are found.

    Returns True if files were removed, False otherwise.
    """
    filename = cast_unicode_py2(filename)
    for nbext in jupyter_path('nbextensions'):
        path = pjoin(nbext, filename)
        if os.path.lexists(path):
            if logger:
                logger.info(f"Removing: {path}")
            if os.path.isdir(path) and not os.path.islink(path):
                shutil.rmtree(path)
            else:
                os.remove(path)
            return True

    return False


def uninstall_nbextension_python(module,
                        user=False, sys_prefix=False, prefix=None, nbextensions_dir=None,
                        logger=None):
    """Uninstall an nbextension bundled in a Python package.

    See parameters of `install_nbextension_python`
    """
    m, nbexts = _get_nbextension_metadata(module)
    for nbext in nbexts:
        dest = nbext['dest']
        require = nbext['require']
        if logger:
            logger.info(f"Uninstalling {dest} {require}")
        uninstall_nbextension(dest, require, user=user, sys_prefix=sys_prefix,
            prefix=prefix, nbextensions_dir=nbextensions_dir, logger=logger)


def _set_nbextension_state(section, require, state,
                           user=True, sys_prefix=False, logger=None):
    """Set whether the section's frontend should require the named nbextension

    Returns True if the final state is the one requested.

    Parameters
    ----------
    section : string
        The section of the server to change, one of NBCONFIG_SECTIONS
    require : string
        An importable AMD module inside the nbextensions static path
    state : bool
        The state in which to leave the extension
    user : bool [default: True]
        Whether to update the user's .jupyter/nbextensions directory
    sys_prefix : bool [default: False]
        Whether to update the sys.prefix, i.e. environment. Will override
        `user`.
    logger : Jupyter logger [optional]
        Logger instance to use
    """
    user = False if sys_prefix else user
    config_dir = os.path.join(
        _get_config_dir(user=user, sys_prefix=sys_prefix), 'nbconfig')
    cm = BaseJSONConfigManager(config_dir=config_dir)
    if logger:
        logger.info(f"{'Enabling' if state else 'Disabling'} {section} extension {require}...")
    cm.update(section, {"load_extensions": {require: state}})

    validate_nbextension(require, logger=logger)

    return cm.get(section).get(require) == state


def _set_nbextension_state_python(state, module, user, sys_prefix,
                                  logger=None):
    """Enable or disable some nbextensions stored in a Python package

    Returns a list of whether the state was achieved (i.e. changed, or was
    already right)

    Parameters
    ----------

    state : Bool
        Whether the extensions should be enabled
    module : str
        Importable Python module exposing the
        magic-named `_jupyter_nbextension_paths` function
    user : bool
        Whether to enable in the user's nbextensions directory.
    sys_prefix : bool
        Enable/disable in the sys.prefix, i.e. environment
    logger : Jupyter logger [optional]
        Logger instance to use
    """
    m, nbexts = _get_nbextension_metadata(module)
    return [_set_nbextension_state(section=nbext["section"],
                                   require=nbext["require"],
                                   state=state,
                                   user=user, sys_prefix=sys_prefix,
                                   logger=logger)
            for nbext in nbexts]


def enable_nbextension(section, require, user=True, sys_prefix=False,
                       logger=None):
    """Enable a named nbextension

    Returns True if the final state is the one requested.

    Parameters
    ----------

    section : string
        The section of the server to change, one of NBCONFIG_SECTIONS
    require : string
        An importable AMD module inside the nbextensions static path
    user : bool [default: True]
        Whether to enable in the user's nbextensions directory.
    sys_prefix : bool [default: False]
        Whether to enable in the sys.prefix, i.e. environment. Will override
        `user`
    logger : Jupyter logger [optional]
        Logger instance to use
    """
    return _set_nbextension_state(section=section, require=require,
                                  state=True,
                                  user=user, sys_prefix=sys_prefix,
                                  logger=logger)


def disable_nbextension(section, require, user=True, sys_prefix=False,
                        logger=None):
    """Disable a named nbextension

    Returns True if the final state is the one requested.

    Parameters
    ----------

    section : string
        The section of the server to change, one of NBCONFIG_SECTIONS
    require : string
        An importable AMD module inside the nbextensions static path
    user : bool [default: True]
        Whether to enable in the user's nbextensions directory.
    sys_prefix : bool [default: False]
        Whether to enable in the sys.prefix, i.e. environment. Will override
        `user`.
    logger : Jupyter logger [optional]
        Logger instance to use
    """
    return _set_nbextension_state(section=section, require=require,
                                  state=False,
                                  user=user, sys_prefix=sys_prefix,
                                  logger=logger)


def _find_disable_nbextension(section, require, logger=None):
    """Disable an nbextension from the first config location where it is enabled.

    Returns True if it changed any config, False otherwise.
    """
    for config_dir in jupyter_config_path():
        cm = BaseJSONConfigManager(
            config_dir=os.path.join(config_dir, 'nbconfig'))
        d = cm.get(section)
        if d.get('load_extensions', {}).get(require, None):
            if logger:
                logger.info("Disabling %s extension in %s", require, config_dir)
            cm.update(section, {'load_extensions': {require: None}})
            return True

    return False


def enable_nbextension_python(module, user=True, sys_prefix=False,
                              logger=None):
    """Enable some nbextensions associated with a Python module.

    Returns a list of whether the state was achieved (i.e. changed, or was
    already right)

    Parameters
    ----------

    module : str
        Importable Python module exposing the
        magic-named `_jupyter_nbextension_paths` function
    user : bool [default: True]
        Whether to enable in the user's nbextensions directory.
    sys_prefix : bool [default: False]
        Whether to enable in the sys.prefix, i.e. environment. Will override
        `user`
    logger : Jupyter logger [optional]
        Logger instance to use
    """
    return _set_nbextension_state_python(True, module, user, sys_prefix,
                                         logger=logger)


def disable_nbextension_python(module, user=True, sys_prefix=False,
                               logger=None):
    """Disable some nbextensions associated with a Python module.

    Returns True if the final state is the one requested.

    Parameters
    ----------

    module : str
        Importable Python module exposing the
        magic-named `_jupyter_nbextension_paths` function
    user : bool [default: True]
        Whether to enable in the user's nbextensions directory.
    sys_prefix : bool [default: False]
        Whether to enable in the sys.prefix, i.e. environment
    logger : Jupyter logger [optional]
        Logger instance to use
    """
    return _set_nbextension_state_python(False, module, user, sys_prefix,
                                         logger=logger)


def validate_nbextension(require, logger=None):
    """Validate a named nbextension.

    Looks across all of the nbextension directories.

    Returns a list of warnings.

    require : str
        require.js path used to load the extension
    logger : Jupyter logger [optional]
        Logger instance to use
    """
    warnings = []
    infos = []

    js_exists = False
    for exts in jupyter_path('nbextensions'):
        # Does the Javascript entrypoint actually exist on disk?
        js = f"{os.path.join(exts, *require.split('/'))}.js"
        js_exists = os.path.exists(js)
        if js_exists:
            break

    require_tmpl = "        - require? {} {}"
    if js_exists:
        infos.append(require_tmpl.format(GREEN_OK, require))
    else:
        warnings.append(require_tmpl.format(RED_X, require))

    if logger:
        if warnings:
            logger.warning("      - Validating: problems found:")
            for msg in warnings:
                logger.warning(msg)
            for msg in infos:
                logger.info(msg)
        else:
            logger.info(f"      - Validating: {GREEN_OK}")

    return warnings


def validate_nbextension_python(spec, full_dest, logger=None):
    """Assess the health of an installed nbextension

    Returns a list of warnings.

    Parameters
    ----------

    spec : dict
        A single entry of _jupyter_nbextension_paths():
            [{
                'section': 'notebook',
                'src': 'mockextension',
                'dest': '_mockdestination',
                'require': '_mockdestination/index'
            }]
    full_dest : str
        The on-disk location of the installed nbextension: this should end
        with `nbextensions/<dest>`
    logger : Jupyter logger [optional]
        Logger instance to use
    """
    infos = []
    warnings = []

    section = spec.get("section", None)
    if section in NBCONFIG_SECTIONS:
        infos.append(f"  {GREEN_OK} section: {section}")
    else:
        warnings.append(f"  {RED_X}  section: {section}")

    require = spec.get("require", None)
    if require is not None:
        require_path = os.path.join(
            full_dest[0:-len(spec["dest"])],
            f"{require}.js")
        if os.path.exists(require_path):
            infos.append(f"  {GREEN_OK} require: {require_path}")
        else:
            warnings.append(f"  {RED_X}  require: {require_path}")

    if logger:
        if warnings:
            logger.warning("- Validating: problems found:")
            for msg in warnings:
                logger.warning(msg)
            for msg in infos:
                logger.info(msg)
            logger.warning(f"Full spec: {spec}")
        else:
            logger.info(f"- Validating: {GREEN_OK}")

    return warnings


#----------------------------------------------------------------------
# Applications
#----------------------------------------------------------------------

from .extensions import (
    BaseExtensionApp, _get_config_dir, GREEN_ENABLED, RED_DISABLED, GREEN_OK, RED_X,
    ArgumentConflict, _base_aliases, _base_flags,
)
from traitlets import Bool, Unicode

flags = {}
flags.update(_base_flags)
flags.update({
    "overwrite" : ({
        "InstallNBExtensionApp" : {
            "overwrite" : True,
        }}, "Force overwrite of existing files"
    ),
    "symlink" : ({
        "InstallNBExtensionApp" : {
            "symlink" : True,
        }}, "Create symlink instead of copying files"
    ),
})

flags['s'] = flags['symlink']

aliases = {}
aliases.update(_base_aliases)
aliases.update({
    "prefix" : "InstallNBExtensionApp.prefix",
    "nbextensions" : "InstallNBExtensionApp.nbextensions_dir",
    "destination" : "InstallNBExtensionApp.destination",
})

class InstallNBExtensionApp(BaseExtensionApp):
    """Entry point for installing notebook extensions"""
    description = """Install Jupyter notebook extensions

    Usage

        jupyter nbclassic-extension install path|url [--user|--sys-prefix]

    This copies a file or a folder into the jupyter nbclassic-extensions directory.
    If a URL is given, it will be downloaded.
    If an archive is given, it will be extracted into nbextensions.
    If the requested files are already up to date, no action is taken
    unless --overwrite is specified.
    """

    examples = """
    jupyter nbclassic-extension install /path/to/myextension
    """
    aliases = aliases
    flags = flags

    overwrite = Bool(False, config=True, help="Force overwrite of existing files")
    symlink = Bool(False, config=True, help="Create symlinks instead of copying files")

    prefix = Unicode('', config=True, help="Installation prefix")
    nbextensions_dir = Unicode('', config=True,
           help="Full path to nbextensions dir (probably use prefix or user)")
    destination = Unicode('', config=True, help="Destination for the copy or symlink")

    def _config_file_name_default(self):
        """The default config file name."""
        return 'jupyter_notebook_config'

    def install_extensions(self):
        """Perform the installation of nbextension(s)"""
        if len(self.extra_args)>1:
            raise ValueError("Only one nbextension allowed at a time. "
                         "Call multiple times to install multiple extensions.")

        if self.python:
            install = install_nbextension_python
            kwargs = {}
        else:
            install = install_nbextension
            kwargs = {'destination': self.destination}

        full_dests = install(self.extra_args[0],
                             overwrite=self.overwrite,
                             symlink=self.symlink,
                             user=self.user,
                             sys_prefix=self.sys_prefix,
                             prefix=self.prefix,
                             nbextensions_dir=self.nbextensions_dir,
                             logger=self.log,
                             **kwargs
                            )

        if full_dests:
            self.log.info(
                f"\nTo initialize this nbextension in the browser every time"
                f" the notebook (or other app) loads:\n\n"
                f"      jupyter nbclassic-extension enable {self.extra_args[0] if self.python else '<the entry point>'}"
                f"{' --user' if self.user else ''}"
                f"{' --py' if self.python else ''}"
                f"{' --sys-prefix' if self.sys_prefix else ''}\n"
            )

    def start(self):
        """Perform the App's function as configured"""
        if not self.extra_args:
            sys.exit('Please specify an nbextension to install')
        else:
            try:
                self.install_extensions()
            except ArgumentConflict as e:
                sys.exit(str(e))


class UninstallNBExtensionApp(BaseExtensionApp):
    """Entry point for uninstalling notebook extensions"""
    version = __version__
    description = """Uninstall Jupyter notebook extensions

    Usage

        jupyter nbclassic-extension uninstall path/url path/url/entrypoint
        jupyter nbclassic-extension uninstall --py pythonPackageName

    This uninstalls an nbextension. By default, it uninstalls from the
    first directory on the search path where it finds the extension, but you can
    uninstall from a specific location using the --user, --sys-prefix or
    --system flags, or the --prefix option.

    If you specify the --require option, the named extension will be disabled,
    e.g.::

        jupyter nbclassic-extension uninstall myext --require myext/main

    If you use the --py or --python flag, the name should be a Python module.
    It will uninstall nbextensions listed in that module, but not the module
    itself (which you should uninstall using a package manager such as pip).
    """

    examples = """
    jupyter nbclassic-extension uninstall dest/dir dest/dir/extensionjs
    jupyter nbclassic-extension uninstall --py extensionPyPackage
    """

    aliases = {
        "prefix" : "UninstallNBExtensionApp.prefix",
        "nbextensions" : "UninstallNBExtensionApp.nbextensions_dir",
        "require": "UninstallNBExtensionApp.require",
    }
    flags = BaseExtensionApp.flags.copy()
    flags['system'] = ({'UninstallNBExtensionApp': {'system': True}},
        "Uninstall specifically from systemwide installation directory")

    prefix = Unicode('', config=True,
        help="Installation prefix. Overrides --user, --sys-prefix and --system"
    )
    nbextensions_dir = Unicode('', config=True,
        help="Full path to nbextensions dir (probably use prefix or user)"
    )
    require = Unicode('', config=True, help="require.js module to disable loading")
    system = Bool(False, config=True,
        help="Uninstall specifically from systemwide installation directory"
    )

    def _config_file_name_default(self):
        """The default config file name."""
        return 'jupyter_notebook_config'

    def uninstall_extension(self):
        """Uninstall an nbextension from a specific location"""
        kwargs = {
            'user': self.user,
            'sys_prefix': self.sys_prefix,
            'prefix': self.prefix,
            'nbextensions_dir': self.nbextensions_dir,
            'logger': self.log
        }

        if self.python:
            uninstall_nbextension_python(self.extra_args[0], **kwargs)
        else:
            if self.require:
                kwargs['require'] = self.require
            uninstall_nbextension(self.extra_args[0], **kwargs)

    def find_uninstall_extension(self):
        """Uninstall an nbextension from an unspecified location"""
        name = self.extra_args[0]
        if self.python:
            _, nbexts = _get_nbextension_metadata(name)
            changed = False
            for nbext in nbexts:
                if _find_uninstall_nbextension(nbext['dest'], logger=self.log):
                    changed = True

                # Also disable it in config.
                for section in NBCONFIG_SECTIONS:
                    _find_disable_nbextension(section, nbext['require'],
                                              logger=self.log)

        else:
            changed = _find_uninstall_nbextension(name, logger=self.log)

        if not changed:
            print(f"No installed extension {name!r} found.")

        if self.require:
            for section in NBCONFIG_SECTIONS:
                _find_disable_nbextension(section, self.require,
                                          logger=self.log)

    def start(self):
        if not self.extra_args:
            sys.exit('Please specify an nbextension to uninstall')
        elif len(self.extra_args) > 1:
            sys.exit("Only one nbextension allowed at a time. "
                     "Call multiple times to uninstall multiple extensions.")
        elif (self.user or self.sys_prefix or self.system or self.prefix
              or self.nbextensions_dir):
            # The user has specified a location from which to uninstall.
            try:
                self.uninstall_extension()
            except ArgumentConflict as e:
                sys.exit(str(e))
        else:
            # Uninstall wherever it is.
            self.find_uninstall_extension()


class ToggleNBExtensionApp(BaseExtensionApp):
    """A base class for apps that enable/disable extensions"""
    name = "jupyter nbclassic-extension enable/disable"
    version = __version__
    description = "Enable/disable an nbextension in configuration."

    section = Unicode('notebook', config=True,
          help="""Which config section to add the extension to, 'common' will affect all pages."""
    )
    user = Bool(True, config=True, help="Apply the configuration only for the current user (default)")

    aliases = {'section': 'ToggleNBExtensionApp.section'}

    _toggle_value = None

    def _config_file_name_default(self):
        """The default config file name."""
        return 'jupyter_notebook_config'

    def toggle_nbextension_python(self, module):
        """Toggle some extensions in an importable Python module.

        Returns a list of booleans indicating whether the state was changed as
        requested.

        Parameters
        ----------
        module : str
            Importable Python module exposing the
            magic-named `_jupyter_nbextension_paths` function
        """
        toggle = (enable_nbextension_python if self._toggle_value
                  else disable_nbextension_python)
        return toggle(module,
                      user=self.user,
                      sys_prefix=self.sys_prefix,
                      logger=self.log)

    def toggle_nbextension(self, require):
        """Toggle some a named nbextension by require-able AMD module.

        Returns whether the state was changed as requested.

        Parameters
        ----------
        require : str
            require.js path used to load the nbextension
        """
        toggle = (enable_nbextension if self._toggle_value
                  else disable_nbextension)
        return toggle(self.section, require,
                      user=self.user, sys_prefix=self.sys_prefix,
                      logger=self.log)

    def start(self):
        if not self.extra_args:
            sys.exit('Please specify an nbextension/package to enable or disable')
        elif len(self.extra_args) > 1:
            sys.exit('Please specify one nbextension/package at a time')
        if self.python:
            self.toggle_nbextension_python(self.extra_args[0])
        else:
            self.toggle_nbextension(self.extra_args[0])


class EnableNBExtensionApp(ToggleNBExtensionApp):
    """An App that enables nbextensions"""
    name = "jupyter nbclassic-extension enable"
    description = """
    Enable an nbextension in frontend configuration.

    Usage
        jupyter nbclassic-extension enable [--system|--sys-prefix]
    """
    _toggle_value = True


class DisableNBExtensionApp(ToggleNBExtensionApp):
    """An App that disables nbextensions"""
    name = "jupyter nbclassic-extension disable"
    description = """
    Disable an nbextension in frontend configuration.

    Usage
        jupyter nbclassic-extension disable [--system|--sys-prefix]
    """
    _toggle_value = None


class ListNBExtensionsApp(BaseExtensionApp):
    """An App that lists and validates nbextensions"""
    name = "jupyter nbclassic-extension list"
    version = __version__
    description = "List all nbextensions known by the configuration system"

    def list_nbextensions(self):
        """List all the nbextensions"""
        config_dirs = [os.path.join(p, 'nbconfig') for p in jupyter_config_path()]

        print("Known nbextensions:")

        for config_dir in config_dirs:
            head = f'  config dir: {config_dir}'
            head_shown = False

            cm = BaseJSONConfigManager(parent=self, config_dir=config_dir)
            for section in NBCONFIG_SECTIONS:
                data = cm.get(section)
                if 'load_extensions' in data:
                    if not head_shown:
                        # only show heading if there is an nbextension here
                        print(head)
                        head_shown = True
                    print(f'    {section} section')

                    for require, enabled in data['load_extensions'].items():
                        print(f'      {require} {GREEN_ENABLED if enabled else RED_DISABLED}')
                        if enabled:
                            validate_nbextension(require, logger=self.log)

    def start(self):
        """Perform the App's functions as configured"""
        self.list_nbextensions()


_examples = """
jupyter nbclassic-extension list                          # list all configured nbextensions
jupyter nbclassic-extension install --py <packagename>    # install an nbextension from a Python package
jupyter nbclassic-extension enable --py <packagename>     # enable all nbextensions in a Python package
jupyter nbclassic-extension disable --py <packagename>    # disable all nbextensions in a Python package
jupyter nbclassic-extension uninstall --py <packagename>  # uninstall an nbextension in a Python package
"""

class NBExtensionApp(BaseExtensionApp):
    """Base jupyter nbclassic-extension command entry point"""
    name = "jupyter nbclassic-extension"
    version = __version__
    description = "Work with Jupyter notebook extensions"
    examples = _examples

    subcommands = dict(
        install=(InstallNBExtensionApp,"Install an nbextension"),
        enable=(EnableNBExtensionApp, "Enable an nbextension"),
        disable=(DisableNBExtensionApp, "Disable an nbextension"),
        uninstall=(UninstallNBExtensionApp, "Uninstall an nbextension"),
        list=(ListNBExtensionsApp, "List nbextensions")
    )

    def start(self):
        """Perform the App's functions as configured"""
        super().start()

        # The above should have called a subcommand and raised NoStart; if we
        # get here, it didn't, so we should self.log.info a message.
        subcmds = ", ".join(sorted(self.subcommands))
        sys.exit(f"Please supply at least one subcommand: {subcmds}")

main = NBExtensionApp.launch_instance

#------------------------------------------------------------------------------
# Private API
#------------------------------------------------------------------------------


def _should_copy(src, dest, logger=None):
    """Should a file be copied, if it doesn't exist, or is newer?

    Returns whether the file needs to be updated.

    Parameters
    ----------

    src : string
        A path that should exist from which to copy a file
    src : string
        A path that might exist to which to copy a file
    logger : Jupyter logger [optional]
        Logger instance to use
    """
    if not os.path.exists(dest):
        return True
    if os.stat(src).st_mtime - os.stat(dest).st_mtime > 1e-6:
        # we add a fudge factor to work around a bug in python 2.x
        # that was fixed in python 3.x: https://bugs.python.org/issue12904
        if logger:
            logger.warn(f"Out of date: {dest}")
        return True
    if logger:
        logger.info(f"Up to date: {dest}")
    return False


def _maybe_copy(src, dest, logger=None):
    """Copy a file if it needs updating.

    Parameters
    ----------

    src : string
        A path that should exist from which to copy a file
    src : string
        A path that might exist to which to copy a file
    logger : Jupyter logger [optional]
        Logger instance to use
    """
    if _should_copy(src, dest, logger=logger):
        if logger:
            logger.info(f"Copying: {src} -> {dest}")
        shutil.copy2(src, dest)


def _safe_is_tarfile(path):
    """Safe version of is_tarfile, return False on IOError.

    Returns whether the file exists and is a tarfile.

    Parameters
    ----------

    path : string
        A path that might not exist and or be a tarfile
    """
    try:
        return tarfile.is_tarfile(path)
    except OSError:
        return False


def _get_nbextension_dir(user=False, sys_prefix=False, prefix=None, nbextensions_dir=None):
    """Return the nbextension directory specified

    Parameters
    ----------

    user : bool [default: False]
        Get the user's .jupyter/nbextensions directory
    sys_prefix : bool [default: False]
        Get sys.prefix, i.e. ~/.envs/my-env/share/jupyter/nbextensions
    prefix : str [optional]
        Get custom prefix
    nbextensions_dir : str [optional]
        Get what you put in
    """
    conflicting = [
        ('user', user),
        ('prefix', prefix),
        ('nbextensions_dir', nbextensions_dir),
        ('sys_prefix', sys_prefix),
    ]
    conflicting_set = [f'{n}={v!r}' for n, v in conflicting if v]
    if len(conflicting_set) > 1:
        raise ArgumentConflict(
            f"cannot specify more than one of user, sys_prefix, prefix, or nbextensions_dir, "
            f"but got: {', '.join(conflicting_set)}"
        )
    if user:
        nbext = pjoin(jupyter_data_dir(), 'nbextensions')
    elif sys_prefix:
        nbext = pjoin(ENV_JUPYTER_PATH[0], 'nbextensions')
    elif prefix:
        nbext = pjoin(prefix, 'share', 'jupyter', 'nbextensions')
    elif nbextensions_dir:
        nbext = nbextensions_dir
    else:
        nbext = pjoin(SYSTEM_JUPYTER_PATH[0], 'nbextensions')
    return nbext


def _get_nbextension_metadata(module):
    """Get the list of nbextension paths associated with a Python module.

    Returns a tuple of (the module,             [{
        'section': 'notebook',
        'src': 'mockextension',
        'dest': '_mockdestination',
        'require': '_mockdestination/index'
    }])

    Parameters
    ----------

    module : str
        Importable Python module exposing the
        magic-named `_jupyter_nbextension_paths` function
    """
    m = import_item(module)
    if not hasattr(m, '_jupyter_nbextension_paths'):
        raise KeyError(
            f'The Python module {module} is not a valid nbextension, '
            f'it is missing the `_jupyter_nbextension_paths()` method.'
        )
    nbexts = m._jupyter_nbextension_paths()
    return m, nbexts



if __name__ == '__main__':
    main()
