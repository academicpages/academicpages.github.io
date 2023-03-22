from _pydevd_bundle.pydevd_constants import EXCEPTION_TYPE_USER_UNHANDLED, EXCEPTION_TYPE_UNHANDLED
from _pydev_bundle import pydev_log


class Frame(object):

    def __init__(
            self,
            f_back,
            f_fileno,
            f_code,
            f_locals,
            f_globals=None,
            f_trace=None):
        self.f_back = f_back
        self.f_lineno = f_fileno
        self.f_code = f_code
        self.f_locals = f_locals
        self.f_globals = f_globals
        self.f_trace = f_trace

        if self.f_globals is None:
            self.f_globals = {}


class FCode(object):

    def __init__(self, name, filename):
        self.co_name = name
        self.co_filename = filename
        self.co_firstlineno = 1


def add_exception_to_frame(frame, exception_info):
    frame.f_locals['__exception__'] = exception_info


def remove_exception_from_frame(frame):
    frame.f_locals.pop('__exception__', None)


FILES_WITH_IMPORT_HOOKS = ['pydev_monkey_qt.py', 'pydev_import_hook.py']


def just_raised(trace):
    if trace is None:
        return False
    return trace.tb_next is None


def ignore_exception_trace(trace):
    while trace is not None:
        filename = trace.tb_frame.f_code.co_filename
        if filename in (
            '<frozen importlib._bootstrap>', '<frozen importlib._bootstrap_external>'):
            # Do not stop on inner exceptions in py3 while importing
            return True

        # ImportError should appear in a user's code, not inside debugger
        for file in FILES_WITH_IMPORT_HOOKS:
            if filename.endswith(file):
                return True

        trace = trace.tb_next

    return False


def cached_call(obj, func, *args):
    cached_name = '_cached_' + func.__name__
    if not hasattr(obj, cached_name):
        setattr(obj, cached_name, func(*args))

    return getattr(obj, cached_name)


class FramesList(object):

    def __init__(self):
        self._frames = []

        # If available, the line number for the frame will be gotten from this dict,
        # otherwise frame.f_lineno will be used (needed for unhandled exceptions as
        # the place where we report may be different from the place where it's raised).
        self.frame_id_to_lineno = {}

        self.exc_type = None
        self.exc_desc = None
        self.trace_obj = None

        # This may be set to set the current frame (for the case where we have
        # an unhandled exception where we want to show the root bu we have a different
        # executing frame).
        self.current_frame = None

        # This is to know whether an exception was extracted from a __cause__ or __context__.
        self.exc_context_msg = ''

    def append(self, frame):
        self._frames.append(frame)

    def last_frame(self):
        return self._frames[-1]

    def __len__(self):
        return len(self._frames)

    def __iter__(self):
        return iter(self._frames)

    def __repr__(self):
        lst = ['FramesList(']

        lst.append('\n    exc_type: ')
        lst.append(str(self.exc_type))

        lst.append('\n    exc_desc: ')
        lst.append(str(self.exc_desc))

        lst.append('\n    trace_obj: ')
        lst.append(str(self.trace_obj))

        lst.append('\n    current_frame: ')
        lst.append(str(self.current_frame))

        for frame in self._frames:
            lst.append('\n    ')
            lst.append(repr(frame))
            lst.append(',')
        lst.append('\n)')
        return ''.join(lst)

    __str__ = __repr__


class _DummyFrameWrapper(object):

    def __init__(self, frame, f_lineno, f_back):
        self._base_frame = frame
        self.f_lineno = f_lineno
        self.f_back = f_back
        self.f_trace = None
        original_code = frame.f_code
        self.f_code = FCode(original_code.co_name , original_code.co_filename)

    @property
    def f_locals(self):
        return self._base_frame.f_locals

    @property
    def f_globals(self):
        return self._base_frame.f_globals


_cause_message = (
    "\nThe above exception was the direct cause "
    "of the following exception:\n\n")

_context_message = (
    "\nDuring handling of the above exception, "
    "another exception occurred:\n\n")


