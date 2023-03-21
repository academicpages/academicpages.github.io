# Changelog

## Deprecated

This changelog is deprecated. Here is where you can find details about the latest updates to this extension:
- Highlighted features for the latest release are described in the VS Code release notes, under the "Contributions to extensions" section: https://code.visualstudio.com/updates
- All issues and code changes can be found by searching our Github repo under the latest milestone. [Example from November 2022](https://github.com/microsoft/vscode-jupyter/issues?q=is%3Aclosed+milestone%3A%22November+2022%22+)

## 1.0.12
* Ship jQuery and requirejs as pre-load scripts so that all outputs have access to these scripts.

## 1.0.10
* Add support for VegaLite 5.
* Fixes to rendering of Vega 5, VegaLite 3 and VegaLite 4.
* Fixes to rendering of JavaScript mime types to ensure the right variables are available and right context is setup.
* Ensure `jQuery` is available when rendering JavaScript mime types.
* Ensure outputs generated using `IPython.display.code` are displayed with the right syntax highlighting.

## 1.0.7
* Update plotly to version 2.11.1
* Update npm packages.

## 1.0.6
* Removed rendering of text/latex in favor of built-in support.

## 1.0.5
* Updated to use Plotly version 2.7.0

## 1.0.4
* Updated to use Plotly version 2.6.4

### Thanks

Thanks to the following projects which we fully rely on to provide some of
our features:

-   [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

Also thanks to the various projects we provide integrations with which help
make this extension useful:

-   [Jupyter](https://jupyter.org/):
    [Notebooks](https://jupyter-notebook.readthedocs.io/en/latest/?badge=latest),
    [ipywidgets](https://ipywidgets.readthedocs.io/en/latest/),
