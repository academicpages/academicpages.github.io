"""The Jupyter HTML Notebook"""

import os

# Packagers: modify the next line if you store the notebook template files
# elsewhere

# Include both notebook/ and notebook/templates/.  This makes it
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

DEFAULT_NOTEBOOK_PORT = 8888

del os

from .nbextensions import install_nbextension
from ._version import version_info, __version__
