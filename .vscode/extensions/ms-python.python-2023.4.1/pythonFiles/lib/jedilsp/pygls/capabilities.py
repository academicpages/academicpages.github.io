############################################################################
# Copyright(c) Open Law Library. All rights reserved.                      #
# See ThirdPartyNotices.txt in the project root for additional notices.    #
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
from functools import reduce
from typing import Any

from lsprotocol.types import (
    TEXT_DOCUMENT_CODE_ACTION, TEXT_DOCUMENT_CODE_LENS,
    TEXT_DOCUMENT_COMPLETION, TEXT_DOCUMENT_DECLARATION,
    TEXT_DOCUMENT_DEFINITION, TEXT_DOCUMENT_DOCUMENT_COLOR,
    TEXT_DOCUMENT_DOCUMENT_HIGHLIGHT, TEXT_DOCUMENT_DOCUMENT_LINK,
    TEXT_DOCUMENT_DOCUMENT_SYMBOL, TEXT_DOCUMENT_FOLDING_RANGE,
    TEXT_DOCUMENT_FORMATTING, TEXT_DOCUMENT_HOVER,
    TEXT_DOCUMENT_IMPLEMENTATION, TEXT_DOCUMENT_ON_TYPE_FORMATTING,
    TEXT_DOCUMENT_RANGE_FORMATTING, TEXT_DOCUMENT_REFERENCES,
    TEXT_DOCUMENT_RENAME, TEXT_DOCUMENT_SELECTION_RANGE,
    TEXT_DOCUMENT_SIGNATURE_HELP, TEXT_DOCUMENT_PREPARE_CALL_HIERARCHY,
    TEXT_DOCUMENT_DID_CLOSE, TEXT_DOCUMENT_DID_OPEN,
    TEXT_DOCUMENT_DID_SAVE, TEXT_DOCUMENT_LINKED_EDITING_RANGE,
    TEXT_DOCUMENT_MONIKER, TEXT_DOCUMENT_SEMANTIC_TOKENS_FULL,
    TEXT_DOCUMENT_SEMANTIC_TOKENS_FULL_DELTA, TEXT_DOCUMENT_SEMANTIC_TOKENS_RANGE,
    TEXT_DOCUMENT_WILL_SAVE, TEXT_DOCUMENT_WILL_SAVE_WAIT_UNTIL,
    TEXT_DOCUMENT_TYPE_DEFINITION, WORKSPACE_DID_CREATE_FILES,
    WORKSPACE_DID_DELETE_FILES, WORKSPACE_DID_RENAME_FILES,
    WORKSPACE_SYMBOL, WORKSPACE_WILL_CREATE_FILES,
    WORKSPACE_WILL_DELETE_FILES, WORKSPACE_WILL_RENAME_FILES
)
from lsprotocol.types import (
    ClientCapabilities, CodeLensOptions, CompletionOptions,
    DocumentLinkOptions, ExecuteCommandOptions, ImplementationOptions,
    SaveOptions, SemanticTokensOptions, SemanticTokensRegistrationOptions,
    SemanticTokensOptionsFullType1, ServerCapabilities,
    ServerCapabilitiesWorkspaceType, SignatureHelpOptions,
    TextDocumentSyncOptions, TypeDefinitionOptions,
    FileOperationOptions, WorkspaceFoldersServerCapabilities
)


def get_capability(
    client_capabilities: ClientCapabilities, field: str, default: Any = None
) -> Any:
    """Check if ClientCapabilities has some nested value without raising
    AttributeError.
    e.g. get_capability('text_document.synchronization.will_save')
    """
    try:
        value = reduce(getattr, field.split("."), client_capabilities)
    except AttributeError:
        return default

    # If we reach the desired leaf value but it's None, return the default.
    return default if value is None else value


