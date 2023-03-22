import logging
import pathlib
import sys
from textwrap import dedent

import nbformat
from jupyter_core.application import JupyterApp  # type: ignore
from traitlets import Bool, Integer, List, Unicode, default
from traitlets.config import catch_config_error

from nbclient import __version__

from .client import NotebookClient

nbclient_aliases = {
    'timeout': 'NbClientApp.timeout',
    'startup_timeout': 'NbClientApp.startup_timeout',
    'kernel_name': 'NbClientApp.kernel_name',
}

nbclient_flags = {
    'allow-errors': (
        {
            'NbClientApp': {
                'allow_errors': True,
            },
        },
        "Errors are ignored and execution is continued until the end of the notebook.",
    ),
}


class NbClientApp(JupyterApp):
    """
    An application used to execute notebook files (``*.ipynb``)
    """

    version = __version__
    name = 'jupyter-execute'
    aliases = nbclient_aliases
    flags = nbclient_flags

    description = Unicode("An application used to execute notebook files (*.ipynb)")
    notebooks = List([], help="Path of notebooks to convert").tag(config=True)
    timeout: int = Integer(
        None,
        allow_none=True,
        help=dedent(
            """
            The time to wait (in seconds) for output from executions.
            If a cell execution takes longer, a TimeoutError is raised.
            ``-1`` will disable the timeout.
            """
        ),
    ).tag(config=True)
    startup_timeout: int = Integer(
        60,
        help=dedent(
            """
            The time to wait (in seconds) for the kernel to start.
            If kernel startup takes longer, a RuntimeError is
            raised.
            """
        ),
    ).tag(config=True)
    allow_errors: bool = Bool(
        False,
        help=dedent(
            """
            When a cell raises an error the default behavior is that
            execution is stopped and a `CellExecutionError`
            is raised.
            If this flag is provided, errors are ignored and execution
            is continued until the end of the notebook.
            """
        ),
    ).tag(config=True)
    skip_cells_with_tag: str = Unicode(
        'skip-execution',
        help=dedent(
            """
            Name of the cell tag to use to denote a cell that should be skipped.
            """
        ),
    ).tag(config=True)
    kernel_name: str = Unicode(
        '',
        help=dedent(
            """
            Name of kernel to use to execute the cells.
            If not set, use the kernel_spec embedded in the notebook.
            """
        ),
    ).tag(config=True)

    @default('log_level')
    def _log_level_default(self):
        return logging.INFO

    @catch_config_error
    def initialize(self, argv=None):
        super().initialize(argv)

        # Get notebooks to run
        self.notebooks = self.get_notebooks()

        # If there are none, throw an error
        if not self.notebooks:
            print(f"{self.name}: error: expected path to notebook")
            sys.exit(-1)

        # Loop and run them one by one
        [self.run_notebook(path) for path in self.notebooks]

    def get_notebooks(self):
        # If notebooks were provided from the command line, use those
        if self.extra_args:
            notebooks = self.extra_args
        # If not, look to the class attribute
        else:
            notebooks = self.notebooks

        # Return what we got.
        return notebooks

    def run_notebook(self, notebook_path):
        # Log it
        self.log.info(f"Executing {notebook_path}")

        name = notebook_path.replace(".ipynb", "")

        # Get its parent directory so we can add it to the $PATH
        path = pathlib.Path(notebook_path).parent.absolute()

        # Set the input file paths
        input_path = f"{name}.ipynb"

        # Open up the notebook we're going to run
        with open(input_path) as f:
            nb = nbformat.read(f, as_version=4)

        # Configure nbclient to run the notebook
        client = NotebookClient(
            nb,
            timeout=self.timeout,
            startup_timeout=self.startup_timeout,
            skip_cells_with_tag=self.skip_cells_with_tag,
            allow_errors=self.allow_errors,
            kernel_name=self.kernel_name,
            resources={'metadata': {'path': path}},
        )

        # Run it
        client.execute()


main = NbClientApp.launch_instance
