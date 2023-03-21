# jedi-language-server

[![image-version](https://img.shields.io/pypi/v/jedi-language-server.svg)](https://python.org/pypi/jedi-language-server)
[![image-license](https://img.shields.io/pypi/l/jedi-language-server.svg)](https://python.org/pypi/jedi-language-server)
[![image-python-versions](https://img.shields.io/badge/python->=3.7-blue)](https://python.org/pypi/jedi-language-server)
[![image-pypi-downloads](https://pepy.tech/badge/jedi-language-server)](https://pepy.tech/project/jedi-language-server)
[![github-action-testing](https://github.com/pappasam/jedi-language-server/actions/workflows/testing.yaml/badge.svg)](https://github.com/pappasam/jedi-language-server/actions/workflows/testing.yaml)

A [Language Server](https://microsoft.github.io/language-server-protocol/) for the latest version(s) of [Jedi](https://jedi.readthedocs.io/en/latest/). If using Neovim/Vim, we recommend using with [coc-jedi](https://github.com/pappasam/coc-jedi). Supports Python versions 3.7 and newer.

**Note:** this tool is actively used by its primary author. He's happy to review pull requests / respond to issues you may discover.

## Installation

Some frameworks, like coc-jedi and vscode-python, will install and manage jedi-language-server for you. If you're setting up manually, you can run the following from your command line (bash / zsh):

```bash
pip install -U jedi-language-server
```

Alternatively (and preferably), use [pipx](https://github.com/pipxproject/pipx) to keep jedi-language-server and its dependencies isolated from your other Python dependencies. Don't worry, jedi is smart enough to figure out which Virtual environment you're currently using!

## Capabilities

jedi-language-server aims to support Jedi's capabilities and expose them through the Language Server Protocol. It supports the following Language Server capabilities:

### Language Features

- [completionItem/resolve](https://microsoft.github.io/language-server-protocol/specification#completionItem_resolve)
- [textDocument/codeAction](https://microsoft.github.io/language-server-protocol/specification#textDocument_codeAction) (refactor.inline, refactor.extract)
- [textDocument/completion](https://microsoft.github.io/language-server-protocol/specifications/specification-current/#textDocument_completion)
- [textDocument/definition](https://microsoft.github.io/language-server-protocol/specifications/specification-current/#textDocument_definition)
- [textDocument/documentHighlight](https://microsoft.github.io/language-server-protocol/specification#textDocument_documentHighlight)
- [textDocument/documentSymbol](https://microsoft.github.io/language-server-protocol/specifications/specification-current/#textDocument_documentSymbol)
- [textDocument/typeDefinition](https://microsoft.github.io/language-server-protocol/specifications/specification-current/#textDocument_typeDefinition)
- [textDocument/hover](https://microsoft.github.io/language-server-protocol/specifications/specification-current/#textDocument_hover)
- [textDocument/publishDiagnostics](https://microsoft.github.io/language-server-protocol/specification#textDocument_publishDiagnostics)
- [textDocument/references](https://microsoft.github.io/language-server-protocol/specifications/specification-current/#textDocument_references)
- [textDocument/rename](https://microsoft.github.io/language-server-protocol/specifications/specification-current/#textDocument_rename)
- [textDocument/signatureHelp](https://microsoft.github.io/language-server-protocol/specification#textDocument_signatureHelp)
- [workspace/symbol](https://microsoft.github.io/language-server-protocol/specifications/specification-current/#workspace_symbol)

### Text Synchronization (for diagnostics)

- [textDocument/didChange](https://microsoft.github.io/language-server-protocol/specification#textDocument_didChange)
- [textDocument/didOpen](https://microsoft.github.io/language-server-protocol/specification#textDocument_didOpen)
- [textDocument/didSave](https://microsoft.github.io/language-server-protocol/specification#textDocument_didSave)

## Editor Setup

The following instructions show how to use jedi-language-server with your development tooling. The instructions assume you have already installed jedi-language-server.

### Vim / Neovim

Users may choose 1 of the following options:

- [coc.nvim](https://github.com/neoclide/coc.nvim) with [coc-jedi](https://github.com/pappasam/coc-jedi).
- [ALE](https://github.com/dense-analysis/ale).
- [Neovim's native LSP client](https://neovim.io/doc/user/lsp.html). See [here](https://github.com/neovim/nvim-lspconfig/blob/master/doc/server_configurations.md#jedi_language_server) for an example configuration.
- [vim-lsp](https://github.com/prabirshrestha/vim-lsp).

Note: this list is non-exhaustive. If you know of a great choice not included in this list, please submit a PR!

### Emacs

Users may choose one of the following options:

- [lsp-jedi](https://github.com/fredcamps/lsp-jedi).
- [eglot](https://github.com/joaotavora/eglot)

Note: this list is non-exhaustive. If you know of a great choice not included in this list, please submit a PR!

### Visual Studio Code (vscode)

Starting from the [October 2021 release](https://github.com/microsoft/vscode-python/releases/tag/2021.10.1317843341), set the `python.languageServer` setting to `Jedi` to use jedi-language-server.

Note: This does not support Python 2.7.

See: <https://github.com/pappasam/jedi-language-server/issues/50#issuecomment-781101169>

## Command line

jedi-language-server can be run directly from the command line.

```console
$ jedi-language-server --help
usage: jedi-language-server [-h] [--version] [--tcp] [--ws] [--host HOST] [--port PORT] [--log-file LOG_FILE] [-v]

Jedi language server: an LSP wrapper for jedi.

optional arguments:
  -h, --help           show this help message and exit
  --version            display version information and exit
  --tcp                use TCP web server instead of stdio
  --ws                 use web socket server instead of stdio
  --host HOST          host for web server (default 127.0.0.1)
  --port PORT          port for web server (default 2087)
  --log-file LOG_FILE  redirect logs to file specified
  -v, --verbose        increase verbosity of log output

Examples:

    Run over stdio     : jedi-language-server
    Run over tcp       : jedi-language-server --tcp
    Run over websockets:
        # only need to pip install once per env
        pip install pygls[ws]
        jedi-language-server --ws

Notes:

    For use with web sockets, user must first run
    'pip install pygls[ws]' to install the correct
    version of the websockets library.
```

If testing sending requests over stdio manually from the command line, you must include Windows-style line endings: `\r\n` . For an example, from within this project, run the following:

```console
$ jedi-language-server < ./example-initialization-request.txt
INFO:pygls.server:Starting IO server
INFO:pygls.feature_manager:Registered "textDocument/didOpen" with options "None"
INFO:pygls.feature_manager:Registered "textDocument/didChange" with options "None"
INFO:pygls.feature_manager:Registered "textDocument/didSave" with options "None"
INFO:pygls.feature_manager:Registered "textDocument/hover" with options "None"
INFO:pygls.protocol:Language server initialized work_done_token=None process_id=None root_uri='file:///home/ubuntu/artifacts/' capabilities=ClientCapabilities(workspace=WorkspaceClientCapabilities(apply_edit=None, workspace_edit=None, did_change_configuration=DidChangeConfigurationClientCapabilities(dynamic_registration=True), did_change_watched_files=None, symbol=None, execute_command=None, workspace_folders=None, configuration=None, semantic_tokens=None, code_lens=None, file_operations=None), text_document=TextDocumentClientCapabilities(synchronization=TextDocumentSyncClientCapabilities(dynamic_registration=True, will_save=False, will_save_wait_until=False, did_save=False), completion=CompletionClientCapabilities(dynamic_registration=True, completion_item=CompletionItemClientCapabilities(snippet_support=False, commit_characters_support=True, documentation_format=[<MarkupKind.PlainText: 'plaintext'>, <MarkupKind.Markdown: 'markdown'>], deprecated_support=False, preselect_support=False, tag_support=None, insert_replace_support=None, resolve_support=None, insert_text_mode_support=None), completion_item_kind=None, context_support=False), hover=HoverClientCapabilities(dynamic_registration=True, content_format=[<MarkupKind.PlainText: 'plaintext'>, <MarkupKind.Markdown: 'markdown'>]), signature_help=SignatureHelpClientCapabilities(dynamic_registration=True, signature_information=SignatureHelpInformationClientCapabilities(documentation_format=[<MarkupKind.PlainText: 'plaintext'>, <MarkupKind.Markdown: 'markdown'>], parameter_information=None, active_parameter_support=None), context_support=None), declaration=DeclarationClientCapabilities(dynamic_registration=True, link_support=True), definition=DefinitionClientCapabilities(dynamic_registration=True, link_support=True), type_definition=TypeDefinitionClientCapabilities(dynamic_registration=True, link_support=True), implementation=ImplementationClientCapabilities(dynamic_registration=True, link_support=True), references=None, document_highlight=None, document_symbol=None, code_action=None, code_lens=None, document_link=None, color_provider=None, formatting=None, range_formatting=None, on_type_formatting=None, rename=None, publish_diagnostics=None, folding_range=None, selection_range=None, linked_editing_range=None, call_hierarchy=None, semantic_tokens=None, moniker=None), window=None, general=None, experimental=None) client_info=None locale=None root_path=None initialization_options=None trace=None workspace_folders=None
INFO:pygls.protocol:Sending data: {"jsonrpc": "2.0", "id": 0, "result": {"capabilities": {"textDocumentSync": {"openClose": true, "change": 2, "willSave": false, "willSaveWaitUntil": false, "save": true}, "completionProvider": {"triggerCharacters": [".", "'", "\""], "resolveProvider": true}, "hoverProvider": true, "signatureHelpProvider": {"triggerCharacters": ["(", ","]}, "definitionProvider": true, "referencesProvider": true, "documentHighlightProvider": true, "documentSymbolProvider": true, "codeActionProvider": {"codeActionKinds": ["refactor.inline", "refactor.extract"]}, "renameProvider": true, "executeCommandProvider": {"commands": []}, "workspaceSymbolProvider": true, "workspace": {"workspaceFolders": {"supported": true, "changeNotifications": true}, "fileOperations": {}}}}}
Content-Length: 758
Content-Type: application/vscode-jsonrpc; charset=utf-8

{"jsonrpc": "2.0", "id": 0, "result": {"capabilities": {"textDocumentSync": {"openClose": true, "change": 2, "willSave": false, "willSaveWaitUntil": false, "save": true}, "completionProvider": {"triggerCharacters": [".", "'", "\""], "resolveProvider": true}, "hoverProvider": true, "signatureHelpProvider": {"triggerCharacters": ["(", ","]}, "definitionProvider": true, "referencesProvider": true, "documentHighlightProvider": true, "documentSymbolProvider": true, "codeActionProvider": {"codeActionKinds": ["refactor.inline", "refactor.extract"]}, "renameProvider": true, "executeCommandProvider": {"commands": []}, "workspaceSymbolProvider": true, "workspace": {"workspaceFolders": {"supported": true, "changeNotifications": true}, "fileOperations": {}}}}}INFO:pygls.server:Shutting down the server
INFO:pygls.server:Closing the event loop.
```

If testing interactively, be sure to manually insert carriage returns. Although this may differ between shell environments, within most bash terminals, you can explicitly insert the required line endings by typing `<C-v><C-m>`, which will insert a `^M`. See:

```console
$ jedi-language-server 2>logs
Content-Length: 1062^M
^M
{"jsonrpc":"2.0","id":0,"method":"initialize","params":{"capabilities":{"textDocument":{"hover":{"dynamicRegistration":true,"contentFormat":["plaintext","markdown"]},"synchronization":{"dynamicRegistration":true,"willSave":false,"didSave":false,"willSaveWaitUntil":false},"completion":{"dynamicRegistration":true,"completionItem":{"snippetSupport":false,"commitCharactersSupport":true,"documentationFormat":["plaintext","markdown"],"deprecatedSupport":false,"preselectSupport":false},"contextSupport":false},"signatureHelp":{"dynamicRegistration":true,"signatureInformation":{"documentationFormat":["plaintext","markdown"]}},"declaration":{"dynamicRegistration":true,"linkSupport":true},"definition":{"dynamicRegistration":true,"linkSupport":true},"typeDefinition":{"dynamicRegistration":true,"linkSupport":true},"implementation":{"dynamicRegistration":true,"linkSupport":true}},"workspace":{"didChangeConfiguration":{"dynamicRegistration":true}}},"initializationOptions":null,"processId":null,"rootUri":"file:///home/ubuntu/artifacts/","workspaceFolders":null}}^M
Content-Length: 758
Content-Type: application/vscode-jsonrpc; charset=utf-8

{"jsonrpc": "2.0", "id": 0, "result": {"capabilities": {"textDocumentSync": {"openClose": true, "change": 2, "willSave": false, "willSaveWaitUntil": false, "save": true}, "completionProvider": {"triggerCharacters": [".", "'", "\""], "resolveProvider": true}, "hoverProvider": true, "signatureHelpProvider": {"triggerCharacters": ["(", ","]}, "definitionProvider": true, "referencesProvider": true, "documentHighlightProvider": true, "documentSymbolProvider": true, "codeActionProvider": {"codeActionKinds": ["refactor.inline", "refactor.extract"]}, "renameProvider": true, "executeCommandProvider": {"commands": []}, "workspaceSymbolProvider": true, "workspace": {"workspaceFolders": {"supported": true, "changeNotifications": true}, "fileOperations": {}}}}}
```

## Configuration

We recommend using [coc-jedi](https://github.com/pappasam/coc-jedi) and following its [configuration instructions](https://github.com/pappasam/coc-jedi#configuration).

If you are configuring manually, jedi-language-server supports the following [initializationOptions](https://microsoft.github.io/language-server-protocol/specification#initialize):

```json
{
  "initializationOptions": {
    "codeAction": {
      "nameExtractVariable": "jls_extract_var",
      "nameExtractFunction": "jls_extract_def"
    },
    "completion": {
      "disableSnippets": false,
      "resolveEagerly": false,
      "ignorePatterns": []
    },
    "diagnostics": {
      "enable": false,
      "didOpen": true,
      "didChange": true,
      "didSave": true
    },
    "hover": {
      "enable": true,
      "disable": {
        "class": { "all": false, "names": [], "fullNames": [] },
        "function": { "all": false, "names": [], "fullNames": [] },
        "instance": { "all": false, "names": [], "fullNames": [] },
        "keyword": { "all": false, "names": [], "fullNames": [] },
        "module": { "all": false, "names": [], "fullNames": [] },
        "param": { "all": false, "names": [], "fullNames": [] },
        "path": { "all": false, "names": [], "fullNames": [] },
        "property": { "all": false, "names": [], "fullNames": [] },
        "statement": { "all": false, "names": [], "fullNames": [] }
      }
    },
    "jediSettings": {
      "autoImportModules": [],
      "caseInsensitiveCompletion": true,
      "debug": false
    },
    "markupKindPreferred": "markdown",
    "workspace": {
      "extraPaths": [],
      "environmentPath": "/path/to/venv/bin/python",
      "symbols": {
        "ignoreFolders": [".nox", ".tox", ".venv", "__pycache__", "venv"],
        "maxSymbols": 20
      }
    }
  }
}
```

See coc-jedi's [configuration instructions](https://github.com/pappasam/coc-jedi#configuration) for an explanation of the above configurations.

## Diagnostics

Diagnostics are provided by Python's built-in `compile` function.

If you would like diagnostics (from [pylint](https://github.com/PyCQA/pylint), [mypy](https://github.com/python/mypy), etc.), we recommend using the powerful [diagnostic-language-server](https://github.com/iamcco/diagnostic-languageserver).

## Code Formatting

Again, we recommend that you use [diagnostic-language-server](https://github.com/iamcco/diagnostic-languageserver). It also supports code formatting.

## Local Development

To build and run this project from source:

### Dependencies

Install the following tools manually:

- [Poetry](https://github.com/sdispater/poetry#installation)
- [GNU Make](https://www.gnu.org/software/make/)

#### Recommended

- [asdf](https://github.com/asdf-vm/asdf)

### Get source code

[Fork](https://help.github.com/en/github/getting-started-with-github/fork-a-repo) this repository and clone the fork to your development machine:

```bash
git clone https://github.com/<YOUR-USERNAME>/jedi-language-server
cd jedi-language-server
```

### Set up development environment

```bash
make setup
```

### Run tests

```bash
make test
```

## Inspiration

Palantir's [python-language-server](https://github.com/palantir/python-language-server) inspired this project. In fact, for consistency's sake, many of python-language-server's CLI options are used as-is in jedi-language-server.

Unlike python-language-server, jedi-language-server:

- Uses [pygls](https://github.com/openlawlibrary/pygls) instead of creating its own low-level Language Server Protocol bindings
- Supports one powerful 3rd party static analysis / completion / refactoring library: Jedi. By only supporting Jedi, we can focus on supporting all Jedi features without exposing ourselves to too many broken 3rd party dependencies (I'm looking at you, [rope](https://github.com/python-rope/rope)).
- Is supremely simple because of its scope constraints. Leave complexity to the Jedi [master](https://github.com/davidhalter). If the force is strong with you, please submit a PR!

## Articles

- [Python in VS Code Improves Jedi Language Server Support](https://visualstudiomagazine.com/articles/2021/03/17/vscode-jedi.aspx)

## Written by

[Samuel Roeca](https://samroeca.com/)
