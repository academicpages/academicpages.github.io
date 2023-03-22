import os

from _pydev_bundle import pydev_log
from _pydevd_bundle.pydevd_trace_dispatch import USING_CYTHON
from _pydevd_bundle.pydevd_constants import USE_CYTHON_FLAG, ENV_FALSE_LOWER_VALUES, \
    ENV_TRUE_LOWER_VALUES, IS_PY36_OR_GREATER, IS_PY38_OR_GREATER, SUPPORT_GEVENT, IS_PYTHON_STACKLESS

frame_eval_func = None
stop_frame_eval = None
dummy_trace_dispatch = None
clear_thread_local_info = None

USING_FRAME_EVAL = False

# "NO" means we should not use frame evaluation, 'YES' we should use it (and fail if not there) and unspecified uses if possible.
use_frame_eval = os.environ.get('PYDEVD_USE_FRAME_EVAL', '').lower()

if use_frame_eval in ENV_FALSE_LOWER_VALUES or USE_CYTHON_FLAG in ENV_FALSE_LOWER_VALUES or not USING_CYTHON:
    pass

elif SUPPORT_GEVENT or (IS_PYTHON_STACKLESS and not IS_PY38_OR_GREATER):
    pass
    # i.e gevent and frame eval mode don't get along very well.
    # https://github.com/microsoft/debugpy/issues/189
    # Same problem with Stackless.
    # https://github.com/stackless-dev/stackless/issues/240

elif use_frame_eval in ENV_TRUE_LOWER_VALUES:
    # Fail if unable to use
    from _pydevd_frame_eval.pydevd_frame_eval_cython_wrapper import frame_eval_func, stop_frame_eval, dummy_trace_dispatch, clear_thread_local_info
    USING_FRAME_EVAL = True

else:
    # Try to use if possible
    if IS_PY36_OR_GREATER:
        try:
            from _pydevd_frame_eval.pydevd_frame_eval_cython_wrapper import frame_eval_func, stop_frame_eval, dummy_trace_dispatch, clear_thread_local_info
            USING_FRAME_EVAL = True
        except ImportError:
            pydev_log.show_compile_cython_command_line()
