__version__ = '0.1.2'

import sys
import platform
from distutils.version import LooseVersion as V

if sys.platform != "darwin" or V(platform.mac_ver()[0]) < V("10.9"):
    from ._dummy import *
else:
    from ._nope import *

del sys, platform, V
