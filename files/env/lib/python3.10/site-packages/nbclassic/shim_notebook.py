"""Shim the notebook module for the classic extensions.
"""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

import sys


def shim_notebook():
    """Define in sys.module the needed notebook packages that should be fullfilled by
    their corresponding and backwards-compatible jupyter-server packages.

    TODO Can we lazy load these loadings?
    
    Note: We could a custom module loader to achieve similar functionality. The 
    logic thar conditional loading seems to be more complicated than simply
    listing by hand the needed subpackages but could avoid latency on server start.
    
    https://docs.python.org/3/library/importlib.html#importlib.abc.Loader

    These are the notebook packages we need to shim:

    auth
    base
    bundler <- no, already available in nbclassic
    edit <- no, already available in nbclassic
    files
    gateway
    i18n <- no, already available in nbclassic
    kernelspecs
    nbconvert
    notebook <- no, already available in nbclassic
    prometheus
    services
    static <- no, already available in nbclassic
    templates <- no, already available in nbclassic
    terminal <- no, already available in nbclassic
    tests <- no, already available in nbclassic
    tree <- no, already available in nbclassic
    view
    __init__.py <- no, already available in nbclassic
    __main__.py <- no, already available in nbclassic
    _sysinfo.py <- no, already available in nbclassic
    _tz.py
    _version.py <- no, already available in nbclassic
    config_manager.py <- no, already available in nbclassic
    extensions.py <- no, already available in nbclassic
    jstest.py <- no, already available in nbclassic
    log.py
    nbextensions.py <- no, already available in nbclassic
    notebookapp.py <- no, already available in nbclassic
    serverextensions.py <- no, already available in nbclassic
    traittypes.py <- no, already available in nbclassic
    transutils.py <- no, already available in nbclassic
    utils.py

    """

    from jupyter_server import auth
    sys.modules["notebook.auth"] = auth
    from jupyter_server import base
    sys.modules["notebook.base"] = base
    from jupyter_server import files
    sys.modules["notebook.files"] = files
    from jupyter_server import gateway
    sys.modules["notebook.gateway"] = gateway
    from jupyter_server import kernelspecs
    sys.modules["notebook.kernelspecs"] = kernelspecs
    from jupyter_server import nbconvert
    sys.modules["notebook.nbconvert"] = nbconvert
    from jupyter_server import prometheus
    sys.modules["notebook.prometheus"] = prometheus
    from jupyter_server import services
    sys.modules["notebook.services"] = services
    from jupyter_server import view
    sys.modules["notebook.view"] = view
    from jupyter_server import _tz
    sys.modules["notebook._tz"] = _tz
    from jupyter_server import log
    sys.modules["notebook.log"] = log
    from jupyter_server import utils
    sys.modules["notebook.utils"] = utils

    base.handlers.IPythonHandler = base.handlers.JupyterHandler
    sys.modules["notebook.base.handlers.IPythonHandler"] = base.handlers.JupyterHandler