def create_frames_list_from_exception_cause(trace_obj, frame, exc_type, exc_desc, memo):
    lst = []
    msg = '<Unknown context>'
    try:
        exc_cause = getattr(exc_desc, '__cause__', None)
        msg = _cause_message
    except Exception:
        exc_cause = None

    if exc_cause is None:
        try:
            exc_cause = getattr(exc_desc, '__context__', None)
            msg = _context_message
        except Exception:
            exc_cause = None

    if exc_cause is None or id(exc_cause) in memo:
        return None

    # The traceback module does this, so, let's play safe here too...
    memo.add(id(exc_cause))

    tb = exc_cause.__traceback__
    frames_list = FramesList()
    frames_list.exc_type = type(exc_cause)
    frames_list.exc_desc = exc_cause
    frames_list.trace_obj = tb
    frames_list.exc_context_msg = msg

    while tb is not None:
        # Note: we don't use the actual tb.tb_frame because if the cause of the exception
        # uses the same frame object, the id(frame) would be the same and the frame_id_to_lineno
        # would be wrong as the same frame needs to appear with 2 different lines.
        lst.append((_DummyFrameWrapper(tb.tb_frame, tb.tb_lineno, None), tb.tb_lineno))
        tb = tb.tb_next

    for tb_frame, tb_lineno in lst:
        frames_list.append(tb_frame)
        frames_list.frame_id_to_lineno[id(tb_frame)] = tb_lineno

    return frames_list


def create_frames_list_from_traceback(trace_obj, frame, exc_type, exc_desc, exception_type=None):
    '''
    :param trace_obj:
        This is the traceback from which the list should be created.

    :param frame:
        This is the first frame to be considered (i.e.: topmost frame). If None is passed, all
        the frames from the traceback are shown (so, None should be passed for unhandled exceptions).

    :param exception_type:
        If this is an unhandled exception or user unhandled exception, we'll not trim the stack to create from the passed
        frame, rather, we'll just mark the frame in the frames list.
    '''
    lst = []

    tb = trace_obj
    if tb is not None and tb.tb_frame is not None:
        f = tb.tb_frame.f_back
        while f is not None:
            lst.insert(0, (f, f.f_lineno))
            f = f.f_back

    while tb is not None:
        lst.append((tb.tb_frame, tb.tb_lineno))
        tb = tb.tb_next

    curr = exc_desc
    memo = set()
    while True:
        initial = curr
        try:
            curr = getattr(initial, '__cause__', None)
        except Exception:
            curr = None

        if curr is None:
            try:
                curr = getattr(initial, '__context__', None)
            except Exception:
                curr = None

        if curr is None or id(curr) in memo:
            break

        # The traceback module does this, so, let's play safe here too...
        memo.add(id(curr))

        tb = getattr(curr, '__traceback__', None)

        while tb is not None:
            # Note: we don't use the actual tb.tb_frame because if the cause of the exception
            # uses the same frame object, the id(frame) would be the same and the frame_id_to_lineno
            # would be wrong as the same frame needs to appear with 2 different lines.
            lst.append((_DummyFrameWrapper(tb.tb_frame, tb.tb_lineno, None), tb.tb_lineno))
            tb = tb.tb_next

    frames_list = None

    for tb_frame, tb_lineno in reversed(lst):
        if frames_list is None and (
                (frame is tb_frame) or
                (frame is None) or
                (exception_type == EXCEPTION_TYPE_USER_UNHANDLED)
            ):
            frames_list = FramesList()

        if frames_list is not None:
            frames_list.append(tb_frame)
            frames_list.frame_id_to_lineno[id(tb_frame)] = tb_lineno

    if frames_list is None and frame is not None:
        # Fallback (shouldn't happen in practice).
        pydev_log.info('create_frames_list_from_traceback did not find topmost frame in list.')
        frames_list = create_frames_list_from_frame(frame)

    frames_list.exc_type = exc_type
    frames_list.exc_desc = exc_desc
    frames_list.trace_obj = trace_obj

    if exception_type == EXCEPTION_TYPE_USER_UNHANDLED:
        frames_list.current_frame = frame
    elif exception_type == EXCEPTION_TYPE_UNHANDLED:
        if len(frames_list) > 0:
            frames_list.current_frame = frames_list.last_frame()

    return frames_list


def create_frames_list_from_frame(frame):
    lst = FramesList()
    while frame is not None:
        lst.append(frame)
        frame = frame.f_back

    return lst
