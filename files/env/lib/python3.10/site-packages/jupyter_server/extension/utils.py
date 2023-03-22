import importlib
import warnings


class ExtensionLoadingError(Exception):
    pass


class ExtensionMetadataError(Exception):
    pass


class ExtensionModuleNotFound(Exception):
    pass


class NotAnExtensionApp(Exception):
    pass


def get_loader(obj, logger=None):
    """Looks for _load_jupyter_server_extension as an attribute
    of the object or module.

    Adds backwards compatibility for old function name missing the
    underscore prefix.
    """
    try:
        func = getattr(obj, "_load_jupyter_server_extension")  # noqa B009
    except AttributeError:
        func = getattr(obj, "load_jupyter_server_extension", None)
        warnings.warn(
            "A `_load_jupyter_server_extension` function was not "
            "found in {name!s}. Instead, a `load_jupyter_server_extension` "
            "function was found and will be used for now. This function "
            "name will be deprecated in future releases "
            "of Jupyter Server.".format(name=obj),
            DeprecationWarning,
        )
    except Exception:
        raise ExtensionLoadingError("_load_jupyter_server_extension function was not found.")
    return func


def get_metadata(package_name, logger=None):
    """Find the extension metadata from an extension package.

    This looks for a `_jupyter_server_extension_points` function
    that returns metadata about all extension points within a Jupyter
    Server Extension pacakge.

    If it doesn't exist, return a basic metadata packet given
    the module name.
    """
    module = importlib.import_module(package_name)

    try:
        return module, module._jupyter_server_extension_points()
    except AttributeError:
        pass

    # For backwards compatibility, we temporarily allow
    # _jupyter_server_extension_paths. We will remove in
    # a later release of Jupyter Server.
    try:
        extension_points = module._jupyter_server_extension_paths()
        if logger:
            logger.warning(
                "A `_jupyter_server_extension_points` function was not "
                "found in {name}. Instead, a `_jupyter_server_extension_paths` "
                "function was found and will be used for now. This function "
                "name will be deprecated in future releases "
                "of Jupyter Server.".format(name=package_name)
            )
        return module, extension_points
    except AttributeError:
        pass

    # Dynamically create metadata if the package doesn't
    # provide it.
    if logger:
        logger.debug(
            "A `_jupyter_server_extension_points` function was "
            "not found in {name}, so Jupyter Server will look "
            "for extension points in the extension pacakge's "
            "root.".format(name=package_name)
        )
    return module, [{"module": package_name, "name": package_name}]


def validate_extension(name):
    """Raises an exception is the extension is missing a needed
    hook or metadata field.
    An extension is valid if:
    1) name is an importable Python package.
    1) the package has a _jupyter_server_extension_paths function
    2) each extension path has a _load_jupyter_server_extension function

    If this works, nothing should happen.
    """
    from .manager import ExtensionPackage

    return ExtensionPackage(name=name)
