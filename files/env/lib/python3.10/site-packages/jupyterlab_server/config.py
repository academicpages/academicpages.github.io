"""JupyterLab Server config"""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

import json
import os.path as osp
from glob import iglob
from itertools import chain
from os.path import join as pjoin

from jupyter_core.paths import SYSTEM_CONFIG_PATH, jupyter_config_dir, jupyter_path
from jupyter_server.services.config.manager import ConfigManager, recursive_update
from traitlets import Bool, HasTraits, List, Unicode, default

from .server import url_path_join as ujoin

# -----------------------------------------------------------------------------
# Module globals
# -----------------------------------------------------------------------------

DEFAULT_TEMPLATE_PATH = osp.join(osp.dirname(__file__), "templates")


def get_package_url(data):
    """Get the url from the extension data"""
    # homepage, repository  are optional
    if "homepage" in data:
        url = data["homepage"]
    elif "repository" in data and isinstance(data["repository"], dict):
        url = data["repository"].get("url", "")
    else:
        url = ""
    return url


def get_federated_extensions(labextensions_path):
    """Get the metadata about federated extensions"""
    federated_extensions = {}
    for ext_dir in labextensions_path:
        # extensions are either top-level directories, or two-deep in @org directories
        for ext_path in chain(
            iglob(pjoin(ext_dir, "[!@]*", "package.json")),
            iglob(pjoin(ext_dir, "@*", "*", "package.json")),
        ):
            with open(ext_path, encoding="utf-8") as fid:
                pkgdata = json.load(fid)
            if pkgdata["name"] not in federated_extensions:
                data = dict(
                    name=pkgdata["name"],
                    version=pkgdata["version"],
                    description=pkgdata.get("description", ""),
                    url=get_package_url(pkgdata),
                    ext_dir=ext_dir,
                    ext_path=osp.dirname(ext_path),
                    is_local=False,
                    dependencies=pkgdata.get("dependencies", dict()),
                    jupyterlab=pkgdata.get("jupyterlab", dict()),
                )
                install_path = osp.join(osp.dirname(ext_path), "install.json")
                if osp.exists(install_path):
                    with open(install_path, encoding="utf-8") as fid:
                        data["install"] = json.load(fid)
                federated_extensions[data["name"]] = data
    return federated_extensions


def get_static_page_config(app_settings_dir=None, logger=None, level="all"):
    """Get the static page config for JupyterLab

    Parameters
    ----------
    logger: logger, optional
        An optional logging object
    level: string, optional ['all']
        The level at which to get config: can be 'all', 'user', 'sys_prefix', or 'system'
    """
    cm = _get_config_manager(level)
    return cm.get("page_config")


def get_page_config(labextensions_path, app_settings_dir=None, logger=None):
    """Get the page config for the application handler"""
    # Build up the full page config
    page_config: dict = {}

    disabled_key = "disabledExtensions"

    # Start with the app_settings_dir as lowest priority
    if app_settings_dir:
        app_page_config = pjoin(app_settings_dir, "page_config.json")
        if osp.exists(app_page_config):
            with open(app_page_config, encoding="utf-8") as fid:
                data = json.load(fid)

            # Convert lists to dicts
            for key in [disabled_key, "deferredExtensions"]:
                if key in data:
                    data[key] = {key: True for key in data[key]}

            recursive_update(page_config, data)

    # Get the traitlets config
    static_page_config = get_static_page_config(logger=logger, level="all")
    recursive_update(page_config, static_page_config)

    # Handle federated extensions that disable other extensions
    disabled_by_extensions_all = {}
    extensions = page_config["federated_extensions"] = []

    federated_exts = get_federated_extensions(labextensions_path)

    # Ensure there is a disabled key
    page_config.setdefault(disabled_key, {})

    for (_, ext_data) in federated_exts.items():
        if "_build" not in ext_data["jupyterlab"]:
            logger.warning("%s is not a valid extension" % ext_data["name"])
            continue
        extbuild = ext_data["jupyterlab"]["_build"]
        extension = {"name": ext_data["name"], "load": extbuild["load"]}

        if "extension" in extbuild:
            extension["extension"] = extbuild["extension"]
        if "mimeExtension" in extbuild:
            extension["mimeExtension"] = extbuild["mimeExtension"]
        if "style" in extbuild:
            extension["style"] = extbuild["style"]
        extensions.append(extension)

        # If there is disabledExtensions metadata, consume it.
        name = ext_data["name"]

        if ext_data["jupyterlab"].get(disabled_key):
            disabled_by_extensions_all[ext_data["name"]] = ext_data["jupyterlab"][disabled_key]

    # Handle source extensions that disable other extensions
    # Check for `jupyterlab`:`extensionMetadata` in the built application directory's package.json
    if app_settings_dir:
        app_dir = osp.dirname(app_settings_dir)
        package_data_file = pjoin(app_dir, "static", "package.json")
        if osp.exists(package_data_file):
            with open(package_data_file, encoding="utf-8") as fid:
                app_data = json.load(fid)
            all_ext_data = app_data["jupyterlab"].get("extensionMetadata", {})
            for (ext, ext_data) in all_ext_data.items():
                if ext in disabled_by_extensions_all:
                    continue
                if ext_data.get(disabled_key):
                    disabled_by_extensions_all[ext] = ext_data[disabled_key]

    disabled_by_extensions = {}
    for name in sorted(disabled_by_extensions_all):
        # skip if the extension itself is disabled by other config
        if page_config[disabled_key].get(name) is True:
            continue

        disabled_list = disabled_by_extensions_all[name]
        for item in disabled_list:
            disabled_by_extensions[item] = True

    rollup_disabled = disabled_by_extensions
    rollup_disabled.update(page_config.get(disabled_key, []))
    page_config[disabled_key] = rollup_disabled

    # Convert dictionaries to lists to give to the front end
    for (key, value) in page_config.items():

        if isinstance(value, dict):
            page_config[key] = [subkey for subkey in value if value[subkey]]

    return page_config


