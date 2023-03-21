############################################################################
# Original work Copyright 2017 Palantir Technologies, Inc.                 #
# Original work licensed under the MIT License.                            #
# See ThirdPartyNotices.txt in the project root for license information.   #
# All modifications Copyright (c) Open Law Library. All rights reserved.   #
#                                                                          #
# Licensed under the Apache License, Version 2.0 (the "License")           #
# you may not use this file except in compliance with the License.         #
# You may obtain a copy of the License at                                  #
#                                                                          #
#     http: // www.apache.org/licenses/LICENSE-2.0                         #
#                                                                          #
# Unless required by applicable law or agreed to in writing, software      #
# distributed under the License is distributed on an "AS IS" BASIS,        #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. #
# See the License for the specific language governing permissions and      #
# limitations under the License.                                           #
############################################################################
"""This module contains Language Server Protocol types
https://microsoft.github.io/language-server-protocol/specification

-- General Messages --

Class attributes are named with camel case notation because client is expecting
that.
"""
from functools import reduce
from typing import Any, List, Optional, Union

from pygls.lsp.types.basic_structures import (Model, NumType, RegularExpressionsClientCapabilities,
                                              Trace, WorkDoneProgressParams,
                                              WorkspaceEditClientCapabilities)
from pygls.lsp.types.diagnostics import PublishDiagnosticsClientCapabilities
from pygls.lsp.types.file_operations import FileOperationRegistrationOptions
from pygls.lsp.types.language_features import (CallHierarchyClientCapabilities,
                                               CallHierarchyOptions,
                                               CallHierarchyRegistrationOptions,
                                               CodeActionClientCapabilities, CodeActionOptions,
                                               CodeLensClientCapabilities, CodeLensOptions,
                                               CodeLensWorkspaceClientCapabilities,
                                               CompletionClientCapabilities, CompletionOptions,
                                               DeclarationClientCapabilities, DeclarationOptions,
                                               DeclarationRegistrationOptions,
                                               DefinitionClientCapabilities, DefinitionOptions,
                                               DocumentColorClientCapabilities,
                                               DocumentColorOptions,
                                               DocumentColorRegistrationOptions,
                                               DocumentFormattingClientCapabilities,
                                               DocumentFormattingOptions,
                                               DocumentHighlightClientCapabilities,
                                               DocumentHighlightOptions,
                                               DocumentLinkClientCapabilities, DocumentLinkOptions,
                                               DocumentOnTypeFormattingClientCapabilities,
                                               DocumentOnTypeFormattingOptions,
                                               DocumentRangeFormattingClientCapabilities,
                                               DocumentRangeFormattingOptions,
                                               DocumentSymbolClientCapabilities,
                                               DocumentSymbolOptions,
                                               FoldingRangeClientCapabilities, FoldingRangeOptions,
                                               FoldingRangeRegistrationOptions,
                                               HoverClientCapabilities, HoverOptions,
                                               ImplementationClientCapabilities,
                                               ImplementationOptions,
                                               ImplementationRegistrationOptions,
                                               LinkedEditingRangeClientCapabilities,
                                               LinkedEditingRangeOptions,
                                               LinkedEditingRangeRegistrationOptions,
                                               MonikerClientCapabilities, MonikerOptions,
                                               MonikerRegistrationOptions,
                                               ReferenceClientCapabilities, ReferenceOptions,
                                               RenameClientCapabilities, RenameOptions,
                                               SelectionRangeClientCapabilities,
                                               SelectionRangeOptions,
                                               SelectionRangeRegistrationOptions,
                                               SemanticTokensClientCapabilities,
                                               SemanticTokensOptions,
                                               SemanticTokensRegistrationOptions,
                                               SemanticTokensWorkspaceClientCapabilities,
                                               SignatureHelpClientCapabilities,
                                               SignatureHelpOptions,
                                               TypeDefinitionClientCapabilities,
                                               TypeDefinitionOptions,
                                               TypeDefinitionRegistrationOptions)
from pygls.lsp.types.text_synchronization import TextDocumentSyncKind
from pygls.lsp.types.window import (ShowDocumentClientCapabilities,
                                    ShowMessageRequestClientCapabilities)
