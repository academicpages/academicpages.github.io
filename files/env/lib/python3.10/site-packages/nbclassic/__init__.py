import os
import sys
from ._version import __version__


# Packagers: modify this line if you store the notebook static files elsewhere
DEFAULT_STATIC_FILES_PATH = os.path.join(os.path.dirname(__file__), "static")


NOTEBOOK_V7_DETECTED = False

# Notebook shim to ensure notebook extensions backwards compatiblity.

try:
    from notebook._version import version_info as notebook_version_info
except Exception:
    notebook_version_info = None
    # No notebook python package found.
    # Shimming notebook to jupyter_server for notebook extensions backwards compatibility.
    # We shim the complete notebook module.
    import jupyter_server
    sys.modules["notebook"] = jupyter_server
    from jupyter_server.base import handlers
    from notebook.base import handlers as notebook_handlers
    handlers.IPythonHandler = handlers.JupyterHandler
    notebook_handlers.IPythonHandler = handlers.JupyterHandler

if notebook_version_info is not None:
    # Notebook is available on the platform.
    # We shim based on the notebook version.
    if notebook_version_info >= (7,):
        NOTEBOOK_V7_DETECTED = True
        from .shim_notebook import shim_notebook
        # Shimming existing notebook python package > 6 to jupyter_server.
        # For notebook extensions backwards compatibility.
        shim_notebook()
        # Sanity check for the notebook shim.
        from jupyter_server.base.handlers import IPythonHandler as JupyterServerIPythonHandler
        assert JupyterServerIPythonHandler.__name__ == "JupyterHandler"
        from notebook.base.handlers import IPythonHandler as NotebookIPythonHandler
        assert NotebookIPythonHandler.__name__ == "JupyterHandler" or NotebookIPythonHandler.__name__ == "IPythonHandler"


# Include both nbclassic/ and nbclassic/templates/.  This makes it
# possible for users to override a template with a file that inherits from that
# template.
#
# For example, if you want to override a specific block of notebook.html, you
# can create a file called notebook.html that inherits from
# templates/notebook.html, and the latter will resolve correctly to the base
# implementation.
DEFAULT_TEMPLATE_PATH_LIST = [
    os.path.dirname(__file__),
    os.path.join(os.path.dirname(__file__), "templates"),
]


def nbclassic_path():
    if NOTEBOOK_V7_DETECTED:
        return "/nbclassic"
    return ""

def _jupyter_server_extension_paths():
    # Locally import to avoid install errors.
    from .notebookapp import NotebookApp

    return [
        {
            'module': 'nbclassic.notebookapp',
            'app': NotebookApp,
            'name': 'jupyter-nbclassic'
        }
    ]
