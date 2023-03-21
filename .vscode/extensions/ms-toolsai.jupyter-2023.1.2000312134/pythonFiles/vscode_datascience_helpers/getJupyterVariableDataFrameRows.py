# Query Jupyter server for the rows of a data frame
import json as _VSCODE_json
import builtins
import pandas as _VSCODE_pd
import pandas.io.json as _VSCODE_pd_json
import builtins as _VSCODE_builtins

# In IJupyterVariables.getValue this '_VSCode_JupyterTestValue' will be replaced with the json stringified value of the target variable
# Indexes off of _VSCODE_targetVariable need to index types that are part of IJupyterVariable
_VSCODE_targetVariable = _VSCODE_json.loads("""_VSCode_JupyterTestValue""")
_VSCODE_evalResult = _VSCODE_builtins.eval(_VSCODE_targetVariable["name"])

# _VSCode_JupyterStartRow and _VSCode_JupyterEndRow should be replaced dynamically with the literals
# for our start and end rows
_VSCODE_startRow = _VSCODE_builtins.max(_VSCode_JupyterStartRow, 0)
_VSCODE_endRow = _VSCODE_builtins.min(
    _VSCode_JupyterEndRow, _VSCODE_targetVariable["rowCount"]
)

# Assume we have a dataframe. If not, turn our eval result into a dataframe
_VSCODE_df = _VSCODE_evalResult
if isinstance(_VSCODE_evalResult, list):
    _VSCODE_df = _VSCODE_pd.DataFrame(_VSCODE_evalResult)
elif isinstance(_VSCODE_evalResult, _VSCODE_pd.Series):
    _VSCODE_df = _VSCODE_pd.Series.to_frame(_VSCODE_evalResult)
elif isinstance(_VSCODE_evalResult, dict):
    _VSCODE_evalResult = _VSCODE_pd.Series(_VSCODE_evalResult)
    _VSCODE_df = _VSCODE_pd.Series.to_frame(_VSCODE_evalResult)
elif _VSCODE_targetVariable["type"] == "ndarray":
    _VSCODE_df = _VSCODE_pd.DataFrame(_VSCODE_evalResult)
elif hasattr(_VSCODE_df, "toPandas"):
    _VSCODE_df = _VSCODE_df.toPandas()
# If not a known type, then just let pandas handle it.
elif not (hasattr(_VSCODE_df, "iloc")):
    _VSCODE_df = _VSCODE_pd.DataFrame(_VSCODE_evalResult)

# Turn into JSON using pandas. We use pandas because it's about 3 orders of magnitude faster to turn into JSON
_VSCODE_rows = _VSCODE_df.iloc[_VSCODE_startRow:_VSCODE_endRow]
_VSCODE_result = _VSCODE_pd_json.to_json(
    None, _VSCODE_rows, orient="table", date_format="iso"
)
builtins.print(_VSCODE_result)

# Cleanup our variables
del _VSCODE_df
del _VSCODE_endRow
del _VSCODE_startRow
del _VSCODE_rows
del _VSCODE_result
del _VSCODE_json
del _VSCODE_pd
del _VSCODE_pd_json
del _VSCODE_builtins