class ServerCapabilitiesBuilder:
    """Create `ServerCapabilities` instance depending on builtin and user registered
    features.
    """
    def __init__(
        self,
        client_capabilities,
        features,
        feature_options,
        commands,
        sync_kind
    ):
        self.client_capabilities = client_capabilities
        self.features = features
        self.feature_options = feature_options
        self.commands = commands
        self.sync_kind = sync_kind

        self.server_cap = ServerCapabilities()

    def _provider_options(self, feature, default=True):
        if feature in self.features:
            return self.feature_options.get(feature, default)
        return None

    def _with_text_doc_sync(self):
        open_close = (
            TEXT_DOCUMENT_DID_OPEN in self.features
            or TEXT_DOCUMENT_DID_CLOSE in self.features
        )
        will_save = (
            get_capability(
                self.client_capabilities,
                'text_document.synchronization.will_save'
            )
            and TEXT_DOCUMENT_WILL_SAVE in self.features
        )
        will_save_wait_until = (
            get_capability(
                self.client_capabilities,
                'text_document.synchronization.will_save_wait_until'
            )
            and TEXT_DOCUMENT_WILL_SAVE_WAIT_UNTIL in self.features
        )
        if TEXT_DOCUMENT_DID_SAVE in self.features:
            if TEXT_DOCUMENT_DID_SAVE in self.feature_options:
                include_text = self.feature_options[TEXT_DOCUMENT_DID_SAVE].include_text
                save = SaveOptions(include_text=include_text)
            else:
                save = True
        else:
            save = False

        self.server_cap.text_document_sync = TextDocumentSyncOptions(
            open_close=open_close,
            change=self.sync_kind,
            will_save=will_save,
            will_save_wait_until=will_save_wait_until,
            save=save,
        )

        return self

    def _with_completion(self):
        value = self._provider_options(TEXT_DOCUMENT_COMPLETION, default=CompletionOptions())
        if value is not None:
            self.server_cap.completion_provider = value
        return self

    def _with_hover(self):
        value = self._provider_options(TEXT_DOCUMENT_HOVER)
        if value is not None:
            self.server_cap.hover_provider = value
        return self

    def _with_signature_help(self):
        value = self._provider_options(
            TEXT_DOCUMENT_SIGNATURE_HELP, default=SignatureHelpOptions()
        )
        if value is not None:
            self.server_cap.signature_help_provider = value
        return self

    def _with_declaration(self):
        value = self._provider_options(TEXT_DOCUMENT_DECLARATION)
        if value is not None:
            self.server_cap.declaration_provider = value
        return self

    def _with_definition(self):
        value = self._provider_options(TEXT_DOCUMENT_DEFINITION)
        if value is not None:
            self.server_cap.definition_provider = value
        return self

    def _with_type_definition(self):
        value = self._provider_options(
            TEXT_DOCUMENT_TYPE_DEFINITION, default=TypeDefinitionOptions()
        )
        if value is not None:
            self.server_cap.type_definition_provider = value
        return self

    def _with_implementation(self):
        value = self._provider_options(
            TEXT_DOCUMENT_IMPLEMENTATION, default=ImplementationOptions()
        )
        if value is not None:
            self.server_cap.implementation_provider = value
        return self

    def _with_references(self):
        value = self._provider_options(TEXT_DOCUMENT_REFERENCES)
        if value is not None:
            self.server_cap.references_provider = value
        return self

    def _with_document_highlight(self):
        value = self._provider_options(TEXT_DOCUMENT_DOCUMENT_HIGHLIGHT)
        if value is not None:
            self.server_cap.document_highlight_provider = value
        return self

    def _with_document_symbol(self):
        value = self._provider_options(TEXT_DOCUMENT_DOCUMENT_SYMBOL)
        if value is not None:
            self.server_cap.document_symbol_provider = value
        return self

    def _with_code_action(self):
        value = self._provider_options(TEXT_DOCUMENT_CODE_ACTION)
        if value is not None:
            self.server_cap.code_action_provider = value
        return self

    def _with_code_lens(self):
        value = self._provider_options(TEXT_DOCUMENT_CODE_LENS, default=CodeLensOptions())
        if value is not None:
            self.server_cap.code_lens_provider = value
        return self

    def _with_document_link(self):
        value = self._provider_options(TEXT_DOCUMENT_DOCUMENT_LINK, default=DocumentLinkOptions())
        if value is not None:
            self.server_cap.document_link_provider = value
        return self

    def _with_color(self):
        value = self._provider_options(TEXT_DOCUMENT_DOCUMENT_COLOR)
        if value is not None:
            self.server_cap.color_provider = value
        return self

    def _with_document_formatting(self):
        value = self._provider_options(TEXT_DOCUMENT_FORMATTING)
        if value is not None:
            self.server_cap.document_formatting_provider = value
        return self

    def _with_document_range_formatting(self):
        value = self._provider_options(TEXT_DOCUMENT_RANGE_FORMATTING)
        if value is not None:
            self.server_cap.document_range_formatting_provider = value
        return self

    def _with_document_on_type_formatting(self):
        value = self._provider_options(TEXT_DOCUMENT_ON_TYPE_FORMATTING)
        if value is not None:
            self.server_cap.document_on_type_formatting_provider = value
        return self

    def _with_rename(self):
        value = self._provider_options(TEXT_DOCUMENT_RENAME)
        if value is not None:
            self.server_cap.rename_provider = value
        return self

    def _with_folding_range(self):
        value = self._provider_options(TEXT_DOCUMENT_FOLDING_RANGE)
        if value is not None:
            self.server_cap.folding_range_provider = value
        return self

    def _with_execute_command(self):
        self.server_cap.execute_command_provider = \
            ExecuteCommandOptions(commands=self.commands)
        return self

    def _with_selection_range(self):
        value = self._provider_options(TEXT_DOCUMENT_SELECTION_RANGE)
        if value is not None:
            self.server_cap.selection_range_provider = value
        return self

    def _with_call_hierarchy(self):
        value = self._provider_options(TEXT_DOCUMENT_PREPARE_CALL_HIERARCHY)
        if value is not None:
            self.server_cap.call_hierarchy_provider = value
        return self

    def _with_semantic_tokens(self):

        providers = [
            TEXT_DOCUMENT_SEMANTIC_TOKENS_FULL,
            TEXT_DOCUMENT_SEMANTIC_TOKENS_FULL_DELTA,
            TEXT_DOCUMENT_SEMANTIC_TOKENS_RANGE
        ]

        for provider in providers:
            value = self._provider_options(provider, None)
            if value:
                break

        if value is None:
            return self

        if isinstance(value, SemanticTokensRegistrationOptions):
            self.server_cap.semantic_tokens_provider = value
            return self

        if TEXT_DOCUMENT_SEMANTIC_TOKENS_FULL_DELTA in self.features:
            full_support = SemanticTokensOptionsFullType1(delta=True)
        else:
            full_support = TEXT_DOCUMENT_SEMANTIC_TOKENS_FULL in self.features

        options = SemanticTokensOptions(
            legend=value,
            full=full_support or None,
            range=TEXT_DOCUMENT_SEMANTIC_TOKENS_RANGE in self.features or None
        )

        if options.full or options.range:
            self.server_cap.semantic_tokens_provider = options

        return self

    def _with_linked_editing_range(self):
        value = self._provider_options(TEXT_DOCUMENT_LINKED_EDITING_RANGE)
        if value is not None:
            self.server_cap.linked_editing_range_provider = value
        return self

    def _with_moniker(self):
        value = self._provider_options(TEXT_DOCUMENT_MONIKER)
        if value is not None:
            self.server_cap.moniker_provider = value
        return self

    def _with_workspace_symbol(self):
        value = self._provider_options(WORKSPACE_SYMBOL)
        if value is not None:
            self.server_cap.workspace_symbol_provider = value
        return self

    def _with_workspace_capabilities(self):
        # File operations
        file_operations = FileOperationOptions()
        operations = [
            (WORKSPACE_WILL_CREATE_FILES, "will_create"),
            (WORKSPACE_DID_CREATE_FILES, "did_create"),
            (WORKSPACE_WILL_DELETE_FILES, "will_delete"),
            (WORKSPACE_DID_DELETE_FILES, "did_delete"),
            (WORKSPACE_WILL_RENAME_FILES, "will_rename"),
            (WORKSPACE_DID_RENAME_FILES, "did_rename"),
        ]

        for method_name, capability_name in operations:
            client_supports_method = get_capability(
                self.client_capabilities, f'workspace.file_operations.{capability_name}'
            )

            if client_supports_method:
                value = self._provider_options(method_name, None)
                setattr(file_operations, capability_name, value)

        self.server_cap.workspace = ServerCapabilitiesWorkspaceType(
            workspace_folders=WorkspaceFoldersServerCapabilities(
                supported=True,
                change_notifications=True,
            ),
            file_operations=file_operations,
        )
        return self

    def _build(self):
        return self.server_cap

    def build(self):
        return (
            self
            ._with_text_doc_sync()
            ._with_completion()
            ._with_hover()
            ._with_signature_help()
            ._with_declaration()
            ._with_definition()
            ._with_type_definition()
            ._with_implementation()
            ._with_references()
            ._with_document_highlight()
            ._with_document_symbol()
            ._with_code_action()
            ._with_code_lens()
            ._with_document_link()
            ._with_color()
            ._with_document_formatting()
            ._with_document_range_formatting()
            ._with_document_on_type_formatting()
            ._with_rename()
            ._with_folding_range()
            ._with_execute_command()
            ._with_selection_range()
            ._with_call_hierarchy()
            ._with_semantic_tokens()
            ._with_linked_editing_range()
            ._with_moniker()
            ._with_workspace_symbol()
            ._with_workspace_capabilities()
            ._build()
        )
