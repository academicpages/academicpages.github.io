# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root
# for license information.

from __future__ import absolute_import, division, print_function, unicode_literals

"""An implementation of the Debug Adapter Protocol (DAP) for Python.

https://microsoft.github.io/debug-adapter-protocol/
"""

# debugpy stable public API consists solely of members of this module that are
# enumerated below.
__all__ = [
    "__version__",
    "breakpoint",
    "configure",
    "connect",
    "debug_this_thread",
    "is_client_connected",
    "listen",
    "log_to",
    "trace_this_thread",
    "wait_for_client",
]

import codecs
import os

from debugpy import _version
from debugpy.common import compat


# Expose debugpy.server API from subpackage, but do not actually import it unless
# and until a member is invoked - we don't want the server package loaded in the
# adapter, the tests, or setup.py.

# Docstrings for public API members must be formatted according to PEP 8 - no more
# than 72 characters per line! - and must be readable when retrieved via help().


def log_to(path):
    """Generate detailed debugpy logs in the specified directory.

    The directory must already exist. Several log files are generated,
    one for every process involved in the debug session.
    """

    from debugpy.server import api

    return api.log_to(path)


def configure(properties=None, **kwargs):
    """Sets debug configuration properties that cannot be set in the
    "attach" request, because they must be applied as early as possible
    in the process being debugged.

    For example, a "launch" configuration with subprocess debugging
    disabled can be defined entirely in JSON::

        {
            "request": "launch",
            "subProcess": false,
            ...
        }

    But the same cannot be done with "attach", because "subProcess"
    must be known at the point debugpy starts tracing execution. Thus,
    it is not available in JSON, and must be omitted::

        {
            "request": "attach",
            ...
        }

    and set from within the debugged process instead::

        debugpy.configure(subProcess=False)
        debugpy.listen(...)

    Properties to set can be passed either as a single dict argument,
    or as separate keyword arguments::

        debugpy.configure({"subProcess": False})
    """

    from debugpy.server import api

    return api.configure(properties, **kwargs)


def listen(address):
    """Starts a debug adapter debugging this process, that listens for
    incoming socket connections from clients on the specified address.

    address must be either a (host, port) tuple, as defined by the
    standard socket module for the AF_INET address family, or a port
    number. If only the port is specified, host is "127.0.0.1".

    Returns the interface and the port on which the debug adapter is
    actually listening, in the same format as address. This may be
    different from address if port was 0 in the latter, in which case
    the adapter will pick some unused ephemeral port to listen on.

    This function does't wait for a client to connect to the debug
    adapter that it starts. Use wait_for_client() to block execution
    until the client connects.
    """

    from debugpy.server import api

    return api.listen(address)


@compat.kwonly
def connect(address, access_token=None):
    """Tells an existing debug adapter instance that is listening on the
    specified address to debug this process.

    address must be either a (host, port) tuple, as defined by the
    standard socket module for the AF_INET address family, or a port
    number. If only the port is specified, host is "127.0.0.1".

    access_token must be the same value that was passed to the adapter
    via the --server-access-token command-line switch.

    This function does't wait for a client to connect to the debug
    adapter that it connects to. Use wait_for_client() to block
    execution until the client connects.
    """

    from debugpy.server import api

    return api.connect(address, access_token=access_token)


def wait_for_client():
    """If there is a client connected to the debug adapter that is
    debugging this process, returns immediately. Otherwise, blocks
    until a client connects to the adapter.

    While this function is waiting, it can be canceled by calling
    wait_for_client.cancel() from another thread.
    """

    from debugpy.server import api

    return api.wait_for_client()


def is_client_connected():
    """True if a client is connected to the debug adapter that is
    debugging this process.
    """

    from debugpy.server import api

    return api.is_client_connected()


def breakpoint():
    """If a client is connected to the debug adapter that is debugging
    this process, pauses execution of all threads, and simulates a
    breakpoint being hit at the line following the call.

    On Python 3.7 and above, this is the same as builtins.breakpoint().
    """

    from debugpy.server import api

    return api.breakpoint()


def debug_this_thread():
    """Makes the debugger aware of the current thread.

    Must be called on any background thread that is started by means
    other than the usual Python APIs (i.e. the "threading" module),
    in order for breakpoints to work on that thread.
    """

    from debugpy.server import api

    return api.debug_this_thread()


def trace_this_thread(should_trace):
    """Tells the debug adapter to enable or disable tracing on the
    current thread.

    When the thread is traced, the debug adapter can detect breakpoints
    being hit, but execution is slower, especially in functions that
    have any breakpoints set in them. Disabling tracing when breakpoints
    are not anticipated to be hit can improve performance. It can also
    be used to skip breakpoints on a particular thread.

    Tracing is automatically disabled for all threads when there is no
    client connected to the debug adapter.
    """

    from debugpy.server import api

    return api.trace_this_thread(should_trace)


__version__ = _version.get_versions()["version"]

# Force absolute path on Python 2.
__file__ = os.path.abspath(__file__)

# Preload encodings that we're going to use to avoid import deadlocks on Python 2,
# before importing anything from debugpy.
map(codecs.lookup, ["ascii", "utf8", "utf-8", "latin1", "latin-1", "idna", "hex"])
