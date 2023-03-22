# -----------------------------------------------------------------------------
#  Copyright (c) The Jupyter Development Team
#
#  Distributed under the terms of the BSD License.  The full license is in
#  the file COPYING, distributed as part of this software.
# -----------------------------------------------------------------------------
from .. import localinterfaces


def test_load_ips():
    # Override the machinery that skips it if it was called before
    localinterfaces._load_ips.called = False

    # Just check this doesn't error
    localinterfaces._load_ips(suppress_exceptions=False)
