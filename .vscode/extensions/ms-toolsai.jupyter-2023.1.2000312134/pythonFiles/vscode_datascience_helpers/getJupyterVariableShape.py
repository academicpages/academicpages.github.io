# Query Jupyter server for defined variables list
# Tested on 2.7 and 3.6
import json as _VSCODE_json
import builtins

# In IJupyterVariables.getValue this '_VSCode_JupyterTestValue' will be replaced with the json stringified value of the target variable
# Indexes off of _VSCODE_targetVariable need to index types that are part of IJupyterVariable
_VSCODE_targetVariable = _VSCODE_json.loads("""_VSCode_JupyterTestValue""")

# Secure here as what we are doing an eval on is under our control
_VSCODE_evalResult = eval(_VSCODE_targetVariable["name"])  # nosec

# Find shape and count if available
if hasattr(_VSCODE_evalResult, "shape"):
    try:
        # Get a bit more restrictive with exactly what we want to count as a shape, since anything can define it
        if isinstance(_VSCODE_evalResult.shape, tuple):
            _VSCODE_shapeStr = str(_VSCODE_evalResult.shape)
            if (
                len(_VSCODE_shapeStr) >= 3
                and _VSCODE_shapeStr[0] == "("
                and _VSCODE_shapeStr[-1] == ")"
                and "," in _VSCODE_shapeStr
            ):
                _VSCODE_targetVariable["shape"] = _VSCODE_shapeStr
            del _VSCODE_shapeStr
    except TypeError:
        pass

if hasattr(_VSCODE_evalResult, "__len__"):
    try:
        _VSCODE_targetVariable["count"] = len(_VSCODE_evalResult)
    except TypeError:
        pass

builtins.print(_VSCODE_json.dumps(_VSCODE_targetVariable))
del _VSCODE_json
