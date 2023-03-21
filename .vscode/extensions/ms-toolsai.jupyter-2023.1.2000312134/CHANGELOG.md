# Changelog

## Deprecated

This changelog is deprecated. Here is where you can find details about the latest updates to this extension:
- Highlighted features for the latest release are described in the VS Code release notes, under the "Contributions to extensions" section: https://code.visualstudio.com/updates
- All issues and code changes can be found by searching our Github repo under the latest milestone. [Example from November 2022](https://github.com/microsoft/vscode-jupyter/issues?q=is%3Aclosed+milestone%3A%22November+2022%22+)

## 2022.10.110 (2 November 2022)

### Enhancements

1. If a display name is specified for a remote jupyte server display that name instead of (Remote) in the kernel picker.
   ([#11381](https://github.com/Microsoft/vscode-jupyter/issues/11381))
1. Display an error message (with instructions to resolve the issue) in the cell output when attempting to run a cell against a kernel from an untrusted location.
   ([#11622](https://github.com/Microsoft/vscode-jupyter/issues/11622))
1. Make insiders kernel picker now a two step selection process that picks a source and a controller.
   ([#11642](https://github.com/Microsoft/vscode-jupyter/issues/11642))
1. Update kernel source command to use newly available NotebookDocument context from kernel picker command source.
   ([#11759](https://github.com/Microsoft/vscode-jupyter/issues/11759))

### Fixes

1. Outputs containing Plotly plots generated with the `notebook` renderer are now displayed even after re-opening this notebook in a new install of VS Code.
   ([#6404](https://github.com/Microsoft/vscode-jupyter/issues/6404))
1. Restore the command to import a notebook from the explorer context menu.
   ([#9252](https://github.com/Microsoft/vscode-jupyter/issues/9252))
1. Optimize the way stream outputs are handled, to support large output streams without crashing VS Code.
   ([#11031](https://github.com/Microsoft/vscode-jupyter/issues/11031))
1. Fully remove message asking users to try out pre-release Jupyter if they are on Insiders.
   ([#11477](https://github.com/Microsoft/vscode-jupyter/issues/11477))
1. Ensure kernel messages are handled by a cell even after cell execution completes.
   ([#11526](https://github.com/Microsoft/vscode-jupyter/issues/11526))
1. A restored Interactive Window will be re-used for code cells from the same python file.
   ([#11574](https://github.com/Microsoft/vscode-jupyter/issues/11574))
1. In the insiders kernel picker, don't prepopulate the server display name field with the URI.
   ([#11643](https://github.com/Microsoft/vscode-jupyter/issues/11643))
1. Update the "Install Python" kernel command to use the python api directly and remove controller loaded context.
   ([#11647](https://github.com/Microsoft/vscode-jupyter/issues/11647))

### Code Health

1. Adopt the new Python Extension API used to enumerate Python environments, resulting in improvements such as faster listing of Kernels in the Kernel Picker.
   ([#7583](https://github.com/Microsoft/vscode-jupyter/issues/7583))
1. Reduce the amount of work done for each code lens creation to help performance.
   ([#11433](https://github.com/Microsoft/vscode-jupyter/issues/11433))
1. Ship renderer preload scripts in the [Notebook Renderer Extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter-renderers).
   ([#11671](https://github.com/Microsoft/vscode-jupyter/issues/11671))
1. Initialize the environment variable `PYDEVD_IPYTHON_COMPATIBLE_DEBUGGING` at the point of spawning the Python kernel.
   ([#11682](https://github.com/Microsoft/vscode-jupyter/issues/11682))

### Thanks

Thanks to the following projects which we fully rely on to provide some of
our features:

-   [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
-   [debugpy](https://pypi.org/project/debugpy/)

Also thanks to the various projects we provide integrations with which help
make this extension useful:

-   [Jupyter](https://jupyter.org/):
    [Notebooks](https://jupyter-notebook.readthedocs.io/en/latest/?badge=latest),
    [JupyterHub](https://jupyterhub.readthedocs.io/en/stable/),
    [ipywidgets](https://ipywidgets.readthedocs.io/en/latest/),
    [nbconvert](https://nbconvert.readthedocs.io/en/latest/)

## 2022.9.120 (11 October 2022)
### Enhancements
1. Display an error message (with instructions to resolve the issue) in the cell output when attempting to run a cell against a kernel from an untrusted location.
   ([#11622](https://github.com/Microsoft/vscode-jupyter/issues/11622))

### Thanks

Thanks to the following projects which we fully rely on to provide some of
our features:

-   [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
-   [debugpy](https://pypi.org/project/debugpy/)

Also thanks to the various projects we provide integrations with which help
make this extension useful:

-   [Jupyter](https://jupyter.org/):
    [Notebooks](https://jupyter-notebook.readthedocs.io/en/latest/?badge=latest),
    [JupyterHub](https://jupyterhub.readthedocs.io/en/stable/),
    [ipywidgets](https://ipywidgets.readthedocs.io/en/latest/),
    [nbconvert](https://nbconvert.readthedocs.io/en/latest/)

## 2022.9.110 (11 October 2022)
### Fixes
1. Fixed vulnerability described in [CVE-2022-41083](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-41083)

### Thanks

Thanks to the following projects which we fully rely on to provide some of
our features:

-   [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
-   [debugpy](https://pypi.org/project/debugpy/)

Also thanks to the various projects we provide integrations with which help
make this extension useful:

-   [Jupyter](https://jupyter.org/):
    [Notebooks](https://jupyter-notebook.readthedocs.io/en/latest/?badge=latest),
    [JupyterHub](https://jupyterhub.readthedocs.io/en/stable/),
    [ipywidgets](https://ipywidgets.readthedocs.io/en/latest/),
    [nbconvert](https://nbconvert.readthedocs.io/en/latest/)


## 2022.9.110 (11 October 2022)
### Fixes
1. Fixed vulnerability described in [CVE-2022-41083](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-41083)

### Thanks

Thanks to the following projects which we fully rely on to provide some of
our features:

-   [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
-   [debugpy](https://pypi.org/project/debugpy/)

Also thanks to the various projects we provide integrations with which help
make this extension useful:

-   [Jupyter](https://jupyter.org/):
    [Notebooks](https://jupyter-notebook.readthedocs.io/en/latest/?badge=latest),
    [JupyterHub](https://jupyterhub.readthedocs.io/en/stable/),
    [ipywidgets](https://ipywidgets.readthedocs.io/en/latest/),
    [nbconvert](https://nbconvert.readthedocs.io/en/latest/)


## 2022.9.100 (4 October 2022)

### Enhancements

1. Add code folding regions for `# %%` cells within python files.
   ([#1527](https://github.com/Microsoft/vscode-jupyter/issues/1527))
2. Deleting a cell in the interactive window is now an undo-able operation.
   ([#7756](https://github.com/Microsoft/vscode-jupyter/issues/7756))
3. Add cell tag and slideshow editing support.
   ([#1121](https://github.com/microsoft/vscode-jupyter/issues/1121))

### Fixes

1. The cell scrolled to will be selected after using the go to cell code lens.
   ([#7687](https://github.com/Microsoft/vscode-jupyter/issues/7687))
1. Make sure the "Install Python" and "Install Python Extension" commands only show up after we have loaded our controllers.
   ([#10960](https://github.com/Microsoft/vscode-jupyter/issues/10960))
1. Ensure the cache of kernels is not updated when kernel discovery ends midway.
   ([#11240](https://github.com/Microsoft/vscode-jupyter/issues/11240))
1. Don't show unclickable links when failing to connect to a jupyter server in the web extension.
   ([#11285](https://github.com/Microsoft/vscode-jupyter/issues/11285))

### Code Health

1. Removed delayed scrolling reveal in the interactive window now that core does auto-scrolling.
   ([#7686](https://github.com/Microsoft/vscode-jupyter/issues/7686))
1. Ignore errors when disposing a kernel.
   ([#11304](https://github.com/Microsoft/vscode-jupyter/issues/11304))

### Thanks

Thanks to the following projects which we fully rely on to provide some of
our features:

-   [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
-   [debugpy](https://pypi.org/project/debugpy/)

Also thanks to the various projects we provide integrations with which help
make this extension useful:

-   [Jupyter](https://jupyter.org/):
    [Notebooks](https://jupyter-notebook.readthedocs.io/en/latest/?badge=latest),
    [JupyterHub](https://jupyterhub.readthedocs.io/en/stable/),
    [ipywidgets](https://ipywidgets.readthedocs.io/en/latest/),
    [nbconvert](https://nbconvert.readthedocs.io/en/latest/)

## 2022.8.100 (30 August 2022)

### Fixes

1. Display a prompt when Python environment used to start Jupyter cannot, providing the user with the ability to select a Python Environment.
   ([#1110](https://github.com/Microsoft/vscode-jupyter/issues/1110))
1. Start and maintain a single Python process for interrupting Python kernels (one process per session).
   ([#9909](https://github.com/Microsoft/vscode-jupyter/issues/9909))
1. Don't save an incorrect server password in our cached password list, and keep displaying the server input prompt after a failed password attempt.
   ([#10300](https://github.com/Microsoft/vscode-jupyter/issues/10300))
1. Pass `--user` flag when installing dependencies into a `Global` Python environment such as the one installed from Windows Store.
   ([#10478](https://github.com/Microsoft/vscode-jupyter/issues/10478))
1. Handle situations when the connection to a remote Kernel is lost after executing a cell.
   This also fixes the issue [Unable to interrupt a kernel when the remote kernel connection is lost [#9828](https://github.com/Microsoft/vscode-jupyter/issues/9828)](https://github.com/microsoft/vscode-jupyter/issues/9828).
   ([#10568](https://github.com/Microsoft/vscode-jupyter/issues/10568))
1. Ensure cells in Interactive Window are executed in correct order when executing from both code lenses and the input box.
   ([#10671](https://github.com/Microsoft/vscode-jupyter/issues/10671))
1. Do not append/prepend path values unnecessarily.
   ([#10906](https://github.com/Microsoft/vscode-jupyter/issues/10906))
1. Ensure user variables overriding `builtins` do not break the dataframe viewer.
   ([#10941](https://github.com/Microsoft/vscode-jupyter/issues/10941))
1. Remove duplicate `Cancel` button from modal dialog for interrupting kernels.
   ([#10999](https://github.com/Microsoft/vscode-jupyter/issues/10999))
1. Kill all of the child processes spawned by a local kernel when the kernel is shutdown.
   ([#11018](https://github.com/Microsoft/vscode-jupyter/issues/11018))
1. Initialize the environment variable `PYDEVD_IPYTHON_COMPATIBLE_DEBUGGING` for the `Python` debugger when debugging `Interactive Window` and `Notebooks`.
   This also addresses the following issues [10600](https://github.com/microsoft/vscode-jupyter/issues/10600), [10106](https://github.com/microsoft/vscode-jupyter/issues/10106)
   ([#11033](https://github.com/Microsoft/vscode-jupyter/issues/11033))
1. Ensure users can connect to `Azure ML Jupyter Server`.
   ([#11084](https://github.com/Microsoft/vscode-jupyter/issues/11084))

### Code Health

1. Stop creating hidden terminals to look for Jupyter Notebook application.
   ([#10935](https://github.com/Microsoft/vscode-jupyter/issues/10935))
1. Fix the test "Export a basic notebook document with nbconvert" CI failure.
   ([#11190](https://github.com/Microsoft/vscode-jupyter/issues/11190))
1. Fix the macOS smoke test which is failing every time on CI.
   ([#11193](https://github.com/Microsoft/vscode-jupyter/issues/11193))

### Thanks

Thanks to the following projects which we fully rely on to provide some of
our features:

-   [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
-   [debugpy](https://pypi.org/project/debugpy/)

Also thanks to the various projects we provide integrations with which help
make this extension useful:

-   [Jupyter](https://jupyter.org/):
    [Notebooks](https://jupyter-notebook.readthedocs.io/en/latest/?badge=latest),
    [JupyterHub](https://jupyterhub.readthedocs.io/en/stable/),
    [ipywidgets](https://ipywidgets.readthedocs.io/en/latest/),
    [nbconvert](https://nbconvert.readthedocs.io/en/latest/)


## 2022.7.110 (12 Aug 2022)

### Fixes

1. Ensure users can connect to `Azure ML Jupyter Server`. ([#11084](https://github.com/Microsoft/vscode-jupyter/issues/11084))

### Thanks

Thanks to the following projects which we fully rely on to provide some of
our features:

-   [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
-   [debugpy](https://pypi.org/project/debugpy/)

Also thanks to the various projects we provide integrations with which help
make this extension useful:

-   [Jupyter](https://jupyter.org/):
    [Notebooks](https://jupyter-notebook.readthedocs.io/en/latest/?badge=latest),
    [JupyterHub](https://jupyterhub.readthedocs.io/en/stable/),
    [ipywidgets](https://ipywidgets.readthedocs.io/en/latest/),
    [nbconvert](https://nbconvert.readthedocs.io/en/latest/)

## 2022.7.100 (3 Aug 2022)

### Enhancements

1. DataFrame viewer enabled on the web.
   ([#9665](https://github.com/Microsoft/vscode-jupyter/issues/9665))
1. The Variable Viewer now shows strings wrapped in single quotes.
   ([#10225](https://github.com/Microsoft/vscode-jupyter/issues/10225))
1. Rework kernel selection to be in either 'remote' mode or 'local' mode to avoid confusion about what kernels should be displayed.
   ([#10435](https://github.com/Microsoft/vscode-jupyter/issues/10435))
1. Added a more info button to the kernel depedency prompt to give more information about ipykernel.
   ([#10658](https://github.com/Microsoft/vscode-jupyter/issues/10658))
1. Use the Python Extension install python command versus just pointing at python.org.
   ([#10696](https://github.com/Microsoft/vscode-jupyter/issues/10696))
1. Only show the "kernel may need to be restarted" message when installing Python if there are active kernels.
   ([#10697](https://github.com/Microsoft/vscode-jupyter/issues/10697))
1. Added a setting 'jupyter.showOnlyOneTypeOfKernel' to allow trying out the new kernel picker UI.
   ([#10782](https://github.com/Microsoft/vscode-jupyter/issues/10782))
1. Don't show the Python getting started page when installing via the Jupyter kernel picker command.
   ([#10793](https://github.com/Microsoft/vscode-jupyter/issues/10793))

### Fixes

1. Fixes related to loading of environment variables from `.env` files ([#10359](https://github.com/Microsoft/vscode-jupyter/issues/10359), [#9774](https://github.com/Microsoft/vscode-jupyter/issues/9774), [#10392](https://github.com/Microsoft/vscode-jupyter/issues/10392), [#10755](https://github.com/Microsoft/vscode-jupyter/issues/10755)).
1. Load environment variables for Python kernels from file defined in the setting `python.envFile` ([#9691](https://github.com/Microsoft/vscode-jupyter/issues/9691)).
1. Fixes problem where clipboard permissions are required in order to enter a Jupyter server URL. (only applies when 'jupyter.showOnlyOneTypeOfKernel' is enabled)
   ([#10191](https://github.com/Microsoft/vscode-jupyter/issues/10191))
1. Fix problem of determining whether or not in 'local' or 'remote' mode for a Jupyter connection.
   ([#10363](https://github.com/Microsoft/vscode-jupyter/issues/10363))
1. Don't prompt to install python extension on just trying to check the packages that are in an interpreter.
   ([#10615](https://github.com/Microsoft/vscode-jupyter/issues/10615))
1. Ensure the extension loads in the `Safari` browser.
   ([#10621](https://github.com/Microsoft/vscode-jupyter/issues/10621))
1. Fixed localization on `package.json` sections: `capabilities`, `contributes.walkthroughs`, `contributes.commands` and `contributes.debuggers`. As well as the localizations on the exceptions thrown if the extension fails to activate and the localization on the messages for deprecated features.
   ([#10624](https://github.com/Microsoft/vscode-jupyter/issues/10624))
1. Fix language of picking a jupyter server when in the web extension.
   ([#10672](https://github.com/Microsoft/vscode-jupyter/issues/10672))
1. Change wording on 'Connect to Your Own Jupyter Server' to 'Connect to a Jupyter Server'.
   ([#10675](https://github.com/Microsoft/vscode-jupyter/issues/10675))
1. Fix error that pops up when trying to restart during debugging a notebook.
   ([#10741](https://github.com/Microsoft/vscode-jupyter/issues/10741))
1. Stop waiting for kernel to start (or be idle) when switching kernels.
   ([#10795](https://github.com/Microsoft/vscode-jupyter/issues/10795))
1. Display messages from background threads in cell outputs.
   ([#10864](https://github.com/Microsoft/vscode-jupyter/issues/10864))
1. Fixes problem with starting a kernel when ZMQ wasn't supported on Windows.
   ([#10940](https://github.com/Microsoft/vscode-jupyter/issues/10940))

### Code Health

1. Use modal dialogs in places where user input is necessary as part of a workflow.
   ([#10436](https://github.com/Microsoft/vscode-jupyter/issues/10436))
1. Load static resources for IPyWidgets from known directories as documented [here](https://docs.jupyter.org/en/latest/use/jupyter-directories.html#data-files).
   ([#10722](https://github.com/Microsoft/vscode-jupyter/issues/10722))

### Thanks

Thanks to the following projects which we fully rely on to provide some of
our features:

-   [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
-   [debugpy](https://pypi.org/project/debugpy/)

Also thanks to the various projects we provide integrations with which help
make this extension useful:

-   [Jupyter](https://jupyter.org/):
    [Notebooks](https://jupyter-notebook.readthedocs.io/en/latest/?badge=latest),
    [JupyterHub](https://jupyterhub.readthedocs.io/en/stable/),
    [ipywidgets](https://ipywidgets.readthedocs.io/en/latest/),
    [nbconvert](https://nbconvert.readthedocs.io/en/latest/)

## 2022.6.120 (14 July 2022)

### Fixes

1. Stop incorrectly looking at .python property in the python debug configuration.
   ([#10789](https://github.com/Microsoft/vscode-jupyter/issues/10789))

## 2022.6.110 (11 July 2022)

### Fixes

1. Temporarily disable localising certain phrases that would break some of the extension features while we investigate the underlying reason.
   ([#10752](https://github.com/microsoft/vscode-jupyter/issues/10752))

### Thanks

Thanks to the following projects which we fully rely on to provide some of
our features:

-   [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
-   [debugpy](https://pypi.org/project/debugpy/)

Also thanks to the various projects we provide integrations with which help
make this extension useful:

-   [Jupyter](https://jupyter.org/):
    [Notebooks](https://jupyter-notebook.readthedocs.io/en/latest/?badge=latest),
    [JupyterHub](https://jupyterhub.readthedocs.io/en/stable/),
    [ipywidgets](https://ipywidgets.readthedocs.io/en/latest/),
    [nbconvert](https://nbconvert.readthedocs.io/en/latest/)

## 2022.6.100 (6 July 2022)

### Enhancements

1. Ensure static resources required by IPyWidgets get downloaded appropriately in the Web and when using local or remote Jupyter Servers.
   ([#8834](https://github.com/Microsoft/vscode-jupyter/issues/8834))
1. Enabled export Interactive Window for web.
   ([#10291](https://github.com/Microsoft/vscode-jupyter/issues/10291))
1. Enabled expand and collapse Interactive Window cells in Web.
   ([#10524](https://github.com/Microsoft/vscode-jupyter/issues/10524))
1. For the new "Install Python Extension" command only show the modal dialog box if triggered via a running document.
   ([#10548](https://github.com/Microsoft/vscode-jupyter/issues/10548))
1. Change the logic to show our "Install Python (Extension)" commands in the kernel picker more often.
   ([#10583](https://github.com/Microsoft/vscode-jupyter/issues/10583))

### Fixes

1. Support displaying of complex outputs (such as Plots) in the Output Widget.
   ([#9503](https://github.com/Microsoft/vscode-jupyter/issues/9503))
1. Fixes to pick the correct python version when opening in the DataViewer from python debug menu.
   ([#10007](https://github.com/Microsoft/vscode-jupyter/issues/10007))
1. Ensure IPyWidgets get loaded correctly when loading resources from the CDN, Remote Jupyter or local the Python Environment.
   ([#10060](https://github.com/Microsoft/vscode-jupyter/issues/10060))
1. Fix problem with variable view not refreshing when switching between tabs.
   ([#10241](https://github.com/Microsoft/vscode-jupyter/issues/10241))
1. Fix error link clicking in the web version of the extension.
   ([#10287](https://github.com/Microsoft/vscode-jupyter/issues/10287))
1. Fixed loading of scripts related to custom IPyWidgets.
   ([#10319](https://github.com/Microsoft/vscode-jupyter/issues/10319))
1. Enable `IPyWidgets` for Kernels other than `Python`.
   ([#10330](https://github.com/Microsoft/vscode-jupyter/issues/10330))
1. Fix inconsistent link in README. Thanks @ChaseKnowlden
   ([#10396](https://github.com/Microsoft/vscode-jupyter/issues/10396))
1. Fix problem with continuous progress bar in the 'Jupyter:Variables' window by making the jupyter extension load when this view is visible.
   ([#10413](https://github.com/Microsoft/vscode-jupyter/issues/10413))
1. Fix problem with widgets being rendered offscreen and not appearing when scrolling.
   ([#10485](https://github.com/Microsoft/vscode-jupyter/issues/10485))
1. Replace 'Python 3' dummy kernel with commands to install the python extension or install python.
   ([#10513](https://github.com/Microsoft/vscode-jupyter/issues/10513))
1. Ensure we always import scripts required to load DataFrame and variable information.
   ([#10516](https://github.com/Microsoft/vscode-jupyter/issues/10516))
1. Ensure we can run Latex from within a Interactive Window cell (with a cell marker).
   ([#10531](https://github.com/Microsoft/vscode-jupyter/issues/10531))
1. Remove extra button from Restart Kernel modal. (Thanks [kilacoda](https://github.com/kilacoda))
   ([#10539](https://github.com/Microsoft/vscode-jupyter/issues/10539))
1. Add support for loading of widget scripts found within the [global Jupyter data directory](https://docs.jupyter.org/en/latest/use/jupyter-directories.html#envvar-JUPYTER_DATA_DIR).
   ([#8241](https://github.com/Microsoft/vscode-jupyter/issues/8241))
1. Set a longer timeout so that if we fail to install the Python extension for some reason we don't just wait forever.
   ([#10617](https://github.com/Microsoft/vscode-jupyter/issues/10617))
1. Expose `jQuery` in Notebook Cell outputs for IPyWidgets.
   ([#10660](https://github.com/Microsoft/vscode-jupyter/issues/10660))

### Code Health

1. Removed deprecated 'change directory on import/export' option
   ([#8752](https://github.com/Microsoft/vscode-jupyter/issues/8752))
1. Remove usage of console.log in renderers.
   ([#10202](https://github.com/Microsoft/vscode-jupyter/issues/10202))
1. Fix 'Special Token Check' test.
   ([#10565](https://github.com/Microsoft/vscode-jupyter/issues/10565))

### Thanks

Thanks to the following projects which we fully rely on to provide some of
our features:

-   [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
-   [debugpy](https://pypi.org/project/debugpy/)

Also thanks to the various projects we provide integrations with which help
make this extension useful:

-   [Jupyter](https://jupyter.org/):
    [Notebooks](https://jupyter-notebook.readthedocs.io/en/latest/?badge=latest),
    [JupyterHub](https://jupyterhub.readthedocs.io/en/stable/),
    [ipywidgets](https://ipywidgets.readthedocs.io/en/latest/),
    [nbconvert](https://nbconvert.readthedocs.io/en/latest/)

## 2022.5.100 (7 June 2022)

### Enhancements

1. Document context keys for keybinding 'when' clauses.
   ([#6573](https://github.com/Microsoft/vscode-jupyter/issues/6573))
1. Alert boxes of the form `<div style="alert alert-danger">` are now styled as colored boxes, to match how they are in Jupyter.
   (thanks [Eric Wieser](https://github.com/eric-wieser/))
   ([#8399](https://github.com/Microsoft/vscode-jupyter/issues/8399))
1. Enabled the Interactive Window in web.
   ([#9717](https://github.com/Microsoft/vscode-jupyter/issues/9717))
1. Enabled the Variables Viewer in web.
   ([#10154](https://github.com/microsoft/vscode-jupyter/pull/10154))
   However, neither the DataFrame viewer nor the Plot viewer are enabled in this release.
   (Tracking: [#9665](https://github.com/microsoft/vscode-jupyter/issues/9665))

### Fixes

1. Validate remote Jupyter Server connections when attempting to start a kernel.
   ([#8043](https://github.com/Microsoft/vscode-jupyter/issues/8043))
1. Fix to provide autocomplete inside of quoted strings. This fix also enabled a setting to allow the use of Jedi for completions in a kernel, but should be used with caution. Jedi can hang the kernel preventing exeuction from happening.
   ([#8893](https://github.com/Microsoft/vscode-jupyter/issues/8893))
1. Clear locally saved connection info when we run the server clear command.
   ([#8956](https://github.com/Microsoft/vscode-jupyter/issues/8956))
1. Ensure the format progress message disappears once export has completed.
   ([#9112](https://github.com/Microsoft/vscode-jupyter/issues/9112))
1. Notify failures in connection to remote Jupyter Server only when connecting to those kernels.
   ([#9167](https://github.com/Microsoft/vscode-jupyter/issues/9167))
1. Show the export commands for non-python notebooks.
   ([#9571](https://github.com/Microsoft/vscode-jupyter/issues/9571))
1. Makes progress indicators appear for web extension when connecting to kernels.
   ([#9784](https://github.com/Microsoft/vscode-jupyter/issues/9784))
1. Support reopening a notebook in web browser and having it remember its original kernel.
   ([#9826](https://github.com/Microsoft/vscode-jupyter/issues/9826))
1. Allow usage of the jupyter API in stable builds so Juptyer Power Toys can use it.
   ([#9868](https://github.com/Microsoft/vscode-jupyter/issues/9868))
1. Support notebook debugging in the web extension.
   ([#9973](https://github.com/Microsoft/vscode-jupyter/issues/9973))
1. Support widgets that can be downloaded from a CDN in the web extension. Non CDN widgets will come later.
   ([#9984](https://github.com/Microsoft/vscode-jupyter/issues/9984))
1. Add editor context key support into the web extension.
   ([#9990](https://github.com/Microsoft/vscode-jupyter/issues/9990))
1. Fix problem with `PYTHONNOUSERSITE` being set even when not desired. There's a setting now that will set this environment variable on kernel launch if it's needed: `jupyter.excludeUserSitePackages`.
   ([#9995](https://github.com/Microsoft/vscode-jupyter/issues/9995))
1. Don't show the python extension install ui when auto starting kernels.
   ([#10011](https://github.com/Microsoft/vscode-jupyter/issues/10011))
1. Support standard ipywidgets in the web extension.
   ([#10051](https://github.com/Microsoft/vscode-jupyter/issues/10051))
1. When connecting to a remote Jupyter server with a password you will not have to input the server URL twice to have it apply anymore.
   ([#10103](https://github.com/Microsoft/vscode-jupyter/issues/10103))
1. Fix clicking on links for error callstacks to open the same original python file instead of a new one.
   ([#10149](https://github.com/Microsoft/vscode-jupyter/issues/10149))
1. Gracefully handle failures when attempting to convert ANSI codes to HTML in large error output within the errors renderer.
   ([#10172](https://github.com/Microsoft/vscode-jupyter/issues/10172))
1. Fix 'go to source' to work again in the interactive window.
   ([#10205](https://github.com/Microsoft/vscode-jupyter/issues/10205))
1. Fixes run by line not stopping on any lines.
   ([#10207](https://github.com/Microsoft/vscode-jupyter/issues/10207))
1. Fix Jupyter: Variables hiding when closing a notebook or an interactive window.
   ([#10209](https://github.com/Microsoft/vscode-jupyter/issues/10209))
1. Fix error renderer to return tracebacks.
   ([#10239](https://github.com/Microsoft/vscode-jupyter/issues/10239))
1. Fix problem with interactive window links being off by one.
   ([#10283](https://github.com/Microsoft/vscode-jupyter/issues/10283))

### Code Health

1. Add test to make sure if the active interpreter is switched, the interactive window switches to that interpreter.
   ([#5478](https://github.com/Microsoft/vscode-jupyter/issues/5478))
1. Add tests to verify notebook metadata is in a notebook.
   ([#5601](https://github.com/Microsoft/vscode-jupyter/issues/5601))
1. Add telemetry test to verify we output a specific set for different operations.
   ([#6883](https://github.com/Microsoft/vscode-jupyter/issues/6883))
1. Added a Performance test to test and ensure expected performance characteristics.
   ([#7437](https://github.com/Microsoft/vscode-jupyter/issues/7437))
1. Don't skip code completions when the server is busy. Instead let it timeout if the server doesn't come back.
   ([#9797](https://github.com/Microsoft/vscode-jupyter/issues/9797))
1. Add test for remote https jupyter servers.
   ([#9844](https://github.com/Microsoft/vscode-jupyter/issues/9844))
1. Change document to notebook off of NotebookEditor class due to API change.
   ([#10083](https://github.com/Microsoft/vscode-jupyter/issues/10083))
1. Dataframe tests were failing when Pylance was updated to return the 'Name' column for a dataframe.
   ([#10259](https://github.com/Microsoft/vscode-jupyter/issues/10259))

### Thanks

Thanks to the following projects which we fully rely on to provide some of
our features:

-   [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
-   [debugpy](https://pypi.org/project/debugpy/)

Also thanks to the various projects we provide integrations with which help
make this extension useful:

-   [Jupyter](https://jupyter.org/):
    [Notebooks](https://jupyter-notebook.readthedocs.io/en/latest/?badge=latest),
    [JupyterHub](https://jupyterhub.readthedocs.io/en/stable/),
    [ipywidgets](https://ipywidgets.readthedocs.io/en/latest/),
    [nbconvert](https://nbconvert.readthedocs.io/en/latest/)

## 2022.4.101 (6 May 2022)

### Fixes

1. Fix regression in finding the python interpreter for viewing values in the debugger.
   ([#9928](https://github.com/Microsoft/vscode-jupyter/issues/9928))

### Thanks

Thanks to the following projects which we fully rely on to provide some of
our features:

-   [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
-   [debugpy](https://pypi.org/project/debugpy/)

Also thanks to the various projects we provide integrations with which help
make this extension useful:

-   [Jupyter](https://jupyter.org/):
    [Notebooks](https://jupyter-notebook.readthedocs.io/en/latest/?badge=latest),
    [JupyterHub](https://jupyterhub.readthedocs.io/en/stable/),
    [ipywidgets](https://ipywidgets.readthedocs.io/en/latest/),
    [nbconvert](https://nbconvert.readthedocs.io/en/latest/)

## 2022.4.100 (2 May 2022)

### Enhancements

1. Ensure widgets using IPyWidgets 8.0 get rendered correctly.
   ([#8552](https://github.com/Microsoft/vscode-jupyter/issues/8552))
1. Display a meaningful message in the cell that last ran when the kernel crashed.
   ([#9375](https://github.com/Microsoft/vscode-jupyter/issues/9375))
1. Add support for connecting to remote jupyter kernels from the web extension. The server needs to start with '--NotebookApp.allow*origin=\_baseurl*' in order to connect from a webpage.
   ([#9663](https://github.com/Microsoft/vscode-jupyter/issues/9663))

### Fixes

1. Don't append another cell to a python file when the cell was empty.
   ([#9452](https://github.com/Microsoft/vscode-jupyter/issues/9452))
1. Mark cell as not executing when dismissing the prompt to restart a dead kernel.
   ([#9538](https://github.com/Microsoft/vscode-jupyter/issues/9538))
1. Fix problem with path names in overriding modules.
   ([#9560](https://github.com/Microsoft/vscode-jupyter/issues/9560))
1. Replace `Buffer` constructors with safer methods to reduce security concerns. (Thanks [caphosra](https://github.com/caphosra))
   ([#9589](https://github.com/Microsoft/vscode-jupyter/issues/9589))
1. Ensure `raw` cells do not stay in a pending execution state.
   ([#9633](https://github.com/Microsoft/vscode-jupyter/issues/9633))
1. Only set preferred kernel on exact matches.
   ([#9685](https://github.com/Microsoft/vscode-jupyter/issues/9685))
1. Use kernel name in preferred kernel sorting algorithm.
   ([#9704](https://github.com/Microsoft/vscode-jupyter/issues/9704))
1. Make sure that notebook metadata is updating when changing between python envs (or kernelspecs) that use the same python version number.
   ([#9727](https://github.com/Microsoft/vscode-jupyter/issues/9727))
1. Fix kernels not showing up at all if remote kernel fetch fails.
   ([#9728](https://github.com/Microsoft/vscode-jupyter/issues/9728))
1. Ask for allowing unauthorized connections for https jupyter servers without certification.
   ([#9758](https://github.com/Microsoft/vscode-jupyter/issues/9758))
1. Fixes problem with crashes in the python extension preventing the jupyter extension from running.
   ([#9800](https://github.com/Microsoft/vscode-jupyter/issues/9800))
1. Fix remote kernels not being reselected on reopening a notebook.
   ([#9809](https://github.com/Microsoft/vscode-jupyter/issues/9809))
1. Fix handling of kernel errors in web extension.
   ([#9817](https://github.com/Microsoft/vscode-jupyter/issues/9817))

### Code Health

1. Finish layout of src folder into:

    - intellisense
    - interactive-window
    - kernels
    - notebooks
    - platform
    - telemetry
    - test
    - webviews
      ([#8976](https://github.com/Microsoft/vscode-jupyter/issues/8976))

1. Allow passing a Uri instead of a Notebook document to the kernel API.
   ([#9495](https://github.com/Microsoft/vscode-jupyter/issues/9495))
1. Clean up react17 reference in package.json it's not needed anymore.
   ([#9543](https://github.com/Microsoft/vscode-jupyter/issues/9543))
1. Remove events from shipping code. Not needed.
   ([#9596](https://github.com/Microsoft/vscode-jupyter/issues/9596))
1. Switch to using URIs wherever possible instead of strings for file paths.
   ([#9599](https://github.com/Microsoft/vscode-jupyter/issues/9599))
1. Remove usage of textDocumentNotebook proposed API that was unnecessary.
   ([#9679](https://github.com/Microsoft/vscode-jupyter/issues/9679))
1. Skip logging the entire server settings.
   ([#9791](https://github.com/Microsoft/vscode-jupyter/issues/9791))

### Thanks

Thanks to the following projects which we fully rely on to provide some of
our features:

-   [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
-   [debugpy](https://pypi.org/project/debugpy/)

Also thanks to the various projects we provide integrations with which help
make this extension useful:

-   [Jupyter](https://jupyter.org/):
    [Notebooks](https://jupyter-notebook.readthedocs.io/en/latest/?badge=latest),
    [JupyterHub](https://jupyterhub.readthedocs.io/en/stable/),
    [ipywidgets](https://ipywidgets.readthedocs.io/en/latest/),
    [nbconvert](https://nbconvert.readthedocs.io/en/latest/)

## 2022.3.100 (25 March 2022)

### Enhancements

### Fixes

1. Add support for named index in dataframe viewer for DataFrames and Series.
   ([#5348](https://github.com/Microsoft/vscode-jupyter/issues/5348))
1. Fix interactive window such that if a new kernel is picked when opening or the kernel is canceled, the interactive window will run with the new kernel or show the canceled state (instead of just showing no status at all).
   ([#8817](https://github.com/Microsoft/vscode-jupyter/issues/8817))
1. Fix 'ipykernel_launcher' not found when using a global python environment and '.env' file exists.
   ([#9127](https://github.com/Microsoft/vscode-jupyter/issues/9127))
1. Support conda installations that require using conda.bat instead of conda.exe on windows.
   ([#9133](https://github.com/Microsoft/vscode-jupyter/issues/9133))
1. Register kernelspecs in a private directory without cluttering user kernelspecs.
   ([#9141](https://github.com/Microsoft/vscode-jupyter/issues/9141))
1. Hide Notebook Editor icons contributed by the Jupyter extension when selecting a Kernel contributed by another extension.
   ([#9155](https://github.com/Microsoft/vscode-jupyter/issues/9155))
1. Only append SVG to the figure format if required. If not required, don't mess with the default.
   ([#9191](https://github.com/Microsoft/vscode-jupyter/issues/9191))
1. Deprecated the "Jupyter: Create new Jupyter notebook" Command since it has moved to the built-in ipynb extension in VS Code.
   ([#9250](https://github.com/Microsoft/vscode-jupyter/issues/9250))
1. Fix auto scrolling in the interactive window.
   ([#9259](https://github.com/Microsoft/vscode-jupyter/issues/9259))
1. Fix problem with double install ipykernel message when cancelling.
   ([#9267](https://github.com/Microsoft/vscode-jupyter/issues/9267))
1. Ensure the handle to the kernel connection file is disposed.
   ([#9298](https://github.com/Microsoft/vscode-jupyter/issues/9298))
1. Fix notebook intellisense to work again after recent regression.
   ([#9385](https://github.com/Microsoft/vscode-jupyter/issues/9385))
1. Fix all cells to not show a timer when queueing up multiple.
   ([#9405](https://github.com/Microsoft/vscode-jupyter/issues/9405))
1. Fixes intellisense provided by the kernel missing.
   ([#9424](https://github.com/Microsoft/vscode-jupyter/issues/9424))
1. Fixes IPyWidgets not working after refactor of source tree.
   ([#9475](https://github.com/Microsoft/vscode-jupyter/issues/9475))
1. Register platform commands.
   ([#9476](https://github.com/Microsoft/vscode-jupyter/issues/9476))

### Code Health

1. Eliminate unused parameter for concatMultilineString.
   ([#5144](https://github.com/Microsoft/vscode-jupyter/issues/5144))
1. Move installation of python packages into the Jupyter extension (stop using an API from the python extension).
   ([#8457](https://github.com/Microsoft/vscode-jupyter/issues/8457))
1. Re-use the same codeWatchers per document when providing code lenses.
   ([#8919](https://github.com/Microsoft/vscode-jupyter/issues/8919))
1. Refactor kernel related code into a 'kernels' subfolder.
   ([#8970](https://github.com/Microsoft/vscode-jupyter/issues/8970))
1. Refactor 'notebook' related code into a 'notebooks' folder.
   ([#8971](https://github.com/Microsoft/vscode-jupyter/issues/8971))
1. Move interactive window related code to its own root folder.
   ([#8972](https://github.com/Microsoft/vscode-jupyter/issues/8972))
1. Refactor client code into a 'platform' directory and organize serviceRegistry files in a hierarchical structure.
   ([#8981](https://github.com/Microsoft/vscode-jupyter/issues/8981))
1. Update to Typescript 4.6.
   ([#9173](https://github.com/Microsoft/vscode-jupyter/issues/9173))
1. Match the node version used by VS code to build.
   ([#9325](https://github.com/Microsoft/vscode-jupyter/issues/9325))
1. Remove `src\ipywidgets` from repository and move to a separate npm module.
   ([#9337](https://github.com/Microsoft/vscode-jupyter/issues/9337))

### Thanks

Thanks to the following projects which we fully rely on to provide some of
our features:

-   [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
-   [debugpy](https://pypi.org/project/debugpy/)

Also thanks to the various projects we provide integrations with which help
make this extension useful:

-   [Jupyter](https://jupyter.org/):
    [Notebooks](https://jupyter-notebook.readthedocs.io/en/latest/?badge=latest),
    [JupyterHub](https://jupyterhub.readthedocs.io/en/stable/),
    [ipywidgets](https://ipywidgets.readthedocs.io/en/latest/),
    [nbconvert](https://nbconvert.readthedocs.io/en/latest/)

## 2022.2.103 (7 March 2022)

### Fixes

1. Load environment variables defined in kernelspecs.
   ([#9171](https://github.com/Microsoft/vscode-jupyter/issues/9171))
1. Do not inherit `PYTHONNOUSERSITE` from the process running Jupyter.
   ([#9233](https://github.com/Microsoft/vscode-jupyter/issues/9233))
1. Update display names of Python Environments in kernel picker if the Python version has changed.
   ([#9104](https://github.com/Microsoft/vscode-jupyter/issues/9104))
1. Support for detection of missing dependencies in scenarios where users re-create the Python Environments (virtual env or Conda env) or for some reason manually uninstall some of the dependencies.
   ([#9135](https://github.com/Microsoft/vscode-jupyter/issues/9135))

### Thanks

Thanks to the following projects which we fully rely on to provide some of
our features:

-   [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
-   [debugpy](https://pypi.org/project/debugpy/)

Also thanks to the various projects we provide integrations with which help
make this extension useful:

-   [Jupyter](https://jupyter.org/):
    [Notebooks](https://jupyter-notebook.readthedocs.io/en/latest/?badge=latest),
    [JupyterHub](https://jupyterhub.readthedocs.io/en/stable/),
    [ipywidgets](https://ipywidgets.readthedocs.io/en/latest/),
    [nbconvert](https://nbconvert.readthedocs.io/en/latest/)

## 2022.2.102 (4 March 2022)

### Fixes

1. Ensure we detect and set the `site_packages` directory only for environments that can be activated.
   This ensures we can correctly start Python Kernels in the Python Windows Store Apps.
   ([#9219](https://github.com/Microsoft/vscode-jupyter/issues/9212))

### Thanks

Thanks to the following projects which we fully rely on to provide some of
our features:

-   [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
-   [debugpy](https://pypi.org/project/debugpy/)

Also thanks to the various projects we provide integrations with which help
make this extension useful:

-   [Jupyter](https://jupyter.org/):
    [Notebooks](https://jupyter-notebook.readthedocs.io/en/latest/?badge=latest),
    [JupyterHub](https://jupyterhub.readthedocs.io/en/stable/),
    [ipywidgets](https://ipywidgets.readthedocs.io/en/latest/),
    [nbconvert](https://nbconvert.readthedocs.io/en/latest/)

## 2022.2.101 (3 March 2022)

### Enhancements

1. When a new Conda Environment is created, refresh the list of kernels to include this new Conda environment.
   ([#8508](https://github.com/Microsoft/vscode-jupyter/issues/8508))
1. Modify command `jupyter.selectjupyteruri` to allow URI parameter.
   (Thanks [C-SELLERS](https://github.com/C-SELLERS))
   ([#8918](https://github.com/Microsoft/vscode-jupyter/issues/8918))

### Fixes

1. Add `jupyter.logKernelOutputSeparately` to expose the console logs of a kernel and or jupyter server (when we don't start a kernel directly ourselves). This option should make it easier to diagnose kernel only problems.
   ([#4954](https://github.com/Microsoft/vscode-jupyter/issues/4954))
1. Handle situations where nbconvert is installed but jupyter is not installed (our dependency installer will install both).
   ([#6838](https://github.com/Microsoft/vscode-jupyter/issues/6838))
1. Re-run the cells when changing kernels due to missing `ipykernel`.
   ([#8381](https://github.com/Microsoft/vscode-jupyter/issues/8381))
1. Support connecting to remote kernels that are busy.
   ([#8414](https://github.com/Microsoft/vscode-jupyter/issues/8414))
1. When using "Show in Data Viewer" from the python debug variables menu prompt to install pandas if it's not there already.
   ([#8423](https://github.com/Microsoft/vscode-jupyter/issues/8423))
1. Give preference to `cellId` in the cell metadata when sending cell metadata over for execution.
   ([#8761](https://github.com/Microsoft/vscode-jupyter/issues/8761))
1. Rename labels to match the new feature of allowing remote and local connections to exist simultaneously.
   ([#8780](https://github.com/Microsoft/vscode-jupyter/issues/8780))
1. Refresh the remote kernel connection count in kernels for Interactive Window.
   ([#8798](https://github.com/Microsoft/vscode-jupyter/issues/8798))
1. Do not execute startup code if there isn't any.
   ([#8879](https://github.com/Microsoft/vscode-jupyter/issues/8879))
1. Fix completions for dataframe columns.
   ([#8888](https://github.com/Microsoft/vscode-jupyter/issues/8888))
1. Provide a better message to indicate when we have no variables yet and are fetching them instead of saying no variables defined.
   ([#8898](https://github.com/Microsoft/vscode-jupyter/issues/8898))
1. Make autocomplete return faster regardless of how long pylance takes to return.
   ([#8906](https://github.com/Microsoft/vscode-jupyter/issues/8906))
1. Fix kernel dying when interrupting on Windows.
   ([#8945](https://github.com/Microsoft/vscode-jupyter/issues/8945))
1. Fix our waiting for RequestKernelInfo (might have been hurting raw kernel start some).
   ([#8989](https://github.com/Microsoft/vscode-jupyter/issues/8989))
1. Avoid waiting for completions during kernel startup (as completions request could fail without a response).
   ([#9014](https://github.com/Microsoft/vscode-jupyter/issues/9014))
1. Adopt new [`notebookKernel` contextkey](https://github.com/microsoft/vscode/pull/143163) (1.65) to prevent our interactive window toolbar from appearing on IWs belonging to other extensions.
   (Thanks [gjsjohnmurray](https://github.com/gjsjohnmurray))
   ([#9037](https://github.com/Microsoft/vscode-jupyter/issues/9037))
1. Leverage new [`notebookKernel` contextkey](https://github.com/microsoft/vscode/pull/143163) and [IW placeholder text fix](https://github.com/microsoft/vscode/pull/143211) (1.65) to prevent our interactive window `Shift+Enter` keybinding from affecting IWs belonging to other extensions.
   (Thanks [gjsjohnmurray](https://github.com/gjsjohnmurray))
   ([#9038](https://github.com/Microsoft/vscode-jupyter/issues/9038))
1. Correctly handle tilde in python traceback file path links.
   ([#9058](https://github.com/Microsoft/vscode-jupyter/issues/9058))
1. When running `shell commands`, ensure the kernel first looks for executables in Python Environment associated with the Kernel.
   E.g. commands such as `!pip` and `!python` will point to the `pip` and `python` executable associated with the kernel.
   ([#9089](https://github.com/Microsoft/vscode-jupyter/issues/9089))
1. Fix 'ipykernel_launcher' not found when using a global python environment and '.env' file exists.
   ([#9127](https://github.com/Microsoft/vscode-jupyter/issues/9127))

### Code Health

1. Add 'goto definition' test from a notebook.
   ([#5125](https://github.com/Microsoft/vscode-jupyter/issues/5125))
1. Switch to building with webpack 5.
   ([#7827](https://github.com/Microsoft/vscode-jupyter/issues/7827))

### Thanks

Thanks to the following projects which we fully rely on to provide some of
our features:

-   [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
-   [debugpy](https://pypi.org/project/debugpy/)

Also thanks to the various projects we provide integrations with which help
make this extension useful:

-   [Jupyter](https://jupyter.org/):
    [Notebooks](https://jupyter-notebook.readthedocs.io/en/latest/?badge=latest),
    [JupyterHub](https://jupyterhub.readthedocs.io/en/stable/),
    [ipywidgets](https://ipywidgets.readthedocs.io/en/latest/),
    [nbconvert](https://nbconvert.readthedocs.io/en/latest/)

## 2022.1.120 (January Release on 11 February 2022)

### Fixes

1. Fix daemon startup to work for non direct kernel cases
   ([#8995](https://github.com/Microsoft/vscode-jupyter/issues/8995))
1. Fix our waiting for RequestKernelInfo (might have been hurting raw kernel start some).
   ([#8989](https://github.com/Microsoft/vscode-jupyter/issues/8989))

### Thanks

Thanks to the following projects which we fully rely on to provide some of
our features:

-   [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
-   [debugpy](https://pypi.org/project/debugpy/)

Also thanks to the various projects we provide integrations with which help
make this extension useful:

-   [Jupyter](https://jupyter.org/):
    [Notebooks](https://jupyter-notebook.readthedocs.io/en/latest/?badge=latest),
    [JupyterHub](https://jupyterhub.readthedocs.io/en/stable/),
    [ipywidgets](https://ipywidgets.readthedocs.io/en/latest/),
    [nbconvert](https://nbconvert.readthedocs.io/en/latest/)

## 2022.1.110 (January Release on 09 February 2022)

### Fixes

1. Fix kernel dying when interrupting on Windows.
   ([#8945](https://github.com/Microsoft/vscode-jupyter/issues/8945))

### Thanks

Thanks to the following projects which we fully rely on to provide some of
our features:

-   [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
-   [debugpy](https://pypi.org/project/debugpy/)

Also thanks to the various projects we provide integrations with which help
make this extension useful:

-   [Jupyter](https://jupyter.org/):
    [Notebooks](https://jupyter-notebook.readthedocs.io/en/latest/?badge=latest),
    [JupyterHub](https://jupyterhub.readthedocs.io/en/stable/),
    [ipywidgets](https://ipywidgets.readthedocs.io/en/latest/),
    [nbconvert](https://nbconvert.readthedocs.io/en/latest/)

## 2022.1.100 (January Release on 03 February 2022)

### Enhancements

1. Reloading VS Code is no longer necessary when switching between local and remote Jupyter servers.
   ([#1367](https://github.com/Microsoft/vscode-jupyter/issues/1367))
1. Expose Jupyter Kernel API to 3rd party extensions.
   This API is still in preview and only available in VS Code Insiders, further information can be found here https://github.com/microsoft/vscode-jupyter/wiki/Accessing-Jupyter-Kernels-from-3rd-party-extensions.
   ([#5532](https://github.com/Microsoft/vscode-jupyter/issues/5532))
1. Recommend using `%matplotlib widget` when any other `%matplotlib` choice is set.
   ([#8365](https://github.com/Microsoft/vscode-jupyter/issues/8365))
1. Be able to retrieve XSRF token with session cookie from notebook server on Kubeflow. (@shawnzhu)
   ([#8441](https://github.com/Microsoft/vscode-jupyter/issues/8441))
1. Add support for pre-release version of Extensions for VS Code Insiders.
   ([#8463](https://github.com/Microsoft/vscode-jupyter/issues/8463))
1. Allow to retrieve the jupyter filename programmatically (**vsc_ipynb_file**) [fix support for ClearML](https://github.com/Microsoft/vscode-jupyter/blob/HEAD/<[#8475](https:/github.com/Microsoft/vscode-jupyter/issues/8475)>)
1. Display both local and remote kernels together in the kernel picker.
   ([#8489](https://github.com/Microsoft/vscode-jupyter/issues/8489))

### Fixes

1. Install `IPyKernel` without a terminal when dealing with `Virtual Environments` on windows.
   ([#1253](https://github.com/Microsoft/vscode-jupyter/issues/1253))
1. Use the appropriate directory for a notebook if remoting to 'localhost'
   ([#1551](https://github.com/Microsoft/vscode-jupyter/issues/1551))
1. Fix VS code leaving kernel processes running during shutdown.
   ([#1626](https://github.com/Microsoft/vscode-jupyter/issues/1626))
1. Deprecate "Change Directory on Import Export Setting"
   ([#4419](https://github.com/Microsoft/vscode-jupyter/issues/4419))
1. Fix plot viewer so that plots are full size when opening.
   ([#7523](https://github.com/Microsoft/vscode-jupyter/issues/7523))
1. Support viewing dataframes (in the dataframe viewer) that contain columns used as an index.
   ([#7603](https://github.com/Microsoft/vscode-jupyter/issues/7603))
1. Support automatic reconnection to a remote kernel when reopening a notebook.
   ([#7610](https://github.com/Microsoft/vscode-jupyter/issues/7610))
1. Fix completions for paths for notebooks so that you can keep tabbing through all entries. This used to stop after the first level.
   ([#7816](https://github.com/Microsoft/vscode-jupyter/issues/7816))
1. Prevent variables from getting stuck in the Loading... state after restart.
   ([#7970](https://github.com/Microsoft/vscode-jupyter/issues/7970))
1. Allow queueing of multiple cells in the interactive window.
   ([#8022](https://github.com/Microsoft/vscode-jupyter/issues/8022))
1. Correctly handle leading spaces in cells when debugging with the interactive window.
   ([#8263](https://github.com/Microsoft/vscode-jupyter/issues/8263))
1. Support intellisense after connecting to a remote server (defaults to active python interpreter)
   ([#8285](https://github.com/Microsoft/vscode-jupyter/issues/8285))
1. Make run file in interactive window respect cell boundaries.
   ([#8312](https://github.com/Microsoft/vscode-jupyter/issues/8312))
1. Get `%matplotlib qt5` working again.
   QT5's event loop is slightly different and can't handle concurrent requests so make sure to wait for a request before issuing another.
   ([#8322](https://github.com/Microsoft/vscode-jupyter/issues/8322))
1. Fix problems when 'print' has been overridden by user code.
   ([#8356](https://github.com/Microsoft/vscode-jupyter/issues/8356))
1. Ensure interactive IPyWidgets work even after restarting Remote Kernels.
   ([#8378](https://github.com/Microsoft/vscode-jupyter/issues/8378))
1. Continue attempting to create a kernel for the IW if it failed to start previously
   ([#8383](https://github.com/Microsoft/vscode-jupyter/issues/8383))
1. Fix intellisense to work when no folder is opened.
   ([#8409](https://github.com/Microsoft/vscode-jupyter/issues/8409))
1. Fix intellisense after deleting a line from a cell that contains the word 'await' or a magic.
   ([#8419](https://github.com/Microsoft/vscode-jupyter/issues/8419))
1. Set suggested kernel for interactive window correctly.
   ([#8424](https://github.com/Microsoft/vscode-jupyter/issues/8424))
1. Fix semantic colorization in the first cell of a notebook.
   ([#8437](https://github.com/Microsoft/vscode-jupyter/issues/8437))
1. Context key not updated when interactive window is created from command palette.
   ([#8455](https://github.com/Microsoft/vscode-jupyter/issues/8455))
1. Autocompletions from the jupyter kernel can sometimes not appear.
   ([#8536](https://github.com/Microsoft/vscode-jupyter/issues/8536))
1. Fix problem with markdown cells in the interactive window not being split if they have code in them too.
   ([#8543](https://github.com/Microsoft/vscode-jupyter/issues/8543))
1. Fix conda environments not working when ZMQ support is not enabled.
   Ensure `sys.path` is setup such that packages installed in selected environments is given preference (imported) over global site-packages.
   I.e. this fix will ensure packages are first imported from the selected environment, and then from the global site-packages.
   ([#8553](https://github.com/Microsoft/vscode-jupyter/issues/8553))
1. Apply correct resource settings to notebookFileRoot in multi-root workspaces.
   ([#8561](https://github.com/Microsoft/vscode-jupyter/issues/8561))
1. Fix problem where error stack traces would show random code that hadn't actually been run.
   ([#8568](https://github.com/Microsoft/vscode-jupyter/issues/8568))
1. Fix caching of conda environment data so that subsequent runs of conda kernels are faster.
   ([#8580](https://github.com/Microsoft/vscode-jupyter/issues/8580))
1. Allows execution in more than one interactive window at the same time.
   ([#8615](https://github.com/Microsoft/vscode-jupyter/issues/8615))
1. Don't ask the user to enable CDN widget sources if they are already enabled and add more information to the warning message when we fail to download the widget.
   ([#8626](https://github.com/Microsoft/vscode-jupyter/issues/8626))
1. Fix traceback parsing when using IPython 8.0 or greater.
   ([#8675](https://github.com/Microsoft/vscode-jupyter/issues/8675))
1. Expand ~ in notebookFileRoot setting.
   ([#8679](https://github.com/Microsoft/vscode-jupyter/issues/8679))
1. Fix launching kernel on Mac M1 (or zmq not supported) using default environment.
   ([#8681](https://github.com/Microsoft/vscode-jupyter/issues/8681))
1. Fix the interactive debugging tests to shut down debugging correctly at the end.
   ([#8684](https://github.com/Microsoft/vscode-jupyter/issues/8684))
1. Fix error tracebacks to not have background colors. Background colors from Jupyter don't match VS code themes, so they were just removed.
   ([#8697](https://github.com/Microsoft/vscode-jupyter/issues/8697))
1. Fix prompting to switch to prerelease even when already on prerelease.
   ([#8724](https://github.com/Microsoft/vscode-jupyter/issues/8724))
1. Fix problem with markdown cells causing off by one errors in notebooks.
   ([#8769](https://github.com/Microsoft/vscode-jupyter/issues/8769))
1. Fix for intellisense breaking after typing a magic into a cell other than the first.
   ([#8830](https://github.com/Microsoft/vscode-jupyter/issues/8830))

### Code Health

1. Refactor any code using a string for a file path to support a URI instead. This should make remote file systems work better.
   ([#1420](https://github.com/Microsoft/vscode-jupyter/issues/1420))
1. Make sure submissions include a news file.
   ([#3200](https://github.com/Microsoft/vscode-jupyter/issues/3200))
1. Consolidate requirements.txt files into a smaller set.
   ([#3992](https://github.com/Microsoft/vscode-jupyter/issues/3992))
1. Change error message prompting user to install IPykernel into an information message.
   ([#8415](https://github.com/Microsoft/vscode-jupyter/issues/8415))
1. Display modal dialog when attempting to run Python notebooks without the Python extension installed.
   ([#8416](https://github.com/Microsoft/vscode-jupyter/issues/8416))
1. Display error message when failing to connect to the remote Jupyter server.
   ([#8474](https://github.com/Microsoft/vscode-jupyter/issues/8474))
1. Remove `jupyter.runMagicCommands` (which has been deprecated for over a year) in favor of `runStartupCommands`.
   ([#8485](https://github.com/Microsoft/vscode-jupyter/issues/8485))
1. Activate `conda` environments using `conda run`.
   ([#8544](https://github.com/Microsoft/vscode-jupyter/issues/8544))
1. Improvements to progress message displayed when starting kernels. The messages now attempt to provide more information about the progress and hopefully make it easier to understand what is going on (or what is slow when starting a kernel).
   ([#8583](https://github.com/Microsoft/vscode-jupyter/issues/8583))
1. Update README.md to remove insiders specific references.
   ([#8548](https://github.com/Microsoft/vscode-jupyter/issues/8548))

### Thanks

Thanks to the following projects which we fully rely on to provide some of
our features:

-   [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
-   [debugpy](https://pypi.org/project/debugpy/)

Also thanks to the various projects we provide integrations with which help
make this extension useful:

-   [Jupyter](https://jupyter.org/):
    [Notebooks](https://jupyter-notebook.readthedocs.io/en/latest/?badge=latest),
    [JupyterHub](https://jupyterhub.readthedocs.io/en/stable/),
    [ipywidgets](https://ipywidgets.readthedocs.io/en/latest/),
    [nbconvert](https://nbconvert.readthedocs.io/en/latest/)

VS Code Stable releases along with the minimum recommended version of the Jupyter Extension.

| Release   | VS Code Stable | Recommended Jupyter Build |
| --------- | -------------- | ------------------------- |
| November  | 1.63.0         | **2021.11.100**1550889    |
| October   | 1.62.0         | **2021.10.100**1414422    |
| September | 1.61.2         | **2021.9.110**1343141     |
| August    | 1.60.2         | **2021.8.204**1215044     |
| July      | 1.59.1         | **2021.8.123**6758218     |
| June      | 1.58.2         | **2021.8.105**4968649     |

## 2021.11.100 (November Release on 8 December 2021)

### Enhancements

1. Performance improvements related to startup of Kernels.
    - Support pre-warming Kernels to improve startup experience of Notebooks. ([#7903](https://github.com/microsoft/vscode-jupyter/issues/7903))
    - Faster activation of Python environments such as Conda. ([#8342](https://github.com/microsoft/vscode-jupyter/pull/8342))
    - Avoid starting default kernel when starting jupyter. ([#8185](https://github.com/microsoft/vscode-jupyter/issues/8185))
    - Avoid looking for IPyKernel when we've found it once before. ([#8196](https://github.com/microsoft/vscode-jupyter/issues/8196))
    - Avoid unnecessarily searching for `Jupyter` packages when `Jupyter` runtime isnt' rqeuired to start Kernels. ([#8350](https://github.com/microsoft/vscode-jupyter/issues/8350))
      ([#8352](https://github.com/Microsoft/vscode-jupyter/issues/8352))
1. Add diagnostics messages recommending the usage of `%pip install` & `%conda install` over `!pip install`.
   ([#6864](https://github.com/Microsoft/vscode-jupyter/issues/6864))
1. Prompt and install `pip` if `pip` is not available when installing missing dependencies such as `ipykernel`.
   ([#7739](https://github.com/Microsoft/vscode-jupyter/issues/7739))
1. Add support for interrupting non-python kernels.
   ([#8107](https://github.com/Microsoft/vscode-jupyter/issues/8107))
1. Support iPyWidgets when connecting to an existing (already running) remote kernel.
   ([#8179](https://github.com/Microsoft/vscode-jupyter/issues/8179))
1. Identify and recommend renaming user created python files that overwrite builtins and cause Kernels to crash (or not start at all).
   ([#8195](https://github.com/Microsoft/vscode-jupyter/issues/8195))
1. Recommend updating `traitlets` to `5.1.1` if `jupyter` fails to start.
   ([#8295](https://github.com/Microsoft/vscode-jupyter/issues/8295))
1. Attempt to pip install Data Science packages such as `ipykernel` outside a terminal when dealing with Global Python Environments.
   ([#8325](https://github.com/Microsoft/vscode-jupyter/issues/8325))
1. Display kernel startup failure messages in cell outputs for improved visibility.
   ([#8351](https://github.com/Microsoft/vscode-jupyter/issues/8351))
1. Improvements to error messages displayed when Kernel startup fails.
   ([#8354](https://github.com/Microsoft/vscode-jupyter/issues/8354))
1. Warn when using outdated versions of Python (Python 2.7 & the like).
   ([#7960](https://github.com/Microsoft/vscode-jupyter/issues/7960))

### Fixes

1. Top level awaits in a notebook cell should not cause an error to be shown.
   ([#1510](https://github.com/Microsoft/vscode-jupyter/issues/1510))
1. Cancel active kernel startup when switching to another kernel.
   ([#5896](https://github.com/Microsoft/vscode-jupyter/issues/5896))
1. Fix highlighting of elements in a cell.
   ([#5932](https://github.com/Microsoft/vscode-jupyter/issues/5932))
1. For interactive window commands (run all, run above, run below) add them to a queue instead of just trying to execute one by one.
   ([#6982](https://github.com/Microsoft/vscode-jupyter/issues/6982))
1. Fix completions to skip file names when not inside of a string.
   ([#7136](https://github.com/Microsoft/vscode-jupyter/issues/7136))
1. Fix regression to show "Show in Data Viewer" option from nested variables in the debug variables view.
   ([#7295](https://github.com/Microsoft/vscode-jupyter/issues/7295))
1. Eliminate duplicate content in jupyter completions.
   ([#7772](https://github.com/Microsoft/vscode-jupyter/issues/7772))
1. Make jupyter kernel autocomplete less aggressive and customizable. The new 'jupyter.completionTriggerCharacters' can be used to determine what causes a kernel to return completions.
   ([#7880](https://github.com/Microsoft/vscode-jupyter/issues/7880))
1. Make 'Jupyter: Export interactive as Jupyter notebook' command work.
   ([#7947](https://github.com/Microsoft/vscode-jupyter/issues/7947))
1. Let code in 'jupyter.runStartupCommands' work with intellisense.
   For example, if your startup commands were 'import pandas as pd', auto completion would now work automatically for 'pd.' without having to type the import first.
   ([#7993](https://github.com/Microsoft/vscode-jupyter/issues/7993))
1. Allow for nbconvert export when a global jupyter interpreter has not been set before.
   ([#8050](https://github.com/Microsoft/vscode-jupyter/issues/8050))
1. Eliminate extra long labels in jupyter completions.
   ([#8080](https://github.com/Microsoft/vscode-jupyter/issues/8080))
1. Fixes related to handling of carriage returns in outputs.
   ([#8112](https://github.com/Microsoft/vscode-jupyter/issues/8112))
1. Make the import ipynb commands use the currently selected pythonExportMethod setting.
   ([#8158](https://github.com/Microsoft/vscode-jupyter/issues/8158))
1. Display notebook paths associated with remote kernels in the kernel picker.
   ([#8175](https://github.com/Microsoft/vscode-jupyter/issues/8175))
1. Do not prompt to install Python extension when opening a `.NET` notebook.
   ([#8204](https://github.com/Microsoft/vscode-jupyter/issues/8204))
1. Turn off telemetry for tracking the number of notebooks in a workspace.
   ([#8293](https://github.com/Microsoft/vscode-jupyter/issues/8293))
1. Recommend installing `traitlets` version `5.1.1` if Jupyter fails to start and the version of `traitlets` is older.
   ([#8295](https://github.com/Microsoft/vscode-jupyter/issues/8295))
1. Fix interactive window intellisense to work after new concat changes for notebook intellisense.
   ([#8353](https://github.com/Microsoft/vscode-jupyter/issues/8353))
1. Fix intellisense problems after editing notebook cells.
   ([#8374](https://github.com/Microsoft/vscode-jupyter/issues/8374))
1. Ensure interactive widgets work when connecting to remote Jupyter (or when falling back to starting Jupyter locally).
   ([#8378](https://github.com/Microsoft/vscode-jupyter/issues/8378))

### Code Health

1. Make sure interrupt during run by line is tested.
   ([#8002](https://github.com/Microsoft/vscode-jupyter/issues/8002))
1. Add setting to allow usage of experimental pylance intellisense in notebooks.
   ([#8096](https://github.com/Microsoft/vscode-jupyter/issues/8096))

### Thanks

Thanks to the following projects which we fully rely on to provide some of
our features:

-   [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
-   [debugpy](https://pypi.org/project/debugpy/)

Also thanks to the various projects we provide integrations with which help
make this extension useful:

-   [Jupyter](https://jupyter.org/):
    [Notebooks](https://jupyter-notebook.readthedocs.io/en/latest/?badge=latest),
    [JupyterHub](https://jupyterhub.readthedocs.io/en/stable/),
    [ipywidgets](https://ipywidgets.readthedocs.io/en/latest/),
    [nbconvert](https://nbconvert.readthedocs.io/en/latest/)

## 2021.10.100 (October Release on 3 November 2021)

### Enhancements

1. Group kernels in kernel picker based on the type of the Python environment & kernel.
   ([#7934](https://github.com/microsoft/vscode-jupyter/issues/7934))
1. Add ability to filter kernels displayed in the kernel picker.
   ([#7373](https://github.com/microsoft/vscode-jupyter/issues/7373))
1. Add ability to not generate a new cell when hitting SHIFT+ENTER in a python file.
   (Thanks [janosh](https://github.com/janosh))
   ([#7966](https://github.com/Microsoft/vscode-jupyter/issues/7966))

### Fixes

1. New default export that just uses conversion in typescript as opposed to nbconvert. Allow the option to comment out magics or use the old nbconvert style of export via a setting.
   ([#5222](https://github.com/Microsoft/vscode-jupyter/issues/5222))
1. Track the active kernel in a notebook when providing intellisense.
   ([#6333](https://github.com/Microsoft/vscode-jupyter/issues/6333))
1. Hide Jupyter specific toolbar icons from notebooks.
   ([#6543](https://github.com/Microsoft/vscode-jupyter/issues/6543))
1. Fix notebooks opening and being marked as dirty on every open.
   ([#6637](https://github.com/Microsoft/vscode-jupyter/issues/6637))
1. Fix semantic colorization in notebooks.
   ([#6799](https://github.com/Microsoft/vscode-jupyter/issues/6799))
1. Close input prompts displayed by kernel when interrupting/restarting kernels.
   ([#6897](https://github.com/Microsoft/vscode-jupyter/issues/6897))
1. Delete all of the old kernelspecs generated by the extension (as some were incorrectly generated), with the ability to manually recover them if necessary.
   ([#7171](https://github.com/Microsoft/vscode-jupyter/issues/7171))
1. Support using the variable viewer when a data viewer window is open.
   ([#7325](https://github.com/Microsoft/vscode-jupyter/issues/7325))
1. Changes to how we check if kernels have started (as a result now suppor kernels such as [Wolfram](https://github.com/WolframResearch/WolframLanguageForJupyter)).
   ([#7334](https://github.com/Microsoft/vscode-jupyter/issues/7334))
1. Allow intellisense completions from Jupyter to be shown in the interactive window.
   ([#7406](https://github.com/Microsoft/vscode-jupyter/issues/7406))
1. Change filtering for text data in the data viewer to search for any instance of a string unless regular expression chars are detected. If any regular expression chars are detected, switch to using regular expressions to match.
   ([#7628](https://github.com/Microsoft/vscode-jupyter/issues/7628))
1. Fix debugging from the interactive window.
   ([#7650](https://github.com/Microsoft/vscode-jupyter/issues/7650))
1. Specifying a jupyter command line only makes sense if we need to use jupyter to launch kernels (no ZMQ support).
   ([#7724](https://github.com/Microsoft/vscode-jupyter/issues/7724))
1. Don't make the outline button and command dependent on if the outline view is visible.
   ([#7766](https://github.com/Microsoft/vscode-jupyter/issues/7766))
1. Incorrect paths displayed for non-python kernels in kernel picker.
   ([#7931](https://github.com/Microsoft/vscode-jupyter/issues/7931))
1. Group kernels in by kernel picker by Python environment type (prefix non-python kernels with `Jupyter Kernel`).
   ([#7934](https://github.com/Microsoft/vscode-jupyter/issues/7934))
1. Fix build break in ipywidget build. (thanks [ChaseKnowlden](https://github.com/ChaseKnowlden))
   ([#7935](https://github.com/Microsoft/vscode-jupyter/issues/7935))
1. Ensure `__file__` is set when changing kernels in Interactive Window.
   ([#7941](https://github.com/Microsoft/vscode-jupyter/issues/7941))
1. Interactive window is not necessarily using active interpreter when creating the controller.
   ([#7945](https://github.com/Microsoft/vscode-jupyter/issues/7945))
1. Improve performance of widgets over remote connections. (thanks [sdissegna-maystreet](https://github.com/sdissegna-maystreet))
   ([#7965](https://github.com/Microsoft/vscode-jupyter/issues/7965))
1. Remove duplicates from kernel picker & ensure globally registered kernels point to the right interpreter.
   ([#7994](https://github.com/Microsoft/vscode-jupyter/issues/7994))
1. Ensure kernel language is defined in the `ipynb` metadata.
   ([#8003](https://github.com/Microsoft/vscode-jupyter/issues/8003))
1. Change 'Stop' for debugging in the interactive window to interrupt the execution so it actually stops as soon as possible.
   ([#8069](https://github.com/Microsoft/vscode-jupyter/issues/8069))
1. Avoid losing ipywidgets kernel communications when switching kernel. (thanks [sdissegna-maystreet](https://github.com/sdissegna-maystreet))
   ([#8085](https://github.com/Microsoft/vscode-jupyter/issues/8085))

### Code Health

1. Replace instances of `traceInfoIf` with `traceInfoIfCI` as almost all of them were just for CI tracing.
   ([#7574](https://github.com/Microsoft/vscode-jupyter/issues/7574))
1. Upgrade to the latest jupyterlab/services API for communicating with kernels and jupyter servers.
   ([#7675](https://github.com/Microsoft/vscode-jupyter/issues/7675))
1. Get rid of unnecessary 'Open with Notebook Editor' command as this is built into VS code itself.
   ([#7725](https://github.com/Microsoft/vscode-jupyter/issues/7725))

### Thanks

Thanks to the following projects which we fully rely on to provide some of
our features:

-   [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
-   [debugpy](https://pypi.org/project/debugpy/)

Also thanks to the various projects we provide integrations with which help
make this extension useful:

-   [Jupyter](https://jupyter.org/):
    [Notebooks](https://jupyter-notebook.readthedocs.io/en/latest/?badge=latest),
    [JupyterHub](https://jupyterhub.readthedocs.io/en/stable/),
    [ipywidgets](https://ipywidgets.readthedocs.io/en/latest/),
    [nbconvert](https://nbconvert.readthedocs.io/en/latest/)

## 2021.9.110 (September Release on 14 October 2021)

### Fixes

1. Ensure `Change Kernel` option in the prmopt allows users to change kernels.
   ([#7779](https://github.com/Microsoft/vscode-jupyter/issues/7779))
1. Ensure restarting kernels in `Interactive Window` retains support for `__file__`.
   ([#7883](https://github.com/Microsoft/vscode-jupyter/issues/7883))

### Thanks

Thanks to the following projects which we fully rely on to provide some of
our features:

-   [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
-   [debugpy](https://pypi.org/project/debugpy/)

Also thanks to the various projects we provide integrations with which help
make this extension useful:

-   [Jupyter](https://jupyter.org/):
    [Notebooks](https://jupyter-notebook.readthedocs.io/en/latest/?badge=latest),
    [JupyterHub](https://jupyterhub.readthedocs.io/en/stable/),
    [ipywidgets](https://ipywidgets.readthedocs.io/en/latest/),
    [nbconvert](https://nbconvert.readthedocs.io/en/latest/)

## 2021.9.100 (September Release on 6 October 2021)

### Enhancements

1. Split Notebook renderers into a separate extension ([Jupyter Notebook Renderers](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter-renderers)), allowing users to view Notebook outputs such as plotly, vega on [github.dev](https://github.dev).
   ([#1909](https://github.com/Microsoft/vscode-jupyter/issues/1909))
1. Added support to use Run by Line and Notebook Debugging in remote kernels.
   ([#7576](https://github.com/Microsoft/vscode-jupyter/issues/7576))
1. Added ability to create notebooks using the menu option `File -> New File...`.
   ([#7363](https://github.com/Microsoft/vscode-jupyter/issues/7363))
1. Added a command to the command palette and an icon to the notebook toolbar to open the the table of contents for Notebooks.
   ([#7305](https://github.com/microsoft/vscode-jupyter/issues/7305))

### Fixes

1. Strip CR from CRLF of source when sending code to the kernel for execution.
   ([#4576](https://github.com/Microsoft/vscode-jupyter/issues/4576))
1. Show global Python kernel specs that use ipykernel to launch.
   ([#6389](https://github.com/Microsoft/vscode-jupyter/issues/6389))
1. Fixes related to remote connections in `Interactive Window`.
   ([#6881](https://github.com/Microsoft/vscode-jupyter/issues/6881))
1. Fixes to restarting of kernels when kernel dies (as opposed to manually restarting a kernel).
   ([#7167](https://github.com/Microsoft/vscode-jupyter/issues/7167))
1. Code cell submissions should go to active window in 'multiple' mode.
   ([#7249](https://github.com/Microsoft/vscode-jupyter/issues/7249))
1. Interrupt kernel button on interactive window toolbar should be disabled when kernel is not busy.
   ([#7269](https://github.com/Microsoft/vscode-jupyter/issues/7269))
1. Fix 'Connecting to...' message in interactive window not being updated in-place if a code cell is inserted before the connection completes.
   ([#7280](https://github.com/Microsoft/vscode-jupyter/issues/7280))
1. Fix changing kernel in interactive windows started with an interpreter that does not have ipykernel installed.
   ([#7288](https://github.com/Microsoft/vscode-jupyter/issues/7288))
1. Preserve leading tab characters on code lines for #%% cells submitted to interactive window.
   ([#7303](https://github.com/Microsoft/vscode-jupyter/issues/7303))
1. Display error message from Python stack trace when kernel dies (also if kernel dies when attempting to restart).
   ([#7318](https://github.com/Microsoft/vscode-jupyter/issues/7318))
1. Don't add an extra linefeed in interactive window markdown.
   ([#7355](https://github.com/Microsoft/vscode-jupyter/issues/7355))
1. Fix Debug Cell codelens opening the wrong source file after restarting the kernel in the interactive window.
   ([#7366](https://github.com/Microsoft/vscode-jupyter/issues/7366))
1. Refresh list of remote kernels if a notebook is already open.
   ([#7385](https://github.com/Microsoft/vscode-jupyter/issues/7385))
1. Fix allowing the dataframe viewer to open large data frames. Also fix variable fetching code from updating the execution count.
   ([#7420](https://github.com/Microsoft/vscode-jupyter/issues/7420))
1. Apply background to the image element in a notebook output, instead of applying it to the entire output container.
   ([#7470](https://github.com/Microsoft/vscode-jupyter/issues/7470))
1. Support retina output option for Matplotlib.
   ([#7471](https://github.com/Microsoft/vscode-jupyter/issues/7471))
1. Clicking 'Change Kernel' for interactive window started from script file when ipykernel is not installed should display the kernel picker.
   ([#7476](https://github.com/Microsoft/vscode-jupyter/issues/7476))
1. Fix `jupyter.magicCommandsAsComments` when executing code cells in the interactive window.
   ([#7481](https://github.com/Microsoft/vscode-jupyter/issues/7481))
1. `jupyter.interactive.removeCell` now supports being invoked from the command palette or with a custom keybinding when an interactive window has focus.
   ([#7541](https://github.com/Microsoft/vscode-jupyter/issues/7541))
1. Fix the context keys for the variable explorer when working with the interactive window.
   ([#7556](https://github.com/Microsoft/vscode-jupyter/issues/7556))
1. Ensure empty #%% cells are skipped and do not interfere with running of subsequent cells in the interactive window.
   ([#7581](https://github.com/Microsoft/vscode-jupyter/issues/7581))
1. Fix interactive window debugging sourcemap resolution after running a markdown cell.
   ([#7589](https://github.com/Microsoft/vscode-jupyter/issues/7589))
1. Support a highlight around a cell when goto cell is clicked in the interactive window.
   ([#7648](https://github.com/Microsoft/vscode-jupyter/issues/7648))
1. Support multiline comments in the middle of a cell being submitted to the interactive window.
   ([#7658](https://github.com/Microsoft/vscode-jupyter/issues/7658))

### Code Health

1. Basic test for plotviewer metadata and SVG setting.
   ([#7209](https://github.com/Microsoft/vscode-jupyter/issues/7209))
1. Fix failing variable view tests.
   ([#7443](https://github.com/Microsoft/vscode-jupyter/issues/7443))

### Thanks

Thanks to the following projects which we fully rely on to provide some of
our features:

-   [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
-   [debugpy](https://pypi.org/project/debugpy/)

Also thanks to the various projects we provide integrations with which help
make this extension useful:

-   [Jupyter](https://jupyter.org/):
    [Notebooks](https://jupyter-notebook.readthedocs.io/en/latest/?badge=latest),
    [JupyterHub](https://jupyterhub.readthedocs.io/en/stable/),
    [ipywidgets](https://ipywidgets.readthedocs.io/en/latest/),
    [nbconvert](https://nbconvert.readthedocs.io/en/latest/)

## 2021.8.203 (August Release on 1 September 2021)

### Enhancements

1. Updated the preview to debugging in native notebooks. Set the `jupyter.experimental.debugging` setting to true, and a `Debug Cell` option will appear on the dropdown in the `Execute Cell` button. Pressing it will run the cell and hit any breakpoints you've set.
   ([#1652](https://github.com/Microsoft/vscode-jupyter/issues/1652))
1. Added the `Run by Line` feature. In Python notebooks, press `F10` while selecting a cell or click the first button on the cell toolbar to start a lightweight debugging session and run the cell line by line. To set it up, follow the steps [here](https://github.com/microsoft/vscode-jupyter/wiki/Setting-Up-Run-by-Line-and-Debugging-for-Notebooks).
   ([#5607](https://github.com/Microsoft/vscode-jupyter/issues/5607))
1. Add diskpath to logging for loading third party widgets to support local testing of new widget versions.
   ([#6294](https://github.com/Microsoft/vscode-jupyter/issues/6294))
1. Default plot output to just PNG, and support showing PNGs or SVGs in the Plot Viewer control. The enablePlotViewer setting still turns on both PNG and SVG plot output, but it's now off by default, not on.
   ([#6913](https://github.com/Microsoft/vscode-jupyter/issues/6913))
1. Update Simplified Chinese translation. (thanks [FiftysixTimes7](https://github.com/FiftysixTimes7))
   ([#7049](https://github.com/Microsoft/vscode-jupyter/issues/7049))

### Fixes

1. Run by line now stops after running the last line.
   ([#6858](https://github.com/Microsoft/vscode-jupyter/issues/6858))
1. Ensure execution of `raw` cells are skipped when we have multiple cells.
   ([#6954](https://github.com/Microsoft/vscode-jupyter/issues/6954))
1. Fixes to autocompletions returned by Jupyter Kernel (sort as returned by the kernel and trigger when entering quotes).
   ([#6979](https://github.com/Microsoft/vscode-jupyter/issues/6979))
1. Populate the interactive window variable explorer when focus is in the #%% Python file.
   ([#6993](https://github.com/Microsoft/vscode-jupyter/issues/6993))
1. Reinitialize kernels after a restart, including resetting current working directory and rerunning startup commands.
   ([#7016](https://github.com/Microsoft/vscode-jupyter/issues/7016))
1. Restore support for `jupyter.collapseCellInputCodeByDefault` in native interactive window.
   ([#7031](https://github.com/Microsoft/vscode-jupyter/issues/7031))
1. Fix restart kernel in native interactive window when executing a #%% cell.
   ([#7081](https://github.com/Microsoft/vscode-jupyter/issues/7081))
1. Fix code indentation being lost on interactive window export.
   ([#7088](https://github.com/Microsoft/vscode-jupyter/issues/7088))
1. Ensure variable explorer handles kernel restarts.
   ([#7126](https://github.com/Microsoft/vscode-jupyter/issues/7126))
1. Add remappable `esc` keybinding to clear contents of native interactive window input box, bound to `interactive.input.clear` command in VS Code core.
   ([#7157](https://github.com/Microsoft/vscode-jupyter/issues/7157))
1. Fix ability to use command palette restart/interrupt from command palette when focus is in a Python file linked to an interactive window.
   ([#7158](https://github.com/Microsoft/vscode-jupyter/issues/7158))
1. Fix A/B shortcuts to insert cell in command mode instead of edit mode. All Jupyter keyboard shortcuts are now provided through the Jupyter keymap extension, which is included with the Jupyter extension and can be uninstalled.
   ([#7172](https://github.com/Microsoft/vscode-jupyter/issues/7172))
1. Fixes kernel spec generation (on Mac M1/Non ZMQ supported machines) to include the appropriate environment.
   ([#7186](https://github.com/Microsoft/vscode-jupyter/issues/7186))
1. Support kernelspec argv containing non traditional args for `{connection_file}`.
   ([#7203](https://github.com/Microsoft/vscode-jupyter/issues/7203))
1. Fix export for already-open native notebooks.
   ([#7233](https://github.com/Microsoft/vscode-jupyter/issues/7233))
1. Fix being able to save PNG plots from the plot viewer.
   ([#7265](https://github.com/Microsoft/vscode-jupyter/issues/7265))
1. When no notebook or interactive window is active then clear the variables view.
   ([#7266](https://github.com/Microsoft/vscode-jupyter/issues/7266))
1. Fix placeholder 'Connecting to...' sys info cell not being overwritten after a kernel connection is established if cells are added to the interactive window first.
   ([#7280](https://github.com/Microsoft/vscode-jupyter/issues/7280))
1. Ensure that interactive window is started with active Python interpreter after active interpreter is changed.
   ([#7301](https://github.com/Microsoft/vscode-jupyter/issues/7301))
1. Restore support for Bash Kernel.
   ([#7345](https://github.com/microsoft/vscode-jupyter/issues/7345))

### Code Health

1. Remove old Interactive Window, old Notebook Editor and LiveShare code (all of this functionality is now Natively supported by VS Code).
   ([#6488](https://github.com/Microsoft/vscode-jupyter/issues/6488))

### Thanks

Thanks to the following projects which we fully rely on to provide some of
our features:

-   [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
-   [debugpy](https://pypi.org/project/debugpy/)

Also thanks to the various projects we provide integrations with which help
make this extension useful:

-   [Jupyter](https://jupyter.org/):
    [Notebooks](https://jupyter-notebook.readthedocs.io/en/latest/?badge=latest),
    [JupyterHub](https://jupyterhub.readthedocs.io/en/stable/),
    [ipywidgets](https://ipywidgets.readthedocs.io/en/latest/),
    [nbconvert](https://nbconvert.readthedocs.io/en/latest/)

## 2021.8.11 (July Release on 3 August 2021)

### Enhancements

1. Updated the preview to run by line in native notebooks. Set the `jupyter.experimental.debugging` setting to true, install ipykernel 6 on your selected kernel and a `Run by Line` button will appear on cell toolbars. Pressing it will start a lightweight debugging session and let you run the cell line by line.
   ([#5607](https://github.com/microsoft/vscode-jupyter/issues/5607))

### Fixes

1. Restore plotviewer in Native Notebooks.
   ([#6315](https://github.com/Microsoft/vscode-jupyter/issues/6315))
1. Fix debugging in `Interactive Window` when using `IPyKernel 6`.
   ([#6534](https://github.com/Microsoft/vscode-jupyter/issues/6534))
1. Add a placeholder `Python 3` kernel if user doesn't have any Python interpreters, with ability to notify user to install Python extenssion or Python runtime.
   ([#5864](https://github.com/Microsoft/vscode-jupyter/issues/5864))
1. Fixes to completion items received from Jupyter.
   ([#5956](https://github.com/Microsoft/vscode-jupyter/issues/5956))
1. Run all and restarting does not actually interrupt the rest of the running cells.
   ([#5996](https://github.com/Microsoft/vscode-jupyter/issues/5996))
1. Remove popup tip that indicates to users the kernel picker is in the bottom right.
   ([#6016](https://github.com/Microsoft/vscode-jupyter/issues/6016))
1. Ensure Pyspark kernels are listed.
   ([#6316](https://github.com/Microsoft/vscode-jupyter/issues/6316))
1. Fix problem where the active interpreter is not being used for the interactive window when not running with raw kernel.
   ([#6409](https://github.com/Microsoft/vscode-jupyter/issues/6409))
1. `Ctrl+Enter` in native notebooks should put cell into command mode immediately, then run the cell.
   ([#6582](https://github.com/Microsoft/vscode-jupyter/issues/6582))
1. List non-traditional (not using `ipykernel`) global Python kernelspecs.
   ([#6622](https://github.com/Microsoft/vscode-jupyter/issues/6622))
1. Clone the Notebook metadata before udpating it.
   ([#6624](https://github.com/Microsoft/vscode-jupyter/issues/6624))
1. Format the readme to render correctly on the VS Code extensions side bar. Thanks [jyooru](https://github.com/jyooru)!
   ([#6648](https://github.com/Microsoft/vscode-jupyter/issues/6648))
1. Ensure we get Jupyter Server info correctly in Python 3.6.
   ([#6738](https://github.com/Microsoft/vscode-jupyter/issues/6738))
1. List kernels in situations where extension is installed after opening a notebook.
   ([#6824](https://github.com/Microsoft/vscode-jupyter/issues/6824))

### Thanks

Thanks to the following projects which we fully rely on to provide some of
our features:

-   [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
-   [debugpy](https://pypi.org/project/debugpy/)

Also thanks to the various projects we provide integrations with which help
make this extension useful:

-   [Jupyter](https://jupyter.org/):
    [Notebooks](https://jupyter-notebook.readthedocs.io/en/latest/?badge=latest),
    [JupyterHub](https://jupyterhub.readthedocs.io/en/stable/),
    [ipywidgets](https://ipywidgets.readthedocs.io/en/latest/),
    [nbconvert](https://nbconvert.readthedocs.io/en/latest/)

### Code Health

## 2021.8.1 (June Release on 19 July 2021)

### Fixes

1. Fix for kernel not starting with correct path (causes DLL load and import modules failures).
   ([#5833](https://github.com/Microsoft/vscode-jupyter/issues/5833))

## 2021.8.0 (June Release on 8 July 2021)

### Enhancements

1. In preview native notebooks UI, contribute `L` keybinding to toggle line numbers for the current cell, and `shift+L` keybinding to toggle line numbers for all cells.
   ([#4438](https://github.com/Microsoft/vscode-jupyter/issues/4438))
1. Add xarray arrays to Data Viewer.
   ([#5590](https://github.com/Microsoft/vscode-jupyter/issues/5590))
1. When editing a markdown cell in preview native notebooks UI, contribute `ctrl+enter` keybinding to render current markdown cell, and `shift+enter` to render current markdown cell and skip to the next cell.
   ([#5976](https://github.com/Microsoft/vscode-jupyter/issues/5976))
1. Contribute extension-level `shift+enter` keybinding to execute current code cell and select below in preview native notebooks UI.
   ([#6037](https://github.com/Microsoft/vscode-jupyter/issues/6037))
1. Added ability to save plots in the preview native notebooks UI.
   ([#6183](https://github.com/Microsoft/vscode-jupyter/issues/6183))
1. Added a preview to run by line and debugging in native notebooks. Set the `jupyter.experimental.debugging` setting to true, install ipykernel 6 on your selected kernel and a `debug` button will appear. Pressing it will start a debugging session and let you set and hit breakpoints.
   ([#5607](https://github.com/microsoft/vscode-jupyter/issues/5607))
1. Add `jupyter.enableNativeInteractiveWindow` setting to opt into the preview native interactive window experience, with support for VS Code customizations like keybindings, themes, snippets and more.([#1388](https://github.com/microsoft/vscode-jupyter/issues/1388))

### Fixes

1. Fix problems loading other language kernels in the Interactive Window and in non insiders webviews.
   ([#893](https://github.com/Microsoft/vscode-jupyter/issues/893))
1. Only ask user to switch to `"perFile"` mode if `"jupyter.interactiveWindowMode": "multiple"` and they have submitted code from two different source files.
   ([#5471](https://github.com/Microsoft/vscode-jupyter/issues/5471))
1. On remote connections check for new or removed LiveKernelConnections on document open.
   ([#5984](https://github.com/Microsoft/vscode-jupyter/issues/5984))
1. In preview native notebooks interface, show editor title buttons only when "notebook.globalToolbar" setting is set to `false`.
   ([#6019](https://github.com/Microsoft/vscode-jupyter/issues/6019))
1. Ship require.js with our notebook preloads and renderers.
   ([#6034](https://github.com/Microsoft/vscode-jupyter/issues/6034))
1. Save output in \*.ipynb even when output is created without any Jupyter output metadata.
   ([#6192](https://github.com/Microsoft/vscode-jupyter/issues/6192))
1. In preview native notebooks interface, contribute `ctrl+enter` keybinding which puts the current cell into control mode instead of leaving it in edit mode after running.
   ([#6198](https://github.com/Microsoft/vscode-jupyter/issues/6198))
1. Fix interrupt button in Native Notebook toolbar.
   ([#6254](https://github.com/Microsoft/vscode-jupyter/issues/6254))
1. Fix problem where the active interpreter is not being used for the interactive window when not running with raw kernel.
   ([#6409](https://github.com/Microsoft/vscode-jupyter/issues/6409))

### Code Health

1. Add doc switching variable view tests for native notebooks.
   ([#4355](https://github.com/Microsoft/vscode-jupyter/issues/4355))
1. Fix 'Restarting kernel will cancel cell execution & we can re-run a cell' test.
   ([#6139](https://github.com/Microsoft/vscode-jupyter/issues/6139))
1. Restore GitHub token access for CodeQL, issue locking and issue assignment workflows.
   ([#6170](https://github.com/Microsoft/vscode-jupyter/issues/6170))
1. Fix flake notebookAndWebview test.
   ([#6234](https://github.com/Microsoft/vscode-jupyter/issues/6234))

### Thanks

Thanks to the following projects which we fully rely on to provide some of
our features:

-   [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
-   [debugpy](https://pypi.org/project/debugpy/)

Also thanks to the various projects we provide integrations with which help
make this extension useful:

-   [Jupyter](https://jupyter.org/):
    [Notebooks](https://jupyter-notebook.readthedocs.io/en/latest/?badge=latest),
    [JupyterHub](https://jupyterhub.readthedocs.io/en/stable/),
    [ipywidgets](https://ipywidgets.readthedocs.io/en/latest/),
    [nbconvert](https://nbconvert.readthedocs.io/en/latest/)

## 2021.6.999 (May Release on 16 June 2021)

### Fixes

1. On remote connections check for new or removed LiveKernelConnections on document open.
   ([#5984](https://github.com/Microsoft/vscode-jupyter/issues/5984))
1. When editing a markdown cell in preview native notebooks UI, contribute `ctrl+enter` keybinding to render current markdown cell, and `shift+enter` to render current markdown cell and skip to the next cell.
   ([#5976](https://github.com/Microsoft/vscode-jupyter/issues/5976))
1. In preview native notebooks UI, contribute `L` keybinding to toggle line numbers for the current cell, and `shift+L` keybinding to toggle line numbers for all cells.
   ([#4438](https://github.com/Microsoft/vscode-jupyter/issues/4438))
1. Contribute extension-level `shift+enter` keybinding to execute current code cell and select below in preview native notebooks UI.
   ([#6037](https://github.com/Microsoft/vscode-jupyter/issues/6037))
1. In preview native notebooks interface, contribute `ctrl+enter` keybinding which puts the current cell into control mode instead of leaving it in edit mode after running.
   ([#6198](https://github.com/Microsoft/vscode-jupyter/issues/6198))
1. Fix interrupt button in Native Notebook toolbar.
   ([#6254](https://github.com/Microsoft/vscode-jupyter/issues/6254))

### Code Health

1. Fix 'Restarting kernel will cancel cell execution & we can re-run a cell' test.
   ([#6139](https://github.com/Microsoft/vscode-jupyter/issues/6139))

## 2021.6.99 (May Release on 8 June 2021)

### Enhancements

1. Data Viewer Filter Rows must use explicit wildcards to search for substrings in string filters. For example, filtering by "stable" will not show the value "unstable" anymore, but filtering by "\*stable" will show "stable" and "unstable".
   ([#1142](https://github.com/Microsoft/vscode-jupyter/issues/1142))
1. Sort variables by name and type in variable explorer.
   ([#4585](https://github.com/Microsoft/vscode-jupyter/issues/4585))
1. Limit languages dispalyed in the Cell language picker to languages supported by the kernel.
   ([#5580](https://github.com/Microsoft/vscode-jupyter/issues/5580))
1. Move native notebooks cell toolbar to the left by default.
   ([#5605](https://github.com/Microsoft/vscode-jupyter/issues/5605))
1. Display modal dialog box (so users don't miss this) when IPyKernel (or Jupyter) is missing (required to run Python in Interactive Window or Notebooks).
   ([#5798](https://github.com/Microsoft/vscode-jupyter/issues/5798))
1. Add support for [Virtual Workspaces](https://github.com/microsoft/vscode/wiki/Virtual-Workspaces).
   ([#5803](https://github.com/Microsoft/vscode-jupyter/issues/5803))
1. Losslessly compressed PNG images to save ~20KB.
   (thanks [Christopher Yeh](https://github.com/chrisyeh96))
   ([#5869](https://github.com/Microsoft/vscode-jupyter/issues/5869))
1. Adopt `notebook/toolbar` contribution point for native notebooks.
   ([#5954](https://github.com/Microsoft/vscode-jupyter/issues/5954))
1. Tweak variable view fit and finish to match VS Code.
   ([#5955](https://github.com/Microsoft/vscode-jupyter/issues/5955))
1. Replace 'Run cells above' and 'Run cell and below' commands and cell toolbar buttons with VS Code's built-in 'Execute Above Cells' and 'Execute Cell And Below' commands and unified run button.
   ([#6025](https://github.com/microsoft/vscode-jupyter/issues/6025))

### Fixes

1. Update/reinstall if module such as `IPyKernel` was installed once before or already exists.
   ([#4758](https://github.com/Microsoft/vscode-jupyter/issues/4758))
1. Stop listing default kernelspecs in kernel picker.
   ([#5445](https://github.com/Microsoft/vscode-jupyter/issues/5445))
1. Store interpreter information in notebook metadata instead of the generated kernelspec name.
   ([#5612](https://github.com/Microsoft/vscode-jupyter/issues/5612))
1. Restore the `Run Above/Below` cells command in `Command Palette`.
   ([#5746](https://github.com/Microsoft/vscode-jupyter/issues/5746))
1. Migrate 'workbench.editorAssociations' setting to new format.
   ([#5806](https://github.com/Microsoft/vscode-jupyter/issues/5806))
1. Add ABCMeta and type to variable explorer exclude list.
   ([#5865](https://github.com/Microsoft/vscode-jupyter/issues/5865))
1. Blank Python notebooks do not use active interpreter.
   ([#5874](https://github.com/Microsoft/vscode-jupyter/issues/5874))
1. Change language of cell to reflect langauges supported by the selected Kernel.
   ([#5924](https://github.com/Microsoft/vscode-jupyter/issues/5924))
1. Resolve issue related to `Interrupt` button vanishing when tabbing across notebooks while a cell is being executed.
   ([#5925](https://github.com/Microsoft/vscode-jupyter/issues/5925))
1. Delete encrypted storage in a try catch to avoid errors.
   ([#5934](https://github.com/Microsoft/vscode-jupyter/issues/5934))
1. Support new renderer API in Jupyter.
   ([#5952](https://github.com/Microsoft/vscode-jupyter/issues/5952))
1. Hide kernels belonging to deleted Python environments from kernel picker.
   ([#6164](https://github.com/Microsoft/vscode-jupyter/issues/6164))

### Code Health

1. Error category for unsupported kernelspec file args.
   ([#5492](https://github.com/Microsoft/vscode-jupyter/issues/5492))
1. Fix basic execution issues with nonConda 'remote' and nonConda 'local' test suites.
   ([#5660](https://github.com/Microsoft/vscode-jupyter/issues/5660))
1. Update to new message API for native notebook preloads.
   ([#5753](https://github.com/Microsoft/vscode-jupyter/issues/5753))
1. Rename of onDidChangeCellExecutionState.
   ([#5809](https://github.com/Microsoft/vscode-jupyter/issues/5809))
1. Fix functional ipywidget tests.
   ([#5842](https://github.com/Microsoft/vscode-jupyter/issues/5842))
1. When using remote Jupyter connections pre-fetch kernels only when opening a notebook.
   ([#5846](https://github.com/Microsoft/vscode-jupyter/issues/5846))
1. Removed execution isolation script.
   ([#5931](https://github.com/Microsoft/vscode-jupyter/issues/5931))
1. VSCode API naming changes for NotebookCellExecution, NotebookRendererScript.
   ([#6014](https://github.com/Microsoft/vscode-jupyter/issues/6014))
1. API Changes viewType => notebookType and notebook namespace to notebooks.
   ([#6046](https://github.com/microsoft/vscode-jupyter/issues/6046))
1. Update test init code to use window and not notebook for editor properties.
   ([#6098](https://github.com/Microsoft/vscode-jupyter/issues/6098))
1. Support the new renderer API in jupyter extension.
   ([#6118](https://github.com/Microsoft/vscode-jupyter/issues/6118))
1. Update to new notebookcontroller selection function name.
   ([#6121](https://github.com/Microsoft/vscode-jupyter/issues/6121))
1. Inline execution handler change to notebook API.
   ([#6137](https://github.com/Microsoft/vscode-jupyter/issues/6137))

### Thanks

Thanks to the following projects which we fully rely on to provide some of
our features:

-   [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
-   [debugpy](https://pypi.org/project/debugpy/)

Also thanks to the various projects we provide integrations with which help
make this extension useful:

-   [Jupyter](https://jupyter.org/):
    [Notebooks](https://jupyter-notebook.readthedocs.io/en/latest/?badge=latest),
    [JupyterHub](https://jupyterhub.readthedocs.io/en/stable/),
    [ipywidgets](https://ipywidgets.readthedocs.io/en/latest/),
    [nbconvert](https://nbconvert.readthedocs.io/en/latest/)

## 2021.6.0 (05 May 2021)

### Enhancements

1. Manage contributed Jupyter kernels registration.
   ([#4490](https://github.com/Microsoft/vscode-jupyter/issues/4490))
1. Update variable explorer icon.
   ([#5355](https://github.com/Microsoft/vscode-jupyter/issues/5355))
1. Add keybind 'O' to toggle the output of all selected cells in a notebook.
   ([#5425](https://github.com/Microsoft/vscode-jupyter/issues/5425))
1. Recommend extensions when opening notebooks targeting specific languages.
   ([#5577](https://github.com/Microsoft/vscode-jupyter/issues/5577))

### Fixes

1. Restore the Intellisense documentation on custom editor notebook.
   ([#5124](https://github.com/Microsoft/vscode-jupyter/issues/5124))
1. Upgrade vega-transforms and support vegalite v4.
   ([#5149](https://github.com/Microsoft/vscode-jupyter/issues/5149))
1. Add a 10 minute delay to surveys.
   ([#5261](https://github.com/Microsoft/vscode-jupyter/issues/5261))
1. Display formatted markdown description for `jupyter.variableQueries` setting in settings UI.
   ([#5289](https://github.com/Microsoft/vscode-jupyter/issues/5289))
1. Pass remote Jupyter server's default kernelspec name in remote kernel connection.
   ([#5290](https://github.com/Microsoft/vscode-jupyter/issues/5290))
1. Ensure data viewer grid is resized when slice panel is toggled so that horizontal scrollbar remains visible.
   ([#5309](https://github.com/Microsoft/vscode-jupyter/issues/5309))
1. When 3rd party CDN downloads need to be enabled for ipywidgets support, display More Info and Enable Downloads buttons instead of embedding them as links in the message.
   ([#5352](https://github.com/Microsoft/vscode-jupyter/issues/5352))
1. Fix the output link in the kernel timeout message.
   ([#5360](https://github.com/Microsoft/vscode-jupyter/issues/5360))
1. Stop asking users to install ipykernel on autostart, only do it when a cell is run.
   ([#5368](https://github.com/Microsoft/vscode-jupyter/issues/5368))
1. Fix for 'Export as Python Script' option not appearing.
   ([#5403](https://github.com/Microsoft/vscode-jupyter/issues/5403))
1. Update to remove usage of .cells property from NotebookDocument. Also update TextDocument with notebook property and QuickPick.
   ([#5417](https://github.com/Microsoft/vscode-jupyter/issues/5417))
1. Delete extension context secrets if we get an error when getting them.
   Small fixes on error handling.
   ([#5419](https://github.com/Microsoft/vscode-jupyter/issues/5419))
1. When native notebook is untrusted, do not allow cell execution and prompt to trust.
   ([#5436](https://github.com/Microsoft/vscode-jupyter/issues/5436))
1. Resize the untrusted icon.
   ([#5437](https://github.com/Microsoft/vscode-jupyter/issues/5437))
1. Save notebook metadata in ipynb even if the selected Kernel is provided by some other extension.
   ([#5460](https://github.com/Microsoft/vscode-jupyter/issues/5460))
1. Invalidate cached interpreters when Python extension active interpreter changes.
   ([#5470](https://github.com/Microsoft/vscode-jupyter/issues/5470))
1. Use interpreter information stored in kernelspec.json file when starting kernels.
   ([#5495](https://github.com/Microsoft/vscode-jupyter/issues/5495))
1. Update to new selections API.
   ([#5515](https://github.com/Microsoft/vscode-jupyter/issues/5515))
1. CellStatusBarItem update for Native Notebooks. Along with other breaking API changes.
   ([#5527](https://github.com/Microsoft/vscode-jupyter/issues/5527))
1. Remove statusbar from Notebook Cells.
   ([#5541](https://github.com/Microsoft/vscode-jupyter/issues/5541))
1. Hide Jupyter commands from other types of notebooks.
   ([#5559](https://github.com/Microsoft/vscode-jupyter/issues/5559))
1. Update to newest vscode Notebook API changes.
   ([#5598](https://github.com/Microsoft/vscode-jupyter/issues/5598))
1. Increase the width of the data viewer scrollbar.
   ([#5610](https://github.com/Microsoft/vscode-jupyter/issues/5610))
1. Fix `NameError: name '_VSCODE_InfoImport' is not defined` when attempting to open the data viewer from 2 or more different scopes in a single debug session.
   ([#5627](https://github.com/Microsoft/vscode-jupyter/issues/5627))
1. Use active interpreter when starting Kernels for Interactive Window.
   ([#5628](https://github.com/Microsoft/vscode-jupyter/issues/5628))
1. Use `download` package to download widget scripts.
   ([#5633](https://github.com/Microsoft/vscode-jupyter/issues/5633))
1. Start kernel if not already started when using `Run cells above/below`.
   ([#5636](https://github.com/Microsoft/vscode-jupyter/issues/5636))

### Code Health

1. Add functional test for large data in data viewer.
   ([#5207](https://github.com/Microsoft/vscode-jupyter/issues/5207))
1. Pass `NotebookDocument` when invoking `jupyter.notebookeditor.interruptkernel`.
   ([#5242](https://github.com/Microsoft/vscode-jupyter/issues/5242))
1. Remove data slicing experiment feature gate.
   ([#5399](https://github.com/Microsoft/vscode-jupyter/issues/5399))
1. Ignore errors throw by VS Code when updating cell output during execution.
   ([#5446](https://github.com/Microsoft/vscode-jupyter/issues/5446))
1. Improvements to telemetry used to check if we're not starting the right interpreter (for a Python kernel).
   ([#5509](https://github.com/Microsoft/vscode-jupyter/issues/5509))
1. Add telemetry to check if we fail to update kernelspecs with environment variables.
   ([#5547](https://github.com/Microsoft/vscode-jupyter/issues/5547))
1. Ensure `canvas` and `playwright-chromium` are setup as optional dependencies in `package.json`.
   ([#5567](https://github.com/Microsoft/vscode-jupyter/issues/5567))
1. Fix tests after kernel push changes.
   ([#5585](https://github.com/Microsoft/vscode-jupyter/issues/5585))

### Thanks

Thanks to the following projects which we fully rely on to provide some of
our features:

-   [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
-   [debugpy](https://pypi.org/project/debugpy/)

Also thanks to the various projects we provide integrations with which help
make this extension useful:

-   [Jupyter](https://jupyter.org/):
    [Notebooks](https://jupyter-notebook.readthedocs.io/en/latest/?badge=latest),
    [JupyterHub](https://jupyterhub.readthedocs.io/en/stable/),
    [ipywidgets](https://ipywidgets.readthedocs.io/en/latest/),
    [nbconvert](https://nbconvert.readthedocs.io/en/latest/)

## 2021.5.1 (12 April 2021)

### Code Health

1. Check the responses of prompts for installation of missing packages such as `IPyKernel`.
   ([#5432](https://github.com/Microsoft/vscode-jupyter/issues/5432))

### Fixes

1. Fix for 'Export as Python Script' option not appearing.
   ([#5403](https://github.com/Microsoft/vscode-jupyter/issues/5403))
1. Delete extension context secrets if we get an error when getting them.
   Small fixes on error handling.
   ([#5419](https://github.com/Microsoft/vscode-jupyter/issues/5419))
1. Enable correct plot background for Native Notebooks.
   ([#5353](https://github.com/Microsoft/vscode-jupyter/issues/5353))
1. Stop asking users to install ipykernel on autostart, only do it when a cell is ran.
   ([#5368](https://github.com/microsoft/vscode-jupyter/issues/5368))
1. Invalidate cached interpreters when Python extension active interpreter changes.
   ([#5470](https://github.com/microsoft/vscode-jupyter/issues/5470))

## 2021.5.0 (31 March 2021)

### Enhancements

1. Be able to provide string argument to jupyter.execSelectionInteractive for extensibility.
   (thanks [Andrew Craig](https://github.com/andycraig/))
   ([#1689](https://github.com/Microsoft/vscode-jupyter/issues/1689))

### Fixes

1. Jupyter variables tab will always be named 'Jupyter Variables'.
   ([#4458](https://github.com/Microsoft/vscode-jupyter/issues/4458))
1. Variable view will stay as long as you have a notebook open (not necessarily active).
   ([#4562](https://github.com/Microsoft/vscode-jupyter/issues/4562))
1. Add quotations to arguments with blank spaces when executing kernel processes.
   ([#4647](https://github.com/Microsoft/vscode-jupyter/issues/4647))
1. Do not prompt to install Python extension when creating a blank notebook.
   ([#4965](https://github.com/Microsoft/vscode-jupyter/issues/4965))
1. Cache the active workspace Python Interpreter.
   ([#5004](https://github.com/Microsoft/vscode-jupyter/issues/5004))
1. Don't prewarm variables for global jupyter interpreter if ZMQ is supported.
   ([#5009](https://github.com/Microsoft/vscode-jupyter/issues/5009))
1. When closing the Interactive Window, shutdown sessions started by Interactive Window.
   ([#5030](https://github.com/Microsoft/vscode-jupyter/issues/5030))
1. Stop wrapping new errors if we threw the original error.
   ([#5089](https://github.com/Microsoft/vscode-jupyter/issues/5089))
1. Ignore errors when getting the environment variables for a Python environment.
   ([#5093](https://github.com/Microsoft/vscode-jupyter/issues/5093))
1. Revert viewsContainter name to Jupyter and view name to Variables to avoid un-named viewsContainer.
   ([#5102](https://github.com/Microsoft/vscode-jupyter/issues/5102))
1. Ensure extensions depending on Jupyter do not fail to load if Jupyter extension fails to load.
   ([#5145](https://github.com/Microsoft/vscode-jupyter/issues/5145))
1. Don't display the data science banner for non-Jupyter notebooks.
   ([#5181](https://github.com/Microsoft/vscode-jupyter/issues/5181))
1. Don't use NotebookEditor.onDidDispose and support new err / out specific stream mime types.
   ([#5191](https://github.com/Microsoft/vscode-jupyter/issues/5191))
1. Prevent unnecessary activation of the Python extension.
   ([#5193](https://github.com/Microsoft/vscode-jupyter/issues/5193))
1. Update widget kernel for new NotebookOutputEventParams.
   ([#5195](https://github.com/Microsoft/vscode-jupyter/issues/5195))
1. Updates to code used to run Python in an isolated manner.
   ([#5212](https://github.com/Microsoft/vscode-jupyter/issues/5212))
1. Changes to proposed API for using resolveKernel instead of resolveNotebook. Since this change goes along with widget tests also renable and fix those tests.
   ([#5217](https://github.com/Microsoft/vscode-jupyter/issues/5217))
1. Fix data viewer display of non-numeric index columns in DataFrames.
   ([#5253](https://github.com/Microsoft/vscode-jupyter/issues/5253))
1. Display messages notifying user to enable support for CDNs when rendering IPyWidgets.
   ([#5074](https://github.com/Microsoft/vscode-jupyter/issues/5074))
1. When reopening a newly created Notebook with a Julia kernel, the cells should be detected as `Julia`.
   ([#5148](https://github.com/Microsoft/vscode-jupyter/issues/5148))
1. Support switching kernels in Native Notebooks when connecting to Jupyter.
   ([#1215](https://github.com/Microsoft/vscode-jupyter/issues/1215))
1. Refactor how Kernels are searched and selected.
   ([#4995](https://github.com/microsoft/vscode-jupyter/pull/4995))
1. Fix run selection/line to work from the active editor
   ([#5287](https://github.com/Microsoft/vscode-jupyter/issues/5287))
1. Update variable view to use the new API for native cell execution notification.
   ([#5316](https://github.com/Microsoft/vscode-jupyter/issues/5316))
1. Ensure users in CodeSpaces do not get prompted to forward Kernel Ports.
   ([#5283](https://github.com/Microsoft/vscode-jupyter/issues/5283))
1. Disable surveys in CodeSpaces.
   ([#5295](https://github.com/Microsoft/vscode-jupyter/issues/5295))
1. Ensure Git diff viewer does not get replaced by Notebook Editor.
   ([#633](https://github.com/Microsoft/vscode-jupyter/issues/633))
   (thanks [Matt Bierner](https://github.com/mjbvz))

### Code Health

1. Ability to queue telemetry until all of the data required is available.
   ([#4956](https://github.com/Microsoft/vscode-jupyter/issues/4956))
1. Fix variables test. We had a new import of sys, which was causing the variable fetching to have to do one extra fetch, pushing it over the limit to require a second chunk fetch.
   ([#5016](https://github.com/Microsoft/vscode-jupyter/issues/5016))
1. Add tests for data viewer slice data functionality.
   ([#5066](https://github.com/Microsoft/vscode-jupyter/issues/5066))
1. Remove setting `jupyter.useNotebookEditor`.
   ([#5130](https://github.com/Microsoft/vscode-jupyter/issues/5130))
1. Enable `debug` logging by default.
   ([#5238](https://github.com/Microsoft/vscode-jupyter/issues/5238))

### Thanks

Thanks to the following projects which we fully rely on to provide some of
our features:

-   [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
-   [debugpy](https://pypi.org/project/debugpy/)

Also thanks to the various projects we provide integrations with which help
make this extension useful:

-   [Jupyter](https://jupyter.org/):
    [Notebooks](https://jupyter-notebook.readthedocs.io/en/latest/?badge=latest),
    [JupyterHub](https://jupyterhub.readthedocs.io/en/stable/),
    [ipywidgets](https://ipywidgets.readthedocs.io/en/latest/),

## 2021.3.0 (3 March 2021)

### Enhancements

1. Add ability to view a slice of the current variable in the data viewer using either axis/index dropdowns or a slice expression input field.
   ([#305](https://github.com/Microsoft/vscode-jupyter/issues/305))
1. Enable refreshing active data viewer contents using Jupyter: Refresh Data Viewer command in the command palette, Cmd+R or Ctrl+R, or the refresh button in the editor title menu.
   ([#1143](https://github.com/Microsoft/vscode-jupyter/issues/1143))
1. Always open the data viewer in the last view group that it was moved to.
   ([#4689](https://github.com/Microsoft/vscode-jupyter/issues/4689))
1. Support for other extensions to provide a default language when creating new notebooks.
   ([#4859](https://github.com/Microsoft/vscode-jupyter/issues/4859))

### Fixes

1. Remove special casing to ignore warnings.
   ([#1312](https://github.com/Microsoft/vscode-jupyter/issues/1312))
1. Allow jupyter kernels to not be handled by the jupyter extension.
   ([#4423](https://github.com/Microsoft/vscode-jupyter/issues/4423))
1. Restore the 'Select a Kernel' command on the interactive window.
   ([#4479](https://github.com/Microsoft/vscode-jupyter/issues/4479))
1. Correctly syntax color items in native variable view.
   ([#4499](https://github.com/Microsoft/vscode-jupyter/issues/4499))
1. Don't ask for a kernel restart if the kernel was interrupted in native notebooks.
   ([#4669](https://github.com/Microsoft/vscode-jupyter/issues/4669))
1. Popup a tip when opening a notebook for the first time.
   ([#4775](https://github.com/Microsoft/vscode-jupyter/issues/4775))
1. Ensure we save the contents when closing a (webview based) notebook.
   ([#4779](https://github.com/Microsoft/vscode-jupyter/issues/4779))
1. Stop sending cells executed silently to other extensions.
   ([#4867](https://github.com/Microsoft/vscode-jupyter/issues/4867))
1. Do not prompt to install missing dependencies on GitHub Codespaces.
   ([#4882](https://github.com/Microsoft/vscode-jupyter/issues/4882))

### Code Health

1. Synchronously check if `zmq` is supported.
   ([#4764](https://github.com/Microsoft/vscode-jupyter/issues/4764))
1. Telemetry to track the commands executed using ICommandManager.
   ([#4926](https://github.com/Microsoft/vscode-jupyter/issues/4926))
1. More telemetry to track kernel failure reasons.
   ([#4940](https://github.com/Microsoft/vscode-jupyter/issues/4940))
1. Add telemetry flag to differentiate between stable vs insider builds of the extension.
   ([#4959](https://github.com/Microsoft/vscode-jupyter/issues/4959))
1. Add telemetry to check if we have started the right local Python kernel.
   ([#4999](https://github.com/Microsoft/vscode-jupyter/issues/4999))

### Thanks

Thanks to the following projects which we fully rely on to provide some of
our features:

-   [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
-   [debugpy](https://pypi.org/project/debugpy/)

Also thanks to the various projects we provide integrations with which help
make this extension useful:

-   [Jupyter](https://jupyter.org/):
    [Notebooks](https://jupyter-notebook.readthedocs.io/en/latest/?badge=latest),
    [JupyterHub](https://jupyterhub.readthedocs.io/en/stable/),
    [ipywidgets](https://ipywidgets.readthedocs.io/en/latest/),

## 2021.2.1 (28 February 2021)

### Fixes

1. Popup a tip when opening a notebook for the first time.
   ([#4775](https://github.com/Microsoft/vscode-jupyter/issues/4775))
1. Ensure we save the contents when closing a (webview based) notebook.
   ([#4779](https://github.com/Microsoft/vscode-jupyter/issues/4779))
1. Allow kernels to not be handled by the jupyter extension.
   ([#4423](https://github.com/Microsoft/vscode-jupyter/issues/4423)
1. Enable native notebook if sync'd settings is forcing it.
   ([#4845](https://github.com/Microsoft/vscode-jupyter/issues/4845)
1. Fix 'Export as Notebook' not working after opening a notebook on a python file.
   ([#4869](https://github.com/Microsoft/vscode-jupyter/issues/4869)

## 2021.2.0 (17 February 2021)

### Enhancements

1. Support multidimensional data in the data viewer. >2D dimensions are flattened, with the ability to double-click on a truncated cell to view the full value in a horizontally scrollable field.
   ([#298](https://github.com/Microsoft/vscode-jupyter/issues/298))
1. Support NaN, Inf, -Inf in data viewer.
   ([#299](https://github.com/Microsoft/vscode-jupyter/issues/299))
1. Support viewing PyTorch tensors and TensorFlow EagerTensors in variable explorer and data viewer.
   ([#304](https://github.com/Microsoft/vscode-jupyter/issues/304))
1. Show more detailed error messages when the kernel dies or times out.
   ([#1254](https://github.com/Microsoft/vscode-jupyter/issues/1254))
1. Do not invoke requestKernelInfo when the Kernel.info property already contains this information.
   ([#3202](https://github.com/Microsoft/vscode-jupyter/issues/3202))
1. Support rendering of outputs such as Plotly, Altair, Vega, and the like in Native Notebooks.
   ([#3936](https://github.com/Microsoft/vscode-jupyter/issues/3936))
1. Add full Simplified Chinese translation.
   (thanks [FiftysixTimes7](https://github.com/FiftysixTimes7))
   ([#4418](https://github.com/Microsoft/vscode-jupyter/issues/4418))
1. Add a button to the native notebook toolbar to show the variable panel. Disable button when panel is already visible.
   ([#4486](https://github.com/Microsoft/vscode-jupyter/issues/4486))
1. Users on AML Compute will automatically get the new Native Notebook experience.
   ([#4550](https://github.com/Microsoft/vscode-jupyter/issues/4550))
1. Improved Tensor tooltips in Python files which have been run in the interactive window.
   ([#302](https://github.com/Microsoft/vscode-jupyter/issues/302))
1. Minimize number of icons on the notebook toolbar (put the rest in overflow).
   ([#4730](https://github.com/Microsoft/vscode-jupyter/issues/4730))
1. Add survey for the new Notebooks experience experiment.
   ([#4726](https://github.com/microsoft/vscode-jupyter/issues/4726))
1. Don't overwrite the top level VS Code Save and Undo command keybindings.
   ([#4527](https://github.com/Microsoft/vscode-jupyter/issues/4527))

### Fixes

1. Added a progress notification when restarting the kernel.
   ([#1197](https://github.com/Microsoft/vscode-jupyter/issues/1197))
1. Fix error with selecting jupyter server URI when no workspace open.
   ([#4037](https://github.com/Microsoft/vscode-jupyter/issues/4037))
1. Fix Z (and CTRL+Z when using custom editor support) to update data model so that save works.
   ([#4058](https://github.com/Microsoft/vscode-jupyter/issues/4058))
1. Preload font awesome for ipywidgets.
   ([#4095](https://github.com/Microsoft/vscode-jupyter/issues/4095))
1. When comparing to existing running kernel only consider the kernelspec when launched via kernelspec.
   ([#4109](https://github.com/Microsoft/vscode-jupyter/issues/4109))
1. Fix notebook cells running out of order (for VS code insiders notebook editor).
   ([#4136](https://github.com/Microsoft/vscode-jupyter/issues/4136))
1. Support installing ipykernel when necessary in native notebooks.
   ([#4153](https://github.com/Microsoft/vscode-jupyter/issues/4153))
1. `__file__` variable is now set after changing kernel in the interactive window.
   ([#4164](https://github.com/Microsoft/vscode-jupyter/issues/4164))
1. Fix support for IPyWidgets in Interactive Window.
   ([#4203](https://github.com/Microsoft/vscode-jupyter/issues/4203))
1. Fix hover tips on notebooks (and the interactive window).
   ([#4218](https://github.com/Microsoft/vscode-jupyter/issues/4218))
1. Fix problem with creating a blank notebook from the python extension start page.
   ([#4242](https://github.com/Microsoft/vscode-jupyter/issues/4242))
1. Don't suppress whitespace at start of output for native notebooks.
   ([#4254](https://github.com/Microsoft/vscode-jupyter/issues/4254))
1. Clear output of a cell if its executed while empty.
   ([#4286](https://github.com/Microsoft/vscode-jupyter/issues/4286))
1. Wait for datascience code to activate when activating the extension.
   ([#4295](https://github.com/Microsoft/vscode-jupyter/issues/4295))
1. Fix problem when run all cells an exception is thrown, cells can no longer be run.
   ([#4309](https://github.com/Microsoft/vscode-jupyter/issues/4309))
1. Update trust icons.
   ([#4338](https://github.com/Microsoft/vscode-jupyter/issues/4338))
1. Display trusted icon when a notebook is trusted.
   ([#4339](https://github.com/Microsoft/vscode-jupyter/issues/4339))
1. Enable 'Run To Line', 'Run From Line' and 'Run Selection/Line in Interactive Window' on the editor context.
   The 'shift+enter' keybinding still follows the "jupyter.sendSelectionToInteractiveWindow" setting.
   ([#4368](https://github.com/Microsoft/vscode-jupyter/issues/4368))
1. If a kernel refuses to interrupt ask the user if they want to restart instead.
   ([#4369](https://github.com/Microsoft/vscode-jupyter/issues/4369))
1. Refresh variable explorer when docking is changed.
   ([#4485](https://github.com/Microsoft/vscode-jupyter/issues/4485))
1. Correctly handle kernel restarts in native variable viewer.
   ([#4492](https://github.com/Microsoft/vscode-jupyter/issues/4492))
1. All notebook commands should be prefixed with 'Notebook'.
   ([#4494](https://github.com/Microsoft/vscode-jupyter/issues/4494))
1. Don't retain context on variable view. Update view with current execution count when made visible.
   ([#4541](https://github.com/Microsoft/vscode-jupyter/issues/4541))
1. Remove unnecessary files from the VSIX that just take up space.
   ([#4551](https://github.com/Microsoft/vscode-jupyter/issues/4551))
1. Support set_next_input message payload.
   ([#4566](https://github.com/Microsoft/vscode-jupyter/issues/4566))
1. Fix the Variable Explorer height so the horizontal scroll bar is shown.
   ([#4598](https://github.com/Microsoft/vscode-jupyter/issues/4598))
1. Allow viewing class instance variables in the data viewer.
   ([#4606](https://github.com/Microsoft/vscode-jupyter/issues/4606))
1. Update message that recommends the python extension to a warning and mention it gives an enhanced experience.
   ([#4615](https://github.com/Microsoft/vscode-jupyter/issues/4615))
1. Correctly hide old interpreters registered as kernels from the selector.
   ([#4632](https://github.com/Microsoft/vscode-jupyter/issues/4632))
1. Allow installing python extension in codespaces.
   ([#4664](https://github.com/Microsoft/vscode-jupyter/issues/4664))
1. Add notebook codicon for Juypter viewContainer.
   ([#4538](https://github.com/Microsoft/vscode-jupyter/issues/4538))
1. Allow options to show native variable view only when looking at native notebooks.
   ([#4761](https://github.com/Microsoft/vscode-jupyter/issues/4761))
1. Fix CTRL+ENTER and ALT+ENTER to behave as expected for a jupyter notebook.
   ([#4713](https://github.com/Microsoft/vscode-jupyter/issues/4713))
1. If .NET interactive is installed, make sure to use the new notebook editor.
   ([#4771](https://github.com/Microsoft/vscode-jupyter/issues/4771))
1. Only clean up a notebook editor when it's closed, not when the panel is disposed.
   ([#4786](https://github.com/Microsoft/vscode-jupyter/issues/4786))
1. Fixes problem with duplicate jupyter kernels being generated.
   ([#4720](https://github.com/Microsoft/vscode-jupyter/issues/4720))

### Code Health

1. Deprecate src\client\datascience\kernel-launcher\helpers.ts.
   ([#1195](https://github.com/Microsoft/vscode-jupyter/issues/1195))
1. Stop preloading requirejs in ipywidgets for native notebooks.
   ([#4015](https://github.com/Microsoft/vscode-jupyter/issues/4015))
1. Add .vscode tests to test the new variable view.
   ([#4355](https://github.com/Microsoft/vscode-jupyter/issues/4355))
1. Update CI to set xvfb correctly, and new test step that can do native notebooks + old webviews.
   ([#4412](https://github.com/Microsoft/vscode-jupyter/issues/4412))
1. Run cells below test randomly failing on shutdown.
   ([#4445](https://github.com/Microsoft/vscode-jupyter/issues/4445))
1. Fix julia test to pass.
   ([#4453](https://github.com/Microsoft/vscode-jupyter/issues/4453))
1. Add UI side telemetry for variable view.
   ([#4649](https://github.com/Microsoft/vscode-jupyter/issues/4649))
1. Prevent Winston logger from exiting the Extension Host when there are unhandled exceptions.
   ([#4702](https://github.com/Microsoft/vscode-jupyter/issues/4702))

### Thanks

Thanks to the following projects which we fully rely on to provide some of
our features:

-   [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
-   [debugpy](https://pypi.org/project/debugpy/)

Also thanks to the various projects we provide integrations with which help
make this extension useful:

-   [Jupyter](https://jupyter.org/):
    [Notebooks](https://jupyter-notebook.readthedocs.io/en/latest/?badge=latest),
    [JupyterHub](https://jupyterhub.readthedocs.io/en/stable/),
    [ipywidgets](https://ipywidgets.readthedocs.io/en/latest/),

## 2020.12.1 (10 December 2020)

### Fixes

1. Fix support for IPyWidgets in Interactive Window.
   ([#4203](https://github.com/Microsoft/vscode-jupyter/issues/4203))

## 2020.12.0 (9 December 2020)

### Enhancements

1. Add support for IPyWidget in Native Notebooks.
   ([#251](https://github.com/Microsoft/vscode-jupyter/issues/251))

### Fixes

1. Information in the interactive window is python specific.
   ([#340](https://github.com/Microsoft/vscode-jupyter/issues/340))
1. Allow user to cancel asking about logging level.
   ([#348](https://github.com/Microsoft/vscode-jupyter/issues/348))
1. Watch for any addition of the python extension, and don't suggest a full reload when it is added.
   ([#405](https://github.com/Microsoft/vscode-jupyter/issues/405))
1. Only offer to export to python script when the metadata specifies python as its language.
   ([#407](https://github.com/Microsoft/vscode-jupyter/issues/407))
1. Hide webview based Notebook command `Select Kernel` when a Notebook is opened using the new VS Code Native Notebook editor.
   ([#426](https://github.com/Microsoft/vscode-jupyter/issues/426))
1. Correctly pass the candidate interpreter when exporting.
   ([#1363](https://github.com/Microsoft/vscode-jupyter/issues/1363))
1. `__file__` variable not set after restarting kernel in the interactive window.
   ([#1373](https://github.com/Microsoft/vscode-jupyter/issues/1373))
1. Fix the search path for Jupyter kernels on UNIX systems (thanks [Giulio Girardi](https://github.com/rapgenic/))
   ([#3918](https://github.com/Microsoft/vscode-jupyter/issues/3918))
1. Fix the directory for exporting from the interactive window and notebooks to match the directory where the original file was created.
   ([#3991](https://github.com/Microsoft/vscode-jupyter/issues/3991))
1. Fix variable fetching on remote machines that don't have our scripts files on them.
   ([#4006](https://github.com/Microsoft/vscode-jupyter/issues/4006))
1. Display survey prompt once per session.
   ([#4077](https://github.com/Microsoft/vscode-jupyter/issues/4077))
1. Guard against AttributeErrors in our DataViewer code.
   ([#4082](https://github.com/Microsoft/vscode-jupyter/issues/4082))
1. Ensure user cannot belong to Custom Editor experiment is already in Native Notebook experiment.
   ([#4105](https://github.com/Microsoft/vscode-jupyter/issues/4105))
1. Fix problems with code in UI getting out of sync with code being executed or saved to disk.
   ([#1701](https://github.com/Microsoft/vscode-jupyter/issues/1701))

### Code Health

1. Added an onCreated event to the Interactive Window provider so external buttons can appear on creation.
   ([#413](https://github.com/Microsoft/vscode-jupyter/issues/413))
1. Use notebookIdentity instead of the notebook when handling external buttons. It handles the case when the user doesn't autostart the kernel.
   ([#414](https://github.com/Microsoft/vscode-jupyter/issues/414))

### Thanks

Thanks to the following projects which we fully rely on to provide some of
our features:

-   [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
-   [debugpy](https://pypi.org/project/debugpy/)

Also thanks to the various projects we provide integrations with which help
make this extension useful:

-   [Jupyter](https://jupyter.org/):
    [Notebooks](https://jupyter-notebook.readthedocs.io/en/latest/?badge=latest),
    [JupyterHub](https://jupyterhub.readthedocs.io/en/stable/),
    [ipywidgets](https://ipywidgets.readthedocs.io/en/latest/),

## 2020.11.3 (03 December 2020)

### Fixes

1. Display survey prompt once per session.
   ([#4077](https://github.com/Microsoft/vscode-jupyter/issues/4077))

## 2020.11.2 (30 November 2020)

### Fixes

1. When removing our dynamically added editor associations always remove them if Native / Custom Editor is disabled, not just if we remember adding them.
   ([#3988](https://github.com/Microsoft/vscode-jupyter/issues/3988))
1. Ensure survey prompt is not displayed multiple times..
   ([#4002](https://github.com/Microsoft/vscode-jupyter/issues/4002))
1. Migrate references to python.dataScience.\* in when clauses of keybindings.json.
   ([#1088](https://github.com/Microsoft/vscode-jupyter/issues/1088))

### Thanks

Thanks to the following projects which we fully rely on to provide some of
our features:

-   [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
-   [debugpy](https://pypi.org/project/debugpy/)

Also thanks to the various projects we provide integrations with which help
make this extension useful:

-   [Jupyter](https://jupyter.org/):
    [Notebooks](https://jupyter-notebook.readthedocs.io/en/latest/?badge=latest),
    [JupyterHub](https://jupyterhub.readthedocs.io/en/stable/),
    [ipywidgets](https://ipywidgets.readthedocs.io/en/latest/),

## 2020.11.1 (19 November 2020)

### Fixes

1. Interactive window input prompt does not allow any keyboard input.
   ([#446](https://github.com/Microsoft/vscode-jupyter/issues/446))
1. Support opening Notebooks using Native Notebook editor even if the Python extension is not installed.
   ([#1074](https://github.com/Microsoft/vscode-jupyter/issues/1074))
1. Show kernel picker in the interactive window.
   ([#411](https://github.com/Microsoft/vscode-jupyter/issues/411))

### Thanks

Thanks to the following projects which we fully rely on to provide some of
our features:

-   [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
-   [debugpy](https://pypi.org/project/debugpy/)

Also thanks to the various projects we provide integrations with which help
make this extension useful:

-   [Jupyter](https://jupyter.org/):
    [Notebooks](https://jupyter-notebook.readthedocs.io/en/latest/?badge=latest),
    [JupyterHub](https://jupyterhub.readthedocs.io/en/stable/),
    [ipywidgets](https://ipywidgets.readthedocs.io/en/latest/),

## 2020.11.0 (11 November 2020)

### Thanks

Thanks to the following projects which we fully rely on to provide some of
our features:

-   [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
-   [debugpy](https://pypi.org/project/debugpy/)

Also thanks to the various projects we provide integrations with which help
make this extension useful:

-   [Jupyter](https://jupyter.org/):
    [Notebooks](https://jupyter-notebook.readthedocs.io/en/latest/?badge=latest),
    [JupyterHub](https://jupyterhub.readthedocs.io/en/stable/),
    [ipywidgets](https://ipywidgets.readthedocs.io/en/latest/),
