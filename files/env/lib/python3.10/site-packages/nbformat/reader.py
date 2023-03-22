"""API for reading notebooks of different versions"""

# Copyright (c) IPython Development Team.
# Distributed under the terms of the Modified BSD License.

import json

from .validator import ValidationError


class NotJSONError(ValueError):
    pass


def parse_json(s, **kwargs):
    """Parse a JSON string into a dict."""
    try:
        nb_dict = json.loads(s, **kwargs)
    except ValueError as e:
        # Limit the error message to 80 characters.  Display whatever JSON will fit.
        raise NotJSONError(("Notebook does not appear to be JSON: %r" % s)[:77] + "...") from e
    return nb_dict


# High level API


def get_version(nb):
    """Get the version of a notebook.

    Parameters
    ----------
    nb : dict
        NotebookNode or dict containing notebook data.

    Returns
    -------
    Tuple containing major (int) and minor (int) version numbers
    """
    major = nb.get("nbformat", 1)
    minor = nb.get("nbformat_minor", 0)
    return (major, minor)


def reads(s, **kwargs):
    """Read a notebook from a json string and return the
    NotebookNode object.

    This function properly reads notebooks of any version.  No version
    conversion is performed.

    Parameters
    ----------
    s : unicode | bytes
        The raw string or bytes object to read the notebook from.

    Returns
    -------
    nb : NotebookNode
        The notebook that was read.

    Raises
    ------
    ValidationError
        Notebook JSON for a given version is missing an expected key and cannot be read.
    NBFormatError
        Specified major version is invalid or unsupported.
    """
    from . import NBFormatError, versions

    nb_dict = parse_json(s, **kwargs)
    (major, minor) = get_version(nb_dict)
    if major in versions:
        try:
            return versions[major].to_notebook_json(nb_dict, minor=minor)
        except AttributeError as e:
            raise ValidationError(f"The notebook is invalid and is missing an expected key: {e}")
    else:
        raise NBFormatError("Unsupported nbformat version %s" % major)


def read(fp, **kwargs):
    """Read a notebook from a file and return the NotebookNode object.

    This function properly reads notebooks of any version.  No version
    conversion is performed.

    Parameters
    ----------
    fp : file
        Any file-like object with a read method.

    Returns
    -------
    nb : NotebookNode
        The notebook that was read.
    """
    return reads(fp.read(), **kwargs)
