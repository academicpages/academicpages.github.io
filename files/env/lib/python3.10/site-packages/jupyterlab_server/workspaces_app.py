# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

"""A workspace management CLI"""
import json
import sys
import warnings
from pathlib import Path

from jupyter_core.application import JupyterApp
from traitlets import Bool, Unicode

from ._version import __version__
from .config import LabConfig
from .workspaces_handler import WorkspacesManager

# Default workspace ID
#  Needs to match PageConfig.defaultWorkspace define in packages/coreutils/src/pageconfig.ts
DEFAULT_WORKSPACE = "default"


class WorkspaceListApp(JupyterApp, LabConfig):
    """An app to list workspaces."""

    version = __version__
    description = """
    Print all the workspaces available

    If '--json' flag is passed in, a single 'json' object is printed.
    If '--jsonlines' flag is passed in, 'json' object of each workspace separated by a new line is printed.
    If nothing is passed in, workspace ids list is printed.
    """
    flags = dict(
        jsonlines=(
            {"WorkspaceListApp": {"jsonlines": True}},
            ("Produce machine-readable JSON Lines output."),
        ),
        json=(
            {"WorkspaceListApp": {"json": True}},
            ("Produce machine-readable JSON object output."),
        ),
    )

    jsonlines = Bool(
        False,
        config=True,
        help=(
            "If True, the output will be a newline-delimited JSON (see https://jsonlines.org/) of objects, "
            "one per JupyterLab workspace, each with the details of the relevant workspace"
        ),
    )
    json = Bool(
        False,
        config=True,
        help=(
            "If True, each line of output will be a JSON object with the "
            "details of the workspace."
        ),
    )

    def initialize(self, *args, **kwargs):
        """Initialize the app."""
        super().initialize(*args, **kwargs)
        self.manager = WorkspacesManager(self.workspaces_dir)

    def start(self):
        """Start the app."""
        workspaces = self.manager.list_workspaces()
        if self.jsonlines:
            for workspace in workspaces:
                print(json.dumps(workspace))  # noqa
        elif self.json:
            print(json.dumps(workspaces))  # noqa
        else:
            for workspace in workspaces:
                print(workspace["metadata"]["id"])  # noqa


class WorkspaceExportApp(JupyterApp, LabConfig):
    """A workspace export app."""

    version = __version__
    description = """
    Export a JupyterLab workspace

    If no arguments are passed in, this command will export the default
        workspace.
    If a workspace name is passed in, this command will export that workspace.
    If no workspace is found, this command will export an empty workspace.
    """

    def initialize(self, *args, **kwargs):
        """Initialize the app."""
        super().initialize(*args, **kwargs)
        self.manager = WorkspacesManager(self.workspaces_dir)

    def start(self):
        """Start the app."""
        if len(self.extra_args) > 1:  # pragma: no cover
            warnings.warn("Too many arguments were provided for workspace export.")
            self.exit(1)

        raw = DEFAULT_WORKSPACE if not self.extra_args else self.extra_args[0]
        try:
            workspace = self.manager.load(raw)
            print(json.dumps(workspace))  # noqa
        except Exception:  # pragma: no cover
            self.log.error(json.dumps(dict(data=dict(), metadata=dict(id=raw))))


class WorkspaceImportApp(JupyterApp, LabConfig):
    """A workspace import app."""

    version = __version__
    description = """
    Import a JupyterLab workspace

    This command will import a workspace from a JSON file. The format of the
        file must be the same as what the export functionality emits.
    """
    workspace_name = Unicode(
        None,
        config=True,
        allow_none=True,
        help="""
        Workspace name. If given, the workspace ID in the imported
        file will be replaced with a new ID pointing to this
        workspace name.
        """,
    )

    aliases = {"name": "WorkspaceImportApp.workspace_name"}

    def initialize(self, *args, **kwargs):
        """Initialize the app."""
        super().initialize(*args, **kwargs)
        self.manager = WorkspacesManager(self.workspaces_dir)

    def start(self):
        """Start the app."""
        if len(self.extra_args) != 1:  # pragma: no cover
            self.log.info("One argument is required for workspace import.")
            self.exit(1)

        with self._smart_open() as fid:
            try:  # to load, parse, and validate the workspace file.
                workspace = self._validate(fid)
            except Exception as e:  # pragma: no cover
                self.log.info(f"{fid.name} is not a valid workspace:\n{e}")
                self.exit(1)

        try:
            workspace_path = self.manager.save(workspace["metadata"]["id"], json.dumps(workspace))
        except Exception as e:  # pragma: no cover
            self.log.info(f"Workspace could not be exported:\n{e!s}")
            self.exit(1)

        self.log.info(f"Saved workspace: {workspace_path!s}")

    def _smart_open(self):
        file_name = self.extra_args[0]

        if file_name == "-":  # pragma: no cover
            return sys.stdin
        else:
            file_path = Path(file_name).resolve()

            if not file_path.exists():  # pragma: no cover
                self.log.info(f"{file_name!s} does not exist.")
                self.exit(1)

            return file_path.open(encoding="utf-8")

    def _validate(self, data):
        workspace = json.load(data)

        if "data" not in workspace:
            raise Exception("The `data` field is missing.")

        # If workspace_name is set in config, inject the
        # name into the workspace metadata.
        if self.workspace_name is not None and self.workspace_name != "":
            workspace["metadata"] = {"id": self.workspace_name}
        else:
            if "id" not in workspace["metadata"]:
                raise Exception("The `id` field is missing in `metadata`.")

        return workspace
