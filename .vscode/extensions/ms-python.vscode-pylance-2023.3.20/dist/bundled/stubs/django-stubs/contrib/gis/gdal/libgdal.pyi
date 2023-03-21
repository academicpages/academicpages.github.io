from typing import Any

logger: Any
lib_path: Any
lib_names: Any
lgdal: Any
lwingdal: Any

def std_call(func: Any) -> Any: ...
def gdal_version() -> Any: ...
def gdal_full_version() -> Any: ...
def gdal_version_info() -> Any: ...

GDAL_VERSION: Any
CPLErrorHandler: Any

def err_handler(error_class: Any, error_number: Any, message: Any) -> None: ...
def function(name: Any, args: Any, restype: Any) -> Any: ...

set_error_handler: Any
