# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

# Source borrowed from site-packages/jupyter_core/paths.py


def __vsc_print_nbextension_widgets():
    import os as __vscode_os
    import site as __vscode_site
    import sys as __vscode_sys
    import tempfile as __vscode_tempfile
    from pathlib import Path as __vscode_Path

    pjoin = __vscode_os.path.join

    def envset(name):
        """Return True if the given environment variable is set

        An environment variable is considered set if it is assigned to a value
        other than 'no', 'n', 'false', 'off', '0', or '0.0' (case insensitive)
        """
        return __vscode_os.environ.get(name, "no").lower() not in [
            "no",
            "n",
            "false",
            "off",
            "0",
            "0.0",
        ]

    def get_home_dir():
        """Get the real path of the home directory"""
        homedir = __vscode_os.path.expanduser("~")
        # Next line will make things work even when /home/ is a symlink to
        # /usr/home as it is on FreeBSD, for example
        homedir = str(__vscode_Path(homedir).resolve())
        return homedir

    _dtemps: dict = {}

    def _mkdtemp_once(name):
        """Make or reuse a temporary directory.

        If this is called with the same name in the same process, it will return
        the same directory.
        """
        try:
            return _dtemps[name]
        except KeyError:
            d = _dtemps[name] = __vscode_tempfile.mkdtemp(prefix=name + "-")
            return d

    def jupyter_config_dir():
        """Get the Jupyter config directory for this platform and user.

        Returns JUPYTER_CONFIG_DIR if defined, else ~/.jupyter
        """

        env = __vscode_os.environ
        if env.get("JUPYTER_NO_CONFIG"):
            return _mkdtemp_once("jupyter-clean-cfg")

        if env.get("JUPYTER_CONFIG_DIR"):
            return env["JUPYTER_CONFIG_DIR"]

        home_dir = get_home_dir()
        return pjoin(home_dir, ".jupyter")

    def jupyter_data_dir():
        """Get the config directory for Jupyter data files for this platform and user.

        These are non-transient, non-configuration files.

        Returns JUPYTER_DATA_DIR if defined, else a platform-appropriate path.
        """
        env = __vscode_os.environ

        if env.get("JUPYTER_DATA_DIR"):
            return env["JUPYTER_DATA_DIR"]

        home = get_home_dir()

        if __vscode_sys.platform == "darwin":
            return __vscode_os.path.join(home, "Library", "Jupyter")
        elif __vscode_os.name == "nt":
            appdata = __vscode_os.environ.get("APPDATA", None)
            if appdata:
                return str(__vscode_Path(appdata, "jupyter").resolve())
            else:
                return pjoin(jupyter_config_dir(), "data")
        else:
            # Linux, non-OS X Unix, AIX, etc.
            xdg = env.get("XDG_DATA_HOME", None)
            if not xdg:
                xdg = pjoin(home, ".local", "share")
            return pjoin(xdg, "jupyter")

    if __vscode_os.name == "nt":
        programdata = __vscode_os.environ.get("PROGRAMDATA", None)
        if programdata:
            SYSTEM_JUPYTER_PATH = [pjoin(programdata, "jupyter")]
        else:  # PROGRAMDATA is not defined by default on XP.
            SYSTEM_JUPYTER_PATH = [
                __vscode_os.path.join(__vscode_sys.prefix, "share", "jupyter")
            ]
    else:
        SYSTEM_JUPYTER_PATH = [
            "/usr/local/share/jupyter",
            "/usr/share/jupyter",
        ]

    ENV_JUPYTER_PATH = [__vscode_os.path.join(__vscode_sys.prefix, "share", "jupyter")]

    def jupyter_path(*subdirs):
        """Return a list of directories to search for data files

        JUPYTER_PATH environment variable has highest priority.

        If the JUPYTER_PREFER_ENV_PATH environment variable is set, the environment-level
        directories will have priority over user-level directories.

        If the Python __vscode_site.ENABLE_USER_SITE variable is True, we also add the
        appropriate Python user site subdirectory to the user-level directories.


        If ``*subdirs`` are given, that subdirectory will be added to each element.

        Examples:

        >>> jupyter_path()
        ['~/.local/jupyter', '/usr/local/share/jupyter']
        >>> jupyter_path('kernels')
        ['~/.local/jupyter/kernels', '/usr/local/share/jupyter/kernels']
        """

        paths: list = []

        # highest priority is explicit environment variable
        if __vscode_os.environ.get("JUPYTER_PATH"):
            paths.extend(
                p.rstrip(__vscode_os.sep)
                for p in __vscode_os.environ["JUPYTER_PATH"].split(__vscode_os.pathsep)
            )

        # Next is environment or user, depending on the JUPYTER_PREFER_ENV_PATH flag
        user = [jupyter_data_dir()]
        if __vscode_site.ENABLE_USER_SITE:
            # Check if __vscode_site.getuserbase() exists to be compatible with virtualenv,
            # which often does not have this method.
            if hasattr(__vscode_site, "getuserbase"):
                userbase = __vscode_site.getuserbase()
            else:
                userbase = __vscode_site.USER_BASE

            if userbase:
                userdir = __vscode_os.path.join(userbase, "share", "jupyter")
                if userdir not in user:
                    user.append(userdir)

        env = [p for p in ENV_JUPYTER_PATH if p not in SYSTEM_JUPYTER_PATH]

        if envset("JUPYTER_PREFER_ENV_PATH"):
            paths.extend(env)
            paths.extend(user)
        else:
            paths.extend(user)
            paths.extend(env)

        # finally, system
        paths.extend(SYSTEM_JUPYTER_PATH)

        # add subdir, if requested
        if subdirs:
            paths = [pjoin(p, *subdirs) for p in paths]
        return paths

    __vsc_nbextension_widgets = []
    __vsc_file = ""
    __vsc_nbextension_Folder = ""
    __vscode_widget_folder = ""
    import glob as _VSCODE_glob

    try:
        for __vsc_nbextension_Folder in jupyter_path("nbextensions"):
            for __vsc_file in _VSCODE_glob.glob(
                __vsc_nbextension_Folder
                + __vscode_os.path.sep
                + "*"
                + __vscode_os.path.sep
                + "extension.js"
            ):
                __vscode_widget_folder = __vsc_file.replace(
                    __vsc_nbextension_Folder, ""
                )
                if not __vscode_widget_folder in __vsc_nbextension_widgets:
                    __vsc_nbextension_widgets.append(__vscode_widget_folder)

        print(__vsc_nbextension_widgets)
    except:
        pass

    # We need to ensure these variables don't interfere with the variable viewer, hence delete them after use.
    del _VSCODE_glob
    del __vsc_file
    del __vsc_nbextension_Folder
    del __vscode_widget_folder
    del __vsc_nbextension_widgets
    del __vscode_os
    del __vscode_site
    del __vscode_sys
    del __vscode_tempfile
    del __vscode_Path


__vsc_print_nbextension_widgets()

del __vsc_print_nbextension_widgets
