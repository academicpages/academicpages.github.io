"""
Basic post processor
"""
# -----------------------------------------------------------------------------
# Copyright (c) 2013, the IPython Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------

from ..utils.base import NbConvertBase


# -----------------------------------------------------------------------------
# Classes
# -----------------------------------------------------------------------------
class PostProcessorBase(NbConvertBase):
    def __call__(self, input):
        """
        See def postprocess() ...
        """
        self.postprocess(input)

    def postprocess(self, input):
        """
        Post-process output from a writer.
        """
        raise NotImplementedError("postprocess")