from pygls.lsp.types.workspace import (DidChangeConfigurationClientCapabilities,
                                       DidChangeWatchedFilesClientCapabilities,
                                       ExecuteCommandClientCapabilities, ExecuteCommandOptions,
                                       SaveOptions, TextDocumentSyncClientCapabilities,
                                       WorkspaceFolder, WorkspaceFoldersServerCapabilities,
                                       WorkspaceSymbolClientCapabilities)


class ClientInfo(Model):
    name: str
    version: Optional[str]


class ServerInfo(Model):
    name: str
    version: Optional[str]


class TextDocumentClientCapabilities(Model):
    synchronization: Optional[TextDocumentSyncClientCapabilities]
    completion: Optional[CompletionClientCapabilities]
    hover: Optional[HoverClientCapabilities]
    signature_help: Optional[SignatureHelpClientCapabilities]
    declaration: Optional[DeclarationClientCapabilities]
    definition: Optional[DefinitionClientCapabilities]
    type_definition: Optional[TypeDefinitionClientCapabilities]
    implementation: Optional[ImplementationClientCapabilities]
    references: Optional[ReferenceClientCapabilities]
    document_highlight: Optional[DocumentHighlightClientCapabilities]
    document_symbol: Optional[DocumentSymbolClientCapabilities]
    code_action: Optional[CodeActionClientCapabilities]
    code_lens: Optional[CodeLensClientCapabilities]
    document_link: Optional[DocumentLinkClientCapabilities]
    color_provider: Optional[DocumentColorClientCapabilities]
    formatting: Optional[DocumentFormattingClientCapabilities]
    range_formatting: Optional[DocumentRangeFormattingClientCapabilities]
    on_type_formatting: Optional[DocumentOnTypeFormattingClientCapabilities]
    rename: Optional[RenameClientCapabilities]
    publish_diagnostics: Optional[PublishDiagnosticsClientCapabilities]
    folding_range: Optional[FoldingRangeClientCapabilities]
    selection_range: Optional[SelectionRangeClientCapabilities]
    linked_editing_range: Optional[LinkedEditingRangeClientCapabilities]
    call_hierarchy: Optional[CallHierarchyClientCapabilities]
    semantic_tokens: Optional[SemanticTokensClientCapabilities]
    moniker: Optional[MonikerClientCapabilities]


class FileOperationsClientCapabilities(Model):
    dynamic_registration: Optional[bool]
    did_create: Optional[bool]
    will_create: Optional[bool]
    did_rename: Optional[bool]
    will_rename: Optional[bool]
    did_delete: Optional[bool]
    will_delete: Optional[bool]


class WorkspaceClientCapabilities(Model):
    apply_edit: Optional[bool]
    workspace_edit: Optional[WorkspaceEditClientCapabilities]
    did_change_configuration: Optional[DidChangeConfigurationClientCapabilities]
    did_change_watched_files: Optional[DidChangeWatchedFilesClientCapabilities]
    symbol: Optional[WorkspaceSymbolClientCapabilities]
    execute_command: Optional[ExecuteCommandClientCapabilities]
    workspace_folders: Optional[bool]
    configuration: Optional[bool]
    semantic_tokens: Optional[SemanticTokensWorkspaceClientCapabilities]
    code_lens: Optional[CodeLensWorkspaceClientCapabilities]
    file_operations: Optional[FileOperationsClientCapabilities]


class WindowClientCapabilities(Model):
    work_done_progress: Optional[bool]
    show_message: Optional[ShowMessageRequestClientCapabilities]
    show_document: Optional[ShowDocumentClientCapabilities]


class MarkdownClientCapabilities(Model):
    parser: str
    version: Optional[str]


class GeneralClientCapabilities(Model):
    regular_expressions: Optional[RegularExpressionsClientCapabilities]
    markdown: Optional[MarkdownClientCapabilities]


class TextDocumentSyncOptionsServerCapabilities(Model):
    open_close: Optional[bool]
    change: Optional[TextDocumentSyncKind]
    will_save: Optional[bool]
    will_save_wait_until: Optional[bool]
    save: Optional[Union[bool, SaveOptions]]


class WorkspaceFileOperationsServerCapabilities(Model):
    did_create: Optional[FileOperationRegistrationOptions]
    will_create: Optional[FileOperationRegistrationOptions]
    did_rename: Optional[FileOperationRegistrationOptions]
    will_rename: Optional[FileOperationRegistrationOptions]
    did_delete: Optional[FileOperationRegistrationOptions]
    will_delete: Optional[FileOperationRegistrationOptions]


