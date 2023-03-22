"""Base class to manage comms"""

# Copyright (c) IPython Development Team.
# Distributed under the terms of the Modified BSD License.


import comm.base_comm
import traitlets
import traitlets.config


class CommManager(traitlets.config.LoggingConfigurable, comm.base_comm.CommManager):

    kernel = traitlets.Instance("ipykernel.kernelbase.Kernel")
    comms = traitlets.Dict()
    targets = traitlets.Dict()

    def __init__(self, **kwargs):
        # CommManager doesn't take arguments, so we explicitly forward arguments
        traitlets.config.LoggingConfigurable.__init__(self, **kwargs)
        comm.base_comm.CommManager.__init__(self)
