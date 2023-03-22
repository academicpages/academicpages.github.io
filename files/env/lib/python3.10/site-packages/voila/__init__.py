#############################################################################
# Copyright (c) 2018, Voilà Contributors                                    #
# Copyright (c) 2018, QuantStack                                            #
#                                                                           #
# Distributed under the terms of the BSD 3-Clause License.                  #
#                                                                           #
# The full license is in the file LICENSE, distributed with this software.  #
#############################################################################

from ._version import __version__  # noqa
from .server_extension import _load_jupyter_server_extension # noqa
from .server_extension import load_jupyter_server_extension  # noqa


def _jupyter_nbextension_paths():
    return [
        dict(section="notebook", src="static", dest="voila", require="voila/extension")
    ]


def _jupyter_labextension_paths():
    return [{"src": "labextension", "dest": "@voila-dashboards/jupyterlab-preview"}]
