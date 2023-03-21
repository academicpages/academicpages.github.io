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

-- Language Features - Semantic Tokens --

Class attributes are named with camel case notation because client is expecting
that.
"""
import enum
from typing import Dict, List, Optional, Union

from pygls.lsp.types.basic_structures import (Model, PartialResultParams, Range,
                                              StaticRegistrationOptions, TextDocumentIdentifier,
                                              TextDocumentRegistrationOptions,
                                              WorkDoneProgressOptions, WorkDoneProgressParams)


class SemanticTokensWorkspaceClientCapabilities(Model):
    refresh_support: Optional[bool]


class SemanticTokenTypes(str, enum.Enum):
    Namespace = 'namespace'
    Type = 'type'
    Class = 'class'
    Enum = 'enum'
    Interface = 'interface'
    Struct = 'struct'
    TypeParameter = 'typeParameter'
    Parameter = 'parameter'
    Variable = 'variable'
    Property = 'property'
    EnumMember = 'enumMember'
    Event = 'event'
    Function = 'function'
    Method = 'method'
    Macro = 'macro'
    Keyword = 'keyword'
    Modifier = 'modifier'
    Comment = 'comment'
    String = 'string'
    Number = 'number'
    Regexp = 'regexp'
    Operator = 'operator'


class SemanticTokenModifiers(str, enum.Enum):
    Declaration = 'declaration'
    Definition = 'definition'
    Readonly = 'readonly'
    Static = 'static'
    Deprecated = 'deprecated'
    Abstract = 'abstract'
    Async = 'async'
    Modification = 'modification'
    Documentation = 'documentation'
    DefaultLibrary = 'defaultLibrary'


class TokenFormat(str, enum.Enum):
    Relative = 'relative'


class SemanticTokensLegend(Model):
    token_types: List[str]
    token_modifiers: List[str]


class SemanticTokensRequestsFull(Model):
    delta: Optional[bool]


class SemanticTokensRequests(Model):
    range: Optional[Union[bool, Dict]]
    full: Optional[Union[bool, SemanticTokensRequestsFull]]


class SemanticTokensClientCapabilities(Model):
    requests: SemanticTokensRequests
    token_types: List[str]
    token_modifiers: List[str]
    formats: List[TokenFormat]
    overlapping_token_support: Optional[bool]
    multiline_token_support: Optional[bool]
    dynamic_registration: Optional[bool]


class SemanticTokensOptions(WorkDoneProgressOptions):
    legend: SemanticTokensLegend
    range: Optional[Union[bool, Dict]]
    full: Optional[Union[bool, SemanticTokensRequestsFull]]


class SemanticTokensRegistrationOptions(TextDocumentRegistrationOptions, SemanticTokensOptions, StaticRegistrationOptions):
    pass


class SemanticTokensParams(WorkDoneProgressParams, PartialResultParams):
    text_document: TextDocumentIdentifier


class SemanticTokens(Model):
    data: List[int]
    result_id: Optional[str]


class SemanticTokensPartialResult(Model):
    data: List[int]


class SemanticTokensDeltaParams(WorkDoneProgressParams, PartialResultParams):
    text_document: TextDocumentIdentifier
    previous_result_id: str


class SemanticTokensEdit(Model):
    start: int
    delete_count: int
    data: Optional[List[int]]


class SemanticTokensDelta(Model):
    edits: List[SemanticTokensEdit]
    result_id: Optional[str]


class SemanticTokensDeltaPartialResult(Model):
    edits: List[SemanticTokensEdit]


class SemanticTokensRangeParams(WorkDoneProgressParams, PartialResultParams):
    text_document: TextDocumentIdentifier
    range: Range
