"""pyzmq does not ship tornado's futures,
this just raises informative NotImplementedErrors to avoid having to change too much code.
"""

class NotImplementedFuture(object):
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("pyzmq does not ship tornado's Futures, "
            "install tornado >= 3.0 for future support."
        )

Future = TracebackFuture = NotImplementedFuture

def is_future(x):
    return isinstance(x, Future)