class WorkspaceServerCapabilities(Model):
    workspace_folders: Optional[WorkspaceFoldersServerCapabilities]
    file_operations: Optional[WorkspaceFileOperationsServerCapabilities]


class ClientCapabilities(Model):
    workspace: Optional[WorkspaceClientCapabilities]
    text_document: Optional[TextDocumentClientCapabilities]
    window: Optional[WindowClientCapabilities]
    general: Optional[GeneralClientCapabilities]
    experimental: Optional[Any]

    def get_capability(self, field: str, default: Any = None) -> Any:
        """Check if ClientCapabilities has some nested value without raising
        AttributeError.

        e.g. get_capability('text_document.synchronization.will_save')
        """
        try:
            value = reduce(getattr, field.split("."), self)
        except AttributeError:
            return default

        # If we reach the desired leaf value but it's None, return the default.
        value = default if value is None else value
        return value


class InitializeParams(WorkDoneProgressParams):
    process_id: Optional[int]
    root_uri: Optional[str]
    capabilities: ClientCapabilities
    client_info: Optional[ClientInfo]
    locale: Optional[str]
    root_path: Optional[str]
    initialization_options: Optional[Any]
    trace: Optional[Trace]
    workspace_folders: Optional[List[WorkspaceFolder]]


class ServerCapabilities(Model):
    text_document_sync: Optional[Union[TextDocumentSyncOptionsServerCapabilities, NumType]]
    completion_provider: Optional[CompletionOptions]
    hover_provider: Optional[Union[bool, HoverOptions]]
    signature_help_provider: Optional[SignatureHelpOptions]
    declaration_provider: Optional[Union[bool, DeclarationOptions,
                                         DeclarationRegistrationOptions]]
    definition_provider: Optional[Union[bool, DefinitionOptions]]
    type_definition_provider: Optional[Union[bool, TypeDefinitionOptions,
                                             TypeDefinitionRegistrationOptions]]
    implementation_provider: Optional[Union[bool, ImplementationOptions,
                                            ImplementationRegistrationOptions]]
    references_provider: Optional[Union[bool, ReferenceOptions]]
    document_highlight_provider: Optional[Union[bool, DocumentHighlightOptions]]
    document_symbol_provider: Optional[Union[bool, DocumentSymbolOptions]]
    code_action_provider: Optional[Union[bool, CodeActionOptions]]
    code_lens_provider: Optional[CodeLensOptions]
    document_link_provider: Optional[DocumentLinkOptions]
    color_provider: Optional[Union[bool, DocumentColorOptions,
                                   DocumentColorRegistrationOptions]]
    document_formatting_provider: Optional[Union[bool, DocumentFormattingOptions]]
    document_range_formatting_provider: Optional[Union[bool,
                                                       DocumentRangeFormattingOptions]]
    document_on_type_formatting_provider: Optional[DocumentOnTypeFormattingOptions]
    rename_provider: Optional[Union[bool, RenameOptions]]
    folding_range_provider: Optional[Union[bool, FoldingRangeOptions,
                                           FoldingRangeRegistrationOptions]]
    execute_command_provider: Optional[ExecuteCommandOptions]
    selection_range_provider: Optional[Union[bool, SelectionRangeOptions,
                                             SelectionRangeRegistrationOptions]]
    linked_editing_range_provider: Optional[Union[bool, LinkedEditingRangeOptions,
                                                  LinkedEditingRangeRegistrationOptions]]
    call_hierarchy_provider: Optional[Union[bool, CallHierarchyOptions,
                                            CallHierarchyRegistrationOptions]]
    semantic_tokens_provider: Optional[Union[SemanticTokensOptions,
                                             SemanticTokensRegistrationOptions]]
    moniker_provider: Optional[Union[bool, MonikerOptions,
                                     MonikerRegistrationOptions]]
    workspace_symbol_provider: Optional[bool]
    workspace: Optional[WorkspaceServerCapabilities]
    experimental: Optional[Any]


class InitializeResult(Model):
    capabilities: ServerCapabilities
    server_info: Optional[ServerInfo]


class InitializedParams(Model):
    pass
