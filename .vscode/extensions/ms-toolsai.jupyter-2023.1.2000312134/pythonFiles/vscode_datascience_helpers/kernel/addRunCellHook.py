import types as _VSCODE_types
import os
import hashlib as _VSCODE_hashlib
from IPython import get_ipython

# Variable that prevent wrapping from happing more than_once
__VSCODE_wrapped_run_cell = False

# This function computes the hash for the code. It must follow the same algorithm as in use here:
# https://github.com/microsoft/vscode-jupyter/blob/312511f3cbd8b2bb5bc70fa9b771429e22d0c258/src/client/datascience/editor-integration/cellhashprovider.ts#L181
def __VSCODE_compute_hash(code, number=0):
    hash_digest = _VSCODE_hashlib.sha1(code.encode("utf-8")).hexdigest()
    return "<ipython-input-{0}-{1}>".format(number, hash_digest[:12])


# This function will wrap InteractiveShell.run-cell and force its IPYKERNEL_CELL_NAME to match the
# predicted value used by the Jupyter Extension
def __VSCODE_wrap_run_cell(wrapped_func):
    old_func = wrapped_func.__func__
    __VSCODE_wrapped_run_cell = True

    def wrapper(*args, **kwargs):
        try:
            store_history = args[2] if len(args) > 2 else kwargs["store_history"]
            if store_history:
                predicted_name = __VSCODE_compute_hash(args[1], args[0].execution_count)
                os.environ["IPYKERNEL_CELL_NAME"] = predicted_name
            result = old_func(*args, **kwargs)
            if store_history:
                del os.environ["IPYKERNEL_CELL_NAME"]
            return result
        except:
            return old_func(*args, **kwargs)

    return _VSCODE_types.MethodType(wrapper, wrapped_func.__self__)


# Double check this still exists on IPython
if get_ipython() and get_ipython().run_cell and not __VSCODE_wrapped_run_cell:
    get_ipython().run_cell = __VSCODE_wrap_run_cell(get_ipython().run_cell)