def write_page_config(page_config, level="all"):
    """Write page config to disk"""
    cm = _get_config_manager(level)
    cm.set("page_config", page_config)


class LabConfig(HasTraits):
    """The lab application configuration object."""

    app_name = Unicode("", help="The name of the application.").tag(config=True)

    app_version = Unicode("", help="The version of the application.").tag(config=True)

    app_namespace = Unicode("", help="The namespace of the application.").tag(config=True)

    app_url = Unicode("/lab", help="The url path for the application.").tag(config=True)

    app_settings_dir = Unicode("", help="The application settings directory.").tag(config=True)

    extra_labextensions_path = List(
        Unicode(), help="""Extra paths to look for federated JupyterLab extensions"""
    ).tag(config=True)

    labextensions_path = List(
        Unicode(), help="The standard paths to look in for federated JupyterLab extensions"
    ).tag(config=True)

    templates_dir = Unicode("", help="The application templates directory.").tag(config=True)

    static_dir = Unicode(
        "",
        help=(
            "The optional location of local static files. "
            "If given, a static file handler will be "
            "added."
        ),
    ).tag(config=True)

    labextensions_url = Unicode("", help="The url for federated JupyterLab extensions").tag(
        config=True
    )

    settings_url = Unicode(help="The url path of the settings handler.").tag(config=True)

    user_settings_dir = Unicode(
        "", help=("The optional location of the user settings directory.")
    ).tag(config=True)

    schemas_dir = Unicode(
        "",
        help=(
            "The optional location of the settings "
            "schemas directory. If given, a handler will "
            "be added for settings."
        ),
    ).tag(config=True)

    workspaces_api_url = Unicode(help="The url path of the workspaces API.").tag(config=True)

    workspaces_dir = Unicode(
        "",
        help=(
            "The optional location of the saved "
            "workspaces directory. If given, a handler "
            "will be added for workspaces."
        ),
    ).tag(config=True)

    listings_url = Unicode(help="The listings url.").tag(config=True)

    themes_url = Unicode(help="The theme url.").tag(config=True)

    licenses_url = Unicode(help="The third-party licenses url.")

    themes_dir = Unicode(
        "",
        help=(
            "The optional location of the themes "
            "directory. If given, a handler will be added "
            "for themes."
        ),
    ).tag(config=True)

    translations_api_url = Unicode(help="The url path of the translations handler.").tag(
        config=True
    )

    tree_url = Unicode(help="The url path of the tree handler.").tag(config=True)

    cache_files = Bool(
        True,
        help=("Whether to cache files on the server. This should be `True` except in dev mode."),
    ).tag(config=True)

    notebook_starts_kernel = Bool(
        True, help="Whether a notebook should start a kernel automatically."
    ).tag(config=True)

    @default("template_dir")
    def _default_template_dir(self):
        return DEFAULT_TEMPLATE_PATH

    @default("labextensions_url")
    def _default_labextensions_url(self):
        return ujoin(self.app_url, "extensions/")

    @default("labextensions_path")
    def _default_labextensions_path(self):
        return jupyter_path("labextensions")

    @default("workspaces_url")
    def _default_workspaces_url(self):
        return ujoin(self.app_url, "workspaces/")

    @default("workspaces_api_url")
    def _default_workspaces_api_url(self):
        return ujoin(self.app_url, "api", "workspaces/")

    @default("settings_url")
    def _default_settings_url(self):
        return ujoin(self.app_url, "api", "settings/")

    @default("listings_url")
    def _default_listings_url(self):
        return ujoin(self.app_url, "api", "listings/")

    @default("themes_url")
    def _default_themes_url(self):
        return ujoin(self.app_url, "api", "themes/")

    @default("licenses_url")
    def _default_licenses_url(self):
        return ujoin(self.app_url, "api", "licenses/")

    @default("tree_url")
    def _default_tree_url(self):
        return ujoin(self.app_url, "tree/")

    @default("translations_api_url")
    def _default_translations_api_url(self):
        return ujoin(self.app_url, "api", "translations/")


def _get_config_manager(level):
    """Get the location of config files for the current context
    Returns the string to the environment
    """
    allowed = ["all", "user", "sys_prefix", "system", "app", "extension"]
    if level not in allowed:
        raise ValueError(f"Page config level must be one of: {allowed}")

    config_name = "labconfig"

    if level == "all":
        return ConfigManager(config_dir_name=config_name)

    if level == "user":
        config_dir = jupyter_config_dir()
    elif level == "sys_prefix":
        # Delayed import since this gets monkey-patched in tests
        from jupyter_core.paths import ENV_CONFIG_PATH

        config_dir = ENV_CONFIG_PATH[0]
    else:
        config_dir = SYSTEM_CONFIG_PATH[0]

    full_config_path = osp.join(config_dir, config_name)

    return ConfigManager(read_config_path=[full_config_path], write_config_dir=full_config_path)
