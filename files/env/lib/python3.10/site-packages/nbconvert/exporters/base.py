"""Module containing single call export functions."""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

import os

import entrypoints
from nbformat import NotebookNode
from traitlets.config import get_config
from traitlets.log import get_logger
from traitlets.utils.importstring import import_item

from .exporter import Exporter

# -----------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------

__all__ = [
    "export",
    "Exporter",
    "get_exporter",
    "get_export_names",
    "ExporterNameError",
]


class ExporterNameError(NameError):
    pass


class ExporterDisabledError(ValueError):
    pass


def export(exporter, nb, **kw):
    """
    Export a notebook object using specific exporter class.

    Parameters
    ----------
    exporter : ``Exporter`` class or instance
        Class or instance of the exporter that should be used.  If the
        method initializes its own instance of the class, it is ASSUMED that
        the class type provided exposes a constructor (``__init__``) with the same
        signature as the base Exporter class.
    nb : :class:`~nbformat.NotebookNode`
        The notebook to export.
    config : config (optional, keyword arg)
        User configuration instance.
    resources : dict (optional, keyword arg)
        Resources used in the conversion process.

    Returns
    -------
    tuple
        output : str
            The resulting converted notebook.
        resources : dictionary
            Dictionary of resources used prior to and during the conversion
            process.
    """

    # Check arguments
    if exporter is None:
        raise TypeError("Exporter is None")
    elif not isinstance(exporter, Exporter) and not issubclass(exporter, Exporter):
        raise TypeError("exporter does not inherit from Exporter (base)")
    if nb is None:
        raise TypeError("nb is None")

    # Create the exporter
    resources = kw.pop("resources", None)
    if isinstance(exporter, Exporter):
        exporter_instance = exporter
    else:
        exporter_instance = exporter(**kw)

    # Try to convert the notebook using the appropriate conversion function.
    if isinstance(nb, NotebookNode):
        output, resources = exporter_instance.from_notebook_node(nb, resources)
    elif isinstance(nb, (str,)):
        output, resources = exporter_instance.from_filename(nb, resources)
    else:
        output, resources = exporter_instance.from_file(nb, resources)
    return output, resources


def get_exporter(name, config=get_config()):  # noqa
    """Given an exporter name or import path, return a class ready to be instantiated

    Raises ExporterName if exporter is not found or ExporterDisabledError if not enabled
    """

    if name == "ipynb":
        name = "notebook"

    try:
        exporter = entrypoints.get_single("nbconvert.exporters", name).load()
        if getattr(exporter(config=config), "enabled", True):
            return exporter
        else:
            raise ExporterDisabledError('Exporter "%s" disabled in configuration' % (name))
    except entrypoints.NoSuchEntryPoint:
        try:
            exporter = entrypoints.get_single("nbconvert.exporters", name.lower()).load()
            if getattr(exporter(config=config), "enabled", True):
                return exporter
            else:
                raise ExporterDisabledError('Exporter "%s" disabled in configuration' % (name))
        except entrypoints.NoSuchEntryPoint:
            pass

    if "." in name:
        try:
            exporter = import_item(name)
            if getattr(exporter(config=config), "enabled", True):
                return exporter
            else:
                raise ExporterDisabledError('Exporter "%s" disabled in configuration' % (name))
        except ImportError:
            log = get_logger()
            log.error("Error importing %s" % name, exc_info=True)

    raise ExporterNameError(
        'Unknown exporter "{}", did you mean one of: {}?'.format(
            name, ", ".join(get_export_names())
        )
    )


def get_export_names(config=get_config()):  # noqa
    """Return a list of the currently supported export targets

    Exporters can be found in external packages by registering
    them as an nbconvert.exporter entrypoint.
    """
    exporters = sorted(entrypoints.get_group_named("nbconvert.exporters"))
    if os.environ.get("NBCONVERT_DISABLE_CONFIG_EXPORTERS"):
        get_logger().info(
            "Config exporter loading disabled, no additional exporters will be automatically included."
        )
        return exporters

    enabled_exporters = []
    for exporter_name in exporters:
        try:
            e = get_exporter(exporter_name)(config=config)
            if e.enabled:
                enabled_exporters.append(exporter_name)
        except (ExporterDisabledError, ValueError):
            pass
    return enabled_exporters
