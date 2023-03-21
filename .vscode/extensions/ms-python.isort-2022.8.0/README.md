# Import sorting extension for Visual Studio Code using `isort`

A Visual Studio Code extension that provides import sorting using `isort`. The extension ships with `isort=5.10.1`.

Note:

-   This extension is supported for all [actively supported versions](https://devguide.python.org/#status-of-python-branches) of the `python` language (i.e., python >= 3.7).
-   The bundled `isort` is only used if there is no installed version of `isort` found in the selected `python` environment.
-   Minimum supported version of `isort` is `5.10.1`.

## Usage

Once installed in pyVisual Studio Code, the extension will register `isort` as import organizer. You can use keyboard short cut `shift` + `alt` + `O` to trigger organize imports editor action. You can also trigger this from the quick fix available when imports are not organized.

![Fixing import sorting with a code action.](https://github.com/microsoft/vscode-isort/raw/HEAD/images/vscode-isort.gif)

### Import sorting on save

You can enable import sorting on save for python by having the following values in your settings. This adds both import sorting and formatting (using `black`) on save :

```json
  "[python]": {
    "editor.defaultFormatter": "ms-python.black-formatter",
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
        "source.organizeImports": true
    },
  },
  "isort.args":["--profile", "black"],
```

### Disabling `isort` extension

If you want to disable isort extension, you can [disable this extension](https://code.visualstudio.com/docs/editor/extension-marketplace#_disable-an-extension) per workspace in Visual Studio Code.

## Settings

| Settings               | Default                            | Description                                                                                                                                                                                                                                                              |
| ---------------------- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| isort.args             | `[]`                               | Custom arguments passed to `isort`. E.g `"isort.args" = ["--config", "<file>"]`                                                                                                                                                                                          |
| isort.severity         | `{ "W": "Warning", "E": "Error" }` | Controls mapping of severity from `isort` to VS Code severity when displaying in the problems window.                                                                                                                                                                    |
| isort.logLevel         | `error`                            | Sets the tracing level for the extension.                                                                                                                                                                                                                                |
| isort.path             | `[]`                               | Setting to provide custom `isort` executable. This will slow down formatting, since we will have to run `isort` executable every time or file save or open. Example 1: `["~/global_env/isort"]` Example 2: `["conda", "run", "-n", "lint_env", "python", "-m", "isort"]` |
| isort.interpreter      | `[]`                               | Path to a python interpreter to use to run the linter server.                                                                                                                                                                                                            |
| isort.importStrategy   | `useBundled`                       | Setting to choose where to load `isort` from. `useBundled` picks isort bundled with the extension. `fromEnvironment` uses `isort` available in the environment.                                                                                                          |
| isort.showNotification | `off`                              | Setting to control when a notification is shown.                                                                                                                                                                                                                         |

## Commands

| Command        | Description                      |
| -------------- | -------------------------------- |
| isort: Restart | Force re-start the isort server. |
